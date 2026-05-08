# Phase 13: Embedding Infrastructure - Research

**Researched:** 2026-05-08
**Status:** Complete

## Research Question

"What do I need to know to PLAN this phase well?"

## Findings

### 1. Existing Provider Pattern (Canonical Reference)

The codebase already has a mature provider pattern from Phase 7/12 that Phase 13 mirrors exactly:

**Protocol** (`summarize/providers.py`):
- `SummarizerProvider` Protocol with single method `summarize(code, context) -> str`
- `OpenAICompatibleProvider` class: constructor takes `(base_url, model)`, uses `from openai import OpenAI` with optional dep handling (`pip install glma[ai]`)
- Creates `OpenAI` client with `api_key="not-needed"` (local models)
- Calls `self._client.chat.completions.create(...)` for chat completions

**Config Model** (`models.py`):
- `SummarizeConfig(BaseModel)` with fields: `enabled`, `provider`, `model`, `base_url`, `max_chunk_chars`, `model_hint`, `custom_providers`
- `SummarizeProvider(str, Enum)` with `LOCAL` and `PI` values
- `PROVIDER_PRESETS: dict[str, dict[str, str]]` mapping preset names to `{base_url, model}`
- 7 built-in presets: local, pi, ollama, lmstudio, llamacpp, vllm, aphrodite

**Config Loading** (`config.py`):
- `load_summarize_config(repo_root, cli_overrides)` pattern:
  1. Read `.glma.toml` → extract `[summarize]` section
  2. Merge CLI overrides (non-None values)
  3. Extract custom providers from `[summarize.providers]` subtable
  4. Merge custom providers with built-in `PROVIDER_PRESETS`
  5. Resolve provider preset → fill `base_url` and `model` defaults
  6. CLI explicit flags override preset values
  7. Return `SummarizeConfig(**merged)`

**Implication for Phase 13:** The embedding infrastructure follows this pattern identically. The key mapping is:
- `SummarizerProvider` → `EmbeddingProvider`
- `OpenAICompatibleProvider` → `OpenAIEmbeddingProvider`
- `SummarizeConfig` → `SearchConfig`
- `PROVIDER_PRESETS` → `EMBEDDING_PROVIDER_PRESETS`
- `load_summarize_config()` → `load_search_config()`

### 2. OpenAI Embeddings API

The OpenAI Python client's embeddings API differs from chat completions:

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="not-needed")

# Batch embedding - native list input
response = client.embeddings.create(
    model="qwen3-embedding",
    input=["text1", "text2", "text3"],
)

# Each result has .embedding (list[float])
vectors = [item.embedding for item in response.data]
# vectors = [[0.1, -0.2, ...], [0.3, 0.4, ...], ...]
```

**Key differences from chat completions:**
- Endpoint: `/v1/embeddings` (vs `/v1/chat/completions`)
- Client path: `client.embeddings.create(...)` (vs `client.chat.completions.create(...)`)
- Input: `list[str]` native (no messages formatting needed)
- Output: `response.data[i].embedding` → `list[float]` (vs `response.choices[0].message.content` → `str`)
- No system prompt, no max_tokens — just model + input
- `response.data` ordering matches input ordering

**Server compatibility:**
- Ollama: supports `/v1/embeddings` with any embedding model
- LM Studio: supports `/v1/embeddings` with loaded embedding model
- llama.cpp server: supports `/v1/embeddings`
- vLLM: supports `/v1/embeddings`
- All use same `client.embeddings.create()` call

### 3. File Organization Decision

**Option A: New `embedding/` module** (parallel to `summarize/`)
```
src/glma/embedding/
    __init__.py
    providers.py    # EmbeddingProvider protocol + OpenAIEmbeddingProvider
