# test/agentchat/group/test_group_tool_executor.py

2 class(es): TestGroupToolExecutor, TestGroupToolExecutorAsync. 37 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGroupToolExecutor | class |  |
| TestGroupToolExecutorAsync | class |  |

## Chunks

### TestGroupToolExecutor (class, L21-L621)

> *Summary: This test suite verifies the functionality of a tool execution manager, ensuring correct initialization, target management, and parameter modification for tools. It extensively tests methods for processing messages containing tool calls, handling various content types, and managing agent handoffs between conversational agents.*


### mock_agent (method, L23-L30, parent: TestGroupToolExecutor)

> *Summary: This method constructs and returns a mock instance of `ConversableAgent` for testing purposes. It initializes the mock with specific attributes like a name, empty tool lists, and mocked methods for tool management.*


### executor (method, L33-L35, parent: TestGroupToolExecutor)

> *Summary: This method instantiates and returns a new `GroupToolExecutor` instance, primarily used within tests to provide a concrete object for execution.*


### test_initialisation (method, L37-L43, parent: TestGroupToolExecutor)

> *Summary: Verifies that a `GroupToolExecutor` instance is correctly initialized by checking its name matches a predefined constant, and asserting default values for internal states like the next target, system message, human input mode, and code execution configuration.*


### test_next_target_management (method, L45-L65, parent: TestGroupToolExecutor)

> *Summary: This test verifies the state management of a tool executor's next target. It confirms that targets can be successfully set, retrieved, checked for existence, and subsequently cleared, ensuring proper error handling when accessing an unset target.*


### test_modify_context_variables_param (method, L69-L94, parent: TestGroupToolExecutor)

> *Summary: This test verifies that the executor correctly modifies a function's signature to inject dependencies into parameters. It simulates replacing a parameter within the function's signature using mocks and asserts that the replacement methods were called as expected, resulting in an updated signature object.*


### test_modify_context_variables_param_preserves_async (method, L97-L115, parent: TestGroupToolExecutor)

> *Summary: This test verifies that the parameter modification utility preserves asynchronous behavior when wrapping a function. It asserts that the returned callable is an awaitable coroutine and correctly executes it to return the expected string result.*


### test_modify_context_variables_param_preserves_sync (method, L117-L132, parent: TestGroupToolExecutor)

> *Summary: Verifies that when a synchronous tool is passed to the executor's modification function, the returned wrapper remains a standard synchronous function. It confirms this by asserting the wrapper is not an awaitable and successfully executes it with sample inputs.*


### test_change_tool_context_variables_to_depends (method, L135-L171, parent: TestGroupToolExecutor)

> *Summary: This test verifies that the executor correctly modifies a tool's context variables to use dependency injection when provided with specific inputs. It asserts that the agent removes and then re-registers the tool after injecting parameters via `mock_inject_params`.*


### test_register_agents_functions (method, L173-L228, parent: TestGroupToolExecutor)

> *Summary: This test verifies that a tool executor correctly merges functions from multiple agents and registers their associated tools. It confirms that the executor updates its internal function map and calls necessary registration methods for each provided agent's tools.*


### test_generate_group_tool_reply_with_no_tool_calls (method, L230-L241, parent: TestGroupToolExecutor)

> *Summary: When provided with a user message containing no tool calls, this test verifies that the reply generation process fails and returns `None`. It confirms the executor correctly handles input lacking any specified tools.*


### test_generate_group_tool_reply_with_tool_calls (method, L243-L283, parent: TestGroupToolExecutor)

> *Summary: This test verifies that when provided a message containing tool calls, the executor correctly processes it by calling an internal reply generation method. It asserts that the call to this method uses only the initial tool call and returns the expected successful outcome along with the mocked tool response.*


### test_generate_group_tool_reply_with_reply_result (method, L285-L324, parent: TestGroupToolExecutor)

> *Summary: This test verifies the `_generate_group_tool_reply` method's behavior when a tool returns a `ReplyResult`. It simulates an agent receiving a tool response containing context updates and a transition target, asserting that the executor correctly updates the agent's state variables and sets the next group target.*


