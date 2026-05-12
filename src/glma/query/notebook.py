"""Jupyter notebook compaction to compacted markdown.

Parses .ipynb files with nbformat, extracts per-statement variable definitions/references,
tracks cross-cell variable flow, generates rule-based section summaries, and outputs
compacted markdown.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import nbformat

from glma.query.variables import CellVariableInfo, extract_cell_variables, build_variable_flow

if TYPE_CHECKING:
    from glma.summarize.providers import SummarizerProvider


@dataclass
class CachedCell:
    """A cached cell summary entry."""
    index: int
    content_hash: str
    summary: str


def _cell_content_hash(source: str) -> str:
    """Compute BLAKE2b hash of cell source content."""
    return hashlib.blake2b(source.encode("utf-8"), digest_size=32).hexdigest()


def _cell_content_hash_with_outputs(source: str, outputs: list) -> str:
    """Compute BLAKE2b hash of cell source + outputs (for cache invalidation)."""
    hasher = hashlib.blake2b(digest_size=32)
    hasher.update(source.encode("utf-8"))
    for output in outputs:
        output_type = output.get("output_type", "")
        if output_type == "stream":
            text = output.get("text", "")
            if isinstance(text, list):
                text = "".join(text)
            hasher.update(text.encode("utf-8"))
        elif output_type == "execute_result":
            data = output.get("data", {})
            text = data.get("text/plain", "")
            if isinstance(text, list):
                text = "".join(text)
            hasher.update(text.encode("utf-8"))
        elif output_type == "error":
            hasher.update(output.get("ename", "").encode("utf-8"))
            hasher.update(output.get("evalue", "").encode("utf-8"))
    return hasher.hexdigest()


def _format_outputs_for_context(outputs: list, max_chars: int = 1500) -> str:
    """Format cell outputs as text for LLM context, truncated to max_chars.

    Returns a string representation of the outputs suitable for including
    in a summarization prompt. Truncates with a marker if too long.
    """
    parts: list[str] = []
    for output in outputs:
        output_type = output.get("output_type", "")
        if output_type == "stream":
            text = output.get("text", "")
            if isinstance(text, list):
                text = "".join(text)
            parts.append(text.rstrip())
        elif output_type == "execute_result":
            data = output.get("data", {})
            text = data.get("text/plain", "")
            if isinstance(text, list):
                text = "".join(text)
            parts.append(text.rstrip())
        elif output_type == "error":
            ename = output.get("ename", "Error")
            evalue = output.get("evalue", "")
            parts.append(f"[Error: {ename}: {evalue}]")
        elif output_type == "display_data":
            parts.append("[Display output]")

    if not parts:
        return ""

    combined = "\n".join(parts)
    if len(combined) > max_chars:
        combined = combined[:max_chars] + f"\n... (truncated, {len(combined)} chars total)"
    return combined


def _notebook_file_hash(filepath: Path) -> str:
    """Compute BLAKE2b hash of the notebook file contents."""
    content = filepath.read_bytes()
    return hashlib.blake2b(content, digest_size=32).hexdigest()


def _load_cache(cache_dir: Path, notebook_path: Path) -> dict[int, tuple[str, str]]:
    """Load cached cell summaries from disk.

    Returns dict mapping cell_index → (content_hash, summary).
    Returns empty dict if cache doesn't exist or is malformed.
    """
    file_hash = _notebook_file_hash(notebook_path)
    cache_file = cache_dir / f"{notebook_path.stem}-{file_hash}.json"
    if not cache_file.exists():
        return {}
    try:
        data = json.loads(cache_file.read_text("utf-8"))
        result = {}
        for cell_entry in data.get("cells", []):
            idx = cell_entry.get("index", -1)
            chash = cell_entry.get("content_hash", "")
            summary = cell_entry.get("summary", "")
            if idx >= 0 and chash and summary:
                result[idx] = (chash, summary)
        return result
    except (json.JSONDecodeError, KeyError, TypeError):
        return {}


def _save_cache(cache_dir: Path, notebook_path: Path, cells: list[CachedCell]) -> None:
    """Save cell summaries to disk.

    Creates cache_dir if it doesn't exist. Overwrites any existing cache file.
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    file_hash = _notebook_file_hash(notebook_path)
    cache_file = cache_dir / f"{notebook_path.stem}-{file_hash}.json"
    data = {
        "cells": [
            {"index": c.index, "content_hash": c.content_hash, "summary": c.summary}
            for c in cells
        ]
    }
    cache_file.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _extract_heading(source: str) -> tuple[int, str] | None:
    """Extract the highest-level heading from markdown source.

    Returns (level, text) or None if no heading found.
    """
    for line in source.split("\n"):
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            return (len(m.group(1)), m.group(2).strip())
    return None


