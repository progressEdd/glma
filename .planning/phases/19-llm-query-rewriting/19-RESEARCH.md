# Phase 19: LLM Query Rewriting - Research

**Researched:** 2026-05-12
**Status:** Research complete

## Research Question

What do I need to know to PLAN Phase 19 (LLM Query Rewriting) well?

---

## 1. Existing Infrastructure Inventory

### Summarization Provider (Rewrite Reuses This)

**File:** `src/glma/summarize/providers.py`

- `OpenAICompatibleProvider` — the workhorse for LLM calls
  - Constructor: `OpenAICompatibleProvider(base_url=..., model=...)`
  - Uses `openai.OpenAI` client with `base_url` and `api_key="not-needed"`
  - `summarize(code, context)` → calls `self._client.chat.completions.create(model=..., messages=[...], max_tokens=150, timeout=30.0)`
  - `SYSTEM_PROMPT` defines summary style: "1-2 concise sentences for a developer. Focus on purpose, inputs, outputs, and key behavior."
  - The rewrite prompt MUST target this same language style (per CONTEXT.md D-02)

**Key insight:** The rewrite step can reuse `OpenAICompatibleProvider` directly — same constructor, same API pattern. Just pass a different system prompt and the user query as the user message. No need for a separate provider class.

### Config Loading for Summarizer (Rewrite Reads This)

**File:** `src/glma/config.py`

- `load_summarize_config(repo_root, cli_overrides, config_file)` → returns `SummarizeConfig`
- Provider preset resolution: preset name → `{base_url, model}` from `PROVIDER_PRESETS` + custom providers
- CLI overrides merge pattern: file config → CLI flags win
- The search command already has `--summarize-provider`, `--summarize-model`, `--ai-url` flags on the `index` command, NOT on the `search` command yet

**Key insight:** The search command currently does NOT accept `--summarize-provider`/`--summarize-model`/`--ai-url` flags. These need to be added to the `search` command signature (per D-10: reuse summarizer config and flags for rewrite).

### Search Config Model

**File:** `src/glma/models.py`

- `SearchConfig` has fields: `enabled`, `embedding_provider`, `embedding_model`, `embedding_base_url`, `vector_dimensions`, `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`, `custom_providers`
- **Missing field:** `rewrite_prompt: Optional[str]` — needs to be added (REWR-06)
- The `[search]` config section in `.glma.toml` is loaded by `load_search_config()` in `config.py`

### Search Engine (Unchanged)

**File:** `src/glma/search/engine.py`

- `HybridSearchEngine.search(query, mode)` — takes a query string and runs hybrid search
- No changes needed here — the rewrite happens BEFORE the engine call
- The engine is cleanly decoupled from the query construction

### Search Formatters (Need Header Addition)

**File:** `src/glma/search/formatter.py`

- `format_search_output(results, output_format, query, search_mode)` — dispatches to format-specific functions
- `format_search_markdown(results)` — no query parameter currently
- `format_search_kv(results)` — no query parameter currently
- `format_search_json(results, query, search_mode)` — has query
- `format_search_yaml(results, query, search_mode)` — has query

**Key insight:** The markdown and markdown-kv formatters don't currently receive the query string. Adding the original/rewritten query header requires threading these parameters through `format_search_output()` and into each formatter. The JSON/YAML formatters already have `query` — they just need `original_query`/`rewritten_query` fields added.

### CLI Search Command

**File:** `src/glma/cli.py` — `search()` function (~line 450-560)

Current flags: `query_text`, `--search-mode`, `--format`, `--output`, `--repo`, `--embedding-provider`, `--embedding-model`, `--embedding-base-url`, `--vector-dimensions`, `--similarity-threshold`, `--quiet`

**Missing flags (needed for Phase 19):**
1. `--raw` — skip LLM rewriting (REWR-02)
2. `--summarize-provider` — summarizer provider for rewrite (D-10)
3. `--summarize-model` — model for rewrite (D-10)
4. `--ai-url` — override API URL for rewrite (D-10)

**Current flow in search command:**
1. Validate search_mode, format
2. Resolve repo root
3. Validate index exists
4. Build search overrides, load search config
5. Instantiate embedding provider
6. Create `HybridSearchEngine`
7. Call `engine.search(query_text, mode=search_mode)`
8. Format and output results

**New flow with rewrite:**
1-4. Same
5. Load summarizer config (new) if not `--raw`
6. If not `--raw`: instantiate `OpenAICompatibleProvider` with summarizer config, call rewrite
7. Instantiate embedding provider (same)
8. Create `HybridSearchEngine` (same)
9. Call `engine.search(rewritten_query or raw_query, mode=search_mode)`
10. Format with original+rewritten query header

---

## 2. Default Rewrite Prompt Design

Per CONTEXT.md decisions D-02/D-03/D-04:

