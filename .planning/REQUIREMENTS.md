# Requirements: glma

**Defined:** 2026-04-08
**Core Value:** Agents can call a single command and get exactly the code context they need to implement features — no grepping, no raw file parsing, no guesswork.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Indexing

- [ ] **IDXC-01**: User can point the CLI at a repo directory and index all supported files
- [ ] **IDXC-02**: Tool walks directory tree, skipping .git, venvs, node_modules, and other non-source directories
- [ ] **IDXC-03**: Tool auto-detects language from file extension and selects correct tree-sitter grammar
- [ ] **IDXC-04**: Tool parses files with tree-sitter and extracts semantic chunks (functions, classes, methods, module-level code)
- [ ] **IDXC-05**: Tool attaches comments (single-line and block) to their associated code chunks via AST post-processing
- [ ] **IDXC-06**: Tool tracks file content hashes for incremental re-indexing (only re-process changed files)
- [ ] **IDXC-07**: Tool supports C language parsing with tree-sitter-c grammar
- [ ] **IDXC-08**: Tool supports Python language parsing with tree-sitter-python grammar
- [ ] **IDXC-09**: Tool processes files in a streaming fashion (parse → extract → write → discard) for memory efficiency on large repos
- [ ] **IDXC-10**: Tool shows progress during indexing (files processed, estimated time remaining)

### Relationships

- [ ] **RELS-01**: Tool extracts direct function call relationships from AST (function A calls function B)
- [ ] **RELS-02**: Tool extracts import/dependency relationships (file A imports from file B)
- [ ] **RELS-03**: Tool extracts class inheritance relationships (class A extends class B)
- [ ] **RELS-04**: Tool stores all relationships in a queryable format in LanceDB
- [ ] **RELS-05**: Tool confidence-tags relationships as DIRECT or INFERRED based on static analysis certainty
- [ ] **RELS-06**: Tool resolves import aliases (e.g., `import foo; foo.bar()` → identifies `bar` from `foo`)
- [ ] **RELS-07**: Tool resolves `self.method()` calls to the correct class method

### Storage

- [ ] **STOR-01**: Tool stores code chunks in LanceDB with fields: id, file_path, chunk_type, name, content, embedding (optional), metadata
- [ ] **STOR-02**: Tool stores relationships in LanceDB with fields: source_id, target_id, rel_type, confidence
- [ ] **STOR-03**: Tool writes markdown files alongside LanceDB for each indexed file (dual output)
- [ ] **STOR-04**: Tool generates a file-level summary markdown (what this file does, key exports, key functions)
- [ ] **STOR-05**: Index is stored in `.glma-index/` directory within the target repo

### Query Tool

