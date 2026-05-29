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

## 요약: 25개 빌드 분석

## #1 불씨 일제 사격 투사체 발동 번개 연쇄 빌드

- 주력 스킬: 불씨 일제 사격
- final_rank_score: 92.305
- routing_status: `heuristic_only`
- 설명: 이 MVP는 정확한 패시브 경로를 발명하지 않습니다. passive node 이름/스탯과 빌드 메커닉을 매칭한 우선순위 가이드입니다.

### LV1~12

- 전환 타이밍: 초반에는 최종 빌드의 핵심 피해 태그와 생명력/저항 계열을 우선합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: 장비/젬 요구치를 위한 속성 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV12~28

- 전환 타이밍: 주력 스킬/보조젬이 갖춰지는 구간으로, 공격 태그와 방어 기반을 함께 확장합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 회피/막기/avoidance 기반 보강
- 유틸 우선순위: 마나 비용/마나 유지 안정화, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV28~45

- 전환 타이밍: 핵심 메커닉 전환 후보 구간입니다. 정확한 전환 레벨은 unlock 데이터 부재로 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강, 재생/회복/흡수 기반 sustain 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV45~65

- 전환 타이밍: 엔드게임 전 준비 구간입니다. 핵심 딜 스케일링과 방어층을 균형 있게 확보합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV65+

- 전환 타이밍: 최종 빌드 온라인 후보 구간입니다. 정확한 패시브 경로/keystone timing은 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

## #2 연발 사격 가능 얼음촉 화살 투사체 발동 번개 냉기 빌드

- 주력 스킬: 연발 사격 가능 얼음촉 화살
- final_rank_score: 89.923
- routing_status: `heuristic_only`
- 설명: 이 MVP는 정확한 패시브 경로를 발명하지 않습니다. passive node 이름/스탯과 빌드 메커닉을 매칭한 우선순위 가이드입니다.

### LV1~12

- 전환 타이밍: 초반에는 최종 빌드의 핵심 피해 태그와 생명력/저항 계열을 우선합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: 장비/젬 요구치를 위한 속성 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV12~28

- 전환 타이밍: 주력 스킬/보조젬이 갖춰지는 구간으로, 공격 태그와 방어 기반을 함께 확장합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 회피/막기/avoidance 기반 보강
- 유틸 우선순위: 마나 비용/마나 유지 안정화, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV28~45

- 전환 타이밍: 핵심 메커닉 전환 후보 구간입니다. 정확한 전환 레벨은 unlock 데이터 부재로 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강, 재생/회복/흡수 기반 sustain 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV45~65

- 전환 타이밍: 엔드게임 전 준비 구간입니다. 핵심 딜 스케일링과 방어층을 균형 있게 확보합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV65+

- 전환 타이밍: 최종 빌드 온라인 후보 구간입니다. 정확한 패시브 경로/keystone timing은 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

## #3 마름쇠의 발자취 투사체 발동 번개 연쇄 빌드

- 주력 스킬: 마름쇠의 발자취
- final_rank_score: 89.234
- routing_status: `heuristic_only`
- 설명: 이 MVP는 정확한 패시브 경로를 발명하지 않습니다. passive node 이름/스탯과 빌드 메커닉을 매칭한 우선순위 가이드입니다.

### LV1~12

- 전환 타이밍: 초반에는 최종 빌드의 핵심 피해 태그와 생명력/저항 계열을 우선합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: 장비/젬 요구치를 위한 속성 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV12~28

- 전환 타이밍: 주력 스킬/보조젬이 갖춰지는 구간으로, 공격 태그와 방어 기반을 함께 확장합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 회피/막기/avoidance 기반 보강
- 유틸 우선순위: 마나 비용/마나 유지 안정화, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV28~45

- 전환 타이밍: 핵심 메커닉 전환 후보 구간입니다. 정확한 전환 레벨은 unlock 데이터 부재로 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강, 재생/회복/흡수 기반 sustain 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV45~65

- 전환 타이밍: 엔드게임 전 준비 구간입니다. 핵심 딜 스케일링과 방어층을 균형 있게 확보합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV65+

- 전환 타이밍: 최종 빌드 온라인 후보 구간입니다. 정확한 패시브 경로/keystone timing은 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

## #4 원소 표현 투사체 발동 번개 냉기 빌드

- 주력 스킬: 원소 표현
- final_rank_score: 87.573
- routing_status: `heuristic_only`
- 설명: 이 MVP는 정확한 패시브 경로를 발명하지 않습니다. passive node 이름/스탯과 빌드 메커닉을 매칭한 우선순위 가이드입니다.

### LV1~12

- 전환 타이밍: 초반에는 최종 빌드의 핵심 피해 태그와 생명력/저항 계열을 우선합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: 장비/젬 요구치를 위한 속성 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV12~28

- 전환 타이밍: 주력 스킬/보조젬이 갖춰지는 구간으로, 공격 태그와 방어 기반을 함께 확장합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 회피/막기/avoidance 기반 보강
- 유틸 우선순위: 마나 비용/마나 유지 안정화, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV28~45

- 전환 타이밍: 핵심 메커닉 전환 후보 구간입니다. 정확한 전환 레벨은 unlock 데이터 부재로 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강, 재생/회복/흡수 기반 sustain 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV45~65

- 전환 타이밍: 엔드게임 전 준비 구간입니다. 핵심 딜 스케일링과 방어층을 균형 있게 확보합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV65+

- 전환 타이밍: 최종 빌드 온라인 후보 구간입니다. 정확한 패시브 경로/keystone timing은 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

## #5 종말 투사체 발동 번개 연쇄 빌드

- 주력 스킬: 종말
- final_rank_score: 86.209
- routing_status: `heuristic_only`
- 설명: 이 MVP는 정확한 패시브 경로를 발명하지 않습니다. passive node 이름/스탯과 빌드 메커닉을 매칭한 우선순위 가이드입니다.

### LV1~12

- 전환 타이밍: 초반에는 최종 빌드의 핵심 피해 태그와 생명력/저항 계열을 우선합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: 장비/젬 요구치를 위한 속성 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV12~28

- 전환 타이밍: 주력 스킬/보조젬이 갖춰지는 구간으로, 공격 태그와 방어 기반을 함께 확장합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 회피/막기/avoidance 기반 보강
- 유틸 우선순위: 마나 비용/마나 유지 안정화, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV28~45

- 전환 타이밍: 핵심 메커닉 전환 후보 구간입니다. 정확한 전환 레벨은 unlock 데이터 부재로 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 방어도/저항/피해 감소 기반 보강, 재생/회복/흡수 기반 sustain 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 마나 비용/마나 유지 안정화
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV45~65

- 전환 타이밍: 엔드게임 전 준비 구간입니다. 핵심 딜 스케일링과 방어층을 균형 있게 확보합니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현

### LV65+

- 전환 타이밍: 최종 빌드 온라인 후보 구간입니다. 정확한 패시브 경로/keystone timing은 TODO입니다.
- 공격 우선순위: 상태 이상 피해/확률 관련 노드, 연쇄/투사체 확산 관련 노드, 카오스 피해 관련 노드
- 방어 우선순위: 생명력/최대 생명력 확보, 에너지 보호막 기반 보강, 방어도/저항/피해 감소 기반 보강
- 유틸 우선순위: charge 생성/유지 관련 유틸리티, spirit reservation/유틸리티 여유 확보, 이동/공격/시전 속도 유틸리티
- notable/keystone 후보:
  - `Elemental Equilibrium` (keystone, id: 46742) — Create [Lightning] [ElementalInfusion|Infusion] [Remnant|Remnants] instead of [Fire] Create [Cold] [ElementalInfusion|Infusion] [Remnant|Re…
  - `Blackflame Covenant` (keystone, id: 42680) — [Fire] [Spell|Spells] [Conversion|Convert] 100% of Fire Damage to [Chaos|Chaos Damage] [Chaos|Chaos Damage] from [Fire] [Spell|Spells] [Con…
  - `Avatar of Fire` (keystone, id: 18684) — 75% of Damage Converted to Fire Damage Deal no Non-Fire Damage
- TODO/missing data:
  - exact passive route/class start/shortest path 미구현
