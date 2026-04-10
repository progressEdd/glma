# Feature Research

**Domain:** CLI codebase indexer with AI summarization
**Researched:** 2026-04-10
**Confidence:** HIGH

## Feature Landscape

### Table Stakes (Users Expect These)

| Feature | Why Expected | Complexity | Notes |
| ------- | ------------ | ---------- | ----- |
| Per-chunk summaries | File-level summaries exist but are too coarse; agents need function/method-level understanding to answer "what does this function do?" | Medium | chunk.summary field exists in DB, just needs population |
| Summaries persist across runs | If summaries are generated once, they should survive re-export without re-calling the LLM | Low | Ladybug DB already has summary field, just need write-through |
| Summaries flow to all outputs | Once generated, summaries should appear in export markdown, query output, and writer markdown | Low | All output paths already read chunk.summary from DB |
| Configurable model | Users have different local models (Ollama, LM Studio, llama.cpp); shouldn't be hardcoded to one | Low | OpenAI-compatible API already works with all of these |
| Summaries-only export | Agents consuming markdown don't need full source code by default | Trivial | Just flip include_code default to False |

### Differentiators

| Feature | Why It Matters | Complexity | Notes |
| ------- | -------------- | ---------- | ----- |
| Pluggable provider architecture | pi agent integration means agents can summarize code they index — no separate model server needed | Medium | Protocol/ABC pattern, OpenAI-compatible + pi as two backends |
| ARCHITECTURE.md generation | Codebase overview file gives agents instant high-level understanding without reading every file | Medium | Derived from existing relationship data + file-level summaries |
| Incremental summarization | Only summarize new/changed chunks on re-index, not entire codebase every time | Medium | Leverage existing content_hash comparison in pipeline |
| Batch summarization | Rate-limited batched calls to avoid overwhelming local models | Low | Simple chunk batching with configurable concurrency |

### Anti-Features (Do NOT Build)

| Feature | Why Not |
| ------- | ------- |
| Embedding storage | Future milestone (semantic search); Ladybug has vector indices but don't populate yet |
| Query rewriting | Depends on embeddings, future milestone |
| Custom prompt templates | YAGNI for v1.1 — hardcoded system prompt is fine |
| Streaming summaries | Summaries are generated offline during indexing, not real-time |
| Summary quality scoring | Overkill; user can see summaries and re-index if bad |

### Bug Fixes (Table Stakes)

| Bug | Impact | Complexity | Notes |
| --- | ------ | ---------- | ----- |
| Notebook cell source truncation | List comprehensions stripped from cells, losing code | Medium | Tree-sitter or regex truncation issue in notebook.py |
| Stale Phase 3 placeholder | Writer output shows "not yet generated" for file summaries | Trivial | Replace with actual rule-based or AI summary |
| include_code defaults True | Export includes full source by default, bloating output | Trivial | Flip ExportConfig default |

## Feature Categories for v1.1

1. **Bug Fixes** — Include code default, notebook truncation, stale placeholder
2. **Summarization Pipeline** — Per-chunk AI summaries with persistence
3. **Provider Architecture** — Pluggable model providers (local + pi)
4. **Export Enhancement** — ARCHITECTURE.md generation

---
*Feature research for: per-chunk AI summarization with pluggable providers*
*Researched: 2026-04-10*
