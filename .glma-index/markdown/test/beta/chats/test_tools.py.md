# test/beta/chats/test_tools.py

1 function(s): test_remote_tool_with_context.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_remote_tool_with_context | function |  |

## Chunks

### test_remote_tool_with_context (function, L19-L59)

> *Summary: This test verifies that an agent correctly utilizes and updates shared state within a group chat simulation. It sets up two agents, one of which uses a tool to increment a `context.variables["issue_count"]`, then runs the chat and asserts the final context reflects this change.*

