# Phase 20: 3-Way Hybrid Search - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-05-12
**Phase:** 20-3-way-hybrid-search
**Areas discussed:** Graph Scoring Model, Score Normalization & Combination, Score Breakdown Display, Graph Traversal Behavior

---

## Graph Scoring Model

### Q1: How should graph depth map to a relevance score?

| Option | Description | Selected |
|--------|-------------|----------|
| Inverse depth decay (`1/depth`) | Direct neighbor = 1.0, 2 hops = 0.5, 3 hops = 0.33. Simple, predictable. | ✓ |
| Exponential decay (`0.5^(depth-1)`) | Steep dropoff: 1.0, 0.5, 0.25. Emphasizes direct connections heavily. | |
| Fixed tiers (0.8/0.4/0.1) | Less mathematically elegant but easy to reason about. | |

**User's choice:** Inverse depth decay
**Notes:** Simple, matches intuition (half as relevant per hop), depth=2 gives 0.5 which doesn't overwhelm or disappear in the combined score.

### Q2: Should edge type affect the graph score?

| Option | Description | Selected |
|--------|-------------|----------|
| Flat (no edge-type weighting) | All RELATES_TO edges treated equally. Depth is the only signal. | ✓ |
| Weighted by edge type | calls=1.0, inherits=0.9, imports=0.7, includes=0.5. Multiplied into depth score. | |

**User's choice:** Flat
**Notes:** Edge types were designed for code structure, not search relevance. Adding weights creates tuning complexity without clear evidence it improves results.

### Q3: Should confidence level (DIRECT vs INFERRED) affect graph score?

| Option | Description | Selected |
|--------|-------------|----------|
| Ignore confidence | DIRECT and INFERRED edges weighted the same. | ✓ |
| Penalize INFERRED | DIRECT multiplier = 1.0, INFERRED = 0.7. | |

**User's choice:** Ignore confidence
**Notes:** INFERRED tag was meant for display transparency, not scoring. Penalizing could exclude valid cross-file relationships.

### Q4: How to handle graph-only chunks (no keyword or vector score)?

| Option | Description | Selected |
|--------|-------------|----------|
| Include with zero kw/vec scores | Graph-only chunks get combined score = graph_weight × graph_score. | ✓ |
| Exclude graph-only chunks | Graph only boosts existing candidates, never introduces new ones. | |

**User's choice:** Include with zero kw/vec scores
**Notes:** This is the whole point of graph traversal — discovering relevant code the text search missed.

---

## Score Normalization & Combination

### Q1: How should the three weights be specified and validated?

| Option | Description | Selected |
|--------|-------------|----------|
| Three explicit weights that must sum to ~1.0 | graph=0.4, keyword=0.3, vector=0.3. Strict validation. | ✓ |
| Three explicit weights, auto-normalized | User provides raw weights (4, 3, 3), system divides by sum. | |
| Two weights + derived third | Keep existing two, derive third. Backward-compatible. | |

**User's choice:** Three explicit weights summing to ~1.0
**Notes:** Matches existing validator pattern (checks `abs(total - 1.0) > 0.05`). ROADMAP specifies defaults 0.4, 0.3, 0.3.

### Q2: Should scores be min-max normalized or used as-is?

| Option | Description | Selected |
|--------|-------------|----------|
| Min-max normalize per dimension across result set | For each dimension, rescale to [0,1]. No single dimension dominates. | ✓ |
| Use as-is (no renormalization) | Scores already 0-1. Combine directly with weights. | |

**User's choice:** Min-max normalize
**Notes:** HYBR-03 explicitly requires normalization. Vector scores might cluster in 0.7-0.9 while keyword spreads 0.3-0.8.

### Q3: How to handle min==max normalization edge case?

| Option | Description | Selected |
|--------|-------------|----------|
| Smoothing constant (epsilon) | `(score - min) / (max - min + epsilon)`. Standard approach. | ✓ |
| Default to 1.0 when min==max | Only result = maximum relevance. | |
| Default to 0.5 when min==max | Neutral middle-ground. | |

**User's choice:** Smoothing constant (epsilon)
**Notes:** Standard numerical approach, doesn't over-reward single results.

---

## Score Breakdown Display

### Q1: What should score breakdown look like in markdown formats?

| Option | Description | Selected |
|--------|-------------|----------|
| Inline annotation | `> *Scores: graph=0.7, keyword=0.4, vector=0.9, combined=0.67*` | ✓ |
| Header block per result | Structured block with score line before code. | |
| Only in JSON/YAML | Markdown stays lean, no scores at all. | |

**User's choice:** Inline annotation
**Notes:** Mirrors existing summary annotation pattern. Only appears when `--graph` is active.

### Q2: Should JSON/YAML show raw scores, normalized, or both?

| Option | Description | Selected |
|--------|-------------|----------|
| Normalized only | Clean, reflects what was used for ranking. | ✓ |
| Both raw and normalized | `scores` + `raw_scores` dicts. More transparent but doubles output. | |

**User's choice:** Normalized only
**Notes:** Raw scores are an implementation detail. Users debugging ranking can look at combined score and weights.

---

## Graph Traversal Behavior

### Q1: Where should graph traversal seeds come from?

| Option | Description | Selected |
|--------|-------------|----------|
| Top-K from keyword + vector results | Run 2-way first, take top K chunks as BFS seeds. | ✓ |
| Top-K from vector results only | Semantically closest seeds. Keyword matches may be structurally irrelevant. | |
| All chunks that pass threshold | Every 2-way result as seed. More thorough but expensive. | |

**User's choice:** Top-K from keyword + vector results
**Notes:** Uses best of both existing dimensions as seeds. K tied to `graph_fanout` config.

### Q2: Should graph traversal follow edges in both directions?

| Option | Description | Selected |
|--------|-------------|----------|
| Both directions (bidirectional) | Discovers "who depends on this" and "what does this depend on." | ✓ |
| Outgoing only | Only what the matched code *uses*. More focused. | |

**User's choice:** Both directions (bidirectional)
**Notes:** Existing `traverse_relationships()` already does this. Both directions are valuable for search.

### Q3: How should depth and fan-out be configurable?

| Option | Description | Selected |
|--------|-------------|----------|
| Config + CLI flags | `--graph-depth` and `--graph-fanout` flags, with config defaults. | ✓ |
| Config file only | Keeps CLI simple. Most users won't tweak these. | |

**User's choice:** Config + CLI flags
**Notes:** Follows existing pattern. Power users tuning search will want to experiment interactively.

### Q4: Which depth determines score for multi-path chunks?

| Option | Description | Selected |
|--------|-------------|----------|
| Minimum depth (shortest path) | BFS visited set ensures first discovery = shortest. | ✓ |
| Average depth | Smoother but less intuitive. | |
| Maximum depth (longest path) | Most conservative. | |

**User's choice:** Minimum depth (shortest path)
**Notes:** BFS naturally discovers shortest paths first. The visited set already handles this.

---

## Agent's Discretion

- Exact epsilon value for normalization smoothing
- How to extract discovered chunks from `traverse_relationships()` edge results
- How to handle self-referential edges during graph search
- Whether `graph_fanout` limits seeds or per-node fan-out or both
- Module structure (extend `engine.py` or new `graph.py`)
- Exact `SearchConfig` validator update for 3-way weight sum
- Test structure and coverage specifics

## Deferred Ideas

None - discussion stayed within phase scope.
