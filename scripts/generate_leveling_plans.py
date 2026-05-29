import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL_BUILDS_PATH = ROOT / "data" / "meta" / "final_ranked_builds.json"
SKILLS_PATH = ROOT / "data" / "skills" / "skills.json"
SUPPORTS_PATH = ROOT / "data" / "supports" / "supports.json"
PASSIVE_PATH = ROOT / "data" / "passive" / "data.json"
OUT_PATH = ROOT / "data" / "meta" / "leveling_plans.json"
REPORT_PATH = ROOT / "reports" / "leveling_guides.md"


LEVEL_BRACKETS = [
    ("LV1~12", "early_act"),
    ("LV12~28", "first_transition"),
    ("LV28~45", "mechanic_setup"),
    ("LV45~65", "pre_endgame"),
    ("LV65+", "endgame_online"),
]

SUPPORT_LIMIT_BY_STAGE = {
    "early_act": 2,
    "first_transition": 3,
    "mechanic_setup": 4,
    "pre_endgame": 5,
    "endgame_online": 6,
}

PASSIVE_PRIORITY_BY_MECHANIC = {
    "projectile": "투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선",
    "extra_projectile": "추가 투사체와 투사체 스케일링 노드 우선",
    "returning_projectile": "투사체 왕복/반환 시너지와 적중 수 증가 노드 우선",
    "chain": "연쇄/투사체 clear speed 관련 노드 우선",
    "overlap": "효과 범위와 범위 중첩 효율 노드 우선",
    "trigger": "발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선",
    "trigger_loop": "발동 루프 안정화 전까지 방어/자원 노드 우선",
    "crit": "치명타 확률과 치명타 피해 배율 노드 우선",
    "crit_scaling": "치명타 확률과 치명타 피해 배율 노드 우선",
    "gain_as_extra": "추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선",
    "conversion": "피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선",
    "fire": "화염 피해와 점화/원소 피해 노드 우선",
    "cold": "냉기 피해와 냉각/동결 안정성 노드 우선",
    "lightning": "번개 피해와 감전/원소 피해 노드 우선",
    "chaos": "카오스 피해와 지속 피해/중독 관련 노드 우선",
    "minion": "소환수 피해/생존/지속시간 노드 우선",
    "life": "생명력 기반 방어 노드 우선",
    "mana": "마나/자원 sustain 노드 우선",
}

STAGE_PRIORITY_FOCUS = {
    "early_act": ["life", "mana", "projectile", "fire", "cold", "lightning", "minion"],
    "first_transition": ["projectile", "overlap", "chain", "life", "mana", "crit"],
    "mechanic_setup": ["trigger", "crit_scaling", "gain_as_extra", "conversion", "overlap", "life"],
    "pre_endgame": ["returning_projectile", "extra_projectile", "chain", "trigger", "crit_scaling", "gain_as_extra", "conversion"],
    "endgame_online": ["trigger_loop", "returning_projectile", "extra_projectile", "chain", "overlap", "crit_scaling", "gain_as_extra", "conversion"],
}

TOP_BUILD_LIMIT = 25


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


def index_by_name(items):
    return {normalize_key(item.get("name")): item for item in items if item.get("name")}


def extract_passive_nodes(passive_data):
    nodes = passive_data.get("nodes", {}) if isinstance(passive_data, dict) else {}
    result = []
    for node in nodes.values():
        if not isinstance(node, dict):
            continue
        name = node.get("name") or ""
        stats = node.get("stats") or []
        if not name and not stats:
            continue
        result.append({
            "name": name,
            "stats": stats,
            "text": f"{name} {' '.join(stats)}".lower(),
        })
    return result


def find_passive_hints(core_mechanics, passive_nodes, limit=8):
    terms = [term for term in core_mechanics if term and len(term) > 3]
    hints = []
    seen = set()
    for node in passive_nodes:
        text = node["text"]
        if not any(term.replace("_", " ") in text or term in text for term in terms):
            continue
        name = node["name"] or "이름 없는 패시브"
        if name in seen:
            continue
        seen.add(name)
        hints.append({
            "name": name,
            "stats": node["stats"][:3],
            "inference": "core_mechanics 키워드와 passive stat 텍스트가 부분 매칭된 후보입니다. 실제 경로/거리/레벨은 TODO입니다.",
        })
        if len(hints) >= limit:
            break
    return hints


