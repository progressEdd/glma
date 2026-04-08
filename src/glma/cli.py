"""CLI interface for glma."""

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
