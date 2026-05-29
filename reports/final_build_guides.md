# Final Build Guides

> 이 문서는 interaction, DPS, legality, survivability MVP 산출물을 결합한 최종 랭킹 초안입니다.
> leveling/passive/gear progression은 실제 데이터가 아직 없으므로 TODO 섹션으로 명확히 표시합니다.

## 입력 / 출력

- 입력: `data/meta/build_interaction_analysis.json`
- 입력: `data/meta/build_dps_estimates.json`
- 입력: `data/meta/build_legality_analysis.json`
- 입력: `data/meta/build_survivability_estimates.json`
- JSON 출력: `data/meta/final_ranked_builds.json`
- 리포트 출력: `reports/final_build_guides.md`

## Ranking Formula

- DPS: 40%
- Interaction: 20%
- Legality: 20%
- Survivability: 20%
- 누락된 점수는 제외하고 남은 가중치만 안전하게 정규화합니다.

## Summary

- ranked builds: 100
- top build: 불씨 일제 사격 투사체 발동 번개 연쇄 빌드 / final_rank_score 92.305

## Ranked Build Guides

### Rank 1. 불씨 일제 사격 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 불씨 일제 사격
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 92.305
- estimated_dps_score: 3446.009
- single_target_score: 3067.77
- mapping_score: 3968.339
- interaction_score: 1132.0
- survivability_score: 35.98
- legality_score: 57

#### 추천 보조젬

- 마름쇠
- 화산 분출
- 분화구
- 얼어붙은 악의
- 충전된 징표
- 정전기 감전

#### 추천 유니크

- 황혼의 감시 / engine
- 세케마의 결의 / engine
- 이중 시야 / engine
- 질식의 진노 / engine
- 붕괴하는 지평선 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- charge_scaling
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- ... 외 19개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 3개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 2. 연발 사격 가능 얼음촉 화살 투사체 발동 번개 냉기 빌드

- 메인 스킬: 연발 사격 가능 얼음촉 화살
- 아키타입: 투사체 발동 번개 냉기
- final_rank_score: 89.923
- estimated_dps_score: 3065.501
- single_target_score: 2729.028
- mapping_score: 3530.155
- interaction_score: 1007.0
- survivability_score: 40.44
- legality_score: 65

#### 추천 보조젬

- 마름쇠
- 얼어붙은 악의
- 화산 분출
- 독 포자
- 분화구
- 몽상가의 종소리

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 붕괴하는 지평선 / engine
- 어둠살대 / engine
- 폭풍의 합창 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability] DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 3. 마름쇠의 발자취 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 마름쇠의 발자취
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 89.234
- estimated_dps_score: 3025.911
- single_target_score: 2693.783
- mapping_score: 3484.565
- interaction_score: 994.0
- survivability_score: 40.44
- legality_score: 65

#### 추천 보조젬

- 마름쇠
- 독 포자
- 화산 분출
- 분화구
- 몽상가의 종소리
- 얼어붙은 악의

#### 추천 유니크

- 붕괴하는 지평선 / engine
- 이중 시야 / engine
- 어둠살대 / engine
- 폭풍의 합창 / engine
- 세케마의 결의 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability] DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 4. 원소 표현 투사체 발동 번개 냉기 빌드

- 메인 스킬: 원소 표현
- 아키타입: 투사체 발동 번개 냉기
- final_rank_score: 87.573
- estimated_dps_score: 3217.695
- single_target_score: 2864.517
- mapping_score: 3705.418
- interaction_score: 1057.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 세차게 흐르는 전류
- 화산 분출
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 얼어붙은 악의

#### 추천 유니크

- 세케마의 결의 / engine
- 이중 시야 / engine
- 황혼의 감시 / engine
- 폭풍의 합창 / engine
- 뱀구덩이 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 3개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 5. 종말 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 종말
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 86.209
- estimated_dps_score: 3095.935
- single_target_score: 2756.121
- mapping_score: 3565.202
- interaction_score: 1017.0
- survivability_score: 35.98
- legality_score: 57

