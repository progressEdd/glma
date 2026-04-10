# Requirements: glma

**Defined:** 2026-04-10
**Core Value:** Agents can call a single command and get exactly the code context they need to implement features — no grepping, no raw file parsing, no guesswork.

## v1.1 Requirements

Requirements for Polish & Complete milestone. Each maps to roadmap phases.

### Bug Fixes

- [ ] **FIX-01**: Export defaults to summaries-only (ExportConfig.include_code defaults to False)
- [ ] **FIX-02**: Notebook cell source truncation fixed for list/dict/set comprehensions
- [ ] **FIX-03**: Stale Phase 3 placeholder in writer.py replaced with actual summary (rule-based or AI)

### Summarization Pipeline

- [ ] **SUMM-01**: Per-chunk AI summaries generated and persisted to Ladybug DB (chunk.summary field)
- [ ] **SUMM-02**: Incremental summarization — only process chunks where summary is NULL/empty
- [ ] **SUMM-03**: Summaries appear in export markdown, query output, and writer markdown automatically

### Provider Architecture

- [ ] **PROV-01**: SummarizerProvider protocol with summarize(code, context) → str method
- [ ] **PROV-02**: OpenAI-compatible provider supporting Ollama, LM Studio, llama.cpp server
- [ ] **PROV-03**: Pi agent provider for summarization via pi's API
- [ ] **PROV-04**: Summarization configuration in .glma.toml [summarize] section + CLI flags (--summarize, --summarize-provider, --summarize-model)

### Export Enhancement

- [ ] **ARCH-01**: ARCHITECTURE.md generated from relationship + summary data and included in exports

## v2 Requirements

Deferred to future milestones. Tracked but not in current roadmap.

### Summarization

- **SUMM-04**: Standalone `glma summarize` command for re-summarization without re-indexing
- **SUMM-05**: Resume after partial failure (skip already-summarized chunks)
- **SUMM-06**: Batch concurrency tuning for parallel model requests

### Semantic Search

- **SRCH-01**: Embed chunk summaries with small embedding model
- **SRCH-02**: LLM-based query rewriting for semantic search
- **SRCH-03**: Vector similarity search over embedded summaries
- **SRCH-04**: Hybrid search combining graph relationships + semantic similarity

### Language Support

- **LANG-01**: C++ support via tree-sitter-cpp
- **LANG-02**: TypeScript support via tree-sitter-typescript
- **LANG-03**: Rust support via tree-sitter-rust

### Integration

- **MCP-01**: MCP server interface for direct agent integration
- **PROV-05**: Local model provider presets (--ai-provider ollama/llamacpp/etc.)

## Out of Scope

| Feature | Reason |
| ------- | ------ |
| Web UI / dashboard | Agents and humans consume markdown; no visual interface needed |
| Real-time collaboration | Single-user tool, no multi-user sync |
| Custom prompt templates | YAGNI for v1.1 — hardcoded system prompt is sufficient |
| Streaming summaries | Summaries generated offline during indexing, not real-time |
| Summary quality scoring | Overkill; user can see summaries and re-index if bad |
| Embedding storage | Future milestone (semantic search); Ladybug has vector indices but don't populate yet |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| FIX-01 | Phase 5 | Pending |
| FIX-02 | Phase 5 | Pending |
| FIX-03 | Phase 5 | Pending |
| SUMM-01 | Phase 6 | Pending |
| SUMM-02 | Phase 6 | Pending |
| SUMM-03 | Phase 7 | Pending |
| PROV-01 | Phase 6 | Pending |
| PROV-02 | Phase 7 | Pending |
| PROV-03 | Phase 7 | Pending |
| PROV-04 | Phase 7 | Pending |
| ARCH-01 | Phase 8 | Pending |

**Coverage:**
- v1.1 requirements: 11 total
- Mapped to phases: 11
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-10*
*Last updated: 2026-04-10 after v1.1 milestone definition*
