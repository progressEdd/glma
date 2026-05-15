# test/agentchat/contrib/vectordb/test_pgvectordb.py

2 function(s): is_postgres_accessible, test_pgvector.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| is_postgres_accessible | function |  |
| test_pgvector | function |  |

## Chunks

### is_postgres_accessible (function, L24-L30)

> *Summary: Checks for PostgreSQL accessibility by attempting to establish and immediately close a connection to the local `postgres` database. Returns `True` if the connection succeeds, otherwise returns `False`.*


### test_pgvector (function, L38-L140)

> *Summary: This test suite verifies the functionality of a PostgreSQL vector database wrapper by testing collection creation and management using various connection methods (connection string, `psycopg` object, and explicit parameters). It further validates core operations including document insertion, updating, deletion, retrieval via similarity search, and fetching documents by ID.*

