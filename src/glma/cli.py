"""CLI interface for glma."""

import asyncio
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from glma import __version__

app = typer.Typer(
    name="glma",
    help="Index codebases into a queryable graph database with companion markdown output.",
    no_args_is_help=True,
)
console = Console()


def version_callback(value: bool) -> None:
    if value:
        console.print(f"glma {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None, "--version", "-v", help="Show version.", callback=version_callback, is_eager=True,
    ),
) -> None:
    """glma - Codebase indexing tool."""
    pass


@app.command()
def index(
    path: Optional[Path] = typer.Argument(
        None,
        help="Path to repository to index. Defaults to current directory.",
    ),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress progress output."),
    config_file: Optional[Path] = typer.Option(None, "--config", help="Path to .glma.toml config file."),
    languages: Optional[list[str]] = typer.Option(None, "--lang", help="Languages to index (c, python)."),
    output_dir: Optional[str] = typer.Option(None, "--output", "-o", help="Output directory for index."),
    summarize: bool = typer.Option(
        False,
        "--summarize",
        help="Run AI summarization pass after indexing to generate per-chunk summaries.",
    ),
    summarize_provider: Optional[str] = typer.Option(
        None,
        "--summarize-provider",
        help="Summarization provider: 'local' (OpenAI-compatible) or 'pi'.",
    ),
    summarize_model: Optional[str] = typer.Option(
        None,
        "--summarize-model",
        help="Model name for summarization (e.g., 'llama3', 'codellama').",
    ),
) -> None:
    """Index a repository's source files into the glma database."""
    from glma.config import load_config
    from glma.models import Language

    repo_path = path.resolve() if path else Path.cwd()

    # Build CLI overrides
    cli_overrides: dict = {}
    if quiet:
        cli_overrides["quiet"] = True
    if languages:
        cli_overrides["languages"] = [Language(lang) for lang in languages]
    if output_dir:
        cli_overrides["output_dir"] = output_dir

    # Load config (file + CLI overrides)
    cfg = load_config(repo_path, cli_overrides)

    if not cfg.quiet:
        console.print(f"[bold]glma[/bold] indexing [cyan]{repo_path}[/cyan]")
        console.print(f"  Languages: {', '.join(l.value for l in cfg.languages)}")
        console.print(f"  Output: {cfg.output_dir}")

    # Run the indexing pipeline
    from glma.index.pipeline import run_index
    from glma.index.progress import IndexProgress

    progress = IndexProgress(quiet=cfg.quiet, console=console)
    result = run_index(repo_path, cfg, progress=progress)

    if result.total_files == 0:
        console.print("[yellow]No supported source files found.[/yellow]")
        raise typer.Exit(1)

    # Summarization pass (after indexing)
    if summarize:
        from glma.config import load_summarize_config
        from glma.summarize import summarize_chunks
        from glma.summarize.providers import OpenAICompatibleProvider, PiProvider
        from glma.db.ladybug_store import LadybugStore

        # Build summarize CLI overrides
        summarize_overrides = {"enabled": True}
        if summarize_provider:
            summarize_overrides["provider"] = summarize_provider
        if summarize_model:
            summarize_overrides["model"] = summarize_model

        summ_cfg = load_summarize_config(repo_path, summarize_overrides)

        # Instantiate provider
        try:
            if summ_cfg.provider.value == "pi":
                provider = PiProvider(model=summ_cfg.model)
            else:
                provider = OpenAICompatibleProvider(
                    base_url=summ_cfg.base_url,
                    model=summ_cfg.model,
                )
        except ImportError as e:
            console.print(f"[red]Error:[/red] {e}")
            raise typer.Exit(1)

        # Load all chunks from DB for summarization
        db_path_summ = repo_path / cfg.output_dir / "db" / "index.lbug"
        store = LadybugStore(db_path_summ)
        indexed_files = store.get_indexed_files()

        if not cfg.quiet:
            console.print(f"[bold]Summarizing[/bold] chunks with {summ_cfg.provider.value} provider...")

        for file_path in sorted(indexed_files.keys()):
            chunks = store.get_chunks_for_file(file_path)
            if chunks:
                summarize_chunks(store, chunks, provider)

        # Regenerate static markdown files with AI summaries
        from glma.index.writer import write_markdown

        for file_path in sorted(indexed_files.keys()):
            chunks = store.get_chunks_for_file(file_path)
            if chunks:
                file_rels = store.get_file_relationships(file_path)
                write_markdown(chunks, repo_path, cfg.output_dir, relationships=file_rels)

        if not cfg.quiet:
            console.print(f"[green]✓[/green] Summarization complete: {len(indexed_files)} files processed")


def _write_output(text: str, output_path: Optional[str]) -> None:
    """Write output to file or stdout."""
    if output_path:
        Path(output_path).write_text(text, encoding="utf-8")
    else:
        console.print(text, highlight=False, soft_wrap=True, markup=False)


def _group_rels_by_chunk(rels: list[dict], chunk_ids: list[str]) -> dict:
    """Group flat relationship list by chunk_id.

    Returns dict keyed by chunk_id with 'outgoing' and 'incoming' lists.
    """
    result: dict[str, dict] = {cid: {"outgoing": [], "incoming": []} for cid in chunk_ids}
    for rel in rels:
        if rel.get("direction") == "incoming":
            target_id = rel.get("target_id", "")
            if target_id in result:
                result[target_id]["incoming"].append(rel)
        else:
            source_id = rel.get("source_id", "")
            if source_id in result:
                result[source_id]["outgoing"].append(rel)
    return result


@app.command()
def query(
    filepath: str = typer.Argument(..., help="Path to file to query (relative to repo root)."),
    verbose: bool = typer.Option(False, "--verbose", "-V", help="Include full code bodies."),
    depth: int = typer.Option(1, "--depth", "-d", help="Relationship traversal depth (1-10)."),
    no_relationships: bool = typer.Option(False, "--no-relationships", help="Skip dependency section."),
    output_format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown, json."),
    rel_types: Optional[str] = typer.Option(None, "--rel-types", help="Comma-separated relationship types to show."),
    summary_only: bool = typer.Option(False, "--summary-only", help="Show only file summary."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (default: stdout)."),
    repo_root: Optional[Path] = typer.Option(None, "--repo", "-r", help="Repo root directory (auto-detected)."),
    include_outputs: bool = typer.Option(False, "--include-outputs", help="Include notebook cell outputs (default: off)."),
    include_code: bool = typer.Option(False, "--include-code", help="Include full source code in notebook output (default: summary only)."),
    summarize: bool = typer.Option(
        False,
        "--summarize",
        help="Generate per-cell AI summaries for notebook queries.",
    ),
    summarize_provider: Optional[str] = typer.Option(
        None,
        "--summarize-provider",
        help="Summarization provider: 'local' (OpenAI-compatible) or 'pi'.",
    ),
    summarize_model: Optional[str] = typer.Option(
        None,
        "--summarize-model",
        help="Model name for summarization (e.g., 'llama3', 'codellama').",
    ),
) -> None:
    """Query an indexed file and output compacted markdown."""
    # Validate flags
    if output_format not in ("markdown", "json"):
        sys.stderr.write("Error: format must be 'markdown' or 'json'\n")
        raise typer.Exit(4)
    if depth < 1 or depth > 10:
        sys.stderr.write("Error: depth must be between 1 and 10\n")
        raise typer.Exit(4)

    # Resolve repo root
    if repo_root:
        repo_root_path = repo_root.resolve()
    else:
        # Walk up from CWD looking for .glma-index/ or .glma.toml
        repo_root_path = Path.cwd()
        found = False
        for parent in [repo_root_path] + list(repo_root_path.parents):
            if (parent / ".glma-index").is_dir() or (parent / ".glma.toml").is_file():
                repo_root_path = parent
                found = True
                break
        if not found:
            sys.stderr.write("Error: Not inside an indexed repository. Use --repo to specify root.\n")
            raise typer.Exit(4)

    # Notebook dispatch: bypass LadybugStore entirely
    if filepath.endswith('.ipynb'):
        disk_path = repo_root_path / filepath
        if not disk_path.exists():
            sys.stderr.write(f"Error: File not found: {filepath}\n")
            raise typer.Exit(1)

        # Summarization setup for notebooks
        nb_provider = None
        nb_cache_dir = None
        if summarize:
            from glma.config import load_summarize_config
            from glma.summarize.providers import OpenAICompatibleProvider, PiProvider

            summarize_overrides = {"enabled": True}
            if summarize_provider:
                summarize_overrides["provider"] = summarize_provider
            if summarize_model:
                summarize_overrides["model"] = summarize_model

            summ_cfg = load_summarize_config(repo_root_path, summarize_overrides)

            try:
                if summ_cfg.provider.value == "pi":
                    nb_provider = PiProvider(model=summ_cfg.model)
                else:
                    nb_provider = OpenAICompatibleProvider(
                        base_url=summ_cfg.base_url,
                        model=summ_cfg.model,
                    )
            except ImportError as e:
                console.print(f"[red]Error:[/red] {e}")
                raise typer.Exit(1)

            nb_cache_dir = repo_root_path / ".glma-index" / "notebook-cache"

        from glma.query.notebook import compact_notebook
        result_text = compact_notebook(
            disk_path,
            include_outputs=include_outputs,
            include_code=include_code,
            provider=nb_provider,
            cache_dir=nb_cache_dir,
        )
        _write_output(result_text, output)
        return

    # Locate index database
    db_path = repo_root_path / ".glma-index" / "db" / "index.lbug"
    if not db_path.exists():
        sys.stderr.write("Error: No index found. Run `glma index` first.\n")
        raise typer.Exit(4)

    # Check file exists on disk
    disk_path = repo_root_path / filepath
    if not disk_path.exists():
        sys.stderr.write(f"Error: File not found: {filepath}\n")
        raise typer.Exit(1)

    # Look up file in index
    from glma.db.ladybug_store import LadybugStore
    store = LadybugStore(db_path)
    file_record = store.get_file_record(filepath)
    if file_record is None:
        sys.stderr.write(f"Error: File not indexed: {filepath}\n")
        raise typer.Exit(2)

    # Stale index check
    from glma.index.pipeline import file_content_hash
    current_hash = file_content_hash(disk_path)
    stale = current_hash != file_record.content_hash
    if stale:
        sys.stderr.write("Warning: File has been modified since last index. Results may be stale.\n")

    # Build QueryConfig
    from glma.models import QueryConfig
    cfg = QueryConfig(
        verbose=verbose,
        depth=min(depth, 10),
        no_relationships=no_relationships,
        output_format=output_format,
        rel_types=rel_types.split(",") if rel_types else [],
        summary_only=summary_only,
    )

    # Load data
    chunks = store.get_chunks_for_file(filepath)
    chunk_ids = [c.id for c in chunks]

    # Relationship loading
    if cfg.depth > 1:
        all_rels_flat = store.traverse_relationships(chunk_ids, max_depth=cfg.depth)
        relationships = _group_rels_by_chunk(all_rels_flat, chunk_ids)
    else:
        all_rels_flat = store.get_file_relationships(filepath)
        relationships = store.get_all_relationships_for_file(filepath)
        # Build a flat list from the grouped dict for JSON output
        flat_rels: list[dict] = []
        for cid, rels in relationships.items():
            flat_rels.extend(rels.get("outgoing", []))
            flat_rels.extend(rels.get("incoming", []))
        all_rels_flat = flat_rels

    # Format output
    if cfg.output_format == "json":
        from glma.query.formatter import format_json_output
        output_text = format_json_output(filepath, file_record, chunks, all_rels_flat, verbose=cfg.verbose)
    else:
        from glma.query.formatter import format_compact_output
        output_text = format_compact_output(filepath, file_record, chunks, relationships, query_config=cfg)

    _write_output(output_text, output)

    if stale:
        raise typer.Exit(3)


@app.command()
def watch(
    path: Optional[Path] = typer.Argument(
        None,
        help="Path to repository to watch. Defaults to current directory.",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-V", help="Log every file event."),
    config_file: Optional[Path] = typer.Option(None, "--config", help="Path to .glma.toml config file."),
    debounce: Optional[float] = typer.Option(None, "--debounce", help="Batch window in seconds."),
) -> None:
    """Watch for file changes and incrementally re-index."""
    from glma.config import load_config, load_watch_config

    repo_path = path.resolve() if path else Path.cwd()

    # Validate repo has been indexed
    index_config = load_config(repo_path)
    db_path = repo_path / index_config.output_dir / "db" / "index.lbug"
    if not db_path.exists():
        console.print("[red]Error: No index found. Run `glma index` first.[/red]")
        raise typer.Exit(4)

    # Build watch CLI overrides
    watch_overrides: dict = {}
    if verbose:
        watch_overrides["verbose"] = True
    if debounce is not None:
        watch_overrides["debounce_seconds"] = debounce

    watch_config = load_watch_config(repo_path, watch_overrides)

    # Run the async watcher
    from glma.watch import watch_and_index
    asyncio.run(watch_and_index(repo_path, index_config, watch_config, console=console))


@app.command()
def export(
    path: Optional[Path] = typer.Argument(
        None,
        help="Path to indexed repository. Defaults to current directory.",
    ),
    output: str = typer.Option(
        ".",
        "--output",
        "-o",
        help="Output path: directory, .tar.gz archive, or '-' for stdout pipe.",
    ),
    ai_summaries: bool = typer.Option(
        False,
        "--ai-summaries",
        help="Include AI-generated chunk summaries from the index in export output.",
    ),
    include_code: bool = typer.Option(
        False,
        "--include-code",
        help="Include full source code in export (default: signatures only).",
    ),
    config_file: Optional[Path] = typer.Option(
        None,
        "--config",
        help="Path to .glma.toml config file.",
    ),
) -> None:
    """Export the full index as static markdown for air-gapped consumption."""
    from glma.config import load_config, load_export_config

    repo_path = path.resolve() if path else Path.cwd()

    # Validate repo has been indexed
    index_config = load_config(repo_path)
    db_path = repo_path / index_config.output_dir / "db" / "index.lbug"
    if not db_path.exists():
        console.print("[red]Error: No index found. Run `glma index` first.[/red]")
        raise typer.Exit(4)

    # Build export CLI overrides
    export_overrides: dict = {}
    export_overrides["output_path"] = output if output != "." else None
    if ai_summaries:
        export_overrides["ai_summaries"] = True
    if include_code:
        export_overrides["include_code"] = True

    export_config = load_export_config(repo_path, export_overrides)

    # Run export
    from glma.db.ladybug_store import LadybugStore
    from glma.export import export_index

    store = LadybugStore(db_path)
    export_index(repo_path, export_config, store, console=console)
