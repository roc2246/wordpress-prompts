# Agent Skill Review Checklist

Use only for a full skill-architecture audit.

- **Discovery:** valid `SKILL.md`, concise name/description, clear activation boundary.
- **Progressive disclosure:** core workflow only in `SKILL.md`; optional detail in small references.
- **Token efficiency:** no duplicated standards, giant catch-all references, or bulk file-loading instructions.
- **Scripts:** deterministic work belongs in scripts; scripts should return concise results, not whole source files.
- **Portability:** avoid tool-specific assumptions unless the skill requires them; referenced paths must exist.
- **Modularity:** one coherent capability per skill; prefer narrower skills over overlapping mega-skills.
- **Hygiene:** remove stale prompts, generated caches, dead references, and unnecessary assets.
- **Validation:** verify frontmatter, referenced files, script syntax, and final inventory.
