# MU-Plugin Runtime

- MU-plugins load automatically and do not use the normal plugin activation flow.
- Check loader organization, load order assumptions, and dependencies on conventional plugins/themes.
- Minimize unconditional work on every request.
- Guard integrations/dependencies gracefully and fail safely.
- Keep site-critical behavior independent of presentation/theme code.
- Prefer explicit namespacing/prefixing to reduce global collisions.
