---
name: wordpress-component
description: Builds or refactors reusable WordPress theme components/template parts with PHP markup, accessible behavior, and accompanying SCSS/JavaScript when needed. Use when the user asks to create, extract, modernize, or standardize a reusable theme component or template part. Works from an attached or selected project directory without requiring individual child-file attachments.
metadata:
  author: riley-childs
  version: "1.2"
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

For recursive or multi-file work, locate the requested target in the current workspace and run `scripts/inventory.py` against the narrowest relevant root. Do not ask the user to attach the entire theme/plugin/project with `@file` when workspace access is available.

Use the inventory only as a deterministic path index and coverage checklist. Pass only task-relevant extensions, then inspect file contents selectively in small logical batches. Never bulk-load every inventoried file into the model context in one request.
