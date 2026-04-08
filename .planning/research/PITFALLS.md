# Pitfalls Research

**Domain:** Codebase indexing CLI tool with graph database and semantic search
**Researched:** 2026-04-08
**Confidence:** MEDIUM

## Critical Pitfalls

### Pitfall 1: Relationship Extraction Accuracy (The Hackathon Wall)

**What goes wrong:**
Extracting "function A calls function B" seems straightforward but is deceptively hard. Tree-sitter gives you AST nodes, but resolving which actual function is being called requires:
- Handling aliases (`import foo; foo.bar()` → `bar` belongs to `foo`)
- Handling `self.method()` → need to know the class context
- Handling function pointers/callbacks → static analysis can't resolve these
- Handling macros (C) → preprocessor directives aren't in the AST
- Handling dynamic dispatch (Python) → `obj.method()` could call any subclass

**Why it happens:**
Developers expect graph-database-quality relationships from static analysis alone. Static analysis has fundamental limits for dynamic languages.

**How to avoid:**
- Start with what's resolvable: direct function calls, explicit imports, class inheritance
- Tag relationships with confidence levels (DIRECT_CALL vs POSSIBLE_CALL)
- Don't try to resolve everything — 80% accuracy on relationships is enormously valuable
- Use heuristics for common patterns (e.g., `self.method()` → look up method in current class hierarchy)

**Warning signs:**
- Spending weeks trying to resolve indirect calls
- Relationship accuracy below ~70% for common patterns
- Special-casing every language feature

**Phase to address:** Phase 2 (relationship extraction) — design for partial resolution from the start

### Pitfall 2: Comment Attachment (Known from Hackathon)

**What goes wrong:**
Single-line comments (`//` in C, `#` in Python) are separate AST nodes in tree-sitter. They don't attach to the following code block. A function with a doc comment gets chunked as two separate pieces.

**Why it happens:**
Tree-sitter's grammar treats comments as trivia nodes, not part of the function definition node.

**How to avoid:**
- Custom post-processing: walk AST siblings, attach preceding comment nodes to their following code node
- Handle both single-line (`//`, `#`) and block comments (`/* */`, `""" """"`)
- This is a solved problem — most code intelligence tools do this as a post-pass

**Warning signs:**
- Code chunks missing their docstrings or explanatory comments
- Users saying "the context is incomplete"

**Phase to address:** Phase 1 (chunking) — solve early, affects everything downstream

### Pitfall 3: Large Repo Performance

**What goes wrong:**
Linux kernel has 35K+ C files. Naive parsing of every file sequentially takes hours. Memory usage balloons when holding all ASTs in memory simultaneously.

**Why it happens:**
Sequential processing + in-memory accumulation + no parallelism = slow

**How to avoid:**
- Stream processing: parse → extract → write → discard (don't hold all ASTs)
- Parallel file processing (multiprocessing or async)
- Progress tracking with estimated time remaining
- Early bailout: skip files that haven't changed (content hash comparison)

**Warning signs:**
- Indexing takes >10 minutes for a medium repo
- Memory usage >2GB during indexing
- Users killing the process thinking it's hung

**Phase to address:** Phase 1 (indexing) — design for streaming from the start

### Pitfall 4: Index Staleness

**What goes wrong:**
Code changes but the index doesn't update. Agents query stale data and get wrong context. This is worse than no index at all — agents trust the index.

**Why it happens:**
File watching isn't set up, or the watcher misses changes (rename, move, delete edge cases), or the incremental update logic has bugs.

**How to avoid:**
- Content hash-based staleness detection (don't rely on timestamps alone)
- Show index age in query results: "Index updated 2 hours ago"
- Support explicit `glma index --force` for full rebuild
- Validate index integrity on query (spot-check a few files)

**Warning signs:**
- Query results show deleted functions
- Agents implement features based on old API signatures

**Phase to address:** Phase 3 (file watching / incremental updates)

## Moderate Pitfalls

### Pitfall 5: Notebook Compaction Complexity

**What goes wrong:**
Jupyter notebooks are JSON with embedded outputs, metadata, and execution state. Naive extraction misses:
- Variable definitions that span cells (cell 1 defines `x`, cell 5 uses `x`)
- Import statements in earlier cells that affect later cells
- Cell execution order ≠ cell document order
- Output contamination (cell outputs may contain sensitive data)

**Prevention:**
- Parse the notebook as a linear execution sequence, not individual cells
- Track variable scope across cells (simple def-use analysis)
- Strip outputs by default (configurable)
- Handle non-code cells (markdown) as context markers

### Pitfall 6: Embedding Quality vs. Speed

**What goes wrong:**
Large embedding models give better semantic search but are slow and memory-heavy. Local models may not capture code semantics well. Wrong model choice = semantic search feels useless.

**Prevention:**
- Start with `all-MiniLM-L6-v2` (fast, good general quality)
- Evaluate with real queries against the indexed codebase
- Consider code-specific models (CodeBERT, UniXcoder) as future optimization
- Make embedding model configurable

### Pitfall 7: Markdown Information Overload

**What goes wrong:**
Dumping ALL chunk content + ALL relationships for a large file produces 500+ lines of markdown. Agents have context windows too — too much context is as bad as too little.

**Prevention:**
- Default: summary + function signatures + relationship list (not full code)
- `--verbose` flag: include full code for each chunk
- Smart truncation: show most relevant chunks first, reference others
- File-level summary at the top (what this file does, key exports)

## Minor Pitfalls

### Pitfall 8: Binary File Handling

**What goes wrong:** Indexing crashes on binary files (images, compiled objects, `.so` files)
**Prevention:** Skip files matching binary patterns; detect binary via file header or extension

### Pitfall 9: Encoding Issues

**What goes wrong:** Files with non-UTF-8 encoding cause parse errors
**Prevention:** Try UTF-8 first, fall back to latin-1, skip files that can't be decoded

### Pitfall 10: Circular Dependencies

**What goes wrong:** A imports B, B imports A → infinite loop in relationship traversal
**Prevention:** Track visited nodes during relationship traversal; limit depth

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Language detection | Wrong grammar for ambiguous extensions (`.h` could be C or C++) | Default to C, try both, use heuristics |
| Chunking | Overly granular chunks (every expression as a chunk) | Chunk at function/class/module level only |
| Relationship extraction | False positives (same function name in different scopes) | Include fully qualified names where possible |
| Markdown output | Too much output, drowning the agent | Layered output: summary → details → full code |
| File watching | Missing changes during rapid edits | Debounce file events; hash-based verification |
| Air-gapped export | Exported markdown is stale | Include generation timestamp; make re-export easy |
| Embedding generation | Slow first-run (downloading model) | Download model during `glma index`, show progress |

## Sources

- Direct hackathon experience (pitfalls 2, 3, 4)
- tree-sitter documentation and community issues
- Code intelligence tool post-mortems (Sourcegraph blog, Aider discussions)
- LanceDB documentation and performance guidelines
- Confidence: MEDIUM-HIGH for hackathon-validated pitfalls; MEDIUM for anticipated pitfalls
