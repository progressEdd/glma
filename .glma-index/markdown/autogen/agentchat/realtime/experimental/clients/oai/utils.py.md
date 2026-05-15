# autogen/agentchat/realtime/experimental/clients/oai/utils.py

1 function(s): parse_oai_message.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| parse_oai_message | function |  |

## Chunks

### parse_oai_message (function, L21-L48)

> *Summary: This function transforms a raw dictionary received from the OpenAI Realtime API into a specific `RealtimeEvent` object based on its `"type"` field. It handles various event types, such as session creation/updates, audio data deltas, and function call completion, returning the appropriate structured event instance.*

