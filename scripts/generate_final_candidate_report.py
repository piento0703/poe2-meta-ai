import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "meta" / "best_class_for_cluster.json"
OUT_PATH = ROOT / "data" / "meta" / "final_candidate_report.md"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def tier(score, avg_dist):
    if score >= 28 and avg_dist <= 12:
        return "S"
    if score >= 22 and avg_dist <= 16:
        return "A+"
    if score >= 16 and avg_dist <= 24:
        return "A"
    if score >= 10:
        return "B"
    return "C"


def risk_label(avg_dist):
    if avg_dist <= 10:
        return "LOW"
    if avg_dist <= 16:
        return "MEDIUM"
    if avg_dist <= 24:
        return "HIGH"
    return "VERY HIGH"


def write_candidate(lines, idx, row):
    best = row.get("best_class")

    if not best:
        return

    score = best["class_efficiency_score"]
    avg_dist = best["avg_distance_to_core_passives"]

    lines.append(f"## {idx}. [{tier(score, avg_dist)}] {row['cluster']}")
    lines.append("")
    lines.append(f"- Recommended Class: **{best['classLabel']}**")
    lines.append(f"- Class Efficiency Score: `{score}`")
    lines.append(f"- Avg Distance to Core Passives: `{avg_dist}`")
    lines.append(f"- Route Risk: `{risk_label(avg_dist)}`")
    lines.append(f"- Distance Adjusted Archetype Score: `{row['distance_adjusted_score']}`")
    lines.append("")

    lines.append("### Core Skills")
    lines.append("")
    for s in row.get("top_skills", [])[:5]:
        lines.append(f"- {s['skill']} — `{s['score']}`")

    lines.append("")
    lines.append("### Core Passives")
    lines.append("")
    for p in row.get("top_passives", [])[:8]:
        lines.append(f"- {p['passive']} — `{p['score']}`")

    lines.append("")
    lines.append("### Class Ranking")
    lines.append("")
    for c in row.get("class_rankings", [])[:6]:
        lines.append(
            f"- {c['classLabel']} — avg `{c['avg_distance_to_core_passives']}`, "
            f"eff `{c['efficiency']}`, score `{c['class_efficiency_score']}`"
        )

    lines.append("")


def main():
    data = load_json(INPUT_PATH)

    candidates = [
        row for row in data
        if row.get("best_class")
    ]

    candidates.sort(
        key=lambda x: x["best_class"]["class_efficiency_score"],
        reverse=True
    )

    lines = []

    lines.append("# PoE2 0.5 Final Build Candidate Report")
    lines.append("")
    lines.append("Generated from:")
    lines.append("")
    lines.append("- skill-passive synergy")
    lines.append("- core tag co-occurrence")
    lines.append("- central passive frequency")
    lines.append("- passive distance weighting")
    lines.append("- class start distance optimization")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("# Top Build Candidates")
    lines.append("")

    for i, row in enumerate(candidates[:30], 1):
        write_candidate(lines, i, row)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Final Candidate Report 생성 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP Final Build Candidates")
    print("=" * 100)

    for i, row in enumerate(candidates[:20], 1):
        best = row["best_class"]
        score = best["class_efficiency_score"]
        avg_dist = best["avg_distance_to_core_passives"]

        print(
            f"{i:02}. [{tier(score, avg_dist)}] "
            f"{row['cluster']} | "
            f"class={best['classLabel']} | "
            f"avg_dist={avg_dist} | "
            f"class_score={score}"
        )


if __name__ == "__main__":
    main()