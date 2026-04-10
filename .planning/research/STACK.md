# Stack Research

**Domain:** CLI codebase indexer with AI summarization
**Researched:** 2026-04-10
**Confidence:** HIGH

## Recommended Stack

### Core Technologies (already in place)

| Technology | Version | Purpose | Why Recommended |
| ---------- | ------- | ------- | --------------- |
| real-ladybug | ≥0.15.3 | Graph DB with native vector indices | Already in use, ex-Kuzu, summary field exists on Chunk nodes |
| tree-sitter | ≥0.25.2 | AST parsing | Already proven for C and Python |
| typer | ≥0.24.1 | CLI framework | Already in use |
| pydantic | ≥2.12 | Data models | Already in use, Chunk model has summary field |
| rich | ≥14.0 | Progress display | Already in use |

### New Dependencies Needed

| Library | Version | Purpose | Why Recommended |
| ------- | ------- | ------- | --------------- |
| openai | ≥1.30 | LLM API client for summarization | Already used conditionally in export.py; make it a proper dependency for the summarization pipeline. Works with Ollama, LM Studio, llama.cpp server, any OpenAI-compatible API |
| httpx | ≥0.27 | Async HTTP for pi agent provider | pi's API uses REST; httpx is lightweight, already a transitive dep of openai |

### What NOT to Add

| Avoid | Why | Use Instead |
| ----- | --- | ----------- |
| litellm | Overkill for 2 provider backends, adds heavy dependency tree | Simple provider protocol with OpenAI client + httpx |
| langchain | Massive framework, not needed for single-purpose summarization | Direct openai client calls |
| sentence-transformers | Embedding is future milestone, not v1.1 | Defer to semantic search milestone |
| tenacity | Retry logic is overkill for this scope | Simple try/except with logging (already pattern in codebase) |

### Provider Architecture

**Protocol/ABC approach** (not a library):
- `SummarizerProvider` protocol with `summarize(code: str, context: str) -> str` method
- `OpenAICompatibleProvider` — wraps `openai.OpenAI` client, works with Ollama/LM Studio/llama.cpp/local servers
- `PiAgentProvider` — calls pi's API to summarize code (httpx-based)
- Both produce same output: a summary string that gets written to `chunk.summary` in DB

**Configuration:**
- `.glma.toml` section: `[summarize]` with `provider`, `model`, `base_url` fields
- CLI flags: `glma index --summarize --summarize-provider local|pi --summarize-model <name>`

## Version Compatibility

| Package | Compatible With | Notes |
| ------- | --------------- | ----- |
| openai ≥1.30 | Python 3.13 | Works with any OpenAI-compatible server |
| httpx ≥0.27 | Python 3.13 | Already transitive dep of openai |

## Sources

- Existing codebase analysis — openai already conditionally imported in export.py
- Ladybug DB schema — Chunk.summary STRING field already exists
- pyproject.toml — current dependency versions verified

---
*Stack research for: per-chunk AI summarization with pluggable providers*
*Researched: 2026-04-10*
