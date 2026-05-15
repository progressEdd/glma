# test/a2a/chats/test_group_chat.py

2 function(s): test_round_robin_pattern, test_handoffs.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_round_robin_pattern | function |  |
| test_handoffs | function |  |

## Chunks

### test_round_robin_pattern (function, L20-L63)

> *Summary: This test verifies a round-robin communication pattern by setting up local and remote agents connected via an ASGI application. It initiates a group chat with the `RoundRobinPattern` to ensure messages are distributed sequentially among all participating agents, asserting the final message history reflects this rotation.*


### test_handoffs (function, L67-L113)

> *Summary: Sets up a simulated group chat environment by connecting a local agent to two remote agents via HTTP services. It then initiates a conversation and asserts that the resulting chat history correctly reflects the handoffs between the participating agents.*

