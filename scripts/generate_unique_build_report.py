import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MATCH_PATH = ROOT / "data" / "meta" / "unique_build_matches.json"
OUT_PATH = ROOT / "data" / "meta" / "unique_build_report.md"


EN_TO_KO = {
    # 시스템 태그
    "trigger": "발동",
    "projectile": "투사체",
    "chain": "연쇄",
    "extra_projectile": "추가 투사체",
    "gain_as_extra": "추가 피해 획득",
    "conversion": "전환",
    "crit": "치명타",
    "fire": "화염",
    "cold": "냉기",
    "lightning": "번개",
    "chaos": "카오스",
    "duration": "지속시간",
    "minion": "소환수",
    "charge": "충전",
    "spirit": "정신력",
    "mana": "마나",
    "life": "생명력",
    "aoe": "효과 범위",
    "fork": "갈라짐",
    "pierce": "관통",
    "meta_energy": "메타 에너지",
    "spell": "주문",
    "attack": "공격",
    "physical": "물리",
    "cooldown": "재사용 대기시간",
    "attribute": "능력치",

    # 베이스 타입
    "Ring": "반지",
    "Jade Amulet": "비취 목걸이",
    "Pearl Ring": "진주 반지",
    "Voltaic Staff": "전격 지팡이",
    "Wyrm Quarterstaff": "고룡 쿼터스태프",
    "Dyad Crossbow": "다이애드 쇠뇌",
    "Helix Spear": "나선 창",
    "Ashen Staff": "재의 지팡이",
    "Iron Greaves": "철각 경갑",
    "Toxic Quiver": "맹독 화살통",
    "Broadhead Quiver": "브로드헤드 화살통",
    "Chiming Staff": "차임 지팡이",
    "Artillery Bow": "포격 활",
    "Penetrating Quiver": "관통 화살통",
    "Ironhead Spear": "철두 창",
    "Hunting Spear": "사냥 창",
    "War Spear": "전쟁 창",
    "Warden Bow": "감시자 활",
    "Recurve Bow": "리커브 활",
    "Pronged Spear": "갈래 창",
    "Torn Gloves": "찢어진 장갑",
    "Guarded Helm": "수호 투구",
    "Ornate Gauntlets": "화려한 건틀릿",

    # 유니크 이름
    "Choir of the Storm": "폭풍의 합창",
    "Snakepit": "뱀구덩이",
    "Earthbound": "대지속박",
    "Collapsing Horizon": "붕괴하는 지평선",
    "Double Vision": "이중 환영",
    "Spire of Ire": "분노의 첨탑",
    "Dusk Vigil": "황혼의 감시",
    "Corpsewade": "시체걸음",
    "Murkshaft": "암흑 화살통",
    "Sekhema's Resolve": "세케마의 결의",
    "Asphyxia's Wrath": "질식의 분노",
    "Sire of Shards": "파편의 군주",
    "Fairgraves' Curse": "페어그레이브의 저주",
    "Drillneck": "드릴넥",
    "Tyranny's Grip": "폭군의 손아귀",
    "Chainsting": "연쇄침",
    "Daevata's Wind": "다에바타의 바람",
    "Ironbound": "강철 속박",
    "Splinterheart": "쪼개진 심장",
    "Atziri's Contempt": "앗지리의 경멸",
    "Painter's Servant": "화가의 하인",
    "Erian's Cobble": "에리안의 조약돌",
    "Death Articulated": "구현된 죽음",
}


BAD_UNIQUE_NAMES = {
    "Radius is doubled",
    "Flasks",
    "Charms",
    "Soul Cores",
    "Rare",
    "Magic",
    "Normal",
}


def ko(text):
    return EN_TO_KO.get(text, text)


def to_ko(tags):
    return [ko(t) for t in tags]


def normalize_display_tags(tags):
    return [ko(t) for t in tags]


def is_bad_unique(u):
    name = u.get("name", "").strip()

    if name in BAD_UNIQUE_NAMES:
        return True

    bad_starts = [
        "Radius ",
        "Enemies ",
        "Enemy ",
        "Life ",
        "Mana ",
        "Energy Shield",
        "Adds ",
        "Increased ",
        "Reduced ",
        "You ",
        "Your ",
        "Minions ",
    ]

    return any(name.startswith(x) for x in bad_starts)


def main():
    data = json.load(open(MATCH_PATH, encoding="utf-8"))

    lines = []

    lines.append("# PoE2 유니크 빌드 리포트")
    lines.append("")
    lines.append("Skill + Support + Passive + Unique 4축 기반 빌드 후보")
    lines.append("")

    for i, build in enumerate(data[:50], start=1):
        shared_tags = build.get("shared_tags_ko") or to_ko(
            build.get("shared_tags", [])
        )

        shared_tags = normalize_display_tags(shared_tags)

        lines.append(
            f"## #{i} {ko(build['skill'])} + {ko(build['support'])}"
        )

        lines.append("")
        lines.append(f"- Build Score: **{build['build_score']}**")
        lines.append(
            f"- Shared Tags: {', '.join(shared_tags)}"
        )

        lines.append("")
        lines.append("### 추천 유니크")
        lines.append("")

        count = 0

        for u in build.get("uniques", []):
            if is_bad_unique(u):
                continue

            matched_tags = (
                u.get("matched_tags_ko")
                or to_ko(u.get("matched_tags", []))
            )

            unique_tags = (
                u.get("unique_tags_ko")
                or to_ko(u.get("unique_tags", []))
            )

            matched_tags = normalize_display_tags(matched_tags)
            unique_tags = normalize_display_tags(unique_tags)

            unique_name = ko(u.get("name", ""))
            base_type = ko(u.get("base_type", ""))

            lines.append(
                f"- **{unique_name}** "
                f"/ {base_type} "
                f"/ 점수 {u['score']} "
                f"/ 매칭: {', '.join(matched_tags)} "
                f"/ 태그: {', '.join(unique_tags)}"
            )

            count += 1

            if count >= 10:
                break

        lines.append("")
        lines.append("---")
        lines.append("")

    OUT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print("Unique build report 생성 완료")
    print(f"저장 위치: {OUT_PATH}")


if __name__ == "__main__":
    main()