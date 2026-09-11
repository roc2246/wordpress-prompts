---
name: html-markup-review
description: Review and improve HTML or HTML-generating templates for semantics, document structure, accessibility, forms, media, maintainability, and standards compliance. Use for HTML, PHP templates, JSX/TSX, Vue, Liquid, Twig, Handlebars, and static-site markup.
metadata:
  author: riley-childs
  version: "1.0"
---

# HTML Markup Review

Review markup at the rendered-HTML level while preserving the host template language. Make the smallest change that fixes a confirmed problem; do not rewrite working markup for preference alone.

## Workflow

1. Identify the syntax and template environment from the file and nearby code.
2. Inspect the smallest relevant markup region plus its data/control-flow context.
3. Apply the core modules below to the rendered structure.
4. Load only the matching adapter when framework-specific syntax or behavior is present.
5. Classify meaningful findings as `Error`, `Improvement`, or `Optional`; prioritize Errors and Improvements.
6. Preserve classes, IDs, template expressions, JavaScript hooks, visual layout, and behavior unless they cause the issue.
7. Return the improved markup and briefly explain the important changes and any items that need human context.

## Core modules

Load references as needed:

- `references/semantic-html.md` for element choice, controls, lists, tables, and native semantics.
- `references/document-structure.md` for landmarks, headings, nesting, and wrappers.
- `references/accessibility.md` for names, keyboard access, ARIA, and state/validation messaging.
- `references/forms.md` for labels, grouping, input types, autocomplete, required fields, and buttons.
- `references/images-media.md` for alt text, figures, responsive media, and layout shift.
- `references/markup-cleanup.md` for repetition, nesting, class structure, and maintainability.

## Optional adapters

Adapters extend the core rules; they never replace them. Load only the relevant reference:

- `references/adapters/wordpress.md`
- `references/adapters/react.md`
- `references/adapters/shopify-liquid.md`
- `references/adapters/other-templates.md`

## Guardrails

- Prefer native HTML over ARIA when native semantics provide the behavior.
- Do not invent image alternative text when purpose cannot be established; flag it instead.
- Do not convert every `div` or `span`; change it only when the replacement accurately describes the content or behavior.
- Treat template expressions, loops, conditionals, components, and generated attributes as valid host syntax.
- Do not remove template logic or rename public hooks as part of a markup cleanup.
- Do not propose large architectural refactors unless they clearly reduce markup complexity or prevent a real defect.

## Output

For review-only requests, list confirmed findings first with severity and location, then optional suggestions. For edits, show the changed markup, summarize why it changed, and note validation or unresolved context.
