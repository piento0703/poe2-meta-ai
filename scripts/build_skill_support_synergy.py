import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILLS_PATH = ROOT / "data" / "skills" / "skills.json"
SUPPORTS_PATH = ROOT / "data" / "supports" / "supports.json"

OUT_PATH = ROOT / "data" / "meta" / "skill_support_synergy.json"


TAG_NORMALIZE = {
    "투사체": "projectile",
    "Projectile": "projectile",
    "projectile": "projectile",

    "발동": "trigger",
    "Trigger": "trigger",
    "trigger": "trigger",

    "지속시간": "duration",
    "Duration": "duration",
    "duration": "duration",

    "효과 범위": "aoe",
    "AoE": "aoe",
    "aoe": "aoe",

    "화염": "fire",
    "Fire": "fire",
    "fire": "fire",

    "냉기": "cold",
    "Cold": "cold",
    "cold": "cold",

    "번개": "lightning",
    "Lightning": "lightning",
    "lightning": "lightning",

    "근접": "melee",
    "Melee": "melee",
    "melee": "melee",

    "강타": "slam",
    "Slam": "slam",
    "slam": "slam",

    "소환수": "minion",
    "Minion": "minion",
    "minion": "minion",

    "토템": "totem",
    "Totem": "totem",
    "totem": "totem",

    "유탄": "grenade",
    "Grenade": "grenade",
    "grenade": "grenade",

    "카오스": "chaos",
    "Chaos": "chaos",
    "chaos": "chaos",

    "청산": "payoff",
    "Payoff": "payoff",
    "payoff": "payoff",

    "형태 변환": "shapeshift",
    "Shapeshift": "shapeshift",
    "shapeshift": "shapeshift",

    "연쇄": "chain",
    "Chain": "chain",
    "chain": "chain",

    "주문": "spell",
    "Spell": "spell",
    "spell": "spell",

    "공격": "attack",
    "Attack": "attack",
    "attack": "attack",

    "물리": "physical",
    "Physical": "physical",
    "physical": "physical",

    "카오스": "chaos",
    "Chaos": "chaos",

    "버프": "buff",
    "Buff": "buff",

    "조건부": "conditional",
    "Conditional": "conditional",

    "징표": "mark",
    "Mark": "mark",

    "저주": "curse",
    "Curse": "curse",

    "폭풍": "storm",
    "Storm": "storm",
}


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
}


TAG_WEIGHTS = {
    "projectile": 5,
    "trigger": 5,
    "chain": 4,
    "duration": 4,
    "aoe": 3,
    "fire": 3,
    "cold": 3,
    "lightning": 3,
    "melee": 2,
    "slam": 2,
    "minion": 2,
    "totem": 2,
    "grenade": 5,
    "chaos": 2,
    "payoff": 2,
    "shapeshift": 4,
    "spell": 2,
    "attack": 2,
    "physical": 2,
    "buff": 1,
    "conditional": 2,
    "mark": 2,
    "curse": 2,
    "storm": 2,
}


def normalize_tags(tags):
    normalized = []

    for tag in tags:
        normalized.append(TAG_NORMALIZE.get(tag, tag.lower() if isinstance(tag, str) else tag))

    return sorted(set(normalized))


def to_ko_tags(tags):
    return [EN_TO_KO.get(tag, tag) for tag in tags]


def calc_synergy(skill_tags_raw, support_tags_raw):
    skill_tags = set(normalize_tags(skill_tags_raw))
    support_tags = set(normalize_tags(support_tags_raw))

    overlap = skill_tags & support_tags

    score = 0

    for tag in overlap:
        score += TAG_WEIGHTS.get(tag, 1)

    combo_bonus = 0

    if {"trigger", "projectile"} <= overlap:
        combo_bonus += 5

    if {"chain", "projectile"} <= overlap:
        combo_bonus += 5

    if {"trigger", "duration"} <= overlap:
        combo_bonus += 4

    if {"grenade", "projectile"} <= overlap:
        combo_bonus += 4

    if {"fire", "trigger"} <= overlap:
        combo_bonus += 3

    if {"lightning", "chain"} <= overlap:
        combo_bonus += 3

    return score + combo_bonus, sorted(overlap), sorted(skill_tags), sorted(support_tags)


def main():
    skills = json.load(open(SKILLS_PATH, encoding="utf-8"))
    supports = json.load(open(SUPPORTS_PATH, encoding="utf-8"))

    results = []

    for skill in skills:
        skill_name = skill["name"]
        skill_tags_raw = skill.get("tags", [])

        for support in supports:
            support_name = support["name"]
            support_tags_raw = support.get("tags_ko", support.get("tags", []))

            score, overlap, skill_tags, support_tags = calc_synergy(
                skill_tags_raw,
                support_tags_raw,
            )

            if score < 3:
                continue

            results.append({
                "skill": skill_name,
                "support": support_name,
                "score": score,

                "shared_tags": overlap,
                "shared_tags_ko": to_ko_tags(overlap),

                "skill_tags": skill_tags,
                "skill_tags_ko": to_ko_tags(skill_tags),
                "support_tags": support_tags,
                "support_tags_ko": to_ko_tags(support_tags),

                "skill_tags_raw": skill_tags_raw,
                "support_tags_raw": support_tags_raw,
            })

    results.sort(key=lambda x: -x["score"])

    OUT_PATH.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Skill + Support synergy 분석 완료")
    print(f"저장 위치: {OUT_PATH}")
    print(f"결과 수: {len(results)}")
    print()

    print("=" * 100)

    for r in results[:50]:
        print(
            f"{r['skill']} + {r['support']} "
            f"score={r['score']} "
            f"shared={r['shared_tags_ko']}"
        )


if __name__ == "__main__":
    main()