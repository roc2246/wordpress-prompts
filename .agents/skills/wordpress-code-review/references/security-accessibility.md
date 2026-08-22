# Security and Accessibility

Load only when relevant.

- Validate expected values before use; sanitize untrusted input; authorize privileged actions; use nonces where request intent matters; escape as late as possible for the output context.
- Prefer WordPress escaping helpers appropriate to HTML, attributes, URLs, and JavaScript contexts.
- Check generated markup for semantic elements, labels/names, heading order, keyboard access, focus behavior, and meaningful link/button text.
- Do not add ARIA where native HTML already expresses the semantics.
