---
wave: 1
depends_on: []
files_modified:
  - src/glma/models.py
  - src/glma/summarize/pipeline.py
  - src/glma/summarize/providers.py
  - src/glma/cli.py
  - tests/test_summarize.py
  - tests/test_config.py
  - tests/test_cli.py
requirements_addressed: [TRUNC-01]
autonomous: true
---

# Plan 01: Decomposition Pipeline for Oversized Chunks

**Wave:** 1
**Objective:** Add try-first, decompose-on-failure logic to the summarization pipeline so that oversized chunks (like ag2's 32K-char AgentBuilder class) are summarized via decomposition instead of failing. Add `max_chunk_chars` config field and `--max-chunk-chars` CLI flag.

## Tasks

### Task 1: Add `max_chunk_chars` to SummarizeConfig

<read_first>
- 02-worktrees/glma/src/glma/models.py — current SummarizeConfig class (around line 155-170)
</read_first>

<action>
In `src/glma/models.py`, add a `max_chunk_chars` field to the `SummarizeConfig` class after the `base_url` field:

```python
max_chunk_chars: int = Field(
    default=3000,
    ge=100,
    description="Max chars per chunk before decomposition triggers. Chunks exceeding this are decomposed (class→method summaries→compose, or map-reduce for standalone chunks). Default 3000 ≈ 750 tokens.",
)
```

No other changes to models.py needed — the field follows the same pattern as existing fields.
</action>

<acceptance_criteria>
- `src/glma/models.py` contains `max_chunk_chars: int = Field(` with `default=3000`
- `SummarizeConfig()` instantiated without args has `max_chunk_chars == 3000`
- `SummarizeConfig(max_chunk_chars=5000).max_chunk_chars == 5000`
- All existing tests still pass: `cd 02-worktrees/glma && uv run pytest tests/ -x -q`
</acceptance_criteria>

---

### Task 2: Add `--max-chunk-chars` CLI flag

<read_first>
- 02-worktrees/glma/src/glma/cli.py — `index()` command function, specifically the `--summarize` flag handling and the `summarize_overrides` dict construction (around lines 70-90)
- 02-worktrees/glma/src/glma/config.py — `load_summarize_config()` function to understand how overrides flow
</read_first>

<action>
In `src/glma/cli.py`, add a new parameter to the `index()` function, right after the `--summarize-model` parameter:

```python
max_chunk_chars: Optional[int] = typer.Option(
    None,
    "--max-chunk-chars",
    help="Max chars per chunk for summarization (default: 3000). Triggers decomposition if exceeded.",
),
```

Then, in the `if summarize:` block where `summarize_overrides` is built (around line 85), add the max_chunk_chars override:

```python
if max_chunk_chars is not None:
    summarize_overrides["max_chunk_chars"] = max_chunk_chars
```

This follows the exact same pattern as the existing `--summarize-provider` and `--summarize-model` overrides — the key is added to the dict only when the user provides a value, and `load_summarize_config()` handles the merge automatically.
</action>

<acceptance_criteria>
- `src/glma/cli.py` contains `--max-chunk-chars` in the `index()` function signature
- `src/glma/cli.py` has `if max_chunk_chars is not None:` adding to `summarize_overrides`
- `glma index --help` output contains `--max-chunk-chars`
- All existing tests still pass: `cd 02-worktrees/glma && uv run pytest tests/ -x -q`
</acceptance_criteria>

---

### Task 3: Add `_is_context_length_error` helper and `_extract_class_header` helper

<read_first>
- 02-worktrees/glma/src/glma/summarize/pipeline.py — current module, all of it (only 66 lines)
- 02-worktrees/glma/src/glma/summarize/providers.py — `SYSTEM_PROMPT` constant used in summarization requests
</read_first>

<action>
In `src/glma/summarize/pipeline.py`, add these helper functions BEFORE the `summarize_chunks()` function:

```python
import re


def _is_context_length_error(exc: Exception) -> bool:
    """Check if an exception indicates a context length / token limit error.

    Matches error patterns from OpenAI-compatible APIs (Ollama, LM Studio, llama.cpp, OpenAI).
    """
    msg = str(exc).lower()
    status_code = getattr(getattr(exc, "status_code", None), "value", None) or getattr(exc, "status_code", None)
    # Check for 400 status with context-length indicators
    has_context_indicator = any(
        pattern in msg
        for pattern in ["context length", "context_length", "n_keep", "n_ctx", "max_tokens", "token limit", "too many tokens"]
    )
    if has_context_indicator:
        return True
    # OpenAI BadRequestError with status 400 — check if it looks like a size issue
    if status_code == 400 and ("token" in msg or "length" in msg or "too long" in msg):
        return True
    return False


def _extract_class_header(content: str) -> str:
    """Extract the class header portion from a class chunk's source code.

    Returns everything before the first method definition (class declaration,
    docstring, class-level variables, decorators). Falls back to the first 1500 chars.
    """
    lines = content.split("\n")
    header_lines: list[str] = []
    for line in lines:
        # Detect method definitions: lines with 'def ' at any indent level
        # but skip lines inside strings (heuristic: only match at valid indent levels)
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        # A method def has indent >= 4 (inside class body) and starts with 'def '
        if indent >= 4 and stripped.startswith("def "):
            break
        header_lines.append(line)

    header = "\n".join(header_lines)
    # Cap at 1500 chars to avoid sending too much
    if len(header) > 1500:
        header = header[:1500] + "\n... (class header truncated)"
    return header


def _map_reduce_summarize(
    content: str,
    context: str,
    provider: Protocol,
    segment_chars: int = 2000,
    overlap_chars: int = 200,
) -> str:
    """Summarize oversized content via map-reduce: split, summarize segments, combine.

    Args:
        content: The oversized source code.
        context: Metadata context for the chunk.
        provider: SummarizerProvider to call.
        segment_chars: Max chars per segment.
        overlap_chars: Overlap between segments.

    Returns:
        Combined summary string, or empty string if all segments fail.
    """
    # Split into overlapping segments
    segments: list[str] = []
    start = 0
    while start < len(content):
        end = min(start + segment_chars, len(content))
        segments.append(content[start:end])
        start += segment_chars - overlap_chars
        if start >= len(content):
            break

    if not segments:
        return ""

    # Summarize each segment
    segment_summaries: list[str] = []
    for i, seg in enumerate(segments):
        try:
            seg_context = f"{context}\nSegment {i + 1}/{len(segments)} of oversized chunk"
            summary = provider.summarize(seg, seg_context)
            if summary:
                segment_summaries.append(summary)
        except Exception:
            pass  # Skip failed segments

    if not segment_summaries:
        return ""

    # Combine: if only one segment summary, return it directly
    if len(segment_summaries) == 1:
        return segment_summaries[0]

    # Ask provider to combine
    combined = "\n".join(f"- {s}" for s in segment_summaries)
    combine_context = f"{context}\n\nThese are summaries of segments from an oversized code chunk. Write a single 1-2 sentence summary combining them."
    try:
        return provider.summarize(combined, combine_context)
    except Exception:
        # Fallback: just concatenate
        return "; ".join(segment_summaries)


def _decompose_class_chunk(
    chunk: Chunk,
    child_chunks: list[Chunk],
    all_chunks: list[Chunk],
    store: LadybugStore,
    provider: Protocol,
) -> str | None:
    """Summarize a class chunk by first summarizing its methods, then composing.

    1. Summarize each method child individually.
    2. Extract class header (docstring, class vars, decorators).
    3. Send class header + method summaries to provider for class-level summary.

    Args:
        chunk: The oversized class chunk.
        child_chunks: Method chunks with parent_id == chunk.id.
        all_chunks: Full chunk list (for context, not modified here).
        store: LadybugStore for persisting method summaries.
        provider: SummarizerProvider for calling the LLM.

    Returns:
        Class summary string, or None if decomposition fails.
    """
    method_summaries: list[str] = []

    # Step 1: Summarize each method child
    for child in child_chunks:
        if child.summary:
            # Already summarized (incremental)
            method_summaries.append(f"{child.name}: {child.summary}")
            continue
        try:
            child_context = (
                f"File: {child.file_path}\n"
                f"Chunk: {child.name} ({child.chunk_type.value})\n"
                f"Lines: {child.start_line}-{child.end_line}"
            )
            # If the child itself is oversized, map-reduce it
            child_summary: str | None = None
            try:
                child_summary = provider.summarize(child.content, child_context)
            except Exception as child_exc:
                if _is_context_length_error(child_exc):
                    child_summary = _map_reduce_summarize(child.content, child_context, provider)
                else:
                    raise
            if child_summary:
                store.update_chunk_summary(child.id, child_summary)
                child.summary = child_summary
                method_summaries.append(f"{child.name}: {child_summary}")
        except Exception as e:
            logger.warning("Failed to summarize method %s during class decomposition: %s", child.id, e)

    if not method_summaries:
        return None

    # Step 2: Extract class header
    class_header = _extract_class_header(chunk.content)

    # Step 3: Compose class summary from header + method summaries
    combined_input = f"Class header:\n```\n{class_header}\n```\n\nMethod summaries:\n" + "\n".join(f"- {ms}" for ms in method_summaries)
    compose_context = (
        f"File: {chunk.file_path}\n"
        f"Chunk: {chunk.name} (class)\n"
        f"Lines: {chunk.start_line}-{chunk.end_line}\n"
        f"NOTE: This class was too large to summarize directly. Summarize it based on its header and method summaries."
    )
    try:
        return provider.summarize(combined_input, compose_context)
    except Exception:
        # Even the composed summary failed — return a concatenation of method summaries
        return "; ".join(method_summaries)
```

Add `import re` to the top of the file alongside the existing `import logging`.

These helpers are standalone pure functions with no side effects (except `_decompose_class_chunk` which updates the store — it's a deliberately impure helper for the pipeline).
</action>

<acceptance_criteria>
- `src/glma/summarize/pipeline.py` contains `def _is_context_length_error(exc: Exception) -> bool:`
- `src/glma/summarize/pipeline.py` contains `def _extract_class_header(content: str) -> str:`
- `src/glma/summarize/pipeline.py` contains `def _map_reduce_summarize(`
- `src/glma/summarize/pipeline.py` contains `def _decompose_class_chunk(`
- `_is_context_length_error` returns `True` for strings containing `"context length"`, `"n_ctx"`, `"n_keep"`
- `_is_context_length_error` returns `False` for strings like `"connection refused"`
- `_extract_class_header` returns content before the first `def ` at indent >= 4
- `import re` is present at the top of the file
- All existing tests still pass: `cd 02-worktrees/glma && uv run pytest tests/ -x -q`
</acceptance_criteria>

---

### Task 4: Integrate decomposition into `summarize_chunks()`

<read_first>
- 02-worktrees/glma/src/glma/summarize/pipeline.py — the `summarize_chunks()` function and the new helpers from Task 3
- 02-worktrees/glma/src/glma/models.py — `Chunk` model, especially `parent_id` and `chunk_type` fields
</read_first>

<action>
Replace the `summarize_chunks()` function with a version that catches context-length errors and delegates to decomposition. The function signature stays the same. Here is the full replacement:

```python
def summarize_chunks(
    store: LadybugStore,
    chunks: list[Chunk],
    provider: Protocol,
    max_chunk_chars: int = 3000,
) -> list[Chunk]:
    """Process chunks, generate AI summaries, and persist to database.

    Skips chunks that already have a non-empty summary (incremental mode).
    When a chunk triggers a context-length error from the provider, attempts
    decomposition: class chunks are summarized via their method children,
    standalone chunks are summarized via map-reduce.
    Failed summarization calls are logged and skipped without aborting the pipeline.

    Args:
        store: LadybugStore instance for database updates.
        chunks: List of Chunk objects to summarize.
        provider: SummarizerProvider implementation.
        max_chunk_chars: Character budget hint. Chunks exceeding this trigger
            proactive logging. Actual hard limit is the provider's rejection.

    Returns:
        List of chunks with summaries populated (unchanged for skipped/failed chunks).
    """
    updated: list[Chunk] = []
    summarized_count = 0
    skipped_count = 0
    failed_count = 0
    decomposed_count = 0

    # Build parent_id lookup for class decomposition
    children_by_parent: dict[str, list[Chunk]] = {}
    for c in chunks:
        if c.parent_id:
            children_by_parent.setdefault(c.parent_id, []).append(c)

    for chunk in chunks:
        # Skip chunks that already have a summary (incremental)
        if chunk.summary:
            skipped_count += 1
            updated.append(chunk)
            continue

        # Log proactive warning for oversized chunks (advisory, not a cutoff)
        if len(chunk.content) > max_chunk_chars:
            logger.info(
                "Large chunk detected: %s (%d chars, threshold: %d). Will attempt direct summarization first.",
                chunk.id, len(chunk.content), max_chunk_chars,
            )

        try:
            context = (
                f"File: {chunk.file_path}\n"
                f"Chunk: {chunk.name} ({chunk.chunk_type.value})\n"
                f"Lines: {chunk.start_line}-{chunk.end_line}"
            )
            summary = provider.summarize(chunk.content, context)
            if summary:
                store.update_chunk_summary(chunk.id, summary)
                chunk.summary = summary
                summarized_count += 1
            else:
                logger.warning("Provider returned empty summary for chunk %s", chunk.id)
                failed_count += 1
        except Exception as e:
            # Check if this is a context-length error we can decompose
            if _is_context_length_error(e):
                logger.warning(
                    "Context length error for chunk %s (%d chars). Attempting decomposition.",
                    chunk.id, len(chunk.content),
                )
                summary = _attempt_decomposition(
                    chunk, chunks, children_by_parent, store, provider,
                )
                if summary:
                    store.update_chunk_summary(chunk.id, summary)
                    chunk.summary = summary
                    decomposed_count += 1
                    logger.info("Decomposition succeeded for chunk %s", chunk.id)
                else:
                    logger.warning("Decomposition also failed for chunk %s. Skipping.", chunk.id)
                    failed_count += 1
            else:
                logger.warning("Summarization failed for chunk %s: %s", chunk.id, e)
                failed_count += 1

        updated.append(chunk)

    logger.info(
        "Summarization complete: %d summarized, %d decomposed, %d skipped, %d failed",
        summarized_count, decomposed_count, skipped_count, failed_count,
    )
    return updated


def _attempt_decomposition(
    chunk: Chunk,
    all_chunks: list[Chunk],
    children_by_parent: dict[str, list[Chunk]],
    store: LadybugStore,
    provider: Protocol,
) -> str | None:
    """Attempt to summarize an oversized chunk via decomposition.

    Strategy:
    - Class chunk with method children → summarize methods, compose class summary
    - Standalone chunk → map-reduce

    Args:
        chunk: The oversized chunk that failed direct summarization.
        all_chunks: Full chunk list for the file.
        children_by_parent: Pre-built lookup of parent_id → child chunks.
        store: LadybugStore for persisting intermediate summaries.
        provider: SummarizerProvider.

    Returns:
        Summary string, or None if decomposition fails.
    """
    child_chunks = children_by_parent.get(chunk.id, [])

    if child_chunks:
        # Class decomposition: summarize methods, compose class summary
        logger.info(
            "Decomposing class chunk %s via %d method children",
            chunk.id, len(child_chunks),
        )
        return _decompose_class_chunk(chunk, child_chunks, all_chunks, store, provider)
    else:
        # Map-reduce for standalone oversized chunks
        logger.info(
            "Decomposing standalone chunk %s via map-reduce",
            chunk.id,
        )
        context = (
            f"File: {chunk.file_path}\n"
            f"Chunk: {chunk.name} ({chunk.chunk_type.value})\n"
            f"Lines: {chunk.start_line}-{chunk.end_line}"
        )
        return _map_reduce_summarize(chunk.content, context, provider)
```

**IMPORTANT:** Update the call site in `cli.py` where `summarize_chunks()` is called. The function now accepts `max_chunk_chars` as a keyword argument. Find the line:

```python
summarize_chunks(store, chunks, provider)
```

And change it to:

```python
summarize_chunks(store, chunks, provider, max_chunk_chars=summ_cfg.max_chunk_chars)
```

This is in the `if summarize:` block, inside the `for file_path` loop (around line 130 of cli.py).
</action>

<acceptance_criteria>
- `src/glma/summarize/pipeline.py` contains `def summarize_chunks(` with `max_chunk_chars: int = 3000` parameter
- `src/glma/summarize/pipeline.py` contains `def _attempt_decomposition(`
- `src/glma/summarize/pipeline.py` calls `_is_context_length_error(e)` inside the except block
- `src/glma/summarize/pipeline.py` builds `children_by_parent` dict from chunks
- `src/glma/summarize/pipeline.py` logs `"Context length error for chunk"` on context-length failures
- `src/glma/summarize/pipeline.py` logs `"Decomposition succeeded for chunk"` on success
- `src/glma/cli.py` passes `max_chunk_chars=summ_cfg.max_chunk_chars` to `summarize_chunks()`
- Log message includes `"decomposed"` count in the summary line
- All existing tests still pass: `cd 02-worktrees/glma && uv run pytest tests/ -x -q`
</acceptance_criteria>

---

### Task 5: Write tests for decomposition pipeline

<read_first>
- 02-worktrees/glma/tests/test_summarize.py — existing test patterns (MockProvider, FailingProvider, fixtures)
- 02-worktrees/glma/src/glma/summarize/pipeline.py — new helpers from Tasks 3-4
- 02-worktrees/glma/src/glma/models.py — Chunk, ChunkType for creating test fixtures
</read_first>

<action>
Add the following test classes to `tests/test_summarize.py`. Keep all existing tests unchanged.

```python
class ContextLengthError(Exception):
    """Simulates an OpenAI-compatible context length error."""
    def __init__(self, msg: str = "Error code: 400 - context_length_exceeded"):
        super().__init__(msg)
        self.status_code = 400


class OversizedChunkProvider:
    """Provider that raises context-length error for chunks > threshold chars."""

    def __init__(self, threshold: int = 500, response_prefix: str = "Summary of"):
        self.calls: list[tuple[str, str]] = []
        self.threshold = threshold
        self.response_prefix = response_prefix

    def summarize(self, code: str, context: str) -> str:
        self.calls.append((code, context))
        if len(code) > self.threshold:
            raise ContextLengthError(
                f"Error code: 400 - The number of tokens exceeds the context length ({len(code)} chars)"
            )
        return f"{self.response_prefix}: {context.split(chr(10))[1] if chr(10) in context else 'chunk'}"


class TestIsContextLengthError:
    """Test the _is_context_length_error helper."""

    def test_detects_context_length(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("context length exceeded")) is True

    def test_detects_n_ctx(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("n_keep: 8312 >= n_ctx: 4096")) is True

    def test_detects_token_limit(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("token limit exceeded")) is True

    def test_rejects_connection_error(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(ConnectionError("connection refused")) is False

    def test_rejects_generic_500(self):
        from glma.summarize.pipeline import _is_context_length_error
        assert _is_context_length_error(RuntimeError("internal server error")) is False


class TestExtractClassHeader:
    """Test the _extract_class_header helper."""

    def test_extracts_header_before_methods(self):
        from glma.summarize.pipeline import _extract_class_header
        content = "class Foo:\n    \"\"\"Docstring.\"\"\"\n    x = 1\n\n    def bar(self):\n        pass\n\n    def baz(self):\n        pass"
        header = _extract_class_header(content)
        assert "class Foo:" in header
        assert "Docstring" in header
        assert "x = 1" in header
        assert "def bar" not in header
        assert "def baz" not in header

    def test_handles_class_with_no_methods(self):
        from glma.summarize.pipeline import _extract_class_header
        content = "class Foo:\n    x = 1\n    y = 2"
        header = _extract_class_header(content)
        assert header == content

    def test_truncates_at_1500_chars(self):
        from glma.summarize.pipeline import _extract_class_header
        content = "class Foo:\n" + "    x = 1\n" * 200  # ~2000+ chars
        header = _extract_class_header(content)
        assert len(header) <= 1560  # 1500 + truncation marker


class TestMapReduceSummarize:
    """Test the _map_reduce_summarize helper."""

    def test_splits_and_combines(self):
        from glma.summarize.pipeline import _map_reduce_summarize
        provider = MockProvider()
        content = "x" * 300  # Small enough that each segment fits
        result = _map_reduce_summarize(content, "File: test.py", provider, segment_chars=200, overlap_chars=50)
        assert result  # Got a summary
        assert len(provider.calls) >= 2  # At least 2 segment calls + 1 combine

    def test_returns_empty_on_total_failure(self):
        from glma.summarize.pipeline import _map_reduce_summarize
        provider = FailingProvider()
        result = _map_reduce_summarize("some content", "context", provider)
        assert result == ""


class TestDecompositionIntegration:
    """Integration tests for the full decomposition pipeline in summarize_chunks."""

    def test_class_decomposition_on_context_error(
        self, store, sample_file_record
    ):
        """Oversized class chunk triggers class decomposition when method children exist."""
        store.upsert_file(sample_file_record)

        # Create a class chunk with oversized content
        class_content = "class BigClass:\n    \"\"\"A big class.\"\"\"\n" + "    x = 1\n" * 200
        class_chunk = Chunk(
            id="src/main.c::class::BigClass::5",
            file_path="src/main.c",
            chunk_type=ChunkType.CLASS,
            name="BigClass",
            content=class_content,
            summary=None,
            start_line=5,
            end_line=210,
            content_hash="class_hash",
            parent_id=None,
        )
        # Create method children (small, should summarize fine)
        method_chunk = Chunk(
            id="src/main.c::method::do_thing::10",
            file_path="src/main.c",
            chunk_type=ChunkType.METHOD,
            name="do_thing",
            content="def do_thing(self):\n    return 42",
            summary=None,
            start_line=10,
            end_line=11,
            content_hash="method_hash",
            parent_id="src/main.c::class::BigClass::5",
        )
        store.upsert_chunks("src/main.c", [class_chunk, method_chunk])

        # Provider that fails for large content, succeeds for small
        provider = OversizedChunkProvider(threshold=100)
        result = summarize_chunks(
            store, [class_chunk, method_chunk], provider, max_chunk_chars=100,
        )

        # Class chunk should have a summary via decomposition
        assert result[0].summary is not None
        # Method chunk should have a direct summary
        assert result[1].summary is not None

    def test_map_reduce_for_standalone_oversized(
        self, store, sample_file_record
    ):
        """Oversized standalone chunk (no children) triggers map-reduce."""
        store.upsert_file(sample_file_record)

        big_content = "def huge_function():\n" + "    x = 1\n" * 300
        big_chunk = Chunk(
            id="src/main.c::function::huge_function::5",
            file_path="src/main.c",
            chunk_type=ChunkType.FUNCTION,
            name="huge_function",
            content=big_content,
            summary=None,
            start_line=5,
            end_line=310,
            content_hash="big_hash",
            parent_id=None,
        )
        store.upsert_chunks("src/main.c", [big_chunk])

        provider = OversizedChunkProvider(threshold=100)
        result = summarize_chunks(
            store, [big_chunk], provider, max_chunk_chars=100,
        )

        assert result[0].summary is not None

    def test_graceful_failure_when_decomposition_also_fails(
        self, store, sample_file_record
    ):
        """If both direct and decomposed summarization fail, chunk is skipped."""
        store.upsert_file(sample_file_record)

        big_chunk = Chunk(
            id="src/main.c::function::big::5",
            file_path="src/main.c",
            chunk_type=ChunkType.FUNCTION,
            name="big",
            content="x" * 1000,
            summary=None,
            start_line=5,
            end_line=10,
            content_hash="hash_big",
            parent_id=None,
        )
        store.upsert_chunks("src/main.c", [big_chunk])

        # Provider that always fails (even for small segments)
        provider = FailingProvider()
        result = summarize_chunks(
            store, [big_chunk], provider, max_chunk_chars=100,
        )

        assert result[0].summary is None  # Failed gracefully
        assert len(result) == 1  # Didn't crash

    def test_max_chunk_chars_default(self):
        """Verify default max_chunk_chars is 3000."""
        from glma.models import SummarizeConfig
        cfg = SummarizeConfig()
        assert cfg.max_chunk_chars == 3000

    def test_max_chunk_chars_from_config(self):
        """Verify max_chunk_chars loads from config dict."""
        from glma.models import SummarizeConfig
        cfg = SummarizeConfig(max_chunk_chars=5000)
        assert cfg.max_chunk_chars == 5000
```

These tests cover:
- `_is_context_length_error` — positive and negative cases
- `_extract_class_header` — normal, no-methods, and truncation cases
- `_map_reduce_summarize` — splitting behavior and total failure
- Full pipeline integration — class decomposition, map-reduce, and graceful failure
- Config field — default and explicit values
</action>

<acceptance_criteria>
- `tests/test_summarize.py` contains `class TestIsContextLengthError:` with 5 tests
- `tests/test_summarize.py` contains `class TestExtractClassHeader:` with 3 tests
- `tests/test_summarize.py` contains `class TestMapReduceSummarize:` with 2 tests
- `tests/test_summarize.py` contains `class TestDecompositionIntegration:` with 4 tests
- `cd 02-worktrees/glma && uv run pytest tests/test_summarize.py -v` — all new and existing tests pass
- Total test count increases by 14+ (5 + 3 + 2 + 4)
</acceptance_criteria>

---

### Task 6: Run full test suite and verify

<read_first>
- 02-worktrees/glma/tests/test_summarize.py — all tests (existing + new)
- 02-worktrees/glma/tests/test_config.py — verify config tests still pass
</read_first>

<action>
Run the complete test suite to verify nothing is broken:

```bash
cd 02-worktrees/glma && uv run pytest tests/ -x -v
```

If any tests fail, fix the root cause. Common issues to check:
1. `test_summarize.py` existing tests may break if `summarize_chunks()` signature changed — verify the `max_chunk_chars` parameter has a default value of 3000 so existing calls without it still work.
2. `test_cli.py` tests that invoke `index()` — the new `max_chunk_chars` parameter has `Optional[int]` type with `None` default, so existing CLI tests should pass.
3. `test_config.py` tests that instantiate `SummarizeConfig()` — the new field has a default, so no breakage.

Then run with coverage to see decomposition code is exercised:

```bash
cd 02-worktrees/glma && uv run pytest tests/test_summarize.py -v --tb=short
```

Verify the total test count is 274 + 14 = 288 or more.
</action>

<acceptance_criteria>
- `cd 02-worktrees/glma && uv run pytest tests/ -x -q` exits with code 0
- Total test count is ≥ 288 (274 existing + 14 new)
- `test_summarize.py` shows all tests passing (existing 8 + new 14 = 22)
- `test_config.py` tests still pass
- `test_cli.py` tests still pass
</acceptance_criteria>

---

## Verification

1. `cd 02-worktrees/glma && uv run pytest tests/ -x -q` — all tests pass
2. `uv run glma index --help | grep -- --max-chunk-chars` — flag is documented
3. `grep -c "def _is_context_length_error\|def _extract_class_header\|def _map_reduce_summarize\|def _decompose_class_chunk\|def _attempt_decomposition" src/glma/summarize/pipeline.py` — returns 5 (all helpers present)
4. `grep "max_chunk_chars" src/glma/models.py` — config field exists
5. `grep "max_chunk_chars" src/glma/cli.py` — CLI flag wired up

## must_haves

- [ ] `summarize_chunks()` catches context-length errors and attempts decomposition
- [ ] Class chunks with method children are decomposed via method summaries → class summary
- [ ] Standalone oversized chunks are decomposed via map-reduce
- [ ] Decomposition failures are logged and the chunk is skipped (no crash)
- [ ] `max_chunk_chars` config field exists with default 3000
- [ ] `--max-chunk-chars` CLI flag works
- [ ] All 274 existing tests still pass
- [ ] New tests cover decomposition paths
