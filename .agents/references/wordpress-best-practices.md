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
