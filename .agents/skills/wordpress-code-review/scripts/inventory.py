#!/usr/bin/env python3
"""Inventory handwritten WordPress theme/project files for an Agent Skill audit.

With no --ext flags, defaults to source extensions useful for a mixed theme review.
Use repeated --ext flags to narrow the inventory.
"""
from pathlib import Path
import argparse

EXCLUDED = {
    ".git", "node_modules", "vendor", "dist", "build", "coverage", ".cache",
    "uploads", "upgrade", "languages", "ai1wm-backups", "backups-dup-lite",
}
GENERATED_NAMES = {"style.css.map"}
DEFAULT_EXTENSIONS = {".php", ".js", ".jsx", ".ts", ".tsx", ".scss", ".css"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument(
        "--ext",
        action="append",
        help="Extension such as .php; repeatable. Defaults to common theme source extensions.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Target is not a directory: {root}")

    exts = set(args.ext) if args.ext else DEFAULT_EXTENSIONS
    exts = {ext if ext.startswith(".") else f".{ext}" for ext in exts}

    files = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in exts:
            continue
        if any(part in EXCLUDED for part in path.parts):
            continue
        if (
            path.name in GENERATED_NAMES
            or path.name.endswith(".min.js")
            or path.name.endswith(".min.css")
        ):
            continue
        files.append(path.relative_to(root))

    for path in sorted(files):
        print(path.as_posix())
    print(f"TOTAL={len(files)}")


if __name__ == "__main__":
    main()
