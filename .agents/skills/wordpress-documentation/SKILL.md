---
name: wordpress-documentation
description: Audits WordPress project documentation for accuracy, drift, setup clarity, architecture, standards, and missing developer guidance. Use when the user asks to review, update, synchronize, or improve README/project documentation after code or architecture changes.
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
