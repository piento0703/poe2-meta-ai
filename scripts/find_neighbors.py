import json
from pathlib import Path
from collections import deque

DATA_PATH = Path("data/passive/data.json")

TARGET_NAME = "Spirit of the Wyvern"
MAX_DEPTH = 2

IMPORTANT_KEYWORDS = [
    "gain",
    "extra",
    "lightning",
    "elemental",
    "critical",
    "crit",
    "skill speed",
    "attack",
    "melee",
    "projectile",
    "shapeshift",
    "charge",
    "power charge",
    "spirit",
]

with DATA_PATH.open("r", encoding="utf-8") as f:
    data = json.load(f)

nodes = data["nodes"]


def node_text(node):
    name = str(node.get("name", ""))
    stats = " ".join(map(str, node.get("stats", [])))
    return f"{name} {stats}".lower()


def get_connections(node):
    connected = set()
    for nid in node.get("out", []):
        connected.add(str(nid))
    for nid in node.get("in", []):
        connected.add(str(nid))
    return connected


def find_node_by_name(name):
    matches = []
    for node_id, node in nodes.items():
        if node.get("name") == name:
            matches.append((node_id, node))
    return matches


matches = find_node_by_name(TARGET_NAME)

if not matches:
    print(f"노드를 찾지 못함: {TARGET_NAME}")
    exit()

target_id, target_node = matches[0]

visited = set()
queue = deque()
results = []

queue.append((target_id, 0))
visited.add(target_id)

while queue:
    current_id, depth = queue.popleft()
    node = nodes.get(str(current_id))

    if not node:
        continue

    text = node_text(node)
    matched_keywords = [
        keyword for keyword in IMPORTANT_KEYWORDS
        if keyword.lower() in text
    ]

    results.append({
        "id": current_id,
        "depth": depth,
        "name": node.get("name", ""),
        "stats": node.get("stats", []),
        "keywords": matched_keywords,
    })

    if depth >= MAX_DEPTH:
        continue

    for next_id in get_connections(node):
        if next_id not in visited:
            visited.add(next_id)
            queue.append((next_id, depth + 1))


print("=" * 100)
print(f"타겟: {TARGET_NAME}")
print(f"Node ID: {target_id}")
print(f"탐색 반경: {MAX_DEPTH}")
print(f"발견 노드 수: {len(results)}")
print("=" * 100)

for item in sorted(results, key=lambda x: (x["depth"], x["name"])):
    print(f"\n[Depth {item['depth']}] Node ID: {item['id']}")
    print(f"Name: {item['name']}")

    if item["keywords"]:
        print(f"Keywords: {', '.join(item['keywords'])}")

    for stat in item["stats"]:
        print(f" - {stat}")