### test_generate_group_tool_reply_with_multiple_tools (method, L326-L388, parent: TestGroupToolExecutor)

> *Summary: This test verifies the logic for generating a group tool reply when multiple tools are invoked. It simulates receiving results from two distinct tools, asserting that the agent's context variables are correctly updated with data from both responses and that the final output content aggregates all tool replies.*


### test_error_handling (method, L390-L403, parent: TestGroupToolExecutor)

> *Summary: This test verifies that the tool reply generation method correctly raises a `ValueError` when the underlying function fails to return a message after executing a tool call. It achieves this by mocking the response to indicate no message was returned for the specified tool invocation.*


### test_function_is_agent_llm_handoff (method, L405-L451, parent: TestGroupToolExecutor)

> *Summary: This test verifies the `function_is_agent_llm_handoff` logic by simulating various scenarios where an agent might or might not support LLM handoffs for a given function. It asserts that the method correctly returns `False` if the agent isn't found, lacks necessary attributes, or doesn't list the target function in its defined handoff conditions, and `True` only when the function is explicitly listed.*


### test_get_sender_agent_for_message (method, L453-L487, parent: TestGroupToolExecutor)

> *Summary: Verifies the logic for retrieving a sender agent from a message dictionary, using mocked group manager and chat objects as input. It tests scenarios where no name is present, the group manager is missing, an agent is successfully found via `agent_by_name`, or when the specified agent does not exist in the groupchat.*


### test_is_handoff_function (method, L489-L547, parent: TestGroupToolExecutor)

> *Summary: This test verifies the `is_handoff_function` logic by passing various message structures to it, asserting that it correctly identifies a handoff function based on the presence of required fields and the outcome of an internal check against agent LLM functions. It confirms edge cases like missing keys or invalid tool call formats return `False`, while valid handoff calls return `True`.*


### test_normalize_tool_content_none (method, L549-L552, parent: TestGroupToolExecutor)

> *Summary: When passed `None` as input to the normalization method, it consistently returns an empty string. This verifies the expected handling of null content within the tool execution logic.*


### test_normalize_tool_content_string (method, L554-L557, parent: TestGroupToolExecutor)

> *Summary: Verifies that the internal tool content normalization method correctly handles and returns an input string unchanged. It takes a string as input and asserts the output is identical to the original string.*


### test_normalize_tool_content_plain_list (method, L559-L563, parent: TestGroupToolExecutor)

> *Summary: When provided with a standard Python list as input, this test verifies that the internal normalization method converts it into a JSON string representation of that list. The expected output is the serialized JSON string matching the input list's contents.*


### test_normalize_tool_content_empty_list (method, L565-L568, parent: TestGroupToolExecutor)

> *Summary: When provided with an empty list as input, this test verifies that the tool content normalization method returns a JSON string representing an empty array.*


### test_normalize_tool_content_openai_format (method, L570-L577, parent: TestGroupToolExecutor)

> *Summary: Verifies that the internal tool content normalization method correctly processes an input list structured in OpenAI message format (containing text and image URL parts). It asserts that the output matches a specific, casted representation of the original input structure.*


### test_normalize_tool_content_list_of_dicts_no_type (method, L579-L583, parent: TestGroupToolExecutor)

> *Summary: When provided a list of dictionaries lacking a `"type"` key, the method returns the input content serialized as a JSON string. This test verifies that no transformation occurs when type information is absent in the dictionary elements.*


### test_normalize_tool_content_tuple (method, L585-L589, parent: TestGroupToolExecutor)

> *Summary: When provided with a tuple input, this test verifies that the internal normalization method converts it into a JSON string representation of the original tuple content. The expected output is the serialized JSON string matching the input tuple's values.*


### test_normalize_tool_content_dict (method, L591-L595, parent: TestGroupToolExecutor)

> *Summary: Verifies that the internal tool content normalization method correctly serializes a given dictionary input into a JSON string output. It confirms the resulting string matches the expected JSON representation of the original dictionary structure.*


