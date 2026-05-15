# test/agentchat/test_conversable_agent.py

71 function(s): conversable_agent, test_conversable_agent_name_with_white_space, test_sync_trigger, test_async_trigger, test_async_trigger_in_sync_chat, test_sync_trigger_in_async_chat, test_context, test_generate_code_execution_reply, test_max_consecutive_auto_reply, test_max_consecutive_auto_reply_with_max_turns and 61 more. 2 class(es): TestWrapFunction, TestAsyncReplyFunctionSkipping. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| conversable_agent | function |  |
| test_conversable_agent_name_with_white_space | function |  |
| test_sync_trigger | function |  |
| test_async_trigger | function |  |
| test_async_trigger_in_sync_chat | function |  |
| test_sync_trigger_in_async_chat | function |  |
| test_context | function |  |
| test_generate_code_execution_reply | function |  |
| test_max_consecutive_auto_reply | function |  |
| test_max_consecutive_auto_reply_with_max_turns | function |  |
| test_conversable_agent | function |  |
| test_terminate_chat_true | function |  |
| test_terminate_chat_false_non_termination_content | function |  |
| test_terminate_chat_false_non_string_content | function |  |
| test_a_initiate_chat_triggers_terminate_chat | function |  |
| test_generate_reply | function |  |
| test_generate_reply_raises_on_messages_and_sender_none | function |  |
| test_a_generate_reply_raises_on_messages_and_sender_none | function |  |
| test_generate_reply_with_messages_and_sender_none | function |  |
| test_a_generate_reply_with_messages_and_sender_none | function |  |
| test_a_get_human_input_console_io | function |  |
| test_a_get_human_input_thread_stream | function |  |
| test_a_get_human_input_async_thread_stream | function |  |
| test_update_function_signature_and_register_functions | function |  |
| TestWrapFunction | class |  |
| get_origin | function |  |
| test_register_for_llm | function |  |
| test_register_for_llm_api_style_function | function |  |
| test_register_for_llm_without_description | function |  |
| test_register_for_llm_with_docstring | function |  |
| test_register_for_llm_without_LLM | function |  |
| test_register_for_llm_without_configuration | function |  |
| test_register_for_llm_without_model_name | function |  |
| test_register_for_execution | function |  |
| test_register_functions | function |  |
| test_function_registration_e2e_sync | function |  |
| _test_function_registration_e2e_async | function |  |
| test_function_registration_e2e_async | function |  |
| test_max_turn | function |  |
| test_message_func | function |  |
| test_summary | function |  |
| test_summarize_chat_with_dict_summary | function |  |
| test_process_before_send | function |  |
| test_messages_with_carryover | function |  |
| test_chat_history | function |  |
| test_http_client | function |  |
| test_adding_duplicate_function_warning | function |  |
| test_process_gemini_carryover | function |  |
| test_process_carryover | function |  |
| test_handle_gemini_carryover | function |  |
| test_handle_carryover | function |  |
| test_conversable_agent_with_whitespaces_in_name_end2end | function |  |
| test_context_variables | function |  |
| test_gemini_with_tools_parameters_set_to_is_annotated_with_none_as_default_value | function |  |
| test_conversable_agent_with_deepseek_reasoner | function |  |
| test_invalid_functions_parameter | function |  |
| test_update_system_message | function |  |
| test_tools_property | function |  |
| test_add_tool_for_llm | function |  |
| test_add_tool_for_llm_invalid_type | function |  |
| test_remove_tool_for_llm | function |  |
| test_remove_tool_by_name_for_llm | function |  |
| test_remove_tool_for_llm_not_found | function |  |
| test_tool_integration | function |  |
| test_execute_function_resolves_async_tool | function |  |
| test_generate_tool_calls_reply_handles_async_tool | function |  |
| test_create_or_get_executor | function |  |
| test_validate_llm_config | function |  |
| test_cache_context | function |  |
| test_set_ui_tools | function |  |
| test_unset_ui_tools | function |  |
| test_run_method_no_double_tool_registration | function |  |
| TestAsyncReplyFunctionSkipping | class |  |

