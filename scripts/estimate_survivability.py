import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTERACTION_PATH = ROOT / "data" / "meta" / "build_interaction_analysis.json"
DPS_PATH = ROOT / "data" / "meta" / "build_dps_estimates.json"
LEGALITY_PATH = ROOT / "data" / "meta" / "build_legality_analysis.json"
OUT_PATH = ROOT / "data" / "meta" / "build_survivability_estimates.json"
REPORT_PATH = ROOT / "reports" / "survivability_report.md"


# Heuristic-only relative survivability weights.
# These are not real PoE2 EHP, resistance, armour/evasion, block, or recovery values.
# Missing exact game data is recorded in missing_data rather than invented.
DEFENSIVE_RULES = {
    "life": {
        "category": "ehp",
        "score": 18,
        "ko": "생명력 태그",
        "reason": "생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함",
    },
    "energy_shield": {
        "category": "ehp",
        "score": 20,
        "ko": "에너지 보호막 태그",
        "reason": "ES 관련 태그가 있으면 상대 EHP 기반으로 가산하지만 실제 ES 수치는 알 수 없음",
    },
    "es": {
        "category": "ehp",
        "score": 20,
        "ko": "ES 태그",
        "reason": "ES 관련 태그가 있으면 상대 EHP 기반으로 가산하지만 실제 ES 수치는 알 수 없음",
    },
    "mana": {
        "category": "sustain",
        "score": 9,
        "ko": "마나 태그",
        "reason": "마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함",
    },
    "spirit": {
        "category": "sustain",
        "score": 5,
        "ko": "정신력 태그",
        "reason": "정신력 태그는 예약/유지형 방어 가능성을 시사하지만 실제 수치가 없어 낮게 반영함",
    },
    "charge": {
        "category": "mitigation",
        "score": 7,
        "ko": "충전 태그",
        "reason": "충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함",
    },
    "charge_scaling": {
        "category": "mitigation",
        "score": 7,
        "ko": "충전 스케일링",
        "reason": "충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함",
    },
    "cold": {
        "category": "avoidance",
        "score": 6,
        "ko": "냉기 태그",
        "reason": "냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함",
    },
    "minion": {
        "category": "avoidance",
        "score": 5,
        "ko": "소환수 태그",
        "reason": "소환수는 어그로 분산 가능성이 있으나 실제 AI/소환수 수치가 없어 낮게 반영함",
    },
    "minion_scaling": {
        "category": "avoidance",
        "score": 5,
        "ko": "소환수 스케일링",
        "reason": "소환수 스케일링은 어그로 분산 가능성으로만 보수적으로 반영함",
    },
    "ailment_scaling": {
        "category": "avoidance",
        "score": 4,
        "ko": "상태이상 스케일링",
        "reason": "상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함",
    },
}

CATEGORY_FIELDS = {
    "ehp": "ehp_score",
    "recovery": "recovery_score",
    "mitigation": "mitigation_score",
    "avoidance": "avoidance_score",
    "sustain": "sustain_score",
}

BASE_DIMENSION_SCORE = 35
MAX_DIMENSION_SCORE = 100


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


def merge_inputs(interaction_builds, dps_builds, legality_builds):
    dps_index = index_by_build_name(dps_builds)
    legality_index = index_by_build_name(legality_builds)
    merged = []

    for build in interaction_builds:
        key = normalize_key(build.get("build_name"))
        combined = dict(build)
        if key in dps_index:
            combined["dps_analysis"] = dps_index[key]
        if key in legality_index:
            combined["legality_analysis"] = legality_index[key]
        merged.append(combined)

    return merged


