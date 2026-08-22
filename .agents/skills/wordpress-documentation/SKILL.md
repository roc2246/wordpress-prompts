---
name: wordpress-documentation
description: Audit or update WordPress project documentation for accuracy, setup/onboarding clarity, architecture, maintenance guidance, and drift from the codebase. Use for README, architecture, developer handoff, or code-documentation work.
metadata:
  author: riley-childs
  version: "2.0"
---

# WordPress Documentation

Use `.agents/skills/_base/common-workflow.md` and `.agents/skills/_base/common-output.md`.

## Workflow
1. Inventory documentation/config/source only as needed with `scripts/inventory.py`; do not read the whole project to verify a narrow doc claim.
2. Load `references/documentation-quality.md` for audit criteria.
3. Verify claims against the smallest relevant source/config set.
4. Prefer concise, durable documentation over comments that restate code.

## Output
Identify accurate material, missing/outdated guidance, proposed updates, and the highest-impact documentation action. When editing, keep terminology/commands consistent with the repository.
