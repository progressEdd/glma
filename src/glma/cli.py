"""CLI interface for glma."""

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


def _write_output(text: str, output_path: Optional[str]) -> None:
    """Write output to file or stdout."""
    if output_path:
        Path(output_path).write_text(text, encoding="utf-8")
    else:
        console.print(text, highlight=False, soft_wrap=True)


@app.command()
def query(
    filepath: str = typer.Argument(..., help="Path to file to query (relative to repo root)."),
    verbose: bool = typer.Option(False, "--verbose", "-V", help="Include full code bodies."),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path (default: stdout)."),
    repo_root: Optional[Path] = typer.Option(None, "--repo", "-r", help="Repo root directory (auto-detected)."),
) -> None:
    """Query an indexed file and output compacted markdown."""
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

    # Load data and format
    chunks = store.get_chunks_for_file(filepath)
    relationships = store.get_all_relationships_for_file(filepath)
    from glma.query.formatter import format_compact_output
    output_text = format_compact_output(filepath, file_record, chunks, relationships, verbose=verbose)

    _write_output(output_text, output)

    if stale:
        raise typer.Exit(3)
