---
name: wordpress-scss-review
description: Review WordPress SCSS/CSS for architecture, Sass usage, specificity, tokens, responsive behavior, accessibility, reuse, and maintainability. Use for styling audits/refactors, not general PHP/theme review.
metadata:
  author: riley-childs
  version: "3.0"
---

# WordPress SCSS Review

Use `_base/common-workflow.md` and `_base/common-output.md`.

1. Run `scripts/inventory.py <root> --ext .scss --ext .css`; inspect entrypoints/partials first.
2. Load `references/architecture-and-sass.md` only for organization/reuse concerns.
3. Load `references/responsive-accessibility.md` only when layout/interactions require it.
4. Use `references/exhaustive-review.md` only for an explicit full styling audit.
