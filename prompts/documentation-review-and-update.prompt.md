# documentation-review-and-update.prompt.md

## Required Project Context

Before completing this task, use:

* project-context.md
* project-instructions.md
* coding-standards.md
* style-guide.md
* wordpress-best-practices.md
* architecture.md

Prioritize project standards over generic recommendations.

---

# Documentation Review and Update

## Context

This is a WordPress project that should be understandable, maintainable,
and easy to onboard for other developers.

Documentation should help another developer quickly understand:

* What the project does
* How it is structured
* How it is maintained
* Why architectural decisions were made

Documentation should be practical, concise, and maintainable.

---

## Task

Review all provided files and determine whether documentation should be:

* Added
* Updated
* Refactored
* Expanded
* Simplified

Review:

* README files
* PHP docblocks
* Function documentation
* Component documentation
* Theme documentation
* Plugin documentation
* MU-plugin documentation
* SCSS documentation
* Architecture documentation
* Installation instructions
* Setup instructions

---

## Evaluate

### Project Documentation

Check whether documentation clearly explains:

* Project purpose
* Features
* Technology stack
* Installation
* Theme structure
* Plugin structure
* MU-plugin structure
* Development workflow

---

### Code Documentation

Check for:

* Missing docblocks
* Inaccurate comments
* Outdated comments
* Unnecessary comments
* Poorly explained functions
* Poorly explained business logic

---

### Project Handoff Readiness

Determine whether documentation would help:

* A WordPress agency
* A freelance client
* An in-house team
* Another developer maintaining the project

---

## Return Format

### 1. Documentation Score (1-10)

### 2. What Is Already Well Documented

### 3. Missing Documentation

For each item provide:

* What is missing
* Why it matters
* Priority (High / Medium / Low)

### 4. Outdated Documentation

Identify anything that no longer matches the code.

### 5. Suggested Documentation Updates

Provide revised documentation where appropriate.

### 6. README Improvements

Identify improvements that would make the project easier to use and maintain.

### 7. Architecture Documentation Improvements

Identify anything that should be documented about:

* Theme structure
* Components
* Plugins
* MU-plugins
* SCSS architecture
* Build process

### 8. Project Readiness

Would the current documentation make this project appear:

* Professional
* Maintainable
* Production-ready

Explain why.

### 9. Highest Impact Documentation Improvement

If only one documentation task could be completed, what should it be and why?

---

## Documentation Rules

Prefer:

* Clear language
* Concise explanations
* Practical examples
* Accurate documentation
* Maintainable documentation

Avoid:

* Commenting obvious code
* Repeating code in comments
* Excessive documentation
* Documentation that becomes difficult to maintain

Focus on documentation that improves maintainability, onboarding, and handoff quality.

---

## Git Commit Message

If documentation changes are recommended, always provide:

Git commit message: [message]
