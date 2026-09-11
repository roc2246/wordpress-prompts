# Document Structure

- Check the page's landmark model: one meaningful `main`, useful navigation names when multiple navs exist, and no redundant landmarks.
- Verify heading order and that headings describe the section they introduce.
- Check section boundaries, nesting, and whether wrappers add structural value.
- Flag invalid HTML relationships, duplicate IDs, duplicate primary content, and controls nested inside links or buttons.
- Preserve layout and CSS hooks; remove a wrapper only when its removal is behaviorally safe and materially improves structure.
- In partials/components, judge structure in the rendered parent context when that context is available.
