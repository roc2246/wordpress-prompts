---
name: wordpress-code-review
description: Review a WordPress theme or mixed custom WordPress codebase for production readiness, security, architecture, maintainability, and accessibility. Use for broad reviews; prefer narrower PHP, plugin, SCSS, or UX skills for domain-specific requests.
metadata:
  author: riley-childs
  version: "3.0"
---

# WordPress Code Review

Use `_base/common-workflow.md` and `_base/common-output.md`.

1. Run `scripts/inventory.py` on the requested custom-code root; inventory paths only.
2. Inspect entry points and architecture first, then only relevant files in small batches.
3. Load `references/theme-architecture.md` only for theme/template structure.
4. Load `references/security-accessibility.md` only for trust boundaries or rendered interaction.
5. Use `references/exhaustive-review.md` only when the user explicitly wants a full audit.
6. Delegate domain-specific depth to the narrower skill instead of duplicating its checks.
