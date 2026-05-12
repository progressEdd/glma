---
file_path: summarize/pipeline.py
language: python
last_indexed: 2026-04-13T20:15:24.248716+00:00
chunk_count: 1
content_hash: cbf11dbabbfd08772ce5b44f35fd1188a47131581d1855170ba74c0dbd47a561
---

# summarize/pipeline.py

## Summary

Processes a list of code chunks through an AI provider to generate summaries and persist them to the database. It supports incremental updates by skipping existing entries and handles individual failures to ensure overall pipeline stability.

**AI Chunk Summaries:**
- **summarize_chunks**: Generates AI summaries for a list of code chunks using a provided provider and persists the results to the database. It implements incremental processing by skipping already summarized chunks and ensures pipeline stability by catching and logging individual summarization failures.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| summarize_chunks | function | L12-L66 |  |

## Chunks

### summarize_chunks (function, L12-L66)

> *Summary: Generates AI summaries for a list of code chunks using a provided provider and persists the results to the database. It implements incremental processing by skipping already summarized chunks and ensures pipeline stability by catching and logging individual summarization failures.*

> **Calls:** ? (glma.models) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (typing) (INFERRED), ? (logging) (INFERRED), ? (logger.info) (INFERRED), ? (updated.append) (INFERRED), ? (logger.warning) (INFERRED), ? (logger.warning) (INFERRED), ? (store.update_chunk_summary) (INFERRED), ? (provider.summarize) (INFERRED), ? (updated.append) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| summarize_chunks | ? (logger.info) | INFERRED | L62 |
| summarize_chunks | ? (updated.append) | INFERRED | L60 |
| summarize_chunks | ? (logger.warning) | INFERRED | L57 |
| summarize_chunks | ? (logger.warning) | INFERRED | L54 |
| summarize_chunks | ? (store.update_chunk_summary) | INFERRED | L50 |
| summarize_chunks | ? (provider.summarize) | INFERRED | L48 |
| summarize_chunks | ? (updated.append) | INFERRED | L39 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| glma.db.ladybug_store | INFERRED |
| typing | INFERRED |
| logging | INFERRED |
