# autogen/llm_clients/models/unified_response.py

1 class(es): UnifiedResponse. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| UnifiedResponse | class |  |

## Chunks

### UnifiedResponse (class, L17-L83)

> *Summary: This class provides a standardized, provider-agnostic structure for encapsulating responses from various LLMs. It accepts inputs like message content and metadata to output a unified object containing text, usage metrics, cost, and provider-specific details. Key behaviors include providing convenient properties to aggregate text and reasoning across all contained messages.*


### text (method, L52-L56, parent: UnifiedResponse)

> *Summary: Retrieves the concatenated string content from all contained messages if any exist; otherwise, it returns an empty string. This method aggregates text from a collection of message objects into a single output string.*


### reasoning (method, L59-L61, parent: UnifiedResponse)

> *Summary: Retrieves a flattened list of all `ReasoningContent` objects present across every message within the object's history. This method aggregates and returns these reasoning blocks for quick access.*


### get_content_by_type (method, L63-L74, parent: UnifiedResponse)

> *Summary: Retrieves a list of all content blocks matching a specified `content_type` from every message within the object's collection. It iterates through all messages and aggregates any blocks that match the provided type string.*


### is_standard_status (method, L76-L83, parent: UnifiedResponse)

> *Summary: Determines if the response's current status matches one of the predefined standard values (`completed`, `in_progress`, `failed`). It returns `True` only if a status exists and is within the set of recognized standards, otherwise it returns `False`.*

