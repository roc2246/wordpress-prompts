# WordPress Plugin Code Review

## Required Project Context

Before reviewing the code, use the standards and requirements defined in:

- project-context.md
- coding-standards.md
- style-guide.md
- wordpress-best-practices.md
- architecture.md

If any project-specific instructions conflict with generic WordPress advice, prioritize the project files above.

---

## Context

This project may be a custom WordPress implementation with different business and technical requirements.

Review the provided WordPress plugin code.

The plugin may contain:

- Admin pages
- Settings pages
- Custom Post Types
- Custom Taxonomies
- REST API endpoints
- AJAX handlers
- Database interactions
- Third-party integrations
- User management functionality

## Task

Review the code as a senior WordPress developer.

Evaluate:

- WordPress best practices
- Plugin architecture
- Security
- Escaping
- Sanitization
- Validation
- Nonce usage
- Capability checks
- Maintainability
- Reusability
- Performance
- Accessibility
- Naming conventions
- Separation of concerns
- Production readiness

## Return Format

1. Overall Score (1-10)
2. Strengths
3. Major Issues
4. Security Concerns
5. Accessibility Concerns
6. WordPress Best Practice Violations
7. Suggested Improvements
8. Production Readiness

Prioritize:

1. Security
2. Maintainability
3. WordPress standards
4. Reusability
5. Simplicity

Do not recommend unnecessary complexity.
---

## Mandatory Approval Gate

Use a two-phase workflow when the task includes or could lead to repository edits.

### Phase 1: Review and proposal

- Inspect the relevant files and present findings, recommended changes, affected paths, expected benefits, risks, and concise example patches only where they clarify the proposal.
- Do not edit, create, delete, rename, or overwrite project files during Phase 1.
- Do not run mutating project commands during Phase 1. Read-only inspection/validation is allowed.
- Clearly distinguish required fixes from optional improvements.

At the end of Phase 1, stop and ask exactly:

**Would you like me to go forward and apply these changes?**

Do not apply anything until the user explicitly approves.

### Phase 2: Implementation after approval

Apply only the approved changes. Then run relevant existing PHP syntax/static analysis, lint, tests, and asset build commands when available, fix problems caused by the edits, and report every changed file plus validation results.
