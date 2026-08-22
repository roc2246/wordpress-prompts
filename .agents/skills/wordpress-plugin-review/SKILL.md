---
name: wordpress-plugin-review
description: Review a conventional WordPress plugin for architecture, lifecycle, hooks, admin/settings, REST/AJAX, persistence, permissions, security, performance, accessibility, and production readiness. Use for plugins that are not MU-plugins.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress Plugin Review

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inventory the plugin with `scripts/inventory.py` and inspect the bootstrap/main plugin file first.
2. Follow registration, hooks, services/modules, request handlers, and persistence paths.
3. Load `references/plugin-architecture.md` for lifecycle/structure.
4. Load `references/security-persistence.md` when requests, admin actions, REST/AJAX, options/meta, or database access are in scope.
5. Use `references/exhaustive-review.md` only for full audits.

## Output
Prioritize security/correctness, then lifecycle/architecture, performance, accessibility, and maintainability.
