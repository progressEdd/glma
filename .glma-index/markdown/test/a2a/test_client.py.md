# test/a2a/test_client.py

10 function(s): test_answer_with_str, test_answer_with_text_part, test_answer_with_dict, test_build_agent_from_card, test_streaming_raises_when_no_task_started, test_polling_raises_when_no_task_started, test_streaming_raises_when_no_task_and_no_agent_card, test_polling_raises_when_no_task_and_no_agent_card, test_get_extended_agent_card_when_advertised, test_skip_extended_card_when_not_advertised. 1 class(es): NoEventClient. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NoEventClient | class |  |
| test_answer_with_str | function |  |
| test_answer_with_text_part | function |  |
| test_answer_with_dict | function |  |
| test_build_agent_from_card | function |  |
| test_streaming_raises_when_no_task_started | function |  |
| test_polling_raises_when_no_task_started | function |  |
| test_streaming_raises_when_no_task_and_no_agent_card | function |  |
| test_polling_raises_when_no_task_and_no_agent_card | function |  |
| test_get_extended_agent_card_when_advertised | function |  |
| test_skip_extended_card_when_not_advertised | function |  |

## Chunks

### NoEventClient (class, L16-L26)

> *Summary: This client implementation intentionally ignores incoming events and subscription requests. It provides methods that yield nothing for sending messages or resubscribing, while explicitly failing if a task retrieval is attempted.*


### send_message (method, L17-L19, parent: NoEventClient)

> *Summary: This method is designed to asynchronously transmit a `Message` object, accepting optional keyword arguments. Currently, it contains no operational logic and yields nothing.*


### resubscribe (method, L21-L23, parent: NoEventClient)

> *Summary: This method yields nothing if the input `params` are not used to trigger a re-subscription. It serves as a placeholder or conditional yield point within an asynchronous context.*


### get_task (method, L25-L26, parent: NoEventClient)

> *Summary: This method intentionally raises an assertion error if invoked, indicating it is a placeholder or stub that should never be executed during normal operation. It accepts parameters but provides no functional output.*


### test_answer_with_str (function, L43-L61)

> *Summary: This test verifies the interaction flow when sending a string input to a remote agent. It mocks both the client and remote agents to assert that the remote agent correctly sends an assistant response back to the client upon receiving a user message.*


### test_answer_with_text_part (function, L65-L87)

> *Summary: This test verifies that when a remote agent receives a user message, it correctly responds with text content provided by its mocked client. It asserts the resulting chat history and confirms the correct response payload was sent back to the calling agent.*


### test_answer_with_dict (function, L104-L126)

> *Summary: This test verifies the interaction flow when sending a dictionary as input to a remote agent. It asserts that the remote agent correctly sends a predefined response back to the mocked client, matching both the message history and the specific arguments passed to the client's receiving method.*


### test_build_agent_from_card (function, L129-L145)

> *Summary: This test verifies the `A2aRemoteAgent` constructor by providing it a predefined `AgentCard`. It asserts that the resulting agent object correctly stores the input card and has specific default values for its name and URL.*


### test_streaming_raises_when_no_task_started (function, L149-L166)

> *Summary: This test verifies that attempting to stream a request to an agent fails with a connection error if no task has been initiated. It initializes an agent from a card definition and asserts that iterating over the streaming response raises an `A2aClientError`.*


### test_polling_raises_when_no_task_started (function, L170-L187)

> *Summary: When polling an agent that has not started a task, this test asserts that calling `_ask_polling` raises an `A2aClientError`. It initializes an agent from a defined card and attempts to iterate over the asynchronous response stream using a mock client.*


### test_streaming_raises_when_no_task_and_no_agent_card (function, L191-L199)

> *Summary: This test verifies that the streaming method raises an `A2aClientError` with a specific message when no agent card is configured on the remote agent. It achieves this by initializing an agent, explicitly setting its agent card to `None`, and then attempting to stream a message.*


### test_polling_raises_when_no_task_and_no_agent_card (function, L203-L211)

> *Summary: This test verifies that the polling mechanism throws an `A2aClientError` when no task is present and the agent lacks a defined card. It achieves this by setting the internal agent card to `None` before initiating the asynchronous polling loop with a sample message.*


### test_get_extended_agent_card_when_advertised (function, L215-L237)

> *Summary: This test verifies the retrieval of an extended agent card by calling a remote agent endpoint with specific authentication headers. It asserts that the returned `AgentCard` object correctly matches the provided mock data, including its name and description.*


### test_skip_extended_card_when_not_advertised (function, L241-L251)

> *Summary: This test verifies that an agent's card object correctly indicates it does not support extended authentication when the necessary advertising is absent. It achieves this by mocking a remote agent and asserting the `supports_authenticated_extended_card` flag is false after retrieving the card details.*

