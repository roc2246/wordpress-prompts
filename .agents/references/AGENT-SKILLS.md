# Agent Skills Architecture

This toolkit uses `.agents/skills/` as the primary AI workflow interface. Detailed WordPress review criteria live inside each skill under `references/`, so task-specific context can be loaded only when needed.

## Why this structure

The skill layout follows progressive disclosure:

1. **Discovery:** the agent sees each skill's `name` and `description`.
2. **Activation:** only the matching `SKILL.md` is loaded.
3. **Execution:** detailed checklists, project standards, and scripts are loaded only when the active task requires them.

This avoids injecting every WordPress standard and every review checklist into every request while keeping each skill portable.

## Skill anatomy

Each skill may contain:

- `SKILL.md` — concise metadata and repeatable workflow.
- `references/detailed-checklist.md` — deep/exhaustive review criteria.
- `references/project-standards.md` — bundled WordPress/project conventions loaded only when relevant.
- `scripts/` — deterministic helpers for recursive inventory and repeatable operations.

Shared instructions live under `.agents/skills/_base/`.

## Authoring rules

- Create narrowly scoped skills rather than enlarging global instruction files.
- Make `description` state both what the skill does and when it should activate.
- Keep `SKILL.md` limited to instructions needed on every activation.
- Put long criteria, examples, domain references, schemas, and edge cases in `references/`.
- Use scripts for deterministic operations when they are more reliable than model memory.
- Load project standards selectively.
- Keep instructions portable across assistants unless a capability genuinely requires a specific product.
