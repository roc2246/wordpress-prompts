# Security Boundaries

Apply only where relevant.

- Validate shape/allowed values before use.
- Sanitize untrusted input before storage/use.
- Check capabilities for authorization; authentication alone is not authorization.
- Use nonces for CSRF/request-intent protection where appropriate; nonces do not replace capability checks.
- Escape at output using the correct context helper.
- Parameterize database queries and avoid building SQL from untrusted strings.
- Treat REST/AJAX/form/request/third-party values as untrusted until checked.
