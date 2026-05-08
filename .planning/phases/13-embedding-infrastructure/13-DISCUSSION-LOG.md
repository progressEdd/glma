# Phase 13: Embedding Infrastructure - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-05-08
**Phase:** 13-embedding-infrastructure
**Areas discussed:** Protocol shape, Config structure, Embedding model defaults, Preset naming, Architecture

---

## Architecture

User described the full pipeline architecture during protocol shape discussion:

- **Index path:** Code chunks → summarizer model → chunk summaries → embed summaries → store vectors
- **Query path:** User question → summarizer model → embed summary → hybrid search → ranked chunks
- Summarization and embedding are separate steps; summarizer model generates both chunk summaries and query summaries
- Hugging Face noted as desired future provider (`ENOSYS/Octen-Embedding-8B-750-v1-GGUF`) but agreed to start with OpenAI-compatible only

---

## Protocol Shape

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Batch-only | `embed(texts: list[str]) -> list[list[float]]`, single text wrapped in list | ✓ |
| Batch + single | Both `embed(texts)` and `embed_single(text)` on the protocol | |
| Batch with error results | Returns `list[list[float] \| None]` for partial failure | |

**User's choice:** Batch-only
**Notes:** No partial batch failure handling — local providers either work or fail entirely. Hugging Face deferred to future phase (only OpenAIEmbeddingProvider for now).

---

## Config Structure

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Single flat `[search]` section | All fields in one place, embedding now + hybrid in Phase 15 | ✓ |
| Nested `[search.embedding]` + `[search.hybrid]` | Separate subsections from the start | |

**User's choice:** Single flat `[search]` section (confirmed via "flat is the example right?")
**Notes:** ~8 total fields across Phase 13 and Phase 15, not enough to justify nesting.

---

## Embedding Model Defaults

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Ollama → `nomic-embed-text`, others → `default` | Ollama gets specific model, servers with loaded models use default | |
| All → `default` | Let server decide | |
| All explicitly specified | Pick specific models for each preset | |
| Ollama → `qwen3-embedding`, others → `default` | User-specified Ollama model | ✓ |

**User's choice:** Ollama → `qwen3-embedding`, others → `default`
**Notes:** Also specified Hugging Face model `ENOSYS/Octen-Embedding-8B-750-v1-GGUF` for future use.

---

## Preset Naming

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| Same names as summarization | `ollama`, `lmstudio`, etc. — `[search]` vs `[summarize]` section provides context | |
| Prefixed names | `embed-ollama`, `embed-lmstudio`, etc. — explicit separation | ✓ |

**User's choice:** Prefixed names (`embed-ollama`, `embed-lmstudio`, `embed-vllm`, `embed-llamacpp`, `embed-local`)
**Notes:** Breaks from summarization naming convention but makes intent explicit. User confirmed preference for prefix.

---

## Agent's Discretion

- Exact `OpenAIEmbeddingProvider` implementation details
- Whether to create separate `EMBEDDING_PROVIDER_PRESETS` dict or extend existing one
- Error message wording
- Exact field names in SearchConfig
- Test structure and coverage

## Deferred Ideas

- Hugging Face provider (`sentence-transformers`, model `ENOSYS/Octen-Embedding-8B-750-v1-GGUF`) — future phase
