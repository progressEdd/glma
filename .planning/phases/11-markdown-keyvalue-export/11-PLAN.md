---
wave: 1
depends_on: []
files_modified:
  - 02-worktrees/glma/src/glma/models.py
  - 02-worktrees/glma/src/glma/export.py
  - 02-worktrees/glma/src/glma/cli.py
  - 02-worktrees/glma/src/glma/config.py
  - 02-worktrees/glma/src/glma/query/formatter.py
  - 02-worktrees/glma/tests/test_export.py
  - 02-worktrees/glma/pyproject.toml
requirements_addressed: [KV-01, KV-02]
autonomous: true
---

# Plan 01: Multi-Format Export with KV Default

**Objective:** Add `ExportFormat` enum, strategy-pattern renderers (KV, markdown, JSON, YAML), consolidated CODEBASE.md for KV, `--format`/`-f` flag on export and query commands. Existing markdown output unchanged and backward-compatible.

---

## Task 1: Add ExportFormat Enum and ExportConfig.format Field

<objective>Add the shared format enum and wire it into the export config model.</objective>

<read_first>
- 02-worktrees/glma/src/glma/models.py (current ExportConfig, QueryConfig, all enums)
</read_first>

<action>
In `models.py`:

1. Add a new enum after the existing `Confidence` enum:

```python
class ExportFormat(str, Enum):
    """Supported export output formats."""
    MARKDOWN_KV = "markdown-kv"
    MARKDOWN = "markdown"
    JSON = "json"
    YAML = "yaml"
```

2. Add a `format` field to `ExportConfig`:

```python
    format: ExportFormat = Field(
        default=ExportFormat.MARKDOWN_KV,
        description="Export output format: markdown-kv, markdown, json, yaml",
    )
```

3. In `QueryConfig`, change `output_format` field type from `str` to `ExportFormat`:

```python
    output_format: ExportFormat = Field(
        default=ExportFormat.MARKDOWN,
        description="Output format: markdown-kv, markdown, json, yaml",
    )
```

Note: This change requires updating the query command's format validation (Task 6) since the enum now handles validation.
</action>

<acceptance_criteria>
- `models.py` contains `class ExportFormat(str, Enum)` with exactly four members: `MARKDOWN_KV = "markdown-kv"`, `MARKDOWN = "markdown"`, `JSON = "json"`, `YAML = "yaml"`
- `ExportConfig` has a `format` field with default `ExportFormat.MARKDOWN_KV`
- `QueryConfig.output_format` type is `ExportFormat` with default `ExportFormat.MARKDOWN`
- `from glma.models import ExportFormat` succeeds without error
</acceptance_criteria>

---

## Task 2: Define FormatRenderer Protocol and Markdown Renderer

<objective>Create the strategy pattern infrastructure and wrap existing markdown formatting functions as the MarkdownRenderer implementation.</objective>

<read_first>
- 02-worktrees/glma/src/glma/export.py (entire file — all formatters, writers, and generators)
- 02-worktrees/glma/src/glma/models.py (ExportFormat, ExportConfig after Task 1 changes)
</read_first>

<action>
In `export.py`, after the imports and before `_format_export_file()`:

1. Add imports:
```python
from abc import ABC, abstractmethod
from glma.models import ExportFormat
import json
```

2. Define the renderer protocol:
```python
class FormatRenderer(ABC):
    """Strategy interface for export format rendering."""

    @abstractmethod
    def format_file(
        self,
        file_path: str,
        file_record: Optional[object],
        chunks: list[Chunk],
        relationships: list[dict],
        config: ExportConfig,
    ) -> str:
        """Render a single file's export content."""
        ...

    @abstractmethod
    def generate_root_files(
        self,
        indexed_files: dict,
        file_data: dict[str, dict],
    ) -> dict[str, str]:
        """Generate root-level files (INDEX.md, CODEBASE.md, etc.).

        Returns dict of {filename: content}.
        """
        ...

    @abstractmethod
    def file_extension(self) -> str:
        """File extension for per-file exports (e.g., '.md', '.json', '.yaml')."""
        ...
```

3. Create the MarkdownRenderer by wrapping existing functions:
```python
class MarkdownRenderer(FormatRenderer):
    """Renders current table-based markdown format (backward compatible)."""

    def format_file(self, file_path, file_record, chunks, relationships, config):
        return _format_export_file(file_path, file_record, chunks, relationships, config)

    def generate_root_files(self, indexed_files, file_data):
        return {
            "INDEX.md": generate_index_md(indexed_files, file_data),
            "RELATIONSHIPS.md": generate_relationships_md(file_data),
            "ARCHITECTURE.md": generate_architecture_md(file_data),
        }

    def file_extension(self):
        return ".md"
```

4. Add the factory function:
```python
def get_renderer(fmt: ExportFormat) -> FormatRenderer:
    """Return the appropriate renderer for the given format."""
    if fmt == ExportFormat.MARKDOWN:
        return MarkdownRenderer()
    elif fmt == ExportFormat.MARKDOWN_KV:
        return MarkdownKVRenderer()
    elif fmt == ExportFormat.JSON:
        return JsonRenderer()
    elif fmt == ExportFormat.YAML:
        return YamlRenderer()
    raise ValueError(f"Unknown format: {fmt}")
```

Do NOT modify any existing formatting functions (`_format_export_file`, `generate_index_md`, `generate_relationships_md`, `generate_architecture_md`). They continue to work unchanged as the MarkdownRenderer implementation.
</action>