def collect_mechanics(build):
    mechanics = set(build.get("mechanics", []))

    for nested_key in ["dps_analysis", "legality_analysis"]:
        nested = build.get(nested_key, {})
        for mechanic in nested.get("mechanics", []):
            mechanics.add(mechanic)

    for unique in build.get("recommended_uniques", []):
        for key in ["matched_tags", "unique_tags"]:
            for tag in unique.get(key, []):
                mechanics.add(tag)

    for affix in build.get("recommended_rare_affixes", []):
        for mechanic in affix.get("mechanics", []):
            mechanics.add(mechanic)

    return sorted(mechanics)


def collect_defensive_factors(mechanics):
    factors = []
    category_scores = {category: BASE_DIMENSION_SCORE for category in CATEGORY_FIELDS}

    for mechanic in mechanics:
        rule = DEFENSIVE_RULES.get(mechanic)
        if not rule:
            continue

        category = rule["category"]
        category_scores[category] += rule["score"]
        factors.append({
            "id": mechanic,
            "category": category,
            "score": rule["score"],
            "ko": rule["ko"],
            "reason": rule["reason"],
        })

    return factors, category_scores


def apply_legality_adjustments(category_scores, weaknesses, explanation, build):
    legality = build.get("legality_analysis")
    if not legality:
        return

    legality_score = legality.get("legality_score")
    if legality_score is None:
        return

    if legality_score < 60:
        penalty = 12
        reason = "legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함"
    elif legality_score < 75:
        penalty = 6
        reason = "legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함"
    else:
        penalty = 0
        reason = "legality_score가 MVP 기준 양호하여 별도 생존 감점을 적용하지 않음"

    if penalty:
        for category in category_scores:
            category_scores[category] -= penalty
        weaknesses.append({
            "type": "legality_risk",
            "message": reason,
            "legality_score": legality_score,
        })
    explanation.append(reason)


def detect_weaknesses(build, mechanics, defensive_factors, scores):
    weaknesses = []
    factor_ids = {factor["id"] for factor in defensive_factors}
    dps = build.get("dps_analysis", {})

    if not ({"life", "energy_shield", "es", "mana"} & factor_ids):
        weaknesses.append({
            "type": "low_ehp_evidence",
            "message": "생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.",
        })

    if scores["mitigation"] <= BASE_DIMENSION_SCORE + 2:
        weaknesses.append({
            "type": "mitigation_data_gap",
            "message": "방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.",
        })

    if scores["recovery"] <= BASE_DIMENSION_SCORE + 2:
        weaknesses.append({
            "type": "recovery_data_gap",
            "message": "흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.",
        })

    if dps.get("estimated_dps_score", 0) and dps.get("estimated_dps_score", 0) > 2500 and scores["ehp"] < 55:
        weaknesses.append({
            "type": "glass_cannon_risk",
            "message": "DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.",
            "estimated_dps_score": dps.get("estimated_dps_score"),
        })

    if "trigger_loop" in mechanics or any(combo.get("name") == "Trigger Loop Candidate" for combo in build.get("broken_combos", [])):
        weaknesses.append({
            "type": "trigger_loop_stability_risk",
            "message": "발동 루프 후보는 자원 소모/쿨다운/조건 실패 시 생존 안정성이 떨어질 수 있습니다.",
        })

    return weaknesses


def build_missing_data(build, dps_available, legality_available):
    missing = [
        {
            "type": "exact_defensive_stats_missing",
            "message": "실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.",
        },
        {
            "type": "recovery_values_missing",
            "message": "재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.",
        },
    ]

    if not dps_available:
        missing.append({
            "type": "dps_input_missing",
            "message": "DPS 추정 결과가 없어 glass cannon 위험 평가 일부를 생략했습니다.",
        })

    if not legality_available:
        missing.append({
            "type": "legality_input_missing",
            "message": "legality 분석 결과가 없어 조건부 작동/장비 제한 리스크 반영을 생략했습니다.",
        })

    if not build.get("recommended_rare_affixes"):
        missing.append({
            "type": "defensive_rare_affixes_missing",
            "message": "추천 rare affix 데이터가 없거나 방어 affix가 감지되지 않았습니다.",
        })

    return missing


