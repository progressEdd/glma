---
file_path: config.py
language: python
last_indexed: 2026-04-13T20:15:23.033337+00:00
chunk_count: 4
content_hash: d71cb1f026b914fb70f3761c4ce16ce0592c50f4d9a4ee421730380025375589
---

# config.py

## Summary

Manages application configuration by merging default values with `.glma.toml` file settings and CLI overrides. It provides specialized config objects for indexing, watching, exporting, and summarizing, ensuring that command-line flags take priority over file-based configurations.

**AI Chunk Summaries:**
- **load_config**: Initializes an `IndexConfig` object by merging default values with settings from a `.glma.toml` file and optional CLI overrides. It prioritizes CLI flags over file configurations and handles the conversion of language strings into `Language` enums.
- **load_watch_config**: Loads watch settings by merging values from a `.glma.toml` file and optional CLI overrides. It returns a `WatchConfig` object populated with the combined configuration, prioritizing CLI flags over file-based settings.
- **load_export_config**: Loads export settings by merging values from a `.glma.toml` file and optional CLI overrides. It returns an `ExportConfig` instance populated with the combined configuration, prioritizing non-null CLI flags over file defaults.
- **load_summarize_config**: Initializes a `SummarizeConfig` object by merging settings from a `.glma.toml` file and optional CLI overrides. It prioritizes non-null CLI arguments over file-based configurations found in the `[summarize]` section.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| load_config | function | L10-L43 |  |
| load_watch_config | function | L46-L64 |  |
| load_export_config | function | L67-L85 |  |
| load_summarize_config | function | L88-L106 |  |

## Chunks

### load_config (function, L10-L43)

> *Summary: Initializes an `IndexConfig` object by merging default values with settings from a `.glma.toml` file and optional CLI overrides. It prioritizes CLI flags over file configurations and handles the conversion of language strings into `Language` enums.*

> **Calls:** ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (tomllib) (INFERRED), ? (IndexConfig) (INFERRED), ? (cli_overrides.items) (INFERRED), ? (merged.update) (INFERRED), ? (Language) (INFERRED), ? (raw.get) (INFERRED), ? (load) (INFERRED), ? (open) (INFERRED), ? (config_path.exists) (INFERRED)

### load_watch_config (function, L46-L64)

> *Summary: Loads watch settings by merging values from a `.glma.toml` file and optional CLI overrides. It returns a `WatchConfig` object populated with the combined configuration, prioritizing CLI flags over file-based settings.*

> **Calls:** ? (WatchConfig) (INFERRED), ? (cli_overrides.items) (INFERRED), ? (merged.update) (INFERRED), ? (raw.get) (INFERRED), ? (load) (INFERRED), ? (open) (INFERRED), ? (config_path.exists) (INFERRED)

### load_export_config (function, L67-L85)

> *Summary: Loads export settings by merging values from a `.glma.toml` file and optional CLI overrides. It returns an `ExportConfig` instance populated with the combined configuration, prioritizing non-null CLI flags over file defaults.*

> **Calls:** ? (ExportConfig) (INFERRED), ? (cli_overrides.items) (INFERRED), ? (merged.update) (INFERRED), ? (raw.get) (INFERRED), ? (load) (INFERRED), ? (open) (INFERRED), ? (config_path.exists) (INFERRED)

### load_summarize_config (function, L88-L106)

> *Summary: Initializes a `SummarizeConfig` object by merging settings from a `.glma.toml` file and optional CLI overrides. It prioritizes non-null CLI arguments over file-based configurations found in the `[summarize]` section.*

> **Calls:** ? (SummarizeConfig) (INFERRED), ? (cli_overrides.items) (INFERRED), ? (merged.update) (INFERRED), ? (raw.get) (INFERRED), ? (load) (INFERRED), ? (open) (INFERRED), ? (config_path.exists) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| load_config | ? (IndexConfig) | INFERRED | L43 |
| load_config | ? (cli_overrides.items) | INFERRED | L39 |
| load_config | ? (merged.update) | INFERRED | L37 |
| load_config | ? (Language) | INFERRED | L32 |
| load_config | ? (raw.get) | INFERRED | L28 |
| load_config | ? (load) | INFERRED | L27 |
| load_config | ? (open) | INFERRED | L26 |
| load_config | ? (config_path.exists) | INFERRED | L25 |
| load_watch_config | ? (WatchConfig) | INFERRED | L64 |
| load_watch_config | ? (cli_overrides.items) | INFERRED | L60 |
| load_watch_config | ? (merged.update) | INFERRED | L58 |
| load_watch_config | ? (raw.get) | INFERRED | L54 |
| load_watch_config | ? (load) | INFERRED | L53 |
| load_watch_config | ? (open) | INFERRED | L52 |
| load_watch_config | ? (config_path.exists) | INFERRED | L51 |
| load_export_config | ? (ExportConfig) | INFERRED | L85 |
| load_export_config | ? (cli_overrides.items) | INFERRED | L81 |
| load_export_config | ? (merged.update) | INFERRED | L79 |
| load_export_config | ? (raw.get) | INFERRED | L75 |
| load_export_config | ? (load) | INFERRED | L74 |
| load_export_config | ? (open) | INFERRED | L73 |
| load_export_config | ? (config_path.exists) | INFERRED | L72 |
| load_summarize_config | ? (SummarizeConfig) | INFERRED | L106 |
| load_summarize_config | ? (cli_overrides.items) | INFERRED | L102 |
| load_summarize_config | ? (merged.update) | INFERRED | L100 |
| load_summarize_config | ? (raw.get) | INFERRED | L96 |
| load_summarize_config | ? (load) | INFERRED | L95 |
| load_summarize_config | ? (open) | INFERRED | L94 |
| load_summarize_config | ? (config_path.exists) | INFERRED | L93 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| tomllib | INFERRED |