<acceptance_criteria>
- `export.py` contains `class FormatRenderer(ABC)` with abstract methods `format_file`, `generate_root_files`, `file_extension`
- `export.py` contains `class MarkdownRenderer(FormatRenderer)` that delegates to existing functions
- `export.py` contains `get_renderer(ExportFormat) -> FormatRenderer` factory function
- `get_renderer(ExportFormat.MARKDOWN)` returns a `MarkdownRenderer` instance
- `from glma.export import FormatRenderer, MarkdownRenderer, get_renderer` succeeds
- Existing `_format_export_file()` function body is unchanged
</acceptance_criteria>

---

## Task 3: Implement MarkdownKVRenderer

<objective>Create the KV format renderer that outputs compact key-value markdown per-file and consolidated CODEBASE.md root file.</objective>

<read_first>
- 02-worktrees/glma/src/glma/export.py (existing `_format_export_file()` for data structure reference, `_get_module_name()`, `_group_by_module()`, `_detect_entry_points()`, `_compute_key_interfaces()` for CODEBASE.md generation)
- 02-worktrees/glma/src/glma/models.py (Chunk, ChunkType, FileRecord fields)
- 02-worktrees/glma/src/glma/summaries.py (`generate_rule_summary` for fallback summaries)
- .planning/phases/11-markdown-keyvalue-export/11-CONTEXT.md (D-01 through D-06: KV format decisions)
</read_first>

<action>
In `export.py`, after `MarkdownRenderer` class, add:

```python
class MarkdownKVRenderer(FormatRenderer):
    """Renders compact key-value markdown format (LLM-friendly default)."""

    def format_file(self, file_path, file_record, chunks, relationships, config):
        return _format_kv_file(file_path, file_record, chunks, relationships, config)

    def generate_root_files(self, indexed_files, file_data):
        return {
            "CODEBASE.md": _generate_codebase_md(indexed_files, file_data),
        }

    def file_extension(self):
        return ".md"
```

Implement `_format_kv_file()`:

```python
def _format_kv_file(file_path, file_record, chunks, relationships, config):
    """Generate compact KV markdown for a single file."""
    lines = []

    # File heading
    lines.append(f"# {file_path}")
    lines.append("")

    # File metadata as key-value pairs
    if file_record:
        lang_val = file_record.language.value if hasattr(file_record.language, 'value') else str(file_record.language)
        lines.append(f"language: {lang_val}")
        lines.append(f"last_indexed: {file_record.last_indexed}")
        lines.append(f"chunk_count: {file_record.chunk_count}")
    lines.append("")

    # File summary
    if file_record and hasattr(file_record, 'file_summary') and file_record.file_summary:
        lines.append(f"summary: {file_record.file_summary}")
    else:
        rule_summary = generate_rule_summary(file_path, chunks, relationships)
        lines.append(f"summary: {rule_summary}")
    lines.append("")

    # Per-chunk sections
    for chunk in chunks:
        lines.append(f"## {chunk.name}")
        lines.append("")
        lines.append(f"type: {chunk.chunk_type.value}")
        lines.append(f"lines: L{chunk.start_line}-L{chunk.end_line}")

        if chunk.summary:
            lines.append(f"summary: {chunk.summary}")

        if config.include_code:
            lang_hint = ""
            if file_path.endswith(".py"):
                lang_hint = "python"
            elif file_path.endswith(".c") or file_path.endswith(".h"):
                lang_hint = "c"
            lines.append("")
            lines.append(f"```{lang_hint}")
            lines.append(chunk.content)
            lines.append("```")

        # Relationships as flat comma-separated (D-02: no confidence, no line numbers in per-file)
        chunk_rels = [r for r in relationships if r.get("source_id") == chunk.id]
        outgoing_by_type: dict[str, list[str]] = {}
        for r in chunk_rels:
            rt = r.get("rel_type", "unknown")
            target = r.get("target_name_resolved", r.get("target_name", "?"))
            if r.get("source_id") == r.get("target_id"):
                target = f"? ({r.get('target_name', 'unknown')})"
            outgoing_by_type.setdefault(rt, []).append(target)

        for rt, targets in outgoing_by_type.items():
            lines.append(f"{rt}: {', '.join(targets)}")

        lines.append("")

    return "\n".join(lines)
