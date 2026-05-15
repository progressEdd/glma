# autogen/agents/experimental/document_agent/document_agent.py

3 class(es): DocumentTask, DocumentTriageAgent, DocAgent. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DocumentTask | class |  |
| DocumentTriageAgent | class |  |
| DocAgent | class |  |

## Chunks

### DocumentTask (class, L92-L120)

> *Summary: This model defines a structured representation for task decisions, holding lists of documents to ingest and queries to execute. It provides a `format` method that serializes these inputs into a human-readable string suitable for a TaskManager.*


### format (method, L98-L120, parent: DocumentTask)

> *Summary: Generates a formatted string representation of the agent's tasks for consumption by a `TaskManager`. It aggregates paths/URLs from ingested documents and queries into a numbered list, returning a summary message if no tasks are present.*


### DocumentTriageAgent (class, L123-L143)

> *Summary: This agent analyzes user requests to determine the appropriate task type. It takes an optional LLM configuration and outputs a structured `DocumentTask` object containing necessary ingestions (files/URLs) and associated RAG queries derived from the input.*


### __init__ (method, L126-L143, parent: DocumentTriageAgent)

> *Summary: Initializes an agent designed for document triage by setting a specific system prompt that instructs it to classify tasks and structure responses using a `DocumentTask` format. It configures the underlying LLM with this structured response requirement and sets its operational mode to never require human input.*


### DocAgent (class, L147-L643)

> *Summary: This class orchestrates document ingestion and querying by internally managing a group chat among specialized agents (Triage, Task Manager, Parser, Ingestion, Query, Summary, Error). It accepts initial tasks via `initiate_tasks` to queue documents for processing and queries to run against the configured RAG engine. The primary output is a summary of completed actions or answers derived from the agent workflow.*


### __init__ (method, L153-L557, parent: DocAgent)

> *Summary: Initializes a complex agent system responsible for document processing, orchestrating specialized sub-agents like Triage, Task Manager, Parser, and Query agents. It accepts configurations for LLMs, data paths, and query engines to manage the workflow of ingesting documents and answering user queries via RAG.*


### generate_inner_group_chat_reply (method, L559-L619, parent: DocAgent)

> *Summary: Generates a response for an inner group chat by orchestrating several specialized agents (triage, task manager, data ingestion, etc.) using a defined pattern and context variables. It takes input messages and agent configuration to produce a termination status and the final summarized reply from the group discussion.*


### _get_document_input_message (method, L621-L643, parent: DocAgent)

> *Summary: Extracts and validates the primary input content for the agent, accepting either a raw string or the "content" field from the last dictionary in a list of messages. It returns the extracted string content or raises an error if the provided `messages` format is invalid.*