#### 추천 보조젬

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 충전된 징표

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 황혼의 감시 / engine
- 폭풍의 합창 / engine
- 대지속박 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- charge_scaling
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- ... 외 19개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 3개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 6. 원소 폭풍 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 폭풍
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 86.156
- estimated_dps_score: 3092.899
- single_target_score: 2753.418
- mapping_score: 3561.706
- interaction_score: 1016.0
- survivability_score: 35.98
- legality_score: 57

#### 추천 보조젬

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 충전된 징표

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 황혼의 감시 / engine
- 폭풍의 합창 / engine
- 대지속박 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- charge_scaling
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- ... 외 19개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 3개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 7. 선대의 함성 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 선대의 함성
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 82.503
- estimated_dps_score: 2639.308
- single_target_score: 2349.614
- mapping_score: 3039.361
- interaction_score: 867.0
- survivability_score: 40.44
- legality_score: 65

#### 추천 보조젬

- 화산 분출
- 마름쇠
- 분화구
- 몽상가의 종소리
- 독 포자
- 얼어붙은 악의

#### 추천 유니크

- 황혼의 감시 / engine
- 세케마의 결의 / engine
- 이중 시야 / engine
- 질식의 진노 / engine
- 붕괴하는 지평선 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability] DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 8. 원소 쇄도 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 쇄도
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 80.364
- estimated_dps_score: 2803.694
- single_target_score: 2495.957
- mapping_score: 3228.664
- interaction_score: 921.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 황혼의 감시 / engine
- 폭풍의 합창 / engine
- 대지속박 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 3개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 9. 전용 탈출 사격 투사체 발동 번개 냉기 빌드

- 메인 스킬: 전용 탈출 사격
- 아키타입: 투사체 발동 번개 냉기
- final_rank_score: 75.7
- estimated_dps_score: 2535.813
- single_target_score: 2257.479
- mapping_score: 2920.18
- interaction_score: 833.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 얼어붙은 악의
- 화산 분출
- 마름쇠
- 세차게 흐르는 전류
- 하욕시의 뇌전
- 엄습하는 오한

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 붕괴하는 지평선 / engine
- 폭풍의 합창 / engine
- 질식의 진노 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 3개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 10. 화산 균열 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 화산 균열
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 70.63
- estimated_dps_score: 1957.403
- single_target_score: 1742.556
- mapping_score: 2254.097
- interaction_score: 643.0
- survivability_score: 40.44
- legality_score: 65

#### 추천 보조젬

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출
- 삭망

#### 추천 유니크

- 세케마의 결의 / engine
- 황혼의 감시 / engine
- Sacred Flame / scaling
- Guiding Palm of the Heart / scaling
- Heatshiver / scaling

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- ... 외 1개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 11. 대장간 망치 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 대장간 망치
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 70.63
- estimated_dps_score: 1957.403
- single_target_score: 1742.556
- mapping_score: 2254.097
- interaction_score: 643.0
- survivability_score: 40.44
- legality_score: 65

#### 추천 보조젬

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출
- 삭망

#### 추천 유니크

- 세케마의 결의 / engine
- 황혼의 감시 / engine
- Sacred Flame / scaling
- Guiding Palm of the Heart / scaling
- Heatshiver / scaling

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- ... 외 1개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 12. 부패 효과 범위 발동 번개 화염 빌드

- 메인 스킬: 부패
- 아키타입: 효과 범위 발동 번개 화염
- final_rank_score: 70.299
- estimated_dps_score: 1359.288
- single_target_score: 1580.361
- mapping_score: 1053.996
- interaction_score: 938.0
- survivability_score: 40.68
- legality_score: 70

#### 추천 보조젬

- 분화구
- 독 포자
- 충전된 징표
- 하욕시의 뇌전
- 정전기 감전
- 몽상가의 종소리

#### 추천 유니크

