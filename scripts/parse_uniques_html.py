import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]

HTML_PATH = ROOT / "data" / "uniques" / "unique_items.html"
OUT_PATH = ROOT / "data" / "uniques" / "uniques.json"


BAD_NAMES = {
    "Flasks",
    "Charms",
    "Soul Cores",
    "Update cookie preferences",
    "DB",
    "Items",
    "Unique",
    "Reforging Bench",
    "Gem",
    "Skill Gems",
    "Support Gems",
    "Spirit Gems",
    "Lineage Supports",
    "Modifiers",
    "Desecrated Modifiers",
    "Keywords",
    "Crafting",
    "Liquid Emotions",
    "Quest",
    "Ascendancy Classes",
    "Passive Skill Tree",
    "Act",
    "Waystones",
    "Endgame",
    "Atlas Skill Tree",
    "Economy",
    "Patreon",
    "PoE",
    "TW 繁體中文",
    "CN 简体中文",
    "US English",
    "KR 한국어",
    "JP Japanese",
    "RU Русский",
    "PO Português",
    "TH ภาษาไทย",
    "FR Français",
    "DE Deutsch",
    "ES Spanish",
    "Reset",
    "Requires:",
    "Adds",
    "Physical",
    "Damage",
    "Accuracy",
    "Rating",
    "Attack",
    "Armour",
    "Evasion",
    "Energy",
    "Shield",
    "Energy Shield",
    "Level",
    "Strength",
    "Dexterity",
    "Intelligence",
    "Normal",
    "Magic",
    "Rare",
}


BAD_NAME_PATTERNS = [
    r"^as though\b",
    r"^as if\b",
    r"^with\b",
    r"^to\b",
    r"^from\b",
    r"^Rare$",
    r"^Magic$",
    r"^Normal$",
    r"^Poisoned$",
    r"^Bleeding$",
    r"^Ignited$",
    r"^Shocked$",
    r"^Frozen$",
    r"^Chilled$",
    r"^Cursed$",
    r"^Enemies\b",
    r"^Enemy\b",
    r"^Life\b",
    r"^Mana\b",
    r"^Energy Shield\b",
    r"^Adds\b",
    r"^Added\b",
    r"^Increased\b",
    r"^Reduced\b",
    r"^More\b",
    r"^Less\b",
    r"^You\b",
    r"^Your\b",
    r"^Minions\b",
    r"^Allies\b",
    r"^Skills\b",
    r"^Socketed\b",
    r"^Grants\b",
    r"^Gain\b",
    r"^Lose\b",
    r"^Cannot\b",
    r"^Can\b",
    r"^When\b",
    r"^While\b",
    r"^If\b",
    r"^On\b",
    r"^With\b",
    r"^Against\b",
    r"^Nearby\b",
    r"^Critical\b",
    r"^Projectiles\b",
    r"^Spells\b",
    r"^Attacks\b",
    r"^Hits\b",
    r"^Modifiers\b",
    r"^Quality\b",
    r"^Requires\b",
    r"^Has\b",
    r"^Maximum\b",
    r"^Minimum\b",
    r"^Base\b",
    r"^Item\b",
    r"^Class\b",
    r"^Tags\b",
    r"^Level\b",
    r"^Area\b",
    r"^Effect\b",
    r"^Duration\b",
    r"^Cooldown\b",
    r"^Fire\b",
    r"^Cold\b",
    r"^Lightning\b",
    r"^Chaos\b",
    r"^Physical\b",
]


BASE_TYPE_HINTS = {
    "Club",
    "Mace",
    "Hammer",
    "Axe",
    "Sword",
    "Spear",
    "Flail",
    "Bow",
    "Crossbow",
    "Quiver",
    "Staff",
    "Wand",
    "Sceptre",
    "Dagger",
    "Claw",
    "Quarterstaff",
    "Shield",
    "Buckler",
    "Focus",
    "Helmet",
    "Helm",
    "Hood",
    "Crown",
    "Mask",
    "Cap",
    "Body Armour",
    "Armour",
    "Robe",
    "Vestments",
    "Coat",
    "Jacket",
    "Gloves",
    "Gauntlets",
    "Boots",
    "Greaves",
    "Shoes",
    "Amulet",
    "Ring",
    "Belt",
    "Charm",
    "Jewel",
}


