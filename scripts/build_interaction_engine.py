import json
from pathlib import Path
from mechanic_semantic_parser import parse_option_list, detect_broken_combos


ROOT = Path(__file__).resolve().parents[1]

BUILDS_PATH = ROOT / "data" / "meta" / "generated_builds_filtered.json"
RARE_AFFIX_PATH = ROOT / "data" / "meta" / "rare_affix_semantic_analysis.json"
OUT_PATH = ROOT / "data" / "meta" / "build_interaction_analysis.json"


ARCHETYPE_TO_MECHANICS = {
    "projectile": ["extra_projectile"],
    "chain": ["chain"],
    "trigger": ["trigger"],
    "lightning": ["ailment_scaling"],
    "fire": ["ailment_scaling"],
    "cold": ["ailment_scaling"],
    "crit": ["crit_scaling"],
    "minion": ["minion_scaling"],
    "duration": [],
    "aoe": ["overlap"],
}


SUPPORT_HINTS = {
    "세차게 흐르는 전류": ["chain", "lightning"],
    "마름쇠": ["projectile"],
    "화산 분출": ["overlap", "fire"],
    "분화구": ["overlap", "fire"],
    "정전기 감전": ["ailment_scaling", "lightning"],
    "충전된 징표": ["charge_scaling"],
    "얼어붙은 악의": ["ailment_scaling", "cold"],
    "하욕시의 뇌전": ["lightning", "trigger"],
    "원소 방출": ["ailment_scaling"],
    "촉진시키는 원소": ["ailment_scaling"],
    "독 포자": ["ailment_scaling", "chaos", "overlap"],
    "몽상가의 종소리": ["trigger"],
}


def load_json(path, default=None):
    if default is None:
        default = []

    if not path.exists():
        print(f"[WARN] missing file: {path}")
        return default

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"저장 완료: {path}")


def unique_mechanics(unique):
    mechanics = set()

    for key in ["matched_tags", "unique_tags"]:
        for tag in unique.get(key, []):
            mechanics.add(tag)

    return sorted(mechanics)


def build_base_mechanics(build):
    mechanics = set()

    for archetype in build.get("archetypes", []):
        for m in ARCHETYPE_TO_MECHANICS.get(archetype, []):
            mechanics.add(m)

    for support in build.get("recommended_supports", []):
        for m in SUPPORT_HINTS.get(support, []):
            mechanics.add(m)

    for unique in build.get("recommended_uniques", []):
        for m in unique_mechanics(unique):
            mechanics.add(m)

    return sorted(mechanics)


def pick_best_rare_affixes(rare_affixes, limit=3):
    return sorted(
        rare_affixes,
        key=lambda x: x.get("final_score", 0),
        reverse=True,
    )[:limit]


def merge_mechanics(*lists):
    result = set()

    for values in lists:
        for value in values:
            result.add(value)

    return sorted(result)


def score_interaction(build, mechanics, rare_affixes):
    base_score = build.get("build_score", 0)
    combo_hits = detect_broken_combos(mechanics)
    combo_score = sum(c["score"] for c in combo_hits)

    rare_score = sum(a.get("final_score", 0) for a in rare_affixes[:3])
    rare_score = min(rare_score, 120)

    mechanic_density = len(mechanics) * 3

    final_score = round(
        base_score
        + combo_score
        + rare_score
        + mechanic_density,
        3,
    )

    return final_score, combo_hits


def classify_interaction_level(score):
    if score >= 900:
        return "S급 / 메타 파괴 후보"
    if score >= 700:
        return "A급 / 강력한 OP 후보"
    if score >= 500:
        return "B급 / 실전 빌드 후보"
    if score >= 300:
        return "C급 / 추가 검증 필요"
    return "낮음"


def analyze_build_interactions(builds, rare_affixes):
    results = []

    best_affixes = pick_best_rare_affixes(rare_affixes, limit=3)

    for build in builds:
        base_mechanics = build_base_mechanics(build)

        affix_mechanics = set()
        for affix in best_affixes:
            for m in affix.get("mechanics", []):
                affix_mechanics.add(m)

        merged = merge_mechanics(base_mechanics, affix_mechanics)

        final_score, combo_hits = score_interaction(
            build,
            merged,
            best_affixes,
        )

        results.append({
            "build_name": build.get("build_name", ""),
            "main_skill": build.get("main_skill", ""),
            "base_build_score": build.get("build_score", 0),
            "interaction_score": final_score,
            "interaction_level": classify_interaction_level(final_score),
            "archetype_label_ko": build.get("archetype_label_ko", ""),
            "mechanics": merged,
            "broken_combos": combo_hits,
            "recommended_supports": build.get("recommended_supports", []),
            "recommended_uniques": build.get("recommended_uniques", []),
            "recommended_rare_affixes": best_affixes,
        })

    results.sort(key=lambda x: x["interaction_score"], reverse=True)

    return results


def main():
    builds = load_json(BUILDS_PATH)
    rare_affixes = load_json(RARE_AFFIX_PATH)

    print(f"loaded builds: {len(builds)}")
    print(f"loaded rare affix candidates: {len(rare_affixes)}")

    results = analyze_build_interactions(builds, rare_affixes)

    save_json(OUT_PATH, results)

    for result in results[:10]:
        print("=" * 80)
        print(f"빌드명: {result['build_name']}")
        print(f"상호작용 점수: {result['interaction_score']}")
        print(f"등급: {result['interaction_level']}")
        print(f"메커니즘: {', '.join(result['mechanics'])}")

        if result["broken_combos"]:
            print("Broken Combo:")
            for combo in result["broken_combos"]:
                print(f"- {combo['ko']}: {combo['reason']}")


if __name__ == "__main__":
    main()