- 황혼의 감시 / engine
- 이중 시야 / engine
- 어둠살대 / engine
- 분노의 첨탑 / engine
- 붕괴하는 지평선 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge
- charge_scaling
- cold
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- gain_as_extra
- life
- ... 외 9개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 13. 피사냥개의 징표 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 피사냥개의 징표
- 아키타입: 번개 효과 범위 발동 화염
- final_rank_score: 68.951
- estimated_dps_score: 1392.301
- single_target_score: 1618.744
- mapping_score: 1079.595
- interaction_score: 840.0
- survivability_score: 40.68
- legality_score: 70

#### 추천 보조젬

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표
- 정전기 감전

#### 추천 유니크

- 붕괴하는 지평선 / engine
- 이중 시야 / engine
- 어둠살대 / engine
- 폭풍의 합창 / engine
- 분노의 첨탑 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge
- charge_scaling
- cold
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- gain_as_extra
- life
- ... 외 10개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 14. 원소 상태 이상 시 시전 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 상태 이상 시 시전
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 68.809
- estimated_dps_score: 2140.054
- single_target_score: 1905.159
- mapping_score: 2464.433
- interaction_score: 703.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 황혼의 감시 / engine
- 폭풍의 합창 / engine
- 대지속박 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 15. 조건부 원소 기원 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 조건부 원소 기원
- 아키타입: 투사체 발동 번개 연쇄
- final_rank_score: 68.809
- estimated_dps_score: 2140.054
- single_target_score: 1905.159
- mapping_score: 2464.433
- interaction_score: 703.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

#### 추천 유니크

- 이중 시야 / engine
- 세케마의 결의 / engine
- 황혼의 감시 / engine
- 폭풍의 합창 / engine
- 대지속박 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 16. 구형 번개 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 구형 번개
- 아키타입: 투사체 번개 연쇄 효과 범위
- final_rank_score: 67.749
- estimated_dps_score: 2079.185
- single_target_score: 1850.971
- mapping_score: 2394.338
- interaction_score: 683.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

#### 추천 유니크

- 세케마의 결의 / engine
- 뱀구덩이 / support
- Drillneck / support
- Tyranny's Grip / support
- Chainsting / support

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 17. 공허 환상 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 공허 환상
- 아키타입: 번개 효과 범위 발동 화염
- final_rank_score: 67.438
- estimated_dps_score: 1324.34
- single_target_score: 1539.729
- mapping_score: 1026.897
- interaction_score: 799.0
- survivability_score: 40.68
- legality_score: 70

#### 추천 보조젬

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표
- 정전기 감전

#### 추천 유니크

- 붕괴하는 지평선 / engine
- 이중 시야 / engine
- 어둠살대 / engine
- 폭풍의 합창 / engine
- 분노의 첨탑 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge
- charge_scaling
- cold
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- gain_as_extra
- life
- ... 외 10개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 18. 보강하는 함성 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 보강하는 함성
- 아키타입: 번개 효과 범위 발동 화염
- final_rank_score: 67.032
- estimated_dps_score: 1306.115
- single_target_score: 1518.541
- mapping_score: 1012.766
- interaction_score: 788.0
- survivability_score: 40.68
- legality_score: 70

#### 추천 보조젬

- 분화구
- 몽상가의 종소리
- 독 포자
- 마름쇠
- 충전된 징표
- 정전기 감전

#### 추천 유니크

- 붕괴하는 지평선 / engine
- 이중 시야 / engine
- 어둠살대 / engine
- 폭풍의 합창 / engine
- 분노의 첨탑 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge
- charge_scaling
- cold
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- gain_as_extra
- life
- ... 외 10개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 19. 청산 감전연쇄 화살 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 청산 감전연쇄 화살
- 아키타입: 투사체 번개 연쇄 효과 범위
- final_rank_score: 65.682
- estimated_dps_score: 1960.462
- single_target_score: 1745.279
- mapping_score: 2257.62
- interaction_score: 644.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

#### 추천 유니크

