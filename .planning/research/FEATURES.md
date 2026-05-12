## Feature Categories

### Pipeline Reliability
- **Purpose:** make `glma index`/`glma embed` restartable and interruption-safe.
- **Expected behavior:** each file advances through persisted stages (e.g. discovered → chunked → relationships → markdown → embeddings → complete); reruns skip completed work and resume from the first incomplete stage.
- **Typical mechanics:** checkpoint state in Ladybug or `.glma-index/`; idempotent writes; atomic per-file commits; graceful shutdown on SIGINT/SIGTERM; retry failed units on rerun.
- **Scope for this milestone:** resume/checkpoint, C chunk ID collision fix, per-file markdown regeneration, visible progress.

### LLM Query Rewriting
- **Purpose:** improve search recall by rewriting user intent into codebase-language terms before retrieval.
- **Expected behavior:** keep the original query for logs/debug; send a rewrite prompt to the existing LLM provider; use rewritten text as the actual search input.
- **Typical rewrite rules:** expand vague terms, normalize synonyms, add likely code tokens (function/class/module names, acronyms, file concepts), keep meaning intact, avoid inventing facts.
- **Good behavior:** concise rewrite, no answer generation, no citations, no multi-step reasoning output, deterministic-ish prompt contract.

### Extended Language Support
- **Purpose:** add tree-sitter coverage for C++, TypeScript, and Rust without changing the indexing architecture.
- **Expected behavior:** detect language from file extension, select the proper grammar, chunk the file, extract language-appropriate relationships, and attach comments/docstrings where feasible.
- **Typical mechanics:** add grammars + parser registration + node-type maps; reuse existing chunk/storage/export/query pipeline; tune comment attachment per language syntax.
- **Important note:** this is mostly wiring and mapping, not a new parsing engine.

### 3-Way Hybrid Search
- **Purpose:** combine graph evidence with keyword and vector retrieval.
- **Expected behavior:** search ranks chunks using a combined score from:
  1. fuzzy keyword similarity on summaries,
  2. vector similarity on embeddings,
  3. graph proximity / relationship evidence from Ladybug traversals.
- **Typical mechanics:** retrieve candidates from vector + keyword + graph paths, normalize each score to a common range, then combine with configurable weights and threshold filtering.
- **Graph signal examples:** direct calls/imports/inheritance/include links, hops from a seed chunk, depth-decayed relationship strength.

## Table Stakes (must have)
- Persisted checkpoint/stage state per file.
- Safe rerun after interrupt without duplicating work.
- Query rewrite step that preserves original query.
- Support for C++, TypeScript, Rust grammars.
- 3 signals in search: graph + keyword + vector.
- Score normalization and thresholding.
- No change to existing `glma query` semantics unless explicitly invoked.

## Differentiators (nice to have)
- Rewrite prompt tuned for code search intents (e.g. "where is auth wired up?").
- Depth-aware graph decay instead of binary graph hits.
- Rebuild/revalidate indexes automatically after embeddings change.
- Per-language relationship refinements (TS imports, Rust modules, C++ namespaces/templates).
- Human-readable checkpoint summaries and progress checkpoints.
- Fallback modes for keyword-only or vector-only search when one signal is unavailable.

## Anti-features (explicitly exclude)
- No new orchestration framework (Prefect/Dagster/Celery/Temporal).
- No new database/search system (SQLite/Postgres/Elastic/Neo4j/FAISS/LanceDB).
- No remote/cloud rewrite service; reuse existing local/OpenAI-compatible provider path.
- No reranker stage for this milestone.
- No language-server/compiler dependency for parsing.
- No auto-embedding during search.
- No MCP server in this milestone.

## Complexity Assessment
- **Pipeline reliability:** medium-high. Hard part is partial-failure safety and making every stage idempotent.
- **LLM query rewriting:** medium. Mostly prompt + wiring, but needs guardrails so rewrites stay faithful.
- **Extended language support:** medium. Grammar wiring is easy; accurate node/relationship mappings are the work.
- **3-way hybrid search:** high. Candidate fusion, score normalization, graph traversal semantics, and result ranking all interact.

## Dependencies on Existing Features
- **Existing summary field + embedding pipeline:** query rewriting and hybrid search both depend on chunk summaries and embeddings already being present.
- **Existing embedding/provider abstraction:** reuse the current summarizer/LLM provider stack for rewrite mode.
- **Existing Ladybug graph schema:** graph search depends on stored chunks and relationships.
- **Existing keyword+vector search:** 3-way hybrid extends the current search foundation.
- **Existing tree-sitter C/Python pipeline:** extended language support should follow the same chunk/extract/store conventions.
- **Existing CLI patterns:** `glma index`, `glma query`, `glma embed`, and config overrides should remain the integration model.
