import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]

HTML_PATH = ROOT / "data" / "skills" / "skill_gems.html"
OUT_PATH = ROOT / "data" / "skills" / "skills.json"


KO_TAGS = [
    "효과 범위",
    "집중 유지",
    "형태 변환",
    "위해 요소",
    "지속시간",
    "지속형",
    "조건부",
    "소환수",
    "투사체",
    "청산",
    "잔류물",
    "유지형",
    "전령",
    "강타",
    "공격",
    "근접",
    "깃발",
    "냉기",
    "단계",
    "명령",
    "물리",
    "발동",
    "버프",
    "번개",
    "보조",
    "식물",
    "연쇄",
    "요소",
    "유탄",
    "저주",
    "주문",
    "유지",
    "징표",
    "카오스",
    "타격",
    "탄약",
    "토템",
    "폭풍",
    "함성",
    "혈통",
    "화염",
    "보주",
    "이동",
    "메타",
    "여행",
]


KO_TO_EN = {
    "공격": "attack",
    "근접": "melee",
    "강타": "slam",
    "냉기": "cold",
    "단계": "staged",
    "명령": "command",
    "물리": "physical",
    "발동": "trigger",
    "버프": "buff",
    "번개": "lightning",
    "소환수": "minion",
    "식물": "plant",
    "연쇄": "chain",
    "위해 요소": "hazard",
    "요소": "elemental",
    "유지형": "persistent",
    "유탄": "grenade",
    "잔류물": "remnant",
    "저주": "curse",
    "전령": "herald",
    "조건부": "conditional",
    "주문": "spell",
    "지속시간": "duration",
    "지속형": "persistent",
    "집중 유지": "channelling",
    "유지": "channelling",
    "징표": "mark",
    "청산": "payoff",
    "카오스": "chaos",
    "타격": "strike",
    "탄약": "ammo",
    "토템": "totem",
    "투사체": "projectile",
    "폭풍": "storm",
    "함성": "warcry",
    "혈통": "lineage",
    "형태 변환": "shapeshift",
    "화염": "fire",
    "효과 범위": "aoe",
    "보주": "orb",
    "이동": "travel",
    "여행": "travel",
    "메타": "meta",
}


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def to_en_tags(tags_ko):
    return [KO_TO_EN.get(t, t) for t in tags_ko]


def parse_skills(text):
    text = clean(text)

    tag_alt = "|".join(re.escape(t) for t in sorted(KO_TAGS, key=len, reverse=True))

    pattern = re.compile(
        rf"(?P<name>[가-힣A-Za-z0-9'’.\- ]+?)\s*"
        rf"\(\s*(?P<tier>\d+)\s*\)\s*"
        rf"(?P<tags>(?:{tag_alt})(?:\s*,\s*(?:{tag_alt}))*)"
    )

    skills = []
    seen = set()

    for m in pattern.finditer(text):
        name = clean(m.group("name"))
        tier = int(m.group("tier"))
        raw_tags = clean(m.group("tags"))

        if "이름" in name:
            name = clean(name.split("이름")[-1])

        if not name:
            continue

        tags_ko = [clean(t) for t in raw_tags.split(",") if clean(t)]
        tags_en = to_en_tags(tags_ko)

        key = (name, tier, tuple(tags_ko))
        if key in seen:
            continue

        seen.add(key)

        skills.append({
            "name": name,
            "tier": tier,
            "display_name": f"{name} ({tier})",
            "tags": tags_ko,
            "tags_ko": tags_ko,
            "tags_en": tags_en,
            "raw_tags": raw_tags,
        })

    return skills


def main():
    html = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(" ", strip=True)

    skills = parse_skills(text)

    OUT_PATH.write_text(
        json.dumps(skills, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"스킬 추출 완료: {len(skills)}개")
    print(f"저장 위치: {OUT_PATH}")
    print("=" * 100)

    for s in skills[:30]:
        print(f"{s['name']} ({s['tier']}) {s['raw_tags']} | tags={s['tags']}")


if __name__ == "__main__":
    main()