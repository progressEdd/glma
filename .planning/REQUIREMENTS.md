# Requirements: glma

**Defined:** 2026-05-12
**Core Value:** Agents can call a single command and get exactly the code context they need to implement features — no grepping, no raw file parsing, no guesswork.

## v1.4 Requirements

### Pipeline Reliability

- [ ] **PIPE-01**: Chunk IDs include content hash to prevent collisions from C macros/forward declarations
- [ ] **PIPE-02**: File nodes track pipeline stage (discovered → chunked → relationships_extracted → complete)
- [ ] **PIPE-03**: `glma index` resumes from first incomplete stage on re-run, skipping completed work
- [ ] **PIPE-04**: Graceful SIGINT/SIGTERM handling — no partial file writes on interrupt
- [ ] **PIPE-05**: Markdown regenerated per-file immediately after summarization, not batched at end
- [ ] **PIPE-06**: Summarization pass shows Rich progress bar with per-chunk status and counts

### LLM Query Rewriting

- [ ] **REWR-01**: New `glma search` command — LLM rewrites query by default, then runs hybrid search
- [ ] **REWR-02**: `--raw` flag skips LLM rewriting, runs search with raw user query
- [ ] **REWR-03**: Rewrite uses existing summarizer provider/model infrastructure
- [ ] **REWR-04**: Original query preserved in output for transparency/debugging
- [ ] **REWR-05**: Rewrite prompt tuned for code search — expands vague terms, adds likely tokens, preserves intent
- [ ] **REWR-06**: `[search]` config section supports `rewrite_prompt` overrides

### Extended Language Support

- [ ] **LANG-01**: C++ files detected and parsed via tree-sitter-cpp grammar
- [ ] **LANG-02**: TypeScript files detected and parsed via tree-sitter-typescript grammar
- [ ] **LANG-03**: Rust files detected and parsed via tree-sitter-rust grammar
- [ ] **LANG-04**: Language-specific node type mappings (namespaces, modules, templates, traits)
- [ ] **LANG-05**: Language-specific comment/docstring attachment for each new language
- [ ] **LANG-06**: `.glma.toml` and CLI support for language selection/override for new languages

### Config & Export

- [ ] **CONF-01**: `.glma.toml` config file lives in `.glma-index/` directory (not repo root)

### 3-Way Hybrid Search

- [ ] **HYBR-01**: Graph relationship traversal returns candidate chunks ranked by proximity to seed
- [ ] **HYBR-02**: Search results combine graph, keyword, and vector scores with configurable weights
- [ ] **HYBR-03**: Scores normalized to common range before combining
- [ ] **HYBR-04**: Graph traversal depth and fan-out are configurable
- [ ] **HYBR-05**: `glma search --graph` enables 3-way hybrid mode
- [ ] **HYBR-06**: Search output includes score breakdown when 3-way hybrid is active

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### MCP Server

- **MCP-01**: MCP server interface for direct agent integration
- **MCP-02**: MCP server supports index, query, search, embed operations

## Out of Scope

| Feature | Reason |
| --- | --- |
| Reranking stage | YAGNI for v1.4, 3-way hybrid scoring should suffice |
| MCP server | Deferred to future milestone beyond v1.4 |
| Language server/compiler dependency | Tree-sitter grammars sufficient, no LSP needed |
| Auto-embedding during search | Embedding is a separate concern, run via `glma embed` |
| Cloud embedding/rewrite providers | Air-gapped philosophy, local models only |
| Web UI or dashboard | Agents and humans consume markdown, no visual interface needed |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| PIPE-01 | 16 | Pending |
| PIPE-02 | 16 | Pending |
| PIPE-03 | 16 | Pending |
| PIPE-04 | 16 | Pending |
| PIPE-05 | 16 | Pending |
| PIPE-06 | 16 | Pending |
| REWR-01 | 19 | Pending |
| REWR-02 | 19 | Pending |
| REWR-03 | 19 | Pending |
| REWR-04 | 19 | Pending |
| REWR-05 | 19 | Pending |
| REWR-06 | 19 | Pending |
| LANG-01 | 18 | Pending |
| LANG-02 | 18 | Pending |
| LANG-03 | 18 | Pending |
| LANG-04 | 18 | Pending |
| LANG-05 | 18 | Pending |
| LANG-06 | 18 | Pending |
| CONF-01 | 17 | Pending |
| HYBR-01 | 20 | Pending |
| HYBR-02 | 20 | Pending |
| HYBR-03 | 20 | Pending |
| HYBR-04 | 20 | Pending |
| HYBR-05 | 20 | Pending |
| HYBR-06 | 20 | Pending |

**Coverage:**
- v1.4 requirements: 25 total
- Mapped to phases: 25
- Unmapped: 0 ✓
- Duplicate mappings: 0 ✓

---
*Requirements defined: 2026-05-12*
*Last updated: 2026-05-12 after roadmap creation for v1.4*
