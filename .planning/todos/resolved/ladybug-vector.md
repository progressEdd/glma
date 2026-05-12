---
created: 2026-05-11T00:00:00Z
resolved: 2026-05-12
resolved_by: v1.3 Phases 14-15 (vector storage, hybrid search)
title: Ladybug vector extension reference (research/consumed)
status: done
---

If you've ever tried to bolt a dedicated vector database onto an existing graph database, you know the pain: two systems to manage, data to sync, query results to stitch together across network boundaries. LadybugDB takes a different approach. It ships a native **vector** extension that gives you disk-based approximate nearest-neighbor (ANN) search right inside the same engine where your graph lives. You install one extension, store embeddings as regular node properties, build an index, and query everything --- vectors *and* graph structure --- in the same Cypher statement.

In this article we'll go deep. We'll start with the theory behind the HNSW index algorithm that powers the extension, walk through how each tuning parameter shapes its behavior, and then get practical: creating indexes, querying them, combining vector search with graph traversals, pre-filtering, post-filtering, projected graphs with arbitrary Cypher, and cocmplex multi-step queries. Let's get into it.

* * * *

**1\. How Vector Search Actually Works --- The HNSW Algorithm**

---------------------------------------------------------------

Before we look at any LadybugDB syntax, it's worth understanding what happens under the hood. The vector extension implements a **Hierarchical Navigable Small World (HNSW)** graph. This is the same algorithmic family that powers most modern vector databases --- Pinecone, Weaviate, Qdrant, and others all use some variant of HNSW. It's popular because it offers an excellent trade-off between search speed, recall accuracy, and memory usage.

### **The core idea: a graph of vectors**

Imagine you have a million 384-dimensional embedding vectors. A brute-force search would compute the distance from your query vector to every single one of those million vectors, rank them, and return the top K. That's perfectly accurate, but it's O(n)*O*(*n*) --- painfully slow at scale.

HNSW avoids this by building a **graph** on top of the vectors. Each vector becomes a node in this graph, and edges connect vectors that are relatively close to each other in the embedding space. When you search, instead of scanning all million vectors, you *walk* the graph: start at some entry point, look at the current node's neighbors, move to whichever neighbor is closest to your query, and repeat. You're doing a kind of greedy hill-climbing through the vector space. Because the graph is structured so that nearby vectors are connected, this walk converges quickly toward the true nearest neighbors --- typically in O(log⁡n)*O*(log*n*) hops rather than O(n)*O*(*n*) comparisons.

### **Why "hierarchical"? The two-layer structure**

The original Navigable Small World (NSW) algorithm builds a single graph. It works, but it can get stuck in local optima --- the greedy walk might take a long, winding path to reach the right neighborhood, especially in high-dimensional spaces.

HNSW fixes this by introducing **hierarchy**. LadybugDB's implementation uses **two layers**:

-   **Upper layer** --- A small, sparse graph containing only a sampled subset of all vectors. Think of it like a highway network: fewer nodes, but each one has long-range connections that span large distances in the embedding space. It's controlled by the `pu` parameter, which sets the fraction of vectors promoted to this layer.

-   **Lower layer** --- A dense graph containing *every* vector. This is the local road network: dense connections, short-range, precise. Every vector lives here.

Here's how a search works step by step:

1.  **Enter the upper layer.** The algorithm starts at an entry point in the sparse upper graph. Because there are few nodes here and they have long-range edges, each hop covers a lot of ground. The algorithm greedily walks toward the region closest to the query vector.

