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
