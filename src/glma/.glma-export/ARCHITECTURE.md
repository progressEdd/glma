# Architecture Overview

**Generated:** 2026-04-13T20:31:57.628580+00:00
**Total Modules:** 12

## Project Structure Overview

### Module: __init__

| File | Chunks | Summary |
| ---- | ------ | ------- |
| __init__.py | 0 | File with 0 chunk(s). |

__init__: File with 0 chunk(s).

### Module: __main__

| File | Chunks | Summary |
| ---- | ------ | ------- |
| __main__.py | 0 | File with 0 chunk(s). |

__main__: File with 0 chunk(s).

### Module: cli

| File | Chunks | Summary |
| ---- | ------ | ------- |
| cli.py | 8 | Prints the current application version to the console and terminates execution i... |

version_callback: Prints the current application version to the console and terminates execution if the provided boolean flag is true.; main: Defines the CLI entry point using Typer to handle command-line arguments. It currently supports a `--version` flag that triggers a callback to display the ...

### Module: config

| File | Chunks | Summary |
| ---- | ------ | ------- |
| config.py | 4 | Initializes an `IndexConfig` object by merging default values with settings from... |

load_config: Initializes an `IndexConfig` object by merging default values with settings from a `.glma.toml` file and optional CLI overrides. It prioritizes CLI flags over file configurations and handles the conversion of language strings into `Language` enums.; load_watch_config: Loads watch set...

### Module: db

| File | Chunks | Summary |
| ---- | ------ | ------- |
| db/__init__.py | 0 | File with 0 chunk(s). |
| db/ladybug_store.py | 20 | Manages a graph database for storing and querying code index data, including fil... |

LadybugStore: Manages a graph database for storing and querying code index data, including files, chunks, and their inter-relationships. It provides methods to upsert records, update AI-generated summaries, and perform BFS traversals of relationships between code chunks.; __init__: Initializes th...

### Module: export

| File | Chunks | Summary |
| ---- | ------ | ------- |
| export.py | 13 | Generates an enriched Markdown representation of a single source file using its ... |