def skill_exists(skill_name, skill_index):
    return normalize_key(skill_name) in skill_index


def infer_leveling_skill(build, skill_index):
    main_skill = build.get("main_skill", "")
    if skill_exists(main_skill, skill_index):
        return {
            "name": main_skill,
            "basis": "final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.",
            "is_inferred": True,
        }
    return {
        "name": main_skill or "TODO: main skill missing",
        "basis": "main_skill의 정확한 unlock/사용 가능 레벨을 확인할 수 없어 이름만 유지합니다.",
        "is_inferred": True,
    }


def stage_skill(build, stage_key, skill_index):
    final_skill = infer_leveling_skill(build, skill_index)
    main_skill = final_skill["name"]
    if stage_key == "early_act":
        return {
            "recommended_leveling_skill": main_skill,
            "transition_skill": main_skill,
            "note": "정확한 스킬 unlock level 데이터가 없어 최종 메인 스킬을 조기 후보로 표시합니다. 사용 불가 시 같은 태그의 임시 스킬로 대체해야 합니다.",
            "inference": final_skill["basis"],
        }
    if stage_key == "first_transition":
        return {
            "recommended_leveling_skill": main_skill,
            "transition_skill": main_skill,
            "note": "LV12~28 구간은 보조젬 수를 늘리며 최종 스킬 구조로 전환하는 보수적 단계입니다.",
            "inference": "정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.",
        }
    if stage_key == "mechanic_setup":
        return {
            "recommended_leveling_skill": main_skill,
            "transition_skill": main_skill,
            "note": "핵심 메커닉(trigger/crit/conversion 등)을 하나씩 추가하는 구간으로 표시합니다.",
            "inference": "정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.",
        }
    if stage_key == "pre_endgame":
        return {
            "recommended_leveling_skill": main_skill,
            "transition_skill": main_skill,
            "note": "최종 보조젬/유니크/희귀 affix 후보를 점검하며 endgame 전환을 준비합니다.",
            "inference": "정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.",
        }
    return {
        "recommended_leveling_skill": main_skill,
        "transition_skill": "최종 빌드 online",
        "note": "LV65+부터 최종 랭킹 빌드 구성을 online 후보로 봅니다. 실제 online 레벨은 TODO입니다.",
        "inference": "최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.",
    }


def support_gems_by_stage(build, stage_key, support_index):
    supports = build.get("recommended_supports", [])[:SUPPORT_LIMIT_BY_STAGE[stage_key]]
    result = []
    missing = []
    for support_name in supports:
        support = support_index.get(normalize_key(support_name))
        if not support:
            missing.append(support_name)
            result.append({
                "name": support_name,
                "tags_en": [],
                "missing_data": "supports.json에서 태그를 찾지 못했습니다.",
            })
            continue
        result.append({
            "name": support_name,
            "tags_en": support.get("tags_en", []),
            "meta_tags": support.get("meta_tags", []),
            "inference": "최종 추천 보조젬을 stage별 socket/link 증가 가정으로 순차 배치했습니다. 정확한 unlock level은 TODO입니다.",
        })
    return result, missing


def passive_priority_by_stage(build, stage_key, passive_hints):
    mechanics = build.get("core_mechanics", [])
    focused = [m for m in STAGE_PRIORITY_FOCUS[stage_key] if m in mechanics]
    priorities = []
    for mechanic in focused:
        text = PASSIVE_PRIORITY_BY_MECHANIC.get(mechanic)
        if text:
            priorities.append({
                "mechanic": mechanic,
                "priority": text,
                "inference": "core_mechanics 기반 추론입니다. 실제 passive path/거리/레벨은 TODO입니다.",
            })
    if not priorities:
        priorities.append({
            "mechanic": "generic_defense_and_damage",
            "priority": "초반에는 생명력/자원 안정화 후 메인 피해 태그에 맞는 노드를 우선합니다.",
            "inference": "매칭되는 core mechanic 우선순위가 부족해 일반 원칙으로 표시합니다.",
        })
    return {
        "priorities": priorities[:5],
        "candidate_passive_nodes": passive_hints[:3],
        "missing_data": [
            "정확한 passive route, shortest path, node unlock/order 데이터가 없어 후보와 우선순위만 제공합니다.",
        ],
    }


