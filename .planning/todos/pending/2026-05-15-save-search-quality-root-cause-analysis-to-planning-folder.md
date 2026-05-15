---
created: 2026-05-15T12:00:00Z
title: Save search quality root cause analysis to planning folder
area: planning
files:
  - 02-worktrees/glma/src/glma/search/engine.py
  - 02-worktrees/glma/src/glma/index/relationships.py:37-79
  - 02-worktrees/glma/src/glma/db/ladybug_store.py
  - 02-worktrees/glma/src/glma/search/rewriter.py
---

## Problem

A search for "how does the kernel handle a page fault from allocation to reclaim" against the full Linux kernel codebase produced terrible results:

- All graph scores were 0.00 (the --graph flag did nothing)
- Missing the entire core `mm/` subsystem (mm/memory.c, mm/page_alloc.c, mm/vmscan.c)
- 25+ duplicate `struct mm_struct` entries from arch directories
- No page reclaim coverage at all
- Only arch-specific wrappers surfaced, never the actual implementation

Five root causes identified:

1. **C relationship extraction is file-local only** (`relationships.py` lines 37-79): `_extract_c_calls` only resolves calls within the same file. Cross-file calls like `do_user_addr_fault() → handle_mm_fault() → alloc_pages()` are never linked. Without cross-file edges, BFS traversal from arch wrappers cannot reach `mm/` core. This is why graph=0.00 for everything.

2. **Keyword scoring matches summaries only** (`engine.py` `_fuzzy_score_all`): Uses `fuzz.token_sort_ratio(query, summary)` against LLM-generated summaries. Generic summaries like "Represents a memory page structure" match broadly and score 0.87-0.89, drowning out relevant results.

3. **No chunk deduplication**: Identical `struct mm_struct` declarations from 25+ arch files each become separate chunks with near-identical summaries, spamming results.

4. **Zero-variance normalization** (`engine.py` `_normalize_and_combine_3way`): When all graph scores are 0.0, min-max normalization produces 0/(0+ε)≈0 for every chunk. The graph weight (0.4) is wasted, leaving only 0.3×keyword + 0.3×vector as effective scoring.

5. **No path-aware ranking**: No concept of "core subsystem vs arch wrapper." All chunks compete equally regardless of location in the source tree.

Most impactful fix: #1 (cross-file C call resolution). Without it, the graph feature is fundamentally broken for C codebases.

## Solution

1. Add cross-file C call resolution to `relationships.py` using the LadybugStore to look up function definitions across all indexed files (similar to how `resolver.py` handles Python)
2. Score against content + name + summary, not just summary
3. Deduplicate or collapse identical/near-identical chunks in search results
4. Handle zero-variance normalization gracefully (skip that dimension or redistribute weight)
5. Add optional path-based boosting for core subsystem directories
