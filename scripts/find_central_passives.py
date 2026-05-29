import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "skills" / "skill_passive_synergy.json"

OUT_PATH = ROOT / "data" / "meta" / "central_passives.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    data = load_json(INPUT_PATH)

    passive_scores = defaultdict(float)
    passive_hits = defaultdict(int)
    passive_examples = defaultdict(list)
    passive_tags = {}

    for skill in data:

        if skill["total_score"] < 3500:
            continue

        for p in skill["top_passives"]:

            name = p["passive_name"]

            passive_scores[name] += p["score"]
            passive_hits[name] += 1

            passive_tags[name] = p["passive_tags"]

            if len(passive_examples[name]) < 10:
                passive_examples[name].append(skill["skill"])

    result = []

    for name in passive_scores:

        result.append({
            "passive": name,
            "score": round(passive_scores[name], 2),
            "hits": passive_hits[name],
            "tags": passive_tags[name],
            "examples": passive_examples[name]
        })

    result.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Central Passive Analysis 완료")
    print()

    print("TOP 50 Central Passives")
    print("=" * 80)

    for i, row in enumerate(result[:50], 1):

        print(
            f"{i:02}. "
            f"{row['passive']} | "
            f"score={row['score']} | "
            f"hits={row['hits']} | "
            f"tags={row['tags']}"
        )

        print(
            f"    examples: "
            f"{', '.join(row['examples'][:5])}"
        )


if __name__ == "__main__":
    main()