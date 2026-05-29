import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTERACTION_PATH = ROOT / "data" / "meta" / "build_interaction_analysis.json"
DPS_PATH = ROOT / "data" / "meta" / "build_dps_estimates.json"
OUT_PATH = ROOT / "data" / "meta" / "build_legality_analysis.json"
REPORT_PATH = ROOT / "reports" / "legality_report.md"
SUPPORTS_PATH = ROOT / "data" / "supports" / "supports.json"
SKILLS_PATH = ROOT / "data" / "skills" / "skills.json"


# Conservative checks only. Exact PoE2 support/weapon/trigger legality data is not
# available in this repository yet, so missing exact rules are reported as TODO or
# skipped instead of being treated as certain legality decisions.
CORE_SUPPORT_TAGS = {
    "projectile",
    "chain",
    "fork",
    "pierce",
    "aoe",
    "duration",
    "fire",
    "cold",
    "lightning",
    "chaos",
    "physical",
    "minion",
    "trigger",
    "crit",
    "ailment",
    "persistent",
    "grenade",
    "slam",
    "melee",
    "attack",
    "spell",
}

CONFLICTING_SCALING_GROUPS = [
    {
        "name": "minion_non_minion_scaling_mix",
        "requires": {"minion"},
        "conflicts_with_any": {"projectile", "attack", "spell", "melee", "slam", "grenade"},
        "message": "소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.",
    },
    {
        "name": "attack_spell_scaling_mix",
        "requires": {"attack"},
        "conflicts_with_any": {"spell"},
        "message": "공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.",
    },
]

TRIGGER_MECHANICS = {"trigger", "trigger_loop", "meta_energy"}
TRIGGER_SUPPORT_KEYWORDS = ["발동", "시전", "trigger", "cast"]
WEAPON_AFFIX_SLOTS = {"weapon", "quiver"}
WEAPON_BASE_HINTS = ["staff", "bow", "club", "mace", "sword", "axe", "spear", "crossbow", "wand", "quarterstaff"]


def load_json(path, default=None, *, required=False):
    if default is None:
        default = []

    if not path.exists():
        if required:
            raise FileNotFoundError(f"missing required file: {path}")
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


def normalize_key(value):
    return str(value or "").strip().lower()


def build_index(items, key="name"):
    index = {}
    for item in items:
        value = item.get(key)
        if value:
            index[normalize_key(value)] = item
    return index


def merge_build_sources(interaction_builds, dps_builds):
    dps_index = {normalize_key(item.get("build_name")): item for item in dps_builds}
    merged = []

    for build in interaction_builds:
        name_key = normalize_key(build.get("build_name"))
        combined = dict(build)
        dps = dps_index.get(name_key)
        if dps:
            combined["dps_analysis"] = dps
        merged.append(combined)

    return merged


def collect_mechanics(build):
    mechanics = set(build.get("mechanics", []))

    dps = build.get("dps_analysis", {})
    for mechanic in dps.get("mechanics", []):
        mechanics.add(mechanic)

    for unique in build.get("recommended_uniques", []):
        for key in ["matched_tags", "unique_tags"]:
            for tag in unique.get(key, []):
                mechanics.add(tag)

    for affix in build.get("recommended_rare_affixes", []):
        for mechanic in affix.get("mechanics", []):
            mechanics.add(mechanic)

    return sorted(mechanics)


def collect_support_tags(build, support_index):
    support_details = []
    missing_supports = []
    all_tags = set()

    for support_name in build.get("recommended_supports", []):
        support = support_index.get(normalize_key(support_name))
        if not support:
            missing_supports.append(support_name)
            continue

        tags = set(support.get("tags_en", [])) | set(support.get("meta_tags", []))
        all_tags.update(tags)
        support_details.append({
            "name": support_name,
            "tags": sorted(tags),
        })

    return sorted(all_tags), support_details, missing_supports


def get_skill_tags(build, skill_index):
    skill_name = build.get("main_skill", "")
    skill = skill_index.get(normalize_key(skill_name))
    if not skill:
        return [], skill_name

    return sorted(set(skill.get("tags_en", []))), skill_name


def status_result(status, score_penalty=0, *, violations=None, warnings=None, missing_data=None, details=None):
    return {
        "status": status,
        "score_penalty": score_penalty,
        "violations": violations or [],
        "warnings": warnings or [],
        "missing_data": missing_data or [],
        "details": details or {},
    }


