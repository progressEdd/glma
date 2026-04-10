"""Summarizer provider protocol for pluggable AI summarization."""

from typing import Protocol


class SummarizerProvider(Protocol):
    """Protocol for chunk summarization providers.

    Implementations receive a code chunk and its context, returning a summary string.
    Phase 7 will provide concrete implementations (OpenAI-compatible, pi agent).
    """

    def summarize(self, code: str, context: str) -> str:
        """Summarize a code chunk.

        Args:
            code: Source code of the chunk to summarize.
            context: Metadata about the chunk (file path, name, type, line range).

        Returns:
            Natural language summary of the chunk's purpose and behavior.
        """
        ...
