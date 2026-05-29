import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]

PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
OUT_PATH = ROOT / "data" / "meta" / "start_node_inspection.json"


KEYWORDS = [
    "start",
    "starting",
    "strength",
    "dexterity",
    "intelligence",
    "class",
    "ascendancy",
    "warrior",
    "ranger",
    "witch",
    "sorceress",
    "monk",
    "mercenary",
    "huntress",
    "druid"
]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def flatten_value(value):
    if value is None:
        return ""

    if isinstance(value, str):
        return value

    if isinstance(value, list):
        return " ".join(flatten_value(v) for v in value)

    if isinstance(value, dict):
        return " ".join(flatten_value(v) for v in value.values())

    return str(value)


def node_name(node):
    return node.get("name") or node.get("dn") or ""


def node_text(node):
    return " ".join(flatten_value(v) for v in node.values())


def main():
    data = load_json(PASSIVE_PATH)
    nodes = data["nodes"]

    key_counter = Counter()
    field_samples = defaultdict(list)
    keyword_hits = []

    for node_id, node in nodes.items():
        for key, value in node.items():
            key_counter[key] += 1

            if len(field_samples[key]) < 5:
                field_samples[key].append(value)

        text = node_text(node).lower()
        name = node_name(node)

        matched = [
            kw for kw in KEYWORDS
            if kw in text
        ]

        if matched:
            keyword_hits.append({
                "id": str(node_id),
                "name": name,
                "matched_keywords": matched,
                "keys": list(node.keys()),
                "ascendancyName": node.get("ascendancyName"),
                "isRoot": node.get("isRoot"),
                "isNotable": node.get("isNotable"),
                "isKeystone": node.get("isKeystone"),
                "out_count": len(node.get("out", [])),
                "in_count": len(node.get("in", [])),
                "raw": node
            })

    result = {
        "total_nodes": len(nodes),
        "field_counts": dict(key_counter.most_common()),
        "field_samples": {
            key: samples
            for key, samples in field_samples.items()
        },
        "keyword_hits": keyword_hits[:300]
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Start Node Inspection 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("Top Fields")
    print("=" * 80)
    for key, count in key_counter.most_common(40):
        print(f"{key:30} {count}")

    print()
    print("Keyword Hits Sample")
    print("=" * 80)

    for row in keyword_hits[:80]:
        print(
            f"{row['id']} | {row['name']} | "
            f"keywords={row['matched_keywords']} | "
            f"asc={row['ascendancyName']} | "
            f"isRoot={row['isRoot']}"
        )


if __name__ == "__main__":
    main()