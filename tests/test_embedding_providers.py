"""Tests for embedding provider implementations."""

import pytest
from unittest.mock import MagicMock, patch

from glma.embedding.providers import EmbeddingProvider, OpenAIEmbeddingProvider


class TestEmbeddingProviderProtocol:
    """Test EmbeddingProvider protocol compliance."""

    def test_protocol_defines_embed_method(self):
        """Protocol requires embed(texts) -> list[list[float]]."""
        # Verify protocol exists and has the right signature
        assert hasattr(EmbeddingProvider, "embed")


class TestOpenAIEmbeddingProvider:
    """Test OpenAI-compatible embedding provider."""

    def test_init_raises_import_error_without_openai(self):
        """Init should raise ImportError with helpful message when openai not installed."""
        with patch.dict("sys.modules", {"openai": None}):
            with pytest.raises(ImportError, match="pip install glma\\[ai\\]"):
                OpenAIEmbeddingProvider()

    def test_init_with_custom_url_and_model(self):
        """Init should accept custom base_url and model."""
        mock_client = MagicMock()
        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAIEmbeddingProvider(base_url="http://ollama:11434/v1", model="test-embed")
            mock_openai_cls.assert_called_once_with(base_url="http://ollama:11434/v1", api_key="not-needed")

    def test_embed_calls_embeddings_api(self):
        """embed() should call OpenAI embeddings.create API with input texts."""
        # Mock embedding response
        mock_data = [MagicMock(embedding=[0.1, 0.2, 0.3]), MagicMock(embedding=[0.4, 0.5, 0.6])]
        mock_response = MagicMock()
        mock_response.data = mock_data

        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAIEmbeddingProvider(base_url="http://localhost:1234/v1", model="test-model")
            result = provider.embed(["text1", "text2"])

        assert result == [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        mock_client.embeddings.create.assert_called_once_with(model="test-model", input=["text1", "text2"])

    def test_embed_empty_batch(self):
        """embed([]) should return empty list without calling API."""
        mock_client = MagicMock()
        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAIEmbeddingProvider()
            result = provider.embed([])

        assert result == []
        mock_client.embeddings.create.assert_not_called()

    def test_embed_single_text(self):
        """embed([single_text]) should work for single-item batch."""
        mock_data = [MagicMock(embedding=[0.1, -0.2, 0.3])]
        mock_response = MagicMock()
        mock_response.data = mock_data

        mock_client = MagicMock()
        mock_client.embeddings.create.return_value = mock_response

        mock_openai_cls = MagicMock(return_value=mock_client)
        with patch.dict("sys.modules", {"openai": MagicMock(OpenAI=mock_openai_cls)}):
            provider = OpenAIEmbeddingProvider()
            result = provider.embed(["hello world"])

        assert result == [[0.1, -0.2, 0.3]]
        mock_client.embeddings.create.assert_called_once_with(model="default", input=["hello world"])


class TestEmbeddingProviderPresets:
    """Test embedding provider preset data."""

    def test_embedding_presets_complete(self):
        from glma.models import EMBEDDING_PROVIDER_PRESETS
        expected = {"embed-ollama", "embed-lmstudio", "embed-vllm", "embed-llamacpp", "embed-local"}
        assert set(EMBEDDING_PROVIDER_PRESETS.keys()) == expected

    def test_ollama_preset_has_correct_url(self):
        from glma.models import EMBEDDING_PROVIDER_PRESETS
        assert EMBEDDING_PROVIDER_PRESETS["embed-ollama"]["base_url"] == "http://localhost:11434/v1"

    def test_ollama_preset_has_correct_model(self):
        from glma.models import EMBEDDING_PROVIDER_PRESETS
        assert EMBEDDING_PROVIDER_PRESETS["embed-ollama"]["model"] == "qwen3-embedding"

    def test_presets_are_prefixed(self):
        """All embedding presets start with 'embed-' to distinguish from summarization presets."""
        from glma.models import EMBEDDING_PROVIDER_PRESETS
        for name in EMBEDDING_PROVIDER_PRESETS:
            assert name.startswith("embed-"), f"Embedding preset '{name}' missing 'embed-' prefix"
