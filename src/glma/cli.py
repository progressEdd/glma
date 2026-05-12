"""CLI interface for glma."""

import asyncio
import signal
import sys
import threading
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
        help="Summarization provider: preset name (ollama, lmstudio, llamacpp, vllm, aphrodite, local, pi) or leave unset for auto-detect.",
    ),
    summarize_model: Optional[str] = typer.Option(
        None,
        "--summarize-model",
        help="Model name for summarization (e.g., 'llama3', 'codellama').",
    ),
    ai_url: Optional[str] = typer.Option(
        None,
        "--ai-url",
        help="Override API base URL for the summarization provider.",
    ),
    max_chunk_chars: Optional[int] = typer.Option(
        None,
        "--max-chunk-chars",
        help="Max chars per chunk for summarization (default: 3000). Triggers decomposition if exceeded.",
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

    # Signal handling for graceful shutdown
    shutdown_event = threading.Event()

    def _handle_signal(signum, frame):
        if shutdown_event.is_set():
            # Second signal — force exit
            console.print("[red]Force exit.[/red]")
            raise typer.Exit(1)
        shutdown_event.set()
        console.print("[yellow]Interrupt received. Finishing current file...[/yellow]")

    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    progress = IndexProgress(quiet=cfg.quiet, console=console)
    result = run_index(repo_path, cfg, progress=progress, shutdown_event=shutdown_event)

    if result.total_files == 0:
        console.print("[yellow]No supported source files found.[/yellow]")
        raise typer.Exit(1)

    # If interrupted during indexing, skip summarization
    if shutdown_event.is_set():
        console.print("[yellow]Indexing interrupted. Skipping summarization. Run 'glma index' to resume.[/yellow]")
        raise typer.Exit(0)

    # Summarization pass (after indexing)
    if summarize:
        from glma.config import load_summarize_config
        from glma.summarize import summarize_chunks
        from glma.summarize.providers import OpenAICompatibleProvider
        from glma.db.ladybug_store import LadybugStore

        # Build summarize CLI overrides
        summarize_overrides = {"enabled": True}
        if summarize_provider:
            summarize_overrides["provider"] = summarize_provider
        if summarize_model:
            summarize_overrides["model"] = summarize_model
        if ai_url:
            summarize_overrides["base_url"] = ai_url
        if max_chunk_chars is not None:
            summarize_overrides["max_chunk_chars"] = max_chunk_chars

        summ_cfg = load_summarize_config(repo_path, summarize_overrides)

        # Instantiate provider
        try:
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
                summarize_chunks(store, chunks, provider, max_chunk_chars=summ_cfg.max_chunk_chars)

        # Generate file-level LLM summaries from chunk summaries
        if not cfg.quiet:
            console.print("[dim]Generating file-level summaries...[/dim]")

        for file_path in sorted(indexed_files.keys()):
            record = store.get_file_record(file_path)
            if record and record.file_summary:
                continue  # Already have a file summary
            chunks = store.get_chunks_for_file(file_path)
            chunk_summaries = [c.summary for c in chunks if c.summary]
            if not chunk_summaries:
                continue
            try:
                context = f"File: {file_path}"
                chunk_text = "\n".join(f"- {s}" for s in chunk_summaries)
                prompt = (
                    f"Based on these per-function/class summaries, write a single 1-2 sentence summary of what this file does as a whole.\n"
                    f"\n{chunk_text}"
                )
                file_summary = provider.summarize(prompt, context)
                if file_summary:
                    store.update_file_summary(file_path, file_summary)
            except Exception:
                pass  # Fail open

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
    output_format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown-kv, markdown, json, yaml."),
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
        help="Summarization provider: preset name (ollama, lmstudio, llamacpp, vllm, aphrodite, local, pi) or leave unset for auto-detect.",
    ),
    summarize_model: Optional[str] = typer.Option(
        None,
        "--summarize-model",
        help="Model name for summarization (e.g., 'llama3', 'codellama').",
    ),
) -> None:
    """Query an indexed file and output compacted markdown."""
    # Validate flags
    from glma.models import ExportFormat
    try:
        fmt = ExportFormat(output_format)
    except ValueError:
        valid = ", ".join(f.value for f in ExportFormat)
        sys.stderr.write(f"Error: format must be one of: {valid}\n")
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
            from glma.summarize.providers import OpenAICompatibleProvider

            summarize_overrides = {"enabled": True}
            if summarize_provider:
                summarize_overrides["provider"] = summarize_provider
            if summarize_model:
                summarize_overrides["model"] = summarize_model

            summ_cfg = load_summarize_config(repo_root_path, summarize_overrides)

            try:
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
    format: str = typer.Option(
        "markdown-kv",
        "--format",
        "-f",
        help="Export format: markdown-kv, markdown, json, yaml.",
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

    # Validate and set format
    from glma.models import ExportFormat
    try:
        export_format = ExportFormat(format)
    except ValueError:
        valid = ", ".join(f.value for f in ExportFormat)
        console.print(f"[red]Error:[/red] Invalid format '{format}'. Must be one of: {valid}")
        raise typer.Exit(4)
    export_overrides["format"] = export_format

    export_config = load_export_config(repo_path, export_overrides)

    # Run export
    from glma.db.ladybug_store import LadybugStore
    from glma.export import export_index

    store = LadybugStore(db_path)
    export_index(repo_path, export_config, store, console=console)


@app.command()
def embed(
    path: Optional[Path] = typer.Argument(
        None,
        help="Path to indexed repository. Defaults to current directory.",
    ),
    embedding_provider: Optional[str] = typer.Option(
        None,
        "--embedding-provider",
        help="Embedding provider preset name (e.g., embed-ollama, embed-lmstudio).",
    ),
    embedding_model: Optional[str] = typer.Option(
        None,
        "--embedding-model",
        help="Model name for embeddings (overrides config).",
    ),
    embedding_base_url: Optional[str] = typer.Option(
        None,
        "--embedding-base-url",
        help="API base URL for embedding provider (overrides config).",
    ),
    vector_dimensions: Optional[int] = typer.Option(
        None,
        "--vector-dimensions",
        help="Embedding vector dimensions (must match model output).",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Re-embed chunks even if summary hash matches (still skips chunks without summaries).",
    ),
    quiet: bool = typer.Option(
        False,
        "--quiet",
        "-q",
        help="Suppress progress output.",
    ),
) -> None:
    """Generate embedding vectors for chunk summaries and store in the index."""
    from glma.config import load_config, load_search_config
    from glma.db.ladybug_store import LadybugStore
    from glma.embedding.pipeline import embed_chunks
    from glma.embedding.providers import OpenAIEmbeddingProvider

    repo_path = path.resolve() if path else Path.cwd()

    # Validate index exists
    index_config = load_config(repo_path)
    db_path = repo_path / index_config.output_dir / "db" / "index.lbug"
    if not db_path.exists():
        console.print("[red]Error:[/red] No index found. Run `glma index` first.")
        raise typer.Exit(4)

    # Build search CLI overrides
    search_overrides: dict = {}
    if embedding_provider:
        search_overrides["embedding_provider"] = embedding_provider
    if embedding_model:
        search_overrides["embedding_model"] = embedding_model
    if embedding_base_url:
        search_overrides["embedding_base_url"] = embedding_base_url
    if vector_dimensions is not None:
        search_overrides["vector_dimensions"] = vector_dimensions

    # Load search config (file + CLI overrides)
    search_cfg = load_search_config(repo_path, search_overrides)

    # Instantiate embedding provider
    try:
        provider = OpenAIEmbeddingProvider(
            base_url=search_cfg.embedding_base_url,
            model=search_cfg.embedding_model,
        )
    except ImportError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1)

    if not quiet:
        console.print(f"[bold]glma embed[/bold] with {search_cfg.embedding_provider} ({search_cfg.embedding_model})")
        console.print(f"  Dimensions: {search_cfg.vector_dimensions}")

    # Open database and run embedding pipeline
    store = LadybugStore(db_path, vector_dimensions=search_cfg.vector_dimensions)

    # Rich progress display
    from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

    progress_obj = None
    task_id = None

    def on_batch_progress(batch_num, total_batches, embedded, skipped, failed):
        nonlocal task_id
        if progress_obj and task_id is not None:
            progress_obj.update(task_id, completed=batch_num, description=f"Embedding batch {batch_num}/{total_batches}")

    if not quiet:
        # We don't know total batches upfront, so show a simple spinner + counter
        progress_obj = Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            TimeElapsedColumn(),
            console=console,
        )
        progress_obj.start()
        task_id = progress_obj.add_task("Embedding chunks...", total=None)

    try:
        result = embed_chunks(
            store=store,
            provider=provider,
            config=search_cfg,
            force=force,
            progress_callback=on_batch_progress if not quiet else None,
        )
    except Exception as e:
        if progress_obj:
            progress_obj.stop()
        console.print(f"[red]Error:[/red] Embedding failed: {e}")
        raise typer.Exit(1)
    finally:
        if progress_obj:
            progress_obj.stop()

    # Print summary
    if not quiet:
        console.print()
        console.print(f"  Embedded:  {result.embedded}")
        console.print(f"  Skipped:   {result.skipped}")
        console.print(f"  Failed:    {result.failed}")
        if result.failed_chunk_ids:
            console.print(f"  Failed chunks:")
            for cid in result.failed_chunk_ids[:10]:
                console.print(f"    {cid}")
            if len(result.failed_chunk_ids) > 10:
                console.print(f"    ... and {len(result.failed_chunk_ids) - 10} more")

    # Exit code: 0 if all embedded (or nothing to do), 1 if any failures
    if result.failed > 0:
        raise typer.Exit(1)


@app.command()
def search(
    query_text: str = typer.Argument(..., help="Natural language search query."),
    search_mode: str = typer.Option("hybrid", "--search-mode", help="Search strategy: hybrid, vector, keyword."),
    output_format: str = typer.Option("markdown", "--format", "-f", help="Output format: markdown, markdown-kv, json, yaml."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (default: stdout)."),
    repo_root: Optional[Path] = typer.Option(None, "--repo", "-r", help="Repo root directory (auto-detected)."),
    embedding_provider: Optional[str] = typer.Option(None, "--embedding-provider", help="Embedding provider preset name."),
    embedding_model: Optional[str] = typer.Option(None, "--embedding-model", help="Model name for embeddings."),
    embedding_base_url: Optional[str] = typer.Option(None, "--embedding-base-url", help="API base URL for embedding provider."),
    vector_dimensions: Optional[int] = typer.Option(None, "--vector-dimensions", help="Embedding vector dimensions."),
    similarity_threshold: Optional[float] = typer.Option(None, "--similarity-threshold", help="Minimum similarity score for results (0.0-1.0)."),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress progress output."),
) -> None:
    """Search indexed code using hybrid keyword + vector similarity."""
    from glma.models import ExportFormat

    # Validate search mode
    valid_modes = {"hybrid", "vector", "keyword"}
    if search_mode not in valid_modes:
        sys.stderr.write(f"Error: search-mode must be one of: {', '.join(sorted(valid_modes))}\n")
        raise typer.Exit(4)

    # Validate format
    try:
        fmt = ExportFormat(output_format)
    except ValueError:
        valid = ", ".join(f.value for f in ExportFormat)
        sys.stderr.write(f"Error: format must be one of: {valid}\n")
        raise typer.Exit(4)

    # Resolve repo root
    if repo_root:
        repo_root_path = repo_root.resolve()
    else:
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

    # Validate index exists
    db_path = repo_root_path / ".glma-index" / "db" / "index.lbug"
    if not db_path.exists():
        sys.stderr.write("No index found. Run `glma index` first.\n")
        raise typer.Exit(4)

    # Build search CLI overrides
    from glma.config import load_search_config
    search_overrides: dict = {}
    if embedding_provider:
        search_overrides["embedding_provider"] = embedding_provider
    if embedding_model:
        search_overrides["embedding_model"] = embedding_model
    if embedding_base_url:
        search_overrides["embedding_base_url"] = embedding_base_url
    if vector_dimensions is not None:
        search_overrides["vector_dimensions"] = vector_dimensions
    if similarity_threshold is not None:
        search_overrides["similarity_threshold"] = similarity_threshold

    # Load search config
    search_cfg = load_search_config(repo_root_path, search_overrides)

    # Instantiate embedding provider
    from glma.embedding.providers import OpenAIEmbeddingProvider
    try:
        provider = OpenAIEmbeddingProvider(
            base_url=search_cfg.embedding_base_url,
            model=search_cfg.embedding_model,
        )
    except ImportError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1)

    # Open database and run search
    from glma.db.ladybug_store import LadybugStore
    from glma.search.engine import HybridSearchEngine
    from glma.search.formatter import format_search_output

    store = LadybugStore(db_path, vector_dimensions=search_cfg.vector_dimensions)
    engine = HybridSearchEngine(store, provider, search_cfg)

    try:
        results = engine.search(query_text, mode=search_mode)
    except ValueError as e:
        sys.stderr.write(f"{e}\n")
        raise typer.Exit(1)

    # Handle empty results
    if not results:
        sys.stderr.write(f"No results above threshold {search_cfg.similarity_threshold}. Try lowering --similarity-threshold.\n")
        raise typer.Exit(0)

    # Format and output
    formatted = format_search_output(results, output_format, query_text, search_mode)
    _write_output(formatted, output)

    if not quiet:
        sys.stderr.write(f"Found {len(results)} results\n")
