import re
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

OUT_PATH = ROOT / "data" / "meta" / "mechanic_semantic_test.json"


MECHANIC_RULES = {
    "gain_as_extra": {
        "ko": "추가 피해 획득",
        "weight": 2.0,
        "patterns": [
            r"gain[s]? .* as extra",
            r"damage .* as extra",
            r"extra .* damage",
            r"추가 .* 피해",
            r"피해 .* 추가",
        ],
    },
    "conversion": {
        "ko": "피해 전환",
        "weight": 1.6,
        "patterns": [
            r"convert[s]? .* damage",
            r"converted to",
            r"conversion",
            r"전환",
        ],
    },
    "extra_projectile": {
        "ko": "추가 투사체",
        "weight": 1.9,
        "patterns": [
            r"additional projectile",
            r"\+\d+ .* projectile",
            r"fires? .* additional",
            r"추가 투사체",
            r"투사체 .* 추가",
        ],
    },
    "chain": {
        "ko": "연쇄",
        "weight": 1.7,
        "patterns": [
            r"chain",
            r"chains? \+\d+",
            r"연쇄",
        ],
    },
    "fork": {
        "ko": "갈라짐",
        "weight": 1.4,
        "patterns": [
            r"fork",
            r"갈라짐",
        ],
    },
    "pierce": {
        "ko": "관통",
        "weight": 1.3,
        "patterns": [
            r"pierce",
            r"관통",
        ],
    },
    "returning_projectile": {
        "ko": "돌아오는 투사체",
        "weight": 2.2,
        "patterns": [
            r"returning projectile",
            r"projectiles return",
            r"returns? to you",
            r"돌아오는 투사체",
            r"투사체 .* 돌아",
        ],
    },
    "shotgun": {
        "ko": "다중 적중",
        "weight": 2.3,
        "patterns": [
            r"shotgun",
            r"can hit .* multiple",
            r"hit .* more than once",
            r"여러 번 적중",
            r"다중 적중",
        ],
    },
    "overlap": {
        "ko": "범위 중첩",
        "weight": 2.0,
        "patterns": [
            r"overlap",
            r"overlapping",
            r"area .* overlap",
            r"중첩",
        ],
    },
    "trigger": {
        "ko": "발동",
        "weight": 1.8,
        "patterns": [
            r"trigger",
            r"cast .* when",
            r"cast .* on",
            r"when you crit",
            r"on critical strike",
            r"발동",
            r"치명타 .* 시전",
        ],
    },
    "trigger_loop": {
        "ko": "발동 루프",
        "weight": 2.5,
        "patterns": [
            r"trigger loop",
            r"loop",
            r"recoup .* trigger",
            r"발동 루프",
        ],
    },
    "crit_scaling": {
        "ko": "치명타 스케일링",
        "weight": 1.5,
        "patterns": [
            r"critical strike",
            r"crit",
            r"critical damage",
            r"치명타",
        ],
    },
    "ailment_scaling": {
        "ko": "상태이상 스케일링",
        "weight": 1.4,
        "patterns": [
            r"shock",
            r"ignite",
            r"freeze",
            r"chill",
            r"poison",
            r"bleed",
            r"감전",
            r"점화",
            r"동결",
            r"냉각",
            r"중독",
            r"출혈",
        ],
    },
    "charge_scaling": {
        "ko": "충전 스케일링",
        "weight": 1.5,
        "patterns": [
            r"power charge",
            r"frenzy charge",
            r"endurance charge",
            r"charge",
            r"권능 충전",
            r"격분 충전",
            r"인내 충전",
            r"충전",
        ],
    },
    "mana_scaling": {
        "ko": "마나 스케일링",
        "weight": 1.3,
        "patterns": [
            r"mana",
            r"maximum mana",
            r"마나",
        ],
    },
    "life_scaling": {
        "ko": "생명력 스케일링",
        "weight": 1.2,
        "patterns": [
            r"life",
            r"maximum life",
            r"생명력",
        ],
    },
    "minion_scaling": {
        "ko": "소환수 스케일링",
        "weight": 1.5,
        "patterns": [
            r"minion",
            r"소환수",
        ],
    },
}


DAMAGE_TYPES = {
    "physical": ["physical", "물리"],
    "fire": ["fire", "화염"],
    "cold": ["cold", "냉기"],
    "lightning": ["lightning", "번개"],
    "chaos": ["chaos", "카오스"],
}


