# poe2-meta-ai

## Passive Path Planner MVP

패시브 진행 단계는 최종 랭킹 상위 빌드와 레벨링 플랜을 기반으로 구간별 패시브 우선순위 가이드를 생성합니다. 정확한 passive graph 최단 경로, class start, ascendancy pathing은 아직 신뢰할 수 없으므로 `heuristic_only`로 표시하고 TODO/missing data에 남깁니다.

```bash
python scripts/generate_passive_progression.py
```

입력:

```text
data/meta/final_ranked_builds.json
data/meta/leveling_plans.json
data/passive/data.json
```

출력:

```text
data/meta/passive_progression_plans.json  # gitignore 대상 generated output
reports/passive_progression.md
```

포함 항목:

- LV1~12 / LV12~28 / LV28~45 / LV45~65 / LV65+ 단계별 공격·방어·유틸 우선순위
- passive node 이름/스탯 키워드 기반 notable/keystone 후보
- transition timing
- exact route/pathing이 없는 영역의 missing data / TODO

## Build Package Engine MVP

Build Package 단계는 최종 랭킹 빌드를 실제 플레이 가능한 패키지 형태로 조립하는 MVP입니다. 정확한 class/ascendancy, gem unlock level, support legality, weapon restriction 데이터가 없으면 가짜 확정값을 만들지 않고 TODO/missing data로 표시합니다.

```bash
python scripts/generate_build_packages.py
```

입력:

```text
data/meta/final_ranked_builds.json
data/meta/leveling_plans.json
data/meta/passive_progression_plans.json
data/skills/skills.json
data/supports/supports.json
```

출력:

```text
data/meta/build_packages.json
reports/build_packages.md
```

포함 항목:

- main / clear / boss / movement / aura / curse / utility / trigger / defensive setup
- recommended support links
- leveling transition setup / endgame setup
- recommended class 및 ascendancy 후보 profile
- stage별 gear / weapon priorities
- campaign speed, survivability, single target vs mapping notes
