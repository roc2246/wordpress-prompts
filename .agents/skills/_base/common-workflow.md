# Common Workflow

Use this only for behavior shared by WordPress skills.

1. Treat the selected/named WordPress theme, plugin, or project directory as the workspace root. A directory is a locator, not a request to inject every child file into context.
2. For multi-file work, run the active skill's `scripts/inventory.py` when present. Use its output only as a path index and coverage checklist.
3. Read only task-relevant files, in small logical batches. Prefer entry points, dependencies, hooks, template relationships, and call sites over broad file loading.
4. Load a skill reference only when its topic is relevant. Do not load every reference by default.
5. Base findings on inspected code. Never claim complete coverage without inventory/inspection evidence.
6. Keep WordPress trust boundaries distinct: validate expected shape, sanitize input, authorize with capabilities, use nonces for request intent/CSRF protection where applicable, and escape at output.
7. Keep presentation in themes; durable site functionality belongs in plugins/MU-plugins when it must survive theme changes.
8. Prefer small, production-relevant changes over rewrites or abstractions without clear payoff.

## Context safety

- Never ask the user to attach every child file when workspace access exists.
- Never bulk-read all inventoried files into one prompt.
- Reuse already-inspected context instead of reopening unchanged files.
- Split large audits into deterministic batches and synthesize after coverage is complete.

## Editing

For review-only requests, do not modify files. For explicit implementation requests, make only requested/approved changes, run relevant existing checks, and report changed files and validation results.
