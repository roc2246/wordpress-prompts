---
name: wordpress-php-review
description: Review WordPress PHP for templates, functions.php, modules, hooks, content types, ACF, enqueue logic, trust boundaries, and WordPress API usage. Use when PHP is the primary concern.
metadata:
  author: riley-childs
  version: "3.0"
---

# WordPress PHP Review

Use `_base/common-workflow.md` and `_base/common-output.md`.

1. Run `scripts/inventory.py <root> --ext .php`; inspect bootstrap/setup files first.
2. Load `references/php-wordpress.md` only for API/architecture questions.
3. Load `references/security-boundaries.md` only for input/output, permissions, REST/AJAX, forms, or writes.
4. Use `references/exhaustive-review.md` only for an explicit full PHP audit.
