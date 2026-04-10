"""Summarization pipeline and provider infrastructure."""

from glma.summarize.providers import SummarizerProvider
from glma.summarize.pipeline import summarize_chunks

__all__ = ["SummarizerProvider", "summarize_chunks"]
