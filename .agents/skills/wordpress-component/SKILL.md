---
name: wordpress-component
description: Create or refactor a reusable WordPress theme component/template part with appropriate PHP markup and directly related SCSS/JavaScript. Use when the user asks to build, extract, or standardize a reusable theme component.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress Component

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inspect the nearest existing component/template patterns; use `scripts/inventory.py` only when discovery spans multiple files.
2. Load `references/component-design.md` for structure and API decisions.
3. Load `references/markup-security.md` when dynamic data or interactive markup is involved.
4. Match existing naming/build conventions; do not introduce a parallel component system without need.
5. Implement only the PHP/SCSS/JS required by the component.

## Output
For planning, identify file locations, component inputs, markup/styling/behavior, and usage. For implementation, edit the project directly and validate relevant build/lint checks.
