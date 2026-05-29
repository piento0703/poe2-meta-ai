import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MATCH_PATH = ROOT / "data" / "supports" / "support_archetype_matches.json"
OUT_PATH = ROOT / "data" / "supports" / "support_report.md"


def main():
    data = json.load(open(MATCH_PATH, encoding="utf-8"))

    lines = []
    lines.append("# Support Gem Archetype Report")
    lines.append("")
    lines.append("PoE2 0.5 support gem 자동 매칭 결과")
    lines.append("")

    for archetype, matches in data.items():
        lines.append(f"## {archetype}")
        lines.append("")

        lines.append("| Rank | Support Gem | Tier | Score | Matched Tags | All Tags |")
        lines.append("|---:|---|---:|---:|---|---|")

        for i, m in enumerate(matches[:20], start=1):
            matched = ", ".join(m.get("matched_tags", []))
            tags = ", ".join(m.get("tags", []))

            lines.append(
                f"| {i} | {m['name']} | {m.get('tier', '')} | "
                f"{m['score']} | {matched} | {tags} |"
            )

        lines.append("")
        lines.append("### 1차 해석")
        lines.append("")

        top = matches[:5]

        if top:
            names = ", ".join(m["name"] for m in top)
            lines.append(f"- 상위 후보: {names}")
            lines.append("- 현재 점수는 태그 겹침 기반이므로 실제 성능 확정이 아니라 후보군 선별용이다.")
            lines.append("- 다음 단계에서 MORE/INCREASED, 발동 조건, 연쇄/반복/투사체 수, 지속시간 보정이 필요하다.")
        else:
            lines.append("- 유의미한 보조젬 후보가 탐지되지 않았다.")

        lines.append("")

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")

    print("Support report 생성 완료")
    print(f"저장 위치: {OUT_PATH}")


if __name__ == "__main__":
    main()