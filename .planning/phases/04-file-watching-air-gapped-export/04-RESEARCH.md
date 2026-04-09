# Phase 4: File Watching & Air-Gapped Export - Research

**Researched:** 2026-04-09
**Status:** Complete

## Research Question

"What do I need to know to PLAN this phase well?"

---

## 1. File Watching: Library Choice

### Options Evaluated

| Library | Mechanism | Platform | Async | Dependencies | Notes |
| ------- | --------- | -------- | ----- | ------------ | ----- |
| **watchfiles** | Rust-based (notify crate) | Cross-platform | Yes (async) | Rust compiled | By Samvalley/PyO3, same author as pydantic-core. Fast, low CPU. |
| **watchdog** | Python + OS native (inotify/FSEvents/ReadDirectoryChangesW) | Cross-platform | Yes (asyncio) | Pure Python + pathtools | Mature, well-known, higher CPU overhead than Rust-based |
| **inotify (pyinotify)** | Linux inotify only | Linux only | No | C binding | Limited to Linux, not acceptable for cross-platform CLI |

### Recommendation: `watchfiles`

**Rationale:**
- CONTEXT.md says "watchfiles" in the roadmap plan title: "04-01: File watcher with watchfiles"
- Zero-config cross-platform file watching
- Built on Rust's `notify` crate — extremely fast event processing
- Provides both sync and async APIs (`watchfiles.watch` is an async generator)
- Same author as pydantic-core — high quality, well-maintained
- Minimal dependency footprint (compiled Rust wheel, no system deps)
- Events include: `watchfiles.Change.added`, `.modified`, `.deleted` — covers create/modify/delete. Renames show as delete + add pair.

**API Pattern:**
```python
from watchfiles import awatch, Change

async for changes in awatch(path):
    for change_type, path in changes:
        if change_type == Change.added:
            # New file
        elif change_type == Change.modified:
            # Modified file
        elif change_type == Change.deleted:
            # Deleted file
```

**Integration with glma:**
- `awatch` is an async generator that yields **sets of changes** — each set is already batched by OS event coalescence
- For additional debouncing (e.g., 3s batch window for bulk git operations), wrap with `asyncio.sleep()` collector pattern
- No daemon mode needed — `awatch` runs until cancelled (Ctrl+C raises `KeyboardInterrupt`)

**Rename Detection:**
- `watchfiles` does NOT emit a rename event — renames appear as `deleted` + `added`
- CONTEXT.md D-03 says "Track all file event types: create, modify, delete, and rename. Explicit rename tracking allows single-operation path updates instead of delete+re-parse."
- **Implementation:** After collecting batch events, use a heuristic: if a `deleted` path and an `added` path have the same content hash within the same batch, treat as rename. Otherwise treat as separate delete + add.

### Dependency Addition

```toml
# pyproject.toml
"watchfiles>=1.0",
```

---

## 2. Incremental Re-Indexing via `run_index()`

### Current Pipeline Architecture

`run_index()` in `pipeline.py` already supports incremental indexing:

1. **Walk → hash → skip-if-unchanged** — Computes BLAKE2b hash, compares to stored hash, skips unchanged files
2. **Parse → extract → attach → store** — For changed files only
3. **Relationship extraction** — Pass 2
4. **Cross-file markdown rewrite** — Pass 3
5. **Delete removed files** — Detects files in DB but not on disk

### What Needs to Change for `glma watch`

Currently `run_index()` discovers files via `walk_source_files()`. For watch mode, we need to pass a **specific set of changed files** instead of walking the whole directory.

**Approach (per D-05): Reuse `run_index` with a file filter.**

Minimal changes to `run_index()`:
1. Add optional parameter `changed_files: Optional[list[tuple[Path, str]]] = None`
2. If `changed_files` is provided, skip the `walk_source_files()` call and use the provided list
3. For deleted files: accept a separate `deleted_paths: Optional[list[str]] = None` parameter
4. Skip Pass 2/3 for unchanged files (already done by hash comparison)

**Key Insight:** The pipeline already handles upserts (delete + recreate). Passing only changed files means unchanged files are never touched. The 3-pass pipeline runs only on the affected subset.

**New File Handling:** New files just need parsing + storage — the existing pipeline handles this naturally since `is_new = relative_path not in indexed_paths` already triggers full processing.

### Batch Window Pattern

