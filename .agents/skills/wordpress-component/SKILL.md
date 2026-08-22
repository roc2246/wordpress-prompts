---
name: wordpress-component
description: Builds or refactors reusable WordPress theme components/template parts with PHP markup, accessible behavior, and accompanying SCSS/JavaScript when needed. Use when the user asks to create, extract, modernize, or standardize a reusable theme component or template part.
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
