# Phase 6: Summarization Infrastructure — Research

**Researched:** 2026-04-10
**Status:** Research complete

## Research Question

What do I need to know to PLAN Phase 6 (Summarization Infrastructure) well?

Three deliverables: (1) `SummarizerProvider` protocol, (2) `LadybugStore.update_chunk_summary()` method, (3) `summarize_chunks()` pipeline function. Plus the critical constraint that re-indexing must preserve existing summaries.

---

## DELIVERABLE 1: SummarizerProvider Protocol

### Current Codebase Patterns
- No `Protocol` or `ABC` usage anywhere in the codebase currently
- No `typing.Protocol` imports exist — all typing imports are `Optional`, `Iterator`
- Pydantic `BaseModel` is the dominant pattern for data structures (Chunk, FileRecord, configs)
- The project uses Python 3.13, so `typing.Protocol` is fully available

### Design Decision: Protocol vs ABC
- **`typing.Protocol`** is the right choice: structural subtyping, no inheritance required
- Providers in Phase 7 (OpenAI-compatible, pi) just need to implement `summarize(code, context) -> str`
- No need for `@abstractmethod` or inheritance — Protocol gives duck-typing with type-checker support

### Recommended Signature
```python
from typing import Protocol

class SummarizerProvider(Protocol):
    def summarize(self, code: str, context: str) -> str:
        """Summarize a code chunk given its context.
        
        Args:
            code: The source code of the chunk.
            context: Surrounding context (file path, chunk name, chunk type).
            
        Returns:
            Summary string.
        """
        ...
```

### Where to Put It
- New file: `glma/summarize/providers.py` (or `glma/providers.py`)
- The `summarize_chunks()` function can live in `glma/summarize/__init__.py` or `glma/summarize/pipeline.py`
- Keeps provider infrastructure separate from the existing `glma/summaries.py` (rule-based summaries)

**Recommendation:** Create `glma/summarize/` package with:
- `glma/summarize/__init__.py` — exports `SummarizerProvider`, `summarize_chunks`
- `glma/summarize/providers.py` — `SummarizerProvider` protocol definition
- `glma/summarize/pipeline.py` — `summarize_chunks()` function

This mirrors the existing pattern of `glma/index/`, `glma/query/`, `glma/db/` as sub-packages.

---

## DELIVERABLE 2: LadybugStore.update_chunk_summary()

### Current Schema
The Chunk table in LadybugStore has a `summary STRING` column (line 21 of `ladybug_store.py`):
```sql
CREATE NODE TABLE IF NOT EXISTS Chunk (
    id STRING,
    file_path STRING,
    chunk_type STRING,
    name STRING,
    content STRING,
    summary STRING,
    start_line INT64,
    end_line INT64,
    content_hash STRING,
    parent_id STRING,
    PRIMARY KEY (id)
)
```

### Current Summary Handling
- `upsert_chunks()` (line 92-127) does `DETACH DELETE` + re-create pattern for ALL chunks in a file
- Summary is stored as empty string `""` when NULL: `data["summary"] = data.get("summary") or ""`
- `get_chunks_for_file()` converts empty string back to None: `summary=row[5] or None`
- **Critical**: `upsert_chunks()` destroys existing summaries because it deletes all chunks and re-inserts

### Required Changes

**1. New method: `update_chunk_summary(chunk_id: str, summary: str)`**
Simple UPDATE query:
```sql
MATCH (c:Chunk {id: $cid}) SET c.summary = $summary
```
This is a single-row update — no chunk deletion/recreation needed.

