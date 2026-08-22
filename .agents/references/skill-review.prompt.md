Go through each Agent Skill in my WordPress prompts project and evaluate whether it follows good Agent Skill design practices.

For each skill:

* Check whether the skill has one clear, specific purpose.
* Check whether the `SKILL.md` contains only the instructions needed on activation.
* Identify information that should move to a reference file because it is contextual, detailed, or only needed sometimes.
* Identify deterministic or repeatable logic that should move to a script instead of being explained in `SKILL.md`.
* Look for duplicated, unnecessary, overly verbose, or redundant instructions that waste context-window tokens.
* Check whether the skill is modular rather than trying to handle unrelated WordPress tasks.
* Check whether the description/frontmatter is specific enough for an agent to know both when to activate and when a narrower skill is more appropriate.
* Check that WordPress-specific security boundaries (validation, sanitization, capabilities, nonces, escaping) live at the correct level rather than being repeated everywhere.
* Keep instructions as LLM-agnostic as reasonably possible.
* Recommend changes that reduce token usage without removing information needed for reliable execution.

For each skill, tell me:

1. What is already good.
2. What should be changed.
3. What should remain in `SKILL.md`.
4. What should move to a reference file.
5. What should move to a script, if anything.
6. Whether the skill should be split or merged.
7. Whether any content can simply be removed.

Prioritize minimal token usage, clear activation criteria, progressive disclosure, modularity, portability, and reliable WordPress-specific behavior.
