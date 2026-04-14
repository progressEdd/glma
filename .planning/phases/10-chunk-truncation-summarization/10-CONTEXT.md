# Phase 10: Chunk Truncation for Summarization - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary

`glma index --summarize` completes without errors regardless of chunk sizes or model context window. Oversized chunks are handled gracefully — tried first, then decomposed if they exceed the provider's limits. No new CLI commands, no new chunking logic, no schema changes. Purely making the existing summarization pipeline robust.

</domain>

<decisions>
## Implementation Decisions

### Try-first, decompose-on-failure strategy
- **D-01:** Send every chunk as-is first. Do not pre-truncate or pre-split. Most chunks fit fine.
- **D-02:** If the provider returns a context-length error (e.g., 400 from OpenAI-compatible API), catch it and decompose rather than failing the entire run.
- **D-03:** Decomposition strategy depends on chunk type:
  - **Class chunk with method children** → summarize each method individually first, then send a second request with the class header (docstring, class variables, decorators) + the method summaries as input. The LLM writes the class summary from component summaries rather than raw source.
  - **Standalone oversized chunk** (large function, or class without extracted methods) → map-reduce: split content into overlapping segments, summarize each, combine into final summary.
- **D-04:** Decomposition is triggered by failure, not by pre-calculation. No upfront token counting or sorting needed in the happy path.

### Auto context sizing (when tiktoken available)
- **D-05:** When tiktoken is installed (part of `[ai]` extras alongside `openai`), auto-detect the provider's max context length by querying the `/models` endpoint. Calculate available budget: `max_context - system_prompt_tokens - context_metadata_tokens`.
- **D-06:** Use tiktoken to tokenize chunk content. If the chunk fits within budget, send as-is. If not, the try-first approach still applies — the token check is a proactive optimization to avoid wasted API calls, but the decomposition logic is the same fallback.
- **D-07:** If the `/models` endpoint doesn't expose context length, fall back to a configured default (`max_chunk_chars` as character budget).

### Manual mode (when tiktoken unavailable)
- **D-08:** When tiktoken is not installed, use character-based estimation (~4 chars/token). Compare against `max_chunk_chars` config value (default 3000 chars ≈ 750 tokens).
- **D-09:** Character-based mode still uses the same try-first / decompose-on-failure strategy — the config value is a hint for logging warnings, not a hard cutoff. The actual hard limit is whatever the provider rejects.

### Config surface
- **D-10:** Add `max_chunk_chars` to `SummarizeConfig` (default 3000). Used in manual mode and as fallback when auto context sizing can't determine model limits.
- **D-11:** Add `--max-chunk-chars` CLI flag to `glma index` as per-run override.
- **D-12:** Auto context sizing is on by default when tiktoken is available. No separate config toggle needed — presence of tiktoken enables it.

### Logging
- **D-13:** When a chunk triggers decomposition, log a warning with chunk ID and original size.
- **D-14:** When decomposition succeeds, log an info message confirming the chunk was summarized via decomposition.
- **D-15:** When decomposition also fails (e.g., even segments are too large), log the failure and skip the chunk (same as current behavior for failed summarizations).

### Integration points
- **D-16:** Decomposition happens inside `summarize_chunks()` in `pipeline.py`. The function catches provider errors, checks if the chunk has method children (via `parent_id` relationships), and either does class-decompose or map-reduce.
- **D-17:** Notebook summarization (Phase 9 path) also needs protection — but notebook cells are typically small. The planner should assess whether the shared truncation logic needs to be called there or if it's unnecessary for cells.

### Agent's Discretion
- Exact overlap size for map-reduce segments
- How to extract "class header" content (everything before first method, or parse the AST)
- Whether to summarize class-level string variables (like prompt templates) or strip them as non-code noise
- How to combine map-reduce segment summaries (concatenate + ask LLM for final? or just concatenate?)
- Whether to add a retry with simpler prompt before decomposing

</decisions>

<specifics>
## Specific Ideas

