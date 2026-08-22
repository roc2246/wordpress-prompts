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
