import json
from pathlib import Path
from collections import defaultdict, deque

ROOT = Path(__file__).resolve().parents[1]

PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
DISTANCE_PATH = ROOT / "data" / "meta" / "cluster_distance_scores.json"

OUT_PATH = ROOT / "data" / "meta" / "start_region_rankings.json"


START_KEYWORDS = {
    "Strength": ["Strength"],
    "Dexterity": ["Dexterity"],
    "Intelligence": ["Intelligence"],
    "Str/Dex": ["Strength", "Dexterity"],
    "Dex/Int": ["Dexterity", "Intelligence"],
    "Str/Int": ["Strength", "Intelligence"]
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def node_name(node):
    return node.get("name") or node.get("dn") or ""


def node_text(node):
    parts = []

    for key in ["name", "dn", "sd", "stats", "ascendancyName"]:
        value = node.get(key)

        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, list):
            parts.extend(str(v) for v in value)
        elif isinstance(value, dict):
            parts.extend(str(v) for v in value.values())

    return " ".join(parts)


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


def build_name_to_ids(nodes):
    result = defaultdict(list)

    for node_id, node in nodes.items():
        name = node_name(node)
        if name:
            result[name].append(str(node_id))

    return result


def find_start_nodes(nodes):
    starts = defaultdict(list)

    for node_id, node in nodes.items():
        text = node_text(node)

        if node.get("isRoot") or "Starting" in text or "start" in text.lower():
            for label, keywords in START_KEYWORDS.items():
                if all(k.lower() in text.lower() for k in keywords):
                    starts[label].append(str(node_id))

    # fallback: classStartIndex / group / root 비슷한 필드가 없을 수 있어
    # 너무 비면 전체 루트성 노드 후보를 별도 처리
    if not any(starts.values()):
        for node_id, node in nodes.items():
            text = node_text(node).lower()
            name = node_name(node).lower()

            if "strength" in text or "strength" in name:
                starts["Strength"].append(str(node_id))
            if "dexterity" in text or "dexterity" in name:
                starts["Dexterity"].append(str(node_id))
            if "intelligence" in text or "intelligence" in name:
                starts["Intelligence"].append(str(node_id))

    return starts


def shortest_distance(graph, start_ids, target_ids, max_depth=80):
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


def avg_distance_to_passives(graph, start_ids, passive_names, name_to_ids):
    distances = []

    for name in passive_names:
        target_ids = name_to_ids.get(name)

        if not target_ids:
            continue

        dist = shortest_distance(graph, start_ids, target_ids)

        if dist is not None:
            distances.append(dist)

    if not distances:
        return None, []

    return sum(distances) / len(distances), distances


def main():
    passive_data = load_json(PASSIVE_PATH)
    clusters = load_json(DISTANCE_PATH)

    nodes = passive_data["nodes"]

    graph = build_graph(nodes)
    name_to_ids = build_name_to_ids(nodes)
    start_nodes = find_start_nodes(nodes)

    results = []

    for cluster in clusters[:50]:
        passive_names = [
            p["passive"]
            for p in cluster.get("top_passives", [])[:8]
        ]

        region_scores = []

        for region, start_ids in start_nodes.items():
            if not start_ids:
                continue

            avg_dist, raw = avg_distance_to_passives(
                graph,
                start_ids,
                passive_names,
                name_to_ids
            )

            if avg_dist is None:
                continue

            region_scores.append({
                "region": region,
                "avg_distance_to_core_passives": round(avg_dist, 2),
                "raw_distances": raw,
                "start_node_count": len(start_ids)
            })

        region_scores.sort(
            key=lambda x: x["avg_distance_to_core_passives"]
        )

        best = region_scores[0] if region_scores else None

        results.append({
            "cluster": cluster["cluster"],
            "tags": cluster["tags"],
            "distance_adjusted_score": cluster["distance_adjusted_score"],
            "avg_passive_distance": cluster["avg_passive_distance"],
            "best_region": best,
            "region_rankings": region_scores[:10],
            "top_passives": cluster.get("top_passives", [])[:8],
            "top_skills": cluster.get("top_skills", [])[:5]
        })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Start Region Ranking 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP Archetype Start Regions")
    print("=" * 100)

    for i, row in enumerate(results[:30], 1):
        best = row["best_region"]

        if best:
            best_text = (
                f"{best['region']} "
                f"(avg={best['avg_distance_to_core_passives']})"
            )
        else:
            best_text = "UNKNOWN"

        print(
            f"{i:02}. {row['cluster']} | "
            f"score={row['distance_adjusted_score']} | "
            f"best={best_text}"
        )

        for r in row["region_rankings"][:5]:
            print(
                f"    - {r['region']} | "
                f"avg={r['avg_distance_to_core_passives']} | "
                f"starts={r['start_node_count']}"
            )

        print()


if __name__ == "__main__":
    main()