### test_normalize_tool_content_int (method, L597-L600, parent: TestGroupToolExecutor)

> *Summary: When provided with an integer input, this test verifies that the internal normalization method converts it into a JSON string representation. The function takes an `executor` instance and asserts the output matches the serialized form of the input integer.*


### test_normalize_tool_content_float (method, L602-L605, parent: TestGroupToolExecutor)

> *Summary: Verifies that the internal content normalization method correctly converts a floating-point input to its JSON string representation. It takes a float as input and asserts the output matches the serialized JSON string of that float.*


### test_normalize_tool_content_bool (method, L607-L610, parent: TestGroupToolExecutor)

> *Summary: Verifies that the internal content normalization method correctly converts a Python boolean input to its JSON string representation. It asserts that passing `True` results in the string `"true"`.*


### test_normalize_tool_content_non_json_serializable (method, L612-L621, parent: TestGroupToolExecutor)

> *Summary: This test verifies that the tool content normalization process correctly converts a non-JSON-serializable object into its string representation. It passes an instance of a custom class and asserts the output matches the object's `__str__` method return value.*


### TestGroupToolExecutorAsync (class, L624-L799)

> *Summary: This test suite verifies the asynchronous group tool reply generation logic by simulating various scenarios. It checks for correct handler registration, handles cases with and without tool calls, validates responses containing structured results or `ReplyResult` objects, and tests error handling during execution.*


### executor (method, L628-L630, parent: TestGroupToolExecutorAsync)

> *Summary: Instantiates and returns a new `GroupToolExecutor` instance, primarily used within tests to provide a mock or concrete execution environment.*


### test_async_reply_handler_registered (method, L632-L644, parent: TestGroupToolExecutorAsync)

> *Summary: Verifies that the `GroupToolExecutor` correctly registers an asynchronous reply handler named `_a_generate_group_tool_reply` during initialization. It asserts that this specific async handler is present in the internal list and has the `ignore_async_in_sync_chat` flag set to `True`.*


### test_a_generate_group_tool_reply_with_no_tool_calls (method, L647-L655, parent: TestGroupToolExecutorAsync)

> *Summary: When provided with a user message containing no tool calls, the execution handler should fail and return `None`. This test verifies that the system correctly handles input lacking any requested tools.*


### test_a_generate_group_tool_reply_with_tool_calls (method, L658-L685, parent: TestGroupToolExecutorAsync)

> *Summary: This test verifies the asynchronous reply generation when a message contains tool calls. It simulates an executor processing a user message with a tool call, mocking the subsequent tool execution to assert that the correct response structure is returned upon successful completion.*


### test_a_generate_group_tool_reply_with_reply_result (method, L688-L718, parent: TestGroupToolExecutorAsync)

> *Summary: This test verifies the asynchronous handling of a `ReplyResult` when generating a group tool reply. It simulates an agent receiving a successful tool execution result and asserts that the executor correctly updates context variables, sets the next target, and returns the appropriate response structure.*


### test_a_generate_group_tool_reply_with_multiple_tools (method, L721-L770, parent: TestGroupToolExecutorAsync)

> *Summary: This test verifies the asynchronous handling of multiple tool executions within a group context. It simulates an agent receiving two distinct tool calls, processes their corresponding mock responses, and asserts that both results correctly update the agent's context variables and determine the next transition target.*


### test_a_generate_group_tool_reply_error_handling (method, L773-L783, parent: TestGroupToolExecutorAsync)

> *Summary: This test verifies that the group tool reply generation raises a `ValueError` when the underlying tool execution handler returns success but no corresponding message. It simulates an input containing a user request with a tool call and asserts the expected error is raised during processing.*


### test_a_generate_group_tool_reply_structured_output (method, L786-L799, parent: TestGroupToolExecutorAsync)

> *Summary: This test verifies that the group tool reply generation handler correctly returns structured output when provided with a user message containing a specific tool call. It asserts that the returned `result` matches the expected arguments defined in the input tool call structure.*

