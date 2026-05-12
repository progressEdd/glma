## Existing Stack (validated, do NOT re-research)
- Python 3.13+
- `real-ladybug>=0.15.3` (graph DB, native vector index, full-text search)
- `tree-sitter>=0.25.2`
- `tree-sitter-c>=0.24.1`
- `tree-sitter-python>=0.25.0`
- `typer>=0.24.1`, `rich>=14.0`
- `pydantic>=2.12`, `watchfiles>=1.0`, `rapidfuzz>=3.0`, `pyyaml>=6.0`, `nbformat>=5.10`
- Optional AI path already exists via `openai` extra (`glma[ai]`)
- Existing search path: fuzzy keyword + vector search
- Existing summarizer path: local/OpenAI-compatible provider abstraction

## New Dependencies Needed
1. `tree-sitter-cpp>=0.23.4`
2. `tree-sitter-typescript>=0.23.2`
3. `tree-sitter-rust>=0.24.2`

No new third-party package is required for:
- pipeline resume/checkpointing
- LLM query rewriting
- 3-way hybrid search

Those should reuse the current DB, config, and summarizer/provider layers.

## Integration Points
- **Pipeline resume/checkpoint**
  - Add persistent pipeline state to the existing Ladybug-backed index (preferred) or a small JSON state file under `.glma-index/`.
  - Track per-file stage status: walked, parsed, chunks stored, rels stored, markdown written, embeddings done.
  - Make index steps idempotent and restartable; prefer atomic per-file commits over batch-at-end writes.
  - Resume should read checkpoint state, skip completed files, and continue from the first incomplete stage.

- **LLM query rewriting**
  - Add a pre-search rewrite step in `glma search`.
  - Reuse the existing summarizer provider stack (`SummarizeConfig` / `OpenAICompatibleProvider`) instead of introducing a new model client.
  - Keep the original query for logging/debug and use the rewritten query as the search input.
  - Add a small prompt contract (plain text is enough) that rewrites user intent into codebase-relevant terms.

- **Extended language support (C++, TypeScript, Rust)**
  - Extend `Language` enum + extension detection.
  - Add parser wiring in `index/parser.py` for the new tree-sitter grammars.
  - Add chunk/relationship node mappings per language.
  - Update relationship extraction for language-specific call/import/inheritance forms.
  - Comment attachment heuristics should be reused; only language-specific comment syntax may need tuning.

- **3-way hybrid search (graph + keyword + vector)**
  - Extend `SearchConfig` with graph weighting / depth knobs.
  - Expand `HybridSearchEngine` to score graph proximity/relationship evidence alongside fuzzy keyword and vector similarity.
  - Use existing Ladybug relationship traversal (`traverse_relationships`, `get_*_relationships`) as the graph signal source.
  - Keep search output formatters unchanged except for any new score fields.
  - Prefer graph evidence from direct relationships first, then depth-based decay.

## What NOT to Add
- No new database (do not add SQLite, Postgres, Elasticsearch, Neo4j, LanceDB, FAISS, etc.)
- No orchestration framework (Prefect/Dagster/Celery/Temporal) for checkpointing
- No LangChain/LlamaIndex-style abstraction layer
- No remote/cloud embedding or rewriting service
- No external reranker stage
- No language servers or compiler toolchains for parsing
- No separate search index; reuse Ladybug’s vector + FTS + graph capabilities

## Version Recommendations
- Keep `tree-sitter>=0.25.2` aligned with the current parser stack.
- Add the new grammars at these lower bounds:
  - `tree-sitter-cpp>=0.23.4`
  - `tree-sitter-typescript>=0.23.2`
  - `tree-sitter-rust>=0.24.2`
- Keep `real-ladybug>=0.15.3` (already sufficient for graph traversal + vector/FTS use).
- Keep `rapidfuzz>=3.0` for keyword scoring.
- Keep `openai` as the optional AI client; query rewriting should reuse it via the existing `glma[ai]` extra.
- If checkpoint state is stored on disk, use stdlib only (`json`, `pathlib`, `tempfile`) so no versioned dependency is needed.
