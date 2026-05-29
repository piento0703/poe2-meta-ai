# Build Package Engine MVP

이 리포트는 최종 랭킹 빌드를 실제 플레이 가능한 패키지 형태로 조립하기 위한 한국어 MVP 출력입니다.
정확한 class/ascendancy, gem unlock, support legality, weapon restriction은 아직 발명하지 않고 TODO로 표시합니다.

## 입력/출력

- 입력: `data/meta/final_ranked_builds.json`
- 입력: `data/meta/leveling_plans.json`
- 입력: `data/meta/passive_progression_plans.json`
- 입력: `data/skills/skills.json`
- 입력: `data/supports/supports.json`
- JSON 출력: `data/meta/build_packages.json`
- 리포트 출력: `reports/build_packages.md`

## 공통 주의사항

- 모든 세팅은 태그 기반 휴리스틱 후보입니다.
- exact route, exact gem level, exact ascendancy 이름은 데이터가 없으면 생성하지 않습니다.
- support compatibility와 weapon restriction은 legality validator 결과와 함께 재검증해야 합니다.

## Missing input / TODO

아래 입력 파일이 없어 일부 또는 전체 build package를 생성하지 못했습니다.
상위 파이프라인 산출물을 만든 뒤 다시 실행하세요.

- `data/meta/final_ranked_builds.json`
- `data/meta/leveling_plans.json`
- `data/meta/passive_progression_plans.json`

## 요약: 0개 build package 생성