## Chunks

### conversable_agent (function, L44-L51)

> *Summary: Creates and returns a `ConversableAgent` instance configured for automated interaction. This agent is set up to handle up to 10 consecutive auto-replies without requiring human input.*


### test_conversable_agent_name_with_white_space (function, L55-L67)

> *Summary: This test verifies that an agent can be initialized with a given name and asserts its internal name matches the input. It then confirms that attempting to create a new `ConversableAgent` using a name containing whitespace raises a specific `ValueError`.*


### test_sync_trigger (function, L70-L105)

> *Summary: This test verifies the behavior of reply registration and chat initiation within a `ConversableAgent`. It asserts that registered replies are correctly triggered based on various matching criteria (specific agents, all agents, or sender name prefixes), while also confirming error handling for invalid registrations.*


### test_async_trigger (function, L109-L173)

> *Summary: This test verifies the registration and execution of various reply triggers for an agent system. It demonstrates how to register replies using specific agents, classes, lambda functions based on sender properties, or lists of targets, asserting that the correct response is returned upon initiating a chat.*


### test_async_trigger_in_sync_chat (function, L176-L199)

> *Summary: This test verifies that attempting to use an asynchronous reply function within a synchronous chat initiation raises a `RuntimeError`. It further confirms that explicitly ignoring async replies allows the chat to proceed without calling the mocked reply function.*


### test_sync_trigger_in_async_chat (function, L203-L213)

> *Summary: This test verifies that an asynchronous chat initiated by `agent1` correctly triggers a synchronous reply registered on `agent`. It confirms the response content matches the value returned by the registered callback function.*


### test_context (function, L216-L249)

> *Summary: This test verifies how a `ConversableAgent` processes messages containing context variables. It demonstrates that the agent can correctly render string templates and lambda functions within message content using provided context dictionaries.*


### test_generate_code_execution_reply (function, L252-L361)

> *Summary: This test suite verifies the `generate_code_execution_reply` method's behavior when determining if and how to execute code blocks from a list of messages. It tests various scenarios including configuration checks, message history constraints (`last_n_messages`), and error handling for invalid configurations.*


### test_max_consecutive_auto_reply (function, L364-L390)

> *Summary: Verifies the behavior of `max_consecutive_auto_reply` by testing how an agent limits automatic responses based on configuration and updates. It simulates chat interactions to confirm counter increments, auto-reply triggering, message history length, and control over receiving replies.*


### test_max_consecutive_auto_reply_with_max_turns (function, L393-L433)

> *Summary: This test verifies the behavior when agents are limited by `max_consecutive_auto_reply` during chat initiation. It sets up two agents with different reply limits and asserts that the conversation terminates correctly, logging a specific message when the consecutive auto-reply limit is hit, regardless of the overall turn limit.*


### test_conversable_agent (function, L436-L507)

> *Summary: This test verifies the core messaging and configuration behaviors of a `ConversableAgent`. It checks that agents correctly process incoming/outgoing messages (both string and dictionary formats), enforces validation on message structure, allows updating the system message, and correctly initializes agent descriptions based on provided system or description fields.*


### test_terminate_chat_true (function, L510-L519)

> *Summary: This test verifies that an agent correctly identifies a chat termination when the recipient's termination condition matches a specific message content. It asserts that `_should_terminate_chat` returns `True` given a "TERMINATE" message and a configured recipient.*


### test_terminate_chat_false_non_termination_content (function, L522-L531)

> *Summary: This test verifies that the internal chat termination logic returns `False` when a received message does not match the defined termination condition. It simulates an interaction where the recipient's termination check fails for a standard content message.*


### test_terminate_chat_false_non_string_content (function, L534-L543)

> *Summary: Verifies that the internal chat termination logic returns `False` when the input message content is not a string (specifically `None`). It uses two agents to simulate a conversation and checks the result of the termination check against a non-string message.*


### test_a_initiate_chat_triggers_terminate_chat (function, L547-L567)

