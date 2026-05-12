## Existing Architecture (do NOT re-architect)
- **Entry path:** `glma` CLI → `glma.index.pipeline.run_index()` → tree-sitter chunker/parser/relationship extractor → `LadybugStore` → markdown writer.
- **Indexing passes:**
  1. chunk + attach comments + store file/chunks + write markdown (no rels)
  2. extract/store outgoing relationships + rewrite markdown
  3. resolve incoming cross-file relationships + final markdown rewrite
- **Storage:** Ladybug graph DB holds `File` nodes, `Chunk` nodes, `CONTAINS` edges, `RELATES_TO` edges, and chunk embeddings/vector index.
- **Summaries:** `summarize_chunks()` uses the existing summarizer provider protocol; summaries persist back into Ladybug.
- **Embeddings:** `embed_chunks()` uses embedding provider presets and stores vectors + hashes in Ladybug.
- **Search:** `HybridSearchEngine.search()` currently merges fuzzy keyword scoring from summaries + vector similarity from Ladybug HNSW.
- **Query output:** `glma query` reads from DB and formats layered markdown / KV / JSON / YAML; notebook queries bypass Ladybug entirely.

## New Components Needed
- **Pipeline checkpoint store**
  - Persist per-file stage state (e.g. discovered, chunked, rels, markdown, embedded, complete).
  - Can live in Ladybug `File` properties or a small sidecar state file under `.glma-index/`.
- **Query rewrite service**
  - A small LLM-backed pre-search rewrite step that rephrases user input into codebase-relevant terms.
  - Should reuse the existing summarizer model/provider path, but as a separate prompt/operation.
- **Language support plugins/config**
  - Add tree-sitter grammars and parser registrations for C++, TypeScript, and Rust.
  - Add language-specific extension and AST node mappings.
- **Graph-aware search expansion**
  - A graph candidate expander/scorer that uses relationship traversal as a third signal.
  - Likely a thin layer over `LadybugStore.traverse_relationships()` and existing relationship getters.

## Modified Components
- **`src/glma/index/pipeline.py`**
  - Read/write checkpoint state per file.
  - Resume from the first incomplete stage instead of redoing all passes.
  - Keep per-file writes idempotent.
- **`src/glma/db/ladybug_store.py`**
  - Add checkpoint persistence helpers and any schema needed for stage state.
  - Expose traversal/scoring helpers for search.
- **`src/glma/models.py`**
  - Extend `Language`, `IndexConfig`, `SearchConfig`, and any checkpoint enums/data models.
- **`src/glma/index/detector.py` / `parser.py` / `chunks.py` / `relationships.py`**
  - Register new grammars and language-specific node handling.
- **`src/glma/search/engine.py`**
  - Insert query rewrite before retrieval when enabled.
  - Add graph signal into ranking.
- **`src/glma/search/formatter.py` and CLI search path**
  - Surface rewritten-query metadata if needed.
  - Preserve existing output formats.

## Data Flow Changes
- **Indexing today:** file → parse/chunk → rels → store → markdown.
- **With checkpoints:** file moves through persisted stages; interrupted runs restart at the first missing stage.
- **With query rewriting:** user query → rewrite prompt/model → rewritten query → keyword/vector/graph retrieval.
- **With extended languages:** detector selects C++/TS/Rust grammars before parse/chunk/rel extraction.
- **With 3-way search:** seed candidates from keyword + vector, then expand/boost via graph neighbors and traverse depth.

## Integration Points
- **CLI**
  - `glma index`: checkpoint/resume flags and progress behavior.
  - `glma search`: rewrite mode flag; graph-depth/weight options if exposed.
  - `glma embed`: should remain compatible with resumed indexes.
- **Pipeline**
  - Pass 1/2/3 boundaries are the natural checkpoint boundaries.
  - Markdown rewrites should stay per-file, not batch-at-end.
- **LadybugStore**
  - Source of truth for file/chunk state, relationships, embeddings, and traversal.
- **Summarizer provider protocol**
  - Reuse for rewrite prompts rather than adding a second LLM stack.
- **Tree-sitter wiring**
  - New grammars plug into `parser.py` and `detector.py` with minimal churn.

## Suggested Build Order
1. **Checkpoint state + resume**
   - Foundation for safe reruns and interrupted indexing.
2. **Chunk ID stabilization**
   - Required before reliable resume/relationship reattachment in large C-like codebases.
3. **Extended language wiring**
   - Add grammars, detection, chunk extraction, and relationship mappings.
4. **Query rewriting**
   - Add opt-in rewrite step using existing summarizer infrastructure.
5. **Graph-aware hybrid search**
   - Extend search scoring once traversal and language coverage are stable.
6. **End-to-end validation**
   - Reindex + resume + rewrite + 3-way search on a representative repo.

## Risk Areas
- **Checkpoint correctness:** partial writes can create mismatched File/Chunk/relationship state if stage boundaries are not atomic.
- **Chunk ID stability:** checkpoints, embeddings, and relationships depend on durable IDs; collisions or ID format changes can break resume.
- **LLM rewrite drift:** rewrites must preserve intent and avoid inventing terms that hurt recall.
- **Grammar nuance:** C++/TypeScript/Rust parsing is mostly wiring, but relationship extraction and comment attachment can still be language-specific.
- **Graph search explosion:** traversal can over-collect results unless depth, fan-out, and score decay are constrained.
- **Reindex compatibility:** new language support and checkpoint metadata must not invalidate existing Ladybug stores unexpectedly.
- **UX regressions:** new flags should not change current `glma query` behavior unless explicitly enabled.
