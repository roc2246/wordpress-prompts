---
name: wordpress-code-review
description: General code review for WordPress PHP, theme templates, JavaScript, SCSS, plugins, and common integrations. Use as the catch-all when review scope is mixed or unclear, for maintainability/refactoring audits, production-readiness checks, or when the user asks for a senior WordPress review. Prefer a focused PHP, plugin, MU-plugin, SCSS, or layout skill when the scope is clearly narrow.
metadata:
  author: riley-childs
  version: "1.0"
---

# Workflow

See `.agents/skills/_base/common-workflow.md`.

# Output

See `.agents/skills/_base/common-output.md`.

# Deterministic Inventory

For recursive or full-project audits, use `scripts/inventory.py` instead of relying on memory or a shallow directory listing. Pass only extensions relevant to the task (for example `.php`, `.js`, `.scss`, `.css`). The script provides a reproducible file list and total before review.