def _group_sections(cells: list[dict]) -> list[dict]:
    """Group cells into sections based on markdown headings.

    A markdown cell with a heading starts a new section. Code cells and
    markdown cells without headings belong to the current section.

    Returns a list of sections, each with:
        - title: str (heading text)
        - level: int (heading level 1-6)
        - start_cell: int (first cell index in section)
        - end_cell: int (last cell index in section, inclusive)
        - cell_indices: list[int]
    """
    sections: list[dict] = []
    current: dict | None = None

    for cell_data in cells:
        idx = cell_data["index"]
        cell_type = cell_data["cell_type"]
        source = cell_data["source"]

        if cell_type == "markdown":
            heading = _extract_heading(source)
            if heading:
                # Flush previous section
                if current is not None:
                    sections.append(current)
                current = {
                    "title": heading[1],
                    "level": heading[0],
                    "start_cell": idx,
                    "end_cell": idx,
                    "cell_indices": [idx],
                }
                continue

        # Add to current section (or create an untitled one)
        if current is None:
            current = {
                "title": "Preamble",
                "level": 1,
                "start_cell": idx,
                "end_cell": idx,
                "cell_indices": [idx],
            }
        else:
            current["cell_indices"].append(idx)
            current["end_cell"] = idx

    if current is not None:
        sections.append(current)

    return sections


def _generate_section_summary(
    section: dict,
    cell_infos: list[CellVariableInfo],
    flow: dict,
) -> str:
    """Generate a rule-based summary for a notebook section.

    Summarizes what the section's code cells do by examining imports,
    function/class definitions, and key variable assignments.

    Args:
        section: Section dict from _group_sections.
        cell_infos: All cell variable info objects.
        flow: Cross-cell variable flow dict.

    Returns:
        1-2 sentence summary string.
    """
    parts: list[str] = []
    imports: list[str] = []
    functions: list[str] = []
    classes: list[str] = []
    key_vars: list[str] = []

    for idx in section["cell_indices"]:
        info = cell_infos[idx]
        if info.cell_type != "code":
            continue
        for stmt in info.statements:
            if stmt.statement_type == "import":
                imports.extend(stmt.defines)
            elif stmt.statement_type == "function_def":
                functions.extend(stmt.defines)
            elif stmt.statement_type == "class_def":
                classes.extend(stmt.defines)
            elif stmt.statement_type == "assign" and stmt.defines:
                # Only track variables that are referenced in other cells
                for var in stmt.defines:
                    if var in flow:
                        used_in_cells = flow[var].get("used_in", [])
                        if used_in_cells:
                            used_cells = {u["cell"] for u in used_in_cells}
                            if used_cells - {idx}:
                                key_vars.append(var)

    if imports:
        unique_imports = list(dict.fromkeys(imports))[:8]
        suffix = f" +{len(imports) - len(unique_imports)} more" if len(imports) > 8 else ""
        parts.append(f"imports {', '.join(unique_imports)}{suffix}")

    if functions:
        unique_funcs = list(dict.fromkeys(functions))[:6]
        suffix = f" +{len(functions) - len(unique_funcs)} more" if len(functions) > 6 else ""
        parts.append(f"defines functions: {', '.join(unique_funcs)}{suffix}")

    if classes:
        unique_classes = list(dict.fromkeys(classes))[:6]
        parts.append(f"defines classes: {', '.join(unique_classes)}")

    if key_vars:
        unique_vars = list(dict.fromkeys(key_vars))[:8]
        parts.append(f"produces key variables: {', '.join(unique_vars)}")

    if not parts:
        n_code = sum(1 for i in section["cell_indices"] if cell_infos[i].cell_type == "code")
        n_md = sum(1 for i in section["cell_indices"] if cell_infos[i].cell_type == "markdown")
        if n_code == 0:
            return f"Markdown section with {n_md} cell(s)."
        return f"Section with {n_code} code cell(s)."

    return ". ".join(parts) + "."