> *Summary: This test verifies that initiating a chat with an agent immediately triggers termination when mocked to return a specific message. It asserts that the resulting chat history contains exactly one turn with the content "TERMINATE".*


### test_generate_reply (function, L570-L594)

> *Summary: This test verifies the `generate_reply` method of a conversational agent by simulating function calls and message passing between agents. It asserts correct output when messages are provided with no sender, when messages are absent but a sender is present, and confirms that a `SenderRequiredError` is raised when both inputs are insufficient.*


### test_generate_reply_raises_on_messages_and_sender_none (function, L597-L599)

> *Summary: This test verifies that calling the reply generation method with `None` for both messages and sender arguments correctly raises an `AssertionError`. It ensures the agent handles missing required inputs by failing as expected.*


### test_a_generate_reply_raises_on_messages_and_sender_none (function, L603-L605)

> *Summary: This test verifies that calling the reply generation method with `None` for both messages and sender arguments correctly raises an `AssertionError`. It ensures the agent handles missing required inputs by failing as expected.*


### test_generate_reply_with_messages_and_sender_none (function, L608-L616)

> *Summary: This test verifies that the agent can generate a reply when provided with a list of messages but no specific sender. It asserts that the returned response is not null, catching any unexpected exceptions during execution.*


### test_a_generate_reply_with_messages_and_sender_none (function, L620-L628)

> *Summary: This test verifies that the agent can generate a reply when provided with a list of messages but no specific sender. It asserts that the returned response is not null, catching any unexpected errors during execution.*


### test_a_get_human_input_console_io (function, L633-L642)

> *Summary: This test verifies that an agent correctly retrieves user input when configured for always-on human interaction mode. It mocks console input to ensure the `a_get_human_input` method returns the expected string value.*


### test_a_get_human_input_thread_stream (function, L646-L665)

> *Summary: This test verifies that an agent correctly receives input from a background thread when configured for human interaction. It sets up a `ThreadIOStream` to simulate external input and asserts the agent processes this simulated response successfully.*


### test_a_get_human_input_async_thread_stream (function, L669-L690)

> *Summary: This test verifies that an agent correctly receives human input when configured to use asynchronous thread streaming for I/O. It sets up a background task to asynchronously provide the expected response, ensuring the agent's `a_get_human_input` call resolves with the provided string.*


### test_update_function_signature_and_register_functions (function, L693-L763)

> *Summary: This test verifies the lifecycle of tool definitions for an agent by first adding and asserting the presence of "python" and "sh" function signatures via `update_function_signature`. It then registers these functions using `register_function` and finally demonstrates removal by setting a function's implementation to `None` in a subsequent registration call.*


### TestWrapFunction (class, L766-L854)

> *Summary: This test suite verifies the functionality of a function wrapping mechanism applied to an agent, ensuring it correctly handles synchronous and asynchronous operations with structured data inputs (like currency objects). It confirms that decorated functions behave as expected when called both synchronously and asynchronously.*


### test__wrap_function_sync (method, L767-L801, parent: TestWrapFunction)

> *Summary: This test verifies that a function decorated with `agent._wrap_function` correctly handles synchronous execution when processing structured inputs. It asserts that the wrapped function takes a currency object and a quote symbol, calculates an exchange rate based on predefined logic, and returns a new currency object matching expected JSON output.*


### test__wrap_function_list (method, L804-L817, parent: TestWrapFunction)

> *Summary: This test verifies that a function decorated with `_wrap_function` correctly processes inputs from lists of tuples and custom model instances. It asserts the output matches an expected list constructed by combining transformed tuple data with existing model objects.*


### test__wrap_function_async (method, L820-L854, parent: TestWrapFunction)

> *Summary: This test verifies that a function decorated with `agent._wrap_function` correctly handles asynchronous execution and input validation using Pydantic models. It calls the wrapped currency calculation function with specific inputs to assert the resulting converted amount matches an expected JSON structure.*


### get_origin (function, L857-L858)

> *Summary: This function transforms a dictionary of callables by extracting the `_origin` attribute from each value. It returns a new dictionary with the same keys but containing these extracted origins as values.*


