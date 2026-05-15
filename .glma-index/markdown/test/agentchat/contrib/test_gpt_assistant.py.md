# test/agentchat/contrib/test_gpt_assistant.py

13 function(s): test_gpt_assistant_chat_openai, _test_gpt_assistant_chat, test_get_assistant_instructions, _test_get_assistant_instructions, test_gpt_assistant_instructions_overwrite, _test_gpt_assistant_instructions_overwrite, test_gpt_assistant_existing_no_instructions, test_get_assistant_files, test_assistant_retrieval, test_assistant_mismatch_retrieval and 3 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_gpt_assistant_chat_openai | function |  |
| _test_gpt_assistant_chat | function |  |
| test_get_assistant_instructions | function |  |
| _test_get_assistant_instructions | function |  |
| test_gpt_assistant_instructions_overwrite | function |  |
| _test_gpt_assistant_instructions_overwrite | function |  |
| test_gpt_assistant_existing_no_instructions | function |  |
| test_get_assistant_files | function |  |
| test_assistant_retrieval | function |  |
| test_assistant_mismatch_retrieval | function |  |
| test_gpt_assistant_tools_overwrite | function |  |
| test_gpt_reflection_with_llm | function |  |
| test_assistant_tool_and_function_role_messages | function |  |

## Chunks

### test_gpt_assistant_chat_openai (function, L28-L36)

> *Summary: This test function routes execution to a helper based on the provided `provider` string. It accepts credentials for both OpenAI and Azure, running the core chat test using the appropriate set of credentials.*


### _test_gpt_assistant_chat (function, L39-L100)

> *Summary: This test function initializes a GPT Assistant agent configured with a mock API tool for querying GitHub data. It invokes the assistant with a specific question, then asserts that the correct tool was called with relevant keywords and verifies the structure and content of the returned response.*


### test_get_assistant_instructions (function, L106-L114)

> *Summary: This test function routes execution to a helper based on the provided `provider` string. It accepts credentials for both OpenAI and Azure, calling the appropriate internal test method with the corresponding credential object.*


### _test_get_assistant_instructions (function, L117-L133)

> *Summary: Tests the `GPTAssistantAgent` by creating an instance with specific instructions, then verifies that calling `get_assistant_instructions()` returns the exact string provided during initialization before cleaning up the agent.*


### test_gpt_assistant_instructions_overwrite (function, L139-L147)

> *Summary: This test function routes execution to a helper based on the provided `provider` string, using either OpenAI or Azure credentials. It ensures that instructions can be correctly overwritten when interacting with the GPT assistant for the selected service.*


### _test_gpt_assistant_instructions_overwrite (function, L150-L190)

> *Summary: This test verifies that a `GPTAssistantAgent`'s instructions can be successfully updated when creating a new agent with the same ID and setting `overwrite_instructions=True`. It takes credentials as input, creates an initial assistant, then overwrites its instructions using the provided ID, and asserts the final instructions match the new value.*


### test_gpt_assistant_existing_no_instructions (function, L195-L227)

> *Summary: This test verifies that an agent can correctly retrieve the initial instructions for a GPT Assistant, even after creating a new instance of the assistant using its existing ID but omitting any instructions during creation. It asserts that the retrieved instructions match the original value set when the assistant was first initialized.*


### test_get_assistant_files (function, L232-L269)

> *Summary: This test verifies that a newly created GPTAssistantAgent correctly associates and exposes its uploaded files. It uploads a local file, initializes an agent with this file ID, and then asserts that the agent's associated file IDs are present after retrieval, handling both v1 and v2 API versions.*


### test_assistant_retrieval (function, L274-L341)

> *Summary: This test verifies that an agent can be reliably retrieved from the OpenAI API using a specific name. It creates two identical assistant instances with defined tools and files, asserts they are both found by retrieval functions, and then confirms neither remains after deletion.*


### test_assistant_mismatch_retrieval (function, L346-L438)

> *Summary: This test verifies the `GPTAssistantAgent`'s behavior when configured with mismatched instructions or tools against existing assistants. It creates and tests several assistant instances using different configurations to assert that retrieval functions correctly identify mismatches (e.g., finding two instead of one, or three instead of one). Finally, it cleans up all created resources.*


### test_gpt_assistant_tools_overwrite (function, L443-L556)

> *Summary: This test verifies that an existing GPTAssistantAgent's tools can be successfully replaced when creating a new instance with the same ID and setting `overwrite_tools=True`. It initializes an agent with one set of tools, then creates a second version using the original ID but supplying different tools to confirm they are overwritten.*


### test_gpt_reflection_with_llm (function, L561-L585)

> *Summary: This test verifies the reflection mechanism when using an LLM to summarize chat interactions. It initiates two separate chats with `GPTAssistantAgent` instances, one configured with a specific assistant ID and another without, both using "reflection\_with\_llm" for summarization.*


### test_assistant_tool_and_function_role_messages (function, L590-L652)

> *Summary: This test verifies that internally used message roles like `'tool'` and `'function'` are correctly mapped to the OpenAI API-compatible role (`'assistant'`) when invoking a `GPTAssistantAgent`. It iterates through predefined message combinations, asserting successful invocation and verifying the resulting response structure.*

