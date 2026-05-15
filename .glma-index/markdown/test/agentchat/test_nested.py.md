# test/agentchat/test_nested.py

6 function(s): test_nested, test_sync_nested_chat, test_async_nested_chat, test_async_nested_chat_chat_id_validation, test_sync_nested_chat_in_group, test_async_nested_chat_in_group. 1 class(es): MockAgentReplies. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MockAgentReplies | class |  |
| test_nested | function |  |
| test_sync_nested_chat | function |  |
| test_async_nested_chat | function |  |
| test_async_nested_chat_chat_id_validation | function |  |
| test_sync_nested_chat_in_group | function |  |
| test_async_nested_chat_in_group | function |  |

## Chunks

### MockAgentReplies (class, L17-L31)

> *Summary: This class simulates an agent's responses by accepting a list of predefined strings during initialization. It registers a callback with the provided agent that sequentially returns these mocked messages when prompted for replies.*


### __init__ (method, L18-L20, parent: MockAgentReplies)

> *Summary: Initializes the object by storing a list of predefined string messages and setting an internal index to track message progression. This setup allows for sequential retrieval of mocked conversation data during testing.*


### add_to_agent (method, L22-L31, parent: MockAgentReplies)

> *Summary: Registers a custom reply function with the provided agent, allowing it to respond based on a predefined sequence of mocked messages. This method uses an internal index to serve pre-canned responses when the agent is expected to reply.*


### test_nested (function, L35-L153)

> *Summary: This test function sets up a complex multi-agent conversation environment using AutoGen. It initializes various agents (like assistants, code interpreters, and managers) with specific LLM configurations and then initiates chats to test nested communication flows between these configured participants.*


### test_sync_nested_chat (function, L156-L189)

> *Summary: This test verifies the functionality of nested chats by setting up two inner assistants and a main assistant that manages them. It initiates a chat from a user proxy, expecting the process to terminate after receiving a specific final result message from one of the nested agents.*


### test_async_nested_chat (function, L193-L228)

> *Summary: This test verifies the functionality of nested asynchronous chats by setting up two inner assistants and a main assistant that manages them. It initiates a chat from a user proxy, expecting the process to resolve quickly with only the initial prompt and the final result message in the history.*


### test_async_nested_chat_chat_id_validation (function, L232-L264)

> *Summary: This test verifies that attempting to register nested chats asynchronously without providing a `chat_id` raises a `ValueError`. It sets up multiple assistant agents and mocks their replies before calling the registration method with `use_async=True`.*


### test_sync_nested_chat_in_group (function, L267-L308)

> *Summary: This test verifies nested chat functionality within a group conversation by setting up multiple agents and defining specific communication triggers. It initiates a chat via the user proxy, expecting a defined sequence of messages including a final result from an inner assistant interaction.*


### test_async_nested_chat_in_group (function, L312-L354)

> *Summary: This test verifies nested asynchronous group chat functionality by setting up multiple agents, including two inner assistants with predefined replies and a main group chat. It initiates the conversation via the user proxy and asserts that the final chat history contains the expected sequence of messages, demonstrating successful interaction across nested chats.*

