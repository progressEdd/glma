# Feature Research

**Domain:** Codebase indexing CLI tool with graph database and semantic search
**Researched:** 2026-04-08
**Confidence:** MEDIUM

## Feature Landscape

### Table Stakes (Users Expect These)

Features users assume exist. Missing these = product feels incomplete.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Point-at-repo indexing | This IS the tool — `glma index /path/to/repo` should just work | MEDIUM | Walk directory, detect languages, parse, chunk, store |
| File-level code chunking | Tree-sitter parses files into functions, classes, methods — these are the fundamental units | MEDIUM | Already prototyped in hackathon; needs generalization |
| Relationship extraction | "What calls this function?" — the core value prop that grep can't do | HIGH | The hackathon wall. Requires AST traversal to extract calls, imports, inheritance |
| Query by file path | `glma query src/auth/login.py` returns compacted context | LOW | Lookup by file path, return associated chunks + relationships |
| Markdown output | Agents and humans need readable output, not JSON blobs | LOW | Format chunks + relationships as markdown sections |
| Language auto-detection | File extension → tree-sitter grammar, no manual config | LOW | Simple mapping table: `.c` → C, `.py` → Python, etc. |
| Incremental re-indexing | Only re-parse changed files, don't nuke and rebuild | MEDIUM | Track file hashes/timestamps, only re-process deltas |
| Python and C support | Starting languages, must work reliably | LOW | Grammars already installed and tested |

### Differentiators (Competitive Advantage)

Features that set the product apart. Not required, but valuable.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Jupyter notebook compaction | Flatten `.ipynb` into readable markdown (cell index, code, variables, references) — no other tool does this well | MEDIUM | Parse nbformat JSON, extract cells, trace variable definitions and usages |
| Air-gapped mode | Static markdown files that ARE the database — work with zero runtime deps | MEDIUM | Export all indexed data as markdown files; agents `cat` them instead of querying |
| Semantic search | "Find me code that handles authentication" — not just grep, but meaning-based search | HIGH | Requires embedding model + vector similarity. Local model for air-gapped compat |
| File watching / live sync | `glma watch` — keeps index in sync as code changes | MEDIUM | watchfiles for detection, incremental re-indexing for updates |
| Variable reference tracking | Show where variables are defined and used across files | HIGH | Requires cross-file scope analysis; complex but extremely valuable for agents |
| Import/call graph generation | Visualize or list the dependency graph for a function/file | MEDIUM | Leverage relationship data; output as markdown tree or graphviz |
| Extensible language support | Plugin system for adding new tree-sitter grammars | LOW | Design for it from the start; grammar registry + auto-download |

### Anti-Features

Features to explicitly NOT build.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| IDE integration / plugin | Scope creep; IDEs have their own indexing (LSP, etc.) | CLI-first, output consumable by any tool |
| Code execution | Security risk, scope explosion | Read-only analysis only |
| Real-time collaboration | Single-user tool, adds massive complexity | File-based output that can be shared via git |
| Web UI / dashboard | Not the target use case; agents consume markdown | CLI output + markdown files |
| LLM-dependent indexing | Air-gapped requirement means indexing must work offline | Embeddings optional; structural indexing always works offline |
| Custom AST analysis per language | N parsers = N codebases to maintain | Tree-sitter provides uniform AST across all languages |

## Feature Dependencies

```
Point-at-repo indexing → File-level chunking → Relationship extraction
                                         ↓
                                   Markdown output ← Query by file path
                                         ↓
                              Jupyter notebook compaction (parallel path)
                                         ↓
                              Semantic search (requires embeddings)
                                         ↓
                              Air-gapped mode (markdown export of everything)
                                         ↓
                              File watching (requires incremental re-indexing)
```

**Critical dependency chain:** Chunking must work before relationships can be extracted. Relationships must work before the query tool is useful (beyond just "show me file contents"). Semantic search is an enhancement layer on top.

## MVP Recommendation

Prioritize:
1. Point-at-repo indexing with C and Python support
2. File-level code chunking with tree-sitter
3. Relationship extraction (the core differentiator)
4. Query by file path returning compacted markdown
5. Markdown output (human + agent readable)

Defer:
- **Semantic search:** Requires embedding infrastructure; structural queries cover 80% of use cases first
- **File watching:** Index-on-demand is sufficient for MVP
- **Air-gapped mode:** Full markdown export can come after basic markdown output is solid

## Sources

- Existing hackathon experience (validated chunking, identified relationship extraction as wall)
- tree-sitter capabilities documentation
- LanceDB feature set
- Code intelligence tools landscape (Sourcegraph, Aider, Cursor's indexing)
- Confidence: MEDIUM — feature analysis based on domain understanding, not user research
