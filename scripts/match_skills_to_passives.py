import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]

PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
SKILL_PATH = ROOT / "data" / "skills" / "skills.json"
OUT_PATH = ROOT / "data" / "skills" / "skill_passive_synergy.json"

META_GROUPS = {
    "lightning": ["lightning", "shock", "shocked", "electrocute", "electrocuted"],
    "cold": ["cold", "freeze", "frozen", "chill", "chilled"],
    "fire": ["fire", "ignite", "burn", "burning"],
    "crit": ["critical", "critical hit", "critical damage", "critical chance", "crit"],
    "shapeshift": ["shapeshift", "shapeshifting", "bear", "wolf", "claw"],
    "projectile": ["projectile", "projectiles"],
    "long_range": ["far away", "distance", "long range"],
    "gain_as_extra": ["gain", "as extra", "extra damage"],
    "meta_energy": ["meta", "energy", "meta skills"],
    "reservation": ["reservation", "spirit", "reservation efficiency"],
    "consume_charge": ["consume", "charge"],
    "power_charge": ["power charge", "power charges"],
    "frenzy_charge": ["frenzy charge", "frenzy charges"],
    "endurance_charge": ["endurance charge", "endurance charges"],
    "skill_speed": ["skill speed", "attack speed", "cast speed"],
    "duration": ["duration"],
    "trigger": ["trigger", "triggered"],
    "aoe": ["aoe", "area of effect"],
    "spell": ["spell"],
    "attack": ["attack"],
    "minion": ["minion", "minions"],
    "physical": ["physical"],
    "chaos": ["chaos"]
}

WEIGHTS = {
    "gain_as_extra": 7.0,
    "meta_energy": 6.5,
    "consume_charge": 6.0,
    "crit": 5.5,
    "reservation": 5.0,
    "shapeshift": 5.0,
    "skill_speed": 4.5,
    "power_charge": 4.5,
    "lightning": 4.0,
    "cold": 4.0,
    "projectile": 4.0,
    "long_range": 4.0,
    "trigger": 3.5,
    "duration": 3.0,
    "fire": 3.0,
    "aoe": 2.5,
    "spell": 2.0,
    "attack": 2.0,
    "physical": 2.0,
    "chaos": 2.0,
    "minion": 1.5
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_text(value):
    if value is None:
        return ""

    if isinstance(value, str):
        return value

    if isinstance(value, list):
        return " ".join(normalize_text(v) for v in value)

    if isinstance(value, dict):
        return " ".join(normalize_text(v) for v in value.values())

    return str(value)


def extract_passive_text(node):
    parts = []

    for key in ["name", "dn", "sd", "stats", "reminderText"]:
        if key in node:
            parts.append(normalize_text(node[key]))

    return " ".join(parts).lower()


def detect_tags(text):
    found = set()

    for tag, keywords in META_GROUPS.items():
        for kw in keywords:
            if kw.lower() in text:
                found.add(tag)
                break

    return sorted(found)


def extract_skill_text(skill):
    parts = [
        skill.get("name", ""),
        normalize_text(skill.get("tags", [])),
        skill.get("type", ""),
        skill.get("description", "")
    ]
    return " ".join(parts).lower()


def node_bonus(node):
    bonus = 0

    if node.get("isKeystone"):
        bonus += 5

    if node.get("isNotable"):
        bonus += 3

    if node.get("ascendancyName"):
        bonus += 4

    return bonus


def calculate_score(skill_tags, passive_tags, node):
    overlap = sorted(set(skill_tags) & set(passive_tags))

    if not overlap:
        return 0, []

    score = sum(WEIGHTS.get(tag, 1.0) for tag in overlap)
    score += node_bonus(node)

    if "gain_as_extra" in overlap and "crit" in skill_tags:
        score += 3

    if "shapeshift" in overlap and "crit" in skill_tags:
        score += 3

    if "consume_charge" in overlap and "crit" in skill_tags:
        score += 3

    if "meta_energy" in overlap and "trigger" in skill_tags:
        score += 3

    return round(score, 2), overlap


def main():
    passive_data = load_json(PASSIVE_PATH)
    skills = load_json(SKILL_PATH)

    nodes = passive_data["nodes"]

    passive_index = []

    for node_id, node in nodes.items():
        text = extract_passive_text(node)
        tags = detect_tags(text)

        if not tags:
            continue

        passive_index.append({
            "id": node_id,
            "name": node.get("name") or node.get("dn") or "",
            "text": text,
            "tags": tags,
            "node": node
        })

    results = []

    for skill in skills:
        skill_name = skill.get("name", "")
        skill_text = extract_skill_text(skill)
        skill_tags = detect_tags(skill_text)

        matched = []

        for passive in passive_index:
            score, overlap = calculate_score(
                skill_tags,
                passive["tags"],
                passive["node"]
            )

            if score > 0:
                matched.append({
                    "passive_id": passive["id"],
                    "passive_name": passive["name"],
                    "score": score,
                    "overlap": overlap,
                    "passive_tags": passive["tags"],
                    "is_notable": passive["node"].get("isNotable", False),
                    "is_keystone": passive["node"].get("isKeystone", False),
                    "ascendancy": passive["node"].get("ascendancyName")
                })

        matched.sort(key=lambda x: x["score"], reverse=True)

        total_score = round(sum(x["score"] for x in matched), 2)

        results.append({
            "skill": skill_name,
            "skill_tags": skill_tags,
            "total_score": total_score,
            "matched_passive_count": len(matched),
            "top_passives": matched[:30]
        })

    results.sort(key=lambda x: x["total_score"], reverse=True)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Skill ↔ Passive Synergy 분석 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("TOP 20 Skills")
    print("=" * 80)

    for i, row in enumerate(results[:20], 1):
        print(
            f"{i:02}. {row['skill']} | "
            f"score={row['total_score']} | "
            f"tags={row['skill_tags']} | "
            f"passives={row['matched_passive_count']}"
        )

        for p in row["top_passives"][:5]:
            print(
                f"    - {p['passive_name']} | "
                f"{p['score']} | "
                f"{p['overlap']}"
            )

        print()


if __name__ == "__main__":
    main()