def clamp_score(value):
    return round(max(0, min(MAX_DIMENSION_SCORE, value)), 3)


def estimate_build_survivability(build, dps_available, legality_available):
    mechanics = collect_mechanics(build)
    defensive_factors, raw_category_scores = collect_defensive_factors(mechanics)
    explanation = []
    weaknesses = []

    if defensive_factors:
        explanation.extend(factor["reason"] for factor in defensive_factors)
    else:
        explanation.append("방어 메커닉 태그가 거의 없어 기본 생존 점수에서 시작합니다.")

    apply_legality_adjustments(raw_category_scores, weaknesses, explanation, build)

    scores = {category: clamp_score(score) for category, score in raw_category_scores.items()}
    weaknesses.extend(detect_weaknesses(build, mechanics, defensive_factors, scores))

    ehp_score = scores["ehp"]
    recovery_score = scores["recovery"]
    mitigation_score = scores["mitigation"]
    avoidance_score = scores["avoidance"]
    sustain_score = scores["sustain"]

    survivability_score = round(
        ehp_score * 0.34
        + mitigation_score * 0.22
        + recovery_score * 0.18
        + avoidance_score * 0.14
        + sustain_score * 0.12,
        3,
    )

    if weaknesses:
        explanation.append("약점은 확정 사망 원인이 아니라, 실제 방어 수치가 들어오기 전까지 우선 검증해야 할 리스크입니다.")

    return {
        "build_name": build.get("build_name", ""),
        "main_skill": build.get("main_skill", ""),
        "archetype_label_ko": build.get("archetype_label_ko", ""),
        "survivability_score": survivability_score,
        "ehp_score": ehp_score,
        "recovery_score": recovery_score,
        "mitigation_score": mitigation_score,
        "avoidance_score": avoidance_score,
        "sustain_score": sustain_score,
        "defensive_factors": defensive_factors,
        "weaknesses": weaknesses,
        "missing_data": build_missing_data(build, dps_available, legality_available),
        "explanation": explanation,
        "mechanics": mechanics,
        "dps_summary": {
            "estimated_dps_score": build.get("dps_analysis", {}).get("estimated_dps_score"),
            "single_target_score": build.get("dps_analysis", {}).get("single_target_score"),
            "mapping_score": build.get("dps_analysis", {}).get("mapping_score"),
            "dps_data_available": bool(build.get("dps_analysis")),
        },
        "legality_summary": {
            "is_legal": build.get("legality_analysis", {}).get("is_legal"),
            "legality_score": build.get("legality_analysis", {}).get("legality_score"),
            "legality_data_available": bool(build.get("legality_analysis")),
        },
        "model_notes": [
            "Relative survivability approximation only; exact EHP, armour, evasion, block, resistance, recovery, and sustain values are not modeled.",
            "Internal mechanic ids remain canonical English; Korean text is report/explanation only.",
        ],
    }


def estimate_survivability(builds, dps_available, legality_available):
    results = [estimate_build_survivability(build, dps_available, legality_available) for build in builds]
    results.sort(key=lambda item: item["survivability_score"], reverse=True)
    return results


def fmt_items(items, key="message", limit=5):
    if not items:
        return "- 없음"

    lines = []
    for item in items[:limit]:
        if isinstance(item, dict):
            lines.append(f"- {item.get(key, item.get('reason', item.get('type', str(item))))}")
        else:
            lines.append(f"- {item}")

    if len(items) > limit:
        lines.append(f"- ... 외 {len(items) - limit}개")

    return "\n".join(lines)