```

**Option B: Add to existing files**
```
models.py      # Add SearchConfig, EMBEDDING_PROVIDER_PRESETS
config.py      # Add load_search_config()
```

**Recommendation: Option A for providers, Option B for config.** This matches the existing pattern:
- `summarize/providers.py` has its own module for provider protocol + implementation
- `models.py` holds all Pydantic config models (already has SummarizeConfig, ExportConfig, etc.)
- `config.py` holds all config loading functions (already has load_summarize_config, load_config, etc.)

New files needed:
- `src/glma/embedding/__init__.py`
- `src/glma/embedding/providers.py`

Modified files:
- `src/glma/models.py` — add `SearchConfig`, `EMBEDDING_PROVIDER_PRESETS`
- `src/glma/config.py` — add `load_search_config()`

### 4. Provider Preset Details

From CONTEXT.md decisions (D-13, D-14), embedding presets are prefixed with `embed-` to distinguish from summarization presets:

| Preset | base_url | model | Notes |
|--------|----------|-------|-------|
| `embed-ollama` | `http://localhost:11434/v1` | `qwen3-embedding` | Ollama default embedding model |
| `embed-lmstudio` | `http://localhost:1234/v1` | `ENOSYS/Octen-Embedding-8B-750-v1-GGUF` | Specific LM Studio model |
| `embed-vllm` | `http://localhost:8000/v1` | `default` | vLLM default |
| `embed-llamacpp` | `http://localhost:8080/v1` | `default` | llama.cpp server |
| `embed-local` | `http://localhost:1234/v1` | `default` | Raw/manual, same as lmstudio URL |

**Preset resolution** follows the same priority as summarization:
1. `--embedding-provider <preset>` fills defaults (base_url + model)
2. `--embedding-base-url` overrides URL
3. `--embedding-model` overrides model name
4. Explicit flags always win

### 5. SearchConfig Validation Requirements

From CONTEXT.md (D-11), the Pydantic model needs:

- `enabled: bool = False`
- `embedding_provider: str = "embed-local"` (string, not enum — mirrors how summarize resolves to "local")
- `embedding_model: str = "default"`
- `embedding_base_url: str = "http://localhost:1234/v1"`
- `vector_dimensions: int > 0` (Phase 13 field)
- `similarity_threshold: float` in `[0, 1]` (Phase 15 field, needs default)
- `hybrid_keyword_weight: float` (Phase 15 field, needs default)
- `hybrid_vector_weight: float` (Phase 15 field, needs default)
- `custom_providers: dict[str, dict[str, str]]` (same as SummarizeConfig)

**Validation constraints:**
- `vector_dimensions > 0` (Pydantic `Field(ge=1)`)
- `similarity_threshold` in `[0, 1]` (Pydantic `Field(ge=0, le=1)`)
- Weights sum to ~1.0 (model validator)
- Phase 15 fields have defaults that satisfy constraints even when not configured

### 6. Test Patterns

Existing test structure (`tests/test_providers.py`, `tests/test_config.py`):

**Provider tests** use `unittest.mock.patch.dict("sys.modules", {"openai": ...})` to mock the OpenAI package since it's an optional dependency. Pattern:
- Mock `OpenAI` class → returns mock client
- Mock client's API method → returns mock response
- Assert constructor called with correct args
- Assert API method called with correct params
- Assert return value matches expected

**Config tests** use `tmp_path` fixture to create `.glma.toml` files:
- Test defaults (no config file)
- Test file loading
- Test CLI overrides
- Test preset resolution
- Test custom providers from TOML

**Phase 13 needs** analogous test files:
- `tests/test_embedding_providers.py` — tests for `EmbeddingProvider` and `OpenAIEmbeddingProvider`
- Additions to `tests/test_config.py` — `TestSearchConfig` class with preset resolution tests

### 7. No New Dependencies

Phase 13 adds **zero** new dependencies:
- `openai` package already optional (`pip install glma[ai]`)
- `real-ladybug` already in dependencies (vector support comes in Phase 14)
- No new Python packages needed

### 8. Risks and Edge Cases

1. **openai package version:** The `client.embeddings.create()` API is stable since openai>=1.0. No version pin needed.

2. **Embedding dimension mismatch:** Different models produce different dimension vectors (e.g., 768, 1024, 1536). The `vector_dimensions` config field handles this — it's user-configured to match their model. Phase 14 will store vectors with this dimension.

3. **Empty batch handling:** `embed([])` should return `[]`. The OpenAI API likely rejects empty input, so the provider should handle this edge case.

4. **Large batch size:** Local embedding models may have batch size limits. The provider should not implement chunking in Phase 13 — callers handle batch sizes.

5. **SearchConfig weight validation timing:** The hybrid weight validator only matters when both weights are set. Phase 13 sets defaults (0.5/0.5) but Phase 15 is when they're actively used.

## RESEARCH COMPLETE

All domain knowledge gathered. Phase 13 is a pattern-replication phase — the existing summarization provider/config pattern provides an exact template. No novel architecture or unfamiliar integrations.
