---
name: wordpress-plugin-review
description: Reviews conventional WordPress plugin code for architecture, security, settings/admin pages, custom content types, REST/AJAX, database access, capabilities, nonces, performance, accessibility, and production readiness. Use for plugin code that is not an MU-plugin.
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