- The ag2-framework `AgentBuilder` class is the canonical test case: 32,475 chars, ~8,118 tokens. Contains 11 methods (75-6,965 chars each) and ~4,896 chars of class-level content (docstring, prompt template strings, class variables). The prompt template strings alone are large but aren't code logic — the LLM doesn't need to read them to summarize what the class does.
- Class-level string variables with long prompt templates (like `GROUP_CHAT_DESCRIPTION`, `CODING_AND_TASK_SKILL_INSTRUCTION`) are a significant portion of the bloat. These are data, not logic.
- The decomposition should be invisible to the user — same `chunk.summary` stored in DB, same output in export/query/writer.

</specifics>

<canonical_refs>
## Canonical References

### Source todo (requirements and acceptance criteria)
- `.planning/todos/pending/2026-04-11-truncate-oversized-chunks-before-summarization.md` — Original problem description, error evidence, acceptance criteria

### Summarization pipeline (must read before planning)
- `02-worktrees/glma/src/glma/summarize/pipeline.py` — `summarize_chunks()` function where decomposition logic goes
- `02-worktrees/glma/src/glma/summarize/providers.py` — `SummarizerProvider` protocol, `OpenAICompatibleProvider`, `PiProvider`

### Config models
- `02-worktrees/glma/src/glma/models.py` — `SummarizeConfig` class (lines ~103-119), needs `max_chunk_chars` field
- `02-worktrees/glma/src/glma/cli.py` — `--summarize` flag handling (lines ~47-137), needs `--max-chunk-chars` flag

### Chunk extraction (parent-child relationships)
- `02-worktrees/glma/src/glma/index/chunks.py` — `_walk_chunks()` creates method chunks with `parent_id` linking to class chunk. Planner needs to understand how to look up method children for a given class chunk.

### Prior context (design decisions that constrain this phase)
- `.planning/phases/07-cli-integration-providers/07-CONTEXT.md` — Established single `[summarize]` config section, `SummarizerProvider` protocol, `[ai]` extras group
- `.planning/phases/09-notebook-cell-summarization/09-CONTEXT.md` — Notebook summarization bypasses LadybugStore, calls `provider.summarize()` directly

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `summarize_chunks()` in `pipeline.py` — already has try/except per chunk, already logs failures, already skips and continues. Decomposition fits naturally inside the existing except block.
- `_walk_chunks()` in `chunks.py` — already creates parent_id links from methods to classes. The pipeline can query the store for chunks with `parent_id == class_chunk.id` to find method children.
- `LadybugStore.get_chunks_for_file()` — returns all chunks for a file including both class and method chunks. The pipeline already loads these.

### Established Patterns
- `SummarizerProvider` protocol: `summarize(code: str, context: str) -> str` — decomposition calls this same interface, just with different inputs (class header + method summaries instead of raw source).
- `SummarizeConfig` in `models.py` — new fields follow the same `Field(default=..., description=...)` pattern.
- CLI flag overrides in `cli.py` — `--max-chunk-chars` follows same pattern as `--summarize-provider` / `--summarize-model`.

### Integration Points
- `summarize_chunks()` is called from `cli.py` line ~137 after indexing completes, once per file. Decomposition happens within this call — no CLI changes needed for the decomposition logic itself.
- Notebook path (`compact_notebook()` in `query/notebook.py`) calls `provider.summarize()` directly, not through `summarize_chunks()`. Planner should assess if this path needs protection (cells are typically small but could theoretically be large).

### Key data point for planning
AgentBuilder class chunk structure:
```
Total: 32,475 chars (~8,118 tokens)
├── Class-level: 4,896 chars (~1,224 tokens) — docstring, prompt templates, class vars
└── Methods: 27,579 chars (~6,894 tokens) across 11 methods
    ├── build_from_library: 6,965 chars (1,741 tokens)
    ├── build: 5,325 chars (1,331 tokens)
    ├── _create_agent: 4,936 chars (1,234 tokens)
    ├── __init__: 3,618 chars (904 tokens)
    └── 7 more methods (71-2,583 chars each)
```

</code_context>

<deferred>
## Deferred Ideas

- Pre-emptive token counting to avoid wasted API calls on oversized chunks (optimization, not essential for robustness)
- Stripping class-level string variables (prompt templates) as non-code noise before summarization (related but separate concern — could be its own improvement)
- Configurable decomposition strategy (let users choose between map-reduce and class-decompose) — over-engineering for now

</deferred>

---

*Phase: 10-chunk-truncation-summarization*
*Context gathered: 2026-04-14*
