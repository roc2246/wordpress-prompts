---
name: wordpress-plugin-review
description: Review a conventional WordPress plugin for lifecycle, hooks, admin/settings, REST/AJAX, persistence, permissions, security, performance, accessibility, and production readiness. Use for plugins that are not MU-plugins.
metadata:
  author: riley-childs
  version: "3.0"
---

# WordPress Plugin Review

Use `_base/common-workflow.md` and `_base/common-output.md`.

1. Run `scripts/inventory.py` on the plugin root and inspect the main plugin/bootstrap file first.
2. Load `references/plugin-architecture.md` only for lifecycle/structure.
3. Load `references/security-persistence.md` only for requests, admin actions, REST/AJAX, options/meta, or database access.
4. Use `references/exhaustive-review.md` only for an explicit full audit.
