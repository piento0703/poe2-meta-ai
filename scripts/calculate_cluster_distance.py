import json
from pathlib import Path
from collections import deque, defaultdict

ROOT = Path(__file__).resolve().parents[1]

PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
CLUSTER_PASSIVE_PATH = ROOT / "data" / "meta" / "cluster_passive_rankings.json"

OUT_PATH = ROOT / "data" / "meta" / "cluster_distance_scores.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def node_name(node):
    return node.get("name") or node.get("dn") or ""


def build_graph(nodes):
    graph = defaultdict(set)

    for node_id, node in nodes.items():
        for out_id in node.get("out", []):
            graph[str(node_id)].add(str(out_id))
            graph[str(out_id)].add(str(node_id))

        for in_id in node.get("in", []):
            graph[str(node_id)].add(str(in_id))
            graph[str(in_id)].add(str(node_id))

    return graph


def build_name_to_ids(nodes):
    name_to_ids = defaultdict(list)

    for node_id, node in nodes.items():
        name = node_name(node)

        if name:
            name_to_ids[name].append(str(node_id))

    return name_to_ids


def shortest_distance(graph, start_ids, target_ids, max_depth=30):
    targets = set(target_ids)
    visited = set()
    q = deque()

    for sid in start_ids:
        q.append((sid, 0))
        visited.add(sid)

    while q:
        current, dist = q.popleft()

        if current in targets:
            return dist

        if dist >= max_depth:
            continue

        for nxt in graph[current]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, dist + 1))

    return None


def average_pair_distance(graph, passive_names, name_to_ids):
    distances = []

    valid_names = [
        name for name in passive_names
        if name in name_to_ids
    ]

    for i in range(len(valid_names)):
        for j in range(i + 1, len(valid_names)):
            a = valid_names[i]
            b = valid_names[j]

            dist = shortest_distance(
                graph,
                name_to_ids[a],
                name_to_ids[b]
            )

            if dist is not None:
                distances.append(dist)

    if not distances:
        return None, []

    return sum(distances) / len(distances), distances


def distance_multiplier(avg_distance):
    if avg_distance is None:
        return 0.5

    if avg_distance <= 3:
        return 1.25

    if avg_distance <= 5:
        return 1.1

    if avg_distance <= 8:
        return 1.0

    if avg_distance <= 12:
        return 0.85

    if avg_distance <= 18:
        return 0.65

    return 0.45


def main():
    passive_data = load_json(PASSIVE_PATH)
    clusters = load_json(CLUSTER_PASSIVE_PATH)

    nodes = passive_data["nodes"]
    graph = build_graph(nodes)
    name_to_ids = build_name_to_ids(nodes)

    results = []

    for cluster in clusters:
        top_passive_names = [
            p["passive"]
            for p in cluster.get("top_passives", [])[:8]
        ]

        avg_dist, distances = average_pair_distance(
            graph,
            top_passive_names,
            name_to_ids
        )

        multiplier = distance_multiplier(avg_dist)
        adjusted_score = cluster["cluster_score"] * multiplier

        results.append({
            "cluster": cluster["cluster"],
            "tags": cluster["tags"],
            "original_cluster_score": cluster["cluster_score"],
            "avg_passive_distance": round(avg_dist, 2) if avg_dist is not None else None,
            "distance_multiplier": multiplier,
            "distance_adjusted_score": round(adjusted_score, 2),
            "top_passives": cluster.get("top_passives", [])[:8],
            "top_skills": cluster.get("top_skills", [])[:8],
            "raw_distances": distances
        })

    results.sort(
        key=lambda x: x["distance_adjusted_score"],
        reverse=True
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Cluster Distance Weighting 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP Distance-Adjusted Archetypes")
    print("=" * 100)

    for i, row in enumerate(results[:30], 1):
        print(
            f"{i:02}. {row['cluster']} | "
            f"original={row['original_cluster_score']} | "
            f"avg_dist={row['avg_passive_distance']} | "
            f"multi={row['distance_multiplier']} | "
            f"adjusted={row['distance_adjusted_score']}"
        )

        print("    Top Passives:")
        for p in row["top_passives"][:5]:
            print(f"      - {p['passive']} | {p['score']} | hits={p['hits']}")

        print()


if __name__ == "__main__":
    main()