- [ ] **QURY-01**: User can query by file path and get compacted context as markdown
- [ ] **QURY-02**: Query output includes incoming dependencies (what other files use this file's functions)
- [ ] **QURY-03**: Query output includes outgoing dependencies (what this file depends on)
- [ ] **QURY-04**: Query output includes function/class signatures with their docstrings
- [ ] **QURY-05**: Query output uses layered format: file summary → signatures → details → full code (controllable via flags)

### Jupyter Compaction

- [ ] **JNTP-01**: Tool parses .ipynb files via nbformat and extracts code cells, markdown cells, and outputs separately
- [ ] **JNTP-02**: Tool tracks variable definitions and usages across notebook cells (cell 1 defines x, cell 5 uses x)
- [ ] **JNTP-03**: Tool generates compacted markdown for notebooks: cell index, code, variables defined, variables referenced
- [ ] **JNTP-04**: Tool strips cell outputs by default (configurable) to reduce noise

### CLI Interface

- [ ] **CLIF-01**: CLI provides `glma index <path>` command to index a repository
- [ ] **CLIF-02**: CLI provides `glma query <filepath>` command to query indexed context
- [ ] **CLIF-03**: CLI provides `glma watch <path>` command to watch for changes and incrementally update
- [ ] **CLIF-04**: CLI provides `glma export <path>` command to generate full air-gapped markdown export
- [ ] **CLIF-05**: CLI shows index metadata (when last indexed, number of files, number of chunks) on query

### File Watching

- [ ] **WTCH-01**: Tool detects file changes (create, modify, delete, rename) in the indexed repo
- [ ] **WTCH-02**: Tool incrementally re-indexes only changed files when changes detected
- [ ] **WTCH-03**: Tool updates both LanceDB and markdown when files change (keeps dual output in sync)

### Air-Gapped Mode

- [ ] **AIRG-01**: User can export the full index as static markdown files requiring no runtime to consume
- [ ] **AIRG-02**: Exported markdown includes all chunks, relationships, and file summaries
- [ ] **AIRG-03**: Shell-only agents can `cat` exported markdown files and get full codebase context

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Semantic Search

- **SEMS-01**: User can search by natural language query ("find authentication code") and get semantically relevant chunks
- **SEMS-02**: Tool generates vector embeddings for code chunks using local sentence-transformers model
- **SEMS-03**: Tool supports configurable embedding models (local or API-based)

### Extended Language Support

- **LANG-01**: Tool supports C++ language parsing
- **LANG-02**: Tool supports TypeScript/JavaScript parsing
- **LANG-03**: Tool supports Rust parsing
- **LANG-04**: Language plugin system for community-contributed grammars

### Advanced Features

- **ADVN-01**: Import/call graph visualization (graphviz or mermaid output)
- **ADVN-02**: Cross-file variable reference tracking (where is `config` used across the whole repo?)
- **ADVN-03**: LLM-powered code summaries (optional enhancement for each chunk)
- **ADVN-04**: MCP server interface for direct agent integration

## Out of Scope

| Feature | Reason |
|---------|--------|
| IDE plugin/integration | IDEs have their own indexing; CLI-first is the design |
| Code execution | Security risk, scope explosion; read-only analysis only |
| Web UI / dashboard | Agents and humans consume markdown, no visual interface needed |
| Multi-user sync | Single-user tool, file-based output shared via git |
| Binary file analysis | Only parse text-based source code |
| Real-time collaboration | Would require server infrastructure; out of scope |
| Custom per-language AST parsers | tree-sitter provides uniform parsing across languages |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| IDXC-01 | Phase 1 | Pending |
| IDXC-02 | Phase 1 | Pending |
| IDXC-03 | Phase 1 | Pending |
| IDXC-04 | Phase 1 | Pending |
| IDXC-05 | Phase 1 | Pending |
| IDXC-06 | Phase 1 | Pending |
| IDXC-07 | Phase 1 | Pending |
| IDXC-08 | Phase 1 | Pending |
| IDXC-09 | Phase 1 | Pending |
| IDXC-10 | Phase 1 | Pending |
| RELS-01 | Phase 2 | Pending |
| RELS-02 | Phase 2 | Pending |
| RELS-03 | Phase 2 | Pending |
| RELS-04 | Phase 2 | Pending |
| RELS-05 | Phase 2 | Pending |
| RELS-06 | Phase 2 | Pending |
| RELS-07 | Phase 2 | Pending |
| STOR-01 | Phase 1 | Pending |
| STOR-02 | Phase 2 | Pending |
| STOR-03 | Phase 1 | Pending |
| STOR-04 | Phase 2 | Pending |
| STOR-05 | Phase 1 | Pending |
| QURY-01 | Phase 3 | Pending |
| QURY-02 | Phase 3 | Pending |
| QURY-03 | Phase 3 | Pending |
| QURY-04 | Phase 3 | Pending |
| QURY-05 | Phase 3 | Pending |
| JNTP-01 | Phase 3 | Pending |
| JNTP-02 | Phase 3 | Pending |
| JNTP-03 | Phase 3 | Pending |
| JNTP-04 | Phase 3 | Pending |
| CLIF-01 | Phase 1 | Pending |
| CLIF-02 | Phase 3 | Pending |
| CLIF-03 | Phase 4 | Pending |
| CLIF-04 | Phase 4 | Pending |
| CLIF-05 | Phase 3 | Pending |
| WTCH-01 | Phase 4 | Pending |
| WTCH-02 | Phase 4 | Pending |
| WTCH-03 | Phase 4 | Pending |
| AIRG-01 | Phase 4 | Pending |
| AIRG-02 | Phase 4 | Pending |
| AIRG-03 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 42 total
- Mapped to phases: 42
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-08*
*Last updated: 2026-04-08 after initial definition*
