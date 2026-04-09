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


class RelType(str, Enum):
    """Types of structural relationships between code chunks."""
    CALLS = "calls"
    IMPORTS = "imports"
    INHERITS = "inherits"
    INCLUDES = "includes"  # C-specific: #include relationships


class Confidence(str, Enum):
    """Confidence level for relationship extraction."""
    DIRECT = "DIRECT"
    INFERRED = "INFERRED"


class Relationship(BaseModel):
    """A structural relationship between two code chunks."""
    source_id: str = Field(..., description="Chunk ID of the source")
    target_id: str = Field(default="", description="Chunk ID of target (empty if unresolved)")
    target_name: str = Field(..., description="Name as it appears in source code")
    rel_type: RelType
    confidence: Confidence
    source_line: int = Field(..., ge=1, description="Line where relationship originates")


class QueryConfig(BaseModel):
    """Configuration for query output, derived from CLI flags."""
    verbose: bool = Field(default=False, description="Include full code bodies")
    depth: int = Field(default=1, ge=1, le=10, description="Relationship traversal depth")
    no_relationships: bool = Field(default=False, description="Skip dependency section")
    output_format: str = Field(default="markdown", description="Output format: 'markdown' or 'json'")
    rel_types: list[str] = Field(default_factory=list, description="Filter relationship types (empty = all)")
    summary_only: bool = Field(default=False, description="Show only file summary, skip signatures")


class WatchConfig(BaseModel):
    """Configuration for file watching, loaded from .glma.toml + CLI flags."""
    debounce_seconds: float = Field(
        default=3.0,
        ge=0.5,
        le=30.0,
        description="Batch window for collecting file change events before processing",
    )
    verbose: bool = Field(
        default=False,
        description="Log every file event (type + path)",
    )


class ExportConfig(BaseModel):
    """Configuration for air-gapped export."""
    output_path: Optional[str] = Field(
        default=None,
        description="Output path: directory, .tar.gz/.tgz archive, or '-' for stdout",
    )
    include_code: bool = Field(
        default=True,
        description="Include full source code in exported chunks",
    )
    ai_summaries: bool = Field(
        default=False,
        description="Generate AI-powered file summaries via local model",
    )
    ai_base_url: str = Field(
        default="http://localhost:1234/v1",
        description="OpenAI-compatible API base URL for local model",
    )
    ai_model: str = Field(
        default="default",
        description="Model name for AI summaries",
    )


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
