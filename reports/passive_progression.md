# Passive Progression MVP

이 리포트는 최종 랭킹 상위 빌드의 패시브 진행 우선순위를 한국어로 요약합니다.
정확한 패시브 경로, class start, shortest path, travel-node 비용은 아직 계산하지 않으며 `heuristic_only`로 표시합니다.

## 입력/출력

- 입력: `data/meta/final_ranked_builds.json`
- 입력: `data/meta/leveling_plans.json`
- 입력: `data/passive/data.json`
- JSON 출력: `data/meta/passive_progression_plans.json` (gitignore 대상)
- 리포트 출력: `reports/passive_progression.md`

## 공통 주의사항

- 실제 패시브 경로를 발명하지 않습니다.
- notable/keystone 후보는 passive node 이름/스탯 키워드 매칭 기반입니다.
- 정확한 unlock timing, class start, ascendancy routing은 TODO입니다.

## Missing input / TODO

아래 입력 파일이 없어 빌드별 패시브 진행 후보를 생성하지 못했습니다.
필요한 상위 파이프라인 산출물을 생성한 뒤 다시 실행하세요.

- `data/meta/final_ranked_builds.json`
- `data/meta/leveling_plans.json`

## 요약: 0개 빌드 분석
