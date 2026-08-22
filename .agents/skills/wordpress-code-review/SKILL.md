---
name: wordpress-code-review
description: Audit a WordPress theme or mixed custom WordPress codebase for production readiness, security, architecture, maintainability, accessibility, and framework conventions. Use for broad project/theme reviews; prefer narrower PHP, plugin, SCSS, or UX skills when the request is domain-specific.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress Code Review

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inventory the narrowest requested project/theme root with `scripts/inventory.py`.
2. Inspect entry points/config first, then source in logical batches.
3. Load `references/theme-architecture.md` for theme/template ownership and organization questions.
4. Load `references/security-accessibility.md` only when PHP/output/input or rendered interaction is in scope.
5. For deep audits, use `references/exhaustive-review.md` as a coverage checklist.
6. Route domain-specific findings to the narrower skill rather than duplicating its full checklist.

## Output
Give strengths, critical issues, important improvements, optional polish, and the single highest-value next action. Do not invent issues merely to fill categories.
