# Portable WordPress Agent Skills

Copy the entire `.agents` directory into the root of a WordPress workspace. Skills are intentionally small and use progressive disclosure: `SKILL.md` provides activation/workflow guidance, topical `references/` provide deeper context only when needed, and `scripts/inventory.py` performs deterministic file discovery without dumping source contents into the model context.

For project/theme reviews, name or select the target directory; do not attach every child file. The agent should inventory paths and inspect source in small batches.