def _format_variable_flow_table(flow: dict) -> list[str]:
    """Format the Variable Flow summary table."""
    lines: list[str] = []
    lines.append("## Variable Flow")
    lines.append("")
    lines.append("| Variable | Defined (Cell, Line) | Used (Cells) |")
    lines.append("| -------- | -------------------- | ------------ |")

    for var_name, info in flow.items():
        defined_strs = []
        for d in info["defined_in"]:
            defined_strs.append(f"Cell {d['cell']}, L{d['line']}")

        # Deduplicate used-in cells
        used_cells = sorted(set(d["cell"] for d in info["used_in"]))
        used_strs = [f"Cell {c}" for c in used_cells]

        lines.append(f"| {var_name} | {', '.join(defined_strs)} | {', '.join(used_strs) or '—'} |")

    return lines


def _format_cell(
    index: int,
    cell_info: CellVariableInfo,
    variable_flow: dict,
    include_outputs: bool,
    outputs: list,
    include_code: bool = True,
    summary: str | None = None,
) -> list[str]:
    """Format a single cell's markdown output."""
    lines: list[str] = []

    if cell_info.cell_type == "markdown":
        lines.append(f"### Cell {index} [markdown]")
        lines.append("")
        # Render markdown cells as blockquotes
        for line in cell_info.source.split("\n"):
            lines.append(f"> {line}")
        lines.append("")
        return lines

    # Code cell
    lines.append(f"### Cell {index} [code]")
    lines.append("")

    # AI-generated summary blockquote
    if summary:
        lines.append(f"> *Summary: {summary}*")
        lines.append("")

    if include_code:
        lines.append("```python")
        lines.append(cell_info.source)
        lines.append("```")
    else:
        # Summary mode: show first line + line count
        source_lines = cell_info.source.strip().splitlines()
        if source_lines:
            first_line = source_lines[0][:80]
            lines.append(f"*{len(source_lines)} lines* — `{first_line}{'...' if len(source_lines[0]) > 80 else ''}`")
        else:
            lines.append("*(empty cell)*")

    # Per-statement annotations
    if cell_info.statements:
        lines.append("")
        # Build a map of where each variable was defined (from flow)
        var_defined_cell: dict[str, int] = {}
        for var_name, info in variable_flow.items():
            if info["defined_in"]:
                var_defined_cell[var_name] = info["defined_in"][0]["cell"]

        for stmt in cell_info.statements:
            if not stmt.defines and not stmt.references:
                continue

            parts: list[str] = []

            if stmt.defines:
                parts.append(f"L{stmt.line_number} defines: {', '.join(stmt.defines)}")
            else:
                parts.append(f"L{stmt.line_number}")

            if stmt.references:
                ref_parts: list[str] = []
                for ref in stmt.references:
                    if ref in var_defined_cell and var_defined_cell[ref] != cell_info.cell_index:
                        ref_parts.append(f"{ref} (defined cell {var_defined_cell[ref]})")
                    else:
                        ref_parts.append(ref)
                parts.append(f"references: {', '.join(ref_parts)}")

            lines.append(f"- **{' | '.join(parts)}**")

    # Cell outputs
    if include_outputs and outputs:
        lines.append("")
        lines.append("**Output:**")
        for output in outputs:
            output_type = output.get("output_type", "")
            if output_type == "stream":
                text = output.get("text", "")
                if isinstance(text, list):
                    text = "".join(text)
                lines.append("```")
                lines.append(text.rstrip())
                lines.append("```")
            elif output_type == "execute_result":
                data = output.get("data", {})
                text = data.get("text/plain", "")
                if isinstance(text, list):
                    text = "".join(text)
                lines.append("```")
                lines.append(text.rstrip())
                lines.append("```")
            elif output_type == "error":
                ename = output.get("ename", "Error")
                evalue = output.get("evalue", "")
                lines.append(f"[Error: {ename}: {evalue}]")
            elif output_type == "display_data":
                lines.append("[Display output]")

    lines.append("")
    return lines


def compact_notebook(
    filepath: str | Path,
    include_outputs: bool = False,
    include_code: bool = False,
    provider: SummarizerProvider | None = None,
    cache_dir: Path | None = None,
) -> str:
    """Compact a Jupyter notebook into layered markdown.

    Args:
        filepath: Path to the .ipynb file.
        include_outputs: If True, include cell outputs in the output (default: False).
        include_code: If True, include full source code. If False, show only
            first line + line count per cell (summary mode).
        provider: Optional SummarizerProvider for AI cell summaries.
        cache_dir: Optional directory for caching cell summaries.

    Returns:
        Compacted markdown string.
    """
    filepath = Path(filepath)
    nb = nbformat.read(str(filepath), as_version=4)

    # Extract variable info for each cell
    cell_infos: list[CellVariableInfo] = []
    for index, cell in enumerate(nb.cells):
        if cell.cell_type == "code":
            info = extract_cell_variables(cell.source, index)
        else:
            info = CellVariableInfo(
                cell_index=index,
                cell_type="markdown",
                source=cell.source,
            )
        cell_infos.append(info)

    # Build cross-cell flow
    flow = build_variable_flow(cell_infos)

    # Count cells by type
    code_cells = sum(1 for c in nb.cells if c.cell_type == "code")
    md_cells = len(nb.cells) - code_cells

    # Build cell data for section grouping
    cell_data_list: list[dict] = []
    for index, cell in enumerate(nb.cells):
        cell_data_list.append({
            "index": index,
            "cell_type": cell.cell_type,
            "source": cell.source if cell.cell_type == "markdown" else "",
        })

    # Group into sections
    sections = _group_sections(cell_data_list)

    # Load cache and summarize cells if provider is available
    cell_summaries: dict[int, str] = {}
    if provider is not None and cache_dir is not None:
        cached = _load_cache(cache_dir, filepath)
        cache_updates: list[CachedCell] = []

        for index, cell in enumerate(nb.cells):
            if cell.cell_type != "code":
                continue
            # Skip trivial cells (< 3 non-empty lines)
            non_empty_lines = [ln for ln in cell.source.splitlines() if ln.strip()]
            if len(non_empty_lines) < 3:
                continue

            # Use output-aware hash so cache invalidates when outputs change
            cell_outputs = cell.get("outputs", [])
            content_hash = _cell_content_hash_with_outputs(cell.source, cell_outputs)

            # Check cache
            if index in cached and cached[index][0] == content_hash:
                cell_summaries[index] = cached[index][1]
                cache_updates.append(CachedCell(index=index, content_hash=content_hash, summary=cached[index][1]))
                continue

            # Summarize via provider
            try:
                # Find section heading for this cell
                section_name = "Preamble"
                for sec in sections:
                    if index in sec["cell_indices"]:
                        section_name = sec["title"]
                        break
                context = (
                    f"Notebook: {filepath.name}\n"
                    f"Cell: {index} [code]\n"
                    f"Section: \"{section_name}\""
                )
                # Include truncated cell outputs in context so LLM can summarize
                # what the cell actually produced (respects context window limits)
                output_text = _format_outputs_for_context(cell_outputs, max_chars=1500)
                code_for_summary = cell.source
                if output_text:
                    code_for_summary = f"{cell.source}\n\n# Output:\n{output_text}"
                summary = provider.summarize(code_for_summary, context)
                if summary:
                    cell_summaries[index] = summary
                    cache_updates.append(CachedCell(index=index, content_hash=content_hash, summary=summary))
            except Exception:
                pass  # Fail open — no summary for this cell

        # Persist cache
        if cache_updates:
            _save_cache(cache_dir, filepath, cache_updates)

    # Build output
    lines: list[str] = []
    lines.append(f"# {filepath.name}")
    lines.append(f"*Notebook: {filepath.name} | {len(nb.cells)} cells ({code_cells} code, {md_cells} markdown)*")
    lines.append("")

    # Sections overview
    if sections:
        lines.append("## Sections")
        lines.append("")
        for sec in sections:
            n_cells = len(sec["cell_indices"])
            summary = _generate_section_summary(sec, cell_infos, flow)
            lines.append(f"- **{sec['title']}** (cells {sec['start_cell']}–{sec['end_cell']}, {n_cells} cells): {summary}")
        lines.append("")

    # Cells section
    lines.append("## Cells")
    lines.append("")

    for index, cell in enumerate(nb.cells):
        cell_info = cell_infos[index]
        outputs = cell.get("outputs", []) if cell.cell_type == "code" else []
        cell_lines = _format_cell(
            index, cell_info, flow, include_outputs, outputs,
            include_code=include_code,
            summary=cell_summaries.get(index),
        )
        lines.extend(cell_lines)

    # Variable Flow table
    if flow:
        lines.extend(_format_variable_flow_table(flow))
    else:
        lines.append("## Variable Flow")
        lines.append("")
        lines.append("*(no variable definitions found)*")

    return "\n".join(lines)