```

Implement `_generate_codebase_md()` — consolidated root file (D-04):

```python
def _generate_codebase_md(indexed_files, file_data):
    """Generate consolidated CODEBASE.md merging index + architecture + relationships."""
    lines = []

    lines.append("# Codebase")
    lines.append("")
    lines.append(f"generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"total_files: {len(indexed_files)}")
    total_chunks = sum(len(d.get("chunks", [])) for d in file_data.values())
    lines.append(f"total_chunks: {total_chunks}")
    lines.append("")

    # Statistics as KV
    all_chunks = []
    for d in file_data.values():
        all_chunks.extend(d.get("chunks", []))
    func_count = sum(1 for c in all_chunks if c.chunk_type == ChunkType.FUNCTION)
    class_count = sum(1 for c in all_chunks if c.chunk_type == ChunkType.CLASS)
    method_count = sum(1 for c in all_chunks if c.chunk_type == ChunkType.METHOD)
    lines.append(f"functions: {func_count}")
    lines.append(f"classes: {class_count}")
    lines.append(f"methods: {method_count}")
    lines.append("")

    # Module grouping (from architecture)
    modules = _group_by_module(file_data)
    lines.append(f"## Modules ({len(modules)})")
    lines.append("")
    for module_name, file_paths in modules.items():
        lines.append(f"### {module_name}")
        lines.append("")
        for fp in file_paths:
            data = file_data[fp]
            chunks = data.get("chunks", [])
            summary = data.get("summary", "")
            short = summary[:100] + "..." if len(summary) > 100 else summary
            lines.append(f"{fp}: {len(chunks)} chunks - {short}")
        lines.append("")

    # Entry points (from architecture)
    entry_points = _detect_entry_points(file_data)
    if entry_points:
        lines.append("## Entry Points")
        lines.append("")
        for ep in entry_points:
            chunks_str = ", ".join(ep["chunk_names"][:5]) or "none"
            lines.append(f"{ep['path']}: {ep['method']} ({chunks_str})")
        lines.append("")

    # Key interfaces (from architecture)
    key_interfaces = _compute_key_interfaces(file_data)
    if key_interfaces:
        lines.append("## Key Interfaces")
        lines.append("")
        for iface in key_interfaces:
            summary_part = f" - {iface['summary'][:60]}" if iface['summary'] else ""
            lines.append(f"{iface['name']} ({iface['type']}, {iface['file']}): used by {iface['used_by_count']} files{summary_part}")
        lines.append("")

    # Cross-file dependencies (from relationships)
    lines.append("## Dependencies")
    lines.append("")
    for path in sorted(file_data.keys()):
        rels = file_data[path].get("relationships", [])
        chunks = file_data[path].get("chunks", [])
        chunk_ids = {c.id for c in chunks}

        imports_from: set[str] = set()
        calls_to: set[str] = set()
        imported_by: set[str] = set()
        called_by: set[str] = set()

        for rel in rels:
            if rel.get("direction") == "incoming":
                src_id = rel.get("source_id", "")
                src_file = src_id.split("::")[0] if "::" in src_id else ""
                if src_file and src_file != path:
                    if rel.get("rel_type") == "imports":
                        imported_by.add(src_file)
                    elif rel.get("rel_type") == "calls":
                        called_by.add(src_file)
            else:
                target_id = rel.get("target_id", "")
                target_file = target_id.split("::")[0] if "::" in target_id else ""
                if target_file and target_file != path and target_id not in chunk_ids:
                    if rel.get("rel_type") == "imports":
                        imports_from.add(target_file)
                    elif rel.get("rel_type") == "calls":
                        calls_to.add(target_file)

        if imports_from or calls_to or imported_by or called_by:
            lines.append(f"### {path}")
            lines.append("")
            if imports_from:
                lines.append(f"imports: {', '.join(sorted(imports_from))}")
            if imported_by:
                lines.append(f"imported_by: {', '.join(sorted(imported_by))}")
            if calls_to:
                lines.append(f"calls: {', '.join(sorted(calls_to))}")
            if called_by:
                lines.append(f"called_by: {', '.join(sorted(called_by))}")
            lines.append("")

    # Per-file index
    lines.append("## Files")
    lines.append("")
    for path in sorted(indexed_files.keys()):
        data = file_data.get(path, {})
        record = data.get("record")
        chunks = data.get("chunks", [])
        lang = record.language.value if record and hasattr(record, "language") else "?"

        if record and hasattr(record, 'file_summary') and record.file_summary:
            summary = record.file_summary
        else:
            ai_summaries = [c.summary for c in chunks if c.summary]
            summary = "; ".join(ai_summaries) if ai_summaries else data.get("summary", "")

        lines.append(f"### {path}")
        lines.append("")
        lines.append(f"language: {lang}")
        lines.append(f"chunks: {len(chunks)}")
        lines.append(f"summary: {summary}")
        lines.append("")

    return "\n".join(lines)
```

Note: This reuses existing helper functions `_group_by_module()`, `_detect_entry_points()`, `_compute_key_interfaces()` directly — no duplication.
</action>

<acceptance_criteria>
- `export.py` contains `class MarkdownKVRenderer(FormatRenderer)`
- `_format_kv_file()` produces output starting with `# {file_path}` followed by key-value pairs like `language: python`, `last_indexed: ...`, `chunk_count: N`
- `_format_kv_file()` renders each chunk as `## {chunk_name}` with `type:`, `lines:`, `summary:`, and relationship keys
- `_format_kv_file()` renders relationships as comma-separated targets: `calls: func1, func2` (no confidence levels, no line numbers)
- `_generate_codebase_md()` produces a single file with sections: `## Modules`, `## Entry Points`, `## Key Interfaces`, `## Dependencies`, `## Files`
- `get_renderer(ExportFormat.MARKDOWN_KV).file_extension()` returns `".md"`
- `get_renderer(ExportFormat.MARKDOWN_KV).generate_root_files(...)` returns `{"CODEBASE.md": "..."}`
</acceptance_criteria>

---

## Task 4: Implement JSON and YAML Renderers

<objective>Add JSON and YAML format renderers that serialize export data directly.</objective>

<read_first>
- 02-worktrees/glma/src/glma/export.py (after Tasks 2-3, renderer protocol and MarkdownKVRenderer)
- 02-worktrees/glma/src/glma/models.py (ExportFormat, Chunk, FileRecord fields)
- 02-worktrees/glma/pyproject.toml (current dependencies — need to check if pyyaml exists)
</read_first>

<action>
In `export.py`, after `MarkdownKVRenderer`:

1. Add import at top of file:
```python
import yaml  # pyyaml
```

2. Implement JsonRenderer:
```python
class JsonRenderer(FormatRenderer):
    """Renders export as JSON objects."""

    def format_file(self, file_path, file_record, chunks, relationships, config):
        data = _serialize_file_data(file_path, file_record, chunks, relationships, config)
        return json.dumps(data, indent=2, default=str)

    def generate_root_files(self, indexed_files, file_data):
        root_data = {
            "generated": datetime.now(timezone.utc).isoformat(),
            "total_files": len(indexed_files),
            "files": {
                path: _serialize_file_data(
                    path,
                    data.get("record"),
                    data.get("chunks", []),
                    data.get("relationships", []),
                    ExportConfig(),  # default config for serialization
                )
                for path, data in file_data.items()
            },
        }
        return {"export.json": json.dumps(root_data, indent=2, default=str)}

    def file_extension(self):
        return ".json"
```

3. Implement YamlRenderer:
```python
class YamlRenderer(FormatRenderer):
    """Renders export as YAML."""

    def format_file(self, file_path, file_record, chunks, relationships, config):
        data = _serialize_file_data(file_path, file_record, chunks, relationships, config)
        return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    def generate_root_files(self, indexed_files, file_data):
        root_data = {
            "generated": datetime.now(timezone.utc).isoformat(),
            "total_files": len(indexed_files),
            "files": {
                path: _serialize_file_data(
                    path,
                    data.get("record"),
                    data.get("chunks", []),
                    data.get("relationships", []),
                    ExportConfig(),  # default config for serialization
                )
                for path, data in file_data.items()
            },
        }
        return {"export.yaml": yaml.dump(root_data, default_flow_style=False, allow_unicode=True, sort_keys=False)}

    def file_extension(self):
        return ".yaml"
```

4. Add shared serialization helper:
```python
def _serialize_file_data(file_path, file_record, chunks, relationships, config):
    """Serialize file data to a plain dict for JSON/YAML renderers."""
    result = {"path": file_path}

    if file_record:
        result["metadata"] = {
            "language": file_record.language.value if hasattr(file_record.language, 'value') else str(file_record.language),
            "last_indexed": file_record.last_indexed,
            "chunk_count": file_record.chunk_count,
            "content_hash": file_record.content_hash,
        }
        if hasattr(file_record, 'file_summary') and file_record.file_summary:
            result["metadata"]["file_summary"] = file_record.file_summary

    result["chunks"] = [
        {
            "name": c.name,
            "type": c.chunk_type.value,
            "start_line": c.start_line,
            "end_line": c.end_line,
            "summary": c.summary,
            "content": c.content if config.include_code else None,
            "parent_id": c.parent_id,
        }
        for c in chunks
    ]

    result["relationships"] = [
        {
            "source": r.get("source_name", ""),
            "target": r.get("target_name_resolved", r.get("target_name", "")),
            "type": r.get("rel_type", ""),
            "confidence": r.get("confidence", ""),
            "line": r.get("source_line", None),
        }
        for r in relationships
    ]

    return result
```

5. Update `pyproject.toml` dependencies to add `pyyaml`:
Add `"pyyaml>=6.0"` to the dependencies list in `pyproject.toml`.
</action>

<acceptance_criteria>
- `export.py` contains `class JsonRenderer(FormatRenderer)` and `class YamlRenderer(FormatRenderer)`
- `get_renderer(ExportFormat.JSON).file_extension()` returns `".json"`
- `get_renderer(ExportFormat.YAML).file_extension()` returns `".yaml"`
- `JsonRenderer.format_file()` returns valid JSON (`json.loads()` succeeds)
- `YamlRenderer.format_file()` returns valid YAML (`yaml.safe_load()` succeeds)
- `JsonRenderer.generate_root_files()` returns `{"export.json": "..."}`
- `YamlRenderer.generate_root_files()` returns `{"export.yaml": "..."}`
- `pyproject.toml` contains `"pyyaml>=6.0"` in dependencies
- `_serialize_file_data()` is a shared function used by both renderers
</acceptance_criteria>

---

## Task 5: Wire Renderers into export_index() and Writers

<objective>Update the export orchestration pipeline to use the strategy pattern, routing through the appropriate renderer based on ExportConfig.format.</objective>

<read_first>
- 02-worktrees/glma/src/glma/export.py (current `export_index()`, `_write_files_to_dir()`, `_write_tar_to_stream()` — full function signatures and bodies)
</read_first>

<action>
In `export.py`:

1. Update `export_index()` to use renderer. Replace the per-file formatting loop and root file generation:

Current code:
```python
    # Generate per-file export markdown
    file_exports: dict[str, str] = {}
    for file_path, data in file_data.items():
        export_md = _format_export_file(
            file_path,
            data["record"],
            data["chunks"],
            data["relationships"],
            config,
        )
        file_exports[file_path] = export_md

    # Generate root files
    index_md = generate_index_md(indexed_files, file_data)
    rels_md = generate_relationships_md(file_data)
    arch_md = generate_architecture_md(file_data)
```

Replace with:
```python
    # Select renderer based on format
    renderer = get_renderer(config.format)
    ext = renderer.file_extension()

    # Generate per-file exports
    file_exports: dict[str, str] = {}
    for file_path, data in file_data.items():
        export_content = renderer.format_file(
            file_path,
            data["record"],
            data["chunks"],
            data["relationships"],
            config,
        )
        file_exports[file_path] = export_content

    # Generate root files
    root_files = renderer.generate_root_files(indexed_files, file_data)
```

2. Update the three output modes. Current:
```python
    if output == "-":
        _write_tar_to_stream(sys.stdout.buffer, file_exports, index_md, rels_md, arch_md)
        return Path("-")
    elif output.endswith(".tar.gz") or output.endswith(".tgz"):
        output_path = Path(output)
        with open(output_path, "wb") as f:
            _write_tar_to_stream(f, file_exports, index_md, rels_md, arch_md)
        ...
    else:
        output_dir = Path(output)
        output_dir.mkdir(parents=True, exist_ok=True)
        _write_files_to_dir(output_dir, file_exports, index_md, rels_md, arch_md)
        ...
```

Replace with:
```python
    if output == "-":
        _write_tar_to_stream(sys.stdout.buffer, file_exports, root_files, ext)
        return Path("-")
    elif output.endswith(".tar.gz") or output.endswith(".tgz"):
        output_path = Path(output)
        with open(output_path, "wb") as f:
            _write_tar_to_stream(f, file_exports, root_files, ext)
        ...
    else:
        output_dir = Path(output)
        output_dir.mkdir(parents=True, exist_ok=True)
        _write_files_to_dir(output_dir, file_exports, root_files, ext)
        ...
```

3. Update `_write_files_to_dir()` signature:
```python
def _write_files_to_dir(
    output_dir: Path,
    file_exports: dict[str, str],
    root_files: dict[str, str],
    file_ext: str = ".md",
) -> None:
    """Write export files to a directory."""
    # Write per-file exports
    for file_path, content in file_exports.items():
        md_path = output_dir / (file_path + file_ext)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(content, encoding="utf-8")

    # Write root files
    for name, content in root_files.items():
        (output_dir / name).write_text(content, encoding="utf-8")
```

4. Update `_write_tar_to_stream()` signature:
```python
def _write_tar_to_stream(
    stream: io.RawIOBase,
    file_exports: dict[str, str],
    root_files: dict[str, str],
    file_ext: str = ".md",
) -> None:
    """Write export as tar.gz archive to a stream."""
    with tarfile.open(fileobj=stream, mode="w|gz") as tar:
        # Add per-file exports
        for file_path, content in file_exports.items():
            data = content.encode("utf-8")
            info = tarfile.TarInfo(name=file_path + file_ext)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))

        # Add root files
        for name, content in root_files.items():
            data = content.encode("utf-8")
            info = tarfile.TarInfo(name=name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
```
</action>

<acceptance_criteria>
- `export_index()` calls `get_renderer(config.format)` and uses `renderer.format_file()` and `renderer.generate_root_files()` instead of calling `_format_export_file()`, `generate_index_md()`, etc. directly
- `_write_files_to_dir()` accepts `root_files: dict[str, str]` and `file_ext: str = ".md"` parameters (no longer takes `index_md`, `rels_md`, `arch_md` separately)
- `_write_tar_to_stream()` accepts `root_files: dict[str, str]` and `file_ext: str = ".md"` parameters
- Markdown format export still produces exactly INDEX.md, RELATIONSHIPS.md, ARCHITECTURE.md (backward compatible)
- KV format export produces CODEBASE.md as the only root file
- JSON format export produces export.json root file
- YAML format export produces export.yaml root file
</acceptance_criteria>

---

## Task 6: Add --format Flag to CLI Export and Query Commands

<objective>Add the --format/-f flag to `glma export` command, update `glma query` command to accept yaml format, wire format value into configs.</objective>

<read_first>
- 02-worktrees/glma/src/glma/cli.py (export command at ~line 418, query command at ~line 216 with existing `--format`)
- 02-worktrees/glma/src/glma/models.py (ExportFormat enum after Task 1)
</read_first>

<action>
In `cli.py`:

1. Add `--format`/`-f` to the `export` command. Add a new parameter after `include_code`:

```python
    format: str = typer.Option(
        "markdown-kv",
        "--format",
        "-f",
        help="Export format: markdown-kv, markdown, json, yaml.",
    ),
```

2. In the export command body, validate the format and add to overrides:

After the existing `export_overrides` dict building, add:
```python
    # Validate and set format
    from glma.models import ExportFormat
    try:
        export_format = ExportFormat(format)
    except ValueError:
        valid = ", ".join(f.value for f in ExportFormat)
        console.print(f"[red]Error:[/red] Invalid format '{format}'. Must be one of: {valid}")
        raise typer.Exit(4)
    export_overrides["format"] = export_format
```

3. In the `query` command, update the `output_format` validation. Current:
```python
    if output_format not in ("markdown", "json"):
        sys.stderr.write("Error: format must be 'markdown' or 'json'\n")
        raise typer.Exit(4)
```

Replace with:
```python
    from glma.models import ExportFormat
    try:
        fmt = ExportFormat(output_format)
    except ValueError:
        valid = ", ".join(f.value for f in ExportFormat)
        sys.stderr.write(f"Error: format must be one of: {valid}\n")
        raise typer.Exit(4)
```

4. Update the query command's `output_format` option help text:
```python
    output_format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown-kv, markdown, json, yaml."),
```

5. Update the query output format dispatch. Current:
```python
    if cfg.output_format == "json":
        from glma.query.formatter import format_json_output
        output_text = format_json_output(filepath, file_record, chunks, all_rels_flat, verbose=cfg.verbose)
    else:
        from glma.query.formatter import format_compact_output
        output_text = format_compact_output(filepath, file_record, chunks, relationships, query_config=cfg)
```

Replace with:
```python
    from glma.models import ExportFormat as EF
    if cfg.output_format == EF.JSON:
        from glma.query.formatter import format_json_output
        output_text = format_json_output(filepath, file_record, chunks, all_rels_flat, verbose=cfg.verbose)
    elif cfg.output_format == EF.YAML:
        from glma.query.formatter import format_yaml_output
        output_text = format_yaml_output(filepath, file_record, chunks, all_rels_flat, verbose=cfg.verbose)
    elif cfg.output_format == EF.MARKDOWN_KV:
        from glma.query.formatter import format_kv_output
        output_text = format_kv_output(filepath, file_record, chunks, relationships, query_config=cfg)
    else:
        from glma.query.formatter import format_compact_output
        output_text = format_compact_output(filepath, file_record, chunks, relationships, query_config=cfg)
```
</action>

<acceptance_criteria>
- `glma export --format markdown-kv` sets format to markdown-kv (default)
- `glma export --format markdown` sets format to markdown
- `glma export --format json` sets format to json
- `glma export --format yaml` sets format to yaml
- `glma export -f json` works (short alias)
- `glma export --format invalid` exits with error code 4 and shows valid format names
- `glma query --format yaml` works (new format option for query)
- `glma query --format markdown` still works (backward compatible)
- `glma query --format json` still works (backward compatible)
- Invalid format on query exits with error code 4
</acceptance_criteria>

---

## Task 7: Add YAML and KV Query Output Formatters

<objective>Add format_yaml_output and format_kv_output functions to the query formatter module.</objective>

<read_first>
- 02-worktrees/glma/src/glma/query/formatter.py (current format_json_output, format_compact_output, all helper functions)
- 02-worktrees/glma/src/glma/models.py (ExportFormat enum)
</read_first>

<action>
In `query/formatter.py`:

1. Add import at top:
```python
import yaml
```

2. Add `format_yaml_output()` function:
```python
def format_yaml_output(
    file_path: str,
    file_record: FileRecord,
    chunks: list[Chunk],
    relationships: list[dict],
    verbose: bool = False,
) -> str:
    """Generate YAML output for programmatic consumption."""
    result = {
        "file": file_path,
        "metadata": {
            "language": file_record.language.value,
            "last_indexed": file_record.last_indexed,
            "chunk_count": file_record.chunk_count,
            "content_hash": file_record.content_hash,
        },
        "chunks": [
            {
                "name": chunk.name,
                "type": chunk.chunk_type.value,
                "start_line": chunk.start_line,
                "end_line": chunk.end_line,
                "docstring": chunk.attached_comments[0] if chunk.attached_comments else None,
                "summary": chunk.summary,
                "content": chunk.content if verbose else None,
            }
            for chunk in chunks
        ],
        "relationships": {
            "outgoing": [r for r in relationships if r.get("direction") != "incoming"],
            "incoming": [r for r in relationships if r.get("direction") == "incoming"],
        },
    }
    return yaml.dump(result, default_flow_style=False, allow_unicode=True, sort_keys=False)
```

3. Add `format_kv_output()` function for query's KV mode:
```python
def format_kv_output(
    file_path: str,
    file_record: FileRecord,
    chunks: list[Chunk],
    relationships: dict,
    verbose: bool = False,
    query_config: Optional[QueryConfig] = None,
) -> str:
    """Generate compact key-value markdown for a queried file."""
    if query_config is None:
        query_config = QueryConfig(verbose=verbose)

    lines: list[str] = []

    lines.append(f"# {file_path}")
    lines.append("")
    lines.append(f"language: {file_record.language.value}")
    lines.append(f"last_indexed: {file_record.last_indexed}")
    lines.append(f"chunk_count: {file_record.chunk_count}")
    lines.append("")

    if not query_config.summary_only:
        for chunk in chunks:
            if chunk.parent_id is not None:
                continue
            lines.append(f"## {chunk.name}")
            lines.append("")
            lines.append(f"type: {chunk.chunk_type.value}")
            lines.append(f"lines: L{chunk.start_line}-L{chunk.end_line}")

            if chunk.summary:
                lines.append(f"summary: {chunk.summary}")

            if query_config.verbose:
                lang = _get_lang_hint(file_path)
                lines.append("")
                lines.append(f"```{lang}")
                lines.append(chunk.content)
                lines.append("```")

            # Relationships
            if not query_config.no_relationships:
                chunk_rels = relationships.get(chunk.id, {"outgoing": [], "incoming": []})
                outgoing = chunk_rels.get("outgoing", [])
                incoming = chunk_rels.get("incoming", [])

                # Filter by rel_types if specified
                if query_config.rel_types:
                    outgoing = [r for r in outgoing if r.get("rel_type") in query_config.rel_types]
                    incoming = [r for r in incoming if r.get("rel_type") in query_config.rel_types]

                outgoing_by_type: dict[str, list[str]] = {}
                for rel in outgoing:
                    rt = rel.get("rel_type", "unknown")
                    if rel.get("source_id") == rel.get("target_id") and rel.get("source_id"):
                        target_display = f"? ({rel.get('target_name', 'unknown')})"
                    elif rel.get("target_name_resolved"):
                        target_display = rel["target_name_resolved"]
                    else:
                        target_display = rel.get("target_name", "unknown")
                    outgoing_by_type.setdefault(rt, []).append(target_display)

                for rt, targets in outgoing_by_type.items():
                    lines.append(f"{rt}: {', '.join(targets)}")

                incoming_by_type: dict[str, list[str]] = {}
                for rel in incoming:
                    rt = rel.get("rel_type", "unknown")
                    source_name = rel.get("source_chunk_name", rel.get("source_name", "unknown"))
                    incoming_by_type.setdefault(rt, []).append(source_name)

                for rt, sources in incoming_by_type.items():
                    lines.append(f"{rt}_from: {', '.join(sources)}")

            lines.append("")

    return "\n".join(lines)
```
</action>

<acceptance_criteria>
- `formatter.py` contains `format_yaml_output(file_path, file_record, chunks, relationships, verbose)` function
- `formatter.py` contains `format_kv_output(file_path, file_record, chunks, relationships, verbose, query_config)` function
- `format_yaml_output()` returns valid YAML string
- `format_kv_output()` returns KV markdown with `# filename`, `language:`, `type:`, `lines:` structure
- `from glma.query.formatter import format_yaml_output, format_kv_output` succeeds
</acceptance_criteria>

---

## Task 8: Update and Add Tests

<objective>Update existing tests for new signatures, add comprehensive tests for all four format renderers.</objective>

<read_first>
- 02-worktrees/glma/tests/test_export.py (all existing tests — understand current test structure and which signatures changed)
- 02-worktrees/glma/src/glma/export.py (new `_write_files_to_dir()` and `_write_tar_to_stream()` signatures from Task 5)
- 02-worktrees/glma/src/glma/models.py (ExportFormat enum)
</read_first>

<action>
In `test_export.py`:

1. Update all calls to `_write_files_to_dir()` to use new signature. Current pattern:
```python
_write_files_to_dir(tmp_path, file_exports, "# Index", "# Rels", "# Arch")
```
Replace with:
```python
_write_files_to_dir(tmp_path, file_exports, {"INDEX.md": "# Index", "RELATIONSHIPS.md": "# Rels", "ARCHITECTURE.md": "# Arch"})
```

Specifically update these test methods:
- `TestDirectoryOutput::test_creates_nested_structure` — update `_write_files_to_dir` call, keep assertions for INDEX.md, RELATIONSHIPS.md, ARCHITECTURE.md
- `TestDirectoryOutput::test_file_content_correct` — update `_write_files_to_dir` call, keep assertions
- `TestGenerateArchitectureMd::test_architecture_md_in_directory_output` — update `_write_files_to_dir` call, keep ARCHITECTURE.md assertion

2. Add new test class for KV format:
```python
class TestMarkdownKVRenderer:
    """Tests for MarkdownKVRenderer."""

    def test_kv_file_basic_structure(self):
        """KV file has heading + key-value metadata."""
        from glma.export import MarkdownKVRenderer
        from glma.models import ExportFormat
        renderer = MarkdownKVRenderer()
        chunks = [_make_chunk("my_func")]
        config = ExportConfig(format=ExportFormat.MARKDOWN_KV)
        md = renderer.format_file("src/test.py", None, chunks, [], config)
        assert "# src/test.py" in md
        assert "## my_func" in md
        assert "type: function" in md
        assert "lines: L1-L10" in md

    def test_kv_file_with_record(self):
        """KV file includes file metadata from record."""
        from glma.export import MarkdownKVRenderer
        from glma.models import FileRecord, Language
        renderer = MarkdownKVRenderer()
        chunks = [_make_chunk()]
        record = FileRecord(path="src/test.py", language=Language.PYTHON, content_hash="abc",
                           last_indexed="2026-04-14T00:00:00Z", chunk_count=1)
        config = ExportConfig(format=ExportFormat.MARKDOWN_KV)
        md = renderer.format_file("src/test.py", record, chunks, [], config)
        assert "language: python" in md
        assert "last_indexed: 2026-04-14T00:00:00Z" in md
        assert "chunk_count: 1" in md

    def test_kv_relationships_flat(self):
        """KV relationships rendered as comma-separated targets."""
        from glma.export import MarkdownKVRenderer
        renderer = MarkdownKVRenderer()
        chunks = [_make_chunk("caller")]
        rels = [{
            "source_id": chunks[0].id,
            "source_name": "caller",
            "rel_type": "calls",
            "confidence": "DIRECT",
            "source_line": 5,
            "target_name": "func_a",
            "target_id": "other::function::func_a::1",
        }]
        config = ExportConfig(format=ExportFormat.MARKDOWN_KV)
        md = renderer.format_file("src/test.py", None, chunks, rels, config)
        assert "calls: func_a" in md

    def test_kv_code_included(self):
        """KV format respects include_code."""
        from glma.export import MarkdownKVRenderer
        renderer = MarkdownKVRenderer()
        chunks = [_make_chunk("my_func")]
        config = ExportConfig(format=ExportFormat.MARKDOWN_KV, include_code=True)
        md = renderer.format_file("src/test.py", None, chunks, [], config)
        assert "```python" in md

    def test_kv_root_generates_codebase_md(self):
        """KV renderer generates CODEBASE.md as root file."""
        from glma.export import MarkdownKVRenderer
        renderer = MarkdownKVRenderer()
        indexed_files = {"test.py": "hash1"}
        file_data = {"test.py": {"chunks": [_make_chunk()], "summary": "Test file.", "record": None}}
        root = renderer.generate_root_files(indexed_files, file_data)
        assert "CODEBASE.md" in root
        assert len(root) == 1

    def test_kv_file_extension(self):
        """KV renderer uses .md extension."""
        from glma.export import MarkdownKVRenderer
        renderer = MarkdownKVRenderer()
        assert renderer.file_extension() == ".md"
```

3. Add test class for JSON format:
```python
class TestJsonRenderer:
    """Tests for JsonRenderer."""

    def test_json_valid_output(self):
        """JSON renderer produces valid JSON."""
        import json
        from glma.export import JsonRenderer
        renderer = JsonRenderer()
        chunks = [_make_chunk()]
        config = ExportConfig(format=ExportFormat.JSON)
        output = renderer.format_file("src/test.py", None, chunks, [], config)
        parsed = json.loads(output)
        assert parsed["path"] == "src/test.py"
        assert len(parsed["chunks"]) == 1

    def test_json_root_file(self):
        """JSON renderer generates export.json root file."""
        from glma.export import JsonRenderer
        renderer = JsonRenderer()
        indexed_files = {"test.py": "h"}
        file_data = {"test.py": {"chunks": [], "summary": "", "record": None}}
        root = renderer.generate_root_files(indexed_files, file_data)
        assert "export.json" in root
        assert len(root) == 1

    def test_json_extension(self):
        assert JsonRenderer().file_extension() == ".json"
```

4. Add test class for YAML format:
```python
class TestYamlRenderer:
    """Tests for YamlRenderer."""

    def test_yaml_valid_output(self):
        """YAML renderer produces valid YAML."""
        import yaml
        from glma.export import YamlRenderer
        renderer = YamlRenderer()
        chunks = [_make_chunk()]
        config = ExportConfig(format=ExportFormat.YAML)
        output = renderer.format_file("src/test.py", None, chunks, [], config)
        parsed = yaml.safe_load(output)
        assert parsed["path"] == "src/test.py"

    def test_yaml_root_file(self):
        from glma.export import YamlRenderer
        renderer = YamlRenderer()
        indexed_files = {"test.py": "h"}
        file_data = {"test.py": {"chunks": [], "summary": "", "record": None}}
        root = renderer.generate_root_files(indexed_files, file_data)
        assert "export.yaml" in root

    def test_yaml_extension(self):
        assert YamlRenderer().file_extension() == ".yaml"
```

5. Add test for get_renderer factory:
```python
class TestGetRenderer:
    """Tests for renderer factory."""

    def test_markdown_returns_markdown_renderer(self):
        from glma.export import get_renderer, MarkdownRenderer
        r = get_renderer(ExportFormat.MARKDOWN)
        assert isinstance(r, MarkdownRenderer)

    def test_kv_returns_kv_renderer(self):
        from glma.export import get_renderer, MarkdownKVRenderer
        r = get_renderer(ExportFormat.MARKDOWN_KV)
        assert isinstance(r, MarkdownKVRenderer)

    def test_json_returns_json_renderer(self):
        from glma.export import get_renderer, JsonRenderer
        r = get_renderer(ExportFormat.JSON)
        assert isinstance(r, JsonRenderer)

    def test_yaml_returns_yaml_renderer(self):
        from glma.export import get_renderer, YamlRenderer
        r = get_renderer(ExportFormat.YAML)
        assert isinstance(r, YamlRenderer)
```

6. Add test for query YAML output:
```python
class TestQueryYamlOutput:
    """Tests for YAML query output."""

    def test_yaml_output_valid(self):
        import yaml
        from glma.query.formatter import format_yaml_output
        from glma.models import FileRecord, Language
        record = FileRecord(path="test.py", language=Language.PYTHON, content_hash="h",
                          last_indexed="2026-04-14T00:00:00Z", chunk_count=1)
        chunks = [_make_chunk()]
        output = format_yaml_output("test.py", record, chunks, [])
        parsed = yaml.safe_load(output)
        assert parsed["file"] == "test.py"
        assert parsed["metadata"]["language"] == "python"
```

7. Ensure existing tests that construct `ExportConfig()` still pass. Any test that creates `ExportConfig()` without specifying format will now get `markdown-kv` default. Tests that depend on markdown-specific behavior must explicitly pass `format=ExportFormat.MARKDOWN`. Check these tests:
- `TestFormatExportFile::*` — all construct `ExportConfig()` or `ExportConfig(include_code=...)`. These call `_format_export_file()` directly (NOT through renderer), so format field doesn't affect them. No change needed.
- `TestDirectoryOutput::*` — call `_write_files_to_dir()` directly. Update signature only.
</action>

<acceptance_criteria>
- All existing tests pass: `cd 02-worktrees/glma && python -m pytest tests/test_export.py -v` exits 0
- New test class `TestMarkdownKVRenderer` with at least 6 tests covering KV file structure, metadata, relationships, code inclusion, root file, and extension
- New test class `TestJsonRenderer` with at least 3 tests
- New test class `TestYamlRenderer` with at least 3 tests
- New test class `TestGetRenderer` with 4 tests (one per format)
- New test class `TestQueryYamlOutput` with at least 1 test
- `_write_files_to_dir` calls updated in `TestDirectoryOutput::test_creates_nested_structure`, `test_file_content_correct`, `TestGenerateArchitectureMd::test_architecture_md_in_directory_output`
</acceptance_criteria>

---

## Task 9: Install pyyaml and Run Full Test Suite

<objective>Install the new pyyaml dependency and verify all 274+ existing tests plus new tests pass.</objective>

<read_first>
- 02-worktrees/glma/pyproject.toml (verify pyyaml added in Task 4)
</read_first>

<action>
1. Install pyyaml:
```bash
cd 02-worktrees/glma && pip install pyyaml
```

2. Run full test suite:
```bash
cd 02-worktrees/glma && python -m pytest tests/ -v --tb=short 2>&1 | tail -50
```

3. If any tests fail:
   - For failures in existing tests due to signature changes: update call sites to match new signatures
   - For failures in `test_export.py` due to `_write_files_to_dir` signature: verify all calls pass `root_files` dict instead of separate strings
   - For import errors: verify `pyyaml` is installed and `yaml` module is available

4. Verify test count increased by at least 15 (new format tests).
</action>

<acceptance_criteria>
- `pip install pyyaml` succeeds
- `cd 02-worktrees/glma && python -m pytest tests/ -v` exits 0
- All existing tests pass (no regressions)
- New test classes appear in output: `TestMarkdownKVRenderer`, `TestJsonRenderer`, `TestYamlRenderer`, `TestGetRenderer`, `TestQueryYamlOutput`
- Total test count is at least 289 (274 existing + 15 new minimum)
</acceptance_criteria>

---

## Verification Criteria

After all tasks complete, verify the phase goal:

1. **Default format is KV**: Run `glma export` without `--format` and confirm output files use KV format with `key: value` pairs and CODEBASE.md root file
2. **Markdown backward compatible**: Run `glma export --format markdown` and confirm output matches previous behavior (INDEX.md, RELATIONSHIPS.md, ARCHITECTURE.md with tables)
3. **JSON format works**: Run `glma export --format json` and confirm per-file `.json` exports and `export.json` root file
4. **YAML format works**: Run `glma export --format yaml` and confirm per-file `.yaml` exports and `export.yaml` root file
5. **All tests pass**: `cd 02-worktrees/glma && python -m pytest tests/ -v` exits 0

## must_haves

- `ExportFormat` enum in `models.py` with `markdown_kv`, `markdown`, `json`, `yaml` values
- `glma export` defaults to `markdown-kv` format without any `--format` flag
- `glma export --format markdown` produces identical output to previous version (backward compatible)
- KV format per-file output matches CONTEXT.md D-01/D-02 decisions (flat inline, comma-separated relationships)
- CODEBASE.md consolidates INDEX + RELATIONSHIPS + ARCHITECTURE data into single root file (D-04)
- `FormatRenderer` strategy pattern with per-format implementations (D-10)
- `--format`/`-f` flag on both export and query commands (D-07)
- All existing 274 tests pass
- New tests cover each format renderer

---

*Phase: 11-markdown-keyvalue-export*
*Plan created: 2026-04-14*
