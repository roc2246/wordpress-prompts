---
name: agent-skill-review
description: Audit a SKILL.md-based Agent Skills repository for discoverability, progressive disclosure, token efficiency, modularity, scripts, portability, stale references, and redundancy. Use when reviewing or optimizing Agent Skills architecture.
metadata:
  author: riley-childs
  version: "2.0"
---

# Agent Skill Review

1. Run `scripts/inventory.py` to inspect structure without loading file contents.
2. Read frontmatter first and check skill boundaries/activation overlap.
3. Load `references/review-checklist.md` only for a full architecture audit.
4. Keep always-needed instructions in `SKILL.md`; move optional detail to references and deterministic work to scripts.
5. Flag duplicated instructions, oversized references, stale paths, generated caches, and unnecessary dependencies.
6. For edits, preserve useful domain knowledge and validate the final tree/references.
