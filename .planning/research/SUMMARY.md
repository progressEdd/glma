# Project Research Summary

**Project:** glma
**Domain:** CLI codebase indexer with AI summarization
**Researched:** 2026-04-10
**Confidence:** HIGH

## Executive Summary

This is a polish milestone for an existing, working CLI tool. The codebase already has all the infrastructure for per-chunk AI summaries — the `Chunk.summary` field exists in the model, the DB schema, and all output paths read it. The gap is purely that nothing ever *writes* to it. The summarization feature is "wired for sound but no one's speaking into the mic."

The main new component is a **summarization pipeline** with a pluggable provider architecture. Two providers: OpenAI-compatible (already partially working in export.py) and pi agent (new). The provider protocol is simple: code in, summary string out. Everything else (persistence, output flow, incremental updates) is plumbing that fits naturally into the existing 3-pass pipeline.

Three bug fixes are trivial (flip a default, replace a string, fix a parsing edge case). ARCHITECTURE.md generation is a new export feature that derives a codebase overview from existing relationship data + summaries.

## Stack Additions

- **openai** (≥1.30) — Already conditionally imported; make it an optional `[ai]` extra in pyproject.toml
- **httpx** (≥0.27) — For pi agent provider; already a transitive dependency of openai
- **No new framework** — No litellm, no langchain. Simple provider protocol with direct API calls

## Feature Table Stakes

- **Per-chunk summaries** — Agents need function-level understanding, not just file-level
- **Persistence** — Generate once, survive re-export, flow to all outputs (export, query, writer)
- **Configurable model** — Ollama, LM Studio, llama.cpp, pi — all via one config
- **Incremental** — Only summarize new/changed chunks, don't re-process entire codebase

## Key Architecture Decisions

1. **Summarization is a separate pass**, not part of chunk extraction. Keeps pipeline modular. Can run standalone (`glma summarize`) or as part of index (`glma index --summarize`).
2. **Provider protocol** — `SummarizerProvider` with one method. OpenAI-compatible wraps existing pattern. Pi provider is a separate backend.
3. **Summary preservation on re-index** — `upsert_chunks()` deletes+recreates. Must preserve summaries where content_hash hasn't changed, or summaries get wiped on every re-index.
4. **ARCHITECTURE.md from existing data** — No new indexing needed. File tree + relationships + summaries → architecture overview.

## Build Order

1. Bug fixes (trivial, no risk)
2. Summarization infrastructure (new `summarizer.py`, DB update method, config)
3. CLI integration (`--summarize` flags, `glma summarize` command)
4. Provider implementations (refactor OpenAI from export.py, add pi provider)
5. ARCHITECTURE.md generation (uses summaries from DB)

## Watch Out For

- **Summaries lost on re-index** — `upsert_chunks()` does DETACH DELETE. Must preserve summaries for unchanged chunks.
- **Local model timeouts** — Small models on CPU are slow. Sequential processing, 30s+ timeouts, resume capability.
- **Token limits on large chunks** — Truncate to ~2000 chars before sending to LLM.
- **openai as optional dep** — Keep `[ai]` extra, don't break installs for rule-based-only users.
- **Pi provider API surface** — Research pi's actual API before implementing. Keep fallback to rule-based.

---
*Research summary for: glma v1.1 Polish & Complete*
*Researched: 2026-04-10*
