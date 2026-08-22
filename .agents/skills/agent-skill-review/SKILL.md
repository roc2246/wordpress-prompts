---
name: agent-skill-review
description: Audit an Agent Skills repository for discoverability, progressive disclosure, token efficiency, modularity, deterministic scripting opportunities, portability, stale references, and redundant files. Use when reviewing or optimizing SKILL.md-based AI architecture.
metadata:
  author: riley-childs
  version: "1.0"
---

# Agent Skill Review

## Workflow

1. Run `scripts/inventory.py` to inventory each skill and its `SKILL.md`, references, scripts, and assets without loading file contents.
2. Read skill frontmatter first; evaluate names/descriptions and overlapping activation criteria.
3. Load `references/review-checklist.md` for a full architecture audit.
4. Prefer progressive disclosure: always-needed instructions in `SKILL.md`, contextual/deep knowledge in references, deterministic repeatable work in scripts.
5. Identify duplicated/legacy instruction layers, oversized references, stale paths, generated caches, and hidden cross-skill dependencies.
6. Do not recommend scripts/assets or folder symmetry unless they add real capability.
7. For implementation requests, make safe structural edits, preserve useful domain knowledge, then validate references and the final skill tree.

## Output

For each skill/file, give keep/change/delete and the reason. Prioritize architecture-wide changes, then skill-specific improvements. If files are changed, report validation and a concise Git commit message.
