# Plugin Architecture

- Keep the main plugin file small and focused on bootstrap/registration.
- Check activation/deactivation/uninstall responsibilities and avoid destructive surprises.
- Register hooks at appropriate times; avoid needless work on every request.
- Keep admin-only behavior scoped to admin contexts when possible.
- Separate integrations, persistence, UI/admin, and domain logic when complexity justifies it.
- Avoid theme dependencies for durable plugin behavior.