2.  **Descend to the lower layer.** Once the upper-layer search converges (it can't find a closer neighbor), the algorithm takes its current best position and drops down to the dense lower layer. Now it's in the right neighborhood.

3.  **Refine in the lower layer.** The algorithm does another greedy walk in the dense graph, exploring local connections until it has found the K nearest neighbors with high confidence.

This two-phase approach is what makes HNSW so fast. The upper layer eliminates most of the search space in a few hops, and the lower layer does the precise work. You never scan all vectors.

### **How the index gets built**

Index construction is just as important as search. When you call `CREATE_VECTOR_INDEX`, LadybugDB builds the HNSW graph by inserting vectors one at a time. For each new vector:

1.  It searches the existing graph to find the closest nodes (using the same greedy algorithm described above).

2.  It connects the new vector to its nearest neighbors with edges.

3.  If the new vector is selected for the upper layer (with probability `pu`), it also gets inserted into the upper graph with its own set of connections.

The quality of these connections determines the quality of the index. More connections per node mean more paths for the search algorithm to explore, which improves recall (the chance of finding the true nearest neighbors). But more connections also mean a larger index and slower construction.

### **What each parameter does and why it matters**

Now that you understand the structure, let's talk about the parameters. Each one controls a specific aspect of the index, and understanding them will help you make good trade-off decisions for your use case.

`mu` (default: `30`) --- This is the maximum number of edges per node in the **upper** layer. Remember, the upper layer is the "highway network" with long-range connections. A higher `mu` means each upper-layer node is connected to more peers, giving the search algorithm more choices during the coarse navigation phase. This improves recall but makes the upper layer larger. It must be smaller than `ml` --- the upper layer should be sparser than the lower one, by design.

`ml` (default: `60`) --- This is the maximum number of edges per node in the **lower** layer. The lower layer is where the fine-grained search happens, so it needs denser connectivity than the upper layer. A higher `ml` means more local connections, better recall, but a bigger index. Think of it this way: if `ml` is too low, the greedy walk in the lower layer might get stuck because there aren't enough edges to route around obstacles in the embedding space. If it's too high, you're paying for storage and construction time that gives diminishing returns.

`pu` (default: `0.05`) --- The fraction of vectors promoted to the upper layer, between 0.0 and 1.0. At the default of 0.05, only 5% of vectors get promoted. This keeps the upper layer small and fast to traverse. If you increase `pu`, the upper layer gets denser, which can improve recall for very large datasets (because you have more highway nodes to route through), but it also increases memory usage and construction time. For most workloads, the default is fine. You might bump it to 0.1 or 0.15 for datasets with millions of vectors where you're seeing recall drop-off.

`metric` (default: `cosine`) --- The distance function used to compare vectors. This affects both index construction (which nodes get connected) and search (which direction the greedy walk goes). The choice depends on your embeddings:

-   `cosine` --- Measures the angle between vectors, ignoring magnitude. This is the right choice for most text embeddings (sentence-transformers, OpenAI embeddings, etc.) because these models typically produce normalized or near-normalized vectors where direction encodes meaning.

-   `l2` --- Standard Euclidean distance. Good when the magnitude of the vector carries information, not just the direction.

-   `l2sq` --- Squared Euclidean distance. Mathematically gives the same ranking as `l2` (squared is a monotonic transformation), but skips the square-root computation, making it slightly faster.

-   `dotproduct` --- Negative inner product. Use this for maximum inner-product search (MIPS) when your embeddings are already normalized. In that case, dot product and cosine give the same ranking, but dot product avoids the normalization step.

`efc` (default: `200`) --- The number of candidate vertices to consider during **index construction**. When inserting a new vector, the algorithm searches the existing graph for neighbors to connect to. `efc` controls how wide that search is. A higher `efc` means the construction algorithm explores more candidates before deciding on connections, leading to a higher-quality index (better connections = better recall at search time). The cost is slower index building. For a quick prototype, you can drop this to 100. For a production index where recall matters, you might push it to 400 or higher.

`cache_embeddings` (default: `true`) --- During index construction, the algorithm needs to repeatedly compute distances between vectors. If `cache_embeddings` is true, LadybugDB loads the entire embedding column into memory so these distance computations don't require disk reads. This dramatically speeds up construction but costs RAM proportional to your embedding data. For a million 384-dim float32 vectors, that's about 1.5 GB of RAM. If you're memory-constrained, set this to false --- construction will be slower but will use much less memory. The final index is always disk-based regardless of this setting.

`efs` (default: `200`) --- This one is a **query-time** parameter, not a construction parameter. It controls the number of candidate vertices considered during search. A higher `efs` means the search explores more of the graph before returning results, improving recall at the cost of latency. The nice thing about `efs` is that you can tune it per-query: use a lower value (50--100) for latency-sensitive applications where approximate results are fine, and a higher value (500+) when you need high recall and can tolerate a bit more latency. You don't need to rebuild the index to change `efs`.

### **The recall-speed trade-off in practice**

All of these parameters ultimately control one thing: the trade-off between **recall** (how often the approximate search finds the true nearest neighbors) and **speed** (how fast the search and construction run). There's no free lunch here:

-   Want higher recall? Increase `ml`, `mu`, `efc`, `efs`, and/or `pu`. Everything gets slower and bigger.

-   Want faster search? Decrease `efs`. You can do this without rebuilding.

-   Want faster construction? Decrease `efc` and/or set `cache_embeddings := false`.

-   Working with a huge dataset? Consider increasing `pu` slightly so the upper layer covers more ground.

For most use cases, the defaults are a solid starting point. Start there, measure recall on a held-out test set, and adjust if needed.

* * * *

**2\. Getting Started --- Example Dataset**

-------------------------------------------

Let's set up a small dataset so we have something concrete to work with throughout the rest of this article. We'll create a graph of books and publishers, generate embeddings for the book titles, and load everything into LadybugDB.

```
`# pip install sentence-transformers
import real_ladybug as lb
from sentence_transformers import SentenceTransformer

db = lb.Database("example.lbug")
conn = lb.Connection(db)

conn.execute("INSTALL vector; LOAD vector;")

# Schema
conn.execute("""
    CREATE NODE TABLE Book(
        id SERIAL PRIMARY KEY,
        title STRING,
        title_embedding FLOAT[384],
        published_year INT64
    );
""")
conn.execute("CREATE NODE TABLE Publisher(name STRING PRIMARY KEY);")
conn.execute("CREATE REL TABLE PublishedBy(FROM Book TO Publisher);")

model = SentenceTransformer("all-MiniLM-L6-v2")

titles = [
    "The Quantum World",
    "Chronicles of the Universe",
    "Learning Machines",
    "Echoes of the Past",
    "The Dragon's Call",
]
publishers = [
    "Harvard University Press",
    "Independent Publisher",
    "Pearson",
    "McGraw-Hill Ryerson",
    "O'Reilly",
]
published_years = [2004, 2022, 2019, 2010, 2015]

for title, year in zip(titles, published_years):
    emb = model.encode(title).tolist()
    conn.execute(
        """CREATE (b:Book {
               title: $title,
               title_embedding: $emb,
               published_year: $year
           });""",
        {"title": title, "emb": emb, "year": year},
    )

for pub in publishers:
    conn.execute("CREATE (p:Publisher {name: $pub});", {"pub": pub})

for title, pub in zip(titles, publishers):
    conn.execute(
        """MATCH (b:Book {title: $title})
           MATCH (p:Publisher {name: $pub})
           CREATE (b)-[:PublishedBy]->(p);""",
        {"title": title, "pub": pub},
    )
`
```

A few things to notice here. The `title_embedding` property is declared as `FLOAT[384]` --- that's a fixed-size float array matching the output dimension of the `all-MiniLM-L6-v2` model. LadybugDB requires your embedding property to be typed as an `ARRAY` of `FLOAT` or `DOUBLE`. We also have a `published_year` column, which we'll use later for filtered searches. And we have a `PublishedBy` relationship connecting books to publishers, which we'll traverse from vector search results.

* * * *

**3\. Creating a Vector Index**

---------------------------------

With the data loaded, let's build an index:

```
`CALL CREATE_VECTOR_INDEX(
    'Book',                -- table name
    'book_title_index',    -- index name
    'title_embedding',     -- property (must be FLOAT[] or DOUBLE[])
    metric := 'l2'         -- optional overrides
);
`
```

That's it. Behind the scenes, LadybugDB reads every `title_embedding` value from the `Book` table and builds the two-layer HNSW graph we discussed in section 1. You can pass any of the tuning parameters as named arguments --- `mu`, `ml`, `pu`, `efc`, `cache_embeddings` --- if you want to override the defaults. For our small five-book dataset the defaults are more than enough. For a production dataset with millions of rows, you'd want to think more carefully about these values.

All the optional params (`mu`, `ml`, `pu`, `efc`, `cache_embeddings`) can be passed as named arguments. Defaults work well for moderate-sized datasets; tune `ml`/`mu` upward for very large collections where recall matters more than build-time.

### **Index management**

You can inspect and manage your indexes with a couple of utility functions:

```
`-- List all indexes
CALL SHOW_INDEXES() RETURN *;

-- Drop an index
CALL DROP_VECTOR_INDEX('Book', 'book_title_index');
`
```

`SHOW_INDEXES()` returns useful metadata: the table name, index name, index type (HNSW), the property it was built on, whether the extension is loaded, and the full index definition. Handy for debugging when you have multiple indexes across different tables.

* * * *

**4\. Querying the Vector Index**

-----------------------------------

Now for the fun part. To find the K nearest neighbors of a query vector:

```
`CALL QUERY_VECTOR_INDEX(
    'Book',
    'book_title_index',
    $query_vector,
    2,                    -- K nearest neighbors
    efs := 500            -- optional: expand candidate set for better recall
)
RETURN node.title, distance
ORDER BY distance;
`
```

The function returns two things for each match:

-   `node` --- The full node object. You can access any of its properties (`node.title`, `node.published_year`, etc.), and you can use it as a starting point for graph traversals.

-   `distance` --- The distance between the query vector and this node's vector, computed using whatever metric you specified when creating the index.

Notice the `efs := 500` parameter. Remember, this controls search-time recall. Here we're bumping it above the default of 200 because we want higher accuracy. For a quick exploratory query, you could leave it at the default or even lower it.

### **Combining with graph traversal**

This is where having vector search inside a graph database really pays off. Instead of getting back a list of IDs and then making a separate query to look up related data, you just keep writing Cypher. Use the vector search to find your entry points, then follow edges wherever they lead:

```
`CALL QUERY_VECTOR_INDEX('Book', 'book_title_index', $query_vector, 2)
WITH node AS n, distance
MATCH (n)-[:PublishedBy]->(p:Publisher)
RETURN p.name AS publisher, n.title AS book, distance
ORDER BY distance;
`
```

The `WITH` clause takes the vector search results and feeds them into a standard `MATCH` pattern. We're asking: "Find the 2 books most similar to my query vector, then tell me who published them." The result looks like this:

```
`┌──────────────────────────┬───────────────────┬──────────┐
│ publisher                ┆ book              ┆ distance │
╞══════════════════════════╪═══════════════════╪══════════╡
│ Harvard University Press ┆ The Quantum World ┆ 0.311872 │
│ Pearson                  ┆ Learning Machines ┆ 0.415366 │
└──────────────────────────┴───────────────────┴──────────┘
`
```

In a traditional setup, you'd call the vector database, get back two IDs, then query your graph database for the publisher relationships. Here it's a single query. No network hop, no result-stitching, no consistency issues.

* * * *

**5\. Filtered Vector Search**

--------------------------------

In practice, you almost never want "find me the K closest vectors, period." You usually want something like "find me the K closest vectors *that also satisfy some condition*." Maybe you only want books published after a certain year, or books from a specific publisher, or books that match some complex graph pattern.

There are two ways to do this: **pre-filtering** and **post-filtering**. They have very different performance characteristics, so it's worth understanding both.

### **5.1 Pre-filtering with** `PROJECT_GRAPH`

Pre-filtering is the more powerful approach. The idea is: before you even run the vector search, you create a *projected graph* that contains only the nodes matching your filter. The HNSW search then runs exclusively over this subset. Nodes that don't match the filter are never visited, never scored, never considered.

Here's an example. Say we want books similar to "quantum world", but only those published after 2010:

```
`-- Step 1: project the graph with a filter predicate
CALL PROJECT_GRAPH(
    'filtered_book',                    -- projected graph name
    {'Book': 'n.published_year > 2010'},-- node table → filter expression
    []                                  -- no relationship tables needed
);

-- Step 2: vector search against the projected graph
CALL QUERY_VECTOR_INDEX(
    'filtered_book',       -- use the projected graph name instead of table name
    'book_title_index',
    $query_vector,
    2
)
WITH node AS n, distance AS dist
MATCH (n)-[:PublishedBy]->(p:Publisher)
RETURN n.title AS book,
       n.published_year AS year,
       p.name AS publisher
ORDER BY dist;
`
```

Notice the key trick: in step 2, we pass `'filtered_book'` (the projected graph name) instead of `'Book'` (the table name) as the first argument to `QUERY_VECTOR_INDEX`. That tells LadybugDB to restrict the search to the projected subset.

The result:

```
`┌────────────────────────────┬──────┬───────────────────────┐
│ book                       ┆ year ┆ publisher             │
╞════════════════════════════╪══════╪═══════════════════════╡
│ Chronicles of the Universe ┆ 2022 ┆ Independent Publisher │
│ Learning Machines          ┆ 2019 ┆ Pearson               │
└────────────────────────────┴──────┴───────────────────────┘
`
```

"The Quantum World" is the semantically closest book to our query, but it was published in 2004, so it's excluded by the filter. We get the next two closest books that actually satisfy the condition.

**Why pre-filtering matters:** The HNSW search never visits filtered-out nodes. If your filter eliminates 90% of the data, the search runs over a candidate set that's 10x smaller --- much faster. And crucially, pre-filtering **guarantees** you get exactly K results that satisfy the predicate. With post-filtering, you might not.

### **5.2 Post-filtering**

Post-filtering is simpler to write. You run the vector search over the full, unfiltered index, then apply a `WHERE` clause to the results:

```
`CALL QUERY_VECTOR_INDEX('Book', 'book_title_index', $query_vector, 10)
WITH node AS n, distance
WHERE n.published_year > 2010
RETURN n.title AS book, n.published_year AS year, distance
ORDER BY distance
LIMIT 2;
`
```

This is easier --- you don't need to create a projected graph --- but it has a fundamental problem. We asked for K=10 from the vector search, hoping that at least 2 of those 10 results would pass the filter. If the filter is highly selective (say it eliminates 99% of the data), you might get zero results after filtering even with K=10. You'd have to keep increasing K, which means more wasted work. It's a guessing game.

**The trade-off in a nutshell:** Post-filtering is great for quick exploration and loosely selective filters (filters that only eliminate a small fraction of the data). Pre-filtering is better when the filter is selective, when you need guaranteed result counts, or when you're building a production pipeline where reliability matters.

### **5.3 Pre-filtering vs Post-filtering --- When to use which**

**Pre-filtering** (`PROJECT_GRAPH`):

-   Guarantees exactly K results --- search only touches qualifying nodes.

-   Excellent performance on selective filters --- smaller candidate set.

-   Requires creating a projected graph upfront.

-   Best for highly selective filters and production pipelines.

**Post-filtering** (`WHERE`):

-   No guarantee of K results --- may get fewer than K after filtering.

-   Can waste ANN work on selective filters since most scored nodes get discarded.

-   Easy to use --- just add `WHERE` after the vector call.

-   Best for quick exploration and loosely selective filters.

* * * *

**6\. Complex Queries with Vector Search**

--------------------------------------------

Here's where LadybugDB's approach really shines compared to standalone vector databases. Because `QUERY_VECTOR_INDEX` returns regular Cypher variables (`node`, `distance`), you can compose it with *anything* Cypher offers: aggregations, multi-hop traversals, path patterns, subqueries, and more. It's not a special-purpose API --- it's just another step in a Cypher pipeline.

### **Example: Finding the publisher most aligned with a topic**

Let's say you want to know which publisher has the strongest overall affinity for "quantum machine learning." You don't just want the nearest books --- you want to aggregate across publishers:

```
`CALL QUERY_VECTOR_INDEX('Book', 'book_title_index', $query_vector, 5)
WITH node AS n, distance
MATCH (n)-[:PublishedBy]->(p:Publisher)
RETURN p.name AS publisher,
       COUNT(n) AS matched_books,
       SUM(distance) AS total_distance
ORDER BY total_distance;
`
```

This takes the 5 nearest books, follows the `PublishedBy` edges to their publishers, groups by publisher, and returns aggregated metrics. In a production dataset with thousands of books and hundreds of publishers, this becomes a genuinely useful analytical query --- "which publisher's catalog is most semantically similar to this topic?"

### **Example: Multi-hop "more like this" discovery**

One of the most powerful patterns is using vector search as an entry point, then exploring the graph to find things that are *structurally* related to the *semantically* similar results:

```
`CALL QUERY_VECTOR_INDEX('Book', 'book_title_index', $query_vector, 3)
WITH node AS n, distance
MATCH (n)-[:PublishedBy]->(p:Publisher)<-[:PublishedBy]-(other:Book)
WHERE other.title <> n.title
RETURN n.title AS query_match,
       other.title AS co_published_book,
       p.name AS shared_publisher,
       distance
ORDER BY distance;
`
```

This says: "Find the 3 books most similar to my query, then find *other* books published by the *same* publishers." It's a recommendation pattern that blends semantic similarity with collaborative structure. The vector search finds the topic-relevant books; the graph traversal finds what's related by context (same publisher). You'd need two separate queries and application-level joining to do this with a standalone vector store.

* * * *

**7\. Projected Graphs with Arbitrary Cypher Queries**

--------------------------------------------------------

We've already seen `PROJECT_GRAPH` for simple property predicates. But what if your filter isn't a simple property comparison? What if you want to filter based on relationship patterns, aggregations, or complex subqueries?

That's where `PROJECT_GRAPH_CYPHER` comes in. It lets you define the projected graph using a full Cypher statement:

```
`CALL PROJECT_GRAPH_CYPHER(
    <GRAPH_NAME>,
    <CYPHER_STATEMENT>
);
`
```

The Cypher statement can contain **any** pattern matching you want --- multi-hop patterns, `WHERE` clauses, aggregations, `COLLECT`, `UNWIND`, whatever you need. The only constraint is that the `RETURN` clause must yield a single node variable whose label matches the table with the vector index.

### **Example: Books published by Pearson**

A simple relationship-based filter that you can't express with `PROJECT_GRAPH`'s property predicates alone:

```
`CALL PROJECT_GRAPH_CYPHER(
    'pearson_book',
    'MATCH (b:Book)-[:PublishedBy]->(p:Publisher {name: ''Pearson''}) RETURN b'
);

CALL QUERY_VECTOR_INDEX(
    'pearson_book',
    'book_title_index',
    $query_vector,
    5
)
RETURN node.title, distance
ORDER BY distance;
`
```

Now the vector search only considers books that are connected to the Pearson publisher via a `PublishedBy` edge. The filter is defined by a graph pattern, not just a property value.

### **Example: Complex multi-condition filter**

Here's a more sophisticated example. Say you want books published after 2015, but only from publishers who have at least 2 books in the database:

```
`CALL PROJECT_GRAPH_CYPHER(
    'prolific_recent',
    'MATCH (b:Book)-[:PublishedBy]->(p:Publisher)
     WITH p, COLLECT(b) AS books
     WHERE SIZE(books) >= 2
     UNWIND books AS b
     WHERE b.published_year > 2015
     RETURN b'
);

CALL QUERY_VECTOR_INDEX(
    'prolific_recent',
    'book_title_index',
    $query_vector,
    3
)
RETURN node.title, node.published_year, distance
ORDER BY distance;
`
```

This Cypher statement groups books by publisher, filters to publishers with at least 2 books, unwinds the books back out, filters by year, and returns the qualifying nodes. LadybugDB materializes this set and the HNSW search runs only over it. The key insight is that you can express *any* filtering logic here --- as long as it ends with returning nodes from the indexed table, the vector search will respect it.

This is the most powerful filtering mechanism in LadybugDB's vector search toolkit. You write an arbitrary Cypher subgraph query to define your candidate set, and the HNSW search is restricted to exactly that set. It composes naturally with the rest of the query pipeline --- after the vector search, you can continue with more `MATCH` patterns, `WHERE` clauses, aggregations, whatever you need.

> **Note:** Projected graphs created by `PROJECT_GRAPH_CYPHER` are currently only usable for filtered vector index search and cannot be used with the `algo` extension.

* * * *

**8\. Wrapping Up**

---------------------

LadybugDB's vector extension turns a graph database into a hybrid semantic + structural query engine. Here's what we covered:

-   **The HNSW algorithm** --- A two-layer navigable small world graph that gives you sub-linear approximate nearest-neighbor search. The upper layer provides coarse, long-range navigation; the lower layer provides fine-grained local search. Parameters like `mu`, `ml`, `pu`, `efc`, and `efs` let you tune the recall-speed trade-off for your specific workload.

-   **Basic vector search** --- `QUERY_VECTOR_INDEX(table, index, vec, K)` gives you the K nearest neighbors. You get back `node` (the full graph node) and `distance`, which you can feed into any Cypher pattern.

-   **Graph traversal from vector results** --- Chain `WITH node, distance` into `MATCH` patterns to follow edges from vector-search hits. This is the killer feature: semantic entry points into structural exploration, all in one query.

-   **Pre-filtering** --- Use `PROJECT_GRAPH` or `PROJECT_GRAPH_CYPHER` to restrict the HNSW search to a subset of nodes. Guarantees K results, avoids wasted work on filtered-out candidates.

-   **Post-filtering** --- Apply `WHERE` after the vector search for quick, informal filtering when you don't need guarantees.

-   **Arbitrary Cypher projected graphs** --- `PROJECT_GRAPH_CYPHER` lets you define the filter set with full Cypher, including relationship patterns, aggregations, and multi-hop logic.

The tight integration means you never leave Cypher. Embeddings live as node properties, the HNSW index is a first-class catalog object, and filtered search composes naturally with the full power of graph pattern matching. If you're building applications that need both semantic understanding and structured graph reasoning --- RAG pipelines, recommendation engines, knowledge graphs with natural-language queries --- this is a compelling way to do it without managing two separate systems.