def generate_report(results, dps_available, legality_available):
    lines = [
        "# Survivability Approximation Report",
        "",
        "> 이 리포트는 정확한 PoE2 EHP 계산이 아니라 현재 태그/상호작용/선택 입력을 이용한 상대 생존력 추정입니다.",
        "> 실제 생명력, ES, 방어도, 회피, 막기, 저항, 회복량 데이터가 없으면 missing_data로 표시하고 가짜 수치를 만들지 않습니다.",
        "",
        "## 입력 / 출력",
        "",
        f"- 입력: `{INTERACTION_PATH.relative_to(ROOT)}`",
        f"- 선택 입력: `{DPS_PATH.relative_to(ROOT)}` ({'사용됨' if dps_available else '없음 / 스킵됨'})",
        f"- 선택 입력: `{LEGALITY_PATH.relative_to(ROOT)}` ({'사용됨' if legality_available else '없음 / 스킵됨'})",
        f"- JSON 출력: `{OUT_PATH.relative_to(ROOT)}`",
        f"- 리포트 출력: `{REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## 모델링 범위",
        "",
        "- 포함: life, ES, mana, spirit, charge, cold/ailment control, minion aggro 분산 태그 기반 상대 점수",
        "- 미포함: 실제 생명력/ES 수치, 방어도, 회피, 막기, 저항, 피해 감소, 회복량, 플라스크, 몬스터 피해량",
        "- 누락 데이터는 결과 JSON의 `missing_data` 필드에 표시합니다.",
        "",
        "## 요약",
        "",
        f"- 분석 빌드 수: {len(results)}",
    ]

    if results:
        top = results[0]
        lines.append(f"- 최고 생존력 후보: {top['build_name']} / survivability_score {top['survivability_score']}")

    lines.extend(["", "## Top Survivability Candidates", ""])

    for index, result in enumerate(results[:25], start=1):
        lines.extend([
            f"### {index}. {result['build_name']}",
            "",
            f"- 메인 스킬: {result['main_skill']}",
            f"- survivability_score: {result['survivability_score']}",
            f"- ehp_score: {result['ehp_score']}",
            f"- recovery_score: {result['recovery_score']}",
            f"- mitigation_score: {result['mitigation_score']}",
            f"- avoidance_score: {result['avoidance_score']}",
            f"- sustain_score: {result['sustain_score']}",
            f"- estimated_dps_score: {result['dps_summary']['estimated_dps_score'] if result['dps_summary']['dps_data_available'] else 'N/A'}",
            f"- legality_score: {result['legality_summary']['legality_score'] if result['legality_summary']['legality_data_available'] else 'N/A'}",
            "",
            "#### 방어 근거",
            "",
            fmt_items(result["defensive_factors"], key="reason"),
            "",
            "#### 약점",
            "",
            fmt_items(result["weaknesses"]),
            "",
            "#### Missing Data / TODO",
            "",
            fmt_items(result["missing_data"]),
            "",
        ])

    return "\n".join(lines).rstrip() + "\n"


def main():
    interaction_builds = load_json(INTERACTION_PATH, required=True)
    dps_available = DPS_PATH.exists()
    legality_available = LEGALITY_PATH.exists()
    dps_builds = load_json(DPS_PATH, default=[]) if dps_available else []
    legality_builds = load_json(LEGALITY_PATH, default=[]) if legality_available else []

    builds = merge_inputs(interaction_builds, dps_builds, legality_builds)
    results = estimate_survivability(builds, dps_available, legality_available)

    save_json(OUT_PATH, results)
    save_text(REPORT_PATH, generate_report(results, dps_available, legality_available))

    print(f"loaded interaction builds: {len(interaction_builds)}")
    print(f"loaded dps builds: {len(dps_builds)}")
    print(f"loaded legality builds: {len(legality_builds)}")
    print(f"survivability results: {len(results)}")

    for result in results[:10]:
        print("=" * 80)
        print(f"빌드명: {result['build_name']}")
        print(f"생존 점수: {result['survivability_score']}")
        print(
            f"EHP: {result['ehp_score']} / 회복: {result['recovery_score']} / "
            f"완화: {result['mitigation_score']} / 회피: {result['avoidance_score']} / 유지력: {result['sustain_score']}"
        )


if __name__ == "__main__":
    main()
