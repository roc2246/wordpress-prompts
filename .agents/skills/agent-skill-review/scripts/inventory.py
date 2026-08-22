#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[2]
skills = sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("_"))
for skill in skills:
    print(skill.name)
    for path in sorted(p for p in skill.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"):
        print(f"  {path.relative_to(skill)}")
print(f"TOTAL_SKILLS={len(skills)}")

def path_ok(path):
    return path.suffix != ".pyc"
