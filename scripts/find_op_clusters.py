import json
from pathlib import Path
from collections import deque

DATA_PATH = Path("data/passive/data.json")
MAX_DEPTH = 2
TOP_N = 30

KEYWORD_WEIGHTS = {
    "gain": 5,
    "extra": 5,
    "more": 5,
    "lightning": 4,
    "critical": 4,
    "crit": 4,
    "shapeshift": 4,
    "charge": 4,
    "power charge": 5,
    "projectile": 4,
    "melee": 3,
    "attack": 3,
    "skill speed": 3,
    "elemental": 3,
    "shock": 4,
    "duration": 2,
    "reservation": 4,
    "spirit": 4,
    "converted": 5,
    "repeat": 5,
}

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


def scan_cluster(start_id):
    visited = set()
    queue = deque()
    cluster_nodes = []

    visited.add(str(start_id))
    queue.append((str(start_id), 0))

    while queue:
        current_id, depth = queue.popleft()
        node = nodes.get(str(current_id))

        if not node:
            continue

        text = node_text(node)

        node_score = 0
        matched_keywords = []

        for keyword, weight in KEYWORD_WEIGHTS.items():
            if keyword in text:
                node_score += weight
                matched_keywords.append(keyword)

        cluster_nodes.append({
            "id": current_id,
            "depth": depth,
            "name": node.get("name", ""),
            "stats": node.get("stats", []),
            "score": node_score,
            "keywords": matched_keywords,
        })

        if depth >= MAX_DEPTH:
            continue

        for next_id in get_connections(node):
            if next_id not in visited:
                visited.add(next_id)
                queue.append((next_id, depth + 1))

    total_score = sum(item["score"] for item in cluster_nodes)

    # 빈 이름 노드/root 같은 구조 노드는 제외 보정
    named_nodes = [n for n in cluster_nodes if n["name"]]
    if not named_nodes:
        return None

    return {
        "start_id": start_id,
        "start_name": nodes[str(start_id)].get("name", ""),
        "total_score": total_score,
        "node_count": len(cluster_nodes),
        "matched_nodes": [n for n in cluster_nodes if n["score"] > 0],
    }


clusters = []

for node_id, node in nodes.items():
    if not node.get("name"):
        continue

    cluster = scan_cluster(node_id)
    if cluster and cluster["total_score"] > 0:
        clusters.append(cluster)

clusters.sort(key=lambda x: x["total_score"], reverse=True)

print("=" * 100)
print(f"OP 후보 클러스터 TOP {TOP_N}")
print(f"탐색 반경: {MAX_DEPTH}")
print("=" * 100)

for rank, cluster in enumerate(clusters[:TOP_N], start=1):
    print()
    print("=" * 100)
    print(f"#{rank} | Score: {cluster['total_score']} | Start Node: {cluster['start_name']} | Node ID: {cluster['start_id']}")
    print("=" * 100)

    for item in cluster["matched_nodes"]:
        print(f"\n[Depth {item['depth']}] {item['name']} ({item['id']})")
        print(f"Keywords: {', '.join(item['keywords'])}")

        for stat in item["stats"]:
            print(f" - {stat}")