- The prompt must produce text matching chunk summary language (1-2 descriptive developer sentences about purpose/behavior)
- Must expand abbreviations (auth→authentication), add likely terms, preserve technical terms, maintain intent
- Return ONLY the rewritten query string

**Recommended default prompt:**

```
You are a code search assistant. Rewrite the user's query to be more effective at matching code documentation and summaries.

Rules:
- Expand abbreviations to full terms (auth → authentication, db → database, cfg → configuration)
- Add likely descriptive terms that would appear in developer-focused code summaries
- Preserve technical terms and exact identifiers (function names, class names, API paths)
- Keep the original intent — do not add unrelated concepts
- Use natural descriptive language about what code does (purpose, behavior, inputs, outputs)
- Return ONLY the rewritten query string, no explanation

User query: {query}
```

This prompt targets the same language space as `SYSTEM_PROMPT` in `providers.py` — developer-focused, purpose/behavior descriptions.

---

## 3. Rewrite Module Structure

**Recommended:** New `src/glma/search/rewriter.py` module (per agent's discretion in CONTEXT.md).

**Why separate from engine.py:**
- `engine.py` handles search scoring — no LLM concerns
- `rewriter.py` handles query transformation — LLM concern
- Clean separation: rewriter takes query + config, returns rewritten string
- Easy to test in isolation with mocked provider

**Recommended rewriter interface:**

```python
class QueryRewriter:
    def __init__(self, provider: OpenAICompatibleProvider, rewrite_prompt: Optional[str] = None):
        ...
    
    def rewrite(self, query: str) -> str:
        """Rewrite query using LLM. Returns rewritten string or raises."""
        ...
```

- Uses `OpenAICompatibleProvider.summarize()` internally (or raw client call) with the rewrite system prompt
- `rewrite_prompt` override from config (REWR-06)
- On failure: returns original query + logs warning (D-08)

**Alternative:** Use `OpenAICompatibleProvider.summarize()` directly by passing the rewrite prompt as context. But this conflates summarization with rewriting. Better to use the raw client in the rewriter.

**Better approach:** Create a simple `rewrite_query()` function that takes the OpenAI client, model, and prompt. This avoids coupling to the `summarize()` method signature which expects (code, context).

```python
def rewrite_query(
    client,  # openai.OpenAI
    model: str,
    query: str,
    system_prompt: str,
    timeout: float = 15.0,
    max_tokens: int = 100,
) -> str:
    ...
```

Or, more practically, just use `OpenAICompatibleProvider` but call `self._client` directly in the rewriter:

```python
def rewrite_query(
    query: str,
    base_url: str,
    model: str,
    rewrite_prompt: Optional[str] = None,
) -> str:
    """Rewrite a user query for better code search."""
    from openai import OpenAI
    client = OpenAI(base_url=base_url, api_key="not-needed")
    ...
```

---

## 4. Output Format Changes

### Markdown/Mardown-KV Format (Header Addition)

Before results, add a query info section:

```markdown
# Query: "how does authentication work"
# Rewritten: "authentication user login session verification credential validation"

[existing results]
```

For raw mode:
```markdown
# Query: "authentication" (raw)

[existing results]
```

### JSON/YAML Format (Fields Addition)

```json
{
  "original_query": "how does authentication work",
  "rewritten_query": "authentication user login session verification credential validation",
  "query": "authentication user login session verification credential validation",
  "search_mode": "hybrid",
  ...
}
```

For raw mode:
```json
{
  "original_query": "authentication",
  "rewritten_query": null,
  "query": "authentication",
  ...
}
```

### Signature Changes to Formatter Functions

All formatter functions need new parameters:
- `format_search_output(results, output_format, query, search_mode, original_query=None, rewritten_query=None)`
- `format_search_markdown(results, original_query=None, rewritten_query=None)`
- `format_search_json(results, query, search_mode, original_query=None, rewritten_query=None)`
- `format_search_yaml(results, query, search_mode, original_query=None, rewritten_query=None)`
- `format_search_kv(results, original_query=None, rewritten_query=None)`

---

## 5. Config Schema Change

### SearchConfig Addition (models.py)

```python
class SearchConfig(BaseModel):
    # ... existing fields ...
    rewrite_prompt: Optional[str] = Field(
        default=None,
        description="Custom system prompt for LLM query rewriting. Empty/unset uses built-in default.",
    )
```

### .glma.toml [search] Section

```toml
[search]
rewrite_prompt = """..."""  # Optional custom rewrite prompt
# ... existing fields
```

### Config Loading Change (config.py)

`load_search_config()` already handles `[search]` section. The `rewrite_prompt` field will be automatically parsed from the TOML since `SearchConfig` will include it.

---

## 6. Error Handling Strategy

Per D-08:
- Rewrite failure → fall back to raw query + stderr warning
- No aborting the search command
- Warning format: `"Rewrite failed: {error}. Using raw query."`

**Implementation approach:**
```python
try:
    rewritten = rewrite_query(query, base_url, model, rewrite_prompt)
except Exception as e:
    sys.stderr.write(f"Rewrite failed: {e}. Using raw query.\n")
    rewritten = None  # signals "no rewrite happened"
```

The formatter checks `rewritten is not None` to decide whether to show the header with both queries or just the raw query label.

---

## 7. Test Strategy

### Unit Tests

1. **Test `rewrite_query()` function:**
   - Mock OpenAI client, verify system prompt + user message construction
   - Verify returns rewritten string on success
   - Verify returns None/falls back on failure
   - Verify custom rewrite_prompt is used when provided

2. **Test formatter header changes:**
   - Markdown format: verify "Query:" and "Rewritten:" headers appear
   - JSON format: verify `original_query` and `rewritten_query` fields
   - YAML format: same as JSON
   - Raw mode: verify only "Query: ... (raw)" appears, no rewritten line
   - Empty results still show query header

3. **Test config model:**
   - `SearchConfig` accepts `rewrite_prompt`
   - Default `rewrite_prompt` is None
   - Custom prompt from TOML loads correctly

4. **Test CLI integration:**
   - `--raw` flag skips rewrite (no LLM call)
   - `--summarize-provider`/`--summarize-model`/`--ai-url` pass through to rewriter
   - `glma search --help` shows new flags

### Integration Tests

5. **End-to-end with mocked LLM:**
   - Mock `OpenAICompatibleProvider`, verify rewritten query reaches `engine.search()`
   - Verify output contains both original and rewritten queries

---

## 8. Dependency and Ordering Analysis

### What Can Be Built in Parallel

- **Wave 1 (Independent):**
  1. `search/rewriter.py` — new module, no dependencies on other changes
  2. `SearchConfig.rewrite_prompt` field + config loading — model change
  3. Formatter header changes — formatter modifications

- **Wave 2 (Depends on Wave 1):**
  4. CLI `search` command integration — ties rewriter, config, and formatters together

### File Modification Summary

| File | Change Type | Description |
|------|------------|-------------|
| `src/glma/search/rewriter.py` | **NEW** | Query rewrite module |
| `src/glma/models.py` | MODIFY | Add `rewrite_prompt` to `SearchConfig` |
| `src/glma/config.py` | MODIFY | Ensure `rewrite_prompt` loaded from `[search]` section (may need no changes if auto-handled) |
| `src/glma/search/formatter.py` | MODIFY | Add query header to all formatters, thread `original_query`/`rewritten_query` params |
| `src/glma/cli.py` | MODIFY | Add `--raw`, `--summarize-provider`, `--summarize-model`, `--ai-url` to search command; integrate rewrite step |
| `tests/test_search.py` | MODIFY | Add tests for rewrite, formatter headers, CLI flags |
| `tests/test_rewriter.py` | **NEW** | Unit tests for rewrite module |

### External Dependencies

- No new Python packages required
- `openai` package already an optional dependency (used by `OpenAICompatibleProvider`)
- All LLM interaction reuses existing infrastructure

---

## 9. Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Rewrite latency slows search | Default timeout 15s, failure falls back to raw query (D-08) |
| Custom rewrite prompt breaks | Validate at search time, clear error message (D-12) |
| Markdown header breaks existing consumers | Header uses `#` heading — consistent with file headings, easy to parse/skip |
| SearchConfig backward compat | `rewrite_prompt` is Optional with default None — no breaking change |
| Provider not available when search needs it | Graceful fallback per D-08, error message guides user |

---

## 10. Key Patterns to Follow

From existing codebase:

1. **LLM provider instantiation:** `OpenAICompatibleProvider(base_url=..., model=...)` — create new instance for rewrite
2. **Config loading:** `load_*_config(repo_root, cli_overrides, config_file)` pattern — use `load_summarize_config()` for rewrite provider config
3. **CLI flag pattern:** `typer.Option(None, "--flag-name", help="...")` for optional overrides
4. **Error handling in CLI:** `sys.stderr.write(...)` for errors, `console.print(...)` for Rich output
5. **Test mocking:** Use `MagicMock` for store/provider, `subprocess.run` for CLI tests
6. **Output format dispatch:** `format_search_output()` routes to format-specific functions

---

## RESEARCH COMPLETE

Phase 19 is well-scoped with clear integration points. The main work is:
1. New rewriter module (~50-80 lines)
2. Config model addition (~5 lines)
3. Formatter modifications (~40 lines across 5 functions)
4. CLI integration (~30 lines)
5. Tests (~150-200 lines)

No architectural risks. All infrastructure exists. The rewrite step is a clean "middleware" between query input and search engine execution.
