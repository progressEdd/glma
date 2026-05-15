# autogen/agents/experimental/document_agent/docling_doc_ingest_agent.py

1 class(es): DoclingDocIngestAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DoclingDocIngestAgent | class |  |

## Chunks

### DoclingDocIngestAgent (class, L32-L113)

> *Summary: This agent is designed to ingest documents by utilizing the `docling_parse_docs` tool. It takes a list of document paths/URLs as input and processes them into markdown files, subsequently adding these parsed documents to a specified ChromaDB query engine for retrieval. On success or failure, it reports back to designated successor agents.*


### __init__ (method, L35-L113, parent: DoclingDocIngestAgent)

> *Summary: Initializes an agent responsible for ingesting documents by parsing input files into Markdown and adding them to a specified vector database. It accepts configurations for LLM settings, document paths, and a query engine, returning success or error messages based on the ingestion task's outcome.*

