# WordPress MU-Plugin Review

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

Review the provided WordPress MU-plugin (Must Use Plugin).

Assume the code contains site-wide functionality that automatically loads for every request.

The MU-plugin may contain:

- Business logic
- Custom integrations
- Security functionality
- Custom authentication
- API integrations
- Utility functions
- Content restrictions
- Admin customizations
- Performance optimizations
- Site-wide hooks and filters

## Task

Review this MU-plugin as a senior WordPress developer.

Evaluate:

- Architecture
- Separation of concerns
- Maintainability
- Security
- Scalability
- Hook usage
- Filter usage
- Namespacing
- Dependency management
- Error handling
- Performance
- Production readiness

## Return Format

1. Overall Score (1-10)
2. What Is Good
3. Major Concerns
4. Security Concerns
5. Architecture Concerns
6. Performance Concerns
7. Suggested Refactoring
8. Production Readiness

Review for:

- Escaping
- Sanitization
- Validation
- Capability checks
- Hook design
- Reusability
- Long-term maintainability

Prioritize:

1. Maintainability
2. Security
3. Reliability
4. Simplicity
5. Reusability

Flag anything that would become difficult to maintain over time.

Do not recommend enterprise architecture unless justified.
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
