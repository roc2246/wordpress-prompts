# Architecture

## System Overview

This toolkit targets reusable custom WordPress themes and site-specific WordPress development, with optional custom plugins and MU-plugins where functionality does not belong in the theme.

- Theme responsibilities: presentation, templates, template parts, theme assets, editor-facing theme support, and view-layer integration with WordPress APIs.
- Plugin responsibilities: reusable or site-critical functionality that should survive a theme change.
- MU-plugin responsibilities: site-wide functionality that must load automatically and is intentionally controlled outside the normal plugin activation lifecycle.

## Theme Architecture

A practical custom theme may use:

- `functions.php`: lightweight bootstrap/registration only; delegate substantial functionality to included modules.
- `inc/`: theme setup, enqueue logic, helpers, integrations, customizer/editor support, and other modular PHP.
- `template-parts/`: reusable presentation fragments.
- `templates/` or WordPress template hierarchy files: route/page-level presentation.
- `assets/src/js/` or equivalent: handwritten JavaScript modules.
- `assets/src/scss/` or equivalent: SCSS source organized by settings/tools/components/layout/pages.
- `assets/dist/` or equivalent: generated assets; do not hand-edit generated output.

Adapt names to the actual project rather than forcing this exact tree.

## Request and Rendering Lifecycle

1. WordPress resolves the request and query.
2. WordPress selects the matching template through the template hierarchy.
3. Theme setup, hooks, filters, and enqueued assets contribute behavior.
4. Templates and template parts read data through WordPress APIs.
5. Dynamic output is escaped for its final HTML context.

## Separation of Concerns

- Keep presentation in templates/template parts.
- Keep reusable theme behavior in focused functions/modules.
- Keep durable business functionality out of the theme when it should survive a theme switch.
- Use hooks and filters when they provide a clear WordPress extension point; avoid hook-heavy indirection when a direct function call is simpler.
- Do not place unrelated site functionality in `functions.php` merely because it is convenient.

## Security Architecture

At trust boundaries:

- Validate and sanitize incoming data.
- Use nonces for state-changing requests when appropriate.
- Check capabilities before privileged operations.
- Escape dynamic output as late as possible for the output context.
- Use `$wpdb->prepare()` or WordPress data APIs for database queries.
- Treat REST, AJAX, form, URL, third-party, and user-controlled values as untrusted.

## Data and Content Architecture

- Use native WordPress content models where they fit: posts, pages, custom post types, taxonomies, metadata, users, options, and settings APIs.
- Register post types and taxonomies consistently and explicitly.
- Keep field/integration assumptions documented when using ACF or similar tooling.
- Avoid hardcoding environment-specific URLs, IDs, or credentials.

## Operational Notes

- Keep generated assets separate from source assets.
- Keep setup/build requirements documented.
- Keep documentation synchronized when template structure, asset pipelines, content models, hooks, or integrations change.
- Prefer incremental, project-appropriate architecture over enterprise abstractions.
