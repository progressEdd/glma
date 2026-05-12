# glma v1.4 Pitfalls

## Pipeline Reliability Pitfalls
- **Partial writes:** interrupting mid-file can leave chunks written but file stage/hash not updated.
- **Skipped recovery:** hash-only skipping can permanently bypass Pass 2/3 for files that were chunked before the crash.
- **Checkpoint drift:** in-memory progress and persisted DB state can disagree after restart.
- **Duplicate IDs:** current C chunk IDs collide on macros/forward decls; a checkpoint system that keys off unstable IDs will fail too.
- **Non-idempotent reruns:** repeated upserts, markdown regeneration, or relationship writes can duplicate edges unless writes are deduped.
- **Signal timing:** SIGINT/SIGTERM during DB commits can corrupt the notion of “completed stage” even if the DB transaction itself succeeds.
- **Embedding retry gaps:** failed chunks need explicit retry markers; otherwise resume logic can skip them forever.

## LLM Query Rewriting Pitfalls
- **Semantic drift:** rewrites can change intent or bias toward the model’s guesses instead of the user’s wording.
- **Hallucinated tokens:** model may invent file names, symbols, or subsystem names that hurt retrieval.
- **Over-expansion:** too many synonyms/keywords can dilute precision and pull noisy results.
- **Mode confusion:** rewrite output must stay as a query, not an answer, explanation, or step-by-step plan.
- **Provider variance:** different local/OpenAI-compatible models may rewrite inconsistently.
- **Prompt injection:** user queries may contain instructions that try to override the rewrite prompt.
- **Latency/cost:** every query may become two LLM calls if rewriting is not cached or gated.
- **Auditability:** debug logs must preserve original query + rewritten query to explain retrieval failures.

## Extended Language Support Pitfalls
- **Grammar mismatch:** tree-sitter grammars can parse successfully but still map to the wrong chunk/relationship node types.
- **Comment/docstring rules differ:** C++, TS, and Rust attach comments differently than C/Python.
- **Namespace/module complexity:** C++ namespaces, Rust modules/crates, and TS import paths need language-specific resolution.
- **Preprocessor/macros/templates:** C++ macros and templates can create ambiguous or duplicated symbols like C already does.
- **File extension traps:** `.h`, `.hpp`, `.hh`, `.ts`, `.tsx`, `.rs` need reliable classification, not just generic fallback.
- **Dependency drift:** tree-sitter grammar package versions can change node names or query behavior.
- **Performance variance:** large generated files or heavily templated C++ can blow up parse/chunk time.

## 3-Way Hybrid Search Pitfalls
- **Score incompatibility:** graph proximity, keyword scores, and vector similarity live on different scales.
- **Bad normalization:** a weak normalization step can let one signal dominate every query.
- **Candidate explosion:** graph traversal plus keyword/vector unions can return too many chunks.
- **Graph noise:** inferred edges and shallow relationships can over-reward nearby but irrelevant code.
- **Sparse signals:** some files will have no embeddings, weak text matches, or no graph edges; ranking must degrade gracefully.
- **Duplicate candidates:** the same chunk may arrive from all three channels and needs stable deduping.
- **Threshold coupling:** similarity thresholds that work for vector search may exclude good graph-heavy results.
- **Query rewriting interaction:** rewritten queries may help keyword/vector but hurt graph retrieval if they remove original domain terms.

## Integration Pitfalls
- **Checkpoint vs ID changes:** changing chunk IDs for C can invalidate stored relationships, embeddings, and resume markers.
- **Resume vs search indexes:** resuming indexing while search data is stale can surface partial results.
- **Language support vs hybrid search:** new languages need embeddings, summaries, and relationship extraction before they participate in 3-way search.
- **Rewrite vs retrieval caching:** rewritten queries need separate cache keys from original queries.
- **Markdown/export consistency:** per-file markdown regeneration must stay in sync with DB state after resume.
- **Test matrix growth:** restart + rewrite + new languages + hybrid search creates many combinational failure modes.
- **Backward compatibility:** old indexes need migration or reindex guidance when stage schema or chunk IDs change.

## Prevention Strategies
- Use a **versioned pipeline state machine** per file: discovered → chunked → relationships_extracted → markdown_written → embedded → complete.
- Make every stage **idempotent** and safe to rerun.
- Persist **checkpoint + last successful stage + schema version** in Ladybug or a sidecar state store.
- Commit state **atomically per file**, not per batch.
- Treat chunk IDs as **versioned and collision-resistant** (hash/offset suffix).
- Keep query rewriting **opt-in or gated**, with original query always logged.
- Add **rewrite guardrails**: preserve intent, cap rewrite length, forbid invented symbols.
- Normalize search scores with **explicit calibration tests** and per-signal fallbacks.
- Deduplicate candidates across channels before ranking.
- Add end-to-end tests for **interrupt/restart**, **language parsing**, **rewrite fidelity**, and **hybrid ranking**.

## Which Phase Should Address Each
| Phase | Should Cover | Main Pitfalls |
| --- | --- | --- |
| **Phase 16: Pipeline Reliability** | checkpointing, interrupt recovery, stage persistence, chunk ID migration | pipeline reliability, integration, backward compatibility |
| **Phase 17: LLM Query Rewriting** | rewrite prompt, provider wiring, logging, guardrails | semantic drift, hallucination, prompt injection, latency |
| **Phase 18: Extended Language Support** | C++, TypeScript, Rust grammars, node maps, comment rules, symbol resolution | grammar mismatch, extension traps, parser drift, macro/template edge cases |
| **Phase 19: 3-Way Hybrid Search** | graph + keyword + vector scoring, normalization, dedupe, thresholds | score incompatibility, candidate explosion, sparse-signal fallback, graph noise |
| **Phase 20: Integration Hardening** | cross-feature E2E tests, migrations, resume/rewrite/search compatibility | checkpoint vs ID changes, stale indexes, test matrix explosion, export consistency |

**Rule of thumb:** fix reliability and identity first, then rewrite, then expand languages, then merge signals.
