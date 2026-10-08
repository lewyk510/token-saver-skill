#!/usr/bin/env python3
"""Self-test for the token-saver skill repo.

Docs-only project, but CI must mean something: this validates every markdown
file is well-formed (balanced code fences), that SKILL.md carries a valid
frontmatter with name+description, and that every relative link in README.md
points at a real file. Exit non-zero on any failure.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []


def md_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_fences():
    for p in md_files():
        text = p.read_text(encoding="utf-8")
        if text.count("```") % 2 != 0:
            errors.append(f"{p.relative_to(ROOT)}: unbalanced code fences")


def check_skill_frontmatter():
    skill = ROOT / "SKILL.md"
    if not skill.exists():
        errors.append("SKILL.md missing")
        return
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append("SKILL.md: no frontmatter")
        return
    fm = text.split("---", 2)[1]
    for key in ("name:", "description:"):
        if key not in fm:
            errors.append(f"SKILL.md: frontmatter missing {key}")


def check_readme_links():
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    for target in set(re.findall(r"\]\(([^)]+)\)", readme.read_text(encoding="utf-8"))):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (ROOT / target).exists():
            errors.append(f"README.md: broken link -> {target}")


check_fences()
check_skill_frontmatter()
check_readme_links()

if errors:
    print("selftest FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(f"selftest OK — {len(md_files())} markdown files, frontmatter + links valid")
