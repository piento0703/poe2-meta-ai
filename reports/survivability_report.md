# Survivability Approximation Report

> 이 리포트는 정확한 PoE2 EHP 계산이 아니라 현재 태그/상호작용/선택 입력을 이용한 상대 생존력 추정입니다.
> 실제 생명력, ES, 방어도, 회피, 막기, 저항, 회복량 데이터가 없으면 missing_data로 표시하고 가짜 수치를 만들지 않습니다.

## 입력 / 출력

- 입력: `data/meta/build_interaction_analysis.json`
- 선택 입력: `data/meta/build_dps_estimates.json` (사용됨)
- 선택 입력: `data/meta/build_legality_analysis.json` (사용됨)
- JSON 출력: `data/meta/build_survivability_estimates.json`
- 리포트 출력: `reports/survivability_report.md`

## 모델링 범위

- 포함: life, ES, mana, spirit, charge, cold/ailment control, minion aggro 분산 태그 기반 상대 점수
- 미포함: 실제 생명력/ES 수치, 방어도, 회피, 막기, 저항, 피해 감소, 회복량, 플라스크, 몬스터 피해량
- 누락 데이터는 결과 JSON의 `missing_data` 필드에 표시합니다.

## 요약

- 분석 빌드 수: 100
- 최고 생존력 후보: 부패 효과 범위 발동 번개 화염 빌드 / survivability_score 40.68

## Top Survivability Candidates

### 1. 부패 효과 범위 발동 번개 화염 빌드

- 메인 스킬: 부패
- survivability_score: 40.68
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 43
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1359.288
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 1개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 2. 피사냥개의 징표 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 피사냥개의 징표
- survivability_score: 40.68
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 43
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1392.301
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 1개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 3. 공허 환상 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 공허 환상
- survivability_score: 40.68
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 43
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1324.34
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 1개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 4. 보강하는 함성 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 보강하는 함성
- survivability_score: 40.68
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 43
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1306.115
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 1개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 5. 연발 사격 가능 얼음촉 화살 투사체 발동 번개 냉기 빌드

- 메인 스킬: 연발 사격 가능 얼음촉 화살
- survivability_score: 40.44
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 44
- sustain_score: 43
- estimated_dps_score: 3065.501
- legality_score: 65

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- ... 외 2개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 6. 마름쇠의 발자취 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 마름쇠의 발자취
- survivability_score: 40.44
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 44
- sustain_score: 43
- estimated_dps_score: 3025.911
- legality_score: 65

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- ... 외 2개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 7. 선대의 함성 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 선대의 함성
- survivability_score: 40.44
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 44
- sustain_score: 43
- estimated_dps_score: 2639.308
- legality_score: 65

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- ... 외 2개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 8. 화산 균열 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 화산 균열
- survivability_score: 40.44
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 44
- sustain_score: 43
- estimated_dps_score: 1957.403
- legality_score: 65

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- ... 외 2개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 9. 대장간 망치 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 대장간 망치
- survivability_score: 40.44
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 44
- sustain_score: 43
- estimated_dps_score: 1957.403
- legality_score: 65

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- ... 외 2개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 10. 선대의 혼백 번개 소환수 발동 화염 빌드

- 메인 스킬: 선대의 혼백
- survivability_score: 39.84
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 44
- sustain_score: 38
- estimated_dps_score: 749.196
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- ... 외 1개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 11. 지옥불 함성 효과 범위 발동 번개 화염 빌드

- 메인 스킬: 지옥불 함성
- survivability_score: 39.14
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1267.989
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 12. 무기 담금질 효과 범위 발동 화염 냉기 빌드

- 메인 스킬: 무기 담금질
- survivability_score: 39.14
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1094.097
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 13. 폭발 마그마 장벽 효과 범위 발동 화염 근접 빌드

- 메인 스킬: 폭발 마그마 장벽
- survivability_score: 39.14
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 36
- avoidance_score: 39
- sustain_score: 38
- estimated_dps_score: 1092.641
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 14. 맹독성 영역 투사체 발동 연쇄 효과 범위 빌드

- 메인 스킬: 맹독성 영역
- survivability_score: 38.9
- ehp_score: 47
- recovery_score: 29
- mitigation_score: 29
- avoidance_score: 44
- sustain_score: 43
- estimated_dps_score: 1104.713
- legality_score: 70

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- 마나 태그는 유지력/자원 기반 방어 가능성으로만 보수 가산함
- 소환수는 어그로 분산 가능성이 있으나 실제 AI/소환수 수치가 없어 낮게 반영함
- ... 외 1개

#### 약점

- legality_score가 중간 수준이라 조건부 작동 리스크를 생존 점수에 일부 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 15. 메타 낙뢰 번개 효과 범위 발동 빌드

- 메인 스킬: 메타 낙뢰
- survivability_score: 37.1
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 42
- avoidance_score: 39
- sustain_score: 35
- estimated_dps_score: 947.731
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 16. 격파 장법 효과 범위 근접 발동 냉기 빌드

- 메인 스킬: 격파 장법
- survivability_score: 36.4
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 35
- avoidance_score: 45
- sustain_score: 35
- estimated_dps_score: 926.664
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 17. 연발 사격 가능 빙하 창 냉기 효과 범위 투사체 지속시간 빌드

- 메인 스킬: 연발 사격 가능 빙하 창
- survivability_score: 36.4
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 35
- avoidance_score: 45
- sustain_score: 35
- estimated_dps_score: 725.965
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 18. 빙하 볼트 냉기 효과 범위 투사체 지속시간 빌드

- 메인 스킬: 빙하 볼트
- survivability_score: 36.4
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 35
- avoidance_score: 45
- sustain_score: 35
- estimated_dps_score: 725.965
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 19. 불씨 일제 사격 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 불씨 일제 사격
- survivability_score: 35.98
- ehp_score: 41
- recovery_score: 23
- mitigation_score: 37
- avoidance_score: 38
- sustain_score: 37
- estimated_dps_score: 3446.009
- legality_score: 57

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 3개

#### 약점

- legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 20. 종말 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 종말
- survivability_score: 35.98
- ehp_score: 41
- recovery_score: 23
- mitigation_score: 37
- avoidance_score: 38
- sustain_score: 37
- estimated_dps_score: 3095.935
- legality_score: 57

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 3개

#### 약점

- legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 21. 원소 폭풍 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 폭풍
- survivability_score: 35.98
- ehp_score: 41
- recovery_score: 23
- mitigation_score: 37
- avoidance_score: 38
- sustain_score: 37
- estimated_dps_score: 3092.899
- legality_score: 57

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 3개

#### 약점

- legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.
- DPS 추정치는 높지만 EHP 근거가 낮아 glass cannon 후보일 수 있습니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 22. 기폭 장치 원소 약화 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 기폭 장치 원소 약화
- survivability_score: 35.98
- ehp_score: 41
- recovery_score: 23
- mitigation_score: 37
- avoidance_score: 38
- sustain_score: 37
- estimated_dps_score: 1777.811
- legality_score: 57

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함
- 충전 기반 방어/유지 가능성이 있으나 charge 종류가 불명확해 낮게 반영함
- 충전 스케일링은 방어 충전 활용 가능성이 있으나 실제 charge 종류가 없어 보수적으로 반영함
- 냉각/동결 계열 군중제어 가능성을 회피/안전성에 낮게 반영함
- 생명력 관련 태그가 있어 상대 EHP 기반을 보수적으로 가산함
- ... 외 3개

#### 약점

- legality_score가 낮아 실제 작동 가능성/장비 조건 불확실성을 생존 점수에 강하게 감점함
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 23. 폭발 바람의 무희 효과 범위 발동 근접 번개 빌드

- 메인 스킬: 폭발 바람의 무희
- survivability_score: 35.56
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 35
- avoidance_score: 39
- sustain_score: 35
- estimated_dps_score: 891.406
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 24. 가스 화살 투사체 효과 범위 화염 카오스 빌드

- 메인 스킬: 가스 화살
- survivability_score: 35.56
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 35
- avoidance_score: 39
- sustain_score: 35
- estimated_dps_score: 745.324
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.

### 25. 가스 유탄 투사체 효과 범위 화염 카오스 빌드

- 메인 스킬: 가스 유탄
- survivability_score: 35.56
- ehp_score: 35
- recovery_score: 35
- mitigation_score: 35
- avoidance_score: 39
- sustain_score: 35
- estimated_dps_score: 745.324
- legality_score: 78

#### 방어 근거

- 상태이상 제어 가능성이 있지만 방어 상태이상인지 불명확해 낮게 반영함

#### 약점

- 생명력/ES/마나 기반 방어 태그가 부족해 EHP 근거가 약합니다.
- 방어도/저항/피해 감소/인내 충전 같은 명확한 mitigation 데이터가 부족합니다.
- 흡수/재생/회복 플라스크/처치 시 회복 등 recovery 데이터가 부족합니다.

#### Missing Data / TODO

- 실제 생명력, ES, 방어도, 회피, 막기, 저항, 피해 감소 수치가 없어 상대 휴리스틱으로만 평가했습니다.
- 재생, 흡수, 회복량, 플라스크, 처치 시 회복 수치가 없어 recovery_score는 태그 기반 추정입니다.
