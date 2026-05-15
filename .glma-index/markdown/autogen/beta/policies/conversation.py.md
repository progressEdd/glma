# autogen/beta/policies/conversation.py

1 class(es): ConversationPolicy. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ConversationPolicy | class |  |

## Chunks

### ConversationPolicy (class, L33-L50)

> *Summary: This policy filters a stream of events to ensure only conversation and tool-related events are passed to the LLM. It takes lists of prompts and events, returning the original prompts alongside a subset of events containing only specified conversation types.*


### apply (method, L43-L50, parent: ConversationPolicy)

> *Summary: Filters a list of incoming events to retain only those matching predefined conversation types. It returns the original prompts alongside the subset of relevant events.*