def validate_support_compatibility(build, support_index, skill_index):
    support_tags, support_details, missing_supports = collect_support_tags(build, support_index)
    skill_tags, skill_name = get_skill_tags(build, skill_index)
    warnings = []
    missing_data = []
    violations = []
    penalty = 0

    if not skill_tags:
        missing_data.append({
            "type": "skill_tags_missing",
            "message": f"메인 스킬 `{skill_name}`의 정확한 태그 데이터를 찾지 못해 support compatibility를 완전 검증하지 못했습니다.",
        })
        penalty += 5

    if missing_supports:
        missing_data.append({
            "type": "support_tags_missing",
            "supports": missing_supports,
            "message": "일부 추천 보조젬의 태그 데이터를 찾지 못해 해당 보조젬 호환성 검증을 건너뜁니다.",
        })
        penalty += min(15, len(missing_supports) * 3)

    if skill_tags and support_tags:
        core_skill_tags = set(skill_tags) & CORE_SUPPORT_TAGS
        core_support_tags = set(support_tags) & CORE_SUPPORT_TAGS
        overlap = sorted(core_skill_tags & core_support_tags)

        if not overlap:
            warnings.append({
                "type": "low_tag_overlap",
                "message": "메인 스킬 태그와 추천 보조젬 핵심 태그의 직접 교집합이 낮습니다. 실제 support compatibility 데이터로 재검증이 필요합니다.",
                "skill_core_tags": sorted(core_skill_tags),
                "support_core_tags": sorted(core_support_tags),
            })
            penalty += 12
    else:
        overlap = []

    if not build.get("recommended_supports"):
        warnings.append({
            "type": "no_recommended_supports",
            "message": "추천 보조젬 목록이 없어 support compatibility를 평가할 수 없습니다.",
        })
        penalty += 8

    if missing_data and not warnings and not violations:
        status = "skipped_missing_data"
    elif violations:
        status = "failed"
    elif warnings or missing_data:
        status = "warning"
    else:
        status = "passed_heuristic"

    return status_result(
        status,
        penalty,
        violations=violations,
        warnings=warnings,
        missing_data=missing_data,
        details={
            "skill_name": skill_name,
            "skill_tags": skill_tags,
            "support_tags": support_tags,
            "support_details": support_details,
            "shared_core_tags": overlap,
            "note": "정확한 보조젬 허용/불허 규칙 데이터가 없어 태그 겹침 기반의 보수적 휴리스틱만 적용했습니다.",
        },
    )


def validate_weapon_restrictions(build):
    warnings = []
    missing_data = []
    violations = []
    penalty = 0
    weapon_related = []

    for affix in build.get("recommended_rare_affixes", []):
        slot = affix.get("slot")
        if slot in WEAPON_AFFIX_SLOTS:
            weapon_related.append({"source": "rare_affix", "slot": slot, "name": affix.get("name", "")})

    for unique in build.get("recommended_uniques", []):
        base_type = str(unique.get("base_type", ""))
        if any(hint in base_type.lower() for hint in WEAPON_BASE_HINTS):
            weapon_related.append({"source": "unique", "base_type": base_type, "name": unique.get("name", "")})

    if weapon_related:
        missing_data.append({
            "type": "weapon_requirement_rules_missing",
            "message": "무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.",
            "weapon_related_items": weapon_related,
        })
        warnings.append({
            "type": "weapon_dependent_build",
            "message": "무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.",
        })
        penalty += 10
    else:
        missing_data.append({
            "type": "weapon_requirement_rules_missing",
            "message": "정확한 무기 제한 데이터가 저장소에 없어 weapon restriction 검증을 스킵했습니다.",
        })
        penalty += 3

    return status_result(
        "skipped_missing_data" if not warnings else "warning",
        penalty,
        violations=violations,
        warnings=warnings,
        missing_data=missing_data,
        details={
            "weapon_related_items": weapon_related,
            "note": "실제 게임 무기 제한 데이터가 없으므로 불법 판정은 하지 않고 보수적 경고만 생성합니다.",
        },
    )


