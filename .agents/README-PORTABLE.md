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

## Project review usage

For `wordpress-code-review`, select/attach the theme directory once and ask for the review. The skill treats that directory as the target root and discovers its source files through workspace access. Do not attach the child files individually.

Example:

```text
[attach/select generic-outdoor-theme directory]
Review this WordPress theme.
```

The skill should activate from the request, run its `inventory.py` helper against the selected directory, and inspect the source in small logical batches. The inventory is a path index, not a command to load all file contents into model context.

For large reviews, the selected directory remains only the target locator; the skill must not eagerly load the entire directory into one prompt.

## Directory-first usage for every skill

Attach/select the WordPress theme, plugin, or project directory once, then invoke any skill or describe the task. All skills treat that directory as the workspace root and discover the files they need from it. You should not have to attach source files individually.

Example:

```text
[attach generic-outdoor-theme directory]
Review the PHP.
```

```text
[attach generic-outdoor-theme directory]
Review the SCSS.
```

```text
[attach generic-outdoor-theme directory]
Explain the search implementation.
```

```text
[attach generic-outdoor-theme directory]
Build/refactor the card component.
```

The agent should inspect only task-relevant files in manageable batches rather than loading the entire directory into context.
