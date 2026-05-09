# Requirements: glma

**Defined:** 2026-04-10
**Core Value:** Agents can call a single command and get exactly the code context they need to implement features — no grepping, no raw file parsing, no guesswork.

## v1.1 Requirements

Requirements for Polish & Complete milestone. Each maps to roadmap phases.

### Bug Fixes

- [x] **FIX-01**: Export defaults to summaries-only (ExportConfig.include_code defaults to False) ✓ Phase 5
- [x] **FIX-02**: Notebook cell source truncation fixed for list/dict/set comprehensions ✓ Phase 5
- [x] **FIX-03**: Stale Phase 3 placeholder in writer.py replaced with actual summary (rule-based or AI) ✓ Phase 5

### Summarization Pipeline

- [x] **SUMM-01**: Per-chunk AI summaries generated and persisted to Ladybug DB (chunk.summary field) ✓ Phase 6
- [x] **SUMM-02**: Incremental summarization — only process chunks where summary is NULL/empty ✓ Phase 6
- [x] **SUMM-03**: Summaries appear in export markdown, query output, and writer markdown automatically ✓ Phase 7

### Provider Architecture

- [x] **PROV-01**: SummarizerProvider protocol with summarize(code, context) → str method ✓ Phase 6
- [x] **PROV-02**: OpenAI-compatible provider supporting Ollama, LM Studio, llama.cpp server ✓ Phase 7
- [x] **PROV-03**: Pi agent provider for summarization via pi's API ✓ Phase 7
- [x] **PROV-04**: Summarization configuration in .glma.toml [summarize] section + CLI flags (--summarize, --summarize-provider, --summarize-model) ✓ Phase 7

### Export Enhancement

- [x] **ARCH-01**: ARCHITECTURE.md generated from relationship + summary data and included in exports ✓ Phase 8

### Notebook Summarization

- [x] **NSUMM-01**: `glma query notebook.ipynb --summarize` generates per-cell AI summaries shown in compacted markdown ✓ Phase 9
- [x] **NSUMM-02**: Summaries cached in `.glma-index/notebook-cache/` keyed on cell content hash — unchanged cells not re-summarized ✓ Phase 9
- [x] **NSUMM-03**: `--summarize-provider` and `--summarize-model` flags work for notebook queries (reuse existing provider config) ✓ Phase 9

## v1.3 Requirements

Requirements for Hybrid Semantic Search milestone. Each maps to roadmap phases.

### Embedding Infrastructure

- [ ] **EMB-01**: EmbeddingProvider protocol with `embed(texts: list[str]) -> list[list[float]]` method (batch embedding support)
- [ ] **EMB-02**: OpenAI-compatible embedding provider supporting `/v1/embeddings` endpoint
- [ ] **EMB-03**: Provider presets for `ollama`, `lmstudio`, `vllm`, `llamacpp`, `local` with correct default URLs and models
- [ ] **EMB-04**: Custom embedding providers via `[search.providers]` subtable in `.glma.toml` (merged with built-in presets)
- [ ] **EMB-05**: `[search]` section in `.glma.toml` with `enabled`, `embedding_provider`, `embedding_model`, `embedding_base_url`, `vector_dimensions`, `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`
- [ ] **EMB-06**: SearchConfig model in `models.py` with validation (weights sum to ~1.0, dimensions > 0, threshold 0-1)
- [ ] **EMB-07**: `load_search_config()` in `config.py` following existing pattern (file config + CLI overrides + provider preset resolution)

### Vector Storage

- [ ] **VEC-01**: Ladybug vector index on chunk summary embeddings with configurable dimensions
- [ ] **VEC-02**: Embeddings persisted alongside chunks in Ladybug (chunk.embedding field or separate vector table)
- [ ] **VEC-03**: Incremental embedding — only embed chunks where summary is non-empty and embedding is NULL or summary hash changed
- [ ] **VEC-04**: `glma embed` standalone CLI command to (re-)embed all chunk summaries without re-indexing
- [ ] **VEC-05**: Progress display during embedding (Rich progress bar, consistent with indexing UX)

### Hybrid Search

- [x] **SRCH-01**: Hybrid search combining Ladybug full-text keyword search + vector similarity, with configurable weighting
- [x] **SRCH-02**: `glma query --semantic "<natural language query>"` CLI flag that triggers embedding the query + hybrid search
- [x] **SRCH-03**: Results ranked by combined hybrid score (keyword_weight × keyword_score + vector_weight × vector_score)
- [x] **SRCH-04**: Similarity threshold filtering — results below `similarity_threshold` are excluded
- [x] **SRCH-05**: Query results include relevance score in output (markdown and JSON formats)
- [x] **SRCH-06**: `--search-mode` flag supporting `hybrid` (default), `vector`, `keyword` to force a specific search strategy

## Deferred

### Summarization

- **SUMM-04**: Standalone `glma summarize` command for re-summarization without re-indexing
- **SUMM-05**: Resume after partial failure (skip already-summarized chunks)
- **SUMM-06**: Batch concurrency tuning for parallel model requests

### Future Search

- **SRCH-07**: LLM-based query rewriting for semantic search
- **SRCH-08**: Graph relationship traversal combined with semantic search (3-way hybrid)

### Language Support

- **LANG-01**: C++ support via tree-sitter-cpp
- **LANG-02**: TypeScript support via tree-sitter-typescript
- **LANG-03**: Rust support via tree-sitter-rust

### Integration

- **MCP-01**: MCP server interface for direct agent integration

## Out of Scope

| Feature | Reason |
| ------- | ------ |
| Web UI / dashboard | Agents and humans consume markdown; no visual interface needed |
| Real-time collaboration | Single-user tool, no multi-user sync |
| Custom prompt templates | YAGNI for v1.1 — hardcoded system prompt is sufficient |
| Streaming summaries | Summaries generated offline during indexing, not real-time |
| Summary quality scoring | Overkill; user can see summaries and re-index if bad |
| Cloud embedding providers | Air-gapped philosophy — local models only |
| Custom embedding models/training | Out of scope — use off-the-shelf embedding models |
| Reranking stage | YAGNI for v1.3 — hybrid scoring should be sufficient |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| FIX-01 | Phase 5 | Complete |
| FIX-02 | Phase 5 | Complete |
| FIX-03 | Phase 5 | Complete |
| SUMM-01 | Phase 6 | Complete |
| SUMM-02 | Phase 6 | Complete |
| SUMM-03 | Phase 7 | Complete |
| PROV-01 | Phase 6 | Complete |
| PROV-02 | Phase 7 | Complete |
| PROV-03 | Phase 7 | Complete |
| PROV-04 | Phase 7 | Complete |
| ARCH-01 | Phase 8 | Complete |
| NSUMM-01 | Phase 9 | Complete |
| NSUMM-02 | Phase 9 | Complete |
| NSUMM-03 | Phase 9 | Complete |
| TRUNC-01 | Phase 10 | Complete |
| KV-01 | Phase 11 | Complete |
| KV-02 | Phase 11 | Complete |
| PI-01 | Phase 12 | Complete |
| PI-02 | Phase 12 | Complete |
| EMB-01 | Phase 13 | Pending |
| EMB-02 | Phase 13 | Pending |
| EMB-03 | Phase 13 | Pending |
| EMB-04 | Phase 13 | Pending |
| EMB-05 | Phase 13 | Pending |
| EMB-06 | Phase 13 | Pending |
| EMB-07 | Phase 13 | Pending |
| VEC-01 | Phase 14 | Pending |
| VEC-02 | Phase 14 | Pending |
| VEC-03 | Phase 14 | Pending |
| VEC-04 | Phase 14 | Pending |
| VEC-05 | Phase 14 | Pending |
| SRCH-01 | Phase 15 | ✓ Complete |
| SRCH-02 | Phase 15 | ✓ Complete |
| SRCH-03 | Phase 15 | ✓ Complete |
| SRCH-04 | Phase 15 | ✓ Complete |
| SRCH-05 | Phase 15 | ✓ Complete |
| SRCH-06 | Phase 15 | ✓ Complete |

**Coverage:**
- v1.0 requirements: 15 total (all complete)
- v1.1 requirements: 11 total (all complete)
- v1.2 requirements: 4 total (all complete)
- v1.3 requirements: 18 total
  - EMB: 7 (Phase 13)
  - VEC: 5 (Phase 14)
  - SRCH: 6 (Phase 15)
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-10*
*Last updated: 2026-05-08 after v1.3 milestone definition*
