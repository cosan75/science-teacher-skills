# SPDX-FileCopyrightText: 2026 science-teacher-skills contributors
# SPDX-License-Identifier: Apache-2.0
"""새 과목 레퍼런스 뼈대를 두 스킬에 만든다 (표준 라이브러리만).

  python tools/new_subject.py math 수학

- 레지스트리(SKILL.md 표)에 이미 있는 과목이어야 한다 — slug는 표의 `references/<slug>.md`.
- 두 스킬의 `_subject-template.md`를 복사해 `{{과목명}}`만 채운다. 나머지 `{{…}}`와 `✍` 안내는
  작성자가 채우고 지운다.
- 레지스트리 상태는 바꾸지 않는다. 내용을 다 쓰고 `tests/check_subjects.py`가 통과하는 것을
  확인한 뒤, 두 SKILL.md의 상태를 함께 `ready`로 바꾼다.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = [ROOT / "plugin" / "skills" / s for s in ("ko12-lesson-planning", "ko12-lesson-differentiation")]


def main(argv) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    slug, name = argv[1], argv[2]
    filename = f"{slug}.md"
    registry = (SKILLS[0] / "SKILL.md").read_text(encoding="utf-8")
    if f"`references/{filename}`" not in registry:
        print(f"레지스트리에 references/{filename}이 없습니다 — 두 SKILL.md의 표에 먼저 행을 추가하세요.")
        return 1
    for skill in SKILLS:
        target = skill / "references" / filename
        if target.exists():
            print(f"이미 있음, 건너뜀: {target.relative_to(ROOT)}")
            continue
        template = (skill / "references" / "_subject-template.md").read_text(encoding="utf-8")
        target.write_text(template.replace("{{과목명}}", name), encoding="utf-8", newline="\n")
        print(f"생성: {target.relative_to(ROOT)}")
    print("\n다음 단계:\n"
          "  1. 두 파일의 {{…}} 자리와 ✍ 안내를 채우고 지운다 (기준 구현: science.md)\n"
          "  2. pilot/<과목-학년>/lesson.json 파일럿 1건 + CI 렌더 단계에 추가\n"
          "  3. python tests/check_subjects.py 통과 확인 후 두 SKILL.md 상태를 ready로")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
