# test/a2a/chats/test_tools.py

2 function(s): test_remote_tool_with_context, test_remote_tool_with_ask_user_target.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_remote_tool_with_context | function |  |
| test_remote_tool_with_ask_user_target | function |  |

## Chunks

### test_remote_tool_with_context (function, L22-L77)

> *Summary: This test verifies inter-agent communication by setting up a local and remote conversational agents connected via an HTTP server. It initiates a group chat, allowing the remote agent to modify shared state (`issue_count`) within the `ContextVariables`, which is then asserted in the final context data.*


### test_remote_tool_with_ask_user_target (function, L81-L122)

> *Summary: This test verifies interaction with a remote agent that requires user input when called via an A2A server setup. It initiates a chat, expecting the local user agent to handle the `AskUserTarget` by providing a mocked response, ultimately asserting the final conversation history reflects the successful exchange.*

