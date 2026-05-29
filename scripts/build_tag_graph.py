import json
from pathlib import Path
from collections import defaultdict
from itertools import combinations

ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "skills" / "skill_passive_synergy.json"

OUT_MATRIX = ROOT / "data" / "meta" / "core_tag_cooccurrence.json"
OUT_EDGES = ROOT / "data" / "meta" / "core_tag_graph_edges.json"

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

LOW_SIGNAL_TAGS = {
    "aoe",
    "attack",
    "spell",
    "physical",
    "chaos",
    "minion"
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def pair_key(a, b):
    return f"{a}__{b}"


def main():
    data = load_json(INPUT_PATH)

    pair_counts = defaultdict(int)
    node_counts = defaultdict(int)
    skill_examples = defaultdict(list)

    for row in data:
        raw_tags = set(row.get("skill_tags", []))

        tags = sorted(
            tag for tag in raw_tags
            if tag in CORE_TAGS and tag not in LOW_SIGNAL_TAGS
        )

        if len(tags) < 2:
            continue

        for tag in tags:
            node_counts[tag] += 1

        for a, b in combinations(tags, 2):
            pair_counts[(a, b)] += 1

            if len(skill_examples[(a, b)]) < 10:
                skill_examples[(a, b)].append(row["skill"])

    edges = []

    for (a, b), count in sorted(
        pair_counts.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        edges.append({
            "source": a,
            "target": b,
            "weight": count,
            "examples": skill_examples[(a, b)]
        })

    matrix = {}

    for (a, b), count in pair_counts.items():
        matrix[pair_key(a, b)] = {
            "source": a,
            "target": b,
            "weight": count,
            "examples": skill_examples[(a, b)]
        }

    OUT_MATRIX.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_MATRIX, "w", encoding="utf-8") as f:
        json.dump(matrix, f, ensure_ascii=False, indent=2)

    with open(OUT_EDGES, "w", encoding="utf-8") as f:
        json.dump(edges, f, ensure_ascii=False, indent=2)

    print("Core Tag Co-occurrence Graph 생성 완료")
    print(f"저장 위치: {OUT_MATRIX}")
    print(f"저장 위치: {OUT_EDGES}")
    print()

    print("TOP 50 Core Meta Connections")
    print("=" * 80)

    for i, edge in enumerate(edges[:50], 1):
        print(
            f"{i:02}. "
            f"{edge['source']} ↔ {edge['target']} "
            f"= {edge['weight']}"
        )
        print(f"    examples: {', '.join(edge['examples'][:5])}")

    print()
    print("TOP Core Meta Nodes")
    print("=" * 80)

    for tag, count in sorted(
        node_counts.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{tag:20} {count}")


if __name__ == "__main__":
    main()