def gear_checkpoint_by_stage(build, stage_key):
    uniques = build.get("recommended_uniques", [])
    affixes = build.get("recommended_rare_affixes", [])
    if stage_key == "early_act":
        return {
            "checkpoint": "희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.",
            "recommended_uniques": [],
            "recommended_rare_affixes": [],
            "missing_data": ["정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다."],
        }
    if stage_key == "first_transition":
        return {
            "checkpoint": "최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.",
            "recommended_uniques": uniques[:1],
            "recommended_rare_affixes": affixes[:1],
            "missing_data": ["유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다."],
        }
    if stage_key == "mechanic_setup":
        return {
            "checkpoint": "trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.",
            "recommended_uniques": uniques[:2],
            "recommended_rare_affixes": affixes[:1],
            "missing_data": ["정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다."],
        }
    if stage_key == "pre_endgame":
        return {
            "checkpoint": "최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.",
            "recommended_uniques": uniques[:4],
            "recommended_rare_affixes": affixes[:2],
            "missing_data": ["early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다."],
        }
    return {
        "checkpoint": "최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.",
        "recommended_uniques": uniques,
        "recommended_rare_affixes": affixes,
        "missing_data": ["BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다."],
    }


def final_online_note(stage_key):
    if stage_key == "endgame_online":
        return {
            "is_final_online_stage": True,
            "when_final_build_comes_online": "LV65+ 후보",
            "note": "정확한 스킬/보조젬/유니크 unlock level 데이터가 없어 LV65+를 보수적 final online 구간으로 표시합니다.",
        }
    return {
        "is_final_online_stage": False,
        "when_final_build_comes_online": "TODO: 최종 online 전 준비 단계",
        "note": "이 구간은 최종 빌드 전환 준비 단계입니다. 정확한 transition timing은 TODO입니다.",
    }


def make_stage(build, stage_label, stage_key, skill_index, support_index, passive_hints):
    supports, missing_supports = support_gems_by_stage(build, stage_key, support_index)
    stage = {
        "level_bracket": stage_label,
        "stage_key": stage_key,
        **stage_skill(build, stage_key, skill_index),
        "support_gems_by_stage": supports,
        "passive_priority_by_stage": passive_priority_by_stage(build, stage_key, passive_hints),
        "gear_checkpoint": gear_checkpoint_by_stage(build, stage_key),
        **final_online_note(stage_key),
        "missing_data": [
            "정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.",
            "정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.",
        ],
    }
    if missing_supports:
        stage["missing_data"].append(f"supports.json에서 찾지 못한 보조젬: {', '.join(missing_supports)}")
    return stage


def make_plan(build, rank_index, skill_index, support_index, passive_nodes):
    passive_hints = find_passive_hints(build.get("core_mechanics", []), passive_nodes)
    stages = [
        make_stage(build, label, key, skill_index, support_index, passive_hints)
        for label, key in LEVEL_BRACKETS
    ]
    return {
        "rank": build.get("rank", rank_index),
        "build_name": build.get("build_name", ""),
        "main_skill": build.get("main_skill", ""),
        "final_rank_score": build.get("final_rank_score"),
        "core_mechanics": build.get("core_mechanics", []),
        "leveling_plan": stages,
        "global_missing_data": [
            "정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.",
            "패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.",
            "gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.",
        ],
    }


def generate_plans(final_builds, skills, supports, passive_data):
    skill_index = index_by_name(skills)
    support_index = index_by_name(supports)
    passive_nodes = extract_passive_nodes(passive_data)
    top_builds = final_builds[:TOP_BUILD_LIMIT]
    return [
        make_plan(build, index, skill_index, support_index, passive_nodes)
        for index, build in enumerate(top_builds, start=1)
    ]


