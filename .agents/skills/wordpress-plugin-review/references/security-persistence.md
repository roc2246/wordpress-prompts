# Security and Persistence

- Validate/sanitize request data and escape output by context.
- Require appropriate capabilities for privileged actions; use nonces where CSRF protection is needed.
- Define REST permission callbacks intentionally.
- Protect AJAX/admin-post handlers and do not trust request parameters.
- Use Settings/Options/Metadata APIs where suitable; parameterize custom SQL.
- Avoid autoloading large options unnecessarily and handle schema/data migrations deliberately.
