# Roadmap: glma

## Overview

Build a CLI tool that indexes codebases into a queryable graph database with companion markdown output. AI agents query it to get compacted, relevant code context instead of grepping raw files. Starts with tree-sitter parsing for C and Python, extracts structural relationships (calls, imports, inheritance), and outputs markdown that works even in air-gapped environments.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Core Indexing Pipeline** - Parse repos with tree-sitter, extract chunks, store in LanceDB + markdown
- [ ] **Phase 2: Relationship Extraction** - Extract calls, imports, and inheritance relationships from ASTs
- [ ] **Phase 3: Query Tool & Notebook Compaction** - CLI query interface, Jupyter compaction, layered markdown output
- [ ] **Phase 4: File Watching & Air-Gapped Export** - Live sync, incremental updates, static markdown export

## Phase Details

### Phase 1: Core Indexing Pipeline
**Goal**: User can point `glma index` at any repo and get a fully parsed index of all C and Python files, stored in LanceDB with companion markdown files
**Depends on**: Nothing (first phase)
**Requirements**: IDXC-01, IDXC-02, IDXC-03, IDXC-04, IDXC-05, IDXC-06, IDXC-07, IDXC-08, IDXC-09, IDXC-10, STOR-01, STOR-03, STOR-05, CLIF-01
**Success Criteria** (what must be TRUE):
  1. Running `glma index /path/to/repo` creates `.glma-index/` with a LanceDB database and markdown files for every C and Python file found
  2. Each markdown file contains the extracted chunks (functions, classes, methods) with their associated comments attached
  3. Re-running `glma index` on the same repo only re-processes files whose content hash has changed
  4. Indexing shows progress (files processed count, spinner or progress bar) and completes without crashing on repos with 10K+ files
  5. Binary files, .git directories, venvs, and node_modules are automatically skipped
**Plans**: TBD

Plans:
- [x] 01-01: Project scaffolding, CLI entry point, Ladybug store
- [x] 01-02: Language detection, tree-sitter parsing pipeline, chunk extraction
- [x] 01-03: Comment attachment, markdown output, progress display
- [x] 01-04: Content hashing, incremental re-indexing, integration testing

### Phase 2: Relationship Extraction
**Goal**: The index contains structural relationships (function calls, imports, inheritance) that agents can follow to understand how code connects across files
**Depends on**: Phase 1
**Requirements**: RELS-01, RELS-02, RELS-03, RELS-04, RELS-05, RELS-06, RELS-07, STOR-02, STOR-04
**Success Criteria** (what must be TRUE):
  1. After indexing, querying a function shows what other functions it calls and what functions call it
  2. Import relationships are resolved (including aliases like `import foo; foo.bar()`) and stored in the database
  3. Class inheritance is extracted (class A extends class B) and visible in markdown output
  4. Each relationship is tagged as DIRECT or INFERRED based on analysis confidence
  5. `self.method()` calls are resolved to the correct class method
**Plans**: 3 plans across 3 waves

Plans:
- [ ] 02-01: Relationship data model, LanceDB relationships table, C relationship extraction
- [ ] 02-02: Python relationship extraction, import alias resolution, self.method() resolution
- [ ] 02-03: Confidence tagging, relationship markdown output, cross-file resolution

### Phase 3: Query Tool & Notebook Compaction
**Goal**: Agents can call `glma query <filepath>` and get back compacted, relevant context as markdown — including Jupyter notebooks flattened into readable form
**Depends on**: Phase 2
**Requirements**: QURY-01, QURY-02, QURY-03, QURY-04, QURY-05, JNTP-01, JNTP-02, JNTP-03, JNTP-04, CLIF-02, CLIF-05
**Success Criteria** (what must be TRUE):
  1. `glma query src/auth/login.py` outputs markdown with file summary, function signatures with docstrings, incoming dependencies, and outgoing dependencies
  2. Query output uses layered format by default (summary → signatures → details) and includes full code with `--verbose` flag
  3. Jupyter notebooks (.ipynb) are compacted into markdown showing cell index, code, variables defined, and variables referenced per cell
  4. Cell outputs are stripped by default; variable definitions are tracked across cells (cell 1 defines `x`, cell 5 uses `x`)
  5. Query results show index metadata (last indexed timestamp, number of chunks in file)
**Plans**: TBD

Plans:
- [ ] 03-01: CLI query command, file lookup, layered markdown formatting
- [ ] 03-02: Jupyter notebook parsing, variable tracking, notebook compaction
- [ ] 03-03: Dependency inclusion in output, verbose mode, index metadata display

### Phase 4: File Watching & Air-Gapped Export
**Goal**: The index stays in sync as code changes, and the full index can be exported as static markdown for zero-runtime environments
**Depends on**: Phase 3
**Requirements**: WTCH-01, WTCH-02, WTCH-03, AIRG-01, AIRG-02, AIRG-03, CLIF-03, CLIF-04
**Success Criteria** (what must be TRUE):
  1. Running `glma watch /path/to/repo` detects file changes (create, modify, delete, rename) and incrementally re-indexes only affected files
  2. Both LanceDB and markdown files stay in sync after changes — querying returns current data, not stale data
  3. Running `glma export /path/to/repo` generates a complete markdown export in a specified directory that contains all chunks, relationships, and file summaries
  4. A shell-only agent (no Python runtime) can `cat` the exported markdown files and have full codebase context sufficient to implement features
**Plans**: TBD

Plans:
- [ ] 04-01: File watcher with watchfiles, incremental re-indexing, dual output sync
- [ ] 04-02: Air-gapped markdown export, full index serialization, validation

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Core Indexing Pipeline | 4/4 | Complete | 2026-04-08 |
| 2. Relationship Extraction | 0/3 | Planned | - |
| 3. Query Tool & Notebook Compaction | 0/3 | Not started | - |
| 4. File Watching & Air-Gapped Export | 0/2 | Not started | - |
