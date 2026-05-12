"""Language detection from file extensions."""

from pathlib import Path
from typing import Optional

from glma.models import Language


# Map of file extension → Language
EXTENSION_MAP: dict[str, Language] = {
    ".c": Language.C,
    ".h": Language.CPP,
    ".cpp": Language.CPP,
    ".hpp": Language.CPP,
    ".cc": Language.CPP,
    ".hxx": Language.CPP,
    ".py": Language.PYTHON,
    ".pyw": Language.PYTHON,
    ".ts": Language.TYPESCRIPT,
    ".tsx": Language.TSX,
    ".rs": Language.RUST,
}


def detect_language(filepath: Path) -> Optional[Language]:
    """Detect programming language from file extension.

    Args:
        filepath: Path to the source file.

    Returns:
        Language enum value, or None if extension not recognized.
    """
    return EXTENSION_MAP.get(filepath.suffix.lower())
