import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]

CLUSTER_PATH = ROOT / "data" / "meta" / "auto_clusters.json"
SYNERGY_PATH = ROOT / "data" / "skills" / "skill_passive_synergy.json"

OUT_PATH = ROOT / "data" / "meta" / "cluster_passive_rankings.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    clusters = load_json(CLUSTER_PATH)
    synergy = load_json(SYNERGY_PATH)

    skill_map = {
        row["skill"]: row
        for row in synergy
    }

    results = []

    for cluster in clusters:
        passive_scores = defaultdict(float)
        passive_hits = defaultdict(int)
        passive_tags = {}
        passive_examples = defaultdict(list)

        cluster_skills = cluster.get("top_skills", [])

        for s in cluster_skills:
            skill_name = s["skill"]

            if skill_name not in skill_map:
                continue

            skill_row = skill_map[skill_name]

            for p in skill_row.get("top_passives", []):
                passive_name = p["passive_name"]

                passive_scores[passive_name] += p["score"]
                passive_hits[passive_name] += 1
                passive_tags[passive_name] = p.get("passive_tags", [])

                if len(passive_examples[passive_name]) < 8:
                    passive_examples[passive_name].append(skill_name)

        ranked_passives = []

        for passive_name in passive_scores:
            ranked_passives.append({
                "passive": passive_name,
                "score": round(passive_scores[passive_name], 2),
                "hits": passive_hits[passive_name],
                "tags": passive_tags[passive_name],
                "examples": passive_examples[passive_name]
            })

        ranked_passives.sort(
            key=lambda x: (x["score"], x["hits"]),
            reverse=True
        )

        results.append({
            "cluster": cluster["cluster"],
            "tags": cluster["tags"],
            "cluster_score": cluster["cluster_score"],
            "skill_count": cluster["skill_count"],
            "top_skills": cluster["top_skills"][:10],
            "top_passives": ranked_passives[:25]
        })

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Cluster Passive Ranking 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP Cluster Passive Mapping")
    print("=" * 100)

    for i, row in enumerate(results[:20], 1):
        print(
            f"{i:02}. {row['cluster']} | "
            f"cluster_score={row['cluster_score']} | "
            f"skills={row['skill_count']}"
        )

        print("    Top Skills:")
        for s in row["top_skills"][:5]:
            print(f"      - {s['skill']} | {s['score']}")

        print("    Top Passives:")
        for p in row["top_passives"][:8]:
            print(
                f"      - {p['passive']} | "
                f"score={p['score']} | "
                f"hits={p['hits']} | "
                f"tags={p['tags']}"
            )

        print()


if __name__ == "__main__":
    main()