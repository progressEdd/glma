"""Tests for summarization provider implementations."""

import pytest
from unittest.mock import MagicMock, patch

from glma.summarize.providers import OpenAICompatibleProvider


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


class TestProviderPresets:
    """Test provider preset data."""

    def test_provider_presets_complete(self):
        from glma.models import PROVIDER_PRESETS
        expected = {"local", "pi", "ollama", "lmstudio", "llamacpp", "vllm", "aphrodite"}
        assert set(PROVIDER_PRESETS.keys()) == expected

    def test_pi_provider_removed(self):
        """PiProvider stub was removed - real integration is TypeScript extension."""
        import importlib
        providers = importlib.import_module("glma.summarize.providers")
        assert not hasattr(providers, "PiProvider"), "PiProvider should be removed"
