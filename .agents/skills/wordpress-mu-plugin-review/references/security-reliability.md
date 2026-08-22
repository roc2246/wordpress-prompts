# Security and Reliability

- Apply validation, sanitization, capabilities, nonces, and output escaping at the correct boundaries.
- Treat external services and stored values as fallible/untrusted.
- Avoid fatal failures when optional dependencies are unavailable.
- Check error handling/logging without leaking secrets or sensitive data.
- Be cautious with authentication, authorization, redirects, cron, and site-wide filters because effects are global.
