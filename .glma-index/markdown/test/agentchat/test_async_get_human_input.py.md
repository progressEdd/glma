# test/agentchat/test_async_get_human_input.py

4 function(s): _test_async_get_human_input, test_async_get_human_input, _test_async_max_turn, test_async_max_turn.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _test_async_get_human_input | function |  |
| test_async_get_human_input | function |  |
| _test_async_max_turn | function |  |
| test_async_max_turn | function |  |

## Chunks

### _test_async_get_human_input (function, L19-L41)

> *Summary: This test verifies asynchronous human input handling by mocking the `UserProxyAgent`'s input method to return a predefined string. It initiates chats with an `AssistantAgent` and asserts that the mocked input function was called during the conversation flow.*


### test_async_get_human_input (function, L47-L50)

> *Summary: This asynchronous test function executes a core test case by calling an internal helper with provided credentials. It verifies the functionality of asynchronously retrieving human input within the system under test.*


### _test_async_max_turn (function, L53-L78)

> *Summary: This test simulates an asynchronous chat interaction where the user agent's input is mocked to always return a specific string. It initiates a conversation with a fixed maximum turn count and asserts that the resulting chat history contains a predetermined number of messages based on the mock behavior.*


### test_async_max_turn (function, L84-L87)

> *Summary: This asynchronous test function executes a core test case by calling an internal helper method with provided credentials. It verifies the system's behavior when reaching a predefined maximum number of turns in a chat interaction.*

