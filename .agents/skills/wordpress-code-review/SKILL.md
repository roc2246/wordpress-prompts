---
name: wordpress-code-review
description: General code review for a WordPress theme or mixed WordPress codebase. Use when the user attaches or names a theme directory and asks for a code review, production-readiness audit, maintainability review, or senior WordPress review. The directory attachment is a target locator, not a request to load every file into model context. Works from an attached or selected project directory without requiring individual child-file attachments.
metadata:
  author: riley-childs
  version: "1.3"
---

# Workflow

See `.agents/skills/_base/common-workflow.md`.

# Output

See `.agents/skills/_base/common-output.md`.

# Directory-First Invocation

This skill is designed to work from the **project directory alone**.

- If exactly one WordPress theme/plugin/project directory is attached or selected, use it as the project root automatically.
- Discover the files needed for this skill from that directory.
- Do not ask the user to attach individual child files when workspace access to the directory is available.
- Read only task-relevant files in small batches; do not load the entire directory into model context at once.
- If the user explicitly names a narrower file, component, plugin, template, or subdirectory, use that narrower target while keeping the attached directory as the workspace root.

# Deterministic Inventory

For recursive or multi-file work:

1. Resolve the attached/selected directory to its workspace path.
2. Run `scripts/inventory.py <theme-root>` with no extra flags for a normal mixed-theme review. The script defaults to handwritten PHP, JavaScript/TypeScript, SCSS, and CSS source files.
3. Use the resulting paths only as an index and coverage checklist.
4. Inspect source in small logical batches. Do not bulk-load all inventoried files into context.
5. Review configuration files such as `package.json`, `theme.json`, `composer.json`, or build configuration separately when present and relevant.
6. Continue batch-by-batch until all in-scope files are covered, then synthesize one final report.

For a narrow review, pass `--ext` only for the needed source extensions.

# Context-Budget Guardrail

If the host tries to expand a directory attachment into a huge prompt, do not mirror, quote, or re-request that expanded content. Prefer workspace/file-system reads plus the deterministic inventory. Keep each content-reading batch small enough to leave substantial room for reasoning and findings.

Never tell the user to manually attach every file just to make this skill work.
