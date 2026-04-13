---
file_path: summarize/providers.py
language: python
last_indexed: 2026-04-13T20:15:24.287736+00:00
chunk_count: 8
content_hash: 8e1e2835425efcd41188bce6dffd10edf4a6d802f5976519fe4c99dc14763292
---

# summarize/providers.py

## Summary

Defines a common interface and multiple provider implementations (OpenAI-compatible and Pi) for generating natural language summaries of source code. It handles API integration, dependency validation, and prompt management to transform code snippets and metadata into concise behavioral descriptions.

**AI Chunk Summaries:**
- **SummarizerProvider**: Defines a structural protocol for code summarization services. It requires a `summarize` method that takes source code and metadata as input to return a natural language description of the code's behavior.
- **summarize**: Generates a natural language summary describing the purpose and behavior of a provided code snippet. It takes source code and associated metadata (context) as input and returns a string summary.
- **OpenAICompatibleProvider**: Provides a wrapper for OpenAI-compatible APIs (e.g., Ollama, LM Studio) to generate code summaries. It takes source code and metadata as input and returns a concise natural language summary based on a predefined system prompt.
- **__init__**: Initializes an OpenAI-compatible client using a provided `base_url` and `model` name. It validates the presence of the `openai` package at runtime, raising an `ImportError` with installation instructions if missing.
- **summarize**: Generates a natural language summary of a code snippet by sending the source code and its metadata to an OpenAI-compatible API. It returns the stripped content of the first chat completion response based on a predefined system prompt.
- **PiProvider**: Provides code summarization by interfacing with the `pi` SDK's `Agent`. It takes source code and metadata as input and returns a concise natural language summary generated via the Pi API.
- **__init__**: Initializes the Pi summarization provider by setting the target model and verifying that the `pi` SDK is installed. It raises an `ImportError` if the required environment is not available.
- **summarize**: Generates a concise natural language summary of a code snippet by sending the source code and its metadata to the Pi API. It returns a stripped string containing the AI-generated description of the code's purpose and behavior.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| SummarizerProvider | class | L6-L23 |  |
| OpenAICompatibleProvider | class | L26-L79 |  |
| PiProvider | class | L82-L126 |  |

## Chunks

### SummarizerProvider (class, L6-L23)

> *Summary: Defines a structural protocol for code summarization services. It requires a `summarize` method that takes source code and metadata as input to return a natural language description of the code's behavior.*

> **Calls:** ? (Protocol) (INFERRED), ? (pi) (INFERRED), ? (pi) (INFERRED), ? (openai) (INFERRED), ? (typing) (INFERRED)

### summarize (method, L13-L23)

> *Summary: Generates a natural language summary describing the purpose and behavior of a provided code snippet. It takes source code and associated metadata (context) as input and returns a string summary.*


### OpenAICompatibleProvider (class, L26-L79)

> *Summary: Provides a wrapper for OpenAI-compatible APIs (e.g., Ollama, LM Studio) to generate code summaries. It takes source code and metadata as input and returns a concise natural language summary based on a predefined system prompt.*


### __init__ (method, L39-L57)

> *Summary: Initializes an OpenAI-compatible client using a provided `base_url` and `model` name. It validates the presence of the `openai` package at runtime, raising an `ImportError` with installation instructions if missing.*

> **Calls:** ? (OpenAI) (INFERRED), ? (ImportError) (INFERRED)

### summarize (method, L59-L79)

> *Summary: Generates a natural language summary of a code snippet by sending the source code and its metadata to an OpenAI-compatible API. It returns the stripped content of the first chat completion response based on a predefined system prompt.*

> **Calls:** ? (response.choices[0].message.content.strip) (INFERRED), ? (self._client.chat.completions.create) (INFERRED)

### PiProvider (class, L82-L126)

> *Summary: Provides code summarization by interfacing with the `pi` SDK's `Agent`. It takes source code and metadata as input and returns a concise natural language summary generated via the Pi API.*


### __init__ (method, L89-L105)

> *Summary: Initializes the Pi summarization provider by setting the target model and verifying that the `pi` SDK is installed. It raises an `ImportError` if the required environment is not available.*

> **Calls:** ? (ImportError) (INFERRED)

### summarize (method, L107-L126)

> *Summary: Generates a concise natural language summary of a code snippet by sending the source code and its metadata to the Pi API. It returns a stripped string containing the AI-generated description of the code's purpose and behavior.*

> **Calls:** ? (response.strip) (INFERRED), ? (agent.run) (INFERRED), ? (Agent) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| __init__ | ? (OpenAI) | INFERRED | L56 |
| __init__ | ? (ImportError) | INFERRED | L52 |
| summarize | ? (response.choices[0].message.content.strip) | INFERRED | L79 |
| summarize | ? (self._client.chat.completions.create) | INFERRED | L70 |
| __init__ | ? (ImportError) | INFERRED | L101 |
| summarize | ? (response.strip) | INFERRED | L126 |
| summarize | ? (agent.run) | INFERRED | L125 |
| summarize | ? (Agent) | INFERRED | L124 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| pi | INFERRED |
| pi | INFERRED |
| openai | INFERRED |
| typing | INFERRED |

### Inherits

| Class | Base | Confidence |
| ----- | ---- | ---------- |
| SummarizerProvider | SummarizerProvider | INFERRED |
