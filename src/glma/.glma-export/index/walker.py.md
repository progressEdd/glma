---
file_path: index/walker.py
language: python
last_indexed: 2026-04-13T20:15:23.522954+00:00
chunk_count: 1
content_hash: 5342b746138a726b07fe2e066ae4e5d9cec110f8c74376b1529171df7d5393ae
---

# index/walker.py

## Summary

Recursively scans a repository directory to identify source files based on supported extensions and configuration filters. It yields pairs of absolute file paths and their detected languages while pruning excluded or hidden directories.

**AI Chunk Summaries:**
- **walk_source_files**: Recursively traverses a repository directory to identify source files based on supported extensions and configuration filters. It yields tuples of absolute file paths and their corresponding languages while pruning excluded or hidden directories and files for efficiency.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| walk_source_files | function | L10-L62 |  |

## Chunks

### walk_source_files (function, L10-L62)

> *Summary: Recursively traverses a repository directory to identify source files based on supported extensions and configuration filters. It yields tuples of absolute file paths and their corresponding languages while pruning excluded or hidden directories and files for efficiency.*

> **Calls:** ? (glma.models) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (os) (INFERRED), ? (filename.startswith) (INFERRED), ? (filepath.suffix.lower) (INFERRED), ? (Path) (INFERRED), ? (d.startswith) (INFERRED), ? (walk) (INFERRED), ? (set) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| walk_source_files | ? (filename.startswith) | INFERRED | L59 |
| walk_source_files | ? (filepath.suffix.lower) | INFERRED | L47 |
| walk_source_files | ? (Path) | INFERRED | L46 |
| walk_source_files | ? (d.startswith) | INFERRED | L42 |
| walk_source_files | ? (walk) | INFERRED | L38 |
| walk_source_files | ? (set) | INFERRED | L35 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| os | INFERRED |
