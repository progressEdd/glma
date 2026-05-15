# autogen/beta/knowledge/bootstrap.py

2 class(es): StoreBootstrap, DefaultBootstrap. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| StoreBootstrap | class |  |
| DefaultBootstrap | class |  |

## Chunks

### StoreBootstrap (class, L12-L21)

> *Summary: Defines an asynchronous protocol for initializing a knowledge store with a starting structure. It is intended to be called only on the first execution when an agent starts using a specific store instance.*


### bootstrap (method, L19-L21, parent: StoreBootstrap)

> *Summary: Initializes the knowledge store by creating its foundational structure using a provided `KnowledgeStore` instance and an actor's name. This method sets up the necessary starting state for knowledge management within the system.*


### DefaultBootstrap (class, L24-L76)

> *Summary: This class initializes a standard knowledge store structure, creating specific `SKILL.md` files in various directories like `/log`, `/artifacts`, and `/memory`. It configures the root introduction to either instruct the LLM to use a `knowledge` tool or state that no direct tool access is available, based on an input flag.*


### __init__ (method, L34-L35, parent: DefaultBootstrap)

> *Summary: Initializes the object, optionally setting a boolean flag to control whether tool mentions are included in subsequent operations. This configuration dictates behavior for the instance throughout its lifecycle.*


### bootstrap (method, L37-L76, parent: DefaultBootstrap)

> *Summary: Initializes the knowledge store by writing foundational documentation files to specific directories within it. It sets up introductory text based on whether a tool is available and populates metadata for logs, artifacts, and memory areas.*

