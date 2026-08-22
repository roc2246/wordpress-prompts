# Claude Project Instructions

Use `.agents/skills/` as the primary source for repeatable WordPress workflows. Select the narrowest matching skill from its `name` and `description`, then load only that skill's `SKILL.md` when the task matches.

Keep global context lean:

- Do not preload every project standard or review checklist.
- Load a skill's `references/project-standards.md` only when repository conventions affect the task.
- Load `references/detailed-checklist.md` only for deep or exhaustive work.
- Use bundled scripts for deterministic file inventory or repeatable operations when provided.
- Inspect only files needed for the request, expanding scope for template relationships, hooks, call sites, configuration, or runtime behavior when necessary.

When making code changes, preserve unrelated code, validate with the project's existing checks when available, and provide a concise Git commit message.
