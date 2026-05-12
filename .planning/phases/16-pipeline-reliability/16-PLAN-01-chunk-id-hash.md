---
wave: 1
depends_on: []
files_modified:
  - src/glma/index/chunks.py
  - src/glma/models.py
requirements_addressed:
  - PIPE-01
---

# Plan 01: Chunk ID Hash Suffix (PIPE-01)

## Objective
Change chunk ID format from `{file_path}::{chunk_type}::{name}::{start_line}` to `{file_path}::{name}::{line}::{hash8}` to prevent collisions from C macros and forward declarations. Drop `chunk_type` from ID, add 8-char BLAKE2b content hash suffix.

## Tasks

### Task 1.1: Update `_chunk_id()` in chunks.py

<read_first>
- 02-worktrees/glma/src/glma/index/chunks.py — current `_chunk_id()` function on line 18 and `_content_hash()` on line 13
- 02-worktrees/glma/src/glma/models.py — Chunk model, `id` field docstring on line 30
</read_first>

<action>
1. In `chunks.py`, modify `_chunk_id()` to accept `content_hash` parameter and drop `chunk_type` parameter:
   ```python
   def _chunk_id(file_path: str, name: str, start_line: int, content_hash: str) -> str:
       """Generate a unique chunk ID with content hash suffix."""
       hash8 = content_hash[:8]
       return f"{file_path}::{name}::{start_line}::{hash8}"
   ```
2. Update the call site in `_walk_chunks()` (around line 93) where `_chunk_id()` is called. Change from:
   ```python
   cid = _chunk_id(file_path, chunk_type_str, name, start_line)
   ```
   to:
   ```python
   cid = _chunk_id(file_path, name, start_line, _content_hash(content))
   ```
   Note: `content` variable is already computed at this point (line ~85: `content = child.text.decode("utf-8")`), and `_content_hash(content)` is also already computed for the Chunk's `content_hash` field. Use the local variable `content` to compute the hash for the ID — or better, compute it once and reuse:
   ```python
   content_hash = _content_hash(content)
   cid = _chunk_id(file_path, name, start_line, content_hash)
   ```
   Then pass `content_hash` to the Chunk constructor instead of calling `_content_hash(content)` again.

3. In `models.py`, update the Chunk model's `id` field docstring:
   ```python
   id: str = Field(..., description="Unique identifier: {file_path}::{name}::{start_line}::{hash8}")
   ```
</action>

<acceptance_criteria>
- `chunks.py` contains `def _chunk_id(file_path: str, name: str, start_line: int, content_hash: str) -> str:`
- `chunks.py` does NOT contain the old `_chunk_id` signature with `chunk_type` parameter
- `chunks.py` `_chunk_id` returns a string in format `{file_path}::{name}::{start_line}::{hash8}` (4 colon-separated segments, last is 8 hex chars)
- `chunks.py` `_walk_chunks` calls `_chunk_id(file_path, name, start_line, content_hash)` — no `chunk_type_str` argument
- `chunks.py` computes `_content_hash(content)` once and uses it for both `cid` and Chunk's `content_hash` field
- `models.py` Chunk `id` field description contains `hash8`
- Running `glma index` on any C file produces chunk IDs matching pattern `*::*::*::[0-9a-f]{8}` (8 hex chars at end)
</acceptance_criteria>

---

### Task 1.2: Fix `_load_chunks_from_store()` SQL query in pipeline.py

<read_first>
- 02-worktrees/glma/src/glma/index/pipeline.py — `_load_chunks_from_store()` function at line ~247
- 02-worktrees/glma/src/glma/db/ladybug_store.py — `get_chunks_for_file()` method to see the canonical query pattern
</read_first>

<action>
The `_load_chunks_from_store()` helper already queries Chunk nodes correctly. No changes needed to the SQL query — the `id` field is stored as-is in the DB, so new-format IDs will be read back correctly.

However, verify that `_load_chunks_from_store()` returns the same columns as `get_chunks_for_file()`. If they're in sync, no change needed. This task is a verification task — only make changes if there's a column mismatch.

Compare the RETURN clause in both functions and ensure they match. Currently:
- `_load_chunks_from_store`: `RETURN c.id, c.name, c.chunk_type, c.file_path, c.content, c.summary, c.start_line, c.end_line, c.content_hash, c.parent_id` (10 columns)
- `get_chunks_for_file`: `RETURN c.id, c.name, c.chunk_type, c.file_path, c.content, c.summary, c.start_line, c.end_line, c.content_hash, c.parent_id, c.embedding, c.summary_hash, c.vector_dimensions` (13 columns)

If embedding fields are needed in pipeline processing, update `_load_chunks_from_store` to match. If not, leave as-is.
</action>

<acceptance_criteria>
- `_load_chunks_from_store()` in `pipeline.py` works correctly with new chunk ID format (IDs are just strings, format doesn't matter for the query)
- No test changes needed for this task — the SQL doesn't depend on ID format
</acceptance_criteria>

---
