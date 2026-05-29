import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "meta" / "generated_builds.json"
OUT_PATH = ROOT / "data" / "meta" / "generated_builds_filtered.json"


BAD_ARCHETYPE_SKILL_HINTS = {
    "warcry": ["투사체", "연쇄"],
    "minion": ["투사체"],
}


SKILL_HINTS = {
    "함성": "warcry",
    "소환": "minion",
    "하수인": "minion",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"저장 완료: {path}")


def detect_skill_type(skill_name):
    for keyword, skill_type in SKILL_HINTS.items():
        if keyword in skill_name:
            return skill_type

    return "generic"


def calculate_penalty(build):
    skill_name = build.get("main_skill", "")
    archetype_ko = build.get("archetype_label_ko", "")
    skill_type = detect_skill_type(skill_name)

    penalty = 0
    reasons = []

    bad_arches = BAD_ARCHETYPE_SKILL_HINTS.get(skill_type, [])

    for bad in bad_arches:
        if bad in archetype_ko:
            penalty += 80
            reasons.append(f"{skill_type} 스킬에 {bad} 아키타입 과다 반영")

    supports = build.get("recommended_supports", [])

    if skill_type == "warcry":
        projectile_like = ["마름쇠", "화산 분출", "분화구", "독 포자"]
        count = sum(1 for s in supports if s in projectile_like)

        if count >= 3:
            penalty += 60
            reasons.append("함성 스킬에 투사체/지속 피해형 보조젬 과다 추천")

    return penalty, reasons


def filter_builds(builds):
    filtered = []

    for build in builds:
        penalty, reasons = calculate_penalty(build)

        original_score = build.get("build_score", 0)
        adjusted_score = max(0, original_score - penalty)

        new_build = dict(build)
        new_build["original_build_score"] = original_score
        new_build["validity_penalty"] = penalty
        new_build["validity_reasons"] = reasons
        new_build["build_score"] = adjusted_score

        if adjusted_score <= 0:
            continue

        filtered.append(new_build)

    filtered.sort(key=lambda x: x["build_score"], reverse=True)

    return filtered


def main():
    builds = load_json(INPUT_PATH)

    print(f"loaded builds: {len(builds)}")

    filtered = filter_builds(builds)

    save_json(OUT_PATH, filtered)

    print(f"filtered builds: {len(filtered)}")

    for build in filtered[:10]:
        print("=" * 80)
        print(f"빌드명: {build['build_name']}")
        print(f"점수: {build['build_score']} / 원점수: {build['original_build_score']}")
        print(f"패널티: {build['validity_penalty']}")
        if build["validity_reasons"]:
            print(f"사유: {', '.join(build['validity_reasons'])}")


if __name__ == "__main__":
    main()