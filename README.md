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
