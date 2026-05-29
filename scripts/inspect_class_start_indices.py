import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
OUT_PATH = ROOT / "data" / "meta" / "class_start_indices.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def node_name(node):
    return node.get("name") or node.get("dn") or ""


def short_stats(node):
    stats = node.get("stats", [])

    if isinstance(stats, list):
        return stats[:5]

    return stats


def main():
    data = load_json(PASSIVE_PATH)
    nodes = data["nodes"]

    class_starts = []
    ascendancy_starts = []

    for node_id, node in nodes.items():
        if "classStartIndex" in node:
            class_starts.append({
                "id": str(node_id),
                "classStartIndex": node.get("classStartIndex"),
                "name": node_name(node),
                "x": node.get("x"),
                "y": node.get("y"),
                "out": node.get("out", []),
                "in": node.get("in", []),
                "stats": short_stats(node),
                "raw_keys": list(node.keys())
            })

        if node.get("isAscendancyStart"):
            ascendancy_starts.append({
                "id": str(node_id),
                "name": node_name(node),
                "ascendancyId": node.get("ascendancyId"),
                "x": node.get("x"),
                "y": node.get("y"),
                "out": node.get("out", []),
                "in": node.get("in", []),
                "stats": short_stats(node),
                "raw_keys": list(node.keys())
            })

    class_starts.sort(key=lambda x: x["classStartIndex"])
    ascendancy_starts.sort(key=lambda x: (x.get("ascendancyId") or 999, x["name"]))

    result = {
        "class_starts": class_starts,
        "ascendancy_starts": ascendancy_starts
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Class Start Index Inspection 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("Class Starts")
    print("=" * 80)

    for row in class_starts:
        print(
            f"index={row['classStartIndex']} | "
            f"id={row['id']} | "
            f"name={row['name']} | "
            f"x={row['x']} | y={row['y']}"
        )
        print(f"    stats={row['stats']}")
        print(f"    out={row['out']}")
        print()

    print("Ascendancy Starts")
    print("=" * 80)

    for row in ascendancy_starts:
        print(
            f"ascId={row['ascendancyId']} | "
            f"id={row['id']} | "
            f"name={row['name']} | "
            f"x={row['x']} | y={row['y']}"
        )
        print(f"    stats={row['stats']}")
        print()


if __name__ == "__main__":
    main()