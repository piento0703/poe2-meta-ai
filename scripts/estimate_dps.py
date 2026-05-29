import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "meta" / "build_interaction_analysis.json"
OUT_PATH = ROOT / "data" / "meta" / "build_dps_estimates.json"
REPORT_PATH = ROOT / "reports" / "dps_analysis_report.md"


# Heuristic-only relative DPS weights.
# These are not PoB/game-accurate values; they only separate relative DPS factors
# from the existing interaction analysis without inventing real game data.
PROJECTILE_WEIGHT = 0.22
EXTRA_PROJECTILE_WEIGHT = 0.35
RETURNING_PROJECTILE_WEIGHT = 0.18
CHAIN_MAPPING_WEIGHT = 0.45
FORK_MAPPING_WEIGHT = 0.18
PIERCE_MAPPING_WEIGHT = 0.12
OVERLAP_WEIGHT = 0.35
SHOTGUN_WEIGHT = 0.45
TRIGGER_WEIGHT = 0.32
TRIGGER_LOOP_WEIGHT = 0.55
CRIT_WEIGHT = 0.28
CONVERSION_WEIGHT = 0.18
GAIN_AS_EXTRA_WEIGHT = 0.24
AILMENT_WEIGHT = 0.12
CHARGE_WEIGHT = 0.10


BROKEN_COMBO_DPS_HINTS = {
    "Projectile Return Shotgun": {
        "single_target": 0.55,
        "mapping": 0.10,
        "why": "돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음",
    },
    "Projectile Chain Overlap": {
        "single_target": 0.20,
        "mapping": 0.45,
        "why": "연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음",
    },
    "Extra Projectile Shotgun": {
        "single_target": 0.40,
        "mapping": 0.18,
        "why": "추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음",
    },
    "Gain As Extra Conversion Stack": {
        "single_target": 0.22,
        "mapping": 0.18,
        "why": "추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음",
    },
    "Trigger Crit Engine": {
        "single_target": 0.24,
        "mapping": 0.18,
        "why": "치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음",
    },
    "Trigger Loop Candidate": {
        "single_target": 0.35,
        "mapping": 0.30,
        "why": "발동 조건이 다시 발동 조건을 만드는 구조라면 반복 발동 후보가 될 수 있음",
    },
}


def load_json(path, default=None):
    if default is None:
        default = []

    if not path.exists():
        print(f"[WARN] missing file: {path}")
        return default

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"저장 완료: {path}")


def save_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"저장 완료: {path}")


def clamp_multiplier(value, minimum=1.0, maximum=5.0):
    return round(max(minimum, min(maximum, value)), 3)


def score_base(build):
    # Keep the score relative and bounded. Existing interaction/build scores are
    # already heuristic, so this normalizes them without treating them as real DPS.
    interaction_score = float(build.get("interaction_score", 0) or 0)
    base_build_score = float(build.get("base_build_score", 0) or 0)
    source_score = interaction_score or base_build_score

    if source_score <= 0:
        return 100.0

    return round(max(60.0, min(180.0, source_score / 7.5)), 3)


def collect_mechanics(build):
    mechanics = set(build.get("mechanics", []))

    for unique in build.get("recommended_uniques", []):
        for key in ["matched_tags", "unique_tags"]:
            for tag in unique.get(key, []):
                mechanics.add(tag)

    for affix in build.get("recommended_rare_affixes", []):
        for mechanic in affix.get("mechanics", []):
            mechanics.add(mechanic)

    for combo in build.get("broken_combos", []):
        for mechanic in combo.get("requires", []):
            mechanics.add(mechanic)

    return sorted(mechanics)


def collect_combo_names(build):
    names = []

    for combo in build.get("broken_combos", []):
        name = combo.get("name")
        if name:
            names.append(name)

    return names


def add_if_present(why, mechanics, mechanic_id, text):
    if mechanic_id in mechanics:
        why.append(text)


