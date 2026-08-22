---
name: wordpress-plugin-review
description: Reviews conventional WordPress plugin code for architecture, security, settings/admin pages, custom content types, REST/AJAX, database access, capabilities, nonces, performance, accessibility, and production readiness. Use for plugin code that is not an MU-plugin.
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
