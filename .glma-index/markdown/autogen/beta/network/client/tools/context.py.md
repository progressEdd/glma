# autogen/beta/network/client/tools/context.py

2 function(s): _excerpt, make_context_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _excerpt | function |  |
| make_context_tool | function |  |

## Chunks

### _excerpt (function, L33-L39)

> *Summary: Extracts a string excerpt from an envelope's event data, truncating it to `max_chars` if necessary and appending "..." for brevity. It returns the original text if it is within the limit or empty otherwise.*


### make_context_tool (function, L42-L143)

> *Summary: Creates a callable tool that allows an agent to retrieve past content by either searching text within a channel or knowledge base, or retrieving the most recent messages from a specific speaker in a given channel. It accepts parameters defining the action type ("search" or "quote"), query/speaker details, and scope constraints.*

