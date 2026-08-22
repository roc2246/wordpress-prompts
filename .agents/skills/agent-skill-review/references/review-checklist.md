# Agent Skill Review Checklist

Use only for a full/deep architecture audit.

## Boundaries and discovery
- One clear capability/workflow per skill.
- Neighboring skills have distinguishable activation criteria.
- `name` is concise; `description` states capability and activation conditions.
- Catch-all skills remain fallbacks to narrower skills.

## Progressive disclosure and tokens
- `SKILL.md` contains only instructions useful on most activations.
- Long criteria/examples/edge cases live in topical references.
- Large references are split so narrow tasks load only relevant context.
- Remove duplicated prose, archived prompts, generated caches, and repeated global standards.
- Do not load project-wide standards when a smaller domain reference is enough.

## Scripts/assets
- Deterministic repeatable work uses scripts when more reliable/cheaper than model reasoning.
- Inventory scripts return paths/metadata, not bulk source contents.
- Scripts/assets exist only when useful.

## Portability and validation
- Skills avoid silent dependencies on unrelated sibling skills.
- Referenced paths exist and documentation matches the current architecture.
- Check `__pycache__`, `*.pyc`, nested repositories, stale links, and obsolete entrypoints.
- Inventory all skills before claiming complete coverage.
