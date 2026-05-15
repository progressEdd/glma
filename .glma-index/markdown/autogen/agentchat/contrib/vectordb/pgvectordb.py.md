# autogen/agentchat/contrib/vectordb/pgvectordb.py

2 class(es): Collection, PGVectorDB. 28 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Collection | class |  |
| PGVectorDB | class |  |

## Chunks

### Collection (class, L29-L549)

> *Summary: Manages a PostgreSQL collection for vector storage, initializing with an embedding function and defining metadata like HNSW parameters. It supports CRUD operations (add, upsert, get, delete), querying via similarity search using various distance metrics, and schema management (create/delete).*


### __init__ (method, L43-L79, parent: Collection)

> *Summary: Initializes a vector database collection object, accepting a PostgreSQL client and configuration parameters like the collection name and embedding function. It automatically determines the required vector dimension by encoding a sample sentence using the provided or default embedding function.*


### set_collection_name (method, L81-L84, parent: Collection)

> *Summary: This method sanitizes an input string by replacing hyphens with underscores and then sets the internal collection name attribute to this modified value, returning the sanitized name.*


### add (method, L86-L128, parent: Collection)

> *Summary: Inserts data into the configured PostgreSQL collection using a dynamic SQL query based on provided inputs. It accepts document IDs, documents, and optional embeddings/metadatas to store in various combinations within the database.*


### upsert (method, L130-L192, parent: Collection)

> *Summary: This method inserts or updates records in the vector database collection based on provided IDs, documents, and optional embeddings/metadatas. It dynamically constructs and executes a PostgreSQL `INSERT ... ON CONFLICT DO UPDATE` query to handle various combinations of input data.*


### count (method, L194-L209, parent: Collection)

> *Summary: Retrieves the total document count from a specified collection within the vector database. It executes a `COUNT(*)` SQL query against the configured client and returns the resulting integer or `None` if conversion fails.*


### table_exists (method, L211-L232, parent: Collection)

> *Summary: Determines if a specified PostgreSQL table is present by querying the `information_schema.tables`. It accepts a table name string and returns a boolean indicating its existence in the database.*


### get (method, L234-L310, parent: Collection)

> *Summary: Retrieves documents from a specified collection by constructing and executing a PostgreSQL query based on optional ID lists, filtering criteria (`where`), field inclusions, limits, and offsets. It returns a list of `Document` objects populated with the fetched data or attempts to create the table if the initial query fails due to missing schema elements.*


### update (method, L312-L337, parent: Collection)

> *Summary: This method performs an upsert operation on the vector database collection, inserting new records or updating existing ones based on provided IDs. It accepts lists of document IDs, embeddings, metadata, and full documents to synchronize with the underlying PostgreSQL table.*


### euclidean_distance (method, L340-L351, parent: Collection)

> *Summary: Computes the Euclidean distance between two input vectors, represented as lists of floats. It utilizes NumPy's linear algebra norm function to return a single floating-point distance value.*


### cosine_distance (method, L354-L365, parent: Collection)

> *Summary: Computes the cosine similarity between two input vectors represented as lists of floats. It returns a single float value representing this similarity measure.*


### inner_product_distance (method, L368-L379, parent: Collection)

> *Summary: Computes the Euclidean distance between two input vectors, represented as lists of floats. It utilizes NumPy's linear algebra norm function to calculate the magnitude of the difference between the two arrays.*


### query (method, L381-L450, parent: Collection)

> *Summary: Executes a similarity search against a specified vector database collection using provided query texts and optional filtering parameters. It converts input text to embeddings, constructs a SQL query based on the requested distance type (e.g., cosine or euclidean), fetches matching documents, calculates the precise distance for each result, and returns structured query results.*


### convert_string_to_array (method, L453-L467, parent: Collection)

> *Summary: Parses a string containing space-separated numbers into a list of floats, stripping surrounding brackets if present. If the input is not a string, it returns the original input unchanged.*


### modify (method, L469-L483, parent: Collection)

> *Summary: Updates the metadata associated with a specific database collection. It takes optional collection and new metadata as input, executing an SQL `UPDATE` query against the PostgreSQL client to persist the changes.*


