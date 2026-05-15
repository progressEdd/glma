# autogen/agentchat/contrib/rag/query_engine.py

1 class(es): RAGQueryEngine. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RAGQueryEngine | class |  |

## Chunks

### RAGQueryEngine (class, L16-L76)

> *Summary: Defines an interface for a Retrieval-Augmented Generation (RAG) engine that manages document ingestion and querying against a database. It requires methods to initialize the database with documents, add new documents, establish a connection, and execute string-based queries to retrieve results.*


### init_db (method, L22-L45, parent: RAGQueryEngine)

> *Summary: This method sets up the underlying database by ingesting new data. It accepts either a directory path or a sequence of file paths/URLs to populate the database and returns `True` on success or `False` upon failure.*


### add_docs (method, L47-L55, parent: RAGQueryEngine)

> *Summary: This method ingests new documents into the system's knowledge base. It accepts either a directory path or a sequence of file paths/URLs as input and performs no return value upon successful addition.*


### connect_db (method, L57-L66, parent: RAGQueryEngine)

> *Summary: Establishes a connection to a database using arbitrary positional and keyword arguments. It returns `True` upon successful connection or `False` if the connection fails.*


### query (method, L68-L76, parent: RAGQueryEngine)

> *Summary: This method converts an input string question into a structured database query, then executes it to return the resulting data as a string. It accepts the question along with any optional positional or keyword arguments for execution context.*

