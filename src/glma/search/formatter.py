"""Search result formatters for all output types.

Lean output design (per CONTEXT.md D-04/05/06):
- Markdown: file path heading + code blocks with summary annotations. No scores, no metadata.
- JSON: full metadata including scores, line ranges, chunk names.
- YAML: same structure as JSON.
- Markdown-KV: key-value style with score, type, lines.
"""

import json
from typing import Optional

from glma.search.engine import SearchResult


def _get_lang_hint(file_path: str) -> str:
    """Get language hint for markdown code block."""
    if file_path.endswith(".py"):
        return "python"
    elif file_path.endswith(".c") or file_path.endswith(".h"):
        return "c"
    return ""


def format_search_markdown(
    results: list[SearchResult],
    original_query: Optional[str] = None,
    rewritten_query: Optional[str] = None,
    graph_enabled: bool = False,
) -> str:
    """Format search results as lean markdown — file heading + code blocks + summary annotations.

    No scores, no line numbers, no chunk names in output.
    Consumers who need metadata use glma query <file> or JSON format.
    """
    lines: list[str] = []

    # Query header
    if original_query is not None:
        if rewritten_query is not None:
            lines.append(f'# Query: "{original_query}"')
            lines.append(f'# Rewritten: "{rewritten_query}"')
            lines.append("")
        else:
            lines.append(f'# Query: "{original_query}" (raw)')
            lines.append("")

    if not results:
        return "\n".join(lines)

    current_file = None

    for result in results:
        # File path heading (only when file changes)
        if result.file_path != current_file:
            if current_file is not None:
                lines.append("")  # blank line between files
            lines.append(f"# {result.file_path}")
            lines.append("")
            current_file = result.file_path

        # Code block with summary annotation
        lang = _get_lang_hint(result.file_path)
        lines.append(f"```{lang}")
        lines.append(result.content)
        lines.append("```")
        if result.summary:
            lines.append(f"> *Summary: {result.summary}*")
        if graph_enabled:
            lines.append(f"> *Scores: graph={result.graph_score:.2f}, keyword={result.keyword_score:.2f}, vector={result.vector_score:.2f}, combined={result.combined_score:.2f}*")
        lines.append("")

    return "\n".join(lines)


def format_search_kv(
    results: list[SearchResult],
    original_query: Optional[str] = None,
    rewritten_query: Optional[str] = None,
    graph_enabled: bool = False,
) -> str:
    """Format search results as key-value markdown."""
    lines: list[str] = []

    # Query header
    if original_query is not None:
        if rewritten_query is not None:
            lines.append(f'# Query: "{original_query}"')
            lines.append(f'# Rewritten: "{rewritten_query}"')
            lines.append("")
        else:
            lines.append(f'# Query: "{original_query}" (raw)')
            lines.append("")

    if not results:
        return "\n".join(lines)

    current_file = None

    for result in results:
        if result.file_path != current_file:
            if current_file is not None:
                lines.append("")
            lines.append(f"# {result.file_path}")
            lines.append("")
            current_file = result.file_path

        lines.append(f"## {result.chunk_name}")
        lines.append("")
        lines.append(f"type: {result.chunk_type}")
        lines.append(f"lines: L{result.start_line}-L{result.end_line}")
        lines.append(f"score: {result.combined_score:.3f}")
        if graph_enabled:
            lines.append(f"graph_score: {result.graph_score:.3f}")
            lines.append(f"keyword_score: {result.keyword_score:.3f}")
            lines.append(f"vector_score: {result.vector_score:.3f}")
        if result.summary:
            lines.append(f"summary: {result.summary}")
        lang = _get_lang_hint(result.file_path)
        lines.append("")
        lines.append(f"```{lang}")
        lines.append(result.content)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def format_search_json(
    results: list[SearchResult],
    query: str,
    search_mode: str,
    original_query: Optional[str] = None,
    rewritten_query: Optional[str] = None,
    graph_enabled: bool = False,
) -> str:
    """Format search results as JSON with full metadata."""
    data = {
        "original_query": original_query if original_query is not None else query,
        "rewritten_query": rewritten_query,
        "query": query,
        "search_mode": search_mode,
        "total_results": len(results),
        "results": [
            {
                "file_path": r.file_path,
                "chunk_name": r.chunk_name,
                "chunk_type": r.chunk_type,
                "start_line": r.start_line,
                "end_line": r.end_line,
                "summary": r.summary,
                "content": r.content,
                "scores": {
                    "keyword": round(r.keyword_score, 4),
                    "vector": round(r.vector_score, 4),
                    **({"graph": round(r.graph_score, 4)} if graph_enabled else {}),
                    "combined": round(r.combined_score, 4),
                },
            }
            for r in results
        ],
    }
    return json.dumps(data, indent=2)


def format_search_yaml(
    results: list[SearchResult],
    query: str,
    search_mode: str,
    original_query: Optional[str] = None,
    rewritten_query: Optional[str] = None,
    graph_enabled: bool = False,
) -> str:
    """Format search results as YAML with full metadata."""
    import yaml
    data = {
        "original_query": original_query if original_query is not None else query,
        "rewritten_query": rewritten_query,
        "query": query,
        "search_mode": search_mode,
        "total_results": len(results),
        "results": [
            {
                "file_path": r.file_path,
                "chunk_name": r.chunk_name,
                "chunk_type": r.chunk_type,
                "start_line": r.start_line,
                "end_line": r.end_line,
                "summary": r.summary,
                "content": r.content,
                "scores": {
                    "keyword": round(r.keyword_score, 4),
                    "vector": round(r.vector_score, 4),
                    **({"graph": round(r.graph_score, 4)} if graph_enabled else {}),
                    "combined": round(r.combined_score, 4),
                },
            }
            for r in results
        ],
    }
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def format_search_output(
    results: list[SearchResult],
    output_format: str,
    query: str,
    search_mode: str,
    original_query: Optional[str] = None,
    rewritten_query: Optional[str] = None,
    graph_enabled: bool = False,
) -> str:
    """Dispatch to the appropriate formatter based on output format string.

    Args:
        results: Search results to format.
        output_format: One of 'markdown', 'markdown-kv', 'json', 'yaml'.
        query: Search query used (for JSON/YAML metadata).
        search_mode: Search mode used (for JSON/YAML metadata).
        original_query: Original user query before rewriting.
        rewritten_query: LLM-rewritten query (None if raw mode).

    Returns:
        Formatted string.
    """
    if output_format == "json":
        return format_search_json(results, query, search_mode, original_query=original_query, rewritten_query=rewritten_query, graph_enabled=graph_enabled)
    elif output_format == "yaml":
        return format_search_yaml(results, query, search_mode, original_query=original_query, rewritten_query=rewritten_query, graph_enabled=graph_enabled)
    elif output_format == "markdown-kv":
        return format_search_kv(results, original_query=original_query, rewritten_query=rewritten_query, graph_enabled=graph_enabled)
    else:  # markdown (default)
        return format_search_markdown(results, original_query=original_query, rewritten_query=rewritten_query, graph_enabled=graph_enabled)
