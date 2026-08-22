---
name: wordpress-mu-plugin-review
description: Reviews WordPress must-use plugin code for architecture, security, hooks/filters, dependency behavior, performance, maintainability, and site-wide reliability. Use specifically for files under mu-plugins or functionality intentionally loaded as an MU-plugin.
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
