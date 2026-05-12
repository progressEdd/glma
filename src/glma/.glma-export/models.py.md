---
file_path: models.py
language: python
last_indexed: 2026-04-13T20:15:23.266865+00:00
chunk_count: 13
content_hash: 6c5a8cf7c3c51ae4c7a19387c06acd8ead6f5bdf3ca5444791cd35b79cfa331f
---

# models.py

## Summary

Defines a collection of Pydantic models and enumerations used to represent code structure, relationship metadata, and system configurations. It serves as the central schema layer for managing indexed source files, semantic code segments, and AI-driven summarization settings.

**AI Chunk Summaries:**
- **ChunkType**: Defines a string-based enumeration used to categorize extracted code segments. It provides four distinct types: `FUNCTION`, `CLASS`, `METHOD`, and `MODULE`.
- **Language**: Defines a string-based enumeration of supported programming languages. It maps internal identifiers to their corresponding lowercase string values (`"c"` and `"python"`).
- **Chunk**: Defines a Pydantic data model for representing semantic code segments extracted from source files. It stores metadata including location, content hash, hierarchical relationships (parent IDs), and optional LLM-generated summaries.
- **FileRecord**: Defines a Pydantic data model for tracking indexed files. It stores metadata including the relative path, language, content hash, indexing timestamp, chunk count, and an optional LLM-generated summary.
- **RelType**: Defines a string-based enumeration of structural relationship types (e.g., calls, imports) used to categorize connections between code chunks. It serves as a type-safe set of constants for mapping dependencies.
- **Confidence**: Defines a string-based enumeration to categorize the confidence level of extracted relationships as either `DIRECT` or `INFERRED`.
- **Relationship**: Defines a Pydantic model for representing structural links between two code chunks. It tracks source and target identifiers, the relationship type, confidence level, and the originating line number.
- **QueryConfig**: Defines a Pydantic schema to store query configuration settings derived from CLI flags. It validates and manages parameters for output verbosity, traversal depth, formatting, and relationship filtering.
- **WatchConfig**: Defines a Pydantic model to manage file-watching settings sourced from configuration files or CLI flags. It validates and stores the debounce interval (0.5s–30s) and a verbosity toggle for event logging.
- **SummarizeProvider**: Defines a string-based enumeration of supported summarization backend providers. It restricts available options to `LOCAL` and `PI`.
- **SummarizeConfig**: Defines a Pydantic configuration schema for AI summarization settings, including the enabled status, provider choice, model name, and API endpoint. It serves as a data model for loading parameters from TOML files or CLI flags.
- **ExportConfig**: Defines a Pydantic schema for air-gapped export settings, specifying the output destination and toggles for source code inclusion. It also manages configuration for local AI summary generation, including the API endpoint and model selection.
- **IndexConfig**: Defines a Pydantic model for indexing configuration sourced from TOML files and CLI flags. It manages settings for target languages, output directories, file inclusion/exclusion patterns, and logging verbosity.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| ChunkType | class | L10-L15 |  |
| Language | class | L18-L21 |  |
| Chunk | class | L24-L36 |  |
| FileRecord | class | L39-L46 |  |
| RelType | class | L49-L54 |  |
| Confidence | class | L57-L60 |  |
| Relationship | class | L63-L70 |  |
| QueryConfig | class | L73-L80 |  |
| WatchConfig | class | L83-L94 |  |
| SummarizeProvider | class | L97-L100 |  |
| SummarizeConfig | class | L103-L120 |  |
| ExportConfig | class | L123-L144 |  |
| IndexConfig | class | L147-L173 |  |

## Chunks

### ChunkType (class, L10-L15)

> *Summary: Defines a string-based enumeration used to categorize extracted code segments. It provides four distinct types: `FUNCTION`, `CLASS`, `METHOD`, and `MODULE`.*

> **Calls:** ? (Enum) (INFERRED), ? (str) (INFERRED), ? (pydantic) (INFERRED), ? (pydantic) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (enum) (INFERRED)

### Language (class, L18-L21)

> *Summary: Defines a string-based enumeration of supported programming languages. It maps internal identifiers to their corresponding lowercase string values (`"c"` and `"python"`).*

> **Calls:** ? (Enum) (INFERRED), ? (str) (INFERRED)

