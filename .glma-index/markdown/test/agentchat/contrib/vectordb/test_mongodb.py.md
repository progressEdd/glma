# test/agentchat/contrib/vectordb/test_mongodb.py

22 function(s): is_mongodb_accessible, _wait_for_predicate, _delete_search_indexes, _empty_collections_and_delete_indexes, db, example_documents, db_with_indexed_clxn, collection_name, test_create_collection, test_get_collection and 12 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| is_mongodb_accessible | function |  |
| _wait_for_predicate | function |  |
| _delete_search_indexes | function |  |
| _empty_collections_and_delete_indexes | function |  |
| db | function |  |
| example_documents | function |  |
| db_with_indexed_clxn | function |  |
| collection_name | function |  |
| test_create_collection | function |  |
| test_get_collection | function |  |
| test_delete_collection | function |  |
| test_insert_docs | function |  |
| test_update_docs | function |  |
| test_delete_docs | function |  |
| test_get_docs_by_ids | function |  |
| test_retrieve_docs_empty | function |  |
| test_retrieve_docs_populated_db_empty_query | function |  |
| test_retrieve_docs | function |  |
| test_retrieve_docs_with_embedding | function |  |
| test_retrieve_docs_multiple_queries | function |  |
| test_retrieve_docs_with_threshold | function |  |
| test_wait_until_document_ready | function |  |

## Chunks

### is_mongodb_accessible (function, L39-L46)

> *Summary: Checks connectivity to a MongoDB instance using the configured URI by attempting a `ping` command with a short timeout. Returns `True` if the connection is successful, otherwise returns `False`.*


### _wait_for_predicate (function, L49-L65)

> *Summary: This utility blocks execution until a provided boolean function returns `True`, raising a `TimeoutError` if the condition is not met within the specified time limit. It repeatedly checks the predicate at defined intervals, using an initial start time to enforce the timeout constraint.*


### _delete_search_indexes (function, L68-L79)

> *Summary: Iterates through and drops every search index present on a given MongoDB collection, optionally waiting for the deletion process to complete before returning.*


### _empty_collections_and_delete_indexes (function, L82-L92)

> *Summary: This utility clears specified MongoDB collections, or all collections if none are provided, by first deleting any existing indexes and then dropping the entire collection. It accepts a database abstraction object and an optional list of collection names to target.*


### db (function, L96-L107)

> *Summary: Establishes and tears down a MongoDB connection for testing purposes. It initializes an `MongoDBAtlasVectorDB` instance, yielding it to the caller while ensuring collections and indexes are cleaned up before and after use.*


### example_documents (function, L111-L118)

> *Summary: Provides a list of sample `Document` objects for testing purposes. These documents include mixed data types (integers and strings) in their IDs to test ID handling within the vector database implementation.*


### db_with_indexed_clxn (function, L122-L134)

> *Summary: This generator sets up a MongoDB Atlas VectorDB instance for testing by creating and populating a specified collection with necessary indexes. It yields the initialized `VectorDB` object and its corresponding database collection before cleaning up the resources upon completion.*


### collection_name (function, L141-L147)

> *Summary: Generates a unique MongoDB collection name by randomly selecting an ID between 0 and 100, ensuring it hasn't been used before in the cache, and prepending a predefined prefix. The function returns a string representing the fully qualified collection identifier.*


### test_create_collection (function, L152-L178)

> *Summary: This test verifies the `create_collection` functionality by asserting correct behavior across four scenarios: creating a new collection, overwriting an existing one, returning the existing collection when not overwriting, and raising a `ValueError` under specific non-creation conditions. It uses a database object (`db`) and a string name to simulate these interactions.*


### test_get_collection (function, L183-L193)

> *Summary: This test verifies the functionality of retrieving a MongoDB collection object from a database instance. It asserts that attempting to get a collection without specifying one raises an error, and then confirms that creating and subsequently fetching a named collection returns the expected `Collection` type with the correct name.*


### test_delete_collection (function, L198-L203)

> *Summary: This test verifies the functionality of deleting a MongoDB collection. It asserts that a specified collection can be created and subsequently removed from the database's list of collections.*


### test_insert_docs (function, L208-L230)

> *Summary: This test verifies the `insert_docs` functionality by first asserting that it fails without a specified collection. It then tests successful insertion with upsert enabled and confirms that documents are correctly added to a newly created collection, validating field structure and embedding dimensions.*


### test_update_docs (function, L235-L267)

> *Summary: This test verifies the `update_docs` functionality against a MongoDB instance, ensuring documents are correctly inserted (with upsert), updated by ID, and that attempting to insert without `upsert=True` results in no change. It confirms schema integrity, including the presence of an `embedding` field with correct dimensions.*


### test_delete_docs (function, L272-L279)

> *Summary: This test verifies document deletion by first inserting a set of example documents into a MongoDB collection. It then deletes specific documents identified by IDs `1` and `"1"`, asserting that only the remaining documents (those with IDs `2` and `"2"`) are present in the collection afterward.*


### test_get_docs_by_ids (function, L284-L306)

> *Summary: This test verifies the retrieval of documents from a MongoDB database using specific IDs. It asserts correct document fetching based on whether an `include` parameter is provided and handles edge cases like empty or `None` ID lists.*


### test_retrieve_docs_empty (function, L311-L313)

> *Summary: Verifies that retrieving documents from a MongoDB collection returns an empty list when no matching results are found for the given query. It asserts the output of `db.retrieve_docs` against an expected empty list.*


### test_retrieve_docs_populated_db_empty_query (function, L318-L323)

> *Summary: When provided with an empty query list against a populated MongoDB database, the function asserts that the retrieval method returns an empty list of documents. This verifies correct behavior when no search criteria are supplied to the vector database retriever.*


### test_retrieve_docs (function, L328-L348)

> *Summary: This test verifies the functionality of Atlas Vector Search by first inserting sample documents into a MongoDB collection. It then repeatedly queries the database until it successfully retrieves the expected number of closest matching documents, asserting that the returned IDs match predefined values and do not contain embedding data.*


### test_retrieve_docs_with_embedding (function, L353-L373)

> *Summary: This test verifies Atlas Vector Search functionality by first inserting sample documents into a MongoDB collection. It then waits until the retrieval function successfully returns the expected number of closest matching documents based on an embedding query, finally asserting that the returned results include the correct document IDs and their associated embeddings.*


### test_retrieve_docs_multiple_queries (function, L378-L397)

> *Summary: This test verifies that a vector database correctly retrieves the specified number of closest documents for multiple input queries. It inserts sample data and then asserts that the retrieval function returns an array of results, where each result set contains exactly two matching documents corresponding to its respective query.*


### test_retrieve_docs_with_threshold (function, L402-L420)

> *Summary: This test verifies that a vector database correctly retrieves documents based on a specified similarity threshold. It inserts sample data, then calls `retrieve_docs` with a threshold of $0.3$, asserting that exactly one result is returned and its associated score meets or exceeds $0.7$.*


### test_wait_until_document_ready (function, L425-L440)

> *Summary: This test verifies that a MongoDB vector store correctly handles document readiness after insertion. It initializes the `MongoDBAtlasVectorDB`, inserts provided documents, and then asserts successful retrieval using sample queries before cleaning up the collection.*

