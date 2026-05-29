import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TRIPLE_PATH = ROOT / "data" / "meta" / "triple_synergy_candidates.json"
UNIQUES_PATH = ROOT / "data" / "uniques" / "uniques.json"

OUT_PATH = ROOT / "data" / "meta" / "unique_build_matches.json"


TAG_WEIGHTS = {
    "trigger": 8,
    "projectile": 6,
    "chain": 6,
    "extra_projectile": 7,
    "gain_as_extra": 8,
    "conversion": 7,
    "crit": 5,
    "fire": 4,
    "cold": 4,
    "lightning": 4,
    "chaos": 4,
    "duration": 3,
    "minion": 3,
    "charge": 3,
    "spirit": 3,
    "mana": 2,
    "life": 2,
    "fork": 4,
    "pierce": 4,
    "meta_energy": 5,
}


EN_TO_KO = {
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
    "fork": "갈라짐",
    "pierce": "관통",
    "meta_energy": "메타 에너지",
    "aoe": "효과 범위",
    "spell": "주문",
    "attack": "공격",
    "physical": "물리",
    "cooldown": "재사용 대기시간",
    "attribute": "능력치",
}


BAD_NAMES = {
    "Flasks",
    "Charms",
    "Soul Cores",
    "Rare",
    "Magic",
    "Normal",
    "Radius is doubled",
}


def to_ko(tags):
    return [EN_TO_KO.get(t, t) for t in tags]


def is_bad_unique(unique):
    name = unique.get("name", "").strip()
    base_type = unique.get("base_type", "").strip().lower()

    if name in BAD_NAMES:
        return True

    bad_name_starts = [
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

    if any(name.startswith(x) for x in bad_name_starts):
        return True

    bad_base_starts = [
        "as though",
        "as if",
        "with ",
        "to ",
        "from ",
    ]

    if any(base_type.startswith(x) for x in bad_base_starts):
        return True

    return False


def unique_score(build, unique):
    build_tags = set(build.get("shared_tags", []))
    unique_tags = set(unique.get("tags", []))

    overlap = build_tags & unique_tags

    score = 0

    for tag in overlap:
        score += TAG_WEIGHTS.get(tag, 1)

    if "trigger" in build_tags and "trigger" in unique_tags:
        score += 5

    if "projectile" in build_tags and "projectile" in unique_tags:
        score += 4

    if "fire" in build_tags and "gain_as_extra" in unique_tags:
        score += 5

    if "lightning" in build_tags and "chain" in unique_tags:
        score += 4

    if "crit" in unique_tags and ("trigger" in build_tags or "projectile" in build_tags):
        score += 3

    return score, sorted(overlap)


def main():
    builds = json.load(open(TRIPLE_PATH, encoding="utf-8"))
    uniques = json.load(open(UNIQUES_PATH, encoding="utf-8"))

    results = []

    for build in builds[:200]:
        matched_uniques = []

        for unique in uniques:
            if is_bad_unique(unique):
                continue

            score, overlap = unique_score(build, unique)

            if score <= 0:
                continue

            unique_tags = unique.get("tags", [])

            matched_uniques.append({
                "name": unique["name"],
                "base_type": unique.get("base_type", ""),
                "score": score,
                "matched_tags": overlap,
                "matched_tags_ko": to_ko(overlap),
                "unique_tags": unique_tags,
                "unique_tags_ko": to_ko(unique_tags),
            })

        matched_uniques.sort(key=lambda x: -x["score"])

        if matched_uniques:
            results.append({
                "skill": build["skill"],
                "support": build["support"],
                "build_score": build["score"],
                "shared_tags": build.get("shared_tags", []),
                "shared_tags_ko": build.get("shared_tags_ko", to_ko(build.get("shared_tags", []))),
                "uniques": matched_uniques[:20],
            })

    OUT_PATH.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Unique ↔ Build 매칭 완료")
    print(f"저장 위치: {OUT_PATH}")
    print(f"결과 수: {len(results)}")


if __name__ == "__main__":
    main()