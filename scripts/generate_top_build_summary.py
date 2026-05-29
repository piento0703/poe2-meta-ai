import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BUILDS_PATH = ROOT / "data" / "meta" / "generated_builds_filtered.json"
OUT_PATH = ROOT / "data" / "meta" / "top_build_summary.md"


def load_json(path):
    if not path.exists():
        raise FileNotFoundError(f"missing file: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"저장 완료: {path}")


def fmt_uniques(uniques):
    if not uniques:
        return "없음"

    return ", ".join(u.get("name", "") for u in uniques[:5])


def fmt_supports(supports):
    if not supports:
        return "없음"

    return ", ".join(supports[:6])


def build_one_line_reason(build):
    archetype = build.get("archetype_label_ko", "")
    supports = build.get("recommended_supports", [])
    uniques = build.get("recommended_uniques", [])

    reasons = []

    if archetype:
        reasons.append(f"{archetype} 구조")

    if len(supports) >= 6:
        reasons.append("6링크 후보 충분")

    if len(uniques) >= 3:
        reasons.append("유니크 연계 우수")

    if build.get("validity_penalty", 0) == 0:
        reasons.append("유효성 패널티 없음")

    return " / ".join(reasons) if reasons else "추가 검증 필요"


def generate_summary(builds, limit=10):
    lines = []

    lines.append("# PoE2 Meta AI TOP 10 빌드 요약")
    lines.append("")
    lines.append("이 문서는 필터링된 빌드 후보 중 상위 10개를 빠르게 비교하기 위한 요약 리포트다.")
    lines.append("")
    lines.append("| 순위 | 빌드명 | 점수 | 메인 스킬 | 아키타입 | 추천 보조젬 | 추천 유니크 | 한 줄 평가 |")
    lines.append("|---:|---|---:|---|---|---|---|---|")

    for idx, build in enumerate(builds[:limit], start=1):
        lines.append(
            "| {rank} | {build_name} | {score} | {main_skill} | {archetype} | {supports} | {uniques} | {reason} |".format(
                rank=idx,
                build_name=build.get("build_name", ""),
                score=build.get("build_score", 0),
                main_skill=build.get("main_skill", ""),
                archetype=build.get("archetype_label_ko", ""),
                supports=fmt_supports(build.get("recommended_supports", [])),
                uniques=fmt_uniques(build.get("recommended_uniques", [])),
                reason=build_one_line_reason(build),
            )
        )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 해석 기준")
    lines.append("")
    lines.append("- 점수는 스킬·보조젬·패시브·유니크 태그 중첩도 기반")
    lines.append("- 유효성 패널티가 반영된 최종 점수 기준 정렬")
    lines.append("- 한 줄 평가는 아키타입, 6링크 후보 수, 유니크 연계 수를 기반으로 자동 생성")

    return "\n".join(lines)


def main():
    builds = load_json(BUILDS_PATH)

    print(f"loaded builds: {len(builds)}")

    summary = generate_summary(builds, limit=10)

    save_text(OUT_PATH, summary)

    print("top summary builds: 10")


if __name__ == "__main__":
    main()