- 세케마의 결의 / engine
- 뱀구덩이 / support
- Drillneck / support
- Tyranny's Grip / support
- Chainsting / support

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 20. 지옥불 함성 효과 범위 발동 번개 화염 빌드

- 메인 스킬: 지옥불 함성
- 아키타입: 효과 범위 발동 번개 화염
- final_rank_score: 65.426
- estimated_dps_score: 1267.989
- single_target_score: 1474.214
- mapping_score: 983.202
- interaction_score: 765.0
- survivability_score: 39.14
- legality_score: 70

#### 추천 보조젬

- 분화구
- 몽상가의 종소리
- 마름쇠
- 독 포자
- 충전된 징표
- 정전기 감전

#### 추천 유니크

- 황혼의 감시 / engine
- 이중 시야 / engine
- 붕괴하는 지평선 / engine
- 어둠살대 / engine
- 폭풍의 합창 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge_scaling
- cold
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- gain_as_extra
- life
- lightning
- ... 외 9개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 21. 전기불꽃 투사체 발동 번개 냉기 빌드

- 메인 스킬: 전기불꽃
- 아키타입: 투사체 발동 번개 냉기
- final_rank_score: 63.794
- estimated_dps_score: 1610.598
- single_target_score: 1546.131
- mapping_score: 1699.625
- interaction_score: 767.0
- survivability_score: 34.44
- legality_score: 57

#### 추천 보조젬

- 마름쇠
- 세차게 흐르는 전류
- 얼어붙은 악의
- 정전기 감전
- 살아 있는 번개
- 살아 있는 번개 II

#### 추천 유니크

- 세케마의 결의 / engine
- 폭풍의 합창 / engine
- 이중 시야 / engine
- 대지속박 / engine
- 붕괴하는 지평선 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- ... 외 16개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- ... 외 4개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 22. 연발 사격 가능 번개 화살 투사체 연쇄 효과 범위 소환수 빌드

- 메인 스킬: 연발 사격 가능 번개 화살
- 아키타입: 투사체 연쇄 효과 범위 소환수
- final_rank_score: 63.625
- estimated_dps_score: 1819.963
- single_target_score: 1669.384
- mapping_score: 2027.905
- interaction_score: 616.0
- survivability_score: 34.58
- legality_score: 57

#### 추천 보조젬

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

#### 추천 유니크

- 세케마의 결의 / engine
- 뱀구덩이 / enable
- Drillneck / enable
- Tyranny's Grip / enable
- Chainsting / enable

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- chain
- chaos
- charge
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- fork
- gain_as_extra
- ... 외 18개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 23. 기폭 장치 원소 약화 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 기폭 장치 원소 약화
- 아키타입: 투사체 번개 연쇄 효과 범위
- final_rank_score: 63.259
- estimated_dps_score: 1777.811
- single_target_score: 1582.676
- mapping_score: 2047.283
- interaction_score: 584.0
- survivability_score: 35.98
- legality_score: 57

#### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 분화구
- 충전된 징표

#### 추천 유니크

- 세케마의 결의 / engine
- Painter's Servant / scaling
- Heatshiver / scaling
- 질식의 진노 / scaling
- Queen of the Forest / support

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chain
- chaos
- charge
- charge_scaling
- cold
- conversion
- crit
- crit_scaling
- duration
- extra_projectile
- fire
- ... 외 19개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 연쇄 + 범위 중첩 조합으로 맵핑과 보스 근접 중첩 효율이 함께 증가할 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩으로 여러 피해 스케일링 축을 동시에 활용할 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- ... 외 5개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 소환수 스케일링과 비소환수 직접 피해 스케일링이 함께 강하게 추천되어 실제 적용 대상을 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality] 전환 + 추가 피해 획득 조합은 강력하지만 실제 적용 순서/중복 적용 규칙 데이터가 없어 scaling legality를 확정할 수 없습니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- ... 외 2개

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 24. 무기 담금질 효과 범위 발동 화염 냉기 빌드

