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


class OpenAICompatibleProvider:
    """Summarization provider using OpenAI-compatible API.

    Works with Ollama, LM Studio, llama.cpp server, and any OpenAI-compatible endpoint.
    Requires the 'openai' package (install with: pip install glma[ai]).
    """

    SYSTEM_PROMPT = (
        "Summarize this code chunk in 1-2 concise sentences for a developer. "
        "Focus on purpose, inputs, outputs, and key behavior. "
        "Do not repeat the function/class name as the first word."
    )

    def __init__(self, base_url: str = "http://localhost:1234/v1", model: str = "default"):
        """Initialize provider.

        Args:
            base_url: OpenAI-compatible API base URL.
            model: Model name to use.

        Raises:
            ImportError: If 'openai' package is not installed.
        """
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(
                "Summarization requires the 'openai' package. "
                "Install with: pip install glma[ai]"
            )
        self._client = OpenAI(base_url=base_url, api_key="not-needed")
        self._model = model

    def summarize(self, code: str, context: str) -> str:
        """Summarize a code chunk using the OpenAI-compatible API.

        Args:
            code: Source code of the chunk.
            context: Metadata about the chunk (file path, name, type, line range).

        Returns:
            Natural language summary string.
        """
        user_message = f"{context}\n\n```\n{code}\n```"
        response = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            max_tokens=150,
            timeout=30.0,
        )
        return response.choices[0].message.content.strip()


class PiProvider:
    """Summarization provider using pi's SDK/API.

    Works when glma runs inside the pi agent environment.
    The pi extension registers this as a SummarizerProvider implementation.
    """

    def __init__(self, model: str = "default"):
        """Initialize pi provider.

        Args:
            model: Model name to use for summarization.

        Raises:
            ImportError: If pi SDK is not available (not running inside pi).
        """
        try:
            from pi import Agent
        except ImportError:
            raise ImportError(
                "Pi provider requires the pi SDK. "
                "This provider is only available when running inside the pi environment."
            )
        self._model = model

    def summarize(self, code: str, context: str) -> str:
        """Summarize a code chunk using pi's API.

        Args:
            code: Source code of the chunk.
            context: Metadata about the chunk (file path, name, type, line range).

        Returns:
            Natural language summary string.
        """
        from pi import Agent

        prompt = (
            f"Summarize this code chunk in 1-2 concise sentences. "
            f"Focus on purpose and key behavior.\n\n"
            f"{context}\n\n```\n{code}\n```"
        )
        agent = Agent()
        response = agent.run(prompt, model=self._model)
        return response.strip()

