---
name: wordpress-explain-code
description: Explains selected WordPress/PHP/JavaScript/SCSS code in plain English, including data flow, hooks, template relationships, security/accessibility implications, and how it fits the project. Use for code walkthroughs, onboarding, learning, or “what does this do?” questions. Works from an attached or selected project directory without requiring individual child-file attachments.
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
