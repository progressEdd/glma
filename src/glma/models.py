"""Data models for glma indexing."""

from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class ChunkType(str, Enum):
    """Types of code chunks extracted from source files."""
    FUNCTION = "function"
    CLASS = "class"
    METHOD = "method"
    MODULE = "module"


class Language(str, Enum):
    """Supported programming languages."""
    C = "c"
    PYTHON = "python"


class Chunk(BaseModel):
    """A semantic code chunk extracted from a source file."""
    id: str = Field(..., description="Unique identifier: {file_path}::{chunk_type}::{name}::{start_line}")
    file_path: str = Field(..., description="Relative path from repo root")
    chunk_type: ChunkType
    name: str = Field(..., description="Name of the function, class, or method")
    content: str = Field(..., description="Raw source code of the chunk")
    summary: Optional[str] = Field(None, description="LLM-generated summary (Phase 3)")
    start_line: int = Field(..., ge=1, description="1-indexed start line")
    end_line: int = Field(..., ge=1, description="1-indexed end line")
    content_hash: str = Field(..., description="BLAKE2b hash of the content")
    parent_id: Optional[str] = Field(None, description="ID of parent chunk (method → class)")
    attached_comments: list[str] = Field(default_factory=list, description="Comments attached to this chunk")


class FileRecord(BaseModel):
    """Record of an indexed file."""
    path: str = Field(..., description="Relative path from repo root")
    language: Language
    content_hash: str = Field(..., description="BLAKE2b hash of file content")
    last_indexed: str = Field(..., description="ISO 8601 timestamp")
    chunk_count: int = Field(default=0)


class IndexConfig(BaseModel):
    """Configuration for indexing, loaded from .glma.toml + CLI flags."""
    languages: list[Language] = Field(
        default_factory=lambda: [Language.C, Language.PYTHON],
        description="Languages to index",
    )
    output_dir: str = Field(
        default=".glma-index",
        description="Index output directory (relative to repo root)",
    )
    include: list[str] = Field(
        default_factory=list,
        description="Glob patterns to include (empty = all source files)",
    )
    exclude: list[str] = Field(
        default_factory=lambda: [
            ".git", ".svn", ".hg",
            "venv", ".venv", "env",
            "node_modules", "bower_components",
            "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
            "build", "dist", "egg-info",
            ".tox", ".nox",
            ".glma-index",
        ],
        description="Directory/file names to exclude",
    )
    quiet: bool = Field(default=False, description="Suppress progress output")
