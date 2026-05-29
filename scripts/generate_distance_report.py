import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "meta" / "cluster_distance_scores.json"
OUT_PATH = ROOT / "data" / "meta" / "distance_report.md"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def tier(score):
    if score >= 700:
        return "S"
    if score >= 520:
        return "A+"
    if score >= 380:
        return "A"
    if score >= 260:
        return "B"
    return "C"


def distance_label(avg_dist):
    if avg_dist is None:
        return "UNKNOWN"
    if avg_dist <= 5:
        return "COMPACT"
    if avg_dist <= 8:
        return "NORMAL"
    if avg_dist <= 12:
        return "SPREAD"
    return "TOO FAR"


def write_cluster(lines, idx, row):
    lines.append(f"### {idx}. [{tier(row['distance_adjusted_score'])}] {row['cluster']}")
    lines.append("")
    lines.append(f"- Original Score: `{row['original_cluster_score']}`")
    lines.append(f"- Distance Adjusted Score: `{row['distance_adjusted_score']}`")
    lines.append(f"- Average Passive Distance: `{row['avg_passive_distance']}`")
    lines.append(f"- Distance Label: `{distance_label(row['avg_passive_distance'])}`")
    lines.append(f"- Multiplier: `{row['distance_multiplier']}`")
    lines.append("")

    lines.append("**Top Passives**")
    lines.append("")
    for p in row["top_passives"][:8]:
        lines.append(f"- {p['passive']} — score `{p['score']}`, hits `{p['hits']}`")

    lines.append("")
    lines.append("**Top Skills**")
    lines.append("")
    for s in row["top_skills"][:5]:
        lines.append(f"- {s['skill']} — `{s['score']}`")

    lines.append("")


def main():
    data = load_json(INPUT_PATH)

    by_original = sorted(
        data,
        key=lambda x: x["original_cluster_score"],
        reverse=True
    )

    by_adjusted = sorted(
        data,
        key=lambda x: x["distance_adjusted_score"],
        reverse=True
    )

    compact = [
        row for row in by_adjusted
        if row["avg_passive_distance"] is not None
        and row["avg_passive_distance"] <= 5
    ]

    spread_penalty = [
        row for row in by_original[:30]
        if row["distance_multiplier"] < 1.0
    ]

    survivors = [
        row for row in by_adjusted[:30]
        if row["distance_adjusted_score"] >= 380
    ]

    lines = []

    lines.append("# PoE2 0.5 Distance Adjusted Meta Report")
    lines.append("")
    lines.append("## 1. Distance Adjusted Top Archetypes")
    lines.append("")

    for i, row in enumerate(by_adjusted[:20], 1):
        write_cluster(lines, i, row)

    lines.append("---")
    lines.append("")
    lines.append("## 2. Compact High-Efficiency Archetypes")
    lines.append("")

    if compact:
        for i, row in enumerate(compact[:15], 1):
            lines.append(
                f"{i}. **{row['cluster']}** — adjusted `{row['distance_adjusted_score']}`, "
                f"avg_dist `{row['avg_passive_distance']}`"
            )
    else:
        lines.append("- No compact archetypes found with current top passive set.")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. High Score But Distance-Penalized Archetypes")
    lines.append("")

    for i, row in enumerate(spread_penalty[:15], 1):
        lines.append(
            f"{i}. **{row['cluster']}** — original `{row['original_cluster_score']}` → "
            f"adjusted `{row['distance_adjusted_score']}`, "
            f"avg_dist `{row['avg_passive_distance']}`"
        )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 4. Survivors After Distance Penalty")
    lines.append("")

    for i, row in enumerate(survivors[:20], 1):
        lines.append(
            f"{i}. **[{tier(row['distance_adjusted_score'])}] {row['cluster']}** — "
            f"adjusted `{row['distance_adjusted_score']}`, "
            f"distance `{distance_label(row['avg_passive_distance'])}`"
        )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Distance Report 생성 완료")
    print(f"저장 위치: {OUT_PATH}")

    print()
    print("Distance Survivors")
    print("=" * 80)

    for i, row in enumerate(survivors[:20], 1):
        print(
            f"{i:02}. [{tier(row['distance_adjusted_score'])}] "
            f"{row['cluster']} | "
            f"adjusted={row['distance_adjusted_score']} | "
            f"avg_dist={row['avg_passive_distance']} | "
            f"{distance_label(row['avg_passive_distance'])}"
        )


if __name__ == "__main__":
    main()