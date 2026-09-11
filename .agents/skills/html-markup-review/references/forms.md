# Forms

- Associate every user-facing control with a `label` using `for`/`id` or a valid wrapping label.
- Use the most specific input type and meaningful `name`; preserve server-side names and IDs unless broken.
- Group related controls with `fieldset` and `legend` when one label does not describe the group.
- Give every form button an explicit `type`; use `submit`, `reset`, or `button` intentionally.
- Add `autocomplete` tokens when the field's purpose is known; do not guess sensitive purposes.
- Use `required` only for genuinely required fields and pair constraints with understandable error messaging.
- Keep server/template validation logic intact while improving relationships such as `aria-describedby` or `aria-invalid` when justified.
