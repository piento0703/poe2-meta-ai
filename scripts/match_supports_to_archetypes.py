import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SUPPORTS_PATH = ROOT / "data" / "supports" / "supports.json"
OUT_PATH = ROOT / "data" / "supports" / "support_archetype_matches.json"


ARCHETYPES = {
    "Tri-Element Trigger Duration": {
        "priority_tags": ["발동", "지속시간", "화염", "냉기", "번개", "효과 범위", "조건부", "주문"],
        "weights": {
            "발동": 5,
            "지속시간": 4,
            "화염": 3,
            "냉기": 3,
            "번개": 3,
            "효과 범위": 2,
            "조건부": 2,
            "주문": 2,
        },
    },
    "Projectile Duration Grenade": {
        "priority_tags": ["투사체", "유탄", "지속시간", "효과 범위", "연쇄", "탄약", "발동"],
        "weights": {
            "투사체": 5,
            "유탄": 5,
            "지속시간": 3,
            "효과 범위": 3,
            "연쇄": 3,
            "탄약": 2,
            "발동": 2,
        },
    },
    "Fire Meta Trigger Crit": {
        "priority_tags": ["발동", "화염", "조건부", "효과 범위", "주문", "청산", "버프"],
        "weights": {
            "발동": 5,
            "화염": 4,
            "조건부": 3,
            "효과 범위": 3,
            "주문": 2,
            "청산": 2,
            "버프": 1,
        },
    },
    "Shapeshift Trigger Duration": {
        "priority_tags": ["형태 변환", "발동", "지속시간", "냉기", "버프", "근접", "공격"],
        "weights": {
            "형태 변환": 5,
            "발동": 4,
            "지속시간": 4,
            "냉기": 3,
            "버프": 2,
            "근접": 2,
            "공격": 2,
        },
    },
}


def score_support(support, archetype):
    tags = set(support.get("tags_ko", support.get("tags", [])))
    weights = archetype["weights"]

    score = 0
    matched = []

    for tag, weight in weights.items():
        if tag in tags:
            score += weight
            matched.append(tag)

    # 보조젬 기본 태그는 점수에서 제외하지 않고, 단독 보조만 있는 경우는 약하게 처리
    if tags == {"보조"}:
        score -= 2

    # 태그 수가 많으면 조합성이 높다고 보고 소폭 가산
    if len(tags) >= 4:
        score += 1

    return score, matched


def main():
    supports = json.load(open(SUPPORTS_PATH, encoding="utf-8"))

    result = {}

    for archetype_name, archetype in ARCHETYPES.items():
        scored = []

        for support in supports:
            score, matched_tags = score_support(support, archetype)

            if score <= 0:
                continue

            scored.append({
                "name": support["name"],
                "tier": support.get("tier"),
                "score": score,
                "matched_tags": matched_tags,
                "tags": support.get("tags_ko", support.get("tags", [])),
                "tags_en": support.get("tags_en", []),
            })

        scored.sort(key=lambda x: (-x["score"], x["tier"] or 999, x["name"]))

        result[archetype_name] = scored[:30]

    OUT_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Support archetype 매칭 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    for archetype_name, matches in result.items():
        print("=" * 100)
        print(archetype_name)
        print("=" * 100)

        for m in matches[:15]:
            print(
                f"{m['name']} ({m['tier']}) "
                f"score={m['score']} "
                f"matched={m['matched_tags']} "
                f"tags={m['tags']}"
            )

        print()


if __name__ == "__main__":
    main()