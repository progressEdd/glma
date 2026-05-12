# Roadmap: v1.4 — Hardening & Expansion

**Created:** 2026-05-12
**Milestone:** v1.4
**Phases:** 16–20 (5 phases)
**Requirements:** 25 total (PIPE: 6, REWR: 6, LANG: 6, CONF: 1, HYBR: 6)

## Build Order Rationale

1. **Pipeline reliability first** — stable chunk IDs and resume-safe indexing are the foundation everything else depends on. Broken chunk IDs break resume, embeddings, and relationships.
2. **Config relocation** — small, independent change that reduces repo pollution before broader features land.
3. **Extended language support** — broaden coverage once the pipeline is durable and can safely re-index.
4. **LLM query rewriting** — new `glma search` command built on the now-stable provider stack.
5. **3-way hybrid search** — depends on reliable graph data, embeddings, and keyword search all working correctly.

---

## Phase 16 — Pipeline Reliability

**Goal:** Fix chunk ID collisions, add per-file pipeline stage tracking, resume-from-interrupt, graceful shutdown, per-file markdown output, and summarization progress display. This phase establishes the durable indexing foundation that all subsequent features depend on.

### Requirements

| ID | Description |
|----|-------------|
| PIPE-01 | Chunk IDs include content hash to prevent collisions from C macros/forward declarations |
| PIPE-02 | File nodes track pipeline stage (discovered → chunked → relationships_extracted → complete) |
| PIPE-03 | `glma index` resumes from first incomplete stage on re-run, skipping completed work |
| PIPE-04 | Graceful SIGINT/SIGTERM handling — no partial file writes on interrupt |
| PIPE-05 | Markdown regenerated per-file immediately after summarization, not batched at end |
| PIPE-06 | Summarization pass shows Rich progress bar with per-chunk status and counts |

### Success Criteria

1. **No chunk ID collisions:** Running `glma index` on a C codebase with macros and forward declarations produces zero duplicate chunk IDs (verified by uniqueness query on LadybugStore).
2. **Resume works after interrupt:** Interrupting `glma index` mid-pipeline (SIGINT during relationship extraction) and re-running skips already-completed files/stages and picks up where it left off — total indexing time on re-run is proportional to remaining work, not total work.
3. **Clean shutdown on signal:** Sending SIGINT during indexing produces no partial writes — DB state is consistent and markdown files reflect complete pipeline output for all processed files.
4. **Immediate markdown visibility:** After indexing file A and before indexing file B, file A's markdown exists on disk. No batch-at-end behavior.
5. **Visible summarization progress:** Running `glma index --summarize` shows a Rich progress bar with chunk-level status (pending/done/skipped) and running counts throughout the summarization pass.

### Key Implementation Notes

- Chunk ID format changes from `<file>:<name>:<line>` to `<file>:<name>:<line>:<hash8>` — backward-incompatible, requires re-index.
- Per-file stage tracking stored in Ladybug File nodes as a `pipeline_stage` property.
- Resume logic: walk all File nodes, find first with stage != `complete`, continue pipeline from that stage.
- Signal handlers register at CLI entry, use a shared `shutdown_event` that pipeline stages check between files.
- Per-file markdown: move markdown generation into the per-file pipeline loop, after summarization completes for that file.

---

## Phase 17 — Config Relocation

**Goal:** Move the `.glma.toml` config file from the repository root into the `.glma-index/` directory, reducing repo pollution and keeping all glma artifacts in one place.

### Requirements

| ID | Description |
|----|-------------|
| CONF-01 | `.glma.toml` config file lives in `.glma-index/` directory (not repo root) |

### Success Criteria

1. **Config found in new location:** Running `glma index` reads `.glma-index/.glma.toml` and applies its settings. No `.glma.toml` in repo root is consulted.
2. **Backward compatibility path:** If `.glma.toml` exists in repo root but not in `.glma-index/`, a clear warning is printed telling the user to move it. No silent misconfiguration.
3. **Init creates config in correct location:** `glma init` (or first index) creates `.glma-index/.glma.toml` with defaults, not a root-level file.

### Key Implementation Notes

- Update config loader to look in `.glma-index/.glma.toml` instead of `./.glma.toml`.
- Add fallback check with deprecation warning for root-level config.
- Update any documentation and CLI help text referencing config location.

---

## Phase 18 — Extended Language Support

