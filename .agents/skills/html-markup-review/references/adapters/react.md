# React Adapter

Use only for JSX/TSX or React components. Evaluate the DOM semantics React will render.

- Accept `className`, fragments, JSX expressions, conditional rendering, mapped children, and component boundaries as host syntax.
- Do not treat JSX attribute spelling or expressions as invalid HTML; check the resulting element and accessible name.
- Preserve component APIs, keys, state, event handlers, and test selectors unless they directly cause the markup issue.
- Check whether a component renders a native control before recommending ARIA or keyboard handlers.
