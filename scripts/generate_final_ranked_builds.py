import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTERACTION_PATH = ROOT / "data" / "meta" / "build_interaction_analysis.json"
DPS_PATH = ROOT / "data" / "meta" / "build_dps_estimates.json"
LEGALITY_PATH = ROOT / "data" / "meta" / "build_legality_analysis.json"
SURVIVABILITY_PATH = ROOT / "data" / "meta" / "build_survivability_estimates.json"
OUT_PATH = ROOT / "data" / "meta" / "final_ranked_builds.json"
REPORT_PATH = ROOT / "reports" / "final_build_guides.md"


RANKING_WEIGHTS = {
    "dps": 0.40,
    "interaction": 0.20,
    "legality": 0.20,
    "survivability": 0.20,
}

TODO_LEVELING_SECTION = {
    "status": "TODO",
    "title": "TODO leveling section",
    "notes": [
        "레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.",
        "향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.",
    ],
}

TODO_PASSIVE_PROGRESSION_SECTION = {
    "status": "TODO",
    "title": "TODO passive progression section",
    "notes": [
        "패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.",
        "향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.",
    ],
}

TODO_GEAR_PROGRESSION_SECTION = {
    "status": "TODO",
    "title": "TODO gear progression section",
    "notes": [
        "현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.",
        "향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.",
    ],
}


def load_json(path, default=None, *, required=False):
    if default is None:
        default = []

    if not path.exists():
        if required:
            raise FileNotFoundError(f"missing required file: {path}")
        print(f"[WARN] missing file: {path}")
        return default

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"저장 완료: {path}")


def save_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"저장 완료: {path}")


def normalize_key(value):
    return str(value or "").strip().lower()


def index_by_build_name(items):
    return {normalize_key(item.get("build_name")): item for item in items}


def merge_inputs(interaction_builds, dps_builds, legality_builds, survivability_builds):
    dps_index = index_by_build_name(dps_builds)
    legality_index = index_by_build_name(legality_builds)
    survivability_index = index_by_build_name(survivability_builds)
    merged = []

    for build in interaction_builds:
        key = normalize_key(build.get("build_name"))
        combined = dict(build)
        combined["dps_analysis"] = dps_index.get(key)
        combined["legality_analysis"] = legality_index.get(key)
        combined["survivability_analysis"] = survivability_index.get(key)
        merged.append(combined)

    return merged


def safe_float(value):
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def score_max(values):
    numeric = [value for value in values if value is not None and value > 0]
    return max(numeric) if numeric else None


def normalize_score(value, max_value):
    if value is None or max_value in (None, 0):
        return None
    return round(max(0.0, min(100.0, (value / max_value) * 100.0)), 3)


def collect_score_ranges(builds):
    return {
        "dps": score_max([safe_float((build.get("dps_analysis") or {}).get("estimated_dps_score")) for build in builds]),
        "interaction": score_max([safe_float(build.get("interaction_score")) for build in builds]),
        "legality": score_max([safe_float((build.get("legality_analysis") or {}).get("legality_score")) for build in builds]),
        "survivability": score_max([safe_float((build.get("survivability_analysis") or {}).get("survivability_score")) for build in builds]),
    }


def weighted_rank_score(component_scores):
    weighted_sum = 0.0
    used_weight = 0.0
    used_components = {}
    missing_components = []

    for component, weight in RANKING_WEIGHTS.items():
        score = component_scores.get(component)
        if score is None:
            missing_components.append(component)
            continue
        weighted_sum += score * weight
        used_weight += weight
        used_components[component] = {
            "normalized_score": score,
            "configured_weight": weight,
        }

    if used_weight <= 0:
        return 0.0, used_components, missing_components

    return round(weighted_sum / used_weight, 3), used_components, missing_components


def unique_preserve_order(values):
    seen = set()
    result = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def collect_core_mechanics(build):
    mechanics = []
    for source in [build, build.get("dps_analysis") or {}, build.get("legality_analysis") or {}, build.get("survivability_analysis") or {}]:
        mechanics.extend(source.get("mechanics", []))

    for combo in build.get("broken_combos", []):
        name = combo.get("name")
        if name:
            mechanics.append(name)

    return unique_preserve_order([m for m in mechanics if m])


def build_strength_reasons(build):
    reasons = []

    for combo in build.get("broken_combos", []):
        ko = combo.get("ko")
        reason = combo.get("reason")
        if ko and reason:
            reasons.append(f"{ko}: {reason}")

    dps = build.get("dps_analysis") or {}
    for reason in dps.get("why", [])[:8]:
        reasons.append(reason)

    survivability = build.get("survivability_analysis") or {}
    if survivability.get("survivability_score") is not None:
        reasons.append(
            f"생존력 MVP 점수 {survivability.get('survivability_score')}로 DPS 외 안정성 축도 함께 비교됨"
        )

    legality = build.get("legality_analysis") or {}
    if legality.get("legality_score") is not None:
        reasons.append(
            f"legality_score {legality.get('legality_score')}를 반영해 실제 작동 가능성 리스크를 최종 점수에 포함함"
        )

    if not reasons:
        reasons.append("강점 설명 데이터가 부족합니다. TODO: interaction/DPS/survivability 분석 결과를 보강해야 합니다.")

    return unique_preserve_order(reasons)