**2. Preserve summaries through `upsert_chunks()` (Success Criteria #4)**
This is the hard part. The current delete-and-recreate pattern destroys summaries.

**Strategy A — Read-before-write:**
Before deleting chunks, read existing chunk summaries into a dict keyed by content_hash. After creating new chunks, write back summaries for chunks whose content_hash hasn't changed.

```python
def upsert_chunks(self, file_path: str, chunks: list[Chunk]) -> None:
    # 1. Read existing summaries keyed by content_hash
    existing = self.get_chunks_for_file(file_path)
    summary_map = {c.content_hash: c.summary for c in existing if c.summary}
    
    # 2. Apply preserved summaries to new chunks
    for chunk in chunks:
        if not chunk.summary and chunk.content_hash in summary_map:
            chunk.summary = summary_map[chunk.content_hash]
    
    # 3. Existing delete + insert pattern
    self.conn.execute("MATCH (c:Chunk {file_path: $fp}) DETACH DELETE c", {"fp": file_path})
    for chunk in chunks:
        # ... insert as before ...
```

**Strategy B — Merge instead of delete+recreate:**
Use Ladybug's MERGE or SET operations to update only changed fields. More complex, riskier with existing patterns.

**Recommendation: Strategy A** — It's minimal change to existing code, preserves the proven delete+recreate pattern, and handles the edge case cleanly. Content_hash is the natural key for "same chunk, same content".

### Edge Cases
- What if a chunk's code changes but keeps the same content_hash? (Impossible — BLAKE2b is deterministic)
- What if two chunks have the same content_hash? (Possible — e.g., duplicated utility functions. Both should get the same summary, which is correct behavior)
- What about content_hash on the Chunk model vs content_hash on the actual content? The Chunk.content_hash is already computed from content, so it's reliable.

---

## DELIVERABLE 3: summarize_chunks() Pipeline Function

### Requirements
1. Accept `(store: LadybugStore, chunks: list[Chunk], provider: SummarizerProvider)`
2. Process chunks that have NULL/empty summary (skip already-summarized)
3. Call `provider.summarize(code, context)` for each chunk
4. Write summaries to DB via `store.update_chunk_summary(chunk_id, summary)`
5. Return updated chunks (with summaries populated)

### Context String Format
The `context` parameter needs useful metadata. Recommended format:
```python
context = f"File: {chunk.file_path}\nChunk: {chunk.name} ({chunk.chunk_type.value})\nLines: {chunk.start_line}-{chunk.end_line}"
```

### Error Handling
- If provider fails for one chunk: log warning, skip that chunk, continue with others
- Return the chunks that were successfully summarized
- Don't fail the entire pipeline for one bad chunk

### Suggested Implementation
```python
def summarize_chunks(
    store: LadybugStore,
    chunks: list[Chunk],
    provider: SummarizerProvider,
) -> list[Chunk]:
    """Process chunks, generate AI summaries, persist to DB."""
    updated = []
    for chunk in chunks:
        if chunk.summary:
            updated.append(chunk)
            continue
        try:
            context = f"File: {chunk.file_path}\nChunk: {chunk.name} ({chunk.chunk_type.value})\nLines: {chunk.start_line}-{chunk.end_line}"
            summary = provider.summarize(chunk.content, context)
            store.update_chunk_summary(chunk.id, summary)
            chunk.summary = summary
        except Exception:
            pass  # skip failed chunk
        updated.append(chunk)
    return updated
```

---

## EXISTING AI SUMMARY CODE

### What Already Exists (for reference, NOT for Phase 6)
`export.py:generate_ai_summary()` already has OpenAI-compatible API call logic:
- Takes `file_path`, `chunks`, `base_url`, `model`
- Builds context from chunk metadata
- Calls `client.chat.completions.create()` with system + user messages
- Returns summary string or error message

This is **file-level** summarization, not **per-chunk**. Phase 7 will need to build chunk-level providers that use a similar pattern.

### The Rule-Based Summary (separate, not affected)
`summaries.py:generate_rule_summary()` — deterministic, no LLM. Stays as-is for file-level summaries in export and writer output. Phase 6's per-chunk AI summaries are a different thing.

---

## TESTING CONSIDERATIONS

### New Test File Needed
`tests/test_summarize.py` covering:
1. `SummarizerProvider` protocol — verify a mock implementation satisfies the protocol
2. `LadybugStore.update_chunk_summary()` — insert chunk, update summary, verify DB state
3. `summarize_chunks()` — mock provider, verify:
   - Chunks with existing summary are skipped
   - Chunks without summary get summarized
   - Failed provider calls don't crash the pipeline
4. Summary preservation through `upsert_chunks()` — insert chunks with summaries, re-upsert same chunks with new hash, verify summaries preserved where content_hash unchanged

### Existing Tests Impact
- `test_store.py` — `upsert_chunks` behavior changes (now preserves summaries). Existing tests that insert `summary=None` chunks and then re-insert should still pass. **But must verify** that the new read-before-write logic doesn't break the test for `upsert_replaces_chunks`.
- All 211+ tests must still pass after changes.

---

## LADYBUG (real_ladybug) CYpher CAPABILITIES

### SET Operation Support
Ladybug (ex-Kuzu) supports standard Cypher SET:
```sql
MATCH (c:Chunk {id: $cid}) SET c.summary = $summary
```
This is a straightforward property update on an existing node — well-supported.

### Parameter Binding
Ladybug uses `$param` style parameter binding (confirmed throughout existing codebase in `conn.execute()` calls with dict params).

---

## DEPENDENCY CHECK

### No New Dependencies for Phase 6
- `typing.Protocol` — stdlib (Python 3.13)
- `LadybugStore` — already in codebase
- No `openai` import needed yet (Phase 7 adds actual providers)
- No `pip install` needed

### openai Remains Optional
Per Phase 7 requirements: `openai` remains optional dependency (`pip install glma[ai]`). Phase 6 just defines the protocol — no actual LLM calls.

---

## SUMMARY OF FINDINGS

| Area | Finding | Risk |
| ---- | ------- | ---- |
| Protocol | `typing.Protocol` available, no codebase precedent but straightforward | Low |
| DB update | Simple `SET c.summary = $summary` Cypher, Ladybug supports it | Low |
| Summary preservation | Strategy A (read-before-write in `upsert_chunks`) is safe and minimal | Low |
| Testing | New test file + verify existing tests unaffected | Medium (verify 211+ pass) |
| Dependencies | None needed — all stdlib or existing | None |

**Key Insight:** The most delicate change is modifying `upsert_chunks()` to preserve summaries. This touches the core indexing path. The fix is small (3-4 lines added) but must be tested carefully against existing behavior.

---

*Phase: 06-summarization-infrastructure*
*Research: 2026-04-10*
