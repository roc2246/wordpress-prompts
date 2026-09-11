# Accessibility

- Every control needs a reliable accessible name from visible text, an associated label, or a justified name attribute.
- Prefer native controls and keyboard behavior. Do not make `div`/`span` elements interactive when a button, link, or form control fits.
- Use ARIA only to communicate semantics or state that native HTML cannot provide; keep roles and states consistent.
- Check keyboard access, focusable order, disabled/loading/error states, and visible focus where interaction is present.
- Decorative images should use empty `alt`; meaningful images need context-specific alt text. Flag uncertain purpose instead of guessing.
- Associate validation text with its control and expose invalid/error state accessibly when the surrounding application supports it.
- Check landmark labels only where needed to distinguish repeated landmark types; do not add redundant ARIA labels.
