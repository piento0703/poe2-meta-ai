# PoE2 Meta AI 상호작용 분석 리포트

이 문서는 스킬·보조젬·유니크·일반/레어 아이템 옵션의 메커니즘 상호작용을 기반으로 자동 생성된 리포트다.

## 분석 기준

- 기존 빌드 점수
- 일반/레어 아이템 옵션 semantic score
- Broken Combo 감지
- 메커니즘 밀도
- 상호작용 점수 기준 정렬

---

## 1. 불씨 일제 사격 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 불씨 일제 사격 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 795.0 |
| 상호작용 점수 | 1132.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- fork
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 마름쇠
- 화산 분출
- 분화구
- 얼어붙은 악의
- 충전된 징표
- 정전기 감전

### 추천 유니크

- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 22.0 / 매칭: 화염, 투사체
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 화염, 발동
- 질식의 진노 / 역할: engine / 점수: 19.0 / 매칭: 화염, 투사체
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 2. 원소 표현 투사체 발동 번개 냉기 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 원소 표현 |
| 아키타입 | 투사체 발동 번개 냉기 |
| 기존 빌드 점수 | 723.0 |
| 상호작용 점수 | 1057.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 세차게 흐르는 전류
- 화산 분출
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 얼어붙은 악의

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 27.0 / 매칭: 연쇄, 번개, 투사체
- 이중 시야 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 발동
- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 뱀구덩이 / 역할: engine / 점수: 20.0 / 매칭: 연쇄, 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 3. 종말 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 종말 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 680.0 |
| 상호작용 점수 | 1017.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- fork
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 충전된 징표

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 번개
- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 대지속박 / 역할: engine / 점수: 17.0 / 매칭: 번개, 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 4. 원소 폭풍 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 원소 폭풍 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 679.0 |
| 상호작용 점수 | 1016.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- fork
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 분화구
- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 충전된 징표

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 번개
- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 대지속박 / 역할: engine / 점수: 17.0 / 매칭: 번개, 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 5. 연발 사격 가능 얼음촉 화살 투사체 발동 번개 냉기 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 연발 사격 가능 얼음촉 화살 |
| 아키타입 | 투사체 발동 번개 냉기 |
| 기존 빌드 점수 | 673.0 |
| 상호작용 점수 | 1007.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 마름쇠
- 얼어붙은 악의
- 화산 분출
- 독 포자
- 분화구
- 몽상가의 종소리

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 냉기, 발동
- 세케마의 결의 / 역할: engine / 점수: 17.0 / 매칭: 냉기, 투사체
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 어둠살대 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 6. 마름쇠의 발자취 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 마름쇠의 발자취 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 660.0 |
| 상호작용 점수 | 994.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 마름쇠
- 독 포자
- 화산 분출
- 분화구
- 몽상가의 종소리
- 얼어붙은 악의

### 추천 유니크

- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 이중 시야 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 어둠살대 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 세케마의 결의 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 7. 부패 효과 범위 발동 번개 화염 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 부패 |
| 아키타입 | 효과 범위 발동 번개 화염 |
| 기존 빌드 점수 | 677.0 |
| 상호작용 점수 | 938.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- lightning
- mana
- overlap
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 분화구
- 독 포자
- 충전된 징표
- 하욕시의 뇌전
- 정전기 감전
- 몽상가의 종소리

### 추천 유니크

- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 화염, 발동
- 어둠살대 / 역할: engine / 점수: 20.0 / 매칭: 카오스, 지속시간, 발동
- 분노의 첨탑 / 역할: engine / 점수: 17.0 / 매칭: 카오스, 발동
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 8. 원소 쇄도 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 원소 쇄도 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 587.0 |
| 상호작용 점수 | 921.0 |
| 상호작용 등급 | S급 / 메타 파괴 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 번개
- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 대지속박 / 역할: engine / 점수: 17.0 / 매칭: 번개, 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 메타 파괴 후보로 우선 검증 가치가 높음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 9. 선대의 함성 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 선대의 함성 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 533.0 |
| 상호작용 점수 | 867.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 화산 분출
- 마름쇠
- 분화구
- 몽상가의 종소리
- 독 포자
- 얼어붙은 악의

