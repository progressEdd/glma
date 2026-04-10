# Architecture Research

**Domain:** CLI codebase indexer with AI summarization
**Researched:** 2026-04-10
**Confidence:** HIGH

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLI (typer)                               │
│  glma index --summarize  |  glma export  |  glma query          │
└──────────┬───────────────┬──────────────┬───────────────────────┘
           │               │              │
┌──────────▼───────────────▼──────────────▼───────────────────────┐
│                    Indexing Pipeline                              │
│  walk → detect → hash → parse → extract → attach → summarize →  │
│  store → write markdown                                          │
└──────────┬──────────────────────────────────────┬───────────────┘
           │                                      │
┌──────────▼──────────┐              ┌────────────▼───────────────┐
│   LadybugStore      │              │   Summarization Pipeline   │
│   (real_ladybug)    │◄─────────────│   (NEW)                    │
│                     │              │                            │
│  Chunk.summary ─────│── write ────►│  Provider Protocol         │
│  (already exists)   │              │  ├─ OpenAICompatibleProvider│
│                     │              │  └─ PiAgentProvider        │
└──────────┬──────────┘              └────────────────────────────┘
           │
┌──────────▼──────────────────────────────────────────────────────┐
│                     Output Layer                                  │
│  writer.py (per-file md)  |  export.py (air-gapped)  |          │
│  query/formatter.py       |  ARCHITECTURE.md (NEW)   |          │
└─────────────────────────────────────────────────────────────────┘
```

## New Components

### 1. Summarization Pipeline (`glma/index/summarizer.py` — NEW)

**Purpose:** Generate AI summaries for chunks and persist to DB.

**Integration points:**
- Called from `pipeline.py` after chunk extraction, before markdown write
- Reads chunks from DB, calls provider, writes `chunk.summary` back
- Incremental: only summarize chunks where `summary` is NULL/empty AND content_hash changed

**Interface:**
```python
class SummarizerProvider(Protocol):
    def summarize(self, code: str, context: str) -> str: ...

class OpenAICompatibleProvider:
    """Works with Ollama, LM Studio, llama.cpp server, any OpenAI-compatible API."""
    def __init__(self, base_url: str, model: str): ...

class PiAgentProvider:
    """Uses pi's API for summarization — no separate model server needed."""
    def __init__(self, model: str): ...

def summarize_chunks(
    store: LadybugStore,
    chunks: list[Chunk],
    provider: SummarizerProvider,
    batch_size: int = 5,
) -> list[Chunk]:
    """Summarize chunks that lack summaries. Returns updated chunks."""
```

**Data flow change:**
- Current: `extract_chunks()` → `summary=None` → store → export generates summary on-the-fly
- New: `extract_chunks()` → store → `summarize_chunks()` → update DB → export reads from DB

**Key insight:** Summarization is a separate pass AFTER indexing, not part of chunk extraction. This keeps the pipeline modular and allows re-summarization without re-indexing.

### 2. Provider Configuration (`glma/models.py` extension)

**New model:**
```python
class SummarizeConfig(BaseModel):
    enabled: bool = False
    provider: str = "local"  # "local" or "pi"
    base_url: str = "http://localhost:1234/v1"
    model: str = "default"
    batch_size: int = 5
```

**Config file integration:** `[summarize]` section in `.glma.toml`

### 3. ARCHITECTURE.md Generator (`glma/export.py` extension)

**Purpose:** Generate codebase-level architecture overview.

**Data sources (all already in LadybugStore):**
- File list with languages and chunk counts
- Cross-file relationships (imports, calls, includes)
- Per-file summaries (rule-based or AI)

**Generated content:**
- Project structure tree (directories, file counts)
- Module dependency graph (who imports whom)
- Entry points (files with no incoming imports)
- Key interfaces (most-referenced functions/classes)

**Integration:** Called from `export_index()` in export.py, generates ARCHITECTURE.md alongside INDEX.md and RELATIONSHIPS.md.

## Modified Components

### `pipeline.py`
- Add summarization pass after relationship extraction (Pass 4)
- Or: make it a separate command `glma summarize` that can run independently
- Incremental: only process chunks where `summary IS NULL OR summary = ''`

### `ladybug_store.py`
- Add `update_chunk_summary(chunk_id: str, summary: str)` method
- Currently `upsert_chunks()` deletes and re-creates — summary would be lost on re-index
- Need either: (a) preserve summary on re-index via content_hash check, or (b) separate update method

### `writer.py`
- Replace placeholder line 274 with actual summary from chunk.summary or rule-based fallback
- Already has access to chunks with summaries

### `export.py`
- `generate_ai_summary()` should READ from DB first (chunk.summary), only call LLM if empty
- `include_code` default changes to `False` in ExportConfig
- Add `_generate_architecture_md()` function

### `models.py`
- Add `SummarizeConfig` model
- Update `ExportConfig.include_code` default to `False`
- Remove "Phase 3" from chunk.summary description

## Build Order

1. **Bug fixes first** (no new components, low risk):
   - ExportConfig.include_code default → False
   - Replace writer.py placeholder
   - Fix notebook truncation

2. **Summarization infrastructure** (new component):
   - Add `update_chunk_summary()` to LadybugStore
   - Create `summarizer.py` with provider protocol
   - Add `SummarizeConfig` to models.py

3. **CLI integration** (wire it up):
   - Add `--summarize` flags to `glma index`
   - Add `glma summarize` standalone command
   - Config file support

4. **Provider implementations**:
   - OpenAICompatibleProvider (refactor from existing export.py code)
   - PiAgentProvider (new)

5. **ARCHITECTURE.md** (uses summaries from DB):
   - Generate from existing relationship data + summaries
   - Add to export output

## Integration Considerations

- **Summary preservation on re-index:** When `upsert_chunks()` deletes and re-creates chunks, summaries are lost. Options: (a) read old summaries before upsert and re-attach to matching chunks by content_hash, or (b) only clear summary if content_hash changed. Recommend option (b).
- **Batch sizing:** Local models have limited concurrent request capacity. Default batch_size=5 with sequential processing is safe.
- **Summary staleness:** If code changes, summary becomes stale. Use content_hash to detect — if hash matches, keep existing summary.

---
*Architecture research for: per-chunk AI summarization with pluggable providers*
*Researched: 2026-04-10*
