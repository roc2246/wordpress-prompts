---
name: wordpress-mu-plugin-review
description: Review WordPress must-use plugin code for always-loaded behavior, site-wide architecture, hook timing, dependency assumptions, security, reliability, performance, and maintainability. Use specifically for mu-plugins or functionality intentionally loaded as an MU-plugin.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress MU-Plugin Review

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inventory the MU-plugin root with `scripts/inventory.py`.
2. Identify loader files and always-on execution paths first.
3. Load `references/mu-plugin-runtime.md` for MU-specific behavior.
4. Load `references/security-reliability.md` for privileged/site-wide operations or external dependencies.
5. Use `references/exhaustive-review.md` only for a full audit.

## Output
Prioritize reliability and security because failures can affect the entire site; then performance and maintainability.
