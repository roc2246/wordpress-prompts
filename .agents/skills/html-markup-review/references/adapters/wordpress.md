# WordPress Adapter

Use only when WordPress PHP or WordPress helpers are present. Apply core markup rules to the rendered output.

- Preserve `get_header()`, `get_footer()`, template parts, The Loop, conditionals, and existing hooks.
- Understand `wp_nav_menu()` and `get_search_form()` as generated markup; inspect configuration and surrounding landmarks before changing wrappers.
- Preserve escaping and validate dynamic URLs/content through existing WordPress APIs; do not replace helpers with literal output.
- Account for WordPress image helpers and generated responsive attributes before recommending media changes.
- Treat WordPress conventions as supplemental context, not requirements for non-WordPress files.
