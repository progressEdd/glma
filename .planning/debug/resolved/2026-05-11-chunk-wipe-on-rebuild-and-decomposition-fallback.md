# 2026-05-11: Chunk Wipe on Rebuild + Decomposition Fallback

## Problem 1: `_rebuild_chunk_table()` silently wiped all chunks

Running `glma embed` with `--embedding-provider embed-lmstudio` (1024 dims) against a DB indexed at 768 dims resulted in **all chunks being deleted** with no error:

```
Embedded:  0
Skipped:   0
Failed:    0
```

### Root Cause

`_rebuild_chunk_table_if_needed()` detected the dimension mismatch (768→1024) and called `_rebuild_chunk_table()`. The rebuild tried to:

1. `DROP TABLE Chunk` — **failed** because `RELATES_TO` relationship table references Chunk
2. Caught the exception, fell back to `MATCH (c:Chunk) DETACH DELETE c` — **this deleted all chunk data**
3. Tried `DROP TABLE Chunk` again — **still failed** (RELATES_TO still exists)
4. `CREATE NODE TABLE IF NOT EXISTS Chunk` — **no-op** (table still exists)
5. Re-insert of preserved rows — **failed silently** (caught by `except Exception`)
6. **Result: 0 chunks, 0 relationships, 0 embeddings — all data gone**

The code only dropped `CONTAINS` before `Chunk`, but `RELATES_TO` also references Chunk and wasn't dropped first.

### Fix

Updated `_rebuild_chunk_table()` in `src/glma/db/ladybug_store.py` to drop **both** relationship tables before dropping Chunk:

```python
# Drop relationship tables that reference Chunk (must drop before Chunk)
for rel_table in ["RELATES_TO", "CONTAINS"]:
    try:
        self.conn.execute(f"DROP TABLE {rel_table}")
    except Exception:
        pass

# Drop existing Chunk table
try:
    self.conn.execute("DROP TABLE Chunk")
except Exception:
    ...
```

Verified: 14 chunks preserved through 768→1024 rebuild.

## Problem 2: Decomposition returns `None` when all methods fail

When summarizing large class chunks (e.g., `GPTAssistantAgent` at 24K chars), the pipeline triggers decomposition. Decomposition tries to summarize each child method, but with LM Studio's context length set to **4096 tokens**, even individual methods (~7K chars ≈ 2000+ tokens) could fail if they're borderline. When all methods fail → `method_summaries` is empty → `_decompose_class_chunk()` returns `None` → **chunk gets no summary at all**.

### Fix

Added a fallback in `_decompose_class_chunk()` in `src/glma/summarize/pipeline.py`: when all method summaries fail, extract just the class header (docstring, decorators, class vars) and summarize that instead:

```python
if not method_summaries:
    # Fallback: summarize just the class header
    if class_header.strip():
        return provider.summarize(class_header, header_context)
    return None
```

### User Action Needed

Increased LM Studio context length from 4096 → 8192 (Gemma 4 26B supports it; VRAM increase is ~1-2GB for KV cache, should fit within 24GB).

## Re-index Required

The ag2-framework DB was corrupted (WAL issues) during debugging. Backup saved at `index.lbug.bak`. DB was deleted and needs a full re-index:

```bash
uv run glma index <path> --summarize
uv run glma embed <path> --embedding-provider embed-lmstudio
```

Re-running `--summarize` is incremental — skips chunks with existing summaries, retries failed ones.
