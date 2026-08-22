---
name: wordpress-php-review
description: Focused review of WordPress PHP and custom-theme implementation. Use for templates, functions.php, inc modules, custom post types/taxonomies, ACF integration, hooks, escaping/sanitization, enqueue logic, or PHP-specific WordPress best-practice audits.
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