### test_register_for_llm (function, L861-L929)

> *Summary: This test verifies that registering functions with `register_for_llm` correctly populates the LLM configuration's tool definitions for multiple agents. It asserts that the generated JSON schemas accurately reflect the function names, descriptions, and input parameters provided during registration.*


### test_register_for_llm_api_style_function (function, L932-L996)

> *Summary: This test verifies that registering Python functions with specific metadata (like name, description, and API style) correctly populates the `functions` configuration within each agent's LLM settings. It asserts that the resulting function schemas match predefined expectations based on the registration arguments provided to the decorated methods.*


### test_register_for_llm_without_description (function, L999-L1006)

> *Summary: This test verifies that registering a function with an LLM configuration results in an empty description if no explicit annotation is provided. It instantiates an agent and registers a placeholder function, asserting the resulting description attribute is blank.*


### test_register_for_llm_with_docstring (function, L1009-L1017)

> *Summary: This test verifies that registering a function with a docstring correctly sets the function's description attribute on the agent. It uses a mock credentials object to initialize an agent and then asserts the expected documentation string is captured upon registration.*


### test_register_for_llm_without_LLM (function, L1020-L1029)

> *Summary: This test verifies that attempting to register a function for LLM interaction on an agent lacking `llm_config` raises an `AssertionError`. It confirms the system correctly enforces the requirement of having an LLM configuration before tool registration can occur.*


### test_register_for_llm_without_configuration (function, L1032-L1037)

> *Summary: Asserts that initializing a `ConversableAgent` with an empty configuration list for the LLM raises a `ValueError`. This verifies that the agent requires at least one item in its LLM configuration.*


### test_register_for_llm_without_model_name (function, L1040-L1045)

> *Summary: Asserts that instantiating a `ConversableAgent` with an empty model name in its LLM configuration raises a `ValueError`. This verifies the agent correctly enforces non-empty model identifiers during setup.*


### test_register_for_execution (function, L1048-L1078)

> *Summary: This test verifies that agents and user proxies correctly register functions for execution and LLM invocation. It asserts the internal `function_map` structures of these entities after decorating them with `@register_for_execution` and `@register_for_llm`.*


### test_register_functions (function, L1081-L1117)

> *Summary: This test verifies that a custom function, `exec_python`, is correctly registered with an AI agent and user proxy. It asserts that the agent's configuration accurately reflects the function's name, description, and input schema.*


### test_function_registration_e2e_sync (function, L1121-L1182)

> *Summary: This test verifies end-to-end function registration by setting up an AI agent and a user proxy, then initiating a chat to execute both a decorated timer function and a manually registered stopwatch function. It asserts that the mock objects for these functions were called with the expected input values based on the conversation prompt.*


### _test_function_registration_e2e_async (function, L1185-L1243)

> *Summary: This asynchronous test sets up an AutoGen environment with a coder agent and a user proxy to verify function registration. It initiates a chat asking the agents to execute both an async timer and a sync stopwatch, then asserts that the respective mock functions were called correctly.*


### test_function_registration_e2e_async (function, L1249-L1252)

> *Summary: This asynchronous test verifies end-to-end function registration by calling a helper function with provided credentials. It asserts the correct behavior of the system's function registration mechanism under async conditions.*


### test_max_turn (function, L1256-L1272)

> *Summary: This test verifies the behavior of a conversational agent when limited to a maximum number of turns. It initiates a chat between an `AssistantAgent` and a mocked `UserProxyAgent`, asserting that the resulting conversation history length does not exceed a specific limit (6).*


### test_message_func (function, L1276-L1323)

> *Summary: This test verifies agent interaction by setting up a `UserProxyAgent` and an `AssistantAgent` configured to use a mock function that returns random numbers. It executes two chat scenarios: one with a direct initial message and another where the assistant's response is generated via a helper function, asserting on the resulting chat summary.*


### test_summary (function, L1327-L1393)

