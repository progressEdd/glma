# Project Research Summary

**Project:** glma
**Domain:** Codebase indexing CLI tool with graph database and semantic search
**Researched:** 2026-04-08
**Overall confidence:** MEDIUM

## Executive Summary

glma is a CLI tool that transforms a codebase into a queryable index combining structural relationships (function calls, imports, inheritance) with semantic search. The tool addresses a real gap: AI coding agents currently grep raw files and parse notebook JSON manually, losing the structural understanding that would let them implement features efficiently.

The recommended approach uses tree-sitter for language-agnostic parsing, LanceDB as a unified storage layer (vector embeddings + metadata tables for relationships), and markdown as the primary output format. This combination uniquely satisfies the air-gapped requirement — markdown files serve as a zero-dependency database that shell-only agents can consume.

The primary risk is relationship extraction accuracy. The hackathon hit this wall: tree-sitter provides AST nodes but resolving which function is actually being called (handling aliases, dynamic dispatch, macros) requires careful design. The mitigation is to design for partial resolution from the start — 80% accuracy on direct calls and explicit imports is enormously more valuable than grep, without attempting the impossible goal of perfect static analysis.

## Key Findings

**Stack:** Python 3.13 + tree-sitter + LanceDB + sentence-transformers. LanceDB chosen over Ladybug/Kuzu because it unifies vector search and metadata storage in a single embedded database, avoiding the need to run both a graph DB and a separate vector store. Local embeddings via sentence-transformers satisfy the air-gapped requirement.

**Architecture:** Four-layer pipeline (CLI → Pipeline → Storage → Output). Language plugin pattern for extensibility. Dual output to LanceDB and markdown simultaneously. Streaming processing for large repos.

**Critical pitfall:** Relationship extraction is the hardest problem and the highest-value feature. Design for 80% accuracy, confidence-tag uncertain relationships, and don't try to resolve everything. Comment attachment is a solved-but-must-be-addressed problem.

**Table stakes features:** Point-at-repo indexing, file-level chunking, relationship extraction, query by file path, markdown output, language auto-detection, incremental re-indexing, C + Python support.

## Implications for Roadmap

Based on research, suggested phase structure:

1. **Core Indexing Pipeline** — Walk repo, detect languages, parse with tree-sitter, extract chunks, write to LanceDB + markdown
   - Addresses: Point-at-repo indexing, file-level chunking, language auto-detection, C + Python support
   - Avoids: Large repo performance pitfall (stream from the start), comment attachment pitfall (solve early)

2. **Relationship Extraction** — Walk AST to extract calls, imports, inheritance; store in relationships table; include in query output
   - Addresses: The core differentiator (what grep can't do)
   - Avoids: Relationship accuracy pitfall (design for partial resolution), circular dependency pitfall
   - Research flag: This phase will benefit from deeper research into tree-sitter query patterns for C and Python

3. **Query Tool + Jupyter Compaction** — CLI query interface, notebook compaction, smart output formatting
   - Addresses: Query by file path, notebook compaction, markdown output quality
   - Avoids: Information overload pitfall (layered output: summary → details → full code)

4. **Semantic Search + Watching** — Embedding generation, vector similarity search, file watching for live sync
   - Addresses: Semantic search, file watching, incremental updates
   - Avoids: Index staleness pitfall, embedding quality pitfall
   - Research flag: Evaluate embedding models against real codebase queries

5. **Air-Gapped Export + Polish** — Full markdown export for zero-runtime environments, CLI polish, documentation
   - Addresses: Air-gapped mode, production readiness
   - Avoids: Stale export pitfall (timestamp + re-export)

**Phase ordering rationale:**
- Indexing must come first (everything depends on chunks existing)
- Relationships second (the core value prop; query tool is incomplete without them)
- Query tool third (now we have something to query)
- Semantic search fourth (enhancement on top of structural queries)
- Air-gapped export last (requires everything else to be stable)

**Research flags for phases:**
- Phase 2: Needs deeper research into tree-sitter query language for extracting C/Python relationships
- Phase 4: Needs evaluation of embedding models for code semantics
- Phase 1, 3, 5: Standard patterns, unlikely to need research

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | MEDIUM | LanceDB is well-documented but haven't validated relationship storage patterns in it |
| Features | MEDIUM-HIGH | Feature set driven by direct hackathon experience and clear user need |
| Architecture | MEDIUM | Sound design but unproven at scale (large repos like Linux kernel) |
| Pitfalls | MEDIUM-HIGH | Critical pitfalls identified from direct experience (hackathon wall) |

## Gaps to Address

- LanceDB schema design for relationships needs prototyping (can metadata tables handle the join patterns we need?)
- Embedding model selection needs real-world evaluation against codebase queries
- Notebook variable tracing complexity needs more detailed design (scope across cells)
- C macro handling strategy (preprocessor directives invisible to tree-sitter)
- Python dynamic dispatch handling strategy (`obj.method()` resolution)
