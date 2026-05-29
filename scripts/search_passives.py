import json
from pathlib import Path

DATA_PATH = Path("data/passive/data.json")

KEYWORDS = [
    "lightning",
    "shock",
    "projectile",
    "repeat",
    "charge",
    "power charge",
    "gain",
    "extra",
    "transformed",
    "shape",
    "spirit",
    "melee",
    "area",
    "critical",
]

with DATA_PATH.open("r", encoding="utf-8") as f:
    data = json.load(f)

nodes = data["nodes"]

print(f"전체 노드 수: {len(nodes)}")
print("=" * 80)

for keyword in KEYWORDS:
    results = []

    for node_id, node in nodes.items():
        name = str(node.get("name", ""))
        stats = node.get("stats", [])

        if not name and not stats:
            continue

        stats_text = " ".join(map(str, stats))
        search_text = f"{name} {stats_text}".lower()

        if keyword.lower() in search_text:
            results.append({
                "id": node_id,
                "skill": node.get("skill"),
                "name": name,
                "stats": stats,
                "out": node.get("out", []),
                "in": node.get("in", []),
            })

    print(f"\n[{keyword}] 검색 결과: {len(results)}개")
    print("-" * 80)

    for item in results[:20]:
        print(f"Node ID: {item['id']}")
        print(f"Skill ID: {item['skill']}")
        print(f"Name: {item['name']}")
        for stat in item["stats"]:
            print(f" - {stat}")
        print(f"Connected out: {item['out']}")
        print()