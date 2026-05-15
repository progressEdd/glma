# autogen/llm_clients/models/unified_message.py

1 function(s): normalize_role. 2 class(es): UserRoleEnum, UnifiedMessage. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| UserRoleEnum | class |  |
| normalize_role | function |  |
| UnifiedMessage | class |  |

## Chunks

### UserRoleEnum (class, L23-L29)

> *Summary: Defines a set of standardized string constants representing distinct roles within a conversation or message exchange. It provides typed enumeration for `USER`, `ASSISTANT`, `SYSTEM`, and `TOOL` roles.*


### normalize_role (function, L36-L69)

> *Summary: Converts an input role string into a type-safe `UserRoleEnum` if it matches predefined values ("user", "assistant", etc.), otherwise returns the original string to support custom or unknown roles. It defaults to `ASSISTANT` if no role is provided.*


### UnifiedMessage (class, L72-L145)

> *Summary: Represents a standardized message structure capable of holding multimodal content like text, images, and tool interactions, along with metadata. It provides methods to extract specific data types from its `content` list, such as aggregated text, reasoning blocks, or citations, based on the defined role and block types.*


### get_text (method, L96-L107, parent: UnifiedMessage)

> *Summary: Aggregates all textual content from the message's constituent blocks into a single string. It iterates over `self.content`, calls `get_text()` on each block, and joins any non-empty results with spaces.*


### get_reasoning (method, L109-L111, parent: UnifiedMessage)

> *Summary: Retrieves all structured reasoning content from the message's internal content list. It filters the input to return only objects of type `ReasoningContent`.*


### get_citations (method, L113-L115, parent: UnifiedMessage)

> *Summary: Retrieves all citation objects from the message's content by filtering for instances of `CitationContent`. It returns a list containing only these extracted citation elements.*


### get_tool_calls (method, L117-L119, parent: UnifiedMessage)

> *Summary: Retrieves all `ToolCallContent` objects from the message's content list. It filters the existing content to return only instances representing tool invocations.*


### get_content_by_type (method, L121-L132, parent: UnifiedMessage)

> *Summary: Filters the instance's content list to return all `BaseContent` objects matching a specified `content_type` string. It takes one string argument and outputs a list of filtered content blocks.*


### is_standard_role (method, L134-L145, parent: UnifiedMessage)

> *Summary: Determines if the message's assigned role is one of the predefined standard types (user, assistant, system, tool). It checks both against an enumeration type and a list derived from that enumeration to return a boolean indicating standardization.*

