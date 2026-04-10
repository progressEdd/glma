"""Tests for summarization provider implementations."""

import pytest
from unittest.mock import MagicMock, patch

from glma.summarize.providers import OpenAICompatibleProvider, PiProvider


class TestOpenAICompatibleProvider:
    """Test OpenAI-compatible provider."""

    def test_init_raises_import_error_without_openai(self):
        """Init should raise ImportError with helpful message when openai not installed."""
        with patch.dict("sys.modules", {"openai": None}):
            with pytest.raises(ImportError, match="pip install glma\\[ai\\]"):
                OpenAICompatibleProvider()

    def test_summarize_calls_openai_api(self):
        """summarize() should call OpenAI chat completions API."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "A function that adds two numbers."

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_response

        # Mock the OpenAI class where it's imported (inside __init__)
        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAICompatibleProvider(base_url="http://localhost:1234/v1", model="test-model")
            result = provider.summarize("int add(int a, int b) { return a + b; }", "File: test.c\nChunk: add (function)")

        assert result == "A function that adds two numbers."
        mock_client.chat.completions.create.assert_called_once()
        call_kwargs = mock_client.chat.completions.create.call_args
        assert call_kwargs.kwargs["model"] == "test-model"
        assert call_kwargs.kwargs["max_tokens"] == 150

    def test_summarize_strips_whitespace(self):
        """summarize() should strip whitespace from response."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "  Summary text  \n"

        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_response

        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAICompatibleProvider()
            result = provider.summarize("code", "context")

        assert result == "Summary text"

    def test_init_with_custom_url_and_model(self):
        """Init should accept custom base_url and model."""
        mock_client = MagicMock()
        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAICompatibleProvider(base_url="http://ollama:11434/v1", model="llama3")
            mock_openai_cls.assert_called_once_with(base_url="http://ollama:11434/v1", api_key="not-needed")


class TestPiProvider:
    """Test pi provider."""

    def test_init_raises_import_error_without_pi(self):
        """Init should raise ImportError when pi SDK not available."""
        with patch.dict("sys.modules", {"pi": None}):
            with pytest.raises(ImportError, match="pi SDK"):
                PiProvider()

    def test_satisfies_protocol(self):
        """PiProvider should have summarize method matching protocol."""
        # Just verify the interface exists (can't test actual pi SDK without it)
        assert hasattr(PiProvider, "summarize")
        import inspect
        sig = inspect.signature(PiProvider.summarize)
        params = list(sig.parameters.keys())
        assert "code" in params
        assert "context" in params
