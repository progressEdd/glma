# test/agentchat/test_function_call_groupchat.py

4 function(s): test_function_call_groupchat, test_async_function_call_groupchat, test_group_chat_tool_returns_list, test_no_function_map.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_function_call_groupchat | function |  |
| test_async_function_call_groupchat | function |  |
| test_group_chat_tool_returns_list | function |  |
| test_no_function_map | function |  |

## Chunks

### test_function_call_groupchat (function, L40-L97)

> *Summary: This test sets up a multi-agent group chat involving an executor, a player agent capable of calling functions, and an observer. It verifies that the system correctly executes function calls within the chat flow while also asserting that the `GroupChatManager` rejects configurations containing tool definitions.*


### test_async_function_call_groupchat (function, L102-L142)

> *Summary: This test verifies asynchronous function calling within a group chat simulation by setting up two agents and one with a mocked function. It initiates a conversation instructing the system to call the mocked function and asserts that the function was indeed invoked during the chat process.*


### test_group_chat_tool_returns_list (function, L146-L182)

> *Summary: This integration test verifies that a group chat successfully handles a tool returning a `list[int]` within the AutoPattern framework. It initiates a conversation where an agent calls a function providing `[5, 3, 10]`, asserting that the resulting chat history contains the serialized list content without raising a `TypeError`.*


### test_no_function_map (function, L185-L211)

> *Summary: This test verifies that a `GroupChat` fails when an assistant proposes a function call (`get_random_number`) but none of the participating agents have a defined mapping for it. It asserts that a `ValueError` is raised, specifically indicating the missing function map.*

