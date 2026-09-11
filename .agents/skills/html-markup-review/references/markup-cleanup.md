# Markup Cleanup

- Remove redundant wrappers only when they add no semantic, styling, scripting, or template value.
- Flag repeated hard-coded structures when the host system already has a clear data-driven or component pattern; avoid speculative refactors.
- Keep class and ID hooks stable. Prefer clear, role-oriented class structure over selectors that depend on deep nesting.
- Simplify excessive nesting when it does not change layout, selector behavior, event delegation, or template output.
- Treat maintainability suggestions as optional unless complexity creates a concrete defect or blocks accessibility/semantics.
- Preserve formatting and template syntax unless a small normalization makes the markup safer or easier to audit.
