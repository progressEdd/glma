# autogen/llm_clients/client_v2.py

1 class(es): ModelClientV2. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ModelClientV2 | class |  |

## Chunks

### ModelClientV2 (class, L18-L122)

> *Summary: Defines a protocol for next-generation LLM clients that accepts request parameters and returns a `UnifiedResponse` containing rich, provider-agnostic content blocks. It also provides a backward-compatible method to generate legacy responses while offering utility methods to calculate cost and extract usage from the unified output.*


### create (method, L67-L76, parent: ModelClientV2)

> *Summary: This method generates a completion by accepting request parameters like messages and model configuration. It returns a `UnifiedResponse` object that encapsulates the results while maintaining support for various provider-specific features.*


### create_v1_compatible (method, L78-L97, parent: ModelClientV2)

> *Summary: Provides backward compatibility by taking request parameters and transforming them into a `ChatCompletionExtended` response object. This conversion flattens rich content from the modern unified format to a legacy structure, potentially losing advanced information like citations.*


### cost (method, L99-L109, parent: ModelClientV2)

> *Summary: Calculates the monetary cost of an API interaction by taking a `UnifiedResponse` object as input and returning the total expense in USD. This method is intended to be moved to private once all clients adopt V2.*


### get_usage (method, L112-L122, parent: ModelClientV2)

> *Summary: This method extracts usage statistics from a `UnifiedResponse` object, returning a dictionary containing specific usage metrics defined by internal constants. It processes the response to provide structured data about resource consumption.*

