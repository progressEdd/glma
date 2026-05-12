---
file_path: index/detector.py
language: python
last_indexed: 2026-04-13T20:15:23.559030+00:00
chunk_count: 1
content_hash: 6249cd33c37f11036a83567558b19ca7368109c4b3d41383a824db3c629d571b
---

# index/detector.py

## Summary

Determines the programming language of a file by mapping its extension to a predefined lookup table. It accepts a `Path` object and returns a `Language` enum or `None`.

**AI Chunk Summaries:**
- **detect_language**: Identifies the programming language of a given file by mapping its lowercase extension against a predefined lookup table. It takes a `Path` object as input and returns a corresponding `Language` enum or `None`.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| detect_language | function | L18-L27 |  |

## Chunks

### detect_language (function, L18-L27)

> *Summary: Identifies the programming language of a given file by mapping its lowercase extension against a predefined lookup table. It takes a `Path` object as input and returns a corresponding `Language` enum or `None`.*

> **Calls:** ? (glma.models) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (filepath.suffix.lower) (INFERRED), ? (EXTENSION_MAP.get) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| detect_language | ? (filepath.suffix.lower) | INFERRED | L27 |
| detect_language | ? (EXTENSION_MAP.get) | INFERRED | L27 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
