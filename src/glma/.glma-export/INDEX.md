# Codebase Index

**Generated:** 2026-04-13T20:31:57.627913+00:00
**Total Files:** 28
**Total Chunks:** 148

## Files

| File | Language | Chunks | Summary |
| ---- | -------- | ------ | ------- |
| [__init__.py](__init__.py.md) | python | 0 | File with 0 chunk(s). |
| [__main__.py](__main__.py.md) | python | 0 | File with 0 chunk(s). |
| [cli.py](cli.py.md) | python | 8 | Provides a command-line interface for indexing repositories into a database, managing AI-driven summarization, and exporting documentation as static Markdown. It supports repository monitoring for incremental updates and allows users to query indexed file relationships via JSON or Markdown outputs. |
| [config.py](config.py.md) | python | 4 | Manages application configuration by merging default values with `.glma.toml` file settings and CLI overrides. It provides specialized config objects for indexing, watching, exporting, and summarizing, ensuring that command-line flags take priority over file-based configurations. |
| [db/__init__.py](db/__init__.py.md) | python | 0 | File with 0 chunk(s). |
| [db/ladybug_store.py](db/ladybug_store.py.md) | python | 20 | Provides a graph database interface for indexing code files and chunks, managing their metadata, AI summaries, and inter-relationships via Cypher queries. It supports CRUD operations for file/chunk records and implements complex relationship retrieval through BFS traversals. |
| [export.py](export.py.md) | python | 13 | Exports project metadata and relationship data from a `LadybugStore` into structured Markdown documentation. It generates detailed per-file summaries, dependency graphs, and an overall `ARCHITECTURE.md` overview, outputting the results as a directory, a compressed archive, or a stdout stream. |
| [index/__init__.py](index/__init__.py.md) | python | 0 | File with 0 chunk(s). |
| [index/chunks.py](index/chunks.py.md) | python | 5 | Parses source files into semantic code chunks by traversing AST nodes based on language-specific configurations. It generates unique identifiers and content hashes for each extracted segment, supporting nested structures like methods within classes. |
| [index/comments.py](index/comments.py.md) | python | 4 | Extracts and associates Python docstrings and source code comments with their corresponding code chunks using AST traversal. It processes raw files into structured data by matching comment line ranges to specific functions or classes based on proximity and node type. |
| [index/detector.py](index/detector.py.md) | python | 1 | Determines the programming language of a file by mapping its extension to a predefined lookup table. It accepts a `Path` object and returns a `Language` enum or `None`. |
| [index/parser.py](index/parser.py.md) | python | 4 | Provides a framework for parsing source files into Tree-sitter ASTs using language-specific configuration schemas. It maps AST node types to extractable code chunks, enabling the identification of functions, classes, and dependencies across multiple supported languages. |
| [index/pipeline.py](index/pipeline.py.md) | python | 4 | Implements an incremental indexing pipeline that extracts code chunks and relationships from source files, persisting them to a `LadybugStore`. It utilizes BLAKE2b content hashing to track changes and automatically generates updated markdown documentation for modified files. |
| [index/progress.py](index/progress.py.md) | python | 6 | Provides a Rich-based progress tracking system for the indexing pipeline, managing real-time status bars and final summaries. It tracks processing milestones via start/advance/finish methods while supporting a quiet mode to suppress all console output. |
| [index/relationships.py](index/relationships.py.md) | python | 9 | Extracts structural dependencies—such as function calls, imports, and class inheritance—from C and Python source files using AST traversal. It maps these connections into `Relationship` objects with associated confidence levels based on whether the targets are resolved within the indexed store. |
| [index/resolver.py](index/resolver.py.md) | python | 7 | Analyzes Python ASTs to resolve function calls and import statements to specific code chunks within a `LadybugStore`. It maps local identifiers and module paths to their source definitions by tracking imports and traversing class/function scopes. |
| [index/walker.py](index/walker.py.md) | python | 1 | Recursively scans a repository directory to identify source files based on supported extensions and configuration filters. It yields pairs of absolute file paths and their detected languages while pruning excluded or hidden directories. |
| [index/writer.py](index/writer.py.md) | python | 9 | Generates structured Markdown reports from indexed code chunks and their relationships, including source summaries and dependency tables. It processes chunk metadata and relationship data to write these formatted documents into a mirrored directory structure. |
| [models.py](models.py.md) | python | 13 | Defines a collection of Pydantic models and enumerations used to represent code structure, relationship metadata, and system configurations. It serves as the central schema layer for managing indexed source files, semantic code segments, and AI-driven summarization settings. |
| [query/__init__.py](query/__init__.py.md) | python | 0 | File with 0 chunk(s). |
| [query/formatter.py](query/formatter.py.md) | python | 7 | Provides utilities to format code chunks, index metadata, and relationship mappings into structured Markdown reports or JSON strings. It transforms raw file records and chunk data into human-readable summaries or machine-readable exports based on a provided configuration. |
| [query/notebook.py](query/notebook.py.md) | python | 13 | Processes Jupyter notebooks into structured Markdown summaries by analyzing variable flow, grouping cells into logical sections, and optionally using an AI provider with BLAKE2b-based caching for cell descriptions. It outputs a comprehensive report including section overviews, detailed cell breakdowns, and variable dependency tables. |
| [query/variables.py](query/variables.py.md) | python | 6 | Analyzes notebook cell source code using AST parsing to identify variable definitions and references at the statement level. It aggregates this metadata into a flow dictionary that maps variables to their specific definition and usage locations across multiple cells. |
| [summaries.py](summaries.py.md) | python | 1 | Generates a deterministic, human-readable structural summary of a file by aggregating counts of code elements and identifying unique external dependencies. It outputs a formatted string detailing the internal composition and relationship targets of the provided source chunks. |
| [summarize/__init__.py](summarize/__init__.py.md) | python | 0 | File with 0 chunk(s). |
| [summarize/pipeline.py](summarize/pipeline.py.md) | python | 1 | Processes a list of code chunks through an AI provider to generate summaries and persist them to the database. It supports incremental updates by skipping existing entries and handles individual failures to ensure overall pipeline stability. |
| [summarize/providers.py](summarize/providers.py.md) | python | 8 | Defines a common interface and multiple provider implementations (OpenAI-compatible and Pi) for generating natural language summaries of source code. It handles API integration, dependency validation, and prompt management to transform code snippets and metadata into concise behavioral descriptions. |
| [watch.py](watch.py.md) | python | 4 | Monitors a repository for filesystem changes using `watchfiles` to trigger incremental re-indexing of supported language files. It processes event tuples to detect creations, modifications, deletions, and renames, updating the index accordingly based on provided configuration. |

## Statistics

- Total functions: 95
- Total classes: 24
- Total methods: 29
- Total files: 28