### 추천 유니크

- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 22.0 / 매칭: 화염, 투사체
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 화염, 발동
- 질식의 진노 / 역할: engine / 점수: 19.0 / 매칭: 화염, 투사체
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 10. 피사냥개의 징표 번개 효과 범위 발동 화염 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 피사냥개의 징표 |
| 아키타입 | 번개 효과 범위 발동 화염 |
| 기존 빌드 점수 | 576.0 |
| 상호작용 점수 | 840.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- lightning
- mana
- overlap
- projectile
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표
- 정전기 감전

### 추천 유니크

- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 이중 시야 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 어둠살대 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 분노의 첨탑 / 역할: engine / 점수: 13.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 11. 전용 탈출 사격 투사체 발동 번개 냉기 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 전용 탈출 사격 |
| 아키타입 | 투사체 발동 번개 냉기 |
| 기존 빌드 점수 | 499.0 |
| 상호작용 점수 | 833.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 얼어붙은 악의
- 화산 분출
- 마름쇠
- 세차게 흐르는 전류
- 하욕시의 뇌전
- 엄습하는 오한

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 냉기, 발동
- 세케마의 결의 / 역할: engine / 점수: 17.0 / 매칭: 냉기, 투사체
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 질식의 진노 / 역할: engine / 점수: 14.0 / 매칭: 냉기, 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 12. 공허 환상 번개 효과 범위 발동 화염 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 공허 환상 |
| 아키타입 | 번개 효과 범위 발동 화염 |
| 기존 빌드 점수 | 535.0 |
| 상호작용 점수 | 799.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- lightning
- mana
- overlap
- projectile
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 독 포자
- 분화구
- 몽상가의 종소리
- 마름쇠
- 충전된 징표
- 정전기 감전

### 추천 유니크

- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 이중 시야 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 어둠살대 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 분노의 첨탑 / 역할: engine / 점수: 13.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 13. 보강하는 함성 번개 효과 범위 발동 화염 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 보강하는 함성 |
| 아키타입 | 번개 효과 범위 발동 화염 |
| 기존 빌드 점수 | 524.0 |
| 상호작용 점수 | 788.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- lightning
- mana
- overlap
- projectile
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 분화구
- 몽상가의 종소리
- 독 포자
- 마름쇠
- 충전된 징표
- 정전기 감전

### 추천 유니크

- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 이중 시야 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 어둠살대 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 분노의 첨탑 / 역할: engine / 점수: 13.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 14. 전기불꽃 투사체 발동 번개 냉기 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 전기불꽃 |
| 아키타입 | 투사체 발동 번개 냉기 |
| 기존 빌드 점수 | 464.0 |
| 상호작용 점수 | 767.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 마름쇠
- 세차게 흐르는 전류
- 얼어붙은 악의
- 정전기 감전
- 살아 있는 번개
- 살아 있는 번개 II

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 21.0 / 매칭: 번개, 투사체
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 냉기, 발동
- 대지속박 / 역할: engine / 점수: 17.0 / 매칭: 번개, 발동
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 15. 지옥불 함성 효과 범위 발동 번개 화염 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 지옥불 함성 |
| 아키타입 | 효과 범위 발동 번개 화염 |
| 기존 빌드 점수 | 504.0 |
| 상호작용 점수 | 765.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- mana
- overlap
- projectile
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 분화구
- 몽상가의 종소리
- 마름쇠
- 독 포자
- 충전된 징표
- 정전기 감전

### 추천 유니크

- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 화염, 발동
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 어둠살대 / 역할: engine / 점수: 16.0 / 매칭: 지속시간, 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 16. 무기 담금질 효과 범위 발동 화염 냉기 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 무기 담금질 |
| 아키타입 | 효과 범위 발동 화염 냉기 |
| 기존 빌드 점수 | 500.0 |
| 상호작용 점수 | 755.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- overlap
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II
- 하욕시의 뇌전

### 추천 유니크

- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 화염, 발동
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 분노의 첨탑 / 역할: engine / 점수: 13.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 17. 폭발 마그마 장벽 효과 범위 발동 화염 근접 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 폭발 마그마 장벽 |
| 아키타입 | 효과 범위 발동 화염 근접 |
| 기존 빌드 점수 | 499.0 |
| 상호작용 점수 | 754.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- overlap
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 분화구
- 화산 분출
- 방어구 폭발
- 불난 집 부채질
- 불난 집 부채질 II
- 하욕시의 뇌전

### 추천 유니크

- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 이중 시야 / 역할: engine / 점수: 20.0 / 매칭: 화염, 발동
- 붕괴하는 지평선 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 폭풍의 합창 / 역할: engine / 점수: 16.0 / 매칭: 발동
- 분노의 첨탑 / 역할: engine / 점수: 13.0 / 매칭: 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 18. 원소 상태 이상 시 시전 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 원소 상태 이상 시 시전 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 369.0 |
| 상호작용 점수 | 703.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 번개
- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 대지속박 / 역할: engine / 점수: 17.0 / 매칭: 번개, 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 19. 조건부 원소 기원 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 조건부 원소 기원 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 369.0 |
| 상호작용 점수 | 703.0 |
| 상호작용 등급 | A급 / 강력한 OP 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 방어구 폭발
- 분화구
- 불난 집 부채질

### 추천 유니크

- 이중 시야 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 발동
- 세케마의 결의 / 역할: engine / 점수: 24.0 / 매칭: 냉기, 화염, 번개
- 황혼의 감시 / 역할: engine / 점수: 22.0 / 매칭: 화염, 발동
- 폭풍의 합창 / 역할: engine / 점수: 20.0 / 매칭: 번개, 발동
- 대지속박 / 역할: engine / 점수: 17.0 / 매칭: 번개, 발동

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 강력한 OP 후보로 실전 검증 가치가 있음
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 20. 구형 번개 투사체 번개 연쇄 효과 범위 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 구형 번개 |
| 아키타입 | 투사체 번개 연쇄 효과 범위 |
| 기존 빌드 점수 | 349.0 |
| 상호작용 점수 | 683.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 27.0 / 매칭: 연쇄, 번개, 투사체
- 뱀구덩이 / 역할: support / 점수: 20.0 / 매칭: 연쇄, 투사체
- Drillneck / 역할: support / 점수: 13.0 / 매칭: 투사체
- Tyranny's Grip / 역할: support / 점수: 10.0 / 매칭: 투사체
- Chainsting / 역할: support / 점수: 10.0 / 매칭: 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 21. 격파 장법 효과 범위 근접 발동 냉기 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 격파 장법 |
| 아키타입 | 효과 범위 근접 발동 냉기 |
| 기존 빌드 점수 | 420.0 |
| 상호작용 점수 | 657.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

- ailment_scaling
- cold
- crit_scaling
- extra_projectile
- fire
- gain_as_extra
- overlap
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 화산 분출
- 분화구
- 가시 격발
- 가시나무 강타
- 몽상가의 종소리
- 얼어붙은 악의

### 추천 유니크

- 없음

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 22. 메타 낙뢰 번개 효과 범위 발동 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 메타 낙뢰 |
| 아키타입 | 번개 효과 범위 발동 |
| 기존 빌드 점수 | 417.0 |
| 상호작용 점수 | 654.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

- ailment_scaling
- charge_scaling
- crit_scaling
- extra_projectile
- gain_as_extra
- lightning
- overlap
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 전자기력
- 정전기 감전
- 촉진시키는 원소
- 충전된 징표

### 추천 유니크

- 없음

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 23. 청산 감전연쇄 화살 투사체 번개 연쇄 효과 범위 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 청산 감전연쇄 화살 |
| 아키타입 | 투사체 번개 연쇄 효과 범위 |
| 기존 빌드 점수 | 310.0 |
| 상호작용 점수 | 644.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 27.0 / 매칭: 연쇄, 번개, 투사체
- 뱀구덩이 / 역할: support / 점수: 20.0 / 매칭: 연쇄, 투사체
- Drillneck / 역할: support / 점수: 13.0 / 매칭: 투사체
- Tyranny's Grip / 역할: support / 점수: 10.0 / 매칭: 투사체
- Chainsting / 역할: support / 점수: 10.0 / 매칭: 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 24. 화산 균열 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 화산 균열 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 309.0 |
| 상호작용 점수 | 643.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출
- 삭망

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 12.0 / 매칭: 지속시간, 화염
- 황혼의 감시 / 역할: engine / 점수: 9.0 / 매칭: 화염
- Sacred Flame / 역할: scaling / 점수: 9.0 / 매칭: 화염
- Guiding Palm of the Heart / 역할: scaling / 점수: 9.0 / 매칭: 화염
- Heatshiver / 역할: scaling / 점수: 9.0 / 매칭: 화염

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 25. 대장간 망치 투사체 발동 번개 연쇄 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 대장간 망치 |
| 아키타입 | 투사체 발동 번개 연쇄 |
| 기존 빌드 점수 | 309.0 |
| 상호작용 점수 | 643.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 분화구
- 요철 지대 I
- 요철 지대 II
- 몽상가의 종소리
- 화산 분출
- 삭망

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 12.0 / 매칭: 지속시간, 화염
- 황혼의 감시 / 역할: engine / 점수: 9.0 / 매칭: 화염
- Sacred Flame / 역할: scaling / 점수: 9.0 / 매칭: 화염
- Guiding Palm of the Heart / 역할: scaling / 점수: 9.0 / 매칭: 화염
- Heatshiver / 역할: scaling / 점수: 9.0 / 매칭: 화염

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 26. 폭발 바람의 무희 효과 범위 발동 근접 번개 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 폭발 바람의 무희 |
| 아키타입 | 효과 범위 발동 근접 번개 |
| 기존 빌드 점수 | 398.0 |
| 상호작용 점수 | 632.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

- ailment_scaling
- crit_scaling
- extra_projectile
- fire
- gain_as_extra
- overlap
- returning_projectile
- shotgun
- trigger

### 추천 보조젬

- 분화구
- 화산 분출
- 가시 격발
- 가시나무 강타
- 몽상가의 종소리
- 치명적인 투지

### 추천 유니크

- 없음

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 치명타 기반 발동 엔진 후보

---

## 27. 연발 사격 가능 번개 화살 투사체 연쇄 효과 범위 소환수 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 연발 사격 가능 번개 화살 |
| 아키타입 | 투사체 연쇄 효과 범위 소환수 |
| 기존 빌드 점수 | 282.0 |
| 상호작용 점수 | 616.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- life
- lightning
- mana
- meta_energy
- minion
- minion_scaling
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 전압
- 폭풍연쇄
- 세차게 흐르는 전류
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 27.0 / 매칭: 연쇄, 번개, 투사체
- 뱀구덩이 / 역할: enable / 점수: 20.0 / 매칭: 연쇄, 투사체
- Drillneck / 역할: enable / 점수: 13.0 / 매칭: 투사체
- Tyranny's Grip / 역할: enable / 점수: 10.0 / 매칭: 투사체
- Chainsting / 역할: enable / 점수: 10.0 / 매칭: 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 28. 기폭 장치 원소 약화 투사체 번개 연쇄 효과 범위 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 기폭 장치 원소 약화 |
| 아키타입 | 투사체 번개 연쇄 효과 범위 |
| 기존 빌드 점수 | 247.0 |
| 상호작용 점수 | 584.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- fork
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 하욕시의 뇌전
- 원소 방출
- 촉진시키는 원소
- 정전기 감전
- 분화구
- 충전된 징표

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 21.0 / 매칭: 냉기, 화염, 번개
- Painter's Servant / 역할: scaling / 점수: 17.0 / 매칭: 냉기, 화염, 번개
- Heatshiver / 역할: scaling / 점수: 13.0 / 매칭: 냉기, 화염
- 질식의 진노 / 역할: scaling / 점수: 13.0 / 매칭: 냉기, 화염
- Queen of the Forest / 역할: support / 점수: 12.0 / 매칭: 냉기, 화염, 번개

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 29. 돌발 투사체 번개 연쇄 효과 범위 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 돌발 |
| 아키타입 | 투사체 번개 연쇄 효과 범위 |
| 기존 빌드 점수 | 242.0 |
| 상호작용 점수 | 576.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- overlap
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 원소 방출
- 하욕시의 뇌전
- 촉진시키는 원소
- 전자기력
- 방어구 폭발
- 불타는 죽음

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 21.0 / 매칭: 냉기, 화염, 번개
- Painter's Servant / 역할: scaling / 점수: 17.0 / 매칭: 냉기, 화염, 번개
- Heatshiver / 역할: scaling / 점수: 13.0 / 매칭: 냉기, 화염
- 질식의 진노 / 역할: scaling / 점수: 13.0 / 매칭: 냉기, 화염
- Queen of the Forest / 역할: support / 점수: 12.0 / 매칭: 냉기, 화염, 번개

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 투사체 연쇄 중첩 / 점수: 28 / 이유: 연쇄와 범위 중첩이 동시에 작동하면 화면 정리와 보스딜이 동시에 증가할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---