def build_weaknesses(build, missing_components):
    weaknesses = []

    legality = build.get("legality_analysis") or {}
    for item in legality.get("warnings", [])[:6]:
        message = item.get("message")
        if message:
            weaknesses.append({"source": "legality", "message": message})

    for item in legality.get("missing_data", [])[:4]:
        message = item.get("message")
        if message:
            weaknesses.append({"source": "legality_missing_data", "message": message})

    survivability = build.get("survivability_analysis") or {}
    for item in survivability.get("weaknesses", [])[:6]:
        message = item.get("message")
        if message:
            weaknesses.append({"source": "survivability", "message": message})

    for item in survivability.get("missing_data", [])[:4]:
        message = item.get("message")
        if message:
            weaknesses.append({"source": "survivability_missing_data", "message": message})

    for component in missing_components:
        weaknesses.append({
            "source": "final_ranking_missing_component",
            "message": f"{component} score가 없어 남은 가중치만 정규화해 final_rank_score를 계산했습니다.",
        })

    return weaknesses


def simplify_uniques(uniques):
    simplified = []
    for unique in uniques:
        simplified.append({
            "name": unique.get("name", ""),
            "canonical_name": unique.get("canonical_name", ""),
            "base_type": unique.get("base_type", ""),
            "role": unique.get("role", ""),
            "score": unique.get("score", 0),
            "matched_tags": unique.get("matched_tags", []),
            "unique_tags": unique.get("unique_tags", []),
        })
    return simplified


def simplify_affixes(affixes):
    simplified = []
    for affix in affixes:
        simplified.append({
            "slot": affix.get("slot", ""),
            "name": affix.get("name", ""),
            "mechanics": affix.get("mechanics", []),
            "damage_types": affix.get("damage_types", []),
            "final_score": affix.get("final_score", 0),
            "power_level": affix.get("power_level", ""),
        })
    return simplified


def make_ranked_build(build, score_ranges):
    dps = build.get("dps_analysis") or {}
    legality = build.get("legality_analysis") or {}
    survivability = build.get("survivability_analysis") or {}

    raw_scores = {
        "dps": safe_float(dps.get("estimated_dps_score")),
        "interaction": safe_float(build.get("interaction_score")),
        "legality": safe_float(legality.get("legality_score")),
        "survivability": safe_float(survivability.get("survivability_score")),
    }
    component_scores = {
        component: normalize_score(value, score_ranges.get(component))
        for component, value in raw_scores.items()
    }
    final_rank_score, used_components, missing_components = weighted_rank_score(component_scores)

    weaknesses = build_weaknesses(build, missing_components)

    return {
        "build_name": build.get("build_name", ""),
        "main_skill": build.get("main_skill", ""),
        "archetype_label_ko": build.get("archetype_label_ko", ""),
        "final_rank_score": final_rank_score,
        "score_components": {
            "formula": "DPS 40% + interaction 20% + legality 20% + survivability 20%; missing scores are skipped and remaining weights are normalized.",
            "raw_scores": raw_scores,
            "normalized_scores": component_scores,
            "used_components": used_components,
            "missing_components": missing_components,
        },
        "estimated_dps_score": dps.get("estimated_dps_score"),
        "single_target_score": dps.get("single_target_score"),
        "mapping_score": dps.get("mapping_score"),
        "interaction_score": build.get("interaction_score"),
        "survivability_score": survivability.get("survivability_score"),
        "legality_score": legality.get("legality_score"),
        "recommended_supports": build.get("recommended_supports", []),
        "recommended_uniques": simplify_uniques(build.get("recommended_uniques", [])),
        "recommended_rare_affixes": simplify_affixes(build.get("recommended_rare_affixes", [])),
        "core_mechanics": collect_core_mechanics(build),
        "why_this_build_is_strong": build_strength_reasons(build),
        "weaknesses": weaknesses,
        "todo_leveling_section": TODO_LEVELING_SECTION,
        "todo_passive_progression_section": TODO_PASSIVE_PROGRESSION_SECTION,
        "todo_gear_progression_section": TODO_GEAR_PROGRESSION_SECTION,
    }


def rank_builds(builds):
    score_ranges = collect_score_ranges(builds)
    ranked = [make_ranked_build(build, score_ranges) for build in builds]
    ranked.sort(key=lambda item: item["final_rank_score"], reverse=True)

    for index, item in enumerate(ranked, start=1):
        item["rank"] = index

    return ranked


