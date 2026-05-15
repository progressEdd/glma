# autogen/beta/config/client.py

1 class(es): LLMClient. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LLMClient | class |  |

## Chunks

### LLMClient (class, L17-L26)

> *Summary: Defines a protocol for an asynchronous client capable of interacting with language models. It accepts messages, conversation context, optional tools and response schemas, and a serializer to return a `ModelResponse`.*


### __call__ (method, L18-L26, parent: LLMClient)

> *Summary: This asynchronous method processes a sequence of messages and conversation context, utilizing provided tools and serialization logic. It returns a `ModelResponse` after interacting with the underlying model based on the inputs.*

