# Common Workflow

This workflow applies to **all WordPress Agent Skills** in this repository.

## Directory-First Invocation

The default user workflow for every skill is:

1. The user attaches/selects one WordPress theme, plugin, or project directory.
2. The user asks for the desired task or invokes the relevant skill.
3. Treat the attached/selected directory as the project root automatically.
4. Do **not** require the user to attach child files individually.

When exactly one project directory is attached or selected, infer it as the target root unless the user explicitly names a narrower file, subdirectory, component, plugin, template, or feature.

A directory attachment is a **workspace locator**, not an instruction to eagerly inject every child file into one model request. Use workspace/file-system access to inspect only the files needed for the active skill.

If a skill needs one specific file or component, discover it from the attached directory first. Ask the user for a narrower target only when the request itself is genuinely ambiguous and the workspace cannot resolve it.

## Standard Workflow

1. Identify the requested outcome from the user's message and the attached/selected project directory.
2. Resolve the directory to its workspace path and use it as the project root.
3. For recursive, project-wide, or multi-file work, run the active skill's `scripts/inventory.py` when that skill provides one. Use the inventory only for deterministic discovery and coverage tracking; it is not a bulk-content loader.
4. Pass only extensions relevant to the active task. Examples:
   - PHP review: `.php`
   - SCSS review: `.scss` and, when needed, `.css`
   - plugin/MU-plugin review: primarily `.php`, plus related JS/CSS when relevant
   - component work: PHP plus directly related SCSS/JS
   - documentation: documentation/config files plus only enough source to verify claims
   - mixed code review: `.php`, `.js`, `.jsx`, `.ts`, `.tsx`, `.scss`, `.css`
5. Do **not** read every inventoried file into context at once. Inspect files in small logical batches based on entry points, dependencies, template relationships, hooks, call sites, enqueue/configuration behavior, data flow, or runtime behavior.
6. Prefer repository/workspace access over manual context attachments. Never tell the user to attach every file individually when the attached directory is available.
7. Load `references/project-standards.md` only when repository conventions affect the task.
8. For a deep or exhaustive audit, read `references/detailed-checklist.md`. Do not load it for a narrow question that can be answered from the target code and core instructions.
9. Base findings on code actually inspected. Never claim complete coverage without deterministic evidence. For large audits, track progress in batches rather than attempting one oversized prompt.
10. Treat request data, REST/AJAX input, form values, URLs, third-party data, and stored user-controlled content as runtime trust boundaries. Distinguish validation, sanitization, authorization, nonces, and output escaping.
11. Respect WordPress ownership boundaries: presentation belongs in the theme; durable/site-critical functionality should generally live in a plugin or MU-plugin when it must survive theme changes.
12. Prefer small, high-confidence, production-relevant changes over broad rewrites or unnecessary abstractions.
13. When code changes are requested, follow the repository's approval workflow if the detailed checklist requires it; after implementation, run relevant existing checks and report changed files plus validation results.

## Context Safety

- Treat the context window as a scarce resource.
- The attached directory identifies the workspace; it does not mean every file should be loaded.
- Inventory first when appropriate, then selectively open files.
- Never paste or echo the full inventory plus full contents of all files into one response or tool result.
- Reuse already inspected information instead of reopening unchanged files without a reason.
- If the target is too large for one pass, split work into deterministic batches and continue until the requested scope is covered.
- If the host attempts to expand a directory attachment into oversized context, do not mirror or re-request that content. Prefer direct workspace reads and the skill's inventory workflow.