def fmt_list(items, limit=8):
    if not items:
        return "- 없음"
    lines = []
    for item in items[:limit]:
        if isinstance(item, dict):
            if "name" in item:
                lines.append(f"- {item['name']}")
            elif "priority" in item:
                lines.append(f"- {item['priority']} (`{item.get('mechanic')}`)")
            elif "message" in item:
                lines.append(f"- {item['message']}")
            else:
                lines.append(f"- {json.dumps(item, ensure_ascii=False)}")
        else:
            lines.append(f"- {item}")
    if len(items) > limit:
        lines.append(f"- ... 외 {len(items) - limit}개")
    return "\n".join(lines)


def generate_report(plans):
    lines = [
        "# Leveling Guides MVP",
        "",
        "> 이 문서는 final ranked build 상위 후보에 대한 1~endgame 레벨링 가이드 초안입니다.",
        "> 정확한 unlock level, quest reward, passive path, gear progression 데이터가 없으면 TODO/missing_data로 표시합니다.",
        "",
        "## 입력 / 출력",
        "",
        f"- 입력: `{FINAL_BUILDS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{SKILLS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{SUPPORTS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{PASSIVE_PATH.relative_to(ROOT)}`",
        f"- JSON 출력: `{OUT_PATH.relative_to(ROOT)}`",
        f"- 리포트 출력: `{REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## 공통 레벨 구간",
        "",
        "- LV1~12",
        "- LV12~28",
        "- LV28~45",
        "- LV45~65",
        "- LV65+",
        "",
        f"## 생성된 가이드 수: {len(plans)}",
        "",
    ]
    for plan in plans:
        lines.extend([
            f"## Rank {plan['rank']}. {plan['build_name']}",
            "",
            f"- 메인 스킬: {plan['main_skill']}",
            f"- final_rank_score: {plan['final_rank_score']}",
            "",
            "### Global Missing Data / TODO",
            "",
            fmt_list(plan["global_missing_data"]),
            "",
        ])
        for stage in plan["leveling_plan"]:
            support_names = [item.get("name", "") for item in stage["support_gems_by_stage"]]
            passive_priorities = stage["passive_priority_by_stage"]["priorities"]
            gear = stage["gear_checkpoint"]
            lines.extend([
                f"### {stage['level_bracket']}",
                "",
                f"- 추천 leveling skill: {stage['recommended_leveling_skill']}",
                f"- transition skill: {stage['transition_skill']}",
                f"- final build online: {stage['when_final_build_comes_online']}",
                f"- 추론 근거: {stage['inference']}",
                "",
                "#### Support gems by stage",
                "",
                fmt_list(support_names),
                "",
                "#### Passive priority by stage",
                "",
                fmt_list(passive_priorities),
                "",
                "#### Gear checkpoint",
                "",
                f"- {gear['checkpoint']}",
                "",
                "#### Missing Data / TODO",
                "",
                fmt_list(stage["missing_data"] + gear.get("missing_data", [])),
                "",
            ])
    return "\n".join(lines).rstrip() + "\n"


def main():
    final_builds = load_json(FINAL_BUILDS_PATH, required=True)
    skills = load_json(SKILLS_PATH, required=True)
    supports = load_json(SUPPORTS_PATH, required=True)
    passive_data = load_json(PASSIVE_PATH, required=True)
    plans = generate_plans(final_builds, skills, supports, passive_data)
    save_json(OUT_PATH, plans)
    save_text(REPORT_PATH, generate_report(plans))
    print(f"loaded final ranked builds: {len(final_builds)}")
    print(f"loaded skills: {len(skills)}")
    print(f"loaded supports: {len(supports)}")
    print(f"generated leveling plans: {len(plans)}")
    for plan in plans[:10]:
        print("=" * 80)
        print(f"#{plan['rank']} {plan['build_name']}")
        print(f"stages: {len(plan['leveling_plan'])}")
        print(f"final online: {plan['leveling_plan'][-1]['when_final_build_comes_online']}")


if __name__ == "__main__":
    main()