```python
import asyncio
from datetime import datetime

async def collect_batch(awatch_iter, debounce_seconds: float = 3.0) -> tuple[set, set, set]:
    """Collect file events over a debounce window.
    
    Returns: (created, modified, deleted) sets of Path objects.
    """
    created: set[Path] = set()
    modified: set[Path] = set()
    deleted: set[Path] = set()
    
    # First event starts the window
    changes = await anext(awatch_iter)
    process_changes(changes, created, modified, deleted)
    
    # Collect more events within debounce window
    deadline = asyncio.get_event_loop().time() + debounce_seconds
    while True:
        try:
            remaining = deadline - asyncio.get_event_loop().time()
            if remaining <= 0:
                break
            changes = await asyncio.wait_for(anext(awatch_iter), timeout=remaining)
            process_changes(changes, created, modified, deleted)
            deadline = asyncio.get_event_loop().time() + debounce_seconds  # Reset on new events
        except (asyncio.TimeoutError, StopAsyncIteration):
            break
    
    return created, modified, deleted
```

---

## 3. Dual Output Sync (D-06)

### Current Dual Output

Every indexing operation writes to:
1. **Ladybug DB** — via `LadybugStore` (`.glma-index/db/index.lbug`)
2. **Markdown files** — via `write_markdown()` (`.glma-index/markdown/`)

### Atomicity Pattern

CONTEXT.md D-06: "Atomic-ish write pattern: buffer all changes, write DB + markdown, verify both succeeded."

**Current pipeline behavior:** `run_index()` processes files sequentially. Each file's DB write + markdown write happens independently. If a file's markdown write fails, the DB changes for that file are already committed.

**For watch mode:** Since we're processing a batch, the risk is higher. If processing 50 files and file 30's markdown write fails, files 1-29 are already in DB.

**Recommended approach:**
1. Process all changed files through the pipeline (DB writes + markdown writes)
2. Track any failures in a list
3. On failure, roll back failed files from DB (delete their records)
4. Log failures to user with `⚠ 3 files failed, rolled back: path1, path2, path3`

This is simpler than transaction-based atomicity and sufficient for a CLI tool. Ladybug doesn't support multi-statement transactions anyway.

---

## 4. Air-Gapped Export: Format & Structure

### Export Directory Layout (per D-07)

```
export-output/
├── INDEX.md              # File listing, chunk counts, relationship summaries
├── RELATIONSHIPS.md      # Full cross-file dependency graph as table
├── src/
│   ├── auth/
│   │   ├── login.py.md   # Per-file exported markdown
│   │   └── tokens.py.md
│   └── main.c.md
└── README.md             # How to consume the export (for agents)
```

### Per-File Export Format (per D-09)

Each file gets enriched markdown with metadata header:

```markdown
---
file_path: src/auth/login.py
language: python
last_indexed: 2026-04-09T12:34:56Z
chunk_count: 5
content_hash: abc123...
---

# src/auth/login.py

## Summary
3 functions (authenticate, verify_token, refresh), 1 class (TokenStore). 
Imports: jwt, datetime, os.

## Key Exports
| Name | Type | Description |
| ---- | ---- | ----------- |
...

## Chunks
### authenticate (function, L12-L45)
...

## Relationships
...
```

### INDEX.md Structure

```markdown
# Codebase Index

**Generated:** 2026-04-09T12:34:56Z
**Total Files:** 42
**Total Chunks:** 318

## Files

| File | Language | Chunks | Summary |
| ---- | -------- | ------ | ------- |
| [src/auth/login.py](src/auth/login.py.md) | python | 5 | 3 functions, 1 class |
| [src/main.c](src/main.c.md) | c | 8 | Entry point, signal handlers |

## Statistics
- Total functions: 120
- Total classes: 35
- Total relationships: 450
```

### RELATIONSHIPS.md Structure (per D-08)

```markdown
# Cross-File Relationships

**Generated:** 2026-04-09T12:34:56Z
**Total Relationships:** 450

## Dependency Graph

| Source File | Source Chunk | Type | Target File | Target Chunk | Confidence |
| ----------- | ------------ | ---- | ----------- | ------------ | ---------- |
| [src/auth/login.py](src/auth/login.py.md) | authenticate | calls | [src/auth/tokens.py](src/auth/tokens.py.md) | verify_token | DIRECT |
| [src/main.c](src/main.c.md) | main | includes | [src/config.h](src/config.h.md) | - | DIRECT |

## File Dependencies

### src/auth/login.py
**Imports from:** [tokens.py](src/auth/tokens.py.md), [config.py](src/config.py.md)
**Called by:** [src/api/routes.py](src/api/routes.py.md), [src/cli.py](src/cli.py.md)
```

### Rule-Based File Summaries (per D-10)

Generate summaries from existing data without LLM:

