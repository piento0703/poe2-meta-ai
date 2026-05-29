# Legality Validation Report

> 이 리포트는 실제 게임 규칙 전체 검증이 아니라 현재 저장소에 있는 데이터로 가능한 보수적 MVP 검증입니다.
> 정확한 support compatibility, weapon restriction, trigger condition 데이터가 없는 경우 불법으로 단정하지 않고 TODO/skipped/warning으로 표시합니다.

## 입력 / 출력

- 입력: `data/meta/build_interaction_analysis.json`
- 선택 입력: `data/meta/build_dps_estimates.json` (사용됨)
- JSON 출력: `data/meta/build_legality_analysis.json`
- 리포트 출력: `reports/legality_report.md`

## 요약

- 분석 빌드 수: 100
- plausible/legal 후보 수: 84
- warnings 포함 빌드 수: 100
- missing_data 포함 빌드 수: 100
- violations 포함 빌드 수: 0

## Top Plausible Candidates

### 1. 격파 장법 효과 범위 근접 발동 냉기 빌드

- 메인 스킬: 격파 장법
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 926.664
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 2. 메타 낙뢰 번개 효과 범위 발동 빌드

- 메인 스킬: 메타 낙뢰
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 947.731
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 3. 폭발 바람의 무희 효과 범위 발동 근접 번개 빌드

- 메인 스킬: 폭발 바람의 무희
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 891.406
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 4. 가스 화살 투사체 효과 범위 화염 카오스 빌드

- 메인 스킬: 가스 화살
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 745.324
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 5. 가스 유탄 투사체 효과 범위 화염 카오스 빌드

- 메인 스킬: 가스 유탄
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 745.324
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 6. 기폭 장치 충격 장법 효과 범위 근접 투사체 지속시간 빌드

- 메인 스킬: 기폭 장치 충격 장법
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 734.036
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 7. 폭발 창 투사체 효과 범위 화염 지속시간 빌드

- 메인 스킬: 폭발 창
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 8. 집중 유지 기름 유탄 투사체 효과 범위 화염 지속시간 빌드

- 메인 스킬: 집중 유지 기름 유탄
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 9. 공성 쇠뇌 투사체 효과 범위 화염 지속시간 빌드

- 메인 스킬: 공성 쇠뇌
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 10. 연발 사격 가능 빙하 창 냉기 효과 범위 투사체 지속시간 빌드

- 메인 스킬: 연발 사격 가능 빙하 창
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 11. 빙하 볼트 냉기 효과 범위 투사체 지속시간 빌드

- 메인 스킬: 빙하 볼트
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 12. 합쳐짐 얼어붙은 궤적 효과 범위 냉기 지속시간 근접 빌드

- 메인 스킬: 합쳐짐 얼어붙은 궤적
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 13. 신속한 공격 효과 범위 근접 지속시간 빌드

- 메인 스킬: 신속한 공격
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 634.701
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 14. 창의 지대 효과 범위 지속시간 근접 번개 빌드

- 메인 스킬: 창의 지대
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 15. 뜀틀 충격 효과 범위 근접 지속시간 빌드

- 메인 스킬: 뜀틀 충격
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 634.701
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 16. 강타 포대 쇠뇌 효과 범위 투사체 지속시간 번개 빌드

- 메인 스킬: 강타 포대 쇠뇌
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 17. 기폭 장치 떨어지는 천둥 효과 범위 근접 투사체 번개 빌드

- 메인 스킬: 기폭 장치 떨어지는 천둥
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 18. 청산 방패의 벽 효과 범위 지속시간 근접 빌드

- 메인 스킬: 청산 방패의 벽
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 634.701
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 19. 연발 사격 가능 독 폭발 화살 효과 범위 투사체 카오스 지속시간 빌드

- 메인 스킬: 연발 사격 가능 독 폭발 화살
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 20. 연발 사격 가능 덩굴 화살 효과 범위 투사체 카오스 지속시간 빌드

- 메인 스킬: 연발 사격 가능 덩굴 화살
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 21. 바람 폭풍의 종 효과 범위 지속시간 근접 번개 빌드

- 메인 스킬: 바람 폭풍의 종
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 22. 전용 충격파 토템 효과 범위 근접 지속시간 토템 빌드

- 메인 스킬: 전용 충격파 토템
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 702.072
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 23. 연발 사격 가능 회오리 사격 효과 범위 투사체 지속시간 빌드

- 메인 스킬: 연발 사격 가능 회오리 사격
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 24. 조건부 선대의 전사 토템 효과 범위 지속시간 근접 토템 빌드

- 메인 스킬: 조건부 선대의 전사 토템
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 725.965
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.

### 25. 지진 효과 범위 근접 지속시간 빌드

- 메인 스킬: 지진
- is_legal: True
- legality_score: 78
- decision_basis: plausible_with_missing_data
- estimated_dps_score: 702.072
- support_compatibility_status: passed_heuristic
- weapon_restriction_status: warning
- trigger_condition_status: warning
- scaling_conflict_status: passed_heuristic

#### Warnings

- [weapon_restriction_status] 무기 또는 quiver 관련 추천이 있어 실제 스킬 무기 제한과 슬롯 충돌을 후속 검증해야 합니다.
- [trigger_condition_status] trigger 또는 trigger loop 후보가 감지되었습니다. 실제 발동 조건과 반복 발동 가능 여부를 수동/규칙 데이터로 확인해야 합니다.

#### Missing Data / TODO

- [weapon_restriction_status] 무기 제한/착용 가능 조건/스킬별 사용 가능 무기 데이터가 없어 무기 관련 추천을 확정 검증하지 못했습니다.
- [trigger_condition_status] 발동 조건, 쿨다운, 내부 재사용 대기시간, socket/link 조건 데이터가 없어 trigger legality를 확정 검증하지 못했습니다.
- [scaling_conflict_status] 정확한 스케일링 적용 대상/순서/중복 규칙 데이터가 없어 conflict 검증을 휴리스틱 수준으로만 수행했습니다.
