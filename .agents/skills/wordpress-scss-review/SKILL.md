---
name: wordpress-scss-review
description: Review SCSS/CSS in a WordPress theme or plugin for architecture, Sass usage, specificity, tokens, responsive behavior, accessibility, reusable components, and maintainability. Use for styling audits or SCSS refactors, not general PHP/theme review.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress SCSS Review

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inventory styling source with `scripts/inventory.py <root> --ext .scss --ext .css`.
2. Inspect entrypoints/partials structure before individual components.
3. Load `references/architecture-and-sass.md` for organization/reuse.
4. Load `references/responsive-accessibility.md` when layout/interactions are relevant.
5. Use `references/exhaustive-review.md` only for a full styling audit.

## Output
Prioritize maintainability and actual cascade problems over stylistic preferences. Show revised SCSS only for high-impact fixes.
