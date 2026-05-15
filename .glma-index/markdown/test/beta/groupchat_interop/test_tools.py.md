# test/beta/groupchat_interop/test_tools.py

3 function(s): test_remote_tool_with_context, test_tool_agent_handoff, test_user_target_handoff.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_remote_tool_with_context | function |  |
| test_tool_agent_handoff | function |  |
| test_user_target_handoff | function |  |

## Chunks

### test_remote_tool_with_context (function, L20-L60)

> *Summary: This test verifies that an agent correctly interacts with a remote tool while maintaining shared state via `ContextVariables`. It initiates a group chat simulation, asserting the final message history and confirming the expected update to the shared `issue_count` context variable.*


### test_tool_agent_handoff (function, L64-L106)

> *Summary: This test verifies the handoff mechanism within a group chat simulation. It sets up multiple agents and a round-robin pattern to initiate a conversation, asserting that the resulting chat history correctly reflects tool execution and subsequent message exchanges between agents.*


### test_user_target_handoff (function, L110-L154)

> *Summary: This test verifies the handoff mechanism within a group chat simulation. It sets up multiple agents and uses a round-robin pattern to initiate a conversation, asserting that specific agents take turns speaking and one agent successfully triggers a tool call resulting in a targeted response.*