def estimate_multipliers(mechanics, combo_names):
    mechanic_set = set(mechanics)
    combo_single_bonus = 0.0
    combo_mapping_bonus = 0.0
    why = []

    projectile_multiplier = 1.0
    if "projectile" in mechanic_set:
        projectile_multiplier += PROJECTILE_WEIGHT
    if "extra_projectile" in mechanic_set:
        projectile_multiplier += EXTRA_PROJECTILE_WEIGHT
    if "returning_projectile" in mechanic_set:
        projectile_multiplier += RETURNING_PROJECTILE_WEIGHT

    overlap_multiplier = 1.0
    if "overlap" in mechanic_set:
        overlap_multiplier += OVERLAP_WEIGHT
    if "shotgun" in mechanic_set:
        overlap_multiplier += SHOTGUN_WEIGHT

    trigger_frequency_multiplier = 1.0
    if "trigger" in mechanic_set:
        trigger_frequency_multiplier += TRIGGER_WEIGHT
    if "trigger_loop" in mechanic_set:
        trigger_frequency_multiplier += TRIGGER_LOOP_WEIGHT

    crit_multiplier = 1.0
    if "crit_scaling" in mechanic_set or "crit" in mechanic_set:
        crit_multiplier += CRIT_WEIGHT

    conversion_multiplier = 1.0
    if "conversion" in mechanic_set:
        conversion_multiplier += CONVERSION_WEIGHT

    gain_as_extra_multiplier = 1.0
    if "gain_as_extra" in mechanic_set:
        gain_as_extra_multiplier += GAIN_AS_EXTRA_WEIGHT

    mapping_clear_multiplier = 1.0
    if "chain" in mechanic_set:
        mapping_clear_multiplier += CHAIN_MAPPING_WEIGHT
    if "fork" in mechanic_set:
        mapping_clear_multiplier += FORK_MAPPING_WEIGHT
    if "pierce" in mechanic_set:
        mapping_clear_multiplier += PIERCE_MAPPING_WEIGHT
    if "ailment_scaling" in mechanic_set:
        mapping_clear_multiplier += AILMENT_WEIGHT
    if "charge_scaling" in mechanic_set or "charge" in mechanic_set:
        mapping_clear_multiplier += CHARGE_WEIGHT

    for combo_name in combo_names:
        hint = BROKEN_COMBO_DPS_HINTS.get(combo_name)
        if not hint:
            continue

        combo_single_bonus += hint["single_target"]
        combo_mapping_bonus += hint["mapping"]
        why.append(hint["why"])

    add_if_present(why, mechanic_set, "extra_projectile", "추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림")
    add_if_present(why, mechanic_set, "returning_projectile", "돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함")
    add_if_present(why, mechanic_set, "shotgun", "다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함")
    add_if_present(why, mechanic_set, "overlap", "범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음")
    add_if_present(why, mechanic_set, "trigger", "발동 메커닉이 있어 수동 시전/공격 외 추가 발생 빈도를 상대 점수로 반영함")
    add_if_present(why, mechanic_set, "trigger_loop", "발동 루프 후보는 실제 합법성 검증 전까지는 강한 후보로만 가중함")
    add_if_present(why, mechanic_set, "crit_scaling", "치명타 스케일링이 있어 hit 기반 DPS 증폭 축으로 반영함")
    add_if_present(why, mechanic_set, "conversion", "피해 전환 메커닉이 있어 복수 피해 타입 스케일링 가능성을 반영함")
    add_if_present(why, mechanic_set, "gain_as_extra", "추가 피해 획득 메커닉이 있어 전환/원소 스케일링과의 결합 가능성을 반영함")
    add_if_present(why, mechanic_set, "chain", "연쇄 메커닉이 있어 mapping_score에 강한 가중치를 부여함")

    return {
        "projectile_multiplier": clamp_multiplier(projectile_multiplier),
        "overlap_multiplier": clamp_multiplier(overlap_multiplier),
        "trigger_frequency_multiplier": clamp_multiplier(trigger_frequency_multiplier),
        "crit_multiplier": clamp_multiplier(crit_multiplier),
        "conversion_multiplier": clamp_multiplier(conversion_multiplier),
        "gain_as_extra_multiplier": clamp_multiplier(gain_as_extra_multiplier),
        "mapping_clear_multiplier": clamp_multiplier(mapping_clear_multiplier),
        "combo_single_target_bonus": round(combo_single_bonus, 3),
        "combo_mapping_bonus": round(combo_mapping_bonus, 3),
        "why": why,
    }


