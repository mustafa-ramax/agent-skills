from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "tel:")


def check_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    root = skill_dir.resolve()
    instruction_file = skill_dir / "SKILL.md"
    if not instruction_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    for source in skill_dir.rglob("*.md"):
        content = source.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(content):
            target = target.strip("<>")
            if not target or target.startswith(("#", *EXTERNAL_SCHEMES)):
                continue

            local_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not local_target:
                continue

            resolved = (source.parent / local_target).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{source}: link escapes the skill directory: {target}")
            elif not resolved.exists():
                errors.append(f"{source}: broken local link: {target}")

    return errors


def main() -> int:
    skills_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skills")
    if not skills_root.is_dir():
        print(f"Skills directory not found: {skills_root}", file=sys.stderr)
        return 2

    skill_dirs = sorted(path.parent for path in skills_root.rglob("SKILL.md"))
    if not skill_dirs:
        print(f"No SKILL.md files found under {skills_root}", file=sys.stderr)
        return 2

    errors = [error for skill_dir in skill_dirs for error in check_skill(skill_dir)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Checked local Markdown links in {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
