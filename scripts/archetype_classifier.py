import re
from collections import Counter


ARCHETYPE_RULES = {
    "trigger": {
        "ko": "발동",
        "weight": 1.35,
        "keywords": ["trigger", "meta_energy", "cast_on", "발동"],
    },
    "projectile": {
        "ko": "투사체",
        "weight": 1.25,
        "keywords": ["projectile", "extra_projectile", "pierce", "fork", "투사체", "관통", "갈라짐"],
    },
    "chain": {
        "ko": "연쇄",
        "weight": 1.3,
        "keywords": ["chain", "연쇄"],
    },
    "lightning": {
        "ko": "번개",
        "weight": 1.2,
        "keywords": ["lightning", "shock", "번개", "감전"],
    },
    "fire": {
        "ko": "화염",
        "weight": 1.15,
        "keywords": ["fire", "ignite", "burning", "화염", "점화", "연소"],
    },
    "cold": {
        "ko": "냉기",
        "weight": 1.15,
        "keywords": ["cold", "freeze", "chill", "냉기", "동결", "냉각"],
    },
    "chaos": {
        "ko": "카오스",
        "weight": 1.15,
        "keywords": ["chaos", "poison", "카오스", "중독"],
    },
    "crit": {
        "ko": "치명타",
        "weight": 1.15,
        "keywords": ["crit", "critical", "치명타"],
    },
    "minion": {
        "ko": "소환수",
        "weight": 1.25,
        "keywords": ["minion", "소환수"],
    },
    "grenade": {
        "ko": "수류탄",
        "weight": 1.25,
        "keywords": ["grenade", "수류탄"],
    },
    "duration": {
        "ko": "지속시간",
        "weight": 1.1,
        "keywords": ["duration", "지속시간"],
    },
    "aoe": {
        "ko": "효과 범위",
        "weight": 1.1,
        "keywords": ["aoe", "area", "효과 범위", "범위"],
    },
    "melee": {
        "ko": "근접",
        "weight": 1.1,
        "keywords": ["melee", "slam", "strike", "근접", "타격"],
    },
    "totem": {
        "ko": "토템",
        "weight": 1.15,
        "keywords": ["totem", "토템"],
    },
    "bleed": {
        "ko": "출혈",
        "weight": 1.1,
        "keywords": ["bleed", "bleeding", "출혈"],
    },
}


SCALING_RULES = {
    "crit": ["crit", "critical", "치명타"],
    "cast_speed": ["cast_speed", "cast speed", "시전 속도"],
    "attack_speed": ["attack_speed", "attack speed", "공격 속도"],
    "projectile_count": ["extra_projectile", "additional projectile", "추가 투사체"],
    "chain_count": ["chain", "연쇄"],
    "elemental_damage": ["elemental", "fire", "cold", "lightning", "원소", "화염", "냉기", "번개"],
    "duration": ["duration", "지속시간"],
    "minion_damage": ["minion", "소환수"],
}


def normalize_text(value):
    if value is None:
        return ""

    if isinstance(value, list):
        return " ".join(normalize_text(v) for v in value)

    if isinstance(value, dict):
        return " ".join(normalize_text(v) for v in value.values())

    text = str(value).lower()
    text = re.sub(r"[_\-/,|]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def collect_tags(candidate):
    tags = []

    possible_keys = [
        "tags",
        "tags_en",
        "tags_ko",
        "shared_tags",
        "shared_tags_en",
        "skill_tags",
        "support_tags",
        "passive_tags",
        "unique_tags",
        "matched_tags",
    ]

    for key in possible_keys:
        value = candidate.get(key)
        if isinstance(value, list):
            tags.extend(value)
        elif isinstance(value, str):
            tags.append(value)

    for section_key in ["skill", "support", "passive", "unique", "item"]:
        section = candidate.get(section_key)
        if isinstance(section, dict):
            for key in possible_keys:
                value = section.get(key)
                if isinstance(value, list):
                    tags.extend(value)
                elif isinstance(value, str):
                    tags.append(value)

    return tags


def score_archetypes(candidate):
    text = normalize_text(candidate)
    tags = collect_tags(candidate)
    tag_text = normalize_text(tags)

    combined = f"{text} {tag_text}"

    scores = {}

    for archetype, rule in ARCHETYPE_RULES.items():
        raw_score = 0

        for keyword in rule["keywords"]:
            keyword_norm = normalize_text(keyword)
            if keyword_norm and keyword_norm in combined:
                raw_score += 1

        if raw_score > 0:
            scores[archetype] = round(raw_score * rule["weight"], 3)

    apply_combo_bonus(scores)

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))


def apply_combo_bonus(scores):
    if "trigger" in scores and "projectile" in scores:
        scores["trigger"] += 0.5
        scores["projectile"] += 0.3

    if "projectile" in scores and "chain" in scores:
        scores["projectile"] += 0.4
        scores["chain"] += 0.5

    if "lightning" in scores and "chain" in scores:
        scores["lightning"] += 0.4
        scores["chain"] += 0.3

    if "grenade" in scores and "duration" in scores:
        scores["grenade"] += 0.4
        scores["duration"] += 0.3

    if "minion" in scores and "duration" in scores:
        scores["minion"] += 0.4


def classify_archetypes(candidate, limit=4, min_score=1.0):
    scores = score_archetypes(candidate)

    archetypes = [
        name
        for name, score in scores.items()
        if score >= min_score
    ][:limit]

    return archetypes


def classify_scaling(candidate, limit=4):
    text = normalize_text(candidate)
    counter = Counter()

    for scaling, keywords in SCALING_RULES.items():
        for keyword in keywords:
            if normalize_text(keyword) in text:
                counter[scaling] += 1

    return [name for name, _ in counter.most_common(limit)]


def archetype_to_korean(archetype):
    return ARCHETYPE_RULES.get(archetype, {}).get("ko", archetype)


def build_archetype_label(archetypes, lang="en"):
    if lang == "ko":
        return " ".join(archetype_to_korean(a) for a in archetypes)

    return " ".join(a.replace("_", " ").title() for a in archetypes)


def classify_build(candidate):
    archetypes = classify_archetypes(candidate)
    scaling = classify_scaling(candidate)

    return {
        "archetypes": archetypes,
        "archetype_label_en": build_archetype_label(archetypes, "en"),
        "archetype_label_ko": build_archetype_label(archetypes, "ko"),
        "main_scaling": scaling,
        "archetype_scores": score_archetypes(candidate),
    }


if __name__ == "__main__":
    sample = {
        "skill": {
            "name": "원소 표현",
            "tags_en": ["spell", "projectile", "trigger", "lightning"],
        },
        "support": {
            "name": "세차게 흐르는 전류",
            "tags_en": ["chain", "lightning", "projectile"],
        },
        "shared_tags": ["trigger", "projectile", "chain", "lightning"],
    }

    result = classify_build(sample)

    print(result)