def estimate_build_dps(build):
    mechanics = collect_mechanics(build)
    combo_names = collect_combo_names(build)
    base_score = score_base(build)
    multipliers = estimate_multipliers(mechanics, combo_names)

    single_target_multiplier = (
        multipliers["projectile_multiplier"]
        * multipliers["overlap_multiplier"]
        * multipliers["trigger_frequency_multiplier"]
        * multipliers["crit_multiplier"]
        * multipliers["conversion_multiplier"]
        * multipliers["gain_as_extra_multiplier"]
        * (1 + multipliers["combo_single_target_bonus"])
    )

    mapping_multiplier = (
        multipliers["projectile_multiplier"]
        * multipliers["mapping_clear_multiplier"]
        * multipliers["trigger_frequency_multiplier"]
        * max(1.0, multipliers["overlap_multiplier"] * 0.82)
        * multipliers["crit_multiplier"]
        * multipliers["conversion_multiplier"]
        * multipliers["gain_as_extra_multiplier"]
        * (1 + multipliers["combo_mapping_bonus"])
    )

    single_target_score = round(base_score * single_target_multiplier, 3)
    mapping_score = round(base_score * mapping_multiplier, 3)
    estimated_dps_score = round((single_target_score * 0.58) + (mapping_score * 0.42), 3)

    skipped = []
    todo = [
        "TODO: 실제 PoB/게임 수치가 아닌 현재 메커닉 태그 기반 상대 DPS 추정치입니다.",
        "TODO: 다음 단계에서 support compatibility, weapon restriction, trigger legality 검증 결과와 결합해야 합니다.",
    ]

    if not build.get("recommended_rare_affixes"):
        skipped.append("rare_affix: 추천 희귀 affix 데이터가 없어 rare affix 기반 DPS 가중치를 생략했습니다.")
    if not mechanics:
        skipped.append("mechanics: 메커닉 태그가 없어 기본 상대 점수만 사용했습니다.")

    why = multipliers.pop("why")
    if not why:
        why = ["감지된 고위험 DPS 메커닉이 적어 기본 상호작용 점수 중심으로 추정했습니다."]

    hit_model = {
        "base_relative_score": base_score,
        "base_hit_count": 1,
        "projectile_multiplier": multipliers["projectile_multiplier"],
        "overlap_multiplier": multipliers["overlap_multiplier"],
        "trigger_frequency_multiplier": multipliers["trigger_frequency_multiplier"],
        "crit_multiplier": multipliers["crit_multiplier"],
        "conversion_multiplier": multipliers["conversion_multiplier"],
        "gain_as_extra_multiplier": multipliers["gain_as_extra_multiplier"],
        "mapping_clear_multiplier": multipliers["mapping_clear_multiplier"],
        "combo_single_target_bonus": multipliers["combo_single_target_bonus"],
        "combo_mapping_bonus": multipliers["combo_mapping_bonus"],
        "model_notes": [
            "Relative DPS approximation only; exact hit rate, cast rate, ailment magnitude, monster size, and cooldown breakpoints are not modeled.",
            "All internal mechanics remain canonical English ids; Korean text is report/explanation only.",
        ],
    }

    return {
        "build_name": build.get("build_name", ""),
        "main_skill": build.get("main_skill", ""),
        "archetype_label_ko": build.get("archetype_label_ko", ""),
        "base_build_score": build.get("base_build_score", 0),
        "interaction_score": build.get("interaction_score", 0),
        "estimated_dps_score": estimated_dps_score,
        "single_target_score": single_target_score,
        "mapping_score": mapping_score,
        "hit_model": hit_model,
        "projectile_multiplier": hit_model["projectile_multiplier"],
        "overlap_multiplier": hit_model["overlap_multiplier"],
        "trigger_frequency_multiplier": hit_model["trigger_frequency_multiplier"],
        "crit_multiplier": hit_model["crit_multiplier"],
        "conversion_multiplier": hit_model["conversion_multiplier"],
        "gain_as_extra_multiplier": hit_model["gain_as_extra_multiplier"],
        "mechanics": mechanics,
        "broken_combos": build.get("broken_combos", []),
        "explanation": why,
        "why": why,
        "skipped": skipped,
        "todo": todo,
    }


def estimate_dps(builds):
    results = [estimate_build_dps(build) for build in builds]
    results.sort(key=lambda x: x["estimated_dps_score"], reverse=True)
    return results


def fmt_list(items):
    if not items:
        return "- 없음"

    return "\n".join(f"- {item}" for item in items)


def generate_report(results, source_path):
    lines = [
        "# DPS Approximation Report",
        "",
        "> 이 리포트는 정확한 PoB DPS가 아니라 현재 메커닉 태그와 상호작용 분석을 이용한 상대 DPS 추정입니다.",
        "> 실제 게임 수치, 쿨다운 breakpoints, 보스 크기, 투사체 궤적, hit rate는 아직 모델링하지 않습니다.",
        "",
        "## 입력 / 출력",
        "",
        f"- 입력: `{source_path}`",
        f"- JSON 출력: `{OUT_PATH.relative_to(ROOT)}`",
        f"- 리포트 출력: `{REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## 모델링 범위",
        "",
        "- 포함: projectile, overlap, trigger frequency, crit, conversion, gain-as-extra, chain/fork/pierce mapping 가중치",
        "- 미포함: 실제 gem 레벨 수치, 무기 DPS, 공격/시전 속도 실측값, 쿨다운 breakpoints, 몬스터 크기, 실제 투사체 경로",
        "- 누락 데이터는 결과 JSON의 `todo` 또는 `skipped` 필드에 표시합니다.",
        "",
        "## 요약",
        "",
        f"- 분석 빌드 수: {len(results)}",
    ]

    if results:
        top = results[0]
        lines.extend([
            f"- 최고 추정 DPS 후보: {top['build_name']} / estimated_dps_score {top['estimated_dps_score']}",
            "",
            "## Top DPS Candidates",
            "",
        ])
    else:
        lines.extend([
            "- 분석할 빌드가 없습니다.",
            "- TODO: `data/meta/build_interaction_analysis.json` 생성 후 다시 실행하세요.",
            "",
        ])

    for index, result in enumerate(results[:25], start=1):
        hit_model = result["hit_model"]
        lines.extend([
            f"### {index}. {result['build_name']}",
            "",
            f"- 메인 스킬: {result['main_skill']}",
            f"- 아키타입: {result['archetype_label_ko']}",
            f"- estimated_dps_score: {result['estimated_dps_score']}",
            f"- single_target_score: {result['single_target_score']}",
            f"- mapping_score: {result['mapping_score']}",
            f"- projectile_multiplier: {hit_model['projectile_multiplier']}",
            f"- overlap_multiplier: {hit_model['overlap_multiplier']}",
            f"- trigger_frequency_multiplier: {hit_model['trigger_frequency_multiplier']}",
            f"- crit_multiplier: {hit_model['crit_multiplier']}",
            f"- conversion_multiplier: {hit_model['conversion_multiplier']}",
            f"- gain_as_extra_multiplier: {hit_model['gain_as_extra_multiplier']}",
            "",
            "#### 왜 강한가",
            "",
            fmt_list(result["why"]),
            "",
        ])

        if result["skipped"]:
            lines.extend([
                "#### Skipped / TODO",
                "",
                fmt_list(result["skipped"]),
                "",
            ])

    return "\n".join(lines).rstrip() + "\n"


def main():
    builds = load_json(INPUT_PATH)

    if not builds:
        print("[WARN] 입력 빌드가 없습니다. 빈 DPS 결과와 TODO 리포트를 생성합니다.")

    results = estimate_dps(builds)
    save_json(OUT_PATH, results)
    save_text(REPORT_PATH, generate_report(results, INPUT_PATH.relative_to(ROOT)))

    print(f"loaded builds: {len(builds)}")
    print(f"estimated dps builds: {len(results)}")

    for result in results[:10]:
        print("=" * 80)
        print(f"빌드명: {result['build_name']}")
        print(f"추정 DPS 점수: {result['estimated_dps_score']}")
        print(f"단일 대상: {result['single_target_score']} / 맵핑: {result['mapping_score']}")
        print(f"이유: {', '.join(result['why'][:3])}")


if __name__ == "__main__":
    main()