_format_export_file: Generates an enriched Markdown representation of a single source file using its path, metadata record, code chunks, and relationship data. It constructs a structured document containing YAML frontmatter, AI-generated summaries, a table of key exports, detailed chunk content (...

### Module: index

| File | Chunks | Summary |
| ---- | ------ | ------- |
| index/__init__.py | 0 | File with 0 chunk(s). |
| index/chunks.py | 5 | Generates a 32-byte BLAKE2b hexadecimal hash from a UTF-8 encoded input string. ... |
| index/comments.py | 4 | Extracts the docstring from a Python class or function node by identifying the f... |
| index/detector.py | 1 | Identifies the programming language of a given file by mapping its lowercase ext... |
| index/parser.py | 4 | Defines a configuration schema for language-specific parsing, mapping tree-sitte... |
| index/pipeline.py | 4 | Generates a 64-character hex digest of a file's content using the BLAKE2b algori... |
| index/progress.py | 6 | Manages a Rich-based progress bar and summary display for the indexing pipeline.... |
| index/relationships.py | 9 | Traverses a node's parent hierarchy to locate the nearest `Chunk` that shares th... |
| index/resolver.py | 7 | Defines a data structure to track import metadata, mapping a local alias or name... |
| index/walker.py | 1 | Recursively traverses a repository directory to identify source files based on s... |
| index/writer.py | 9 | Maps a `Chunk` object's type to a human-readable string using a predefined mappi... |

_content_hash: Generates a 32-byte BLAKE2b hexadecimal hash from a UTF-8 encoded input string. It takes a string as input and returns its corresponding content hash.; _chunk_id: Generates a unique identifier string by concatenating the file path, chunk type, name, and starting line number using d...

### Module: models

| File | Chunks | Summary |
| ---- | ------ | ------- |
| models.py | 13 | Defines a string-based enumeration used to categorize extracted code segments. I... |

ChunkType: Defines a string-based enumeration used to categorize extracted code segments. It provides four distinct types: `FUNCTION`, `CLASS`, `METHOD`, and `MODULE`.; Language: Defines a string-based enumeration of supported programming languages. It maps internal identifiers to their correspon...

### Module: query

| File | Chunks | Summary |
| ---- | ------ | ------- |
| query/__init__.py | 0 | File with 0 chunk(s). |
| query/formatter.py | 7 | Determines the markdown language identifier based on a given file path's extensi... |
| query/notebook.py | 13 | Defines a data structure for storing cached notebook cell summaries. It tracks t... |
| query/variables.py | 6 | Defines a data structure to track variable metadata for a single cell statement,... |

_get_lang_hint: Determines the markdown language identifier based on a given file path's extension. It returns `"python"` for `.py` files, `"c"` for `.c` or `.h` files, and an empty string otherwise.; _format_summary: Generates a list of formatted summary strings for top-level chunks, including t...

### Module: summaries

| File | Chunks | Summary |
| ---- | ------ | ------- |
| summaries.py | 1 | Creates a deterministic, human-readable summary of a file by aggregating counts ... |

generate_rule_summary: Creates a deterministic, human-readable summary of a file by aggregating counts and names of functions, classes, and methods from `chunks` and listing unique targets from `relationships`. It returns a formatted string detailing the file's structure and its import/include de...

### Module: summarize

| File | Chunks | Summary |
| ---- | ------ | ------- |
| summarize/__init__.py | 0 | File with 0 chunk(s). |
| summarize/pipeline.py | 1 | Generates AI summaries for a list of code chunks using a provided provider and p... |
| summarize/providers.py | 8 | Defines a structural protocol for code summarization services. It requires a `su... |

summarize_chunks: Generates AI summaries for a list of code chunks using a provided provider and persists the results to the database. It implements incremental processing by skipping already summarized chunks and ensures pipeline stability by catching and logging individual summarization failure...

### Module: watch

| File | Chunks | Summary |
| ---- | ------ | ------- |
| watch.py | 4 | Categorizes a set of `watchfiles` event tuples into three distinct sets based on... |

_classify_events: Categorizes a set of `watchfiles` event tuples into three distinct sets based on the change type. It takes `(Change, str)` pairs as input and returns a tuple containing sets of `Path` objects for created, modified, and deleted files.; _detect_renames: Identifies file renames by ...

## Module Dependencies

| Module | Depends On |
| ------ | ---------- |
| __init__ | *(no external dependencies)* |
| __main__ | *(no external dependencies)* |
| cli | db |
| config | db |
| db | *(no external dependencies)* |
| export | db |
| index | db |
| models | *(no external dependencies)* |
| query | db |
| summaries | db |
| summarize | db |
| watch | db |

## Entry Points

| File | Detection Method | Key Chunks |
| ---- | ---------------- | ---------- |
| __main__.py | detected entry point | *(no top-level chunks)* |
| cli.py | detected entry point | version_callback, main, index, _write_output, _group_rels_by_chunk |
| export.py | detected entry point | _format_export_file, _format_rel_path, generate_index_md, generate_relationships_md, _get_module_name |

## Key Interfaces

| Name | Type | File | Used By (files) |
| ---- | ---- | ---- | --------------- |
| _extract_name_refs (Recursively extracts all variable identi...) | function | query/variables.py | 1 files |
| Relationship (Defines a Pydantic model for representin...) | class | models.py | 1 files |
| get_chunks_for_file (Retrieves all `Chunk` objects associated...) | method | db/ladybug_store.py | 4 files |
| Language (Defines a string-based enumeration of su...) | class | models.py | 6 files |
| get_file_relationships (Retrieves all outgoing `RELATES_TO` rela...) | method | db/ladybug_store.py | 4 files |
| _format_rel_path (Appends a `.md` extension to a given fil...) | function | export.py | 1 files |
| LadybugStore (Manages a graph database for storing and...) | class | db/ladybug_store.py | 3 files |
| _get_module_name (Extracts a module name from a relative f...) | function | export.py | 1 files |
| get_root_node (Parses a source file based on the provid...) | function | index/parser.py | 3 files |
| summarize (Generates a natural language summary des...) | method | summarize/providers.py | 3 files |