**Goal:** Add C++, TypeScript, and Rust as supported languages with full tree-sitter parsing, relationship extraction, and comment attachment. This is primarily wiring work — the parsing pipeline already handles multi-language via tree-sitter.

### Requirements

| ID | Description |
|----|-------------|
| LANG-01 | C++ files detected and parsed via tree-sitter-cpp grammar |
| LANG-02 | TypeScript files detected and parsed via tree-sitter-typescript grammar |
| LANG-03 | Rust files detected and parsed via tree-sitter-rust grammar |
| LANG-04 | Language-specific node type mappings (namespaces, modules, templates, traits) |
| LANG-05 | Language-specific comment/docstring attachment for each new language |
| LANG-06 | `.glma.toml` and CLI support for language selection/override for new languages |

### Success Criteria

1. **C++ indexed end-to-end:** Running `glma index` on a C++ project (`.cpp`, `.hpp`, `.cc`, `.hxx` files) produces chunks, relationships (includes, calls, class inheritance, namespaces), and markdown output with no errors.
2. **TypeScript indexed end-to-end:** Running `glma index` on a TypeScript project (`.ts`, `.tsx` files) produces chunks, relationships (imports, calls, interface extends, type aliases), and markdown output with no errors.
3. **Rust indexed end-to-end:** Running `glma index` on a Rust project (`.rs` files) produces chunks, relationships (use, calls, trait impls, mod), and markdown output with no errors.
4. **Relationship mappings are language-aware:** C++ namespaces, TypeScript modules, and Rust traits/mods appear as distinct relationship types in query output, not as generic "import" or "call" edges.
5. **Config overrides work:** Setting `languages = ["cpp", "rust"]` in `.glma.toml` or passing `--languages cpp,rust` on CLI restricts indexing to only those languages. Unrecognized language strings produce a clear error.

### Key Implementation Notes

- Add grammar dependencies: `tree-sitter-cpp>=0.23.4`, `tree-sitter-typescript>=0.23.2`, `tree-sitter-rust>=0.24.2`.
- Extend file extension → language mapping in the detector module.
- Add language-specific AST node type maps for: named definitions (functions, classes, structs, enums, traits, interfaces), relationships (calls, imports/uses, inheritance/impl, includes/mods), and comment nodes.
- Comment attachment: C++ uses `//` and `/* */` (same as C), TypeScript uses JSDoc `/** */`, Rust uses `///` and `//!`. Map these per language.
- Language filtering: add `--languages` CLI flag and `[languages]` config section with include/exclude lists.

---

## Phase 19 — LLM Query Rewriting

**Goal:** Add `glma search` command that uses LLM to rewrite user queries into codebase-relevant search terms before running hybrid search. Rewriting uses the existing summarizer provider/model infrastructure.

### Requirements

| ID | Description |
|----|-------------|
| REWR-01 | New `glma search` command — LLM rewrites query by default, then runs hybrid search |
| REWR-02 | `--raw` flag skips LLM rewriting, runs search with raw user query |
| REWR-03 | Rewrite uses existing summarizer provider/model infrastructure |
| REWR-04 | Original query preserved in output for transparency/debugging |
| REWR-05 | Rewrite prompt tuned for code search — expands vague terms, adds likely tokens, preserves intent |
| REWR-06 | `[search]` config section supports `rewrite_prompt` overrides |

### Success Criteria

1. **Search command works with rewriting:** Running `glma search "how does authentication work"` produces a rewritten query (visible in output), runs hybrid search with the rewritten query, and returns ranked results. The rewritten query contains code-relevant terms not in the original.
2. **Raw mode bypasses rewrite:** Running `glma search --raw "authentication"` runs hybrid search with the literal query string, no LLM call, and returns results with a "raw query" label in output.
3. **Original query always visible:** Output includes both the original user query and (when rewritten) the LLM-rewritten query, clearly labeled, for debugging and transparency.
4. **Custom rewrite prompt works:** Setting `rewrite_prompt` in `[search]` config section causes `glma search` to use that prompt instead of the default. Invalid prompt templates produce a clear error at search time.

### Key Implementation Notes

