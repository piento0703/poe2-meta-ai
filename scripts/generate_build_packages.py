#!/usr/bin/env python3
"""Generate heuristic playable build packages for ranked PoE2 builds.

The Build Package Engine MVP assembles a build guide shell around each final
ranked build: main skill, clear/boss setups, movement, aura/curse/utility,
defensive notes, gear priorities, and leveling/endgame transitions.

It intentionally does not invent exact game data.  If required upstream outputs
or exact unlock/class/ascendancy data are missing, the result is marked with
TODO/missing_data and conservative heuristic notes.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FINAL_BUILDS_PATH = ROOT / "data" / "meta" / "final_ranked_builds.json"
LEVELING_PLANS_PATH = ROOT / "data" / "meta" / "leveling_plans.json"
PASSIVE_PLANS_PATH = ROOT / "data" / "meta" / "passive_progression_plans.json"
SKILLS_PATH = ROOT / "data" / "skills" / "skills.json"
SUPPORTS_PATH = ROOT / "data" / "supports" / "supports.json"
OUTPUT_JSON_PATH = ROOT / "data" / "meta" / "build_packages.json"
OUTPUT_REPORT_PATH = ROOT / "reports" / "build_packages.md"

TOP_BUILD_LIMIT = 25
REPORT_BUILD_LIMIT = 10
SUPPORT_LINK_LIMIT = 6

LEVEL_STAGES = ["campaign_early", "campaign_mid", "campaign_late", "endgame"]

MECHANIC_SUPPORT_HINTS = {
    "projectile": ["projectile", "projectile_scaling", "pierce", "chain", "fork"],
    "chain": ["chain", "projectile", "projectile_scaling"],
    "returning_projectile": ["projectile", "projectile_scaling", "pierce"],
    "shotgun": ["projectile", "aoe", "projectile_scaling"],
    "overlap": ["aoe", "area", "duration_scaling"],
    "trigger": ["trigger", "trigger_synergy", "persistent"],
    "crit": ["crit", "critical", "critical_damage"],
    "crit_scaling": ["crit", "critical", "critical_damage"],
    "conversion": ["elemental", "fire", "cold", "lightning", "chaos"],
    "gain_as_extra": ["elemental", "chaos", "damage"],
    "fire": ["fire", "ignite"],
    "cold": ["cold", "freeze", "chill"],
    "lightning": ["lightning", "shock"],
    "chaos": ["chaos", "poison"],
    "minion": ["minion", "minion_scaling"],
    "melee": ["melee", "attack"],
    "attack": ["attack"],
    "spell": ["spell"],
    "duration": ["duration", "duration_scaling"],
}

CLASS_ARCHETYPE_HINTS = [
    ("projectile", "projectile/ranged class candidate", "투사체/원거리 스케일링을 우선하는 클래스 후보입니다."),
    ("minion", "minion/occult class candidate", "소환수 지속 운용을 지원하는 클래스 후보입니다."),
    ("spell", "spellcaster class candidate", "주문/원소 피해를 우선하는 클래스 후보입니다."),
    ("trigger", "trigger-engine class candidate", "발동 조건과 자원 유지가 중요한 클래스 후보입니다."),
    ("melee", "melee/weapon class candidate", "근접 무기와 생존 기반을 함께 보는 클래스 후보입니다."),
    ("crit", "critical-scaling class candidate", "치명타 확률/피해 보너스를 활용하는 클래스 후보입니다."),
]

ASCENDANCY_ARCHETYPE_HINTS = [
    ("projectile", "projectile scaling ascendancy profile"),
    ("trigger", "trigger frequency / automation ascendancy profile"),
    ("crit", "critical strike ascendancy profile"),
    ("minion", "minion command / minion durability ascendancy profile"),
    ("fire", "fire ailment / elemental ascendancy profile"),
    ("cold", "cold control / freeze ascendancy profile"),
    ("lightning", "shock / lightning scaling ascendancy profile"),
    ("chaos", "chaos damage / poison ascendancy profile"),
]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def tags_of(item: dict) -> set[str]:
    tags = set()
    for key in ["tags_en", "meta_tags", "archetypes", "core_mechanics", "main_scaling"]:
        for tag in item.get(key, []) or []:
            tags.add(str(tag).lower())
    return tags


def build_index(items: list[dict], key: str = "name") -> dict[str, dict]:
    return {str(item.get(key, "")): item for item in items if isinstance(item, dict) and item.get(key)}


def collect_build_mechanics(build: dict) -> set[str]:
    mechanics = set()
    for key in ["core_mechanics", "archetypes", "main_scaling"]:
        for item in build.get(key, []) or []:
            mechanics.add(str(item).lower())
    for support in build.get("recommended_supports", []) or []:
        if isinstance(support, dict):
            for tag in support.get("meta_tags", []) or support.get("tags_en", []) or []:
                mechanics.add(str(tag).lower())
    return mechanics


def find_skill_candidates(skills: list[dict], required_tags: set[str], mechanics: set[str], limit: int = 5) -> list[dict]:
    candidates = []
    for skill in skills:
        skill_tags = tags_of(skill)
        if required_tags and not required_tags.issubset(skill_tags):
            continue
        score = len(skill_tags & mechanics) * 3 + len(skill_tags & required_tags) * 2
        if score <= 0 and required_tags:
            score = len(skill_tags & required_tags)
        if score <= 0:
            continue
        candidates.append(
            {
                "name": skill.get("name"),
                "tags_en": sorted(skill_tags),
                "score": score,
                "selection_basis": "skills.json tag match; exact unlock level and build legality are not validated here",
            }
        )
    candidates.sort(key=lambda item: (item["score"], item["name"] or ""), reverse=True)
    return candidates[:limit]


def find_support_candidates(supports: list[dict], mechanics: set[str], mode: str, preferred_names: list[str] | None = None) -> list[dict]:
    preferred_names = preferred_names or []
    preferred = []
    support_index = build_index(supports)
    for name in preferred_names:
        if name in support_index:
            support = support_index[name]
            preferred.append(
                {
                    "name": name,
                    "tags_en": sorted(tags_of(support)),
                    "selection_basis": "final_ranked_builds.json recommended_supports에서 가져온 후보입니다.",
                }
            )

    hint_tags = set()
    for mechanic in mechanics:
        hint_tags.update(MECHANIC_SUPPORT_HINTS.get(mechanic, []))
    if mode == "clear":
        hint_tags.update(["aoe", "projectile", "chain", "fork", "duration"])
    elif mode == "boss":
        hint_tags.update(["crit", "critical", "damage", "trigger", "elemental"])
    elif mode == "defense":
        hint_tags.update(["persistent", "buff", "duration"])

    scored = []
    existing = {item["name"] for item in preferred}
    for support in supports:
        name = support.get("name")
        if not name or name in existing:
            continue
        support_tags = tags_of(support)
        score = len(support_tags & hint_tags) * 2 + len(support_tags & mechanics)
        if score <= 0:
            continue
        scored.append(
            {
                "name": name,
                "tags_en": sorted(support_tags),
                "selection_basis": f"{mode} setup tag heuristic; exact support compatibility is TODO",
                "score": score,
            }
        )
    scored.sort(key=lambda item: (item["score"], item["name"] or ""), reverse=True)
    merged = preferred + scored
    return merged[:SUPPORT_LINK_LIMIT]


def setup_block(skill_name: str | None, supports: list[dict], purpose_ko: str, uncertainty: str) -> dict:
    return {
        "skill": skill_name,
        "purpose_ko": purpose_ko,
        "supports": supports,
        "uncertainty": uncertainty,
        "missing_data": [
            "TODO: exact gem level/unlock level is unavailable.",
            "TODO: support compatibility must be validated by the legality engine before final use.",
        ],
    }


def pick_single_skill(skills: list[dict], tags: set[str], mechanics: set[str]) -> dict | None:
    candidates = find_skill_candidates(skills, tags, mechanics, limit=1)
    return candidates[0] if candidates else None


def aura_package(skills: list[dict], mechanics: set[str]) -> dict:
    candidates = find_skill_candidates(skills, {"persistent", "buff"}, mechanics, limit=4)
    return {
        "skills": candidates,
        "note_ko": "정확한 spirit reservation/aura 동시 사용 가능 여부는 TODO입니다. persistent/buff 태그 기반 후보만 표시합니다.",
        "missing_data": ["TODO: reservation cost and aura legality data are unavailable."],
    }


def curse_package(skills: list[dict], mechanics: set[str]) -> dict:
    candidates = find_skill_candidates(skills, {"curse"}, mechanics, limit=3)
    if not candidates:
        candidates = find_skill_candidates(skills, {"mark"}, mechanics, limit=3)
    return {
        "skills": candidates,
        "note_ko": "curse/mark 태그 기반 후보입니다. 실제 curse limit, 보스 저항, 적용 조건은 TODO입니다.",
        "missing_data": ["TODO: curse limit and exact boss applicability are unavailable."],
    }


def utility_skills(skills: list[dict], mechanics: set[str]) -> list[dict]:
    utility = []
    for tags in [{"travel"}, {"warcry"}, {"mark"}, {"persistent", "buff"}]:
        for candidate in find_skill_candidates(skills, tags, mechanics, limit=2):
            if candidate["name"] not in {item["name"] for item in utility}:
                utility.append(candidate)
    return utility[:6]


def trigger_utility_setup(skills: list[dict], supports: list[dict], mechanics: set[str]) -> dict:
    trigger_skill = pick_single_skill(skills, {"trigger"}, mechanics)
    return setup_block(
        trigger_skill.get("name") if trigger_skill else None,
        find_support_candidates(supports, mechanics | {"trigger"}, "trigger"),
        "발동형 유틸리티 후보입니다.",
        "trigger 조건, cooldown, 실제 socket/link 가능 여부는 아직 검증하지 않았습니다.",
    )


def defensive_skills(skills: list[dict], supports: list[dict], mechanics: set[str]) -> dict:
    candidates = []
    for tags in [{"buff", "persistent"}, {"warcry"}, {"travel"}]:
        candidates.extend(find_skill_candidates(skills, tags, mechanics | {"physical", "duration"}, limit=2))
    unique = []
    seen = set()
    for candidate in candidates:
        if candidate["name"] not in seen:
            seen.add(candidate["name"])
            unique.append(candidate)
    return {
        "skills": unique[:5],
        "supports": find_support_candidates(supports, mechanics | {"duration", "persistent"}, "defense")[:4],
        "note_ko": "방어 스킬은 buff/persistent/warcry/travel 태그 기반 후보입니다. guard skill 여부와 정확한 방어 수치는 TODO입니다.",
        "missing_data": ["TODO: exact mitigation/recovery values are unavailable."],
    }


def class_candidates(mechanics: set[str]) -> list[dict]:
    candidates = []
    for mechanic, label, reason in CLASS_ARCHETYPE_HINTS:
        if mechanic in mechanics:
            candidates.append(
                {
                    "candidate": label,
                    "reason_ko": reason,
                    "confidence": "low",
                    "uncertainty": "정확한 PoE2 class/ascendancy resolver 데이터가 없어 archetype profile로만 표시합니다.",
                }
            )
    if not candidates:
        candidates.append(
            {
                "candidate": "generic build class candidate",
                "reason_ko": "빌드 메커닉 정보가 부족해 일반 후보로 표시합니다.",
                "confidence": "low",
                "uncertainty": "TODO: class resolver required.",
            }
        )
    return candidates[:4]


def ascendancy_candidates(mechanics: set[str]) -> list[dict]:
    candidates = []
    for mechanic, label in ASCENDANCY_ARCHETYPE_HINTS:
        if mechanic in mechanics:
            candidates.append(
                {
                    "candidate_profile": label,
                    "matched_mechanic": mechanic,
                    "confidence": "low",
                    "uncertainty": "정확한 ascendancy 이름을 발명하지 않습니다. ascendancy resolver 구현 후 실제 후보명으로 교체해야 합니다.",
                }
            )
    return candidates[:4] or [
        {
            "candidate_profile": "TODO ascendancy resolver profile",
            "matched_mechanic": None,
            "confidence": "low",
            "uncertainty": "빌드 메커닉 또는 ascendancy 데이터가 부족합니다.",
        }
    ]


def stage_priorities(build: dict, mechanics: set[str]) -> tuple[dict, dict]:
    rare_affixes = build.get("recommended_rare_affixes", []) or []
    uniques = build.get("recommended_uniques", []) or []
    mechanic_text = ", ".join(sorted(list(mechanics))[:6]) or "core mechanic TODO"
    gear = {}
    weapon = {}
    for stage in LEVEL_STAGES:
        gear[stage] = {
            "priorities_ko": [
                "생명력/저항/방어 기반을 먼저 확보",
                f"핵심 메커닉({mechanic_text})과 맞는 피해 affix를 점진적으로 추가",
                "고유 아이템은 실제 획득 가능 시점/착용 레벨 확인 전까지 필수로 가정하지 않음",
            ],
            "recommended_uniques_reference": uniques[:3],
            "recommended_rare_affixes_reference": rare_affixes[:5],
            "missing_data": ["TODO: item level, required level, crafting route, drop source are unavailable."],
        }
        weapon[stage] = {
            "priorities_ko": weapon_priority_lines(mechanics),
            "missing_data": ["TODO: exact weapon base restrictions and DPS tiers are unavailable."],
        }
    return gear, weapon


def weapon_priority_lines(mechanics: set[str]) -> list[str]:
    lines = ["주력 스킬이 요구하는 무기 제한을 먼저 확인"]
    if "projectile" in mechanics:
        lines.append("투사체/공격 속도/추가 투사체 또는 관련 태그가 있는 무기 우선")
    if "spell" in mechanics or "trigger" in mechanics:
        lines.append("주문/발동 빌드라면 시전 속도, 원소 피해, 자원 유지 옵션 우선")
    if "crit" in mechanics or "crit_scaling" in mechanics:
        lines.append("치명타 확률/치명타 피해 보너스 스케일링 확인")
    if any(tag in mechanics for tag in ["fire", "cold", "lightning", "chaos"]):
        lines.append("빌드 원소/카오스 태그와 일치하는 피해 증가 옵션 우선")
    return lines


def single_target_vs_mapping(build: dict, mechanics: set[str]) -> dict:
    single = build.get("single_target_score")
    mapping = build.get("mapping_score")
    notes = []
    if "chain" in mechanics or "aoe" in mechanics or "projectile" in mechanics:
        notes.append("mapping: chain/projectile/aoe 계열이면 클리어 성능 후보가 높습니다.")
    if "shotgun" in mechanics or "returning_projectile" in mechanics or "crit" in mechanics:
        notes.append("single target: returning/shotgun/crit 계열이면 보스딜 후보가 높습니다.")
    if single is None or mapping is None:
        notes.append("DPS 세부 점수가 없으면 정량 비교는 TODO입니다.")
    return {
        "single_target_score": single,
        "mapping_score": mapping,
        "notes_ko": notes,
        "uncertainty": "상대 점수와 태그 기반 구분이며 exact PoB DPS가 아닙니다.",
    }


def leveling_transition_setup(build: dict, leveling_plan: dict | None) -> dict:
    if not leveling_plan:
        return {
            "status": "missing_leveling_plan",
            "stages": [],
            "note_ko": "leveling_plans.json 입력이 없어 전환 세팅을 생성하지 못했습니다.",
            "missing_data": ["TODO: run leveling planner first."],
        }
    stages = []
    for stage in leveling_plan.get("leveling_plan", []) or []:
        stages.append(
            {
                "level_bracket": stage.get("level_bracket"),
                "recommended_leveling_skill": stage.get("recommended_leveling_skill"),
                "transition_skill": stage.get("transition_skill"),
                "support_gems_by_stage": stage.get("support_gems_by_stage", []),
                "gear_checkpoint": stage.get("gear_checkpoint"),
                "missing_data": stage.get("missing_data", []),
            }
        )
    return {
        "status": "heuristic_from_leveling_plans",
        "stages": stages,
        "note_ko": "leveling_plans.json의 단계별 정보를 build package에 연결했습니다. 정확한 unlock level은 TODO입니다.",
    }


def passive_summary(passive_plan: dict | None) -> dict:
    if not passive_plan:
        return {
            "status": "missing_passive_progression_plan",
            "note_ko": "passive_progression_plans.json 입력이 없어 패시브 진행 요약을 연결하지 못했습니다.",
            "missing_data": ["TODO: run passive progression planner first."],
        }
    return {
        "status": passive_plan.get("routing_status", "heuristic_only"),
        "note_ko": passive_plan.get("routing_disclaimer_ko"),
        "stage_count": len(passive_plan.get("stages", []) or []),
        "global_missing_data": passive_plan.get("global_missing_data", []),
    }


def build_package(build: dict, skills: list[dict], supports: list[dict], leveling_by_name: dict[str, dict], passive_by_name: dict[str, dict]) -> dict:
    mechanics = collect_build_mechanics(build)
    main_skill = build.get("main_skill")
    preferred_supports = [s for s in build.get("recommended_supports", []) or [] if isinstance(s, str)]

    clear_supports = find_support_candidates(supports, mechanics, "clear", preferred_supports)
    boss_supports = find_support_candidates(supports, mechanics | {"crit", "damage"}, "boss", preferred_supports)
    movement = pick_single_skill(skills, {"travel"}, mechanics)
    gear_priorities, weapon_priorities = stage_priorities(build, mechanics)

    return {
        "rank": build.get("rank"),
        "build_name": build.get("build_name", ""),
        "main_skill": main_skill,
        "package_status": "heuristic_package",
        "uncertainty_ko": "정확한 스킬 unlock, socket/link, spirit reservation, class/ascendancy legality는 아직 검증하지 않았습니다.",
        "clear_setup": setup_block(main_skill, clear_supports, "맵핑/클리어용 링크 후보입니다.", "clear support는 태그 기반 휴리스틱입니다."),
        "boss_setup": setup_block(main_skill, boss_supports, "보스/단일 대상용 링크 후보입니다.", "boss support는 태그 기반 휴리스틱입니다."),
        "movement_skill": movement or {"name": None, "missing_data": ["TODO: travel-tagged movement skill candidate not found."]},
        "aura_package": aura_package(skills, mechanics),
        "curse_package": curse_package(skills, mechanics),
        "utility_skills": utility_skills(skills, mechanics),
        "trigger_utility_setup": trigger_utility_setup(skills, supports, mechanics),
        "defensive_skills": defensive_skills(skills, supports, mechanics),
        "recommended_support_links": {
            "clear": clear_supports,
            "boss": boss_supports,
            "note_ko": "final build의 recommended_supports와 supports.json 태그 매칭을 결합했습니다.",
        },
        "leveling_transition_setup": leveling_transition_setup(build, leveling_by_name.get(build.get("build_name", ""))),
        "endgame_setup": {
            "main_skill": main_skill,
            "core_mechanics": sorted(mechanics),
            "passive_progression_summary": passive_summary(passive_by_name.get(build.get("build_name", ""))),
            "note_ko": "final ranked build를 기준으로 한 엔드게임 세팅 초안입니다. 실제 gear/passive/class legality는 TODO입니다.",
        },
        "recommended_class_candidates": class_candidates(mechanics),
        "recommended_ascendancy_candidates": ascendancy_candidates(mechanics),
        "gear_priorities_by_stage": gear_priorities,
        "weapon_priorities_by_stage": weapon_priorities,
        "campaign_speed_notes": [
            "이동기는 travel 태그 후보를 우선 확인합니다.",
            "초반에는 최종 세팅 고유 아이템을 필수로 가정하지 않습니다.",
            "정확한 캠페인 보상/젬 unlock level 데이터는 TODO입니다.",
        ],
        "survivability_notes": [
            "생명력/저항/방어 affix를 우선 확보합니다.",
            "DPS가 높아도 legality/survivability 점수가 낮으면 glass cannon 위험이 있습니다.",
            "정확한 EHP/회피/방어도/막기 수치는 survivability engine의 실제 데이터 확장 후 갱신해야 합니다.",
        ],
        "single_target_vs_mapping": single_target_vs_mapping(build, mechanics),
        "missing_data": [
            "TODO: exact class and ascendancy resolver is not implemented.",
            "TODO: exact skill gem unlock levels and quest rewards are unavailable.",
            "TODO: exact support compatibility and weapon restrictions must be validated upstream.",
        ],
    }


def missing_inputs() -> list[Path]:
    return [path for path in [FINAL_BUILDS_PATH, LEVELING_PLANS_PATH, PASSIVE_PLANS_PATH, SKILLS_PATH, SUPPORTS_PATH] if not path.exists()]


def render_report(packages: list[dict], missing: list[Path]) -> str:
    lines = [
        "# Build Package Engine MVP",
        "",
        "이 리포트는 최종 랭킹 빌드를 실제 플레이 가능한 패키지 형태로 조립하기 위한 한국어 MVP 출력입니다.",
        "정확한 class/ascendancy, gem unlock, support legality, weapon restriction은 아직 발명하지 않고 TODO로 표시합니다.",
        "",
        "## 입력/출력",
        "",
        f"- 입력: `{FINAL_BUILDS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{LEVELING_PLANS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{PASSIVE_PLANS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{SKILLS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{SUPPORTS_PATH.relative_to(ROOT)}`",
        f"- JSON 출력: `{OUTPUT_JSON_PATH.relative_to(ROOT)}`",
        f"- 리포트 출력: `{OUTPUT_REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## 공통 주의사항",
        "",
        "- 모든 세팅은 태그 기반 휴리스틱 후보입니다.",
        "- exact route, exact gem level, exact ascendancy 이름은 데이터가 없으면 생성하지 않습니다.",
        "- support compatibility와 weapon restriction은 legality validator 결과와 함께 재검증해야 합니다.",
        "",
    ]
    if missing:
        lines.extend([
            "## Missing input / TODO",
            "",
            "아래 입력 파일이 없어 일부 또는 전체 build package를 생성하지 못했습니다.",
            "상위 파이프라인 산출물을 만든 뒤 다시 실행하세요.",
            "",
        ])
        lines.extend(f"- `{path.relative_to(ROOT)}`" for path in missing)
        lines.append("")

    lines.extend([f"## 요약: {len(packages)}개 build package 생성", ""])
    for package in packages[:REPORT_BUILD_LIMIT]:
        lines.extend(
            [
                f"## #{package.get('rank')} {package.get('build_name')}",
                "",
                f"- main skill: {package.get('main_skill')}",
                f"- package_status: `{package.get('package_status')}`",
                f"- mapping: {', '.join(package.get('single_target_vs_mapping', {}).get('notes_ko', [])[:1]) or 'TODO'}",
                f"- bossing: {', '.join(package.get('single_target_vs_mapping', {}).get('notes_ko', [])[1:2]) or 'TODO'}",
                "",
                "### 스킬 패키지",
                "",
                f"- clear setup: {package.get('clear_setup', {}).get('skill')} + {support_names(package.get('clear_setup', {}).get('supports', []))}",
                f"- boss setup: {package.get('boss_setup', {}).get('skill')} + {support_names(package.get('boss_setup', {}).get('supports', []))}",
                f"- movement: {skill_name(package.get('movement_skill'))}",
                f"- aura 후보: {support_names(package.get('aura_package', {}).get('skills', []))}",
                f"- curse/mark 후보: {support_names(package.get('curse_package', {}).get('skills', []))}",
                "",
                "### 클래스/전직 후보",
                "",
            ]
        )
        for candidate in package.get("recommended_class_candidates", [])[:3]:
            lines.append(f"- {candidate.get('candidate')} — {candidate.get('reason_ko')} ({candidate.get('confidence')})")
        for candidate in package.get("recommended_ascendancy_candidates", [])[:3]:
            lines.append(f"- {candidate.get('candidate_profile')} — {candidate.get('uncertainty')}")
        lines.extend(
            [
                "",
                "### TODO / missing data",
                "",
            ]
        )
        for item in package.get("missing_data", [])[:4]:
            lines.append(f"- {item}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def support_names(items: list[dict]) -> str:
    names = [str(item.get("name")) for item in items if isinstance(item, dict) and item.get("name")]
    return ", ".join(names[:6]) if names else "TODO"


def skill_name(item: dict | None) -> str:
    if not isinstance(item, dict):
        return "TODO"
    return str(item.get("name") or item.get("skill") or "TODO")


def main() -> None:
    final_builds = load_json(FINAL_BUILDS_PATH, [])
    leveling_plans = load_json(LEVELING_PLANS_PATH, [])
    passive_plans = load_json(PASSIVE_PLANS_PATH, [])
    skills = load_json(SKILLS_PATH, [])
    supports = load_json(SUPPORTS_PATH, [])

    leveling_by_name = {item.get("build_name", ""): item for item in leveling_plans if isinstance(item, dict)}
    passive_by_name = {item.get("build_name", ""): item for item in passive_plans if isinstance(item, dict)}

    selected_builds = [item for item in final_builds if isinstance(item, dict)][:TOP_BUILD_LIMIT]
    packages = [build_package(build, skills, supports, leveling_by_name, passive_by_name) for build in selected_builds]

    save_json(OUTPUT_JSON_PATH, packages)
    write_text(OUTPUT_REPORT_PATH, render_report(packages, missing_inputs()))

    print(f"저장 완료: {OUTPUT_JSON_PATH}")
    print(f"저장 완료: {OUTPUT_REPORT_PATH}")
    print(f"build packages: {len(packages)}")
    if missing_inputs():
        print("missing inputs:")
        for path in missing_inputs():
            print(f"- {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