def fmt_list(items, limit=8):
    if not items:
        return "- 없음"
    lines = []
    for item in items[:limit]:
        if isinstance(item, dict):
            if "message" in item:
                source = item.get("source")
                prefix = f"[{source}] " if source else ""
                lines.append(f"- {prefix}{item['message']}")
            elif "name" in item:
                extra = item.get("role") or item.get("slot") or ""
                extra_text = f" / {extra}" if extra else ""
                lines.append(f"- {item['name']}{extra_text}")
            else:
                lines.append(f"- {json.dumps(item, ensure_ascii=False)}")
        else:
            lines.append(f"- {item}")
    if len(items) > limit:
        lines.append(f"- ... 외 {len(items) - limit}개")
    return "\n".join(lines)


def generate_report(ranked_builds):
    lines = [
        "# Final Build Guides",
        "",
        "> 이 문서는 interaction, DPS, legality, survivability MVP 산출물을 결합한 최종 랭킹 초안입니다.",
        "> leveling/passive/gear progression은 실제 데이터가 아직 없으므로 TODO 섹션으로 명확히 표시합니다.",
        "",
        "## 입력 / 출력",
        "",
        f"- 입력: `{INTERACTION_PATH.relative_to(ROOT)}`",
        f"- 입력: `{DPS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{LEGALITY_PATH.relative_to(ROOT)}`",
        f"- 입력: `{SURVIVABILITY_PATH.relative_to(ROOT)}`",
        f"- JSON 출력: `{OUT_PATH.relative_to(ROOT)}`",
        f"- 리포트 출력: `{REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## Ranking Formula",
        "",
        "- DPS: 40%",
        "- Interaction: 20%",
        "- Legality: 20%",
        "- Survivability: 20%",
        "- 누락된 점수는 제외하고 남은 가중치만 안전하게 정규화합니다.",
        "",
        "## Summary",
        "",
        f"- ranked builds: {len(ranked_builds)}",
    ]

    if ranked_builds:
        top = ranked_builds[0]
        lines.append(f"- top build: {top['build_name']} / final_rank_score {top['final_rank_score']}")

    lines.extend(["", "## Ranked Build Guides", ""])

    for build in ranked_builds[:25]:
        lines.extend([
            f"### Rank {build['rank']}. {build['build_name']}",
            "",
            f"- 메인 스킬: {build['main_skill']}",
            f"- 아키타입: {build['archetype_label_ko']}",
            f"- final_rank_score: {build['final_rank_score']}",
            f"- estimated_dps_score: {build['estimated_dps_score']}",
            f"- single_target_score: {build['single_target_score']}",
            f"- mapping_score: {build['mapping_score']}",
            f"- interaction_score: {build['interaction_score']}",
            f"- survivability_score: {build['survivability_score']}",
            f"- legality_score: {build['legality_score']}",
            "",
            "#### 추천 보조젬",
            "",
            fmt_list(build["recommended_supports"]),
            "",
            "#### 추천 유니크",
            "",
            fmt_list(build["recommended_uniques"], limit=5),
            "",
            "#### 추천 희귀 Affix",
            "",
            fmt_list(build["recommended_rare_affixes"], limit=5),
            "",
            "#### Core Mechanics",
            "",
            fmt_list(build["core_mechanics"], limit=12),
            "",
            "#### 왜 강한가",
            "",
            fmt_list(build["why_this_build_is_strong"], limit=10),
            "",
            "#### 약점 / 검증 필요",
            "",
            fmt_list(build["weaknesses"], limit=10),
            "",
            "#### TODO Leveling Section",
            "",
            fmt_list(build["todo_leveling_section"]["notes"]),
            "",
            "#### TODO Passive Progression Section",
            "",
            fmt_list(build["todo_passive_progression_section"]["notes"]),
            "",
            "#### TODO Gear Progression Section",
            "",
            fmt_list(build["todo_gear_progression_section"]["notes"]),
            "",
        ])

    return "\n".join(lines).rstrip() + "\n"


def main():
    interaction_builds = load_json(INTERACTION_PATH, required=True)
    dps_builds = load_json(DPS_PATH, required=True)
    legality_builds = load_json(LEGALITY_PATH, required=True)
    survivability_builds = load_json(SURVIVABILITY_PATH, required=True)

    builds = merge_inputs(interaction_builds, dps_builds, legality_builds, survivability_builds)
    ranked_builds = rank_builds(builds)

    save_json(OUT_PATH, ranked_builds)
    save_text(REPORT_PATH, generate_report(ranked_builds))

    print(f"loaded interaction builds: {len(interaction_builds)}")
    print(f"loaded dps builds: {len(dps_builds)}")
    print(f"loaded legality builds: {len(legality_builds)}")
    print(f"loaded survivability builds: {len(survivability_builds)}")
    print(f"final ranked builds: {len(ranked_builds)}")

    for build in ranked_builds[:10]:
        print("=" * 80)
        print(f"#{build['rank']} {build['build_name']}")
        print(f"최종 점수: {build['final_rank_score']}")
        print(
            f"DPS: {build['estimated_dps_score']} / 생존: {build['survivability_score']} / "
            f"합법성: {build['legality_score']} / 상호작용: {build['interaction_score']}"
        )


if __name__ == "__main__":
    main()
