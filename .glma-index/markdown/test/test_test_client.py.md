# test/test_test_client.py

5 function(s): test_mock_async_client, test_mock_sync_client, test_mock_chat, test_mock_async_chat, test_tool_call.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_mock_async_client | function |  |
| test_mock_sync_client | function |  |
| test_mock_chat | function |  |
| test_mock_async_chat | function |  |
| test_tool_call | function |  |

## Chunks

### test_mock_async_client (function, L16-L41)

> *Summary: This test verifies the interaction flow when an agent receives a message from a mocked asynchronous client. It asserts that the agent correctly records the incoming user message and sends back its predefined response to the mock client.*


### test_mock_sync_client (function, L44-L69)

> *Summary: This test verifies the interaction flow when an agent receives a message from a mocked client. It asserts that the agent correctly logs the incoming user message and sends the expected response back to the mock client via its `receive` method.*


### test_mock_chat (function, L72-L95)

> *Summary: This test verifies the chat initiation process between two agents using mocked configurations. It asserts that the resulting `chat_history` correctly captures a sequence of messages exchanged during the simulated conversation turns.*


### test_mock_async_chat (function, L99-L122)

> *Summary: This test verifies the asynchronous chat initiation between two agents using mocked configurations. It asserts that the resulting `chat_history` correctly captures the sequence of messages exchanged during a limited-turn conversation.*


### test_tool_call (function, L125-L160)

> *Summary: This test verifies that two agents correctly execute a registered tool call when initiated by one agent to the other. It asserts that the mocked function is called exactly twice with the specified date string, confirming proper tool invocation handling.*

