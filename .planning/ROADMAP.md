# Roadmap: glma v1.3 — Hybrid Semantic Search

## Overview

Add hybrid keyword + vector search on chunk summaries so agents can find relevant code by meaning, not just exact matches. Embedding providers generate vectors from summaries, Ladybug stores and searches them, and `glma query --semantic` returns hybrid-ranked results.

## Phases

**Phase Numbering:**
- Continues from v1.2 (Phases 10-12)
- v1.3 starts at Phase 13

- [x] **Phase 13: Embedding Infrastructure** - Provider protocol, presets, config, .glma.toml [search] section
- [x] **Phase 14: Vector Storage & Embedding Command** - Ladybug vector index, `glma embed`, incremental embedding
- [ ] **Phase 15: Hybrid Search & Query Integration** - Hybrid keyword+vector search, `--semantic` flag, result ranking

## Phase Details

### Phase 13: Embedding Infrastructure
**Goal**: Any local embedding provider can generate vectors from text via a unified protocol
**Depends on**: v1.2 complete (Phase 7 provider pattern, Phase 10 chunk summaries)
**Requirements**: EMB-01, EMB-02, EMB-03, EMB-04, EMB-05, EMB-06, EMB-07
**Success Criteria** (what must be TRUE):
  1. EmbeddingProvider protocol exists with `embed(texts: list[str]) -> list[list[float]]` method
  2. OpenAIEmbeddingProvider hits `/v1/embeddings` endpoint and returns float vectors
  3. Provider presets exist for ollama, lmstudio, vllm, llamacpp, local with correct URLs/models
  4. Custom providers merge from `[search.providers]` in `.glma.toml`
  5. SearchConfig model validates: dimensions > 0, threshold 0-1, weights sum to ~1.0
  6. `load_search_config()` resolves provider presets the same way `load_summarize_config()` does
  7. All existing tests still pass

### Phase 14: Vector Storage & Embedding Command
**Goal**: Chunk summary embeddings are stored in Ladybug and can be generated/updated via CLI
**Depends on**: Phase 13 (embedding providers working)
**Requirements**: VEC-01, VEC-02, VEC-03, VEC-04, VEC-05
**Success Criteria** (what must be TRUE):
  1. Ladybug has a vector index on chunk embeddings with configurable dimensions
  2. Embeddings are persisted in Ladybug alongside chunks (embedding column or related table)
  3. `glma embed` generates embeddings for all chunks with non-empty summaries, skipping already-embedded chunks (unless forced)
  4. Incremental embedding detects summary hash changes and re-embeds updated chunks
  5. Rich progress bar displays during embedding (consistent with `glma index` UX)
  6. All existing tests still pass

### Phase 15: Hybrid Search & Query Integration
**Goal**: `glma query --semantic "find authentication logic"` returns hybrid-ranked results
**Depends on**: Phase 14 (embeddings stored in Ladybug)
**Requirements**: SRCH-01, SRCH-02, SRCH-03, SRCH-04, SRCH-05, SRCH-06
**Success Criteria** (what must be TRUE):
  1. Hybrid search combines Ladybug full-text + vector similarity with configurable weights
  2. `glma query --semantic "..."` embeds the query string and runs hybrid search
  3. Results ranked by `keyword_weight × keyword_score + vector_weight × vector_score`
  4. Results below `similarity_threshold` are filtered out
  5. Output includes relevance score in both markdown and JSON formats
  6. `--search-mode hybrid|vector|keyword` forces a specific strategy
  7. All existing tests still pass

## Progress

**Execution Order:**
Phases execute in numeric order: 13 → 14 → 15

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 13. Embedding Infrastructure | 1/1 | ✓ Complete | 2026-05-09 |
| 14. Vector Storage & Embedding Command | 0/? | Not started | — |
| 15. Hybrid Search & Query Integration | 0/? | Not started | — |

## Architecture Overview

```
┌─────────────────────────────────────┐
│         .glma.toml [search]         │
│  provider, model, dimensions,       │
│  threshold, hybrid weights          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      EmbeddingProvider Protocol     │
│  embed(texts) → list[list[float]]   │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
 Ollama    LMStudio    vLLM    ...custom
 (preset)  (preset)    (preset)
               │
               ▼
┌─────────────────────────────────────┐
│     Ladybug Graph Database          │
│  - Chunks (content, summary)        │
│  - Embeddings (vector index)        │
│  - Full-text index                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│        Hybrid Search Engine         │
│  keyword_weight × FT score          │
│  + vector_weight × cosine sim       │
│  → ranked results                   │
└──────────────┬──────────────────────┘
               │
               ▼
     glma query --semantic "..."
     glma embed
```

## Notes

- Ladybug (real_ladybug) has native vector index support — no new database dependency
- Provider presets reuse the exact same pattern as `[summarize]` providers (PROVIDER_PRESETS dict)
- Chunk summaries must exist before embedding — `glma embed` warns if no summaries found
- Embedding happens after indexing, not during — keeps the pipeline decoupled