### delete (method, L485-L500, parent: Collection)

> *Summary: Removes specified documents from a vector database collection by executing a SQL `DELETE` query against the table identified by the instance's name. It accepts a list of document IDs and an optional collection name to target the deletion operation.*


### delete_collection (method, L502-L515, parent: Collection)

> *Summary: Removes an entire vector database collection by executing a `DROP TABLE` SQL command against the configured PostgreSQL client. It accepts an optional collection name to specify which table should be deleted.*


### create_collection (method, L517-L549, parent: Collection)

> *Summary: This method initializes a new PostgreSQL collection by executing SQL to create a table with fields for documents, metadata, and vector embeddings. It configures the table with three HNSW indexes (L2, cosine, and inner product) based on provided or default dimension settings.*


### PGVectorDB (class, L553-L927)

> *Summary: This class implements a vector database interface using PostgreSQL with the PGVector extension as its backend. It initializes connections via various parameters and manages collections, allowing users to insert, update, delete, and retrieve documents based on text queries or IDs, utilizing an optional embedding function for vector generation.*


### __init__ (method, L556-L612, parent: PGVectorDB)

> *Summary: Initializes a PostgreSQL vector database client by establishing a connection using provided credentials or a connection string. It configures the embedding function (defaulting to SentenceTransformer) and sets up database metadata, preparing the system for vector operations.*


### establish_connection (method, L614-L689, parent: PGVectorDB)

> *Summary: This method establishes a connection to a PostgreSQL database, accepting an existing connection object or various parameters like a full connection string, host/port details, and credentials. It returns the active `psycopg.Connection` object after ensuring the `vector` extension is created on the database.*


### create_collection (method, L691-L752, parent: PGVectorDB)

> *Summary: This method manages the creation or retrieval of a vector database collection based on provided parameters. It accepts a `collection_name` and boolean flags for `overwrite` and `get_or_create`, returning the corresponding `Collection` object after ensuring its existence according to the specified logic.*


### get_collection (method, L754-L778, parent: PGVectorDB)

> *Summary: Retrieves a specific vector database collection by name or defaults to the currently active one if no name is provided. It ensures that if a named collection is requested and not currently active, it initializes and sets it as the new active collection.*


### delete_collection (method, L780-L795, parent: PGVectorDB)

> *Summary: Removes a specified vector database collection by name, either through the currently active connection or by fetching it directly. It also resets the active collection reference if the deleted collection was the one currently in use.*


### _batch_insert (method, L797-L814, parent: PGVectorDB)

> *Summary: This method inserts or updates data into a vector database collection in batches to optimize performance. It accepts lists of documents, IDs, embeddings, and optional metadata, processing them iteratively up to the defined maximum batch size.*


### insert_docs (method, L816-L848, parent: PGVectorDB)

> *Summary: This method inserts a list of document objects into the configured vector database collection. It validates that each document has content and an ID, optionally accepts pre-computed embeddings, and uses batch insertion to persist the data with specified upsert behavior.*


### update_docs (method, L850-L860, parent: PGVectorDB)

> *Summary: Inserts or updates a provided list of `Document` objects within a specified vector database collection. It utilizes an upsert mechanism to ensure existing documents are modified rather than duplicated.*


### delete_docs (method, L862-L874, parent: PGVectorDB)

> *Summary: Removes specified documents from a vector database collection using a list of document IDs. It accepts an optional collection name to target the deletion operation.*


### retrieve_docs (method, L876-L906, parent: PGVectorDB)

> *Summary: Fetches relevant documents from a vector database collection using a list of text queries. It accepts optional parameters to specify the collection name, maximum number of results, and a distance score threshold for filtering. The function returns structured query results containing the retrieved documents and their associated distances.*


### get_docs_by_ids (method, L908-L927, parent: PGVectorDB)

> *Summary: Retrieves documents from a specified vector database collection using provided IDs or all documents if no IDs are given. It returns a list of `Document` objects, optionally filtering which fields are returned based on the `include` parameter.*

