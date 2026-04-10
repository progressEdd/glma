"""Jupyter notebook compaction to compacted markdown.

Parses .ipynb files with nbformat, extracts per-statement variable definitions/references,
tracks cross-cell variable flow, and generates compacted markdown output.
"""

from pathlib import Path
from typing import Optional

import nbformat

from glma.query.variables import CellVariableInfo, extract_cell_variables, build_variable_flow


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


def compact_notebook(filepath: str | Path, include_outputs: bool = False, include_code: bool = True) -> str:
    """Compact a Jupyter notebook into layered markdown.

    Args:
        filepath: Path to the .ipynb file.
        include_outputs: If True, include cell outputs in the output.
        include_code: If True, include full source code. If False, show only
            first line + line count per cell (summary mode).

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

    # Build output
    lines: list[str] = []
    lines.append(f"# {filepath.name}")
    lines.append(f"*Notebook: {filepath.name} | {len(nb.cells)} cells ({code_cells} code, {md_cells} markdown)*")
    lines.append("")

    # Cells section
    lines.append("## Cells")
    lines.append("")

    for index, cell in enumerate(nb.cells):
        cell_info = cell_infos[index]
        outputs = cell.get("outputs", []) if cell.cell_type == "code" else []
        cell_lines = _format_cell(index, cell_info, flow, include_outputs, outputs, include_code=include_code)
        lines.extend(cell_lines)

    # Variable Flow table
    if flow:
        lines.extend(_format_variable_flow_table(flow))
    else:
        lines.append("## Variable Flow")
        lines.append("")
        lines.append("*(no variable definitions found)*")

    return "\n".join(lines)
