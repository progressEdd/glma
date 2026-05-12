# Phase 19: LLM Query Rewriting - Context

**Gathered:** 2026-05-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Add LLM query rewriting to the existing `glma search` command. Before running hybrid search, the user's natural language query is rewritten by the LLM into codebase-relevant terms. Rewriting uses the existing summarizer provider/model infrastructure. Includes `--raw` flag to skip rewriting and `[search]` config section support for custom rewrite prompts.

Requirements: REWR-01 through REWR-06.

No changes to the hybrid search engine (`HybridSearchEngine`), scoring, result ranking, or the `glma query` command. No new CLI commands — `glma search` already exists from Phase 15.

</domain>

<decisions>
## Implementation Decisions

### Rewrite Prompt Design
- **D-01:** Code-aware expansion approach — the LLM returns a single rewritten query string. No structured output, no multi-variant generation.
- **D-02:** The default rewrite prompt must be aware that chunk summaries are 1-2 concise developer-focused sentences covering purpose, inputs, outputs, and key behavior (matching the summarization system prompt in `src/glma/summarize/providers.py`). The rewritten query should use similar natural language — descriptive phrases about what code does, not just symbol names or code syntax.
- **D-03:** The prompt should: expand abbreviations (auth→authentication), add likely descriptive terms that would appear in summaries, preserve technical terms exactly, maintain original intent.
- **D-04:** Return only the rewritten query string — no explanation, no formatting, no preamble.

### Output Transparency
- **D-05:** Show original + rewritten query in a header section above search results, visible in all output formats (markdown, markdown-kv, json, yaml).
- **D-06:** In JSON/YAML output, include `original_query` and `rewritten_query` as fields in the output structure (machine-readable). Markdown formats show the header as text.
- **D-07:** When `--raw` is used, show only the original query with a "raw query" label — no rewritten line.

### Rewrite Failure Handling
- **D-08:** On rewrite failure (timeout, model down, API error): fall back to raw query with a warning on stderr (`"Rewrite failed: {error}. Using raw query."`). Search proceeds with original user query against hybrid search. Does not abort the command.
- **D-09:** Rewrite uses the existing summarizer provider/model infrastructure — same `--summarize-provider`, `--summarize-model`, `--ai-url` flags and `[summarize]` config section that `glma index --summarize` uses. No separate provider/model for rewriting.

### CLI Flag Integration
- **D-10:** Reuse `[summarize]` config section and `--summarize-provider`/`--summarize-model`/`--ai-url` CLI flags for rewrite model selection. No new provider/model flags.
- **D-11:** `--raw` is the only new CLI flag for `glma search`. When present, it skips the LLM rewrite step entirely and passes the raw user query directly to the hybrid search engine — same behavior as today's `glma search`.
- **D-12:** Add `rewrite_prompt` field to `[search]` config section (REWR-06). Empty/unset = use built-in default prompt. Invalid prompt templates produce a clear error at search time.

### Agent's Discretion
- Exact wording of the default rewrite prompt (must follow D-02/D-03/D-04 constraints)
- How to structure the rewrite module (new `search/rewriter.py` or extend `search/engine.py`)
- Whether the rewrite step creates a new `OpenAICompatibleProvider` instance or reuses one
- Exact header formatting for original vs rewritten query display
- `max_tokens` and `timeout` settings for the rewrite LLM call
- Test structure and coverage specifics

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Summarization infrastructure (rewrite reuses this)
- `src/glma/summarize/providers.py` — `OpenAICompatibleProvider` with `summarize()` method, `SYSTEM_PROMPT` that defines summary style (1-2 concise sentences, purpose/inputs/outputs/behavior). The rewrite prompt MUST target this same language style.
- `src/glma/models.py` — `SummarizeConfig` model with `provider`, `model`, `base_url` fields. Rewrite reads from the same config.
- `src/glma/config.py` — `load_summarize_config()` for provider resolution, config loading, CLI override merging.

### Search infrastructure (rewrite feeds into this)
- `src/glma/search/engine.py` — `HybridSearchEngine` with `search(query, mode)` method. Rewrite produces the query string that gets passed here.
- `src/glma/search/formatter.py` — `format_search_output()` and per-format functions. Needs modification to add original/rewritten query header.
- `src/glma/models.py` — `SearchConfig` model with `[search]` config fields. Needs `rewrite_prompt` field added.

### CLI patterns (must follow)
- `src/glma/cli.py` — `search` command (line ~675) with existing flags. Add `--raw` flag and thread summarizer config through for rewrite.

### Prior phase decisions (constraints)
- `.planning/phases/15-hybrid-search-query-integration/15-CONTEXT.md` — Search result format decisions: lean markdown output, file path heading + code blocks, no scores in markdown output, scores in JSON/YAML.

### Requirements
- `.planning/REQUIREMENTS.md` — REWR-01 through REWR-06 (LLM query rewriting requirements)
- `.planning/ROADMAP.md` — Phase 19 success criteria and key implementation notes

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`OpenAICompatibleProvider`** (`summarize/providers.py`): The rewrite step instantiates this same provider with the summarizer model config to call the LLM for query rewriting.
- **`load_summarize_config()`** (`config.py`): Returns `SummarizeConfig` with provider/model/base_url. The rewrite step reads this to know which model to use.
- **`HybridSearchEngine`** (`search/engine.py`): Unchanged — receives the rewritten (or raw) query string and runs hybrid search.
- **`format_search_output()`** (`search/formatter.py`): Needs header section added for original/rewritten query display. Existing per-format functions (`format_search_markdown`, `format_search_json`, etc.) are the modification targets.
- **`SearchConfig`** (`models.py`): Needs `rewrite_prompt` field added. All other fields stay the same.

### Established Patterns
- **LLM provider instantiation**: `OpenAICompatibleProvider(base_url=..., model=...)` — same constructor for summarization and rewriting.
- **LLM call pattern**: `self._client.chat.completions.create(model=..., messages=[...], max_tokens=..., timeout=...)` — standard OpenAI chat completions API.
- **CLI flag pattern**: Typer `@app.command()` with `typer.Option()` flags. Config loaded via `load_*_config()`, CLI overrides merged in.
- **Config loading**: File config + CLI overrides + preset resolution. `load_summarize_config()` pattern to follow for rewrite config access.
- **Output dispatch**: `--format` flag selects formatter function. All formatters receive same data and produce different output.

### Integration Points
- **`cli.py` `search` command**: Add `--raw` flag. Before calling `engine.search()`, conditionally call rewrite step (unless `--raw`). Load summarizer config for rewrite model selection.
- **`search/engine.py`**: No changes needed — it receives a query string and searches. The rewrite happens before the engine call.
- **`search/formatter.py`**: Add original_query/rewritten_query parameters to `format_search_output()` and each per-format function. Add header section in each format.
- **`models.py` `SearchConfig`**: Add `rewrite_prompt: Optional[str]` field.
- **New `search/rewriter.py`** (or similar): Rewrite step — instantiate summarizer provider, call LLM with rewrite prompt, return rewritten query string. Handle failures per D-08.

</code_context>

<specifics>
## Specific Ideas

- The rewrite prompt should produce text that "speaks the same language" as chunk summaries — natural developer English about purpose and behavior, not code syntax or raw symbol lists.
- `--raw` is a clean bypass — no LLM call at all, query goes straight to hybrid search. Useful for debugging, scripted use, or when no model is available.

</specifics>

<deferred>
## Deferred Ideas

None - discussion stayed within phase scope.

</deferred>

---

*Phase: 19-llm-query-rewriting*
*Context gathered: 2026-05-12*
