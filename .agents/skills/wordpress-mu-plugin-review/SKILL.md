---
name: wordpress-mu-plugin-review
description: Review WordPress must-use plugins for always-loaded behavior, hook timing, dependencies, security, reliability, performance, and maintainability. Use specifically for MU-plugin code.
metadata:
  author: riley-childs
  version: "3.0"
---

# WordPress MU-Plugin Review

Use `_base/common-workflow.md` and `_base/common-output.md`.

1. Run `scripts/inventory.py` on the MU-plugin root; inspect loaders and always-on paths first.
2. Load `references/mu-plugin-runtime.md` for MU-specific lifecycle behavior.
3. Load `references/security-reliability.md` only for privileged/site-wide operations or external dependencies.
4. Use `references/exhaustive-review.md` only for an explicit full audit.
