---
name: wordpress-explain-code
description: Explain selected WordPress PHP, JavaScript, SCSS, templates, hooks, or project flow in practical terms. Use for walkthroughs, onboarding, learning, or “what does this do?” questions; do not activate for a full code review.
metadata:
  author: riley-childs
  version: "2.0"
---

# Explain WordPress Code

Use `.agents/skills/_base/common-output.md`; this skill is read-only unless the user separately asks for changes.

## Workflow
1. Start from the exact selected/named code. Read adjacent definitions/call sites only when needed to explain behavior accurately.
2. Load `references/explanation-guide.md` only when a deeper walkthrough is requested.
3. Explain WordPress concepts in context rather than reciting generic definitions.
4. Mention security/accessibility/maintainability only when materially relevant to the code being explained.

## Output
Give a plain-English summary, execution/data flow, important WordPress concepts, project relationship, and notable caveats. Keep depth proportional to the user's question.
