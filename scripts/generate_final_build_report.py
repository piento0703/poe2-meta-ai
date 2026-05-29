import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BUILDS_PATH = ROOT / "data" / "meta" / "generated_builds_filtered.json"
OUT_PATH = ROOT / "data" / "meta" / "final_build_report.md"


ROLE_KO = {
    "engine": "엔진",
    "scaling": "스케일링",
    "conversion": "전환",
    "enable": "활성화",
    "support": "보조",
}


SCALING_KO = {
    "crit": "치명타",
    "cast_speed": "시전 속도",
    "attack_speed": "공격 속도",
    "projectile_count": "투사체 수",
    "chain_count": "연쇄 횟수",
    "elemental_damage": "원소 피해",
    "duration": "지속시간",
    "minion_damage": "소환수 피해",
}


def load_json(path):
    if not path.exists():
        raise FileNotFoundError(f"missing file: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"저장 완료: {path}")


def fmt_list(items):
    if not items:
        return "- 없음"

    return "\n".join(f"- {item}" for item in items)


def fmt_scaling(items):
    if not items:
        return "- 미분류"

    return "\n".join(f"- {SCALING_KO.get(item, item)}" for item in items)


def fmt_uniques(uniques):
    if not uniques:
        return "- 없음"

    lines = []

    for unique in uniques:
        name = unique.get("name", "")
        canonical_name = unique.get("canonical_name", "")
        role = ROLE_KO.get(unique.get("role", ""), unique.get("role", ""))
        score = unique.get("score", 0)
        matched_tags_ko = unique.get("matched_tags_ko", [])

        tag_text = ", ".join(matched_tags_ko) if matched_tags_ko else "태그 없음"

        if canonical_name and canonical_name != name:
            lines.append(
                f"- {name} ({canonical_name}) / 역할: {role} / 점수: {score} / 매칭: {tag_text}"
            )
        else:
            lines.append(
                f"- {name} / 역할: {role} / 점수: {score} / 매칭: {tag_text}"
            )

    return "\n".join(lines)


def infer_strengths(build):
    archetypes = set(build.get("archetypes", []))
    supports = build.get("recommended_supports", [])
    uniques = build.get("recommended_uniques", [])

    strengths = []

    if "projectile" in archetypes:
        strengths.append("투사체 기반 확장성이 높음")

    if "chain" in archetypes:
        strengths.append("연쇄 기반 화면 정리 능력이 좋음")

    if "trigger" in archetypes:
        strengths.append("발동 구조를 통한 자동화된 딜 사이클 가능성")

    if "lightning" in archetypes:
        strengths.append("번개/감전 기반 순간 화력 확장 가능성")

    if "cold" in archetypes:
        strengths.append("냉기 기반 제어력과 안정성 확보 가능")

    if "fire" in archetypes:
        strengths.append("화염/점화 기반 지속 피해 확장 가능")

    if "minion" in archetypes:
        strengths.append("소환수 기반 자동 전투 구조 가능성")

    if "grenade" in archetypes:
        strengths.append("수류탄/지속시간 기반 폭발 딜 구조 가능성")

    if len(supports) >= 6:
        strengths.append("6링크 구성 후보가 충분함")

    if len(uniques) >= 3:
        strengths.append("유니크 장비 연계 후보가 충분함")

    return strengths or ["뚜렷한 강점은 추가 검증 필요"]


def infer_weaknesses(build):
    archetypes = set(build.get("archetypes", []))
    supports = build.get("recommended_supports", [])
    uniques = build.get("recommended_uniques", [])
    scaling = build.get("main_scaling", [])

    weaknesses = []

    if not uniques:
        weaknesses.append("유니크 연계 근거가 부족함")

    if len(supports) < 4:
        weaknesses.append("보조젬 후보 수가 부족함")

    if "trigger" in archetypes and "crit" not in scaling:
        weaknesses.append("발동 빌드인데 치명타/발동 조건 검증이 추가로 필요함")

    if "projectile" in archetypes and "chain" not in archetypes:
        weaknesses.append("투사체 확장은 있으나 연쇄/관통 구조 보강 필요")

    if build.get("validity_penalty", 0) > 0:
        weaknesses.append("스킬 본체와 일부 추천 태그 간 불일치 가능성 있음")

    return weaknesses or ["명확한 약점은 자동 분석 기준에서 확인되지 않음"]


def infer_warnings(build):
    warnings = []

    if build.get("validity_penalty", 0) >= 80:
        warnings.append("유효성 패널티가 높으므로 실제 게임 내 장착 가능 여부 확인 필요")

    if build.get("candidate_count", 0) < 3:
        warnings.append("후보 조합 수가 적어 통계적 신뢰도가 낮음")

    if build.get("support_count", 0) < 6:
        warnings.append("6링크 완성도가 낮을 수 있음")

    if not build.get("recommended_uniques"):
        warnings.append("유니크 추천 근거가 부족함")

    return warnings or ["특이 주의사항 없음"]


def fmt_build(build, rank):
    title = build.get("build_name", "알 수 없는 빌드")
    score = build.get("build_score", 0)
    original_score = build.get("original_build_score", score)
    validity_penalty = build.get("validity_penalty", 0)
    validity_reasons = build.get("validity_reasons", [])

    main_skill = build.get("main_skill", "")
    archetype_ko = build.get("archetype_label_ko", "")
    archetype_en = build.get("archetype_label_en", "")

    supports = build.get("recommended_supports", [])
    passives = build.get("passive_direction", [])
    uniques = build.get("recommended_uniques", [])
    scaling = build.get("main_scaling", [])

    strengths = infer_strengths(build)
    weaknesses = infer_weaknesses(build)
    warnings = infer_warnings(build)

    candidate_count = build.get("candidate_count", 0)
    support_count = build.get("support_count", 0)
    passive_count = build.get("passive_count", 0)

    return f"""## {rank}. {title}

### 요약

| 항목 | 내용 |
|---|---|
| 최종 빌드 점수 | {score} |
| 원점수 | {original_score} |
| 유효성 패널티 | {validity_penalty} |
| 메인 스킬 | {main_skill} |
| 아키타입 | {archetype_ko} |
| Archetype EN | {archetype_en} |
| 후보 조합 수 | {candidate_count} |
| 보조젬 후보 수 | {support_count} |
| 패시브 후보 수 | {passive_count} |

### 추천 6링크 보조젬

{fmt_list(supports[:6])}

### 추천 패시브 방향

{fmt_list(passives[:10])}

### 추천 유니크

{fmt_uniques(uniques)}

### 핵심 스케일링

{fmt_scaling(scaling)}

### 예상 강점

{fmt_list(strengths)}

### 예상 약점

{fmt_list(weaknesses)}

### 주의사항

{fmt_list(warnings)}

### 유효성 패널티 사유

{fmt_list(validity_reasons)}

### 해석

이 빌드는 `{archetype_ko}` 구조로 분류된다.  
점수는 스킬·보조젬·패시브·유니크 태그의 중첩도와 조합 보너스에 유효성 패널티를 반영해 산출됐다.

---
"""


def generate_report(builds, limit=30):
    lines = []

    lines.append("# PoE2 Meta AI 최종 빌드 추천 리포트")
    lines.append("")
    lines.append("이 문서는 `generated_builds_filtered.json`을 기반으로 자동 생성된 빌드 후보 리포트다.")
    lines.append("")
    lines.append("## 생성 기준")
    lines.append("")
    lines.append("- 메인 스킬 기준 후보 그룹화")
    lines.append("- 추천 보조젬 6링크 자동 추출")
    lines.append("- 패시브 방향 자동 요약")
    lines.append("- 유니크 추천 및 역할 분류")
    lines.append("- archetype / scaling 자동 분류")
    lines.append("- build_score 기준 정렬")
    lines.append("- 유효성 패널티 반영")
    lines.append("- 강점 / 약점 / 주의사항 자동 해석")
    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, build in enumerate(builds[:limit], start=1):
        lines.append(fmt_build(build, idx))

    return "\n".join(lines)


def main():
    builds = load_json(BUILDS_PATH)

    print(f"loaded builds: {len(builds)}")

    report = generate_report(builds, limit=30)

    save_text(OUT_PATH, report)

    print(f"report builds: {min(len(builds), 30)}")


if __name__ == "__main__":
    main()