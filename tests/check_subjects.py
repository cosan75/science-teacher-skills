# SPDX-FileCopyrightText: 2026 science-teacher-skills contributors
# SPDX-License-Identifier: Apache-2.0
"""과목 레지스트리 정합 검사 (표준 라이브러리만).

두 스킬의 SKILL.md가 같은 과목 레지스트리를 갖고, 레지스트리가 references/ 폴더의 실제
파일과 맞는지 본다:

  R1  두 SKILL.md의 레지스트리 표가 한 글자도 다르지 않다
  R2  ready 과목은 두 스킬 모두에 레퍼런스 파일이 있다
  R3  ready 과목 파일에 템플릿 자리표시(`{{`, `✍`)가 남아 있지 않다
  R4  ready 과목 파일이 필수 절 제목을 갖는다
  R5  references/에 레지스트리에도 공용 파일 목록에도 없는 .md가 없다 (고아 파일)
  R6  공용 파일(템플릿·학습맵 시퀀스·역설계)이 있다

planned 과목에 초안 파일이 있는 것은 허용한다(작성 중) — 알림만 출력한다.
사용법: python tests/check_subjects.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugin" / "skills"
PLANNING = SKILLS / "ko12-lesson-planning"
DIFF = SKILLS / "ko12-lesson-differentiation"

COMMON = {
    PLANNING: {"_subject-template.md", "curriculum-kr-mcp.md", "from-assessment.md"},
    DIFF: {"_subject-template.md", "curriculum-kr-mcp.md"},
}
REQUIRED_HEADINGS = {
    PLANNING: ["## 확인(Clarify)", "## 수업 설계", "## lesson.json 작성"],
    DIFF: ["## 원본 수업 확인", "## 차별화 규칙", "## differentiation.json 작성"],
}
ROW = re.compile(r"^\s*\|\s*([^|]+?)\s*\|[^|]*\|\s*`references/([^`]+\.md)`\s*\|\s*(ready|planned)\s*\|\s*$")


def registry(skill: Path):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    start = text.find("| 과목 | 신호")
    if start < 0:
        return "", []
    block = text[start:text.index("\n\n", start)]
    rows = [m.groups() for line in block.splitlines() if (m := ROW.match(line))]
    return block, rows


def main() -> int:
    errors, notes = [], []

    plan_block, rows = registry(PLANNING)
    diff_block, _ = registry(DIFF)
    if plan_block.strip() != diff_block.strip():
        errors.append("R1 두 SKILL.md의 과목 레지스트리가 다르다 — 한쪽만 고쳤는지 확인")
    if not rows:
        errors.append("R1 레지스트리 행을 하나도 읽지 못했다 — 표 형식 확인")

    for skill in (PLANNING, DIFF):
        ref = skill / "references"
        for name in COMMON[skill]:
            if not (ref / name).is_file():
                errors.append(f"R6 {skill.name}: 공용 파일 없음 — {name}")

        listed = set()
        for subject, filename, status in rows:
            listed.add(filename)
            path = ref / filename
            if status == "ready":
                if not path.is_file():
                    errors.append(f"R2 {skill.name}: ready 과목 '{subject}'의 {filename} 없음")
                    continue
                body = path.read_text(encoding="utf-8")
                if "{{" in body or "✍" in body:
                    errors.append(f"R3 {skill.name}/{filename}: 템플릿 자리표시가 남아 있음")
                for h in REQUIRED_HEADINGS[skill]:
                    if not re.search(rf"^{re.escape(h)}", body, re.M):
                        errors.append(f"R4 {skill.name}/{filename}: 필수 절 '{h}' 없음")
            elif path.is_file():
                notes.append(f"{skill.name}/{filename}: planned 과목 '{subject}' 초안 작성 중")

        for md in ref.glob("*.md"):
            if md.name not in listed and md.name not in COMMON[skill]:
                errors.append(f"R5 {skill.name}/{md.name}: 레지스트리에 없는 과목 파일")

    ready = [s for s, _, st in rows if st == "ready"]
    print(f"과목 레지스트리: {len(rows)}개 (ready {len(ready)}: {', '.join(ready)})")
    for n in notes:
        print(f"  · {n}")
    for e in errors:
        print(f"  ✗ {e}")
    print("PASS" if not errors else f"FAIL ({len(errors)})")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
