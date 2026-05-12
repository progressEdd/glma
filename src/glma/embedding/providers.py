"""Embedding provider implementations for vector search."""

from typing import Protocol


class EmbeddingProvider(Protocol):
    """Protocol for embedding providers.

    Takes batch of texts, returns batch of float vectors.
    """

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embedding vectors for a batch of texts.

        Args:
            texts: List of text strings to embed.

        Returns:
            List of float vectors (one per input text).
        """
        ...


class OpenAIEmbeddingProvider:
    """Embedding provider using OpenAI-compatible API.

    Works with Ollama, LM Studio, llama.cpp server, vLLM, and any
    OpenAI-compatible embedding endpoint.
    Requires the 'openai' package (install with: pip install glma[ai]).
    """

    def __init__(self, base_url: str = "http://localhost:1234/v1", model: str = "default"):
        """Initialize provider.

        Args:
            base_url: OpenAI-compatible API base URL.
            model: Model name to use for embeddings.

        Raises:
            ImportError: If 'openai' package is not installed.
        """
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(
                "Embedding requires the 'openai' package. "
                "Install with: pip install glma[ai]"
            )
        self._client = OpenAI(base_url=base_url, api_key="not-needed")
        self._model = model

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embedding vectors for a batch of texts.

        Args:
            texts: List of text strings to embed.

        Returns:
            List of float vectors (one per input text).
        """
        if not texts:
            return []
        response = self._client.embeddings.create(
            model=self._model,
            input=texts,
        )
        return [item.embedding for item in response.data]