## 30. 지속시간 연쇄 번개 투사체 연쇄 소환수 번개 빌드

### 요약

| 항목 | 내용 |
|---|---|
| 메인 스킬 | 지속시간 연쇄 번개 |
| 아키타입 | 투사체 연쇄 소환수 번개 |
| 기존 빌드 점수 | 266.0 |
| 상호작용 점수 | 572.0 |
| 상호작용 등급 | B급 / 실전 빌드 후보 |

### 감지된 핵심 메커니즘

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
- gain_as_extra
- life
- lightning
- mana
- meta_energy
- minion
- minion_scaling
- pierce
- projectile
- returning_projectile
- shotgun
- spirit
- trigger

### 추천 보조젬

- 세차게 흐르는 전류
- 폭풍연쇄
- 전압
- 도미누스의 장악
- 연쇄 I
- 연쇄 II

### 추천 유니크

- 세케마의 결의 / 역할: engine / 점수: 27.0 / 매칭: 연쇄, 번개, 투사체
- 뱀구덩이 / 역할: support / 점수: 20.0 / 매칭: 연쇄, 투사체
- Drillneck / 역할: support / 점수: 13.0 / 매칭: 투사체
- Tyranny's Grip / 역할: support / 점수: 10.0 / 매칭: 투사체
- Chainsting / 역할: support / 점수: 10.0 / 매칭: 투사체

### 추천 일반/레어 아이템 옵션 후보

- 투사체 리턴 샷건 무기 / 슬롯: weapon / 점수: 99.09 / 등급: S급 / 빌드 파괴 가능성 / 메커니즘: extra_projectile, gain_as_extra, returning_projectile, shotgun
- 치명타 발동 목걸이 / 슬롯: amulet / 점수: 34.56 / 등급: B급 / 유효한 시너지 후보 / 메커니즘: crit_scaling, gain_as_extra, trigger

### 감지된 Broken Combo

- 돌아오는 투사체 다중 적중 / 점수: 35 / 이유: 돌아오는 투사체가 같은 대상을 여러 번 때릴 수 있으면 단일딜이 폭증할 수 있음
- 추가 투사체 다중 적중 / 점수: 30 / 이유: 투사체 수 증가가 단순 광역이 아니라 단일 대상 적중 수 증가로 연결될 수 있음
- 추가 피해 획득 + 전환 중첩 / 점수: 24 / 이유: 전환과 추가 피해 획득이 함께 있으면 여러 피해 타입 스케일링을 동시에 받을 수 있음
- 치명타 발동 엔진 / 점수: 22 / 이유: 치명타 확률이 발동 빈도와 피해량을 동시에 밀어올릴 수 있음

### 해석

- 실전 빌드 후보이나 추가 검증 필요
- Broken Combo가 감지되어 단순 태그 매칭보다 높은 우선순위
- 투사체 수 증가와 다중 적중 구조가 결합되어 보스딜 폭증 가능성
- 피해 전환과 추가 피해 획득이 결합되어 복합 스케일링 가능
- 치명타 기반 발동 엔진 후보

---
