# Phase 15: Hybrid Search & Query Integration - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-05-09
**Phase:** 15-hybrid-search-query-integration
**Areas discussed:** Query command structure, Result format & display, Scoring & threshold UX, Search mode fallbacks

---

## Query Command Structure

| Option | Description | Selected |
|--------|-------------|----------|
| `glma query --semantic "text"` | Flag on existing command, overloads positional arg | |
| `glma search "text"` | New top-level command, clean separation | ✓ |
| `glma query --semantic` + `--search` alias | Flag + alias for discoverability | |

**User's choice:** Option 2 — new `glma search` top-level command
**Notes:** Two operations have different inputs (file path vs NL string), different outputs (structured file view vs ranked chunk list), different scopes (single file vs whole codebase). Separate command avoids positional-arg-overloading.

**Follow-up — flag inheritance:**

| Option | Description | Selected |
|--------|-------------|----------|
| Same flags as `query` | --format, --output, --repo, --verbose all work | |
| Subset of flags | --format (json, markdown only), --output, --repo | |
| Agent's discretion | Match obvious ones, decide details in planning | ✓ |

**User's choice:** "Same flags where it makes sense" — inherit the pattern, exact mapping to planning.

---

## Result Format & Display

| Option | Description | Selected |
|--------|-------------|----------|
| Compact hit list | file, chunk name, type, score, one-line summary | |
| Card-style per hit | file heading, chunk name, score, full summary, line range, relationships | |
| Two-tier | Summary table + detailed section | |

**User's choice:** User redirected — summaries are the search medium, results should be **code blocks**. The code is what users/agents actually want.

**Follow-up — metadata per code block:**

| Option | Description | Selected |
|--------|-------------|----------|
| Minimal | file path, chunk name, code | |
| Standard | file path, chunk name, line range, score, code | |
| Standard + summary | file path, chunk name, line range, score, summary, code | |

**User's choice:** Code + summary only. No metadata. If consumer wants line numbers/file details, they can `glma query <file>`.

**Follow-up — file path needed at all?**

| Option | Description | Selected |
|--------|-------------|----------|
| File path as heading only | `# src/auth/login.py` then code blocks | ✓ |
| No file path at all | Pure code + summary blocks | |

**User's choice:** Option 1 — file path as heading. Minimal overhead, essential for follow-up queries.

---

## Scoring & Threshold UX

| Option | Description | Selected |
|--------|-------------|----------|
| Empty output + message | "No results above threshold. Try lowering --similarity-threshold." | ✓ |
| Fallback to top N | Return top 5 below threshold with warning | |
| Agent's discretion | | |

**User's choice:** Option 1 — clean empty state with actionable message. No silent fallback to low-quality results.

---

## Search Mode Fallbacks

**Keyword mode definition — redirected by user:**
Instead of three separate strategies, user proposed unified scoring where "keyword" uses fuzzy matching (fuzzywuzzy-style) rather than exact substring match. Search modes become weight shifts: hybrid=both, vector=vector-only, keyword=fuzzy-only.

**Fuzzy matching implementation:**

| Option | Description | Selected |
|--------|-------------|----------|
| fuzzywuzzy / rapidfuzz | Proven library, token_sort_ratio or similar | ✓ |
| Custom simple fuzzy | Levenshtein or n-gram inline | |
| Agent's discretion | | |

**User's choice:** fuzzywuzzy

**Vector mode without embeddings:**

| Option | Description | Selected |
|--------|-------------|----------|
| Error + message | "No embeddings found. Run `glma embed` first." | ✓ |
| Auto-fallback to keyword | Run keyword search with warning | |
| Agent's discretion | | |

**User's choice:** Option 1 — explicit error. No silent fallback.

---

## Agent's Discretion

- Exact fuzzywuzzy similarity function (token_sort_ratio, partial_ratio, etc.)
- How to structure the search module (new `search/` directory or extend existing)
- Exact result format per output type (json, yaml, markdown, markdown-kv)
- Whether `--similarity-threshold` and `--search-mode` are CLI flags or config-only
- Default number of results (top N, or all above threshold)
- Whether fuzzy matching is Python-side or Cypher-side

## Deferred Ideas

None — discussion stayed within phase scope.
