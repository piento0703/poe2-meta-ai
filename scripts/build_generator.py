import json
from pathlib import Path
from archetype_classifier import classify_build


ROOT = Path(__file__).resolve().parents[1]

TRIPLE_PATH = ROOT / "data" / "meta" / "triple_synergy_candidates.json"
UNIQUE_MATCH_PATH = ROOT / "data" / "meta" / "unique_build_matches.json"
UNIQUE_LOCALIZATION_PATH = ROOT / "data" / "meta" / "unique_localization_map.json"
OUT_PATH = ROOT / "data" / "meta" / "generated_builds.json"


MAX_SUPPORTS = 6
MAX_UNIQUES = 5
MAX_BUILDS = 100


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


def localize_unique_name(name, localization_map):
    return localization_map.get(name, name)


def get_name(obj):
    if isinstance(obj, str):
        return obj

    if not isinstance(obj, dict):
        return ""

    for key in ["name_ko", "display_name", "name", "skill_name", "support_name", "unique_name"]:
        value = obj.get(key)
        if value:
            return value

    return ""


def get_score(obj):
    if not isinstance(obj, dict):
        return 0

    for key in [
        "final_score",
        "score",
        "synergy_score",
        "total_score",
        "weighted_score",
        "match_score",
        "build_score",
    ]:
        value = obj.get(key)
        if isinstance(value, (int, float)):
            return float(value)

    return 0


def extract_skill_name(candidate):
    for key in ["skill_name", "main_skill", "skill"]:
        value = candidate.get(key)

        if isinstance(value, str):
            return value

        if isinstance(value, dict):
            name = get_name(value)
            if name:
                return name

    return "알 수 없는 스킬"


def extract_support_name(candidate):
    for key in ["support_name", "support"]:
        value = candidate.get(key)

        if isinstance(value, str):
            return value

        if isinstance(value, dict):
            name = get_name(value)
            if name:
                return name

    return ""


def extract_passive_name(candidate):
    for key in ["passive_name", "passive", "node", "passive_node"]:
        value = candidate.get(key)

        if isinstance(value, str):
            return value

        if isinstance(value, dict):
            name = get_name(value)
            if name:
                return name

    return ""


def normalize_key(value):
    return str(value).strip().lower()


def group_triples_by_skill(triple_candidates):
    grouped = {}

    for candidate in triple_candidates:
        skill_name = extract_skill_name(candidate)
        key = normalize_key(skill_name)

        if key not in grouped:
            grouped[key] = {
                "skill_name": skill_name,
                "candidates": [],
                "supports": {},
                "passives": {},
                "base_score": 0,
            }

        support_name = extract_support_name(candidate)
        passive_name = extract_passive_name(candidate)
        score = get_score(candidate)

        grouped[key]["candidates"].append(candidate)
        grouped[key]["base_score"] += score

        if support_name:
            current = grouped[key]["supports"].get(support_name, 0)
            grouped[key]["supports"][support_name] = max(current, score)

        if passive_name:
            current = grouped[key]["passives"].get(passive_name, 0)
            grouped[key]["passives"][passive_name] = max(current, score)

    return grouped


def build_unique_index(unique_matches):
    index = {}

    for match in unique_matches:
        skill_name = extract_skill_name(match)
        key = normalize_key(skill_name)

        if key not in index:
            index[key] = []

        uniques = match.get("uniques", [])

        for unique in uniques:
            expanded = {
                "skill": match.get("skill"),
                "support": match.get("support"),
                "build_score": match.get("build_score", 0),
                "shared_tags": match.get("shared_tags", []),
                "shared_tags_ko": match.get("shared_tags_ko", []),
                "unique": unique,
                "score": unique.get("score", 0),
            }

            index[key].append(expanded)

    for key in index:
        index[key].sort(key=get_score, reverse=True)

    return index


def pick_top_names(score_map, limit):
    return [
        name
        for name, _ in sorted(score_map.items(), key=lambda x: x[1], reverse=True)[:limit]
    ]


def extract_unique_name(match):
    unique = match.get("unique")

    if isinstance(unique, dict):
        for key in ["name_ko", "display_name", "name"]:
            value = unique.get(key)
            if value:
                return value

    for key in ["unique_name", "item_name", "name_ko", "name"]:
        value = match.get(key)
        if value:
            return value

    return ""


def pick_uniques(matches, localization_map, limit=MAX_UNIQUES):
    uniques = []
    seen = set()

    for match in matches:
        name = extract_unique_name(match)

        if not name:
            continue

        key = normalize_key(name)

        if key in seen:
            continue

        seen.add(key)

        unique_obj = match.get("unique", {})

        matched_tags = unique_obj.get("matched_tags", [])
        matched_tags_ko = unique_obj.get("matched_tags_ko", [])

        unique_tags = unique_obj.get("unique_tags", [])
        unique_tags_ko = unique_obj.get("unique_tags_ko", [])

        localized_name = localize_unique_name(name, localization_map)

        uniques.append({
            "name": localized_name,
            "canonical_name": name,
            "base_type": unique_obj.get("base_type", ""),
            "score": get_score(match),
            "role": classify_unique_role(match),
            "matched_tags": matched_tags,
            "matched_tags_ko": matched_tags_ko,
            "unique_tags": unique_tags,
            "unique_tags_ko": unique_tags_ko,
        })

        if len(uniques) >= limit:
            break

    return uniques


