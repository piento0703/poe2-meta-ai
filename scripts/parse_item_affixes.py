import json
from pathlib import Path
from mechanic_semantic_parser import parse_option_list


ROOT = Path(__file__).resolve().parents[1]

INPUT_PATH = ROOT / "data" / "items" / "rare_item_affixes.json"
OUT_PATH = ROOT / "data" / "meta" / "rare_affix_semantic_analysis.json"


SAMPLE_AFFIXES = [
    {
        "slot": "weapon",
        "name": "투사체 리턴 샷건 무기",
        "options": [
            "Projectiles return to you",
            "Skills fire 2 additional Projectiles",
            "Projectiles can hit the same target multiple times",
            "Gain 30% of Physical Damage as Extra Fire Damage",
        ],
    },
    {
        "slot": "amulet",
        "name": "치명타 발동 목걸이",
        "options": [
            "Trigger socketed spells when you deal a Critical Strike",
            "30% increased Critical Strike Chance",
            "Gain 20% of Lightning Damage as Extra Chaos Damage",
        ],
    },
]


SLOT_WEIGHT = {
    "weapon": 1.35,
    "quiver": 1.25,
    "amulet": 1.2,
    "ring": 1.15,
    "helmet": 1.05,
    "body_armour": 1.05,
    "gloves": 1.05,
    "boots": 1.0,
    "belt": 1.0,
    "jewel": 1.25,
}


def load_json(path, default=None):
    if default is None:
        default = []

    if not path.exists():
        return default

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"저장 완료: {path}")


def classify_power_level(score):
    if score >= 80:
        return "S급 / 빌드 파괴 가능성"
    if score >= 50:
        return "A급 / 강력한 코어 후보"
    if score >= 30:
        return "B급 / 유효한 시너지 후보"
    if score >= 15:
        return "C급 / 보조 시너지"
    return "낮음"


def analyze_affix_item(item):
    slot = item.get("slot", "unknown")
    name = item.get("name", "unknown item")
    options = item.get("options", [])

    semantic = parse_option_list(options)

    slot_weight = SLOT_WEIGHT.get(slot, 1.0)
    raw_score = semantic["total_semantic_score"]
    final_score = round(raw_score * slot_weight, 3)

    return {
        "slot": slot,
        "name": name,
        "options": options,
        "mechanics": semantic["all_mechanics"],
        "damage_types": semantic["all_damage_types"],
        "broken_combos": semantic["broken_combos"],
        "raw_semantic_score": raw_score,
        "slot_weight": slot_weight,
        "final_score": final_score,
        "power_level": classify_power_level(final_score),
    }


def analyze_items(items):
    results = []

    for item in items:
        analyzed = analyze_affix_item(item)
        results.append(analyzed)

    results.sort(key=lambda x: x["final_score"], reverse=True)

    return results


def main():
    items = load_json(INPUT_PATH, SAMPLE_AFFIXES)

    print(f"loaded affix items: {len(items)}")

    results = analyze_items(items)

    save_json(OUT_PATH, results)

    for item in results:
        print("=" * 80)
        print(f"아이템: {item['name']}")
        print(f"슬롯: {item['slot']}")
        print(f"점수: {item['final_score']}")
        print(f"등급: {item['power_level']}")
        print(f"메커니즘: {', '.join(item['mechanics'])}")

        if item["broken_combos"]:
            print("위험 조합:")
            for combo in item["broken_combos"]:
                print(f"- {combo['ko']}: {combo['reason']}")


if __name__ == "__main__":
    main()