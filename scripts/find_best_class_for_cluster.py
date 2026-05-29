import json
from pathlib import Path
from collections import defaultdict, deque

ROOT = Path(__file__).resolve().parents[1]

PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
DISTANCE_PATH = ROOT / "data" / "meta" / "cluster_distance_scores.json"

OUT_PATH = ROOT / "data" / "meta" / "best_class_for_cluster.json"


CLASS_LABELS = {
    0: "Marauder",
    1: "Witch",
    2: "Ranger",
    3: "Duelist",
    4: "Shadow",
    5: "Templar",
    6: "Marauder",
    7: "Witch",
    8: "Ranger",
    9: "Duelist",
    10: "Shadow",
    11: "Templar"
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def node_name(node):
    return node.get("name") or node.get("dn") or ""


def build_graph(nodes):
    graph = defaultdict(set)

    for node_id, node in nodes.items():
        node_id = str(node_id)

        for out_id in node.get("out", []):
            out_id = str(out_id)
            graph[node_id].add(out_id)
            graph[out_id].add(node_id)

        for in_id in node.get("in", []):
            in_id = str(in_id)
            graph[node_id].add(in_id)
            graph[in_id].add(node_id)

    return graph


def normalize_class_start_indices(value):
    if value is None:
        return []

    if isinstance(value, int):
        return [value]

    if isinstance(value, float):
        return [int(value)]

    if isinstance(value, str):
        try:
            return [int(value)]
        except ValueError:
            return []

    if isinstance(value, list):
        result = []

        for item in value:
            try:
                result.append(int(item))
            except (TypeError, ValueError):
                continue

        return result

    return []


def get_class_starts(nodes):
    starts = {}

    for node_id, node in nodes.items():
        if "classStartIndex" not in node:
            continue

        indices = normalize_class_start_indices(
            node.get("classStartIndex")
        )

        for idx in indices:
            starts[idx] = {
                "id": str(node_id),
                "label": CLASS_LABELS.get(idx, f"Class {idx}"),
                "name": node_name(node),
                "x": node.get("x"),
                "y": node.get("y"),
                "raw_classStartIndex": node.get("classStartIndex")
            }

    return starts


def build_name_to_ids(nodes):
    result = defaultdict(list)

    for node_id, node in nodes.items():
        name = node_name(node)

        if name:
            result[name].append(str(node_id))

    return result


def shortest_distance(graph, start_id, target_ids, max_depth=120):
    targets = set(target_ids)

    visited = {start_id}

    q = deque([(start_id, 0)])

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


def class_distance_to_passives(
    graph,
    class_start_id,
    passive_names,
    name_to_ids
):
    distances = []

    for passive_name in passive_names:
        target_ids = name_to_ids.get(passive_name, [])

        if not target_ids:
            continue

        dist = shortest_distance(
            graph,
            class_start_id,
            target_ids
        )

        if dist is not None:
            distances.append({
                "passive": passive_name,
                "distance": dist
            })

    if not distances:
        return None, []

    avg = sum(
        d["distance"]
        for d in distances
    ) / len(distances)

    return avg, distances


def efficiency_label(avg_distance):
    if avg_distance is None:
        return "UNKNOWN"

    if avg_distance <= 10:
        return "EXCELLENT"

    if avg_distance <= 16:
        return "GOOD"

    if avg_distance <= 24:
        return "OK"

    if avg_distance <= 34:
        return "EXPENSIVE"

    return "TOO FAR"


def main():
    passive_data = load_json(PASSIVE_PATH)
    clusters = load_json(DISTANCE_PATH)

    nodes = passive_data["nodes"]

    graph = build_graph(nodes)

    class_starts = get_class_starts(nodes)

    name_to_ids = build_name_to_ids(nodes)

    results = []

    for cluster in clusters[:80]:

        passive_names = [
            p["passive"]
            for p in cluster.get("top_passives", [])[:8]
        ]

        class_rankings = []

        for idx, start in class_starts.items():

            avg_dist, raw = class_distance_to_passives(
                graph,
                start["id"],
                passive_names,
                name_to_ids
            )

            if avg_dist is None:
                continue

            score = (
                cluster["distance_adjusted_score"]
                / max(avg_dist, 1)
            )

            class_rankings.append({
                "classStartIndex": idx,
                "classLabel": start["label"],
                "startNodeName": start["name"],
                "startNodeId": start["id"],
                "avg_distance_to_core_passives": round(avg_dist, 2),
                "efficiency": efficiency_label(avg_dist),
                "class_efficiency_score": round(score, 2),
                "raw_distances": raw
            })

        class_rankings.sort(
            key=lambda x: x["class_efficiency_score"],
            reverse=True
        )

        results.append({
            "cluster": cluster["cluster"],
            "tags": cluster["tags"],
            "distance_adjusted_score": cluster["distance_adjusted_score"],
            "avg_passive_distance": cluster["avg_passive_distance"],
            "best_class": (
                class_rankings[0]
                if class_rankings
                else None
            ),
            "class_rankings": class_rankings,
            "top_passives": cluster.get("top_passives", [])[:8],
            "top_skills": cluster.get("top_skills", [])[:5]
        })

    results.sort(
        key=lambda x: (
            x["best_class"]["class_efficiency_score"]
            if x["best_class"]
            else 0
        ),
        reverse=True
    )

    OUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(
            results,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("Best Class For Cluster 분석 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP Class-Optimized Archetypes")
    print("=" * 100)

    for i, row in enumerate(results[:30], 1):

        best = row["best_class"]

        if not best:
            continue

        print(
            f"{i:02}. "
            f"{row['cluster']} | "
            f"best={best['classLabel']} | "
            f"avg_dist={best['avg_distance_to_core_passives']} | "
            f"eff={best['efficiency']} | "
            f"class_score={best['class_efficiency_score']}"
        )

        print("    Top Passives:")

        for p in row["top_passives"][:5]:
            print(
                f"      - "
                f"{p['passive']} | "
                f"{p['score']}"
            )

        print()


if __name__ == "__main__":
    main()