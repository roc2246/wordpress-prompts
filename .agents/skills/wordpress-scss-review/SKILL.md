---
name: wordpress-scss-review
description: Reviews SCSS/CSS architecture in WordPress themes or plugins for mobile-first structure, specificity, tokens, reusable components, responsive behavior, accessibility, and maintainability. Use for styling audits, 7-1 architecture reviews, or SCSS refactoring proposals.
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
