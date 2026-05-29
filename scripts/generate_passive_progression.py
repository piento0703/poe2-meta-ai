#!/usr/bin/env python3
"""Generate heuristic passive progression guidance for top ranked builds.

This MVP intentionally does not calculate exact passive tree routes.  The PoE2
passive graph data in this repository is useful for candidate lookup, but the
project does not yet have reliable class start selection, ascendancy resolution,
or shortest-path routing.  Exact pathing is therefore marked as TODO/missing data
in both JSON and Markdown outputs.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINAL_BUILDS_PATH = ROOT / "data" / "meta" / "final_ranked_builds.json"
LEVELING_PLANS_PATH = ROOT / "data" / "meta" / "leveling_plans.json"
PASSIVE_DATA_PATH = ROOT / "data" / "passive" / "data.json"
OUTPUT_JSON_PATH = ROOT / "data" / "meta" / "passive_progression_plans.json"
OUTPUT_REPORT_PATH = ROOT / "reports" / "passive_progression.md"

LEVEL_BRACKETS = ["LV1~12", "LV12~28", "LV28~45", "LV45~65", "LV65+"]
TOP_BUILD_LIMIT = 25
REPORT_BUILD_LIMIT = 5
CANDIDATE_LIMIT = 5

MECHANIC_PRIORITY_RULES = {
    "projectile": {
        "label_ko": "투사체 피해/속도/관통/추가 투사체 관련 노드",
        "keywords": ["projectile", "projectiles", "pierce", "fork", "chain"],
    },
    "chain": {
        "label_ko": "연쇄/투사체 확산 관련 노드",
        "keywords": ["chain", "projectile", "projectiles"],
    },
    "returning_projectile": {
        "label_ko": "투사체 반복 히트와 시너지가 있는 투사체 노드",
        "keywords": ["projectile", "projectiles", "pierce", "speed"],
    },
    "shotgun": {
        "label_ko": "중첩 히트/범위/투사체 수 증가와 관련된 노드",
        "keywords": ["projectile", "projectiles", "area", "aoe"],
    },
    "overlap": {
        "label_ko": "범위 중첩/효과 범위 관련 노드",
        "keywords": ["area", "aoe", "radius", "projectile"],
    },
    "trigger": {
        "label_ko": "발동 조건 안정화와 재사용 대기시간/자원 관련 노드",
        "keywords": ["trigger", "cooldown", "cast speed", "attack speed", "mana", "spirit"],
    },
    "crit": {
        "label_ko": "치명타 확률/치명타 피해 보너스 노드",
        "keywords": ["critical", "crit"],
    },
    "crit_scaling": {
        "label_ko": "치명타 스케일링 노드",
        "keywords": ["critical", "crit", "critical damage bonus"],
    },
    "conversion": {
        "label_ko": "피해 전환/원소 피해 스케일링 노드",
        "keywords": ["convert", "conversion", "elemental", "fire", "cold", "lightning"],
    },
    "gain_as_extra": {
        "label_ko": "추가 피해 획득과 함께 스케일되는 원소/카오스 피해 노드",
        "keywords": ["extra", "elemental", "chaos", "damage"],
    },
    "fire": {"label_ko": "화염 피해/점화 관련 노드", "keywords": ["fire", "ignite"]},
    "cold": {"label_ko": "냉기 피해/동결 관련 노드", "keywords": ["cold", "freeze", "chill"]},
    "lightning": {"label_ko": "번개 피해/감전 관련 노드", "keywords": ["lightning", "shock"]},
    "chaos": {"label_ko": "카오스 피해 관련 노드", "keywords": ["chaos", "poison"]},
    "minion": {"label_ko": "소환수 피해/생존 관련 노드", "keywords": ["minion", "minions"]},
    "ailment_scaling": {
        "label_ko": "상태 이상 피해/확률 관련 노드",
        "keywords": ["ailment", "ignite", "shock", "poison", "bleed", "freeze"],
    },
}

DEFENSIVE_RULES = {
    "life": ["life", "maximum life"],
    "es": ["energy shield", "maximum energy shield", "es"],
    "mitigation": ["armour", "physical damage reduction", "resistance", "resistances"],
    "avoidance": ["evasion", "avoid", "dodge", "block"],
    "recovery": ["regenerate", "recovery", "recoup", "leech"],
}

UTILITY_RULES = {
    "mana": ["mana", "cost"],
    "spirit": ["spirit"],
    "charge": ["charge", "charges"],
    "speed": ["movement speed", "attack speed", "cast speed"],
    "attribute": ["strength", "dexterity", "intelligence", "attribute"],
}

STAGE_FOCUS = {
    "LV1~12": {
        "offensive": ["main_damage", "early_accuracy"],
        "defensive": ["life", "mitigation"],
        "utility": ["attribute", "mana"],
        "transition": "초반에는 최종 빌드의 핵심 피해 태그와 생명력/저항 계열을 우선합니다.",
    },
    "LV12~28": {
        "offensive": ["main_damage", "projectile_or_element"],
        "defensive": ["life", "avoidance"],
        "utility": ["mana", "speed"],
        "transition": "주력 스킬/보조젬이 갖춰지는 구간으로, 공격 태그와 방어 기반을 함께 확장합니다.",
    },
    "LV28~45": {
        "offensive": ["core_mechanic", "crit_or_conversion"],
        "defensive": ["life", "mitigation", "recovery"],
        "utility": ["charge", "spirit", "mana"],
        "transition": "핵심 메커닉 전환 후보 구간입니다. 정확한 전환 레벨은 unlock 데이터 부재로 TODO입니다.",
    },
    "LV45~65": {
        "offensive": ["core_mechanic", "scaling_stack"],
        "defensive": ["life", "es", "mitigation", "avoidance"],
        "utility": ["charge", "speed"],
        "transition": "엔드게임 전 준비 구간입니다. 핵심 딜 스케일링과 방어층을 균형 있게 확보합니다.",
    },
    "LV65+": {
        "offensive": ["final_scaling", "broken_interaction_support"],
        "defensive": ["life", "es", "mitigation", "avoidance", "recovery"],
        "utility": ["charge", "spirit", "speed"],
        "transition": "최종 빌드 온라인 후보 구간입니다. 정확한 패시브 경로/keystone timing은 TODO입니다.",
    },
}


def load_json(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def missing_input_paths() -> list[Path]:
    return [path for path in [FINAL_BUILDS_PATH, LEVELING_PLANS_PATH, PASSIVE_DATA_PATH] if not path.exists()]


def text_blob(node: dict) -> str:
    parts = [str(node.get("name", ""))]
    parts.extend(str(stat) for stat in node.get("stats", []) if stat)
    return " ".join(parts).lower()


def classify_node_type(node: dict) -> str:
    if node.get("isKeystone"):
        return "keystone"
    if node.get("isNotable"):
        return "notable"
    if node.get("name") and node.get("stats"):
        return "named_passive"
    return "passive"


def extract_passive_candidates(passive_data: dict) -> list[dict]:
    candidates = []
    nodes = passive_data.get("nodes", {}) if isinstance(passive_data, dict) else {}
    for node_id, node in nodes.items():
        if not isinstance(node, dict):
            continue
        name = str(node.get("name", "")).strip()
        stats = [str(stat) for stat in node.get("stats", []) if stat]
        if not name and not stats:
            continue
        if name.lower() in {"passive point", ""} and not stats:
            continue
        candidates.append(
            {
                "id": str(node_id),
                "name": name or f"passive_{node_id}",
                "type": classify_node_type(node),
                "stats": stats[:4],
                "search_text": text_blob(node),
            }
        )
    return candidates


def score_candidates(candidates: list[dict], keyword_groups: list[list[str]], limit: int = CANDIDATE_LIMIT) -> list[dict]:
    scored = []
    for candidate in candidates:
        text = candidate["search_text"]
        score = 0
        matched = []
        for keywords in keyword_groups:
            for keyword in keywords:
                if keyword.lower() in text:
                    score += 3 if candidate["type"] in {"notable", "keystone"} else 1
                    matched.append(keyword)
        if score:
            scored.append(
                {
                    "id": candidate["id"],
                    "name": candidate["name"],
                    "type": candidate["type"],
                    "matched_keywords": sorted(set(matched)),
                    "stats": candidate["stats"],
                    "selection_basis": "passive node name/stats keyword heuristic; exact pathing not calculated",
                    "score": score,
                }
            )
    scored.sort(key=lambda item: (item["type"] == "keystone", item["type"] == "notable", item["score"]), reverse=True)
    return scored[:limit]


def build_offensive_priorities(build: dict, passive_candidates: list[dict]) -> tuple[list[dict], list[dict]]:
    mechanics = build.get("core_mechanics", []) or []
    priorities = []
    keyword_groups = []
    seen = set()
    for mechanic in mechanics:
        rule = MECHANIC_PRIORITY_RULES.get(mechanic)
        if not rule or mechanic in seen:
            continue
        seen.add(mechanic)
        priorities.append(
            {
                "mechanic": mechanic,
                "priority_ko": rule["label_ko"],
                "inference": "final_ranked_builds.json의 core_mechanics를 기반으로 한 보수적 추론입니다.",
            }
        )
        keyword_groups.append(rule["keywords"])
        if len(priorities) >= 6:
            break

    if not priorities:
        priorities.append(
            {
                "mechanic": "main_skill_scaling",
                "priority_ko": "주력 스킬 피해 태그와 일치하는 일반 피해 노드",
                "inference": "core_mechanics가 부족해 main_skill 기반 일반 스케일링으로 표시합니다.",
            }
        )
        keyword_groups.append(["damage", str(build.get("main_skill", "")).lower()])

    return priorities, score_candidates(passive_candidates, keyword_groups)


def build_category_priorities(rules: dict[str, list[str]], passive_candidates: list[dict], category: str) -> tuple[list[dict], list[dict]]:
    priorities = [
        {
            "category": key,
            "priority_ko": label,
            "inference": "정확한 패시브 경로가 아니라 node stats/name 키워드 기반 휴리스틱입니다.",
        }
        for key, label in category.items()
    ]
    keyword_groups = [rules[key] for key in category if key in rules]
    return priorities, score_candidates(passive_candidates, keyword_groups)


def stage_category_map(stage: str, key: str) -> dict[str, str]:
    requested = STAGE_FOCUS[stage][key]
    labels = {
        "life": "생명력/최대 생명력 확보",
        "es": "에너지 보호막 기반 보강",
        "mitigation": "방어도/저항/피해 감소 기반 보강",
        "avoidance": "회피/막기/avoidance 기반 보강",
        "recovery": "재생/회복/흡수 기반 sustain 보강",
        "mana": "마나 비용/마나 유지 안정화",
        "spirit": "spirit reservation/유틸리티 여유 확보",
        "charge": "charge 생성/유지 관련 유틸리티",
        "speed": "이동/공격/시전 속도 유틸리티",
        "attribute": "장비/젬 요구치를 위한 속성 확보",
    }
    return {item: labels[item] for item in requested if item in labels}


def find_leveling_plan(build_name: str, leveling_by_name: dict[str, dict]) -> dict:
    return leveling_by_name.get(build_name, {})


def summarize_stage_leveling(leveling_plan: dict, bracket: str) -> dict:
    for stage in leveling_plan.get("leveling_plan", []):
        if stage.get("level_bracket") == bracket:
            return {
                "leveling_skill_reference": stage.get("recommended_leveling_skill"),
                "transition_skill_reference": stage.get("transition_skill"),
                "leveling_note": stage.get("note"),
            }
    return {
        "leveling_skill_reference": None,
        "transition_skill_reference": None,
        "leveling_note": "leveling_plans.json에서 해당 구간을 찾지 못했습니다.",
    }


def build_stage_plan(build: dict, leveling_plan: dict, bracket: str, passive_candidates: list[dict]) -> dict:
    offensive_priorities, offensive_candidates = build_offensive_priorities(build, passive_candidates)
    defensive_priorities, defensive_candidates = build_category_priorities(
        DEFENSIVE_RULES, passive_candidates, stage_category_map(bracket, "defensive")
    )
    utility_priorities, utility_candidates = build_category_priorities(
        UTILITY_RULES, passive_candidates, stage_category_map(bracket, "utility")
    )

    notable_candidates = [item for item in offensive_candidates + defensive_candidates + utility_candidates if item["type"] in {"notable", "keystone"}]
    notable_candidates = notable_candidates[:CANDIDATE_LIMIT]

    return {
        "level_bracket": bracket,
        "routing_status": "heuristic_only",
        "routing_note_ko": "정확한 graph shortest path/class start/ascendancy pathing은 아직 계산하지 않습니다.",
        "leveling_reference": summarize_stage_leveling(leveling_plan, bracket),
        "offensive_priorities": offensive_priorities,
        "defensive_priorities": defensive_priorities,
        "utility_priorities": utility_priorities,
        "notable_keystone_candidates": notable_candidates,
        "candidate_passives": {
            "offensive": offensive_candidates[:3],
            "defensive": defensive_candidates[:3],
            "utility": utility_candidates[:3],
        },
        "transition_timing": STAGE_FOCUS[bracket]["transition"],
        "missing_data": [
            "TODO: exact passive graph routing by class start is not implemented.",
            "TODO: notable ordering is heuristic; shortest path and travel-node cost are unavailable.",
            "TODO: keystone timing requires reliable ascendancy/build legality routing data.",
        ],
    }


def build_progression_plan(build: dict, leveling_by_name: dict[str, dict], passive_candidates: list[dict]) -> dict:
    leveling_plan = find_leveling_plan(build.get("build_name", ""), leveling_by_name)
    return {
        "rank": build.get("rank"),
        "build_name": build.get("build_name", ""),
        "main_skill": build.get("main_skill", ""),
        "final_rank_score": build.get("final_rank_score"),
        "core_mechanics": build.get("core_mechanics", []),
        "routing_status": "heuristic_only",
        "routing_disclaimer_ko": "이 MVP는 정확한 패시브 경로를 발명하지 않습니다. passive node 이름/스탯과 빌드 메커닉을 매칭한 우선순위 가이드입니다.",
        "stages": [build_stage_plan(build, leveling_plan, bracket, passive_candidates) for bracket in LEVEL_BRACKETS],
        "global_missing_data": [
            "TODO: class start node selection is not resolved.",
            "TODO: exact passive graph pathing/shortest path is not reliable yet.",
            "TODO: ascendancy-specific passive timing is not implemented.",
        ],
    }



def compact_stat(value: str, max_length: int = 140) -> str:
    compact = " ".join(str(value).split())
    if len(compact) > max_length:
        return compact[: max_length - 1].rstrip() + "…"
    return compact

def render_candidate_lines(candidates: list[dict]) -> list[str]:
    if not candidates:
        return ["  - 후보 없음: 현재 passive 데이터에서 키워드 매칭 후보를 찾지 못했습니다."]
    lines = []
    for candidate in candidates[:3]:
        stats = compact_stat("; ".join(candidate.get("stats", [])[:1]) or "stats 없음")
        lines.append(
            f"  - `{candidate['name']}` ({candidate['type']}, id: {candidate['id']}) — {stats}"
        )
    return lines


def render_report(results: list[dict]) -> str:
    missing_inputs = missing_input_paths()
    lines = [
        "# Passive Progression MVP",
        "",
        "이 리포트는 최종 랭킹 상위 빌드의 패시브 진행 우선순위를 한국어로 요약합니다.",
        "정확한 패시브 경로, class start, shortest path, travel-node 비용은 아직 계산하지 않으며 `heuristic_only`로 표시합니다.",
        "",
        "## 입력/출력",
        "",
        f"- 입력: `{FINAL_BUILDS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{LEVELING_PLANS_PATH.relative_to(ROOT)}`",
        f"- 입력: `{PASSIVE_DATA_PATH.relative_to(ROOT)}`",
        f"- JSON 출력: `{OUTPUT_JSON_PATH.relative_to(ROOT)}` (gitignore 대상)",
        f"- 리포트 출력: `{OUTPUT_REPORT_PATH.relative_to(ROOT)}`",
        "",
        "## 공통 주의사항",
        "",
        "- 실제 패시브 경로를 발명하지 않습니다.",
        "- notable/keystone 후보는 passive node 이름/스탯 키워드 매칭 기반입니다.",
        "- 정확한 unlock timing, class start, ascendancy routing은 TODO입니다.",
        "",
    ]

    if missing_inputs:
        lines.extend(
            [
                "## Missing input / TODO",
                "",
                "아래 입력 파일이 없어 빌드별 패시브 진행 후보를 생성하지 못했습니다.",
                "필요한 상위 파이프라인 산출물을 생성한 뒤 다시 실행하세요.",
                "",
            ]
        )
        lines.extend(f"- `{path.relative_to(ROOT)}`" for path in missing_inputs)
        lines.append("")

    lines.extend([f"## 요약: {len(results)}개 빌드 분석", ""])

    for result in results[:REPORT_BUILD_LIMIT]:
        lines.extend(
            [
                f"## #{result.get('rank')} {result.get('build_name')}",
                "",
                f"- 주력 스킬: {result.get('main_skill')}",
                f"- final_rank_score: {result.get('final_rank_score')}",
                f"- routing_status: `{result.get('routing_status')}`",
                f"- 설명: {result.get('routing_disclaimer_ko')}",
                "",
            ]
        )
        for stage in result.get("stages", []):
            offensive = ", ".join(item["priority_ko"] for item in stage.get("offensive_priorities", [])[:3])
            defensive = ", ".join(item["priority_ko"] for item in stage.get("defensive_priorities", [])[:3])
            utility = ", ".join(item["priority_ko"] for item in stage.get("utility_priorities", [])[:3])
            lines.extend(
                [
                    f"### {stage.get('level_bracket')}",
                    "",
                    f"- 전환 타이밍: {stage.get('transition_timing')}",
                    f"- 공격 우선순위: {offensive or 'TODO'}",
                    f"- 방어 우선순위: {defensive or 'TODO'}",
                    f"- 유틸 우선순위: {utility or 'TODO'}",
                    "- notable/keystone 후보:",
                ]
            )
            lines.extend(render_candidate_lines(stage.get("notable_keystone_candidates", [])))
            lines.extend(
                [
                    "- TODO/missing data:",
                    "  - exact passive route/class start/shortest path 미구현",
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    final_builds = load_json(FINAL_BUILDS_PATH, [])
    leveling_plans = load_json(LEVELING_PLANS_PATH, [])
    passive_data = load_json(PASSIVE_DATA_PATH, {})

    leveling_by_name = {item.get("build_name", ""): item for item in leveling_plans if isinstance(item, dict)}
    passive_candidates = extract_passive_candidates(passive_data)

    selected_builds = [item for item in final_builds if isinstance(item, dict)][:TOP_BUILD_LIMIT]
    results = [build_progression_plan(build, leveling_by_name, passive_candidates) for build in selected_builds]

    save_json(OUTPUT_JSON_PATH, results)
    write_text(OUTPUT_REPORT_PATH, render_report(results))

    print(f"저장 완료: {OUTPUT_JSON_PATH}")
    print(f"저장 완료: {OUTPUT_REPORT_PATH}")
    print(f"분석 빌드 수: {len(results)}")
    print(f"패시브 후보 수: {len(passive_candidates)}")
    print("routing_status: heuristic_only")


if __name__ == "__main__":
    main()
