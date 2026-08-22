#!/usr/bin/env python3
"""Inventory handwritten WordPress project files for an Agent Skill audit."""
from pathlib import Path
import argparse

EXCLUDED = {
    ".git", "node_modules", "vendor", "dist", "build", "coverage", ".cache",
    "uploads", "upgrade", "languages"
}
GENERATED_NAMES = {"style.css.map"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--ext", action="append", required=True, help="Extension such as .php; repeatable")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    exts = set(args.ext)
    files = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in exts:
            continue
        if any(part in EXCLUDED for part in path.parts):
            continue
        if path.name in GENERATED_NAMES or path.name.endswith(".min.js") or path.name.endswith(".min.css"):
            continue
        files.append(path.relative_to(root))

    for path in sorted(files):
        print(path.as_posix())
    print(f"TOTAL={len(files)}")


if __name__ == "__main__":
    main()
