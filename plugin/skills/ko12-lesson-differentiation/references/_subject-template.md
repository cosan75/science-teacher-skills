<!--
SPDX-FileCopyrightText: 2026 science-teacher-skills contributors
SPDX-License-Identifier: Apache-2.0

새 과목 차별화 레퍼런스의 뼈대. 스킬이 로드하지 않는다(레지스트리에 없음).
`python tools/new_subject.py <slug> <과목명>`이 복사해 references/<slug>.md를 만든다.
기준 구현은 이 폴더의 science.md — R1–R8 절 구조를 그대로 둔다.
-->

# {{과목명}} — 차별화 pedagogy

`ko12-lesson-differentiation`에서 과목이 **{{과목명}}**일 때 로드된다 (SKILL.md 과목 레지스트리).

> ✍ 작성 안내 (완성하면 인용 블록을 모두 지운다)
> - **원본 수업 확인 / 성취기준 확인** 절은 science.md에서 과목명만 바꿔 옮긴다.
> - R1(산출 구조)·R6(보이지 않는 조정)·R8(범위와 기본값)은 과목 중립이다 — 그대로 옮긴다.
> - 과목마다 다시 쓰는 것은 **R3(끌어올리기 진행)·R4(기초 수준 스캐폴드)·R5(필수 장치)·
>   R7(심화 확장)** 넷이다. 과학의 "관찰 → 표현 → 설명"에 해당하는 이 과목의 진행축을 먼저
>   정한다. 예: 수학 — 구체물 → 그림 → 식 / 국어 — 확인 → 추론 → 비판·감상 /
>   사회 — 자료 읽기 → 해석 → 판단·참여.
> - 불변: **세 수준은 같은 핵심 과제**를 다루고 지원만 달라진다. 기초 수준이라고 과목의
>   핵심 사고(과학의 탐구, 수학의 추론, 국어의 해석)를 빼지 않는다.

## 원본 수업 확인

{{science.md의 시나리오 A / B / B2 / C를 과목명만 바꿔 옮긴다}}

---

## 성취기준 확인

SKILL.md의 **Step 2 — 성취기준으로 확인**을 따른다.

---

## 차별화 규칙

### R1 — 산출 구조

{{science.md R1 그대로}}

### R2 — 3범주 범위 보존

{{세 수준 모두 지식·이해 / 과정·기능 / 가치·태도를 같은 성취기준 범위로 — 이 과목의 예시}}

### R3 — {{진행축}}으로 끌어올리기

{{…}}

### R4 — 기초 수준 스캐폴드

{{…}}

#### 스캐폴드 밀도 상한

{{…}}

### R5 — 필수 교수학습 장치

{{…}}

### R6 — 보이지 않는 조정

{{science.md R6 그대로}}

### R7 — 수준 내 점진적 스캐폴딩

{{…}}

### R8 — 범위와 기본값

{{science.md R8 그대로}}

---

### 문서 내용 — 통합 수업안 (`id: teacher_plan`) — 최대 5쪽

{{science.md 템플릿 구조 그대로, 과목 어휘만 교체}}

### 문서 내용 — 학습지 (`id: worksheet_group_a` / `worksheet_group_b` / `worksheet_group_c`)

{{…}}

---

## differentiation.json 작성 — {{과목명}} 매핑

- `shared.subject`: `"{{과목명}}"`
- `shared.grade`: 영문 학년을 앞에 (`"Grade 4 · 초등학교 4학년"`)
- `shared.standard_code` / `shared.standard_text`: 코드와 원문
- `shared.anchor_task`, `shared.t1`..`tN`, `shared.sentence_frames`: science.md와 같은 형태
