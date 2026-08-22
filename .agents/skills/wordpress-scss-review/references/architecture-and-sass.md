# Architecture and Sass

- Prefer clear layers/partials with one obvious entrypoint; use 7-1 only where it helps.
- Use variables/maps/functions/mixins when they remove meaningful repetition, not for abstraction alone.
- Keep nesting shallow and selectors predictable.
- Prefer reusable component classes over page-specific selector chains.
- Control specificity; avoid `!important` unless justified.
- Consolidate repeated design tokens such as spacing/type/breakpoints when a stable system exists.
