## Stack Additions
- Add tree-sitter grammars:
  - `tree-sitter-cpp>=0.23.4`
  - `tree-sitter-typescript>=0.23.2`
  - `tree-sitter-rust>=0.24.2`
- No new DB, queue, reranker, orchestration, or search system is needed.
- Reuse existing Ladybug storage, summarizer/provider stack, and stdlib for checkpoint state if a sidecar file is used.

## Feature Table Stakes

| Category | Must Include |
| --- | --- |
| Pipeline Reliability | Persisted per-file stage state; atomic/idempotent stage writes; safe resume after interrupt; chunk ID stability/collision fix; per-file markdown regeneration; visible progress. |
| LLM Query Rewriting | Opt-in pre-search rewrite using existing provider stack; keep original query for logs/debug; rewritten query becomes retrieval input; rewrite must preserve intent and avoid invention. |
| Extended Language Support | Detect and parse C++, TypeScript, Rust; register grammars; add node/relationship mappings; reuse existing comment attachment where possible; no architecture change. |
| 3-Way Hybrid Search | Combine graph + keyword + vector signals; normalize scores; dedupe candidates; threshold/fallback behavior; preserve existing output formats unless extra score fields are added. |

## Architecture Highlights
- Current flow stays intact: CLI → index pipeline → tree-sitter parse/chunk/relations → LadybugStore → markdown.
- Best checkpoint boundary is per file and per pass: chunked → relationships → markdown → embeddings → complete.
- Resume should continue from the first missing stage, not from the beginning of the file.
- Query rewriting should be a thin pre-search step that reuses the summarizer/provider abstraction.
- Graph search should use Ladybug relationship traversal as a third signal, layered onto existing keyword + vector search.
- Extended languages are mostly parser/detector wiring plus language-specific AST/relationship mappings.

## Watch Out For
- Partial writes and checkpoint drift can leave DB state and in-memory progress out of sync.
- Chunk ID collisions, especially in C-like code, can break resume and relationship reuse.
- Rewrite drift, hallucinated symbols, and over-expansion can hurt retrieval quality.
- Graph traversal can explode candidate counts unless depth/fan-out/decay are constrained.
- Language-specific parsing differences (comments, namespaces, modules, macros/templates) need careful mapping.
- New behavior must not change existing `glma query` semantics unless explicitly enabled.

## Build Order Recommendation
1. **Pipeline reliability first** — establishes safe reruns and stable state, which everything else depends on.
2. **Chunk ID stabilization** — required before resume, embeddings, and relationship reattachment can be trusted.
3. **Extended language support** — add grammars and mappings once the pipeline is durable.
4. **LLM query rewriting** — easier to validate after indexing/search data is stable.
5. **3-way hybrid search** — last, because it depends on reliable summaries, embeddings, and graph data.
6. **Integration hardening** — end-to-end validation for restart, rewrite, new languages, and hybrid ranking.

Rationale: fix identity and restart safety first, then broaden coverage, then add retrieval intelligence, then validate the full stack under failure and reindex scenarios.