# test/agentchat/test_chats.py

12 function(s): work_dir, groupchat_work_dir, tasks_work_dir, test_chat_messages_for_summary, test_chats_group, test_chats, test_chats_general, test_chats_exceptions, _test_chats_w_func, test_chats_w_func and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| work_dir | function |  |
| groupchat_work_dir | function |  |
| tasks_work_dir | function |  |
| test_chat_messages_for_summary | function |  |
| test_chats_group | function |  |
| test_chats | function |  |
| test_chats_general | function |  |
| test_chats_exceptions | function |  |
| _test_chats_w_func | function |  |
| test_chats_w_func | function |  |
| test_udf_message_in_chats | function |  |
| test_post_process_carryover_item | function |  |

## Chunks

### work_dir (function, L25-L27)

> *Summary: This generator function creates and yields a temporary directory path using `TemporaryDirectory`. It ensures the created directory is automatically cleaned up upon exiting the context manager.*


### groupchat_work_dir (function, L31-L33)

> *Summary: This function yields a path to a temporary directory created using `TemporaryDirectory`. It ensures the directory is cleaned up automatically after yielding its value.*


### tasks_work_dir (function, L37-L39)

> *Summary: This generator function creates and yields a temporary directory path using `TemporaryDirectory`. It ensures the created directory is automatically cleaned up upon exiting the context manager.*


### test_chat_messages_for_summary (function, L42-L63)

> *Summary: This test verifies the `chat_messages_for_summary` method across different chat scenarios, asserting that it correctly captures the message history from both direct and group chats involving user and assistant agents. It confirms the expected number of messages returned based on the interaction context.*


### test_chats_group (function, L67-L172)

> *Summary: This test function sets up multiple AI agents (like financial assistants, writers, and critics) within different group chats to simulate complex workflows. It then initiates several chat sessions using a user proxy to execute tasks like answering questions or generating content, finally printing the results and costs of these interactions.*


### test_chats (function, L176-L300)

> *Summary: This test function sets up various AI agents (financial assistants and a writer) with specific configurations, including tool use capabilities for random number generation. It then initiates multiple concurrent chats using the `UserProxyAgent` to test different interaction scenarios, summarizing results from each conversation.*


### test_chats_general (function, L304-L402)

> *Summary: This test function sets up and executes multiple concurrent chat sessions between user agents and specialized AI assistants (financial experts and a writer). It uses predefined tasks to test different interaction patterns, including message summarization methods and turn limits, finally asserting on the resulting chat histories.*


### test_chats_exceptions (function, L406-L482)

> *Summary: This test function verifies that `initiate_chats` raises specific `AssertionError` exceptions when provided with invalid configurations for the `summary_method`. It tests scenarios where an unsupported summary method is used and where a required LLM client is missing for reflection-based summarization.*


### _test_chats_w_func (function, L485-L537)

> *Summary: Sets up an AutoGen multi-agent chat environment using a `chatbot` and `user_proxy`. It defines a function for currency exchange, registers it with the agents, and then initiates a conversation to calculate the conversion of 123.45 USD to EUR, printing the final summary and cost.*


### test_chats_w_func (function, L542-L546)

> *Summary: This test function executes a core chat testing routine by calling `_test_chats_w_func`, passing in provided credentials and the designated working directory for task execution. It serves to validate the functionality of the chat system under specific test conditions.*


### test_udf_message_in_chats (function, L550-L624)

> *Summary: This test verifies multi-agent communication by first having a researcher process stock data into a file and then passing that context to a writer agent. It initiates two separate chats—one for research and one for writing—to confirm the agents correctly interact with shared state and produce summaries.*


### test_post_process_carryover_item (function, L627-L633)

> *Summary: This test verifies the `_post_process_carryover_item` function handles both dictionary and string inputs correctly. It asserts that for a model message dictionary, it returns the content string, and for a raw string input, it returns the string unchanged.*

