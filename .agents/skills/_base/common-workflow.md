# Common Workflow

1. Treat a named directory as a locator, not content to preload.
2. For multi-file work, run the skill inventory script and use its output only as a path index.
3. Read the smallest relevant file set first; expand only when dependencies or evidence require it.
4. Load references only for the issue currently being checked.
5. Never bulk-read an inventory or ask for an entire project attachment when workspace tools can inspect files.
6. Base findings on inspected code; distinguish confirmed issues from suggestions.
7. For edits, change only the requested scope and run available targeted checks.
