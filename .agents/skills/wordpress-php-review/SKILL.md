---
name: wordpress-php-review
description: Review WordPress PHP for templates, functions.php, inc modules, hooks, custom content types, ACF integration, enqueue logic, trust boundaries, and WordPress API usage. Use when PHP is the primary concern rather than a broad theme audit.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress PHP Review

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inventory PHP with `scripts/inventory.py <root> --ext .php`.
2. Inspect bootstrap/setup files first, then templates/modules by dependency or runtime flow.
3. Load `references/php-wordpress.md` for API/architecture checks.
4. Load `references/security-boundaries.md` when input, output, permissions, REST/AJAX, forms, or database writes are involved.
5. Use `references/exhaustive-review.md` only for a full PHP audit.

## Output
Prioritize correctness/security first, then architecture, accessibility of generated markup, and maintainability. Suggest revised code only where it materially clarifies a fix.
