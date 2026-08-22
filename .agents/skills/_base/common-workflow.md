# Common Workflow

This workflow applies to WordPress Agent Skills for code review, audits, and analysis tasks.

1. Identify the requested target and outcome from the user's message and the current workspace. If the user names a theme, plugin, folder, or project, locate it with workspace/file-system tools; do **not** require the user to attach the whole target with `@file`.
2. For recursive, project-wide, or multi-file work, run the skill's `scripts/inventory.py` against the narrowest relevant root. Use it for deterministic discovery and coverage tracking. The inventory script returns file paths and a total only; it is not a bulk-content loader.
3. Pass only extensions relevant to the task. Examples: PHP review uses `.php`; SCSS review uses `.scss` and, when needed, `.css`; mixed theme review may use `.php`, `.js`, `.scss`, and `.css`.
4. Do **not** read every inventoried file into context at once. Use the inventory as an index, then inspect files in small logical batches based on entry points, dependencies, template relationships, hooks, call sites, enqueue/configuration behavior, data flow, or runtime behavior.
5. Prefer repository/workspace access over large manual context attachments. Avoid asking for `@file:<project-folder>` or equivalent whole-folder attachments when the agent can already inspect the workspace.
6. Load `references/project-standards.md` only when repository conventions affect the task.
7. For a deep or exhaustive audit, read `references/detailed-checklist.md`. Do not load it for a narrow question that can be answered from the target code and core instructions.
8. Base findings on code actually inspected. Never claim complete coverage without a deterministic inventory and evidence that every in-scope file was reviewed. For large audits, track progress against the inventory and continue in batches rather than attempting one oversized prompt.
9. Treat request data, REST/AJAX input, form values, URLs, third-party data, and stored user-controlled content as runtime trust boundaries. Distinguish validation, sanitization, authorization, nonces, and output escaping.
10. Respect WordPress ownership boundaries: presentation belongs in the theme; durable/site-critical functionality should generally live in a plugin or MU-plugin when it must survive theme changes.
11. Prefer small, high-confidence, production-relevant changes over broad rewrites or new abstractions.
12. When code changes are requested, follow the repository's approval workflow if the detailed checklist requires it; after implementation, run relevant existing checks and report changed files plus validation results.

## Context Safety

- Treat the context window as a scarce resource.
- Inventory first, then selectively open files.
- Never paste or echo the full inventory plus full contents of all files into one response or tool result.
- Reuse already inspected information instead of reopening unchanged files without a reason.
- If the target is too large for one pass, split the review into deterministic batches and clearly state what has and has not been reviewed.
