---
created: 2026-04-10T00:00:00Z
title: Replace stale Phase 3 placeholder in writer markdown
area: api
files:
  - 02-worktrees/glma/src/glma/index/writer.py:274
  - 02-worktrees/glma/src/glma/export.py:152
---

## Problem

The per-file markdown generated during indexing by `format_file_markdown()` (writer.py:274) still has a hardcoded placeholder:

```
*(File summary not yet generated — available after Phase 3.)*
```

Phase 3 is long complete. The export pipeline (`export.py:_format_export_file()`) already generates proper rule-based and AI summaries, but the index-time markdown writer was never updated to use them. Any `.glma-index/markdown/` file or agent query hitting `format_file_markdown()` sees this stale text instead of a real summary.

Observed in the wild: `# autogen/token_count_utils.py` shows the placeholder at the top.

## Solution

1. In `writer.py:273-274`, replace the hardcoded placeholder with a call to `generate_rule_summary()` (already exists in export.py, may need to import or extract to a shared location)
2. Pass chunks and relationships through to `format_file_markdown()` (already accepts both params)
3. Alternatively, generate the summary during indexing and store it on the `FileRecord` model so both writer and export use the same source
