---
file_path: summaries.py
language: python
last_indexed: 2026-04-13T20:15:23.111886+00:00
chunk_count: 1
content_hash: 4f7f862bd9c25696c6c706aba2d2d3e5a1ea65a365a783720ba879a5ae9bc5fa
---

# summaries.py

## Summary

Generates a deterministic, human-readable structural summary of a file by aggregating counts of code elements and identifying unique external dependencies. It outputs a formatted string detailing the internal composition and relationship targets of the provided source chunks.

**AI Chunk Summaries:**
- **generate_rule_summary**: Creates a deterministic, human-readable summary of a file by aggregating counts and names of functions, classes, and methods from `chunks` and listing unique targets from `relationships`. It returns a formatted string detailing the file's structure and its import/include dependencies.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| generate_rule_summary | function | L6-L54 |  |

## Chunks

### generate_rule_summary (function, L6-L54)

> *Summary: Creates a deterministic, human-readable summary of a file by aggregating counts and names of functions, classes, and methods from `chunks` and listing unique targets from `relationships`. It returns a formatted string detailing the file's structure and its import/include dependencies.*

> **Calls:** ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (len) (INFERRED), ? (". ".join) (INFERRED), ? (parts.append) (INFERRED), ? (", ".join) (INFERRED), ? (parts.append) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (", ".join) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (sorted) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (sorted) (INFERRED), ? (len) (INFERRED), ? (parts.append) (INFERRED), ? (len) (INFERRED), ? (parts.append) (INFERRED), ? (", ".join) (INFERRED), ? (len) (INFERRED), ? (parts.append) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (", ".join) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| generate_rule_summary | ? (len) | INFERRED | L54 |
| generate_rule_summary | ? (". ".join) | INFERRED | L54 |
| generate_rule_summary | ? (parts.append) | INFERRED | L52 |
| generate_rule_summary | ? (", ".join) | INFERRED | L51 |
| generate_rule_summary | ? (parts.append) | INFERRED | L48 |
| generate_rule_summary | ? (len) | INFERRED | L47 |
| generate_rule_summary | ? (len) | INFERRED | L47 |
| generate_rule_summary | ? (", ".join) | INFERRED | L46 |
| generate_rule_summary | ? (r.get) | INFERRED | L43 |
| generate_rule_summary | ? (r.get) | INFERRED | L43 |
| generate_rule_summary | ? (r.get) | INFERRED | L43 |
| generate_rule_summary | ? (sorted) | INFERRED | L43 |
| generate_rule_summary | ? (r.get) | INFERRED | L42 |
| generate_rule_summary | ? (r.get) | INFERRED | L42 |
| generate_rule_summary | ? (r.get) | INFERRED | L42 |
| generate_rule_summary | ? (sorted) | INFERRED | L42 |
| generate_rule_summary | ? (len) | INFERRED | L39 |
| generate_rule_summary | ? (parts.append) | INFERRED | L39 |
| generate_rule_summary | ? (len) | INFERRED | L36 |
| generate_rule_summary | ? (parts.append) | INFERRED | L36 |
| generate_rule_summary | ? (", ".join) | INFERRED | L35 |
| generate_rule_summary | ? (len) | INFERRED | L32 |
| generate_rule_summary | ? (parts.append) | INFERRED | L32 |
| generate_rule_summary | ? (len) | INFERRED | L31 |
| generate_rule_summary | ? (len) | INFERRED | L31 |
| generate_rule_summary | ? (", ".join) | INFERRED | L30 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| glma.models | INFERRED |