def classify_unique_role(match):
    text = json.dumps(match, ensure_ascii=False).lower()

    if any(k in text for k in ["trigger", "meta_energy", "발동", "메타 에너지"]):
        return "engine"

    if any(k in text for k in ["extra", "gain", "as extra", "추가", "획득", "extra_projectile"]):
        return "scaling"

    if any(k in text for k in ["convert", "conversion", "전환"]):
        return "conversion"

    if any(k in text for k in ["enable", "enables", "활성", "가능"]):
        return "enable"

    return "support"


def calculate_build_score(group, archetype_result, uniques):
    base = group["base_score"]

    support_bonus = min(len(group["supports"]), MAX_SUPPORTS) * 8
    passive_bonus = min(len(group["passives"]), 8) * 3
    unique_bonus = len(uniques) * 6
    archetype_bonus = len(archetype_result["archetypes"]) * 10

    combo_bonus = 0
    archetypes = set(archetype_result["archetypes"])

    if {"trigger", "projectile"}.issubset(archetypes):
        combo_bonus += 15

    if {"projectile", "chain"}.issubset(archetypes):
        combo_bonus += 18

    if {"lightning", "chain"}.issubset(archetypes):
        combo_bonus += 12

    if {"minion", "duration"}.issubset(archetypes):
        combo_bonus += 10

    if {"grenade", "duration"}.issubset(archetypes):
        combo_bonus += 10

    return round(
        base
        + support_bonus
        + passive_bonus
        + unique_bonus
        + archetype_bonus
        + combo_bonus,
        3,
    )


def make_build_name(skill_name, archetype_result):
    label = archetype_result.get("archetype_label_ko", "").strip()

    if label:
        return f"{skill_name} {label} 빌드"

    return f"{skill_name} 빌드"


def generate_builds(triple_candidates, unique_matches):
    localization_map = load_json(UNIQUE_LOCALIZATION_PATH, {})

    grouped = group_triples_by_skill(triple_candidates)
    unique_index = build_unique_index(unique_matches)

    builds = []

    for key, group in grouped.items():
        sample_candidates = group["candidates"][:10]

        merged_for_classify = {
            "skill_name": group["skill_name"],
            "supports": list(group["supports"].keys()),
            "passives": list(group["passives"].keys()),
            "samples": sample_candidates,
            "uniques": unique_index.get(key, [])[:10],
        }

        archetype_result = classify_build(merged_for_classify)

        supports = pick_top_names(group["supports"], MAX_SUPPORTS)
        passives = pick_top_names(group["passives"], 10)

        uniques = pick_uniques(
            unique_index.get(key, []),
            localization_map,
            MAX_UNIQUES
        )

        build_score = calculate_build_score(group, archetype_result, uniques)

        build = {
            "build_name": make_build_name(group["skill_name"], archetype_result),
            "main_skill": group["skill_name"],
            "archetype_label_en": archetype_result["archetype_label_en"],
            "archetype_label_ko": archetype_result["archetype_label_ko"],
            "archetypes": archetype_result["archetypes"],
            "main_scaling": archetype_result["main_scaling"],
            "recommended_supports": supports,
            "passive_direction": passives,
            "recommended_uniques": uniques,
            "build_score": build_score,
            "candidate_count": len(group["candidates"]),
            "support_count": len(group["supports"]),
            "passive_count": len(group["passives"]),
        }

        builds.append(build)

    builds.sort(key=lambda x: x["build_score"], reverse=True)

    return builds[:MAX_BUILDS]


def main():
    triple_candidates = load_json(TRIPLE_PATH)
    unique_matches = load_json(UNIQUE_MATCH_PATH)

    print(f"triple candidates: {len(triple_candidates)}")
    print(f"unique matches: {len(unique_matches)}")

    builds = generate_builds(triple_candidates, unique_matches)

    save_json(OUT_PATH, builds)

    print(f"generated builds: {len(builds)}")

    for build in builds[:10]:
        print("=" * 80)
        print(f"빌드명: {build['build_name']}")
        print(f"점수: {build['build_score']}")
        print(f"메인 스킬: {build['main_skill']}")
        print(f"아키타입: {build['archetype_label_ko']}")
        print(f"추천 보조젬: {', '.join(build['recommended_supports'][:6])}")

        unique_names = [u["name"] for u in build["recommended_uniques"][:5]]

        print(f"추천 유니크: {', '.join(unique_names)}")


if __name__ == "__main__":
    main()