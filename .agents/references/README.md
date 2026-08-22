# WordPress AI Dev Toolkit

A reusable Agent Skills and standards toolkit for custom WordPress themes, plugins, and site-specific development.

This repository provides:
- Project standards for WordPress architecture, PHP, SCSS, JavaScript, accessibility, and security.
- Reusable Agent Skills for common engineering and review tasks.
- A progressive-disclosure workflow that keeps AI context focused and portable.

## Agent Skills (Recommended)

The primary workflow is `.agents/skills/`. Each task is a discoverable Agent Skill with concise metadata and instructions. Detailed criteria and bundled standards are loaded only when needed. See `AGENT-SKILLS.md`.

## Repository Structure

```text
wordpress-prompts/
  architecture.md
  CLAUDE.md
  coding-standards.md
  wordpress-best-practices.md
  project-context.md
  project-instructions.md
  style-guide.md
  README.md
  AGENT-SKILLS.md
  .github/
    copilot-instructions.md
  .agents/
    skills/
      wordpress-code-review/
      wordpress-component/
      wordpress-documentation/
      wordpress-explain-code/
      wordpress-layout-ux-review/
      wordpress-mu-plugin-review/
      wordpress-php-review/
      wordpress-plugin-review/
      wordpress-scss-review/
```

## Skill Catalog

- `wordpress-code-review` — general catch-all review for WordPress/PHP/JS/SCSS/theme code.
- `wordpress-component` — builds or refactors reusable theme/template components.
- `wordpress-documentation` — audits and updates repository documentation.
- `wordpress-explain-code` — explains selected WordPress code and project relationships.
- `wordpress-layout-ux-review` — reviews layout, UX, responsiveness, and accessibility.
- `wordpress-mu-plugin-review` — reviews site-wide must-use plugin architecture and safety.
- `wordpress-php-review` — focused PHP/theme and WordPress API review.
- `wordpress-plugin-review` — reviews conventional plugin code, settings, REST/AJAX, and architecture.
- `wordpress-scss-review` — reviews SCSS architecture and frontend styling quality.

## How To Use

1. Copy `.agents/` and the core standards files into a WordPress project, or keep this repository as a reusable reference.
2. Let the assistant match the task to the narrowest skill.
3. Provide the exact files/folders or feature scope to analyze.
4. For broad audits, allow the skill's inventory script to produce a deterministic file list.
5. Review proposed changes before implementation when the active skill uses an approval gate.

## Progressive Disclosure

The toolkit deliberately keeps `SKILL.md` files short. The assistant should load:

- `SKILL.md` on activation.
- `references/project-standards.md` when repository conventions matter.
- `references/detailed-checklist.md` for deep/exhaustive work.
- `scripts/` when deterministic inventory is useful.

This keeps routine tasks from paying the context cost of the entire WordPress standards library.

## Customizing For A Project

Edit the core standards first:

- `project-context.md` — real project/domain assumptions.
- `architecture.md` — actual theme/plugin folders and ownership boundaries.
- `coding-standards.md` — project-specific conventions.
- `style-guide.md` — design tokens and component rules.
- `wordpress-best-practices.md` — project-specific WordPress requirements.

Keep customizations explicit and minimal so the toolkit remains portable.
