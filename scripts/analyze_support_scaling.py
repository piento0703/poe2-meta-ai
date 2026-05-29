import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SUPPORTS_PATH = ROOT / "data" / "supports" / "supports.json"
OUT_PATH = ROOT / "data" / "supports" / "support_scaling_analysis.json"


SCALING_PATTERNS = {
    "more_damage": [
        r"more damage",
        r"더 많은 피해",
    ],

    "increased_damage": [
        r"increased damage",
        r"증가된 피해",
    ],

    "gain_as_extra": [
        r"gain.*as extra",
        r"추가.*획득",
    ],

    "chain": [
        r"chain",
        r"연쇄",
    ],

    "fork": [
        r"fork",
    ],

    "repeat": [
        r"repeat",
        r"반복",
    ],

    "trigger": [
        r"trigger",
        r"발동",
    ],

    "extra_projectile": [
        r"additional projectile",
        r"추가 투사체",
    ],

    "conversion": [
        r"converted to",
        r"전환",
    ],

    "duration_scaling": [
        r"duration",
        r"지속시간",
    ],

    "cooldown": [
        r"cooldown",
        r"재사용 대기시간",
    ],
}


WEIGHTS = {
    "more_damage": 10,
    "gain_as_extra": 9,
    "trigger": 8,
    "repeat": 7,
    "extra_projectile": 7,
    "chain": 6,
    "fork": 6,
    "conversion": 6,
    "duration_scaling": 4,
    "cooldown": 3,
    "increased_damage": 2,
}


def analyze_support(support):
    raw_text = (
        support.get("raw_text", "")
        + " "
        + " ".join(support.get("tags_ko", []))
    ).lower()

    found = []
    score = 0

    for category, patterns in SCALING_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, raw_text):
                found.append(category)
                score += WEIGHTS.get(category, 1)
                break

    return {
        "name": support["name"],
        "tier": support.get("tier"),
        "tags": support.get("tags_ko", []),
        "scaling_tags": sorted(set(found)),
        "scaling_score": score,
    }


def main():
    supports = json.load(open(SUPPORTS_PATH, encoding="utf-8"))

    analyzed = []

    for support in supports:
        result = analyze_support(support)

        if result["scaling_score"] > 0:
            analyzed.append(result)

    analyzed.sort(
        key=lambda x: (
            -x["scaling_score"],
            x["tier"] or 999,
            x["name"]
        )
    )

    OUT_PATH.write_text(
        json.dumps(analyzed, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Support scaling 분석 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("=" * 100)

    for s in analyzed[:50]:
        print(
            f"{s['name']} "
            f"score={s['scaling_score']} "
            f"scaling={s['scaling_tags']} "
            f"tags={s['tags']}"
        )


if __name__ == "__main__":
    main()