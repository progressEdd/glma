"""Tests for query rewriter module."""

import sys
import types
from unittest.mock import MagicMock, patch

import pytest

from glma.search.rewriter import DEFAULT_REWRITE_PROMPT, rewrite_query


def _setup_openai_mock(content="authentication user login session verification"):
    """Set up mock openai module in sys.modules and return (mock_client, mock_openai_module).

    Returns the mock_client so tests can inspect create() call args.
    """
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = content
    mock_client.chat.completions.create.return_value = mock_response

    mock_openai_cls = MagicMock(return_value=mock_client)
    mock_module = types.ModuleType("openai")
    mock_module.OpenAI = mock_openai_cls

    return mock_client, mock_module, mock_openai_cls


class TestDefaultRewritePrompt:
    """Test DEFAULT_REWRITE_PROMPT constant."""

    def test_contains_abbreviation_rule(self):
        assert "Expand abbreviations" in DEFAULT_REWRITE_PROMPT

    def test_contains_return_only_rule(self):
        assert "Return ONLY the rewritten query string" in DEFAULT_REWRITE_PROMPT

    def test_contains_descriptive_language_rule(self):
        assert "natural descriptive language" in DEFAULT_REWRITE_PROMPT


class TestRewriteQuery:
    """Test rewrite_query function."""

    def test_successful_rewrite(self):
        mock_client, mock_module, _ = _setup_openai_mock()
        with patch.dict(sys.modules, {"openai": mock_module}):
            result = rewrite_query("how does auth work", "http://localhost:1234/v1", "default")
        assert result == "authentication user login session verification"
        # Verify system message uses DEFAULT_REWRITE_PROMPT
        call_kwargs = mock_client.chat.completions.create.call_args
        messages = call_kwargs.kwargs["messages"]
        assert messages[0]["content"] == DEFAULT_REWRITE_PROMPT
        assert messages[1]["content"] == "how does auth work"

    def test_custom_rewrite_prompt(self):
        mock_client, mock_module, _ = _setup_openai_mock()
        with patch.dict(sys.modules, {"openai": mock_module}):
            result = rewrite_query(
                "auth", "http://localhost:1234/v1", "default",
                rewrite_prompt="Custom prompt",
            )
        call_kwargs = mock_client.chat.completions.create.call_args
        messages = call_kwargs.kwargs["messages"]
        assert messages[0]["content"] == "Custom prompt"

    def test_empty_response_returns_original(self):
        mock_client, mock_module, _ = _setup_openai_mock(content="")
        with patch.dict(sys.modules, {"openai": mock_module}):
            result = rewrite_query("my query", "http://localhost:1234/v1", "default")
        assert result == "my query"

    def test_strips_whitespace(self):
        mock_client, mock_module, _ = _setup_openai_mock(content="  rewritten query  ")
        with patch.dict(sys.modules, {"openai": mock_module}):
            result = rewrite_query("q", "http://localhost:1234/v1", "default")
        assert result == "rewritten query"

    def test_import_error_when_no_openai(self):
        """ImportError from missing openai package triggers user-friendly error."""
        # Remove openai from sys.modules if present
        saved = sys.modules.get("openai")
        sys.modules.pop("openai", None)
        try:
            with pytest.raises(ImportError, match="pip install glma\\[ai\\]"):
                rewrite_query("q", "http://localhost:1234/v1", "default")
        finally:
            if saved is not None:
                sys.modules["openai"] = saved

    def test_timeout_and_max_tokens_passed(self):
        mock_client, mock_module, _ = _setup_openai_mock()
        with patch.dict(sys.modules, {"openai": mock_module}):
            rewrite_query("q", "http://localhost:1234/v1", "default", timeout=5.0, max_tokens=50)
        call_kwargs = mock_client.chat.completions.create.call_args
        assert call_kwargs.kwargs["timeout"] == 5.0
        assert call_kwargs.kwargs["max_tokens"] == 50
