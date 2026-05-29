import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLUSTER_PATH = ROOT / "data" / "meta" / "cluster_passive_rankings.json"
CENTRAL_PASSIVES_PATH = ROOT / "data" / "meta" / "central_passives.json"
TAG_GRAPH_PATH = ROOT / "data" / "meta" / "core_tag_graph_edges.json"

OUT_PATH = ROOT / "data" / "meta" / "meta_report.md"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def tier_label(score):
    if score >= 700:
        return "S"
    if score >= 550:
        return "A+"
    if score >= 430:
        return "A"
    if score >= 320:
        return "B"
    return "C"


def write_cluster_section(lines, clusters):
    lines.append("# PoE2 0.5 Auto Meta Report")
    lines.append("")
    lines.append("## 1. Top Archetype Clusters")
    lines.append("")

    for i, row in enumerate(clusters[:20], 1):
        tier = tier_label(row["cluster_score"])

        lines.append(f"### {i}. [{tier}] {row['cluster']}")
        lines.append("")
        lines.append(f"- Cluster Score: `{row['cluster_score']}`")
        lines.append(f"- Skill Count: `{row['skill_count']}`")
        lines.append(f"- Tags: `{', '.join(row['tags'])}`")
        lines.append("")

        lines.append("**Top Skills**")
        lines.append("")
        for s in row["top_skills"][:5]:
            lines.append(f"- {s['skill']} — `{s['score']}`")

        lines.append("")
        lines.append("**Top Passives**")
        lines.append("")
        for p in row["top_passives"][:8]:
            lines.append(
                f"- {p['passive']} — score `{p['score']}`, hits `{p['hits']}`, "
                f"tags `{', '.join(p['tags'])}`"
            )

        lines.append("")


def write_passive_section(lines, passives):
    lines.append("---")
    lines.append("")
    lines.append("## 2. Central Passive Hubs")
    lines.append("")

    for i, p in enumerate(passives[:30], 1):
        lines.append(
            f"{i}. **{p['passive']}** — score `{p['score']}`, "
            f"hits `{p['hits']}`, tags `{', '.join(p['tags'])}`"
        )


def write_tag_graph_section(lines, edges):
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. Core Meta Tag Connections")
    lines.append("")

    for i, e in enumerate(edges[:30], 1):
        examples = ", ".join(e.get("examples", [])[:3])
        lines.append(
            f"{i}. `{e['source']}` ↔ `{e['target']}` = `{e['weight']}`"
        )
        if examples:
            lines.append(f"   - examples: {examples}")


def write_final_implications(lines, clusters, passives, edges):
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. Current Meta Implications")
    lines.append("")

    top_cluster_names = [c["cluster"] for c in clusters[:10]]
    top_passive_names = [p["passive"] for p in passives[:10]]

    lines.append("### Strongest Signals")
    lines.append("")
    lines.append("Based on current skill-passive synergy data, the strongest repeated structures are:")
    lines.append("")

    for name in top_cluster_names[:6]:
        lines.append(f"- {name}")

    lines.append("")
    lines.append("### Central Passive Candidates")
    lines.append("")

    for name in top_passive_names[:8]:
        lines.append(f"- {name}")

    lines.append("")
    lines.append("### Working Tier Hypothesis")
    lines.append("")
    lines.append("- **S Tier Candidate:** Tri-Element Trigger Duration")
    lines.append("- **S Tier Candidate:** Projectile Duration Grenade")
    lines.append("- **A+ Candidate:** Fire Meta Trigger Crit")
    lines.append("- **A+ Candidate:** Shapeshift Trigger Duration")
    lines.append("- **A Candidate:** Cold Shapeshift Werewolf")
    lines.append("- **A Candidate:** Fire Wyvern Projectile")


def main():
    clusters = load_json(CLUSTER_PATH)
    passives = load_json(CENTRAL_PASSIVES_PATH)
    edges = load_json(TAG_GRAPH_PATH)

    lines = []

    write_cluster_section(lines, clusters)
    write_passive_section(lines, passives)
    write_tag_graph_section(lines, edges)
    write_final_implications(lines, clusters, passives, edges)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Meta Report 생성 완료")
    print(f"저장 위치: {OUT_PATH}")


if __name__ == "__main__":
    main()