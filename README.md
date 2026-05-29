# poe2-meta-ai

PoE2 Autonomous Build Research Engine.

## DPS Approximation Engine MVP

현재 DPS 단계는 정확한 Path of Building DPS가 아니라, 기존 상호작용 분석 결과를 기반으로 한 **상대 DPS 추정치**를 생성합니다.

```bash
python scripts/estimate_dps.py
```

입력:

```text
data/meta/build_interaction_analysis.json
```

출력:

```text
data/meta/build_dps_estimates.json
reports/dps_analysis_report.md
```

포함 지표:

- `estimated_dps_score`
- `single_target_score`
- `mapping_score`
- `hit_model`
- `projectile_multiplier`
- `overlap_multiplier`
- `trigger_frequency_multiplier`
- `crit_multiplier`
- `conversion_multiplier`
- `gain_as_extra_multiplier`
- `explanation` / `why`

주의:

- 실제 게임 수치, 무기 DPS, 쿨다운 breakpoints, 보스 크기, 투사체 궤적은 아직 모델링하지 않습니다.
- 데이터가 없거나 아직 검증되지 않은 영역은 결과 JSON과 리포트에 `TODO` 또는 `skipped`로 표시합니다.

## Legality Validation Engine MVP

현재 legality 단계는 최종 랭킹 전에 빌드 후보가 **그럴듯하게 가능한지**를 보수적으로 검증합니다.
정확한 게임 규칙 데이터가 없는 영역은 불법으로 단정하지 않고 `missing_data`, `warnings`, `TODO/skipped`로 표시합니다.

```bash
python scripts/validate_build_legality.py
```

입력:

```text
data/meta/build_interaction_analysis.json
data/meta/build_dps_estimates.json  # 있으면 함께 사용
```

출력:

```text
data/meta/build_legality_analysis.json
reports/legality_report.md
```

포함 지표:

- `is_legal`
- `legality_score`
- `violations`
- `warnings`
- `missing_data`
- `support_compatibility_status`
- `weapon_restriction_status`
- `trigger_condition_status`
- `scaling_conflict_status`

## Survivability Engine MVP

현재 survivability 단계는 정확한 EHP 계산이 아니라, 기존 빌드 상호작용/DPS/legality 결과를 기반으로 한 **상대 생존력 추정치**를 생성합니다.
실제 생명력, ES, 방어도, 회피, 막기, 저항, 회복량 데이터가 없는 경우 가짜 수치를 만들지 않고 `missing_data`에 표시합니다.

```bash
python scripts/estimate_survivability.py
```

입력:

```text
data/meta/build_interaction_analysis.json
data/meta/build_dps_estimates.json
data/meta/build_legality_analysis.json  # 있으면 함께 사용
```

출력:

```text
data/meta/build_survivability_estimates.json
reports/survivability_report.md
```

포함 지표:

- `survivability_score`
- `ehp_score`
- `recovery_score`
- `mitigation_score`
- `avoidance_score`
- `sustain_score`
- `defensive_factors`
- `weaknesses`
- `missing_data`
- 한국어 `explanation`

## Final Build Ranking and Guide Generator

최종 랭킹 단계는 interaction, DPS, legality, survivability MVP 결과를 결합해 최종 빌드 후보와 한국어 가이드 초안을 생성합니다.
레벨링, 패시브 진행, 기어 진행은 아직 실제 플래너가 없으므로 TODO 섹션으로만 표시합니다.

```bash
python scripts/generate_final_ranked_builds.py
```

입력:

```text
data/meta/build_interaction_analysis.json
data/meta/build_dps_estimates.json
data/meta/build_legality_analysis.json
data/meta/build_survivability_estimates.json
```

출력:

```text
data/meta/final_ranked_builds.json
reports/final_build_guides.md
```

랭킹 공식:

```text
DPS 40% + interaction 20% + legality 20% + survivability 20%
```

점수가 누락된 경우 해당 항목은 제외하고 남은 가중치만 안전하게 정규화합니다.

## Leveling Planner MVP

레벨링 단계는 최종 랭킹 상위 빌드에 대해 1~endgame 구간별 가이드 초안을 생성합니다.
정확한 스킬 unlock level, quest reward, passive path, gear progression 데이터가 없는 경우 가짜 수치를 만들지 않고 `missing_data` / `TODO`로 표시합니다.

```bash
python scripts/generate_leveling_plans.py
```

입력:

```text
data/meta/final_ranked_builds.json
data/skills/skills.json
data/supports/supports.json
data/passive/data.json
```

출력:

```text
data/meta/leveling_plans.json
reports/leveling_guides.md
```

생성 레벨 구간:

- `LV1~12`
- `LV12~28`
- `LV28~45`
- `LV45~65`
- `LV65+`

포함 항목:

- 추천 leveling skill / transition skill
- stage별 support gems
- stage별 passive priority
- gear checkpoint
- final build online 시점
- missing data / TODO