### Chunk (class, L24-L36)

> *Summary: Defines a Pydantic data model for representing semantic code segments extracted from source files. It stores metadata including location, content hash, hierarchical relationships (parent IDs), and optional LLM-generated summaries.*

> **Calls:** ? (BaseModel) (INFERRED)

### FileRecord (class, L39-L46)

> *Summary: Defines a Pydantic data model for tracking indexed files. It stores metadata including the relative path, language, content hash, indexing timestamp, chunk count, and an optional LLM-generated summary.*

> **Calls:** ? (BaseModel) (INFERRED)

### RelType (class, L49-L54)

> *Summary: Defines a string-based enumeration of structural relationship types (e.g., calls, imports) used to categorize connections between code chunks. It serves as a type-safe set of constants for mapping dependencies.*

> **Calls:** ? (Enum) (INFERRED), ? (str) (INFERRED)

### Confidence (class, L57-L60)

> *Summary: Defines a string-based enumeration to categorize the confidence level of extracted relationships as either `DIRECT` or `INFERRED`.*

> **Calls:** ? (Enum) (INFERRED), ? (str) (INFERRED)

### Relationship (class, L63-L70)

> *Summary: Defines a Pydantic model for representing structural links between two code chunks. It tracks source and target identifiers, the relationship type, confidence level, and the originating line number.*

> **Calls:** ? (BaseModel) (INFERRED)

### QueryConfig (class, L73-L80)

> *Summary: Defines a Pydantic schema to store query configuration settings derived from CLI flags. It validates and manages parameters for output verbosity, traversal depth, formatting, and relationship filtering.*

> **Calls:** ? (BaseModel) (INFERRED)

### WatchConfig (class, L83-L94)

> *Summary: Defines a Pydantic model to manage file-watching settings sourced from configuration files or CLI flags. It validates and stores the debounce interval (0.5s–30s) and a verbosity toggle for event logging.*

> **Calls:** ? (BaseModel) (INFERRED)

### SummarizeProvider (class, L97-L100)

> *Summary: Defines a string-based enumeration of supported summarization backend providers. It restricts available options to `LOCAL` and `PI`.*

> **Calls:** ? (Enum) (INFERRED), ? (str) (INFERRED)

### SummarizeConfig (class, L103-L120)

> *Summary: Defines a Pydantic configuration schema for AI summarization settings, including the enabled status, provider choice, model name, and API endpoint. It serves as a data model for loading parameters from TOML files or CLI flags.*

> **Calls:** ? (BaseModel) (INFERRED)

### ExportConfig (class, L123-L144)

> *Summary: Defines a Pydantic schema for air-gapped export settings, specifying the output destination and toggles for source code inclusion. It also manages configuration for local AI summary generation, including the API endpoint and model selection.*

> **Calls:** ? (BaseModel) (INFERRED)

### IndexConfig (class, L147-L173)

> *Summary: Defines a Pydantic model for indexing configuration sourced from TOML files and CLI flags. It manages settings for target languages, output directories, file inclusion/exclusion patterns, and logging verbosity.*

> **Calls:** ? (BaseModel) (INFERRED)

## Relationships

### Imports

| Import | Confidence |
| ------ | ---------- |
| pydantic | INFERRED |
| pydantic | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| enum | INFERRED |

### Inherits

| Class | Base | Confidence |
| ----- | ---- | ---------- |
| ChunkType | ChunkType | INFERRED |
| ChunkType | ChunkType | INFERRED |
| Language | Language | INFERRED |
| Language | Language | INFERRED |
| Chunk | Chunk | INFERRED |
| FileRecord | FileRecord | INFERRED |
| RelType | RelType | INFERRED |
| RelType | RelType | INFERRED |
| Confidence | Confidence | INFERRED |
| Confidence | Confidence | INFERRED |
| Relationship | Relationship | INFERRED |
| QueryConfig | QueryConfig | INFERRED |
| WatchConfig | WatchConfig | INFERRED |
| SummarizeProvider | SummarizeProvider | INFERRED |
| SummarizeProvider | SummarizeProvider | INFERRED |
| SummarizeConfig | SummarizeConfig | INFERRED |
| ExportConfig | ExportConfig | INFERRED |
| IndexConfig | IndexConfig | INFERRED |
