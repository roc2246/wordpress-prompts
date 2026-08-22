# Project Standards Reference

Load this reference only when repository conventions affect the task. It is bundled with the skill for portability.

---

## Source: `coding-standards.md`

# Coding Standards

## PHP / WordPress

Use:
- WordPress Coding Standards-compatible formatting where practical.
- Context-appropriate escaping such as `esc_html()`, `esc_url()`, `esc_attr()`, and `wp_kses_post()`.
- Sanitization functions appropriate to the input type, such as `sanitize_text_field()`, `sanitize_email()`, and `absint()`.
- Validation before accepting external or user-controlled values.
- Nonces for state-changing form/AJAX operations when appropriate.
- Capability checks before privileged actions.
- WordPress APIs for URLs, queries, options, metadata, HTTP requests, and database access.
- Clear, scoped prefixes or namespaces for custom functions/classes to avoid collisions.

Prefer:
- Small focused modules.
- Reusable template parts for repeated presentation.
- Hooks and filters when they provide a useful WordPress extension point.
- Early returns and readable control flow.
- Dependency injection or explicit parameters when it improves testability without adding ceremony.

Avoid:
- Unescaped dynamic output.
- Trusting sanitized data as automatically valid.
- Hardcoded production URLs or credentials.
- Direct SQL when a WordPress API is appropriate.
- Inline styles/scripts when they belong in the asset pipeline.
- Large `functions.php` files containing unrelated responsibilities.
- Theme-bound business logic that should survive a theme change.

## SCSS

Use:
- Mobile-first styles.
- `rem` units for scalable sizing when appropriate.
- CSS custom properties for runtime theme/design values.
- SCSS variables, maps, mixins, and functions only where they reduce repetition or encode a meaningful rule.
- Grid for page/layout systems and Flexbox for one-dimensional alignment where appropriate.
- Component-oriented partials and a predictable architecture.

Avoid:
- Deep nesting and overly specific selectors.
- Random one-off values when a shared token already exists.
- Large files containing unrelated styles.
- Hand-editing compiled/generated CSS.
- Abstractions that make simple CSS harder to understand.

## JavaScript

Use:
- Small focused modules.
- `const`/`let`, modern browser APIs, and clear event handling.
- Progressive enhancement.
- Accessible interactions with keyboard and focus behavior considered.
- WordPress-provided packages/APIs when the project already depends on them and they fit the task.

Avoid:
- jQuery unless the project or dependency genuinely requires it.
- Avoidable globals.
- DOM behavior that duplicates native HTML capabilities.
- Large state systems for simple theme interactions.

## HTML / Templates

Use:
- Semantic HTML.
- A logical heading hierarchy.
- Proper labels, button elements, landmarks, and link semantics.
- WordPress body/post classes and core helpers where useful.

Avoid:
- Clickable `div`/`span` elements when a button or link is correct.
- ARIA used to compensate for avoidably incorrect native markup.

---

## Source: `wordpress-best-practices.md`

# WordPress Best Practices

## General Rules

Write WordPress code that is secure, readable, maintainable, accessible, and appropriate to the theme/plugin boundary. Prefer WordPress APIs over custom replacements when they solve the problem well.

## Escaping Output

Escape dynamic output for its final context, as late as practical:

```php
echo esc_html( $text );
echo esc_url( $url );
echo esc_attr( $attribute );
echo wp_kses_post( $trusted_rich_text );
```

Do not mechanically apply one escaping function everywhere; choose the correct context.

## Input Validation and Sanitization

- Treat external/user-controlled input as untrusted.
- Validate expected shape/range/allow-list requirements.
- Sanitize values before storage or processing where appropriate.
- Unslash WordPress request data before sanitizing when needed.
- Do not confuse sanitization with authorization or validation.

## Nonces and Capabilities

For privileged or state-changing operations:

- Verify an appropriate nonce when CSRF protection is required.
- Check the user's capability separately.
- Never treat a valid nonce as proof of authorization.

## Database Access

- Prefer `WP_Query`, metadata APIs, options/settings APIs, and other native data APIs.
- For custom SQL, use `$wpdb->prepare()` for dynamic values.
- Avoid unnecessary queries inside loops.
- Consider pagination and query cost for potentially large datasets.

## Theme vs Plugin Responsibilities

Theme code should primarily control presentation. Functionality that must survive a theme change generally belongs in a plugin or MU-plugin, especially business rules, integrations, custom application behavior, and site-critical content-model functionality.

## Templates and Components

- Follow the template hierarchy intentionally.
- Use template parts for repeated presentation.
- Keep heavy business logic out of templates.
- Use core helpers such as `get_template_part()`, `wp_nav_menu()`, `body_class()`, `post_class()`, and enqueue APIs when they fit.

## Assets

- Enqueue scripts and styles instead of hardcoding tags into templates.
- Version assets intentionally for cache invalidation.
- Load scripts in the footer or with appropriate loading strategies when safe.
- Do not hand-edit compiled assets when source files exist.

## Hooks and Filters

- Use hooks/filters when they make code composable or integrate with WordPress lifecycle events.
- Name callbacks clearly.
- Keep hook registration easy to discover.
- Avoid excessive hook indirection for internal code where a direct call is clearer.

## Custom Post Types and Taxonomies

- Choose stable slugs and capabilities.
- Configure public/query/rewrite behavior deliberately.
- Flush rewrite rules only on activation/deactivation or explicit maintenance—not on every request.
- Document ownership: if a content type must survive theme changes, register it in a plugin rather than the theme.

## REST API and AJAX

- Define explicit permission callbacks for REST endpoints.
- Validate and sanitize request parameters.
- Return structured `WP_REST_Response`/`WP_Error` results where appropriate.
- For AJAX, verify nonce/capability requirements and return consistent JSON responses.

## Accessibility

- Use semantic HTML and native controls.
- Ensure menus, forms, dialogs, toggles, and dynamic updates are keyboard-operable.
- Preserve focus visibility and meaningful accessible names.
- Use ARIA only when native HTML is insufficient.

## Performance and Reliability

- Avoid repeated expensive queries.
- Cache expensive derived data only when measurements or workload justify it.
- Handle missing content/configuration gracefully.
- Keep debug output and secrets out of production responses.
- Prefer boring, predictable code over unnecessary framework-style abstractions.

---

## Source: `architecture.md`

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

---

## Source: `style-guide.md`

# Style Guide

## General Style

The theme should look clean, professional, accessible, and adaptable to different brands and content needs.

Prioritize:
- Readability
- Consistency
- Accessibility
- Responsive design
- Reusable components
- Simple, maintainable CSS

Avoid random one-off styling, unnecessary visual complexity, repeated CSS, and styling directly inside PHP templates.

## Layout

Use:
- Mobile-first CSS
- CSS Grid for page-level/two-dimensional layouts
- Flexbox for one-dimensional component alignment
- A consistent container/layout wrapper
- Reasonable max-widths for readable content

Layouts should stack cleanly on small screens, expand intentionally at larger breakpoints, preserve consistent spacing, and avoid preventable layout shifts.

## Spacing

Prefer a small shared spacing scale, for example:

```scss
$space-1: 0.25rem;
$space-2: 0.5rem;
$space-3: 0.75rem;
$space-4: 1rem;
$space-6: 1.5rem;
$space-8: 2rem;
$space-12: 3rem;
$space-16: 4rem;
```

Use the project's real tokens if they already exist; do not introduce a second spacing system without a reason.

## Typography

- Use a deliberate type scale and comfortable line-height.
- Keep body text readable across viewport sizes.
- Preserve semantic heading order independently from visual styling.
- Avoid excessively long line lengths; use content max-widths where needed.

## Components

- Reuse visual patterns instead of duplicating one-off variants.
- Keep component styles near the component's responsibility.
- Define interactive states: hover, focus-visible, active, disabled, error, and loading where relevant.
- Prefer native controls before creating custom interaction patterns.

## Responsive Design

- Start from content needs, not device brand breakpoints.
- Add breakpoints when the layout actually needs them.
- Test navigation, cards, forms, media, tables, and long content at narrow widths.
- Avoid hiding essential content merely to make a layout fit.

## Accessibility

- Maintain sufficient text/background contrast.
- Keep visible keyboard focus.
- Do not rely on color alone to communicate state.
- Respect reduced-motion preferences for nonessential animation.
- Ensure controls have adequate target size and clear labels.

---

## Source: `project-instructions.md`

# Project Instructions

This is a reusable WordPress development toolkit for custom themes and site-specific functionality.

## Main Goals

- Build production-ready, maintainable WordPress implementations.
- Use clean PHP, SCSS, JavaScript, and semantic HTML.
- Keep theme, plugin, and MU-plugin responsibilities appropriately separated.
- Prioritize accessibility, responsiveness, security, and maintainability.
- Preserve portability across client and portfolio projects.

## When Helping With This Project

- Explain code clearly and simply.
- Mention the file path for proposed code.
- Prefer practical production-ready patterns.
- Follow WordPress APIs, coding standards, the project style guide, and the existing architecture.
- Preserve existing architecture unless a change has a clear benefit.
- Avoid adding dependencies, frameworks, or abstractions without justification.

## Code Changes

When implementation is requested:

- Keep changes scoped to the approved task.
- Explain why each meaningful change is being made.
- Note security/accessibility implications when relevant.
- Do not hand-edit generated assets when source files exist.
- Run the project's existing lint, test, build, PHP syntax, or static-analysis checks when available.

## Reviews

Prioritize:

1. Security and data trust boundaries
2. Maintainability
3. Accessibility
4. Correct WordPress architecture and APIs
5. Responsive design
6. Reliability and performance
7. Reusability

Focus on improvements that matter to agencies, freelance clients, small businesses, and in-house teams. Avoid unnecessary enterprise architecture.

## Git Commit Messages

If code changes, refactoring, file creation/deletion, or architecture changes are implemented or proposed, include a concise suggested Git commit message.

Format:

`Git commit message: <imperative summary>`

