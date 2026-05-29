import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILL_SUPPORT_PATH = ROOT / "data" / "meta" / "skill_support_synergy.json"
PASSIVE_SYNERGY_PATH = ROOT / "data" / "skills" / "skill_passive_synergy.json"

OUT_PATH = ROOT / "data" / "meta" / "triple_synergy_candidates.json"


PASSIVE_TAG_WEIGHTS = {
    "trigger": 6,
    "gain_as_extra": 6,
    "crit": 5,
    "projectile": 5,
    "duration": 4,
    "meta_energy": 5,
    "reservation": 3,
    "chain": 5,
    "fork": 5,
    "repeat": 5,
    "shapeshift": 5,
    "consume_charge": 4,
}


def passive_bonus(passives):
    score = 0

    for p in passives:
        text = str(p).lower()

        for tag, weight in PASSIVE_TAG_WEIGHTS.items():
            if tag in text:
                score += weight

    return score


def main():
    skill_support = json.load(open(SKILL_SUPPORT_PATH, encoding="utf-8"))
    passive_data = json.load(open(PASSIVE_SYNERGY_PATH, encoding="utf-8"))

    passive_lookup = {}

    for entry in passive_data:
        skill_name = entry.get("skill")

        if not skill_name:
            continue

        passive_lookup[skill_name] = entry.get("top_passives", [])

    results = []

    for combo in skill_support:
        skill_name = combo["skill"]

        top_passives = passive_lookup.get(skill_name, [])

        p_bonus = min(passive_bonus(top_passives), 20)
        
        total_score = combo["score"] + p_bonus

        if total_score < 8:
            continue

        results.append({
            "skill": skill_name,
            "support": combo["support"],
            "score": total_score,
            "base_score": combo["score"],
            "passive_bonus": p_bonus,
            "shared_tags": combo.get("shared_tags", []),
            "shared_tags_ko": combo.get("shared_tags_ko", combo.get("shared_tags", [])),
            "top_passives": top_passives[:10],
        })

    results.sort(key=lambda x: -x["score"])

    OUT_PATH.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Triple synergy 후보 생성 완료")
    print(f"저장 위치: {OUT_PATH}")
    print()

    print("=" * 100)

    for r in results[:50]:
        print(
            f"{r['skill']} "
            f"+ {r['support']} "
            f"score={r['score']} "
            f"(base={r['base_score']} passive={r['passive_bonus']}) "
            f"shared={r['shared_tags']}"
        )


if __name__ == "__main__":
    main()