- New CLI entry point: `glma search <query>` with `--raw`, `--top-k`, `--mode` flags.
- Rewrite step: instantiate SummarizerProvider (reuse `--summarize-provider` and `--summarize-model` flags), send query + system prompt, get rewritten query string.
- Default rewrite prompt focuses on: expanding abbreviations, adding likely class/function names, preserving original intent, avoiding hallucinated symbols.
- Output format: header with original + rewritten query, then standard search results.
- `[search]` section in `.glma.toml`: `rewrite_prompt`, `mode` (default hybrid), `top_k`.

---

## Phase 20 — 3-Way Hybrid Search

**Goal:** Unify graph relationship traversal with keyword and vector search into a single configurable 3-way hybrid scoring system. This is the capstone feature that makes `glma search` leverage all three data dimensions.

### Requirements

| ID | Description |
|----|-------------|
| HYBR-01 | Graph relationship traversal returns candidate chunks ranked by proximity to seed |
| HYBR-02 | Search results combine graph, keyword, and vector scores with configurable weights |
| HYBR-03 | Scores normalized to common range before combining |
| HYBR-04 | Graph traversal depth and fan-out are configurable |
| HYBR-05 | `glma search --graph` enables 3-way hybrid mode |
| HYBR-06 | Search output includes score breakdown when 3-way hybrid is active |

### Success Criteria

1. **Graph traversal produces ranked candidates:** Given seed chunks from keyword/vector results, graph traversal via relationship edges (calls, imports, inheritance) returns additional candidate chunks ranked by proximity (BFS depth + edge count decay).
2. **3-way scoring combines correctly:** `glma search --graph "query"` returns results where the final score is a weighted combination of graph proximity, keyword relevance, and vector similarity. Changing weights changes ranking order.
3. **Scores are normalized:** Graph, keyword, and vector scores are each normalized to [0, 1] before combining. No single dimension dominates due to scale differences.
4. **Configurable traversal parameters:** `graph_depth` and `graph_fanout` settings in `[search]` config control how deep/wide graph traversal goes. Default depth=2, fanout=10. Extreme values don't crash or hang.
5. **Score breakdown visible in output:** When `--graph` is active, output shows per-result score breakdown: `graph=0.7, keyword=0.4, vector=0.9, combined=0.67` (or similar). When `--graph` is off, output matches v1.3 format exactly.

### Key Implementation Notes

- Graph search: BFS from seed chunks (found by keyword+vector), follow relationship edges, score by inverse-depth decay.
- Score normalization: min-max normalization per dimension across result set, with smoothing for single-result edge cases.
- Weight config: `[search]` section adds `graph_weight`, `keyword_weight`, `vector_weight` (defaults: 0.4, 0.3, 0.3).
- `--graph` flag is opt-in to preserve existing `glma search` behavior when not specified.
- Deduplication: same chunk may be found via keyword, vector, and graph — merge into single result with combined score.
- Output: extend search result format with optional `scores` dict when `--graph` active.

---

## Coverage Validation

| Phase | Requirements | Count |
|-------|-------------|-------|
| 16 — Pipeline Reliability | PIPE-01, PIPE-02, PIPE-03, PIPE-04, PIPE-05, PIPE-06 | 6 |
| 17 — Config Relocation | CONF-01 | 1 |
| 18 — Extended Language Support | LANG-01, LANG-02, LANG-03, LANG-04, LANG-05, LANG-06 | 6 |
| 19 — LLM Query Rewriting | REWR-01, REWR-02, REWR-03, REWR-04, REWR-05, REWR-06 | 6 |
| 20 — 3-Way Hybrid Search | HYBR-01, HYBR-02, HYBR-03, HYBR-04, HYBR-05, HYBR-06 | 6 |
| **Total** | | **25** |

**Unmapped requirements:** 0 ✓
**Duplicate mappings:** 0 ✓
**Coverage:** 25/25 = 100% ✓

---

## Dependencies

```
Phase 16 (Pipeline Reliability)
  ↓
Phase 17 (Config Relocation)
  ↓
Phase 18 (Extended Language Support)
  ↓
Phase 19 (LLM Query Rewriting)
  ↓
Phase 20 (3-Way Hybrid Search)
```

Phase 16 must be first — stable chunk IDs and resume-safe indexing are prerequisites for reliable re-indexing when new languages are added and when search depends on graph data integrity. Phases 17–18 are sequential but relatively independent of each other. Phases 19–20 build on the stable foundation and each other (search needs rewriting before hybrid scoring).

---
*Roadmap created: 2026-05-12*
