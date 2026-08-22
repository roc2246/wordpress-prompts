# PHP and WordPress

- Keep functions cohesive and avoid oversized `functions.php`.
- Prefer WordPress APIs/hooks over reimplementing platform behavior.
- Check hook timing, priorities, callback signatures, and side effects.
- Keep template logic light; move reusable behavior to focused modules.
- Use query APIs correctly and reset global post state when required.
- Avoid hardcoded URLs/paths; use theme/plugin/WordPress helpers.
- Keep durable functionality outside the theme when it must survive theme changes.
