# Common Workflow

This workflow applies to WordPress Agent Skills for code review, audits, and analysis tasks.

1. Identify the exact files/folders and requested outcome. Do not broaden scope without a concrete reason.
2. Inspect the target code and nearby files needed to understand template relationships, hooks, call sites, enqueue/configuration behavior, data flow, or runtime behavior.
3. Load `references/project-standards.md` only when repository conventions affect the task.
4. For a deep or exhaustive audit, read `references/detailed-checklist.md`. Do not load it for a narrow question that can be answered from the target code and core instructions.
5. Base findings on code actually inspected. Never claim complete coverage without a deterministic inventory or evidence that every in-scope file was reviewed.
6. Treat request data, REST/AJAX input, form values, URLs, third-party data, and stored user-controlled content as runtime trust boundaries. Distinguish validation, sanitization, authorization, nonces, and output escaping.
7. Respect WordPress ownership boundaries: presentation belongs in the theme; durable/site-critical functionality should generally live in a plugin or MU-plugin when it must survive theme changes.
8. Prefer small, high-confidence, production-relevant changes over broad rewrites or new abstractions.
9. When code changes are requested, follow the repository's approval workflow if the detailed checklist requires it; after implementation, run relevant existing checks and report changed files plus validation results.
