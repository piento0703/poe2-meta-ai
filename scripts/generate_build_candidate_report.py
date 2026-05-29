import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TRIPLE_PATH = ROOT / "data" / "meta" / "triple_synergy_candidates.json"
OUT_PATH = ROOT / "data" / "meta" / "build_candidate_report.md"


EN_TO_KO = {
    "projectile": "투사체",
    "trigger": "발동",
    "duration": "지속시간",
    "aoe": "효과 범위",
    "fire": "화염",
    "cold": "냉기",
    "lightning": "번개",
    "melee": "근접",
    "slam": "강타",
    "minion": "소환수",
    "totem": "토템",
    "grenade": "유탄",
    "chaos": "카오스",
    "payoff": "청산",
    "shapeshift": "형태 변환",
    "chain": "연쇄",
    "spell": "주문",
    "attack": "공격",
    "physical": "물리",
    "buff": "버프",
    "conditional": "조건부",
    "mark": "징표",
    "curse": "저주",
    "storm": "폭풍",

    "consume_charge": "충전 소모",
    "gain_as_extra": "추가 피해 획득",
    "meta_energy": "메타 에너지",
    "crit": "치명타",
}


ARCHETYPE_KO = {
    "Trigger Chain Projectile": "발동 연쇄 투사체",
    "Projectile Grenade": "투사체 유탄",
    "Shapeshift Melee": "형태 변환 근접",
    "Persistent Minion": "지속 소환수",
    "Fire Trigger": "화염 발동",
    "Cold Duration": "냉기 지속시간",
    "Lightning Chain": "번개 연쇄",
    "Hybrid": "혼합형",
}


def to_ko_tags(tags):
    return [EN_TO_KO.get(tag, tag) for tag in tags]


def format_passive(p):
    if not isinstance(p, dict):
        return str(p)

    name = p.get("passive_name", "Unknown")
    score = p.get("score", "")
    overlap = to_ko_tags(p.get("overlap", []))
    passive_tags = to_ko_tags(p.get("passive_tags", []))

    parts = [f"**{name}**"]

    if score != "":
        parts.append(f"점수 {score}")

    if overlap:
        parts.append(f"겹침: {', '.join(overlap)}")

    if passive_tags:
        parts.append(f"태그: {', '.join(passive_tags)}")

    return " / ".join(parts)


def classify_build(tags_ko):
    tags = set(tags_ko)

    if {"발동", "연쇄", "투사체"} <= tags:
        return "Trigger Chain Projectile"

    if {"유탄", "투사체"} <= tags:
        return "Projectile Grenade"

    if {"형태 변환", "근접"} <= tags:
        return "Shapeshift Melee"

    if {"소환수", "지속시간"} <= tags:
        return "Persistent Minion"

    if {"화염", "발동"} <= tags:
        return "Fire Trigger"

    if {"냉기", "지속시간"} <= tags:
        return "Cold Duration"

    if {"번개", "연쇄"} <= tags:
        return "Lightning Chain"

    return "Hybrid"


def build_summary(entry):
    shared_tags = entry.get("shared_tags_ko")

    if not shared_tags:
        shared_tags = to_ko_tags(entry.get("shared_tags", []))

    archetype = classify_build(shared_tags)
    score = entry["score"]

    if score >= 35:
        tier = "S"
    elif score >= 25:
        tier = "A"
    elif score >= 18:
        tier = "B"
    else:
        tier = "C"

    return archetype, ARCHETYPE_KO.get(archetype, archetype), tier, shared_tags


def main():
    data = json.load(open(TRIPLE_PATH, encoding="utf-8"))

    lines = []

    lines.append("# PoE2 빌드 후보 리포트")
    lines.append("")
    lines.append("자동 생성된 Triple Synergy 기반 빌드 후보")
    lines.append("")

    for i, entry in enumerate(data[:100], start=1):
        archetype, archetype_ko, tier, shared_tags = build_summary(entry)

        lines.append(f"## #{i} {entry['skill']} + {entry['support']}")
        lines.append("")

        lines.append(f"- 티어: **{tier}**")
        lines.append(f"- 아키타입: **{archetype_ko}**")
        lines.append(f"- 총점: **{entry['score']}**")
        lines.append(f"- 기본 점수: {entry['base_score']}")
        lines.append(f"- 패시브 보너스: {entry['passive_bonus']}")
        lines.append("")

        lines.append("### 공통 태그")
        lines.append("")

        for tag in shared_tags:
            lines.append(f"- {tag}")

        lines.append("")

        lines.append("### 핵심 패시브 후보")
        lines.append("")

        for p in entry.get("top_passives", [])[:10]:
            lines.append(f"- {format_passive(p)}")

        lines.append("")
        lines.append("---")
        lines.append("")

    OUT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print("Build candidate report 생성 완료")
    print(f"저장 위치: {OUT_PATH}")


if __name__ == "__main__":
    main()