def validate_trigger_conditions(build, mechanics):
    mechanic_set = set(mechanics)
    warnings = []
    missing_data = []
    violations = []
    penalty = 0

    has_trigger = bool(mechanic_set & TRIGGER_MECHANICS)
    support_text = " ".join(build.get("recommended_supports", [])).lower()
    combo_names = [combo.get("name", "") for combo in build.get("broken_combos", [])]
    has_trigger_combo = any("trigger" in name.lower() for name in combo_names)
    has_trigger_support = any(keyword in support_text for keyword in TRIGGER_SUPPORT_KEYWORDS)

    if has_trigger or has_trigger_combo or has_trigger_support:
        missing_data.append({
            "type": "trigger_condition_rules_missing",
            "message": "발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.",
        })
        warnings.append({
            "type": "trigger_requires_manual_review",
            "message": "trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.",
            "trigger_mechanics": sorted(mechanic_set & TRIGGER_MECHANICS),
            "trigger_combos": [name for name in combo_names if "trigger" in name.lower()],
        })
        penalty += 12
    else:
        missing_data.append({
            "type": "trigger_condition_rules_missing",
            "message": "정확한 trigger condition 데이터가 없어 trigger 검증은 스킵되었습니다. 현재 빌드에서는 trigger 후보가 강하게 감지되지 않았습니다.",
        })
        penalty += 2

    return status_result(
        "warning" if warnings else "skipped_missing_data",
        penalty,
        violations=violations,
        warnings=warnings,
        missing_data=missing_data,
        details={
            "has_trigger_mechanic": has_trigger,
            "has_trigger_combo": has_trigger_combo,
            "has_trigger_support_keyword": has_trigger_support,
            "note": "trigger legality는 정확한 조건 데이터가 추가되기 전까지 warning/TODO로만 표시합니다.",
        },
    )


def validate_scaling_conflicts(build, mechanics, support_tags):
    mechanic_set = set(mechanics) | set(support_tags)
    warnings = []
    missing_data = []
    violations = []
    penalty = 0

    for rule in CONFLICTING_SCALING_GROUPS:
        if rule["requires"].issubset(mechanic_set) and mechanic_set & rule["conflicts_with_any"]:
            warnings.append({
                "type": rule["name"],
                "message": rule["message"],
                "requires": sorted(rule["requires"]),
                "conflicts_found": sorted(mechanic_set & rule["conflicts_with_any"]),
            })
            penalty += 8

    if "conversion" in mechanic_set and "gain_as_extra" in mechanic_set:
        warnings.append({
            "type": "conversion_gain_as_extra_requires_ordering_check",
            "message": "전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.",
        })
        penalty += 5

    if not warnings:
        missing_data.append({
            "type": "scaling_rule_data_missing",
            "message": "정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.",
        })

    status = "warning" if warnings else "passed_heuristic"

    return status_result(
        status,
        penalty,
        violations=violations,
        warnings=warnings,
        missing_data=missing_data,
        details={
            "observed_scaling_tags": sorted(mechanic_set),
            "note": "명확한 충돌은 불법 판정하지 않고 보수적 경고로 남깁니다.",
        },
    )


def flatten_status_items(statuses, key):
    items = []
    for name, status in statuses.items():
        for item in status.get(key, []):
            enriched = dict(item)
            enriched.setdefault("check", name)
            items.append(enriched)
    return items


def analyze_build(build, support_index, skill_index):
    mechanics = collect_mechanics(build)
    support_tags, _, _ = collect_support_tags(build, support_index)

    support_status = validate_support_compatibility(build, support_index, skill_index)
    weapon_status = validate_weapon_restrictions(build)
    trigger_status = validate_trigger_conditions(build, mechanics)
    scaling_status = validate_scaling_conflicts(build, mechanics, support_tags)

    statuses = {
        "support_compatibility_status": support_status,
        "weapon_restriction_status": weapon_status,
        "trigger_condition_status": trigger_status,
        "scaling_conflict_status": scaling_status,
    }

    violations = flatten_status_items(statuses, "violations")
    warnings = flatten_status_items(statuses, "warnings")
    missing_data = flatten_status_items(statuses, "missing_data")

    total_penalty = sum(status.get("score_penalty", 0) for status in statuses.values())
    if violations:
        total_penalty += 35

    legality_score = max(0, min(100, 100 - total_penalty))
    is_legal = not violations and legality_score >= 60

    if missing_data and not violations:
        decision_basis = "plausible_with_missing_data"
    elif violations:
        decision_basis = "violations_detected"
    else:
        decision_basis = "passed_available_heuristics"

    return {
        "build_name": build.get("build_name", ""),
        "main_skill": build.get("main_skill", ""),
        "archetype_label_ko": build.get("archetype_label_ko", ""),
        "is_legal": is_legal,
        "legality_score": legality_score,
        "decision_basis": decision_basis,
        "violations": violations,
        "warnings": warnings,
        "missing_data": missing_data,
        "support_compatibility_status": support_status,
        "weapon_restriction_status": weapon_status,
        "trigger_condition_status": trigger_status,
        "scaling_conflict_status": scaling_status,
        "mechanics": mechanics,
        "dps_summary": {
            "estimated_dps_score": build.get("dps_analysis", {}).get("estimated_dps_score"),
            "single_target_score": build.get("dps_analysis", {}).get("single_target_score"),
            "mapping_score": build.get("dps_analysis", {}).get("mapping_score"),
            "dps_data_available": bool(build.get("dps_analysis")),
        },
    }


def analyze_builds(builds, support_index, skill_index):
    results = [analyze_build(build, support_index, skill_index) for build in builds]
    results.sort(key=lambda item: (item["is_legal"], item["legality_score"]), reverse=True)
    return results


def fmt_items(items, limit=5):
    if not items:
        return "- 없음"

    lines = []
    for item in items[:limit]:
        message = item.get("message", item.get("type", str(item)))
        check = item.get("check")
        if check:
            lines.append(f"- [{check}] {message}")
        else:
            lines.append(f"- {message}")

    if len(items) > limit:
        lines.append(f"- ... 외 {len(items) - limit}개")

    return "\n".join(lines)


def generate_report(results, dps_available):
    legal_count = sum(1 for item in results if item["is_legal"])
    warning_count = sum(1 for item in results if item["warnings"])
    missing_count = sum(1 for item in results if item["missing_data"])
    violation_count = sum(1 for item in results if item["violations"])

    lines = [
        "# Legality Validation Report",
        "",
        "> 이 리포트는 실제 게임 규칙 전체 검증이 아니라 현재 저장소에 있는 데이터로 가능한 보수적 MVP 검증입니다.",
        "> 정확한 support compatibility, weapon restriction, trigger condition 데이터가 없는 경우 불법으로 단정하지 않고 TODO/skipped/warning으로 표시합니다.",
        "",
        "## 입력 / 출력",
        "",
        f"- 입력: `{INTERACTION_PATH.relative_to(ROOT)}`",
        f"- 선택 입력: `{DPS_PATH.relative_to(ROOT)}` ({'사용됨' if dps_available else '없음 / 스킵됨'})",
        f"- JSON 출력: `{OUT_PATH.relative_to(ROOT)}`",
        f"- 리포트 출력: `{REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## 요약",
        "",
        f"- 분석 빌드 수: {len(results)}",
        f"- plausible/legal 후보 수: {legal_count}",
        f"- warnings 포함 빌드 수: {warning_count}",
        f"- missing_data 포함 빌드 수: {missing_count}",
        f"- violations 포함 빌드 수: {violation_count}",
        "",
        "## Top Plausible Candidates",
        "",
    ]

    for index, result in enumerate(results[:25], start=1):
        dps = result["dps_summary"]
        dps_text = dps.get("estimated_dps_score") if dps.get("dps_data_available") else "N/A"
        lines.extend([
            f"### {index}. {result['build_name']}",
            "",
            f"- 메인 스킬: {result['main_skill']}",
            f"- is_legal: {result['is_legal']}",
            f"- legality_score: {result['legality_score']}",
            f"- decision_basis: {result['decision_basis']}",
            f"- estimated_dps_score: {dps_text}",
            f"- support_compatibility_status: {result['support_compatibility_status']['status']}",
            f"- weapon_restriction_status: {result['weapon_restriction_status']['status']}",
            f"- trigger_condition_status: {result['trigger_condition_status']['status']}",
            f"- scaling_conflict_status: {result['scaling_conflict_status']['status']}",
            "",
            "#### Warnings",
            "",
            fmt_items(result["warnings"]),
            "",
            "#### Missing Data / TODO",
            "",
            fmt_items(result["missing_data"]),
            "",
        ])

        if result["violations"]:
            lines.extend([
                "#### Violations",
                "",
                fmt_items(result["violations"]),
                "",
            ])

    return "\n".join(lines).rstrip() + "\n"


def main():
    interaction_builds = load_json(INTERACTION_PATH, required=True)
    dps_available = DPS_PATH.exists()
    dps_builds = load_json(DPS_PATH, default=[]) if dps_available else []
    supports = load_json(SUPPORTS_PATH, default=[])
    skills = load_json(SKILLS_PATH, default=[])

    support_index = build_index(supports)
    skill_index = build_index(skills)
    builds = merge_build_sources(interaction_builds, dps_builds)

    results = analyze_builds(builds, support_index, skill_index)
    save_json(OUT_PATH, results)
    save_text(REPORT_PATH, generate_report(results, dps_available))

    print(f"loaded interaction builds: {len(interaction_builds)}")
    print(f"loaded dps builds: {len(dps_builds)}")
    print(f"legality results: {len(results)}")
    print(f"plausible/legal candidates: {sum(1 for item in results if item['is_legal'])}")

    for result in results[:10]:
        print("=" * 80)
        print(f"빌드명: {result['build_name']}")
        print(f"합법성 점수: {result['legality_score']} / plausible: {result['is_legal']}")
        print(f"경고: {len(result['warnings'])} / 누락 데이터: {len(result['missing_data'])} / 위반: {len(result['violations'])}")


if __name__ == "__main__":
    main()