```python
def generate_rule_summary(chunks: list[Chunk], relationships: list[dict]) -> str:
    """Generate deterministic file summary from chunk + relationship data."""
    functions = [c for c in chunks if c.chunk_type == ChunkType.FUNCTION]
    classes = [c for c in chunks if c.chunk_type == ChunkType.CLASS]
    methods = [c for c in chunks if c.chunk_type == ChunkType.METHOD]
    
    parts = []
    if functions:
        names = ", ".join(f.name for f in functions[:10])
        parts.append(f"{len(functions)} function(s): {names}")
    if classes:
        names = ", ".join(c.name for c in classes)
        parts.append(f"{len(classes)} class(es): {names}")
    
    # Extract unique import targets
    imports = {r["target_name"] for r in relationships if r.get("rel_type") == "imports"}
    if imports:
        parts.append(f"Imports: {', '.join(sorted(imports)[:15])}")
    
    return ". ".join(parts) + "." if parts else "Empty file."
```

---

## 5. AI Summaries via Local Models (per D-11)

### OpenAI-Compatible API Integration

Most local model providers expose the same API:

| Provider | Default URL | API Compatibility |
| -------- | ----------- | ----------------- |
| LM Studio | `http://localhost:1234/v1` | OpenAI `/v1/chat/completions` |
| Ollama | `http://localhost:11434/v1` | OpenAI `/v1/chat/completions` |
| llama.cpp server | `http://localhost:8080/v1` | OpenAI `/v1/chat/completions` |

**Implementation:** Use the `openai` Python client pointed at a configurable base URL.

```python
from openai import OpenAI

def generate_ai_summary(file_path: str, chunks: list[Chunk], base_url: str, model: str = None) -> str:
    client = OpenAI(base_url=base_url, api_key="not-needed")
    
    # Build context from chunks
    code_summary = f"File: {file_path}\n"
    for chunk in chunks:
        code_summary += f"- {chunk.chunk_type.value} {chunk.name} (L{chunk.start_line}-L{chunk.end_line})\n"
    
    response = client.chat.completions.create(
        model=model or "default",
        messages=[
            {"role": "system", "content": "Summarize this source file in 1-2 sentences for a developer. Focus on purpose and key exports."},
            {"role": "user", "content": code_summary},
        ],
        max_tokens=150,
    )
    return response.choices[0].message.content
```

**Config integration (`.glma.toml`):**
```toml
[export]
ai_summaries = false
ai_base_url = "http://localhost:1234/v1"
ai_model = "default"
```

**Dependency:** `openai` is NOT currently a dependency. Need to add it as optional:
```toml
[project.optional-dependencies]
ai = ["openai>=1.0"]
```

Or just add it as a regular dependency since it's lightweight without API keys.

---

## 6. Export Output Modes (per D-12)

### Three Output Modes

1. **Directory** (`--output ./dir`): Write files to disk. Default behavior.
2. **Archive** (`--output export.tar.gz`): Create compressed tar.gz. Detect by `.tar.gz` or `.tgz` extension.
3. **Stdout** (`--output -`): Stream tar archive to stdout for piping.

**Implementation Pattern:**
```python
import tarfile
import sys
from pathlib import Path

def export_index(repo_root: Path, config: ExportConfig, store: LadybugStore):
    output = config.output_path
    
    if output == "-":
        # Stdout mode: stream tar to stdout
        with tarfile.open(fileobj=sys.stdout.buffer, mode="w|gz") as tar:
            _write_export_files(tar, repo_root, config, store)
    elif output.endswith(".tar.gz") or output.endswith(".tgz"):
        # Archive mode
        with tarfile.open(output, "w:gz") as tar:
            _write_export_files(tar, repo_root, config, store)
    else:
        # Directory mode
        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)
        _write_export_files_to_dir(output_path, repo_root, config, store)
```

---

## 7. Config Extensions

### New Config Sections Needed

```toml
# .glma.toml

[watch]
debounce_seconds = 3.0    # Batch window for change collection
verbose = false           # Log every file event

[export]
output_path = null        # Default: ./glma-export/
include_code = true       # Include full code bodies in export
ai_summaries = false      # Use local LLM for summaries
ai_base_url = "http://localhost:1234/v1"
ai_model = "default"
```

### New Models

```python
class WatchConfig(BaseModel):
    debounce_seconds: float = Field(default=3.0, ge=0.5, le=30.0)
    verbose: bool = False

class ExportConfig(BaseModel):
    output_path: Optional[str] = None
    include_code: bool = True
    ai_summaries: bool = False
    ai_base_url: str = "http://localhost:1234/v1"
    ai_model: str = "default"
```

---

## 8. CLI Command Registration

### `glma watch` Command

```python
@app.command()
def watch(
    path: Optional[Path] = typer.Argument(None, help="Path to repository to watch."),
    verbose: bool = typer.Option(False, "--verbose", "-V", help="Log every file event."),
    config_file: Optional[Path] = typer.Option(None, "--config", help="Path to .glma.toml config file."),
    debounce: Optional[float] = typer.Option(None, "--debounce", help="Batch window in seconds."),
) -> None:
    """Watch for file changes and incrementally re-index."""
    # Must run inside an already-indexed repo
    # Validate .glma-index exists
    # Start async watcher loop
```