KEYWORD_TAGS = {
    "trigger": ["trigger", "발동"],
    "projectile": ["projectile", "투사체"],
    "chain": ["chain", "연쇄"],
    "fork": ["fork"],
    "pierce": ["pierce", "관통"],
    "duration": ["duration", "지속시간"],
    "cooldown": ["cooldown", "재사용 대기시간"],
    "gain_as_extra": ["gain.*as extra", "추가.*획득"],
    "conversion": ["converted to", "conversion", "전환"],
    "extra_projectile": ["additional projectile", "추가 투사체"],
    "crit": ["critical", "crit", "치명타"],
    "meta_energy": ["meta", "energy"],
    "fire": ["fire", "ignite", "burning", "화염", "점화"],
    "cold": ["cold", "freeze", "chill", "냉기", "빙결"],
    "lightning": ["lightning", "shock", "번개", "감전"],
    "chaos": ["chaos", "poison", "카오스", "중독"],
    "minion": ["minion", "소환수"],
    "spirit": ["spirit", "정신력"],
    "charge": ["charge", "충전"],
    "life": ["life", "생명력"],
    "mana": ["mana", "마나"],
    "attribute": ["strength", "dexterity", "intelligence", "힘", "민첩", "지능"],
}


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def detect_tags(text):
    text_lower = text.lower()
    found = set()

    for tag, patterns in KEYWORD_TAGS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                found.add(tag)
                break

    return sorted(found)


def looks_like_item_name(line):
    if not line:
        return False

    if line in BAD_NAMES:
        return False

    if len(line) < 3:
        return False

    if line.endswith(":"):
        return False

    for pattern in BAD_NAME_PATTERNS:
        if re.search(pattern, line):
            return False

    if re.search(r"^\d+$", line):
        return False

    if re.search(r"^[+\-]?\d", line):
        return False

    if any(x in line for x in ["%", "—", "|", "/", "\\"]):
        return False

    words = line.split()

    if len(words) > 7:
        return False

    if not line[0].isupper():
        return False

    return True


def looks_like_base_type(line):
    if not line:
        return False

    if line in BAD_NAMES:
        return False

    for pattern in BAD_NAME_PATTERNS:
        if re.search(pattern, line):
            return False

    return any(hint in line for hint in BASE_TYPE_HINTS)


def parse_uniques(text):
    lines = [clean(line) for line in text.split("\n")]
    lines = [line for line in lines if line]

    items = []
    i = 0

    while i < len(lines) - 1:
        name = lines[i]
        next_line = lines[i + 1]

        if looks_like_item_name(name) and looks_like_base_type(next_line):
            base_type = next_line
            mods = []

            j = i + 2

            while j < len(lines):
                line = lines[j]

                if (
                    looks_like_item_name(line)
                    and j + 1 < len(lines)
                    and looks_like_base_type(lines[j + 1])
                ):
                    break

                if line not in BAD_NAMES:
                    mods.append(line)

                j += 1

            mod_text = " ".join(mods)
            tags = detect_tags(mod_text)

            if len(mods) >= 3:
                items.append(
                    {
                        "name": name,
                        "base_type": base_type,
                        "mods": mods,
                        "mod_text": mod_text,
                        "tags": tags,
                    }
                )

            i = j
        else:
            i += 1

    deduped = []
    seen = set()

    for item in items:
        key = (item["name"], item["base_type"])
        if key in seen:
            continue

        seen.add(key)
        deduped.append(item)

    return deduped


def main():
    html = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n")

    uniques = parse_uniques(text)

    OUT_PATH.write_text(
        json.dumps(uniques, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"유니크 아이템 추출 완료: {len(uniques)}개")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("=" * 100)

    for u in uniques[:50]:
        print(
            f"{u['name']} / {u['base_type']} "
            f"tags={u['tags']}"
        )


if __name__ == "__main__":
    main()