> *Summary: Tests how different summary methods (`reflection_with_llm` and a custom function) behave when initiating chats between a `UserProxyAgent` and an `AssistantAgent`. It demonstrates generating summaries based on the conversation history or specific arguments provided during chat initiation.*


### test_summarize_chat_with_dict_summary (function, L1396-L1414)

> *Summary: Tests the agent's ability to generate a structured summary by providing a custom dictionary-returning function as the `summary_method`. It initiates a short chat and asserts that the resulting summary matches the predefined output from the provided summarization logic.*


### test_process_before_send (function, L1417-L1434)

> *Summary: This test verifies the `process_message_before_send` hook by mocking a frontend sender function. It confirms that messages are logged and passed to the mock only when not sent silently, asserting correct behavior for both standard and silent transmissions between two agents.*


### test_messages_with_carryover (function, L1437-L1503)

> *Summary: Verifies the `generate_init_message` method's behavior when handling various input types for messages and optional carryover data. It asserts correct output types (string or dictionary) and validates error raising for invalid carryover inputs, including testing multimodal message structures.*


### test_chat_history (function, L1506-L1574)

> *Summary: Tests agent behavior by initiating conversations between multiple agents, then re-instantiating one agent with the prior conversation history to verify message persistence and correct accumulation across subsequent chats. It asserts that the chat messages correctly reflect the combined interactions from both past and future conversational sessions.*


### test_http_client (function, L1577-L1594)

> *Summary: Asserts that initializing a `ConversableAgent` with an HTTP client configured in the LLM settings raises a `TypeError`. This test verifies expected error handling when providing specific configuration structures to the agent.*


### test_adding_duplicate_function_warning (function, L1597-L1651)

> *Summary: This test verifies that the agent emits `UserWarning`s when attempting to register a function or update an existing function/tool signature with the same name. It confirms warnings are raised for duplicate function registration and overriding existing definitions via `update_function_signature` and `update_tool_signature`.*


### test_process_gemini_carryover (function, L1654-L1660)

> *Summary: This test verifies that an agent correctly incorporates a specified context into its initial message. It passes a base content and a dictionary containing a `carryover` list to the internal processing method, asserting the output combines the original content with the provided context string.*


### test_process_carryover (function, L1663-L1677)

> *Summary: This test verifies the internal `_process_carryover` method's behavior when incorporating context. It asserts that the input content is correctly appended with a formatted carryover string (either single or list-based) or remains unchanged if no carryover is provided.*


### test_handle_gemini_carryover (function, L1680-L1686)

> *Summary: This test verifies that an agent correctly processes a carryover message from Gemini. It asserts that the resulting content is the original message concatenated with a specific context string derived from the provided carryover arguments.*


### test_handle_carryover (function, L1689-L1703)

> *Summary: This test verifies the internal `_handle_carryover` method's behavior when incorporating context. It asserts that the function correctly appends a string or list of carryover messages to the input message, while also ensuring it returns the original message if no carryover is provided.*


### test_conversable_agent_with_whitespaces_in_name_end2end (function, L1708-L1732)

> *Summary: This test verifies that initiating a chat with a `ConversableAgent` fails with a `ValueError` if the agent's name contains spaces when using GPT-4 or OpenAI LLMs. Conversely, it confirms that no error is raised for Anthropic or Gemini models even when the agent name includes whitespace.*


### test_context_variables (function, L1736-L1768)

> *Summary: This test verifies the functionality of context variables within a `ConversableAgent`. It confirms that an agent can be initialized with or without context, and it tests methods for retrieving, setting, overwriting, and bulk updating these stored key-value pairs.*


### test_gemini_with_tools_parameters_set_to_is_annotated_with_none_as_default_value (function, L1774-L1796)

> *Summary: This test verifies that an agent correctly invokes a tool function when the tool's parameter defaults to `None`. It sets up a conversational flow between an agent and a user proxy, triggering the mocked "login" function with its default argument. The assertion confirms the mock was called exactly once during this interaction.*


### test_conversable_agent_with_deepseek_reasoner (function, L1802-L1818)

> *Summary: This test verifies the conversational capability of an agent configured with a DeepSeek reasoner by initiating a chat session between it and a user proxy. It asserts that the resulting summary from the interaction is a string after a limited number of turns.*


### test_invalid_functions_parameter (function, L1821-L1826)

> *Summary: Asserts that initializing an agent with a non-callable or incorrect type for the `functions` argument raises a `TypeError`. This verifies input validation for the agent's function configuration during instantiation.*


### test_update_system_message (function, L1829-L1848)

> *Summary: This test verifies the constraints on the `update_agent_state_before_reply` configuration for an agent. It asserts that the provided update function must be a string or callable, accept two parameters, and return a string.*


### test_tools_property (function, L1851-L1869)

> *Summary: This test verifies that accessing the `tools` property returns an independent copy of the internal tool list. It confirms that modifying the returned list does not affect the agent's actual stored tools.*


### test_add_tool_for_llm (function, L1872-L1891)

> *Summary: This test verifies that a provided `Tool` object is correctly added to an agent's internal list and subsequently registered within the LLM configuration schema. It confirms successful integration by asserting both the presence of the tool internally and its inclusion in the expected list of available tools for the language model.*


### test_add_tool_for_llm_invalid_type (function, L1894-L1899)

> *Summary: This test verifies that attempting to register an invalid type (a string) as a tool for the LLM raises a `TypeError`. It asserts that the error message specifically indicates the input must be a function or a `Tool` object.*


### test_remove_tool_for_llm (function, L1902-L1920)

> *Summary: This test verifies that a registered tool is successfully removed from the LLM's configuration after calling `remove_tool_for_llm`. It registers a sample tool with an agent and asserts that its name no longer appears in the list of available tool schemas.*


### test_remove_tool_by_name_for_llm (function, L1923-L1941)

> *Summary: This test verifies that a registered tool can be successfully removed from the LLM configuration by providing its name to `update_tool_signature`. It asserts that after calling the removal method, the tool's name no longer appears in the list of schemas exposed to the language model.*


### test_remove_tool_for_llm_not_found (function, L1944-L1954)

> *Summary: This test verifies that attempting to remove a non-existent tool from an agent configuration raises an `AssertionError`. It initializes an agent and calls the removal method with a defined tool, expecting the specific error message indicating the tool is missing.*


### test_tool_integration (function, L1957-L1987)

> *Summary: This test verifies the lifecycle of tool integration within an agent by registering, asserting the presence of, and then removing tools. It confirms that the agent's internal list and its configuration passed to the LLM accurately reflect which tools are available.*


### test_execute_function_resolves_async_tool (function, L1990-L2009)

> *Summary: This test verifies that the agent correctly awaits and resolves asynchronous tools when executing a function call. It calls `execute_function` with a request to an async tool, asserting that the returned payload contains the resolved output ("NYC") and that the tool received the correct input ("nyc").*


### test_generate_tool_calls_reply_handles_async_tool (function, L2012-L2036)

> *Summary: This test verifies that the agent correctly processes and awaits asynchronous tool execution when a reply contains tool calls. It simulates an assistant message with a call to `title_tool` and asserts that the resulting response includes the correct, processed output from the async function.*


### test_create_or_get_executor (function, L2039-L2079)

> *Summary: This test verifies that calling `_create_or_get_executor` with a specific tool configuration consistently returns the same agent instance across multiple calls. It asserts that the returned executor is an instance of `ConversableAgent` and correctly exposes the provided tools to both the LLM configuration and the execution environment.*


### test_validate_llm_config (function, L2106-L2110)

> *Summary: This test verifies the configuration validation logic by passing various inputs to `ConversableAgent._validate_llm_config`. It asserts that the returned validated configuration matches the expected output.*


### test_cache_context (function, L2114-L2166)

> *Summary: This test verifies the caching mechanism for agent conversations by comparing execution times across three scenarios: no cache, cold cache, and warm cache. It uses mocked user input to ensure consistent testing while asserting that the warm cache significantly speeds up subsequent identical chat runs compared to the other two states.*


### test_set_ui_tools (function, L2169-L2188)

> *Summary: This test verifies that a `ConversableAgent` correctly registers provided UI tools both within its LLM configuration and its internal function map. It iterates three times, adding a unique mock tool in each iteration and asserting the correct count and names are present in both structures while ensuring previous tools are removed or overwritten as expected.*


### test_unset_ui_tools (function, L2191-L2208)

> *Summary: This test verifies that an agent correctly removes previously registered UI tools from its configuration. It initializes an agent, adds a mock tool, and then calls `unset_ui_tools` to confirm the tool is successfully removed from the internal tool list.*


### test_run_method_no_double_tool_registration (function, L2211-L2245)

> *Summary: Verifies that when an agent is initialized with pre-registered tools and subsequently uses an executor configured with runtime tools, the LLM configuration correctly registers each tool exactly once. It confirms both initial and dynamically added tools are present without duplication in the final tool list and execution map.*


### TestAsyncReplyFunctionSkipping (class, L2248-L2502)

> *Summary: This test suite verifies the logic for selectively skipping synchronous reply functions when an agent operates in asynchronous mode. It ensures that only sync functions lacking an async counterpart are executed, while correctly handling custom registered functions and integration scenarios between two agents.*


### test_get_sync_funcs_to_skip_in_async_chat (method, L2251-L2265, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that the agent correctly identifies specific synchronous methods that possess asynchronous counterparts. It asserts that the returned set of function names matches a predefined list of known sync functions with async equivalents.*


### test_get_sync_funcs_to_skip_excludes_sync_only_functions (method, L2267-L2280, parent: TestAsyncReplyFunctionSkipping)

> *Summary: Verifies that the internal method responsible for identifying synchronous functions to bypass during asynchronous chat does not include the code execution reply function. This ensures that sync-only operations, like generating a code execution response, are correctly handled and not excluded from the skipping set.*


### test_custom_sync_only_function_not_skipped (method, L2282-L2294, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that a user-registered, synchronous reply function is correctly included when determining which functions to execute during asynchronous chat. It asserts that the provided `custom_sync_reply` function is present in the set of functions *not* skipped by the agent's async execution logic.*


### test_custom_async_with_sync_equivalent_skips_sync (method, L2296-L2314, parent: TestAsyncReplyFunctionSkipping)

> *Summary: Verifies that when an asynchronous reply function is registered with `ignore_async_in_sync_chat=True`, the corresponding synchronous reply function is automatically added to a skip list. This ensures the synchronous handler is bypassed during asynchronous chat interactions.*


### test_a_generate_reply_skips_sync_with_async_equivalent (method, L2317-L2330, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that the asynchronous reply generation method correctly bypasses synchronous counterparts when available. It asserts that the internal auto-reply counter is incremented exactly once after calling `a_generate_reply` with a predefined message history.*


### test_a_generate_reply_calls_sync_only_functions (method, L2333-L2350, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that the `a_generate_reply` method invokes registered synchronous reply functions when processing messages. It sets up a mock agent and sender, then asserts that the provided sync-only callback was executed exactly once during the reply generation process.*


### test_a_generate_reply_prefers_async_over_sync (method, L2353-L2377, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that an agent prioritizes asynchronous reply functions over synchronous ones when both are registered for the same interaction. It asserts that only the `async` handler is executed and returns its corresponding response when `a_generate_reply` is called.*


### test_two_agent_async_chat_skips_sync_with_async_equivalent (method, L2381-L2449, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that when initiating an asynchronous chat between two agents using `a_run`, the system correctly prioritizes and executes async reply functions over their synchronous counterparts. It asserts that only the designated async handlers are called during the conversation flow, while sync handlers are skipped.*


### test_two_agent_async_chat_calls_sync_only_functions (method, L2453-L2502, parent: TestAsyncReplyFunctionSkipping)

> *Summary: This test verifies that a synchronous reply function is executed even when initiating an asynchronous chat session between two agents. It confirms the correct sequence of calls by asserting that both the registered sync-only and final async reply functions were invoked during the `a_run` process.*