**Key:** Uses `asyncio.run()` to run the async watchfiles loop. Typer supports async commands natively when using `asyncio.run()` internally.

### `glma export` Command

```python
@app.command()
def export(
    path: Optional[Path] = typer.Argument(None, help="Path to indexed repository."),
    output: str = typer.Option(".", "--output", "-o", help="Output path (directory, .tar.gz, or - for stdout)."),
    ai_summaries: bool = typer.Option(False, "--ai-summaries", help="Generate AI summaries via local model."),
    ai_url: Optional[str] = typer.Option(None, "--ai-url", help="Local model API URL."),
    config_file: Optional[Path] = typer.Option(None, "--config", help="Path to .glma.toml config file."),
) -> None:
    """Export full index as static markdown for air-gapped consumption."""
```

---

## 9. Integration Points & Risk Areas

### Risk: `run_index()` Refactoring

The pipeline was built for full-repo walks. Adding file-filter support must not break existing `glma index` behavior.

**Mitigation:** The `changed_files` parameter defaults to `None`, and existing behavior triggers when it's `None`. The watch codepath provides the explicit file list.

### Risk: Watch + Deleted Files

When a file is deleted, we can't hash it or parse it. The pipeline's "Phase 3: Delete removed files" handles this, but it currently detects deletions by comparing `indexed_paths - source_paths`. For watch mode, we receive explicit delete events.

**Mitigation:** Pass `deleted_paths` separately to a cleanup function that calls:
1. `store.delete_relationships(path)`
2. `store.delete_file(path)`
3. Remove markdown file

This is already exactly what the pipeline does for deletions — just extract it.

### Risk: Cross-File Relationship Consistency

When file A changes and file B imports from A, file B's incoming relationships need updating. The 3-pass pipeline handles this in Pass 3, but only processes files from the current run.

**Mitigation:** After processing changed files, run Pass 3 (cross-file rewrite) for all files that have relationships pointing to changed files. Query: "Find all files whose chunks are targets of relationships FROM changed file chunks." This is a small set and can be derived from the relationship table.

### Risk: Export Completeness for Large Repos

Exporting thousands of files could be slow or produce very large output.

**Mitigation:** 
- Stream files one at a time (don't load all into memory)
- Archive mode (`tar.gz`) streams naturally
- INDEX.md and RELATIONSHIPS.md generated at the end after counting

---

## 10. Testing Strategy

### Unit Tests (Phase 4 specific)

1. **Watch batching:** Test `collect_batch()` with simulated events
2. **Rename detection:** Test heuristic for delete+add → rename
3. **Export format:** Verify per-file markdown has correct metadata header
4. **INDEX.md generation:** Verify file listing, chunk counts, statistics
5. **RELATIONSHIPS.md generation:** Verify cross-file table completeness
6. **Rule-based summaries:** Test summary generation from chunk data
7. **Output modes:** Test directory, tar.gz, and stdout output

### Integration Tests

1. **Watch → change → verify:** Create file, index, modify file, watch detects, verify DB + markdown updated
2. **Watch → delete → verify:** Delete file while watching, verify cleaned up from DB + markdown
3. **Export → verify completeness:** Export full index, verify all files present, all relationships in RELATIONSHIPS.md
4. **Export → cat test:** Export and verify a shell user can understand codebase from export alone

### Test Fixtures

- Use the existing test repo fixture from Phase 1-3 tests
- Add a temporary file modification helper for watch tests
- Add expected export output fixtures

---

## 11. Dependencies Summary

| Dependency | Version | Purpose | New? |
| -----------| --------| ------- | ---- |
| watchfiles | >=1.0 | File system watching | ✓ NEW |
| openai | >=1.0 | Optional AI summaries (local models) | ✓ NEW (optional) |

Existing dependencies used:
- `typer` — CLI commands (watch, export)
- `rich` — Console output formatting
- `pydantic` — Config models (WatchConfig, ExportConfig)
- `real-ladybug` — DB reads for export
- `tarfile` (stdlib) — Archive output
- `asyncio` (stdlib) — Watch event loop

---

## RESEARCH COMPLETE

**Key findings:**
1. **watchfiles** is the right library — fast, cross-platform, async, already referenced in roadmap
2. **run_index()** needs minimal changes — add `changed_files` parameter to skip directory walk
3. **Export** is primarily a read operation — query LadybugStore, format, write to disk/archive/stdout
4. **Rule-based summaries** are deterministic and sufficient — AI summaries are optional enhancement
5. **OpenAI-compatible API** covers all local model providers with one integration
6. **Rename detection** requires heuristic (content hash matching in batch window)
7. **Cross-file consistency** after watch requires running Pass 3 on dependent files too
