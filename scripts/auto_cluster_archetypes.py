import json
from pathlib import Path
from collections import defaultdict
from itertools import combinations

ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "skills" / "skill_passive_synergy.json"
OUT_PATH = ROOT / "data" / "meta" / "auto_clusters.json"

CORE_TAGS = {
    "lightning",
    "cold",
    "fire",
    "crit",
    "shapeshift",
    "gain_as_extra",
    "meta_energy",
    "reservation",
    "consume_charge",
    "power_charge",
    "frenzy_charge",
    "endurance_charge",
    "skill_speed",
    "trigger",
    "duration",
    "projectile",
    "long_range"
}

NOISE_TAGS = {
    "aoe",
    "attack",
    "spell",
    "physical",
    "chaos",
    "minion"
}

TAG_WEIGHTS = {
    "gain_as_extra": 7.0,
    "meta_energy": 6.5,
    "consume_charge": 6.0,
    "crit": 5.5,
    "reservation": 5.0,
    "shapeshift": 5.0,
    "skill_speed": 4.5,
    "power_charge": 4.5,
    "lightning": 4.0,
    "cold": 4.0,
    "fire": 4.0,
    "trigger": 4.0,
    "duration": 3.5,
    "projectile": 3.5,
    "long_range": 3.5
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def core_tags(tags):
    return sorted(
        tag for tag in set(tags)
        if tag in CORE_TAGS and tag not in NOISE_TAGS
    )


def cluster_name(tags):
    priority = [
        "gain_as_extra",
        "meta_energy",
        "consume_charge",
        "power_charge",
        "shapeshift",
        "crit",
        "trigger",
        "duration",
        "projectile",
        "lightning",
        "cold",
        "fire"
    ]

    ordered = sorted(
        tags,
        key=lambda t: priority.index(t) if t in priority else 999
    )

    return " + ".join(ordered)


def tag_weight_score(tags):
    return sum(TAG_WEIGHTS.get(tag, 1.0) for tag in tags)


def main():
    data = load_json(INPUT_PATH)

    clusters = defaultdict(list)

    for row in data:
        tags = core_tags(row.get("skill_tags", []))

        if len(tags) < 2:
            continue

        # 2~4개 조합까지 archetype 후보로 생성
        for size in range(2, min(4, len(tags)) + 1):
            for combo in combinations(tags, size):
                clusters[combo].append({
                    "skill": row["skill"],
                    "score": row["total_score"],
                    "skill_tags": row["skill_tags"]
                })

    results = []

    for combo, skills in clusters.items():
        if len(skills) < 2:
            continue

        total_skill_score = sum(s["score"] for s in skills)
        avg_skill_score = total_skill_score / len(skills)
        combo_weight = tag_weight_score(combo)

        cluster_score = (
            len(skills) * 20
            + avg_skill_score * 0.05
            + combo_weight * 10
        )

        top_skills = sorted(
            skills,
            key=lambda x: x["score"],
            reverse=True
        )[:15]

        results.append({
            "cluster": cluster_name(combo),
            "tags": list(combo),
            "cluster_score": round(cluster_score, 2),
            "skill_count": len(skills),
            "avg_skill_score": round(avg_skill_score, 2),
            "total_skill_score": round(total_skill_score, 2),
            "top_skills": top_skills
        })

    results.sort(
        key=lambda x: x["cluster_score"],
        reverse=True
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Auto Archetype Clustering 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP 40 Auto Archetype Clusters")
    print("=" * 90)

    for i, row in enumerate(results[:40], 1):
        print(
            f"{i:02}. {row['cluster']} | "
            f"score={row['cluster_score']} | "
            f"skills={row['skill_count']} | "
            f"avg={row['avg_skill_score']}"
        )

        for s in row["top_skills"][:5]:
            print(f"    - {s['skill']} | {s['score']}")

        print()


if __name__ == "__main__":
    main()