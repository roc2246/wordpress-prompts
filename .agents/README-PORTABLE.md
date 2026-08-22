# Portable WordPress Agent Skills

This toolkit is intentionally self-contained under `.agents/`.

Copy the `.agents` folder directly into the root of any WordPress workspace or repository. No sibling prompt, documentation, or configuration folders are required by this toolkit.

## Runtime layout

- `.agents/skills/<skill-name>/SKILL.md` — skill entry points
- `.agents/skills/<skill-name>/references/` — progressively disclosed, skill-specific guidance
- `.agents/skills/<skill-name>/scripts/` — deterministic helper scripts where useful
- `.agents/skills/_base/` — shared workflow and output contracts
- `.agents/references/` — toolkit-level source documentation and legacy/reference material

Each skill is designed to remain useful when copied independently because essential project standards are bundled into its own `references/project-standards.md`.