- 메인 스킬: 무기 담금질
- 아키타입: 효과 범위 발동 화염 냉기
- final_rank_score: 63.231
- estimated_dps_score: 1094.097
- single_target_score: 1272.04
- mapping_score: 848.366
- interaction_score: 755.0
- survivability_score: 39.14
- legality_score: 70

#### 추천 보조젬

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II
- 하욕시의 뇌전

#### 추천 유니크

- 황혼의 감시 / engine
- 이중 시야 / engine
- 붕괴하는 지평선 / engine
- 폭풍의 합창 / engine
- 분노의 첨탑 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge
- cold
- crit
- crit_scaling
- extra_projectile
- fire
- gain_as_extra
- life
- lightning
- mana
- ... 외 7개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.

### Rank 25. 폭발 마그마 장벽 효과 범위 발동 화염 근접 빌드

- 메인 스킬: 폭발 마그마 장벽
- 아키타입: 효과 범위 발동 화염 근접
- final_rank_score: 63.196
- estimated_dps_score: 1092.641
- single_target_score: 1270.347
- mapping_score: 847.237
- interaction_score: 754.0
- survivability_score: 39.14
- legality_score: 70

#### 추천 보조젬

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II
- 하욕시의 뇌전

#### 추천 유니크

- 황혼의 감시 / engine
- 이중 시야 / engine
- 붕괴하는 지평선 / engine
- 폭풍의 합창 / engine
- 분노의 첨탑 / engine

#### 추천 희귀 Affix

- 투사체 리턴 샷건 무기 / weapon
- 치명타 발동 목걸이 / amulet

#### Core Mechanics

- ailment_scaling
- chaos
- charge
- cold
- crit
- crit_scaling
- extra_projectile
- fire
- gain_as_extra
- life
- lightning
- mana
- ... 외 7개

#### 왜 강한가

- 돌아오는 투사체 다중 적중: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음
- 돌아오는 투사체 + 다중 적중 조합으로 단일 대상 적중 수가 크게 늘어날 수 있음
- 추가 투사체가 단순 범위 증가가 아니라 같은 대상 다중 적중으로 연결될 수 있음
- 치명타가 발동 빈도와 피해 스케일링을 동시에 밀어올리는 엔진 역할을 할 수 있음
- 추가 투사체 메커닉으로 기본 적중/커버리지 기대값을 올림
- 돌아오는 투사체 메커닉이 있어 왕복 적중 가능성을 별도 가중함
- 다중 적중 가능성이 있어 단일 대상 점수에 큰 가중치를 부여함
- 범위 중첩 메커닉이 있어 보스 근접 중첩과 맵핑 양쪽에 기여할 수 있음
- ... 외 3개

#### 약점 / 검증 필요

- [legality] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [legality] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.
- [legality] 공격/주문 스케일링이 함께 감지되어 메인 스킬 타입과 보조젬 적용 대상을 확인해야 합니다.
- [legality_missing_data] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [legality_missing_data] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [survivability] legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- [survivability] 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- [survivability] 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- [survivability_missing_data] 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- [survivability_missing_data] 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

#### TODO Leveling Section

- 레벨 구간별 스킬 전환 데이터가 아직 없어서 실제 leveling progression은 생성하지 않습니다.
- 향후 Leveling Planner에서 LV1~12, LV12~28, 전환 시점, 최종 빌드 online 시점을 채워야 합니다.

#### TODO Passive Progression Section

- 패시브 경로/노터블 순서/키스톤 타이밍 데이터가 아직 최종 랭킹 입력에 연결되지 않았습니다.
- 향후 Passive Path Planner에서 효율 경로와 전환 타이밍을 채워야 합니다.

#### TODO Gear Progression Section

- 현재는 추천 유니크와 희귀 affix 후보만 표시하며, early/mid/late/final BIS 진행은 생성하지 않습니다.
- 향후 Gear Evolution Planner에서 unique swap, rare affix upgrade, crafting priority를 채워야 합니다.
