# test/agentchat/contrib/vectordb/test_couchbase.py

4 function(s): _empty_collections_and_delete_indexes, db, collection_name, test_couchbase.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _empty_collections_and_delete_indexes | function |  |
| db | function |  |
| collection_name | function |  |
| test_couchbase | function |  |

## Chunks

### _empty_collections_and_delete_indexes (function, L50-L65)

> *Summary: This function clears a specified scope within a Couchbase bucket by iterating through all collections and dropping each one. It takes a cluster object, bucket name, and scope name as input to perform the cleanup operation.*


### db (function, L69-L88)

> *Summary: This generator establishes a connection to Couchbase if not running on macOS or Windows. It initializes and yields a `CouchbaseVectorDB` instance after ensuring the target bucket is empty by deleting existing collections and indexes.*


### collection_name (function, L95-L100)

> *Summary: Generates a unique collection identifier by randomly selecting an integer between 0 and 100, ensuring it hasn't been used before in the cache. It then returns this ID prefixed with `COUCHBASE_COLLECTION_`.*


### test_couchbase (function, L109-L170)

> *Summary: This test suite verifies Couchbase database operations by asserting expected behaviors for collection creation, document upserting, deletion, insertion, and updates. It uses a provided `db` object to execute CRUD operations against a specified collection name, checking for exceptions where appropriate.*

