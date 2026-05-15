# test/agentchat/contrib/capabilities/test_transform_messages.py

1 function(s): test_transform_messages_capability.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_transform_messages_capability | function |  |

## Chunks

### test_transform_messages_capability (function, L17-L57)

> *Summary: This test verifies that message transformation capabilities correctly handle extremely long chat histories. It initializes an agent and applies message limiters to simulate a large context, then attempts to initiate a new chat to ensure the system doesn't crash due to excessive input size.*

