"""Hybrid search engine combining HNSW vector search with fuzzy keyword matching."""

import logging
from dataclasses import dataclass, field

from rapidfuzz import fuzz

from glma.db.ladybug_store import LadybugStore
from glma.embedding.providers import EmbeddingProvider
from glma.models import SearchConfig

logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    """A single search result with scores."""
    chunk_id: str
    file_path: str
    chunk_name: str
    chunk_type: str
    content: str
    summary: str
    start_line: int
    end_line: int
    keyword_score: float = 0.0
    vector_score: float = 0.0
    graph_score: float = 0.0
    combined_score: float = 0.0


class HybridSearchEngine:
    """Combines LadybugDB HNSW vector search with fuzzy keyword matching.

    Scoring: keyword_weight × keyword_score + vector_weight × vector_score
    Both scores normalized to 0-1 range before combining.
    """

    def __init__(
        self,
        store: LadybugStore,
        provider: EmbeddingProvider,
        config: SearchConfig,
    ):
        self._store = store
        self._provider = provider
        self._config = config

    def search(self, query: str, mode: str = "hybrid", graph: bool = False) -> list[SearchResult]:
        """Run hybrid search and return ranked, filtered results.

        Args:
            query: Natural language search query.
            mode: Search strategy — 'hybrid', 'vector', or 'keyword'.
            graph: If True, enable 3-way hybrid scoring with graph traversal.

        Returns:
            List of SearchResult sorted by combined_score descending,
            filtered by similarity_threshold.

        Raises:
            ValueError: If vector mode requested but no embeddings exist.
        """
        # Determine effective weights based on mode
        if mode == "vector":
            kw_weight, vec_weight = 0.0, 1.0
        elif mode == "keyword":
            kw_weight, vec_weight = 1.0, 0.0
        else:  # hybrid
            kw_weight = self._config.hybrid_keyword_weight
            vec_weight = self._config.hybrid_vector_weight

        # Validate vector availability
        needs_vector = vec_weight > 0
        if needs_vector:
            if not self._store.has_embeddings():
                raise ValueError(
                    "No embeddings found. Run `glma embed` first."
                )
            # Ensure vector index exists (lazy creation)
            self._store.create_vector_index(self._config.vector_dimensions)

        # Run vector search if needed
        vector_results: dict[str, dict] = {}
        if needs_vector:
            query_vecs = self._provider.embed([query])
            if not query_vecs:
                raise ValueError("Failed to embed query string.")
            query_vec = query_vecs[0]
            raw_vec = self._store.vector_search(query_vec, k=100)
            vector_results = {r["id"]: r for r in raw_vec}

        # Run keyword search if needed
        keyword_results: dict[str, float] = {}
        chunks_for_keyword: list[dict] = []
        if kw_weight > 0:
            chunks_for_keyword = self._store.get_chunks_with_summaries_for_keyword()
            keyword_results = self._fuzzy_score_all(query, chunks_for_keyword)

        # Merge candidates from both sources
        all_chunk_ids = set(vector_results.keys()) | set(keyword_results.keys())

        # Build chunk metadata
        chunk_meta: dict[str, dict] = {}
        for cid in vector_results:
            chunk_meta[cid] = vector_results[cid]
        for c in chunks_for_keyword:
            if c["id"] not in chunk_meta:
                chunk_meta[c["id"]] = c

        # Build search results with combined scores
        results: list[SearchResult] = []
        for cid in all_chunk_ids:
            meta = chunk_meta.get(cid, {})
            if not meta:
                continue
            kw_score = keyword_results.get(cid, 0.0)
            vec_score = vector_results[cid].get("vector_score", 0.0) if cid in vector_results else 0.0
            combined = kw_weight * kw_score + vec_weight * vec_score

            results.append(SearchResult(
                chunk_id=cid,
                file_path=meta.get("file_path", ""),
                chunk_name=meta.get("name", ""),
                chunk_type=meta.get("chunk_type", ""),
                content=meta.get("content", ""),
                summary=meta.get("summary", ""),
                start_line=meta.get("start_line", 0),
                end_line=meta.get("end_line", 0),
                keyword_score=kw_score,
                vector_score=vec_score,
                combined_score=combined,
            ))

        # Graph traversal phase (3-way hybrid)
        if graph and results:
            # Get seeds from current results (top-K by combined score)
            seeds = sorted(results, key=lambda r: r.combined_score, reverse=True)
            seed_ids = [r.chunk_id for r in seeds[:self._config.graph_fanout]]

            if seed_ids:
                # Run BFS traversal
                edges = self._store.traverse_relationships(
                    seed_ids, max_depth=self._config.graph_depth
                )

                # Extract discovered chunks with minimum depth
                seed_id_set = set(seed_ids)
                chunk_min_depth: dict[str, float] = {}
                for edge in edges:
                    # Skip self-referential edges
                    source_id = edge.get("source_id", "")
                    target_id = edge.get("target_id", "")
                    if source_id == target_id:
                        continue

                    # Determine the discovered chunk ID
                    direction = edge.get("direction", "outgoing")
                    if direction == "incoming":
                        discovered_id = source_id
                    else:
                        discovered_id = target_id

                    depth = edge.get("depth", 1)
                    if discovered_id and discovered_id not in seed_id_set:
                        if discovered_id not in chunk_min_depth or depth < chunk_min_depth[discovered_id]:
                            chunk_min_depth[discovered_id] = depth

                # Fetch metadata for graph-discovered chunks
                if chunk_min_depth:
                    discovered_ids = list(chunk_min_depth.keys())
                    discovered_meta = self._store.get_chunks_by_ids(discovered_ids)
                    meta_by_id = {m["id"]: m for m in discovered_meta}

                    # Add graph-only chunks to results
                    existing_ids = {r.chunk_id for r in results}
                    for cid, depth in chunk_min_depth.items():
                        if cid not in existing_ids and cid in meta_by_id:
                            m = meta_by_id[cid]
                            results.append(SearchResult(
                                chunk_id=cid,
                                file_path=m.get("file_path", ""),
                                chunk_name=m.get("name", ""),
                                chunk_type=m.get("chunk_type", ""),
                                content=m.get("content", ""),
                                summary=m.get("summary", ""),
                                start_line=m.get("start_line", 0),
                                end_line=m.get("end_line", 0),
                                keyword_score=0.0,
                                vector_score=0.0,
                                graph_score=1.0 / depth,
                            ))

            # Normalize all three dimensions and compute 3-way combined score
            if results:
                self._normalize_and_combine_3way(results)

        # Sort by combined score descending
        results.sort(key=lambda r: r.combined_score, reverse=True)

        # Filter by threshold
        threshold = self._config.similarity_threshold
        filtered = [r for r in results if r.combined_score >= threshold]

        logger.info(
            "Search '%s' (mode=%s, graph=%s): %d candidates, %d above threshold %.2f",
            query, mode, graph, len(results), len(filtered), threshold,
        )

        return filtered

    def _normalize_and_combine_3way(self, results: list[SearchResult]) -> None:
        """Min-max normalize graph, keyword, and vector scores, then combine with 3-way weights.

        Modifies results in-place, setting normalized scores and combined_score.
        """
        if not results:
            return

        EPSILON = 1e-9

        def min_max_normalize(values: list[float]) -> list[float]:
            min_v = min(values)
            max_v = max(values)
            range_v = max_v - min_v
            return [(v - min_v) / (range_v + EPSILON) for v in values]

        # Normalize each dimension
        norm_graph = min_max_normalize([r.graph_score for r in results])
        norm_kw = min_max_normalize([r.keyword_score for r in results])
        norm_vec = min_max_normalize([r.vector_score for r in results])

        # Get weights from config
        g_w = self._config.graph_weight
        kw_w = self._config.hybrid_keyword_weight
        vec_w = self._config.hybrid_vector_weight

        # Update scores to normalized values and compute combined
        for i, r in enumerate(results):
            r.graph_score = norm_graph[i]
            r.keyword_score = norm_kw[i]
            r.vector_score = norm_vec[i]
            r.combined_score = g_w * norm_graph[i] + kw_w * norm_kw[i] + vec_w * norm_vec[i]

    @staticmethod
    def _fuzzy_score_all(
        query: str,
        chunks: list[dict],
    ) -> dict[str, float]:
        """Compute fuzzy keyword scores for all chunks.

        Uses rapidfuzz.token_sort_ratio, normalized to 0-1.

        Args:
            query: Search query string.
            chunks: List of chunk dicts with 'id' and 'summary' keys.

        Returns:
            Dict mapping chunk_id to keyword score (0-1).
        """
        scores: dict[str, float] = {}
        for chunk in chunks:
            summary = chunk.get("summary", "")
            if not summary:
                continue
            raw = fuzz.token_sort_ratio(query, summary)
            scores[chunk["id"]] = raw / 100.0
        return scores
