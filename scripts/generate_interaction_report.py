import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "meta" / "build_interaction_analysis.json"
OUT_PATH = ROOT / "data" / "meta" / "interaction_report.md"


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


def fmt_list(items):
    if not items:
        return "- 없음"

    return "\n".join(f"- {item}" for item in items)


def fmt_uniques(uniques):
    if not uniques:
        return "- 없음"

    lines = []

    for unique in uniques[:5]:
        name = unique.get("name", "")
        role = unique.get("role", "")
        score = unique.get("score", 0)
        tags = ", ".join(unique.get("matched_tags_ko", []))

        lines.append(f"- {name} / 역할: {role} / 점수: {score} / 매칭: {tags}")

    return "\n".join(lines)


def fmt_rare_affixes(affixes):
    if not affixes:
        return "- 없음"

    lines = []

    for affix in affixes[:3]:
        name = affix.get("name", "")
        slot = affix.get("slot", "")
        score = affix.get("final_score", 0)
        level = affix.get("power_level", "")
        mechanics = ", ".join(affix.get("mechanics", []))

        lines.append(f"- {name} / 슬롯: {slot} / 점수: {score} / 등급: {level} / 메커니즘: {mechanics}")

    return "\n".join(lines)


def fmt_broken_combos(combos):
    if not combos:
        return "- 없음"

    lines = []

    for combo in combos:
        ko = combo.get("ko", "")
        score = combo.get("score", 0)
        reason = combo.get("reason", "")

        lines.append(f"- {ko} / 점수: {score} / 이유: {reason}")

    return "\n".join(lines)


def infer_build_comment(result):
    level = result.get("interaction_level", "")
    combos = result.get("broken_combos", [])
    mechanics = set(result.get("mechanics", []))

    comments = []

    if "S급" in level:
        comments.append("메타 파괴 후보로 우선 검증 가치가 높음")
    elif "A급" in level:
        comments.append("강력한 OP 후보로 실전 검증 가치가 있음")
    elif "B급" in level:
        comments.append("실전 빌드 후보이나 추가 검증 필요")

    if combos:
        comments.append("Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위")

    if {"extra_projectile", "returning_projectile", "shotgun"}.issubset(mechanics):
        comments.append("투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성")

    if {"gain_as_extra", "conversion"}.issubset(mechanics):
        comments.append("피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능")

    if {"trigger", "crit_scaling"}.issubset(mechanics):
        comments.append("치명타 기반 발동 엔진 후보")

    return comments or ["추가 검증 필요"]


def fmt_result(result, rank):
    build_name = result.get("build_name", "")
    main_skill = result.get("main_skill", "")
    base_score = result.get("base_build_score", 0)
    interaction_score = result.get("interaction_score", 0)
    level = result.get("interaction_level", "")
    archetype = result.get("archetype_label_ko", "")
    mechanics = result.get("mechanics", [])
    supports = result.get("recommended_supports", [])
    uniques = result.get("recommended_uniques", [])
    rare_affixes = result.get("recommended_rare_affixes", [])
    combos = result.get("broken_combos", [])
    comments = infer_build_comment(result)

    return f"""## {rank}. {build_name}

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | {main_skill} |
| 아키타입 | {archetype} |
| 기존 빌드 점수 | {base_score} |
| 상호작용 점수 | {interaction_score} |
| 상호작용 등급 | {level} |

### 감지된 핵심 메커니즘

{fmt_list(mechanics)}

### 추천 보조젬

{fmt_list(supports[:6])}

### 추천 유니크

{fmt_uniques(uniques)}

### 추천 일반/레어 아이템 옵션 후보

{fmt_rare_affixes(rare_affixes)}

### 감지된 Broken Combo

{fmt_broken_combos(combos)}

### 해석

{fmt_list(comments)}

---
"""


def generate_report(results, limit=30):
    lines = []

    lines.append("# PoE2 Meta AI 상호작용 분석 리포트")
    lines.append("")
    lines.append("이 문서는 스킬·보조젬·유니크·일반/레어 아이템 옵션의 메커니즘 상호작용을 기반으로 자동 생성된 리포트다.")
    lines.append("")
    lines.append("## 분석 기준")
    lines.append("")
    lines.append("- 기존 빌드 점수")
    lines.append("- 일반/레어 아이템 옵션 semantic score")
    lines.append("- Broken Combo 감지")
    lines.append("- 메커니즘 밀도")
    lines.append("- 상호작용 점수 기준 정렬")
    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, result in enumerate(results[:limit], start=1):
        lines.append(fmt_result(result, idx))

    return "\n".join(lines)


def main():
    results = load_json(INPUT_PATH)

    print(f"loaded interaction results: {len(results)}")

    report = generate_report(results, limit=30)

    save_text(OUT_PATH, report)

    print(f"interaction report builds: {min(len(results), 30)}")


if __name__ == "__main__":
    main()