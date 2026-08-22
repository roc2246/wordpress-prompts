---
name: wordpress-scss-review
description: Reviews SCSS/CSS architecture in WordPress themes or plugins for mobile-first structure, specificity, tokens, reusable components, responsive behavior, accessibility, and maintainability. Use for styling audits, 7-1 architecture reviews, or SCSS refactoring proposals.
metadata:
  author: riley-childs
  version: "1.1"
---

# Workflow

See `.agents/skills/_base/common-workflow.md`.

# Output

See `.agents/skills/_base/common-output.md`.

# Deterministic Inventory

For recursive or multi-file work, locate the requested target in the current workspace and run `scripts/inventory.py` against the narrowest relevant root. Do not ask the user to attach the entire theme/plugin/project with `@file` when workspace access is available.

Use the inventory only as a deterministic path index and coverage checklist. Pass only task-relevant extensions, then inspect file contents selectively in small logical batches. Never bulk-load every inventoried file into the model context in one request.