BROKEN_COMBO_RULES = [
    {
        "name": "Projectile Return Shotgun",
        "ko": "돌아오는 투사체 다중 적중",
        "requires": ["returning_projectile", "shotgun"],
        "score": 35,
        "reason": "돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음",
    },
    {
        "name": "Projectile Chain Overlap",
        "ko": "투사체 연쇄 중첩",
        "requires": ["chain", "overlap"],
        "score": 28,
        "reason": "연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음",
    },
    {
        "name": "Extra Projectile Shotgun",
        "ko": "추가 투사체 다중 적중",
        "requires": ["extra_projectile", "shotgun"],
        "score": 30,
        "reason": "투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음",
    },
    {
        "name": "Gain As Extra Conversion Stack",
        "ko": "추가 피해 획득 + 전환 중첩",
        "requires": ["gain_as_extra", "conversion"],
        "score": 24,
        "reason": "전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음",
    },
    {
        "name": "Trigger Crit Engine",
        "ko": "치명타 발동 엔진",
        "requires": ["trigger", "crit_scaling"],
        "score": 22,
        "reason": "치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음",
    },
    {
        "name": "Trigger Loop Candidate",
        "ko": "발동 루프 후보",
        "requires": ["trigger", "trigger_loop"],
        "score": 40,
        "reason": "발동 조건이 다시 발동 조건을 만들면 루프성 구조가 될 수 있음",
    },
]


def normalize_text(text):
    if text is None:
        return ""

    if isinstance(text, list):
        return " ".join(normalize_text(x) for x in text)

    if isinstance(text, dict):
        return " ".join(normalize_text(v) for v in text.values())

    text = str(text).lower()
    text = re.sub(r"[_\-/,|]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def match_patterns(text, patterns):
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return True

    return False


def detect_damage_types(text):
    normalized = normalize_text(text)
    found = []

    for damage_type, keywords in DAMAGE_TYPES.items():
        for keyword in keywords:
            if keyword in normalized:
                found.append(damage_type)
                break

    return found


def parse_mechanics(text):
    normalized = normalize_text(text)

    mechanics = []
    score = 0

    for mechanic, rule in MECHANIC_RULES.items():
        if match_patterns(normalized, rule["patterns"]):
            mechanics.append({
                "id": mechanic,
                "ko": rule["ko"],
                "weight": rule["weight"],
            })
            score += rule["weight"]

    damage_types = detect_damage_types(normalized)
    combos = detect_broken_combos([m["id"] for m in mechanics])

    combo_score = sum(c["score"] for c in combos)

    return {
        "text": text,
        "mechanics": mechanics,
        "mechanic_ids": [m["id"] for m in mechanics],
        "mechanic_ko": [m["ko"] for m in mechanics],
        "damage_types": damage_types,
        "broken_combos": combos,
        "semantic_score": round(score + combo_score, 3),
    }


def detect_broken_combos(mechanic_ids):
    found = []
    mechanic_set = set(mechanic_ids)

    for rule in BROKEN_COMBO_RULES:
        if set(rule["requires"]).issubset(mechanic_set):
            found.append({
                "name": rule["name"],
                "ko": rule["ko"],
                "score": rule["score"],
                "reason": rule["reason"],
            })

    return found


def parse_option_list(options):
    results = []
    total_score = 0
    all_mechanics = set()
    all_damage_types = set()
    all_combos = []

    for option in options:
        parsed = parse_mechanics(option)

        results.append(parsed)
        total_score += parsed["semantic_score"]
        all_mechanics.update(parsed["mechanic_ids"])
        all_damage_types.update(parsed["damage_types"])
        all_combos.extend(parsed["broken_combos"])

    cross_combos = detect_broken_combos(list(all_mechanics))
    cross_combo_names = {c["name"] for c in all_combos}

    for combo in cross_combos:
        if combo["name"] not in cross_combo_names:
            all_combos.append(combo)
            total_score += combo["score"]

    return {
        "options": results,
        "all_mechanics": sorted(all_mechanics),
        "all_damage_types": sorted(all_damage_types),
        "broken_combos": all_combos,
        "total_semantic_score": round(total_score, 3),
    }


def main():
    samples = [
        "Projectiles return to you",
        "Skills fire 2 additional Projectiles",
        "Projectiles can hit the same target multiple times",
        "Gain 30% of Physical Damage as Extra Fire Damage",
        "Trigger socketed spells when you deal a Critical Strike",
    ]

    result = parse_option_list(samples)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()