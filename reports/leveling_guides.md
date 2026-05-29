# Leveling Guides MVP

> 이 문서는 final ranked build 상위 후보에 대한 1~endgame 레벨링 가이드 초안입니다.
> 정확한 unlock level, quest reward, passive path, gear progression 데이터가 없으면 TODO/missing_data로 표시합니다.

## 입력 / 출력

- 입력: `data/meta/final_ranked_builds.json`
- 입력: `data/skills/skills.json`
- 입력: `data/supports/supports.json`
- 입력: `data/passive/data.json`
- JSON 출력: `data/meta/leveling_plans.json`
- 리포트 출력: `reports/leveling_guides.md`

## 공통 레벨 구간

- LV1~12
- LV12~28
- LV28~45
- LV45~65
- LV65+

## 생성된 가이드 수: 25

## Rank 1. 불씨 일제 사격 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 불씨 일제 사격
- final_rank_score: 92.305

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 불씨 일제 사격
- transition skill: 불씨 일제 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 마름쇠
- 화산 분출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 불씨 일제 사격
- transition skill: 불씨 일제 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 마름쇠
- 화산 분출
- 분화구

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 불씨 일제 사격
- transition skill: 불씨 일제 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 마름쇠
- 화산 분출
- 분화구
- 얼어붙은 악의

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 불씨 일제 사격
- transition skill: 불씨 일제 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 마름쇠
- 화산 분출
- 분화구
- 얼어붙은 악의
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 불씨 일제 사격
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 마름쇠
- 화산 분출
- 분화구
- 얼어붙은 악의
- 충전된 징표
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 2. 연발 사격 가능 얼음촉 화살 투사체 발동 번개 냉기 빌드

- 메인 스킬: 연발 사격 가능 얼음촉 화살
- final_rank_score: 89.923

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 연발 사격 가능 얼음촉 화살
- transition skill: 연발 사격 가능 얼음촉 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 마름쇠
- 얼어붙은 악의

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 연발 사격 가능 얼음촉 화살
- transition skill: 연발 사격 가능 얼음촉 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 마름쇠
- 얼어붙은 악의
- 화산 분출

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 연발 사격 가능 얼음촉 화살
- transition skill: 연발 사격 가능 얼음촉 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 마름쇠
- 얼어붙은 악의
- 화산 분출
- 독 포자

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 연발 사격 가능 얼음촉 화살
- transition skill: 연발 사격 가능 얼음촉 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 마름쇠
- 얼어붙은 악의
- 화산 분출
- 독 포자
- 분화구

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 연발 사격 가능 얼음촉 화살
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 마름쇠
- 얼어붙은 악의
- 화산 분출
- 독 포자
- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 3. 마름쇠의 발자취 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 마름쇠의 발자취
- final_rank_score: 89.234

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 마름쇠의 발자취
- transition skill: 마름쇠의 발자취
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 마름쇠
- 독 포자

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 마름쇠의 발자취
- transition skill: 마름쇠의 발자취
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 마름쇠
- 독 포자
- 화산 분출

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 마름쇠의 발자취
- transition skill: 마름쇠의 발자취
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 마름쇠
- 독 포자
- 화산 분출
- 분화구

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 마름쇠의 발자취
- transition skill: 마름쇠의 발자취
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 마름쇠
- 독 포자
- 화산 분출
- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 마름쇠의 발자취
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 마름쇠
- 독 포자
- 화산 분출
- 분화구
- 몽상가의 종소리
- 얼어붙은 악의

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 4. 원소 표현 투사체 발동 번개 냉기 빌드

- 메인 스킬: 원소 표현
- final_rank_score: 87.573

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 원소 표현
- transition skill: 원소 표현
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 화산 분출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 원소 표현
- transition skill: 원소 표현
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 화산 분출
- 하욕시의 뇌전

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 원소 표현
- transition skill: 원소 표현
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 화산 분출
- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 원소 표현
- transition skill: 원소 표현
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 화산 분출
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 원소 표현
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 화산 분출
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 얼어붙은 악의

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 5. 종말 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 종말
- final_rank_score: 86.209

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 종말
- transition skill: 종말
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 종말
- transition skill: 종말
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 종말
- transition skill: 종말
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 종말
- transition skill: 종말
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 종말
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 6. 원소 폭풍 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 폭풍
- final_rank_score: 86.156

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 원소 폭풍
- transition skill: 원소 폭풍
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 원소 폭풍
- transition skill: 원소 폭풍
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 원소 폭풍
- transition skill: 원소 폭풍
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 원소 폭풍
- transition skill: 원소 폭풍
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 원소 폭풍
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 7. 선대의 함성 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 선대의 함성
- final_rank_score: 82.503

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 선대의 함성
- transition skill: 선대의 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 화산 분출
- 마름쇠

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 선대의 함성
- transition skill: 선대의 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 화산 분출
- 마름쇠
- 분화구

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 선대의 함성
- transition skill: 선대의 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 화산 분출
- 마름쇠
- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 선대의 함성
- transition skill: 선대의 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 화산 분출
- 마름쇠
- 분화구
- 몽상가의 종소리
- 독 포자

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 선대의 함성
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 화산 분출
- 마름쇠
- 분화구
- 몽상가의 종소리
- 독 포자
- 얼어붙은 악의

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 8. 원소 쇄도 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 쇄도
- final_rank_score: 80.364

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 원소 쇄도
- transition skill: 원소 쇄도
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 원소 쇄도
- transition skill: 원소 쇄도
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 원소 쇄도
- transition skill: 원소 쇄도
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 원소 쇄도
- transition skill: 원소 쇄도
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 원소 쇄도
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 9. 전용 탈출 사격 투사체 발동 번개 냉기 빌드

- 메인 스킬: 전용 탈출 사격
- final_rank_score: 75.7

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 전용 탈출 사격
- transition skill: 전용 탈출 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 얼어붙은 악의
- 화산 분출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 전용 탈출 사격
- transition skill: 전용 탈출 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 얼어붙은 악의
- 화산 분출
- 마름쇠

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 전용 탈출 사격
- transition skill: 전용 탈출 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 얼어붙은 악의
- 화산 분출
- 마름쇠
- 세차게 흐르는 전류

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 전용 탈출 사격
- transition skill: 전용 탈출 사격
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 얼어붙은 악의
- 화산 분출
- 마름쇠
- 세차게 흐르는 전류
- 하욕시의 뇌전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 전용 탈출 사격
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 얼어붙은 악의
- 화산 분출
- 마름쇠
- 세차게 흐르는 전류
- 하욕시의 뇌전
- 엄습하는 오한

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 10. 화산 균열 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 화산 균열
- final_rank_score: 70.63

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 화산 균열
- transition skill: 화산 균열
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 요철 지대 I

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 화산 균열
- transition skill: 화산 균열
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 화산 균열
- transition skill: 화산 균열
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 화산 균열
- transition skill: 화산 균열
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 화산 균열
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출
- 삭망

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 11. 대장간 망치 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 대장간 망치
- final_rank_score: 70.63

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 대장간 망치
- transition skill: 대장간 망치
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 요철 지대 I

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 대장간 망치
- transition skill: 대장간 망치
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 대장간 망치
- transition skill: 대장간 망치
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 대장간 망치
- transition skill: 대장간 망치
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 대장간 망치
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출
- 삭망

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 12. 부패 효과 범위 발동 번개 화염 빌드

- 메인 스킬: 부패
- final_rank_score: 70.299

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 부패
- transition skill: 부패
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 독 포자

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)
- 번개 피해와 감전/원소 피해 노드 우선 (`lightning`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 부패
- transition skill: 부패
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 독 포자
- 충전된 징표

#### Passive priority by stage

- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 부패
- transition skill: 부패
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 독 포자
- 충전된 징표
- 하욕시의 뇌전

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 부패
- transition skill: 부패
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 독 포자
- 충전된 징표
- 하욕시의 뇌전
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 부패
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 독 포자
- 충전된 징표
- 하욕시의 뇌전
- 정전기 감전
- 몽상가의 종소리

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 13. 피사냥개의 징표 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 피사냥개의 징표
- final_rank_score: 68.951

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 피사냥개의 징표
- transition skill: 피사냥개의 징표
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 독 포자
- 분화구

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 피사냥개의 징표
- transition skill: 피사냥개의 징표
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 피사냥개의 징표
- transition skill: 피사냥개의 징표
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 피사냥개의 징표
- transition skill: 피사냥개의 징표
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 피사냥개의 징표
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 14. 원소 상태 이상 시 시전 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 원소 상태 이상 시 시전
- final_rank_score: 68.809

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 원소 상태 이상 시 시전
- transition skill: 원소 상태 이상 시 시전
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 원소 상태 이상 시 시전
- transition skill: 원소 상태 이상 시 시전
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 원소 상태 이상 시 시전
- transition skill: 원소 상태 이상 시 시전
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 원소 상태 이상 시 시전
- transition skill: 원소 상태 이상 시 시전
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 원소 상태 이상 시 시전
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 15. 조건부 원소 기원 투사체 발동 번개 연쇄 빌드

- 메인 스킬: 조건부 원소 기원
- final_rank_score: 68.809

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 조건부 원소 기원
- transition skill: 조건부 원소 기원
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 조건부 원소 기원
- transition skill: 조건부 원소 기원
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 조건부 원소 기원
- transition skill: 조건부 원소 기원
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 조건부 원소 기원
- transition skill: 조건부 원소 기원
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 조건부 원소 기원
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 16. 구형 번개 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 구형 번개
- final_rank_score: 67.749

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 구형 번개
- transition skill: 구형 번개
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 폭풍연쇄

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 구형 번개
- transition skill: 구형 번개
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 구형 번개
- transition skill: 구형 번개
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압
- 도미누스의 장악

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 구형 번개
- transition skill: 구형 번개
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압
- 도미누스의 장악
- 연쇄 I

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 구형 번개
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 17. 공허 환상 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 공허 환상
- final_rank_score: 67.438

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 공허 환상
- transition skill: 공허 환상
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 독 포자
- 분화구

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 공허 환상
- transition skill: 공허 환상
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 공허 환상
- transition skill: 공허 환상
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 공허 환상
- transition skill: 공허 환상
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 공허 환상
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 18. 보강하는 함성 번개 효과 범위 발동 화염 빌드

- 메인 스킬: 보강하는 함성
- final_rank_score: 67.032

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 보강하는 함성
- transition skill: 보강하는 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 보강하는 함성
- transition skill: 보강하는 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 독 포자

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 보강하는 함성
- transition skill: 보강하는 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 독 포자
- 마름쇠

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 보강하는 함성
- transition skill: 보강하는 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 독 포자
- 마름쇠
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 보강하는 함성
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 독 포자
- 마름쇠
- 충전된 징표
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 19. 청산 감전연쇄 화살 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 청산 감전연쇄 화살
- final_rank_score: 65.682

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 청산 감전연쇄 화살
- transition skill: 청산 감전연쇄 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 전압
- 폭풍연쇄

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 청산 감전연쇄 화살
- transition skill: 청산 감전연쇄 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 청산 감전연쇄 화살
- transition skill: 청산 감전연쇄 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 청산 감전연쇄 화살
- transition skill: 청산 감전연쇄 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 청산 감전연쇄 화살
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 20. 지옥불 함성 효과 범위 발동 번개 화염 빌드

- 메인 스킬: 지옥불 함성
- final_rank_score: 65.426

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 지옥불 함성
- transition skill: 지옥불 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 지옥불 함성
- transition skill: 지옥불 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 마름쇠

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 지옥불 함성
- transition skill: 지옥불 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 마름쇠
- 독 포자

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 지옥불 함성
- transition skill: 지옥불 함성
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 마름쇠
- 독 포자
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 지옥불 함성
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 몽상가의 종소리
- 마름쇠
- 독 포자
- 충전된 징표
- 정전기 감전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 21. 전기불꽃 투사체 발동 번개 냉기 빌드

- 메인 스킬: 전기불꽃
- final_rank_score: 63.794

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 전기불꽃
- transition skill: 전기불꽃
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 마름쇠
- 세차게 흐르는 전류

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 전기불꽃
- transition skill: 전기불꽃
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 마름쇠
- 세차게 흐르는 전류
- 얼어붙은 악의

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 전기불꽃
- transition skill: 전기불꽃
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 마름쇠
- 세차게 흐르는 전류
- 얼어붙은 악의
- 정전기 감전

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 전기불꽃
- transition skill: 전기불꽃
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 마름쇠
- 세차게 흐르는 전류
- 얼어붙은 악의
- 정전기 감전
- 살아 있는 번개

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 전기불꽃
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 마름쇠
- 세차게 흐르는 전류
- 얼어붙은 악의
- 정전기 감전
- 살아 있는 번개
- 살아 있는 번개 II

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 22. 연발 사격 가능 번개 화살 투사체 연쇄 효과 범위 소환수 빌드

- 메인 스킬: 연발 사격 가능 번개 화살
- final_rank_score: 63.625

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 연발 사격 가능 번개 화살
- transition skill: 연발 사격 가능 번개 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 전압
- 폭풍연쇄

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 연발 사격 가능 번개 화살
- transition skill: 연발 사격 가능 번개 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 연발 사격 가능 번개 화살
- transition skill: 연발 사격 가능 번개 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 연발 사격 가능 번개 화살
- transition skill: 연발 사격 가능 번개 화살
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 연발 사격 가능 번개 화살
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 23. 기폭 장치 원소 약화 투사체 번개 연쇄 효과 범위 빌드

- 메인 스킬: 기폭 장치 원소 약화
- final_rank_score: 63.259

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 기폭 장치 원소 약화
- transition skill: 기폭 장치 원소 약화
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 기폭 장치 원소 약화
- transition skill: 기폭 장치 원소 약화
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소

#### Passive priority by stage

- 투사체 피해/투사체 수/탄속 또는 투사체 관련 노터블 우선 (`projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 기폭 장치 원소 약화
- transition skill: 기폭 장치 원소 약화
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 피해 전환 후 최종 피해 타입에 맞는 원소/카오스/물리 노드 우선 (`conversion`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 기폭 장치 원소 약화
- transition skill: 기폭 장치 원소 약화
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 분화구

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 기폭 장치 원소 약화
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 분화구
- 충전된 징표

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 연쇄/투사체 clear speed 관련 노드 우선 (`chain`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 24. 무기 담금질 효과 범위 발동 화염 냉기 빌드

- 메인 스킬: 무기 담금질
- final_rank_score: 63.231

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 무기 담금질
- transition skill: 무기 담금질
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 화산 분출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)
- 번개 피해와 감전/원소 피해 노드 우선 (`lightning`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 무기 담금질
- transition skill: 무기 담금질
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발

#### Passive priority by stage

- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 무기 담금질
- transition skill: 무기 담금질
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 무기 담금질
- transition skill: 무기 담금질
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 무기 담금질
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II
- 하욕시의 뇌전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.

## Rank 25. 폭발 마그마 장벽 효과 범위 발동 화염 근접 빌드

- 메인 스킬: 폭발 마그마 장벽
- final_rank_score: 63.196

### Global Missing Data / TODO

- 정확한 unlock level 데이터가 없어 모든 stage는 bracket 기반 추론입니다.
- 패시브 path planner가 아직 없어 passive priority는 실제 경로가 아니라 방향성입니다.
- gear progression planner가 아직 없어 장비 checkpoint는 최종 추천 장비/affix 기반 후보입니다.

### LV1~12

- 추천 leveling skill: 폭발 마그마 장벽
- transition skill: 폭발 마그마 장벽
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: final build main_skill이 skills.json에 존재하므로 보수적으로 leveling skill 후보로 사용합니다.

#### Support gems by stage

- 분화구
- 화산 분출

#### Passive priority by stage

- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 화염 피해와 점화/원소 피해 노드 우선 (`fire`)
- 냉기 피해와 냉각/동결 안정성 노드 우선 (`cold`)
- 번개 피해와 감전/원소 피해 노드 우선 (`lightning`)

#### Gear checkpoint

- 희귀/유니크 의존 없이 스킬 사용 가능 여부와 저항/생존 옵션을 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 campaign gear/drop/vendor 데이터가 없어 일반 checkpoint만 제공합니다.

### LV12~28

- 추천 leveling skill: 폭발 마그마 장벽
- transition skill: 폭발 마그마 장벽
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 전환 레벨 데이터가 없어 stage bracket 기준으로만 추론했습니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발

#### Passive priority by stage

- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)
- 마나/자원 sustain 노드 우선 (`mana`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit`)

#### Gear checkpoint

- 최종 빌드 핵심 태그와 맞는 무기/보조젬 링크를 우선 확인합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 유니크 착용 레벨과 실제 획득 경로 데이터가 없어 후보만 표시합니다.

### LV28~45

- 추천 leveling skill: 폭발 마그마 장벽
- transition skill: 폭발 마그마 장벽
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 gem unlock과 campaign reward 데이터가 없어 메커닉 기반으로 추론했습니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질

#### Passive priority by stage

- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 생명력 기반 방어 노드 우선 (`life`)

#### Gear checkpoint

- trigger/crit/projectile/conversion 같은 핵심 메커닉을 장비와 보조젬으로 부분 구성합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- 정확한 affix tier/unlock/crafting 데이터가 없어 final recommendation을 단계적으로 노출합니다.

### LV45~65

- 추천 leveling skill: 폭발 마그마 장벽
- transition skill: 폭발 마그마 장벽
- final build online: TODO: 최종 online 전 준비 단계
- 추론 근거: 정확한 장비 착용 레벨 데이터가 없어 final recommendations를 checkpoint로만 사용합니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 발동 조건 안정화, 쿨다운/자원/시전 빈도 관련 노드 우선 (`trigger`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크와 핵심 rare affix를 맞추기 시작하는 pre-endgame 단계입니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- early/mid/late gear progression planner가 없어 세부 교체 순서는 TODO입니다.

### LV65+

- 추천 leveling skill: 폭발 마그마 장벽
- transition skill: 최종 빌드 online
- final build online: LV65+ 후보
- 추론 근거: 최종 빌드 online 시점은 정확한 unlock/gear 데이터가 없어 LV65+로 보수 표시했습니다.

#### Support gems by stage

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II
- 하욕시의 뇌전

#### Passive priority by stage

- 투사체 왕복/반환 시너지와 적중 수 증가 노드 우선 (`returning_projectile`)
- 추가 투사체와 투사체 스케일링 노드 우선 (`extra_projectile`)
- 효과 범위와 범위 중첩 효율 노드 우선 (`overlap`)
- 치명타 확률과 치명타 피해 배율 노드 우선 (`crit_scaling`)
- 추가 피해 획득과 원소/카오스 피해 스케일링 노드 우선 (`gain_as_extra`)

#### Gear checkpoint

- 최종 추천 유니크/희귀 affix 후보를 모두 검토하고 final build online 상태로 표시합니다.

#### Missing Data / TODO

- 정확한 gem unlock level, quest reward, vendor availability 데이터가 없어 bracket 기반 보수 추정입니다.
- 정확한 passive progression/path distance 데이터가 없어 passive priority는 core_mechanics 기반 추론입니다.
- BIS 확정, crafting priority, trade availability 데이터는 아직 없습니다.
