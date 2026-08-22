# Theme Architecture

Use when reviewing theme structure or template ownership.

- Keep `functions.php` as orchestration; move cohesive setup/features to focused modules.
- Prefer template parts/components for repeated markup.
- Use WordPress APIs for enqueueing, URLs, queries, menus, images, and localization.
- Keep presentation/theme concerns separate from durable site functionality.
- Avoid hardcoded environment URLs/paths and unnecessary global state.
- Respect existing project conventions unless a change has clear benefit.
