# autogen/agentchat/conversable_agent.py

3 function(s): register_function, normilize_message_to_oai, message_to_dict. 2 class(es): UpdateSystemMessage, ConversableAgent. 135 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| UpdateSystemMessage | class |  |
| ConversableAgent | class |  |
| register_function | function |  |
| normilize_message_to_oai | function |  |
| message_to_dict | function |  |

## Chunks

### UpdateSystemMessage (class, L104-L132)

> *Summary: This class validates the provided content updater, which dictates how an agent's system message is modified before responding. It ensures the input is either a format string (checking for variables) or a callable matching the required signature: `(ConversableAgent, List[Dict[str, Any]]) -> str`.*


### __post_init__ (method, L116-L132, parent: UpdateSystemMessage)

> *Summary: Validates the `content_updater` attribute after initialization, ensuring it is either a string containing placeholders or a callable that accepts two specific arguments and returns a string. It issues warnings if a string lacks variables or raises errors for incorrect types or signatures in the provided updater function.*


### ConversableAgent (class, L136-L4573)

> *Summary: This class provides a comprehensive framework for creating conversational AI agents, allowing configuration of LLM interaction, tool/function execution, and human feedback loops. It manages the entire chat lifecycle—from receiving messages to generating replies via various methods (LLM, code, functions)—and supports both synchronous and asynchronous operation modes.*


### __init__ (method, L157-L390, parent: ConversableAgent)

> *Summary: Initializes an agent with extensive configuration options, accepting parameters like system messages, LLM settings, function maps, and input modes. It sets up internal state management for conversation history, tool execution (including Docker support), reply generation hooks, and various guardrails based on the provided inputs.*


### _validate_name (method, L392-L397, parent: ConversableAgent)

> *Summary: Checks an input string against configuration rules to ensure it does not contain whitespace if OpenAI API type is configured for that setting. Raises a `ValueError` if whitespace is found in the provided name under specific LLM configuration conditions.*


### _get_display_name (method, L399-L407, parent: ConversableAgent)

> *Summary: Retrieves the agent's name as its string representation, allowing customization by overriding this method with another function if needed. It simply returns the value stored in the `self.name` attribute.*


### __str__ (method, L409-L410, parent: ConversableAgent)

> *Summary: Returns a string representation of the agent by calling its internal method to retrieve a display name. This allows the object to be easily represented as text in logs or user interfaces.*


### _add_functions (method, L412-L419, parent: ConversableAgent)

> *Summary: Registers multiple callable functions onto the agent by iterating through a provided list and adding each function individually. It accepts a list of functions as input and modifies the agent's internal state to include these capabilities.*


### _add_single_function (method, L421-L446, parent: ConversableAgent)

> *Summary: Registers a callable function with the agent by setting its name and description for LLM interaction. It prioritizes provided arguments but falls back to the function's own name or docstring if details are missing.*


### _register_update_agent_state_before_reply (method, L448-L494, parent: ConversableAgent)

> *Summary: Registers functions to execute before an agent replies, allowing for pre-speech validation or state modification. It accepts a list or single callable, wrapping `UpdateSystemMessage` types into hooks that update the agent's system message using templates or custom logic.*


### _validate_llm_config (method, L497-L506, parent: ConversableAgent)

> *Summary: This method ensures the provided language model configuration is valid, defaulting to a predefined setting if `None` is passed or returning `False` if explicitly set to `False`. Otherwise, it processes and returns a standardized `LLMConfig` object from the input.*


### _create_client (method, L509-L510, parent: ConversableAgent)

> *Summary: This helper method instantiates an `OpenAIWrapper` object using the provided configuration if it's not explicitly set to `False`. It returns the wrapper instance or `None` based on the input flag.*


### _is_silent (method, L513-L514, parent: ConversableAgent)

> *Summary: Determines the effective silence state for an agent by prioritizing its internal `silent` attribute over a provided default value. It returns a boolean indicating whether the agent should operate silently.*


### name (method, L517-L519, parent: ConversableAgent)

> *Summary: Retrieves the designated identifier for the agent instance. It returns the stored string value representing the agent's name.*


### description (method, L522-L524, parent: ConversableAgent)

> *Summary: Retrieves the stored textual description associated with the agent instance. It returns this pre-defined string attribute as a standard Python string.*


### description (method, L527-L529, parent: ConversableAgent)

> *Summary: Sets an internal string attribute representing the agent's description using a provided `str` input. This method updates the agent's metadata for future use.*


### code_executor (method, L532-L536, parent: ConversableAgent)

> *Summary: Retrieves the internal `CodeExecutor` instance associated with the agent, or returns `None` if no executor has been initialized. This method provides access to the execution environment for running code within the agent's context.*


### register_reply (method, L538-L608, parent: ConversableAgent)

> *Summary: Registers a function to automatically reply based on specified triggers (class, name, agent instance, callable, or list). It manages the order of execution via `position` and handles configuration persistence across chat sessions.*


### replace_reply_func (method, L610-L619, parent: ConversableAgent)

> *Summary: Swaps a specific registered reply function within the agent's list of handlers. It iterates through the internal list, finds the entry matching `old_reply_func`, and updates its associated function to `new_reply_func`.*


### _get_chats_to_run (method, L622-L655, parent: ConversableAgent)

> *Summary: This method processes a queue of potential chats, modifying them by assigning a sender and generating or retrieving the initial message content based on configuration and history. It returns a list containing only those chat configurations that have been successfully prepared to run.*


### _process_nested_chat_carryover (method, L658-L752, parent: ConversableAgent)

> *Summary: This method processes messages from a parent chat to create context for a nested chat. It takes the chat configuration and message history as input, then generates a single contextual message by summarizing or including all/last messages based on the specified `summary_method`, finally updating the chat's message field with this new context.*


### _process_chat_queue_carryover (method, L755-L798, parent: ConversableAgent)

> *Summary: Determines if the initial chat in a queue requires message restoration based on its configuration. It processes nested chat carryover using provided agents, messages, and LLM settings, returning a flag indicating restoration necessity and the original message content if applicable.*


### _summary_from_nested_chats (method, L801-L837, parent: ConversableAgent)

> *Summary: This method orchestrates a sequence of nested chats between specified agents by initiating them based on the provided queue and configuration. It extracts and returns a summary from the final chat in the sequence, handling potential message carryover configurations for the initial nested chat.*


### _a_summary_from_nested_chats (method, L840-L877, parent: ConversableAgent)

> *Summary: This asynchronous method initiates one or more nested chats between a recipient and agents in a queue, optionally carrying over messages from a parent chat. It then extracts and returns a summary generated by the last executed chat based on its configured `summary_method`.*


### register_nested_chats (method, L879-L943, parent: ConversableAgent)

> *Summary: Registers a nested chat reply mechanism by associating a specific function with a given trigger. It accepts a queue of chats, a trigger condition, and configuration options to determine how the nested conversation's output is processed and returned as a reply.*


### system_message (method, L946-L948, parent: ConversableAgent)

> *Summary: Retrieves and returns the predefined system instruction string from the agent's internal configuration. This method accesses the first element of the `_oai_system_message` list to provide context for interactions.*


### update_system_message (method, L950-L956, parent: ConversableAgent)

> *Summary: Modifies the agent's internal configuration by replacing the content of the first system message with the provided string. This updates the instruction set used for subsequent chat completions.*


### update_max_consecutive_auto_reply (method, L958-L970, parent: ConversableAgent)

> *Summary: Sets the maximum allowed consecutive auto replies, either globally across all agents or specifically for a given agent instance. If an agent is provided, it updates only that agent's limit within the internal dictionary; otherwise, it sets the global limit and applies it to all tracked agents.*


### max_consecutive_auto_reply (method, L972-L974, parent: ConversableAgent)

> *Summary: Retrieves the configured limit for sequential automated responses, returning a global default if no specific agent is provided, or an agent-specific limit otherwise.*


### chat_messages (method, L977-L979, parent: ConversableAgent)

> *Summary: Returns a dictionary mapping each `Agent` instance to a list of its associated message dictionaries. This provides access to the complete conversation history for all agents managed by the object.*


### chat_messages_for_summary (method, L981-L983, parent: ConversableAgent)

> *Summary: Retrieves the complete message history for a specified agent from internal storage. This method returns a list of dictionaries representing the entire conversation transcript.*


### last_message (method, L985-L1009, parent: ConversableAgent)

> *Summary: Retrieves the most recent message from a conversation, either by specifying an `Agent` instance or by inspecting all stored conversations. If no agent is provided and multiple conversations exist, it raises an error; otherwise, it returns the last message dictionary or `None`.*


### use_docker (method, L1012-L1016, parent: ConversableAgent)

> *Summary: Returns a boolean indicating Docker usage, the specific Docker image name as a string, or `None` if code execution is disabled based on the agent's configuration. This method checks the internal configuration to determine how code execution should be handled regarding containerization.*


### _message_to_dict (method, L1019-L1029, parent: ConversableAgent)

> *Summary: Transforms an input that can be a string or a dictionary into a standardized dictionary format. If the input is a string, it wraps it in a `{"content": ...}` structure; otherwise, it returns the input as-is if it's already a dictionary.*


### _normalize_name (method, L1032-L1037, parent: ConversableAgent)

> *Summary: This method sanitizes a given string by replacing any characters that are not alphanumeric, underscore, or hyphen with an underscore. It also truncates the resulting string to a maximum length of 64 characters.*


### _assert_valid_name (method, L1040-L1049, parent: ConversableAgent)

> *Summary: Validates an input string to ensure it conforms to naming conventions, allowing only alphanumeric characters, underscores, and hyphens, while also enforcing a maximum length of 64 characters. If the provided `name` fails these checks, it raises a `ValueError`.*


### _append_oai_message (method, L1051-L1078, parent: ConversableAgent)

> *Summary: Normalizes and appends a message to an agent's conversation history for OpenAI compatibility. It accepts either a string or a dictionary, validates its structure based on the provided role, and returns `True` if successfully added, otherwise `False`.*


### _process_message_before_send (method, L1080-L1089, parent: ConversableAgent)

> *Summary: This method iterates through registered hooks to modify a message before it is sent to another agent. It accepts the message content and the target agent as input, returning the potentially modified message.*


### send (method, L1091-L1137, parent: ConversableAgent)

> *Summary: Sends a structured message to another agent, accepting either a string or a dictionary containing content and optional metadata like function calls. It processes the input, ensures it conforms to chat completion standards, and then delivers it to the specified recipient's `receive` method.*


### a_send (method, L1139-L1185, parent: ConversableAgent)

> *Summary: Sends a structured message to another agent, accepting either a string or a dictionary containing content and optional metadata like function calls. It processes the input, ensures it conforms to chat completion standards, and then asynchronously delivers it to the specified recipient.*


### _print_received_message (method, L1187-L1192, parent: ConversableAgent)

> *Summary: This method processes an incoming message, converting it to a dictionary and wrapping it into a structured event model using the sender and recipient context. It then sends this fully formed message model through the default I/O stream for output or logging.*


### _process_received_message (method, L1194-L1206, parent: ConversableAgent)

> *Summary: This method processes an incoming message from a specified agent, ensuring it's formatted correctly as a "user" role message for the underlying AI model. It validates the message content and optionally prints it to the console if not running in silent mode.*


### receive (method, L1208-L1243, parent: ConversableAgent)

> *Summary: Processes an incoming message from another agent, which can be a string or a structured dictionary containing content and metadata like role or tool calls. Based on configuration, it either stops processing or generates and sends a reply back to the original sender.*


### a_receive (method, L1245-L1280, parent: ConversableAgent)

> *Summary: Processes an incoming message from another agent, which can be a string or a structured dictionary containing content or tool calls. Based on configuration and the `request_reply` flag, it either stops processing or asynchronously generates and sends a reply back to the original sender.*


### _prepare_chat (method, L1282-L1295, parent: ConversableAgent)

> *Summary: This method configures the current agent's state for interaction with a specified recipient. It resets counters, sets reply behavior flags, optionally clears conversation history, and recursively prepares the recipient agent if requested.*


### _raise_exception_on_async_reply_functions (method, L1297-L1314, parent: ConversableAgent)

> *Summary: Checks the agent's registered reply functions to ensure no asynchronous methods are present. If any coroutine-callable functions are found, it raises a `RuntimeError` because they require an asynchronous chat initiation method.*


### _should_terminate_chat (method, L1316-L1334, parent: ConversableAgent)

> *Summary: Checks if a conversation should end by verifying the message content and calling a specific termination method on the recipient agent. It returns `True` only if the recipient is an agent, the message has content, and the agent's internal termination check passes for that message.*


### initiate_chat (method, L1336-L1496, parent: ConversableAgent)

> *Summary: This method initiates a conversation between two agents, optionally clearing history and setting limits on turns. It accepts an initial message (or a callable to generate one), configuration for summarization, and optional context data via keyword arguments. The function returns a `ChatResult` containing the full chat history, a generated summary, usage cost, and human input details.*


### run (method, L1498-L1636, parent: ConversableAgent)

> *Summary: Initiates a chat session asynchronously in a background thread, either with another agent or by creating an executor for single-agent mode. It accepts various configuration parameters like history clearing, turn limits, and summarization methods, returning immediately with a `RunResponseProtocol` object that streams events as the conversation progresses.*


### run_iter (method, L1638-L1774, parent: ConversableAgent)

> *Summary: Initiates an iterative chat session between agents by spawning a background thread that yields events as they occur. It accepts various configuration parameters like initial messages, turn limits, summarization methods, and tools to control the conversation flow. The output is a `RunIterResponse` object containing the necessary function to start the event-yielding process.*


### a_initiate_chat (method, L1776-L1852, parent: ConversableAgent)

> *Summary: Initiates a conversational exchange with another agent, optionally clearing history and limiting the number of turns. It generates initial messages, iteratively sends replies based on conversation flow or turn limits, and finally returns a `ChatResult` containing the full history, summary, and usage cost.*


### a_run (method, L1854-L1962, parent: ConversableAgent)

> *Summary: Executes an asynchronous conversation run between agents, optionally involving a recipient agent or initiating a chat with the user. It manages execution flow, handles input/output streams, and returns a response object containing the final chat history, summary, and cost upon completion.*


### a_run_iter (method, L1964-L2105, parent: ConversableAgent)

> *Summary: Initiates an asynchronous chat session by spawning a background thread that runs the conversation. It accepts configuration for recipients, history clearing, message content, and summarization methods to yield events as they occur during the interaction.*


### _summarize_chat (method, L2107-L2156, parent: ConversableAgent)

> *Summary: Retrieves a chat summary by executing a specified method against the agent, optionally using a provided cache for performance. It accepts a `summary_method` (callable or string), arguments, and an optional recipient agent to generate and return a final string summary.*


### _last_msg_as_summary (method, L2159-L2173, parent: ConversableAgent)

> *Summary: Extracts a summary string from the recipient's most recent message directed at the sender. It processes the content, stripping any "TERMINATE" markers whether it is a string or within a list of message dictionaries.*


### _reflection_with_llm_as_summary (method, L2176-L2195, parent: ConversableAgent)

> *Summary: Generates a conversational summary by prompting an LLM agent with a specified prompt and the chat history between two agents. It handles missing or invalid prompts/roles, falling back to a default prompt or returning an empty string upon failure.*


### _reflection_with_llm (method, L2197-L2232, parent: ConversableAgent)

> *Summary: Generates a chat summary by sending the conversation history and a system prompt to an LLM client. It constructs the input by prepending the system prompt to the provided message list and returns the resulting text response from the LLM call.*


### _check_chat_queue_for_sender (method, L2234-L2248, parent: ConversableAgent)

> *Summary: Iterates over a list of chat dictionaries, ensuring each entry has a "sender" key by assigning the agent instance if it's currently missing. It returns a new list containing all the processed chat information.*


### initiate_chats (method, L2250-L2262, parent: ConversableAgent)

> *Summary: This method starts multiple concurrent chats based on a provided queue of chat configuration dictionaries. It processes the input queue, initiates the necessary conversations internally, and returns a list of results for all completed chats.*


### sequential_run (method, L2264-L2327, parent: ConversableAgent)

> *Summary: Executes multiple agent chats sequentially by processing a queue of chat configurations using separate I/O streams for each. It initiates each chat via the specified sender and returns a list of `RunResponseProtocol` objects representing the results once all initiated chats have completed or encountered an error.*


### a_initiate_chats (method, L2329-L2332, parent: ConversableAgent)

> *Summary: This method processes an incoming list of chat requests by first filtering them based on the sender. It then asynchronously initiates these filtered chats and returns a dictionary mapping chat IDs to their respective results.*


### a_sequential_run (method, L2334-L2398, parent: ConversableAgent)

> *Summary: This method sequentially initiates chats for a provided queue of chat configurations, managing I/O streams and collecting results. It processes each chat by calling the sender's `a_initiate_chat` method and sends completion or error events to the corresponding stream.*


### get_chat_results (method, L2400-L2405, parent: ConversableAgent)

> *Summary: Retrieves a specific `ChatResult` or all finished chat results based on an optional index. It returns the single result if an index is provided, otherwise it yields the entire list of completed chats.*


### reset (method, L2407-L2418, parent: ConversableAgent)

> *Summary: This method resets the agent's state by clearing conversation history, resetting reply counters and stop conditions, and optionally calling reset configurations for registered reply functions. It also reinitializes the configuration for each reply function if no specific reset hook is provided.*


### stop_reply_at_receive (method, L2420-L2425, parent: ConversableAgent)

> *Summary: Resets a tracking mechanism for replies, either clearing all recorded states if no specific agent is provided or setting the reply status to false for a given sender. This method modifies the internal `reply_at_receive` state based on the input agent.*


### reset_consecutive_auto_reply_counter (method, L2427-L2432, parent: ConversableAgent)

> *Summary: Resets a counter tracking consecutive automatic replies, either clearing the global count if no specific sender is provided or resetting the count for a given agent instance. This method modifies the internal state to reflect a fresh start in automated responses.*


### clear_history (method, L2434-L2463, parent: ConversableAgent)

> *Summary: This method manages the chat history of an agent, optionally clearing it for a specific recipient or all conversations. It accepts an optional `recipient` and `nr_messages_to_preserve`, allowing it to either completely wipe the history or retain the most recent messages while notifying listeners of the action.*


### generate_oai_reply (method, L2465-L2497, parent: ConversableAgent)

> *Summary: This method generates a response from an OpenAI model by taking a list of messages and optional configuration. It processes the input messages through safeguards before calling the LLM client and then validates the resulting output against another safeguard hook.*


### _generate_oai_reply_from_client (method, L2499-L2547, parent: ConversableAgent)

> *Summary: Processes a list of messages, incorporating any embedded tool responses into a unified message history. It then sends this compiled history to an LLM client and returns the resulting text or structured dictionary response after normalizing function/tool call names for API compatibility.*


### a_generate_oai_reply (method, L2549-L2576, parent: ConversableAgent)

> *Summary: This asynchronous method wraps a synchronous call to generate an OpenAI reply. It accepts message history, a sender agent, and configuration, returning a tuple indicating success and the generated response content.*


### _generate_code_execution_reply_using_executor (method, L2578-L2627, parent: ConversableAgent)

> *Summary: This method generates a reply by executing code blocks found within the most recent messages provided as input. It processes up to a configurable number of preceding messages, sending an event upon finding code and returning a success status along with execution results if any code is run.*


### generate_code_execution_reply (method, L2629-L2677, parent: ConversableAgent)

> *Summary: Generates a reply by executing code blocks found within the most recent messages provided or stored for an agent. It processes up to a configurable number of preceding messages, executes any detected code, and returns success status along with execution logs if code is found and run.*


### _run_async_in_thread (method, L2679-L2692, parent: ConversableAgent)

> *Summary: Executes an asynchronous coroutine within a dedicated background thread, managing its own event loop to prevent blocking the main execution flow. It returns the final resolved value of the provided coroutine after the thread completes its task.*


### generate_function_call_reply (method, L2694-L2720, parent: ConversableAgent)

> *Summary: This method processes the last message in a conversation to generate a reply based on a function call request. It executes the specified tool/function synchronously or asynchronously using provided messages and configuration to return a success status along with the function's output.*


### a_generate_function_call_reply (method, L2722-L2749, parent: ConversableAgent)

> *Summary: This method generates a response by executing a function call specified in the last message of a conversation history. It takes messages and an agent instance as input, returning a boolean indicating success and the resulting data from the executed tool or function.*


### _str_for_tool_response (method, L2751-L2752, parent: ConversableAgent)

> *Summary: Converts a dictionary containing a tool response into a string by extracting the "content" key, defaulting to an empty string if it's missing. This ensures the raw tool output is safely represented as text for further processing.*


### generate_tool_calls_reply (method, L2754-L2814, parent: ConversableAgent)

> *Summary: This method executes functions specified in the last message's `tool_calls`, handling both synchronous and asynchronous execution. It takes a list of messages and an optional sender/config, returning a boolean indicating success and a dictionary containing tool responses or arguments for structured output.*


### _a_execute_tool_call (method, L2816-L2824, parent: ConversableAgent)

> *Summary: This method executes a specified tool call by invoking the corresponding function and then formats the result into a structured message. It takes a `tool_call` dictionary as input and returns a dictionary representing the tool's output with its ID, role, and content.*


### a_generate_tool_calls_reply (method, L2826-L2849, parent: ConversableAgent)

> *Summary: Executes asynchronous tool calls based on the last message's `tool_calls` within a provided conversation history. It returns a boolean indicating if tools were called and a dictionary containing the aggregated tool responses if they were executed.*


### check_termination_and_human_reply (method, L2851-L2998, parent: ConversableAgent)

> *Summary: Determines conversation termination and gathers human feedback based on configured modes ('ALWAYS', 'NEVER', 'TERMINATE'). It processes the last message to check for termination conditions or prompts the user for input, returning a tuple indicating if the chat should stop and any received human reply.*


### a_check_termination_and_human_reply (method, L3000-L3142, parent: ConversableAgent)

> *Summary: Determines if a conversation should end or if human input is required based on message history and configuration. It handles various modes for user interaction ('ALWAYS', 'NEVER', 'TERMINATE'), manages auto-reply counters, and returns a tuple indicating termination status and the resulting human reply (or an interruption response).*


### generate_reply (method, L3144-L3215, parent: ConversableAgent)

> *Summary: Generates a response by sequentially executing registered reply functions based on conversation history or an agent instance. It processes the input messages through several hooks before iterating over handlers, returning the first non-final result or a default reply if none are triggered.*


### a_generate_reply (method, L3217-L3291, parent: ConversableAgent)

> *Summary: Generates a response by sequentially executing registered reply functions based on conversation history and the sender. It processes input messages through several hooks before iterating through configured replies, returning the first non-terminating result or a default reply if none are generated.*


### _get_sync_funcs_to_skip_in_async_chat (method, L3293-L3315, parent: ConversableAgent)

> *Summary: Determines which synchronous reply functions should be bypassed during asynchronous chat execution. It scans registered functions, identifying async methods prefixed with `a_` that have a corresponding non-async counterpart to skip in the async context.*


### _match_trigger (method, L3317-L3349, parent: ConversableAgent)

> *Summary: Determines if a given `sender` agent satisfies a specified `trigger` condition. It handles various trigger types—including strings (matching names), types (checking inheritance), agents, callables, or lists of triggers—returning `True` upon a match or `False` otherwise.*


### get_human_input (method, L3351-L3370, parent: ConversableAgent)

> *Summary: Retrieves user input by prompting with a given string and using an optional `InputStream`. It processes the raw reply through internal hooks before appending it to the agent's history and returning the final string.*


### a_get_human_input (method, L3372-L3392, parent: ConversableAgent)

> *Summary: Retrieves user input asynchronously by calling an `input` function from a provided or default stream. It handles both coroutine and synchronous input functions, appending the received response to the agent's history before returning it.*


### run_code (method, L3394-L3409, parent: ConversableAgent)

> *Summary: Executes a provided string of code using an underlying `execute_code` function. It returns a tuple containing the process exit code, execution logs, and the Docker image utilized during the run.*


### execute_code_blocks (method, L3411-L3446, parent: ConversableAgent)

> *Summary: Processes a list of code blocks by sending execution events and running the code using `run_code` based on its detected or specified language (bash/shell or Python). It aggregates all output logs and immediately returns an error if any executed block fails.*


### _format_json_str (method, L3449-L3476, parent: ConversableAgent)

> *Summary: This utility cleans a raw JSON string by removing newlines that appear outside of quoted values to ensure valid parsing. It also escapes internal newline (`\n`) and tab (`\t`) characters within quotes, preparing the string for reliable JSON deserialization.*


### execute_function (method, L3478-L3551, parent: ConversableAgent)

> *Summary: Executes a specified function by looking up its name in an internal map and parsing arguments from the input dictionary. It returns a tuple indicating execution success along with a result dictionary containing the function's name, role ("function"), and output content.*


### a_execute_function (method, L3553-L3625, parent: ConversableAgent)

> *Summary: Executes a specified asynchronous or synchronous function based on provided arguments extracted from a `func_call` dictionary. It returns a tuple indicating execution success and a result dictionary containing the function's name, role ("function"), and output content.*


### generate_init_message (method, L3627-L3644, parent: ConversableAgent)

> *Summary: This method creates the starting prompt for an agent by either using a provided input or prompting the user if none is given. It then processes this message, incorporating any specified "carryover" context from keyword arguments before returning the final string or dictionary representation.*


### _handle_carryover (method, L3646-L3665, parent: ConversableAgent)

> *Summary: This method processes an incoming message, applying carryover logic if the `kwargs` contain a "carryover" flag. It handles both string and dictionary inputs, routing text content to a standard processor and multimodal content (lists) to a specialized one before returning the potentially modified message structure.*


### _process_carryover (method, L3667-L3681, parent: ConversableAgent)

> *Summary: Appends context information to an existing message based on the `carryover` provided in keyword arguments. It handles both string and list inputs for the carryover, formatting them appropriately before returning the augmented content string.*


### _process_multimodal_carryover (method, L3683-L3689, parent: ConversableAgent)

> *Summary: If a `carryover` context is provided in the arguments, this method prepends a text message containing that context to the input list of multimodal messages. Otherwise, it returns the original content unchanged.*


### a_generate_init_message (method, L3691-L3710, parent: ConversableAgent)

> *Summary: This method generates the starting message for an agent, either by using a provided input or prompting the user if none is given. It then processes this initial message, incorporating any specified carryover information from keyword arguments before returning the final string or dictionary representation.*


### tools (method, L3713-L3718, parent: ConversableAgent)

> *Summary: Returns a shallow copy of the internal list of available `Tool` objects registered with the agent for LLM interaction. This method ensures external modifications do not affect the agent's actual toolset.*


### remove_tool_for_llm (method, L3720-L3726, parent: ConversableAgent)

> *Summary: This method unregisters a specified tool from the LLM's available tools and removes it from the internal tool collection. It raises an error if the provided tool is not currently registered.*


### register_function (method, L3728-L3742, parent: ConversableAgent)

> *Summary: This method updates the agent's internal function registry using a provided map of names to functions. It handles overwriting existing functions with warnings and ensures that any entries mapped to `None` are removed from the active set.*


### update_function_signature (method, L3744-L3795, parent: ConversableAgent)

> *Summary: Modifies the agent's LLM configuration by either adding or removing a specified function signature from its list of available functions. It accepts a function definition (as a dictionary) or a name to remove, and updates the internal `llm_config` before re-initializing the OpenAI client wrapper.*


### update_tool_signature (method, L3797-L3817, parent: ConversableAgent)

> *Summary: Modifies the agent's LLM configuration by updating or removing a specified tool signature within its settings. It takes the tool definition/name, a boolean indicating removal, and an optional flag for silent overrides before re-initializing the client wrapper with the updated configuration.*


### _update_tool_config (method, L3819-L3873, parent: ConversableAgent)

> *Summary: Modifies the tool configuration within an agent's LLM settings based on whether a tool should be added or removed. It accepts the current configuration, the tool signature (as a string or dictionary), and a flag indicating removal, returning the updated configuration dictionary.*


### can_execute_function (method, L3875-L3878, parent: ConversableAgent)

> *Summary: Checks if an agent possesses the capability to run specified functions. It accepts a single function name or a list of names and returns `True` only if every requested function is present in the agent's internal map.*


### function_map (method, L3881-L3883, parent: ConversableAgent)

> *Summary: Provides a dictionary mapping string names to callable functions that the agent can execute. This method returns the internally stored function registry.*


### _wrap_function (method, L3885-L3920, parent: ConversableAgent)

> *Summary: This method decorates a given function to inject chat context parameters and optionally serialize its return value. It dynamically returns either a synchronous or asynchronous wrapper based on the input function's nature, ensuring logging occurs upon execution.*


### _create_tool_if_needed (method, L3923-L3938, parent: ConversableAgent)

> *Summary: This utility ensures an input is represented as a `Tool` object. It accepts either a callable function or an existing `Tool`, optionally wrapping it with provided names and descriptions before returning the finalized `Tool`.*


### register_for_llm (method, L3940-L4012, parent: ConversableAgent)

> *Summary: This factory method returns a decorator that registers a provided function or tool with an agent for LLM interaction. It accepts optional parameters like `name`, `description`, and `api_style` to configure how the function is presented to the language model, ultimately returning the registered tool object.*


### _register_for_llm (method, L4014-L4037, parent: ConversableAgent)

> *Summary: This method registers a provided `Tool` with the agent's LLM configuration, either as a function or a tool based on the specified `api_style`. It requires an existing LLM configuration and handles registration or removal of the tool signature accordingly.*


### set_ui_tools (method, L4039-L4059, parent: ConversableAgent)

> *Summary: Replaces the agent's existing user interface tools by first clearing any previous ones. It then iterates through the provided list of `Tool` objects, registering each with both the LLM and the execution system before updating the internal tool reference.*


### unset_ui_tools (method, L4061-L4068, parent: ConversableAgent)

> *Summary: Removes specified `Tool` objects from the agent's available UI tools by iterating through the input list and calling an internal removal method for each one.*


### _unset_previous_ui_tools (method, L4070-L4084, parent: ConversableAgent)

> *Summary: Clears previously registered user interface tools associated with the agent. It removes these tools from both the internal tool list and the function mapping dictionary, then resets the UI tools list to empty.*


### register_for_execution (method, L4086-L4141, parent: ConversableAgent)

> *Summary: This method acts as a decorator factory that returns a decorator used to register a function or tool with an agent. It takes optional metadata like name and description, then wraps the provided callable into a structured `Tool` object before registering it internally for agent execution.*


### register_model_client (method, L4143-L4150, parent: ConversableAgent)

> *Summary: This method registers a specific model client class and its initialization arguments with an internal client object. It delegates the registration process to the `self.client` instance using the provided class and keyword arguments.*


### register_hook (method, L4152-L4163, parent: ConversableAgent)

> *Summary: Adds a callable function to execute when a specific agent method is invoked. It requires the name of a predefined hook point and an instance implementing `AgentCapability`, appending the new hook to an ordered list for execution.*


### update_agent_state_before_reply (method, L4165-L4174, parent: ConversableAgent)

> *Summary: Executes registered state update hooks against a list of message dictionaries. This method allows external logic to modify the agent's internal context or the provided messages before generating a response.*


### process_all_messages_before_reply (method, L4176-L4187, parent: ConversableAgent)

> *Summary: This method executes all registered capability hooks sequentially against a list of input messages. It returns the final, potentially modified, list of messages after every hook has been applied.*


### process_last_received_message (method, L4189-L4228, parent: ConversableAgent)

> *Summary: This method applies registered capability hooks to modify the content of the final message in a list, provided it's not a function call, context-bearing, or exit command. It returns the original message list if no applicable hooks exist or if the last message is ineligible for processing.*


### _process_tool_input (method, L4230-L4245, parent: ConversableAgent)

> *Summary: This method iterates over registered safeguard hooks, applying each one sequentially to the provided tool input dictionary. It returns the final processed input or `None` immediately if any hook rejects the input.*


### _process_tool_output (method, L4247-L4260, parent: ConversableAgent)

> *Summary: This method iterates over a list of registered safeguard hooks, applying each one sequentially to an incoming tool output dictionary. It returns the final, potentially modified, response after all applicable hooks have executed.*


### _process_llm_input (method, L4262-L4277, parent: ConversableAgent)

> *Summary: This method filters and modifies a list of message dictionaries by sequentially applying registered "safeguard\_llm\_inputs" hooks. It returns the fully processed messages, or `None` immediately if any hook rejects the input.*


### _process_llm_output (method, L4279-L4292, parent: ConversableAgent)

> *Summary: This method applies a series of registered safety hooks to an incoming LLM response, which can be a string or dictionary. It iterates through all configured "safeguard\_llm\_outputs" hooks, passing the output of one hook as the input to the next, and returns the final processed result.*


### _process_human_input (method, L4294-L4309, parent: ConversableAgent)

> *Summary: This method takes a string of user input and passes it sequentially through all registered "safeguard\_human\_inputs" hooks. It returns the final processed string, or `None` immediately if any hook filters the input to `None`.*


### print_usage_summary (method, L4311-L4320, parent: ConversableAgent)

> *Summary: This method outputs a usage summary event, either directly to the default IO stream or via an associated client. It conditionally calls the client's own print\_usage\_summary method if a client object exists, using the provided mode for output.*


### get_actual_usage (method, L4322-L4327, parent: ConversableAgent)

> *Summary: Retrieves a dictionary summarizing the agent's actual usage if an associated client exists; otherwise, it returns `None`.*


### get_total_usage (method, L4329-L4334, parent: ConversableAgent)

> *Summary: Retrieves a dictionary summarizing the agent's total usage if an associated client exists; otherwise, it returns `None`.*


### _create_or_get_executor (method, L4337-L4397, parent: ConversableAgent)

> *Summary: This method constructs or retrieves a specialized agent designed to execute tools, accepting configuration arguments and optional tools as input. It configures the executor with provided tools, registers them for execution and LLM interaction, and yields the resulting `ConversableAgent` instance.*


### _deprecated_run (method, L4399-L4448, parent: ConversableAgent)

> *Summary: Executes a conversational chat session with an agent by initiating a dialogue using the provided message and configuration. It accepts optional arguments for tools, execution parameters, turn limits, history control, and summarization method, returning a `ChatResult`.*


### _deprecated_a_run (method, L4450-L4499, parent: ConversableAgent)

> *Summary: Executes an asynchronous chat session with the agent by initiating a conversation using a provided message and optional configurations like tools or turn limits. It manages the interaction flow, allowing for user input control and providing a final `ChatResult` after the exchange concludes.*


### register_handoff (method, L4501-L4507, parent: ConversableAgent)

> *Summary: Adds a specified context-aware or general condition to the agent's set of registered handoff triggers. This method takes one condition object as input and stores it internally for future evaluation.*


### register_handoffs (method, L4509-L4515, parent: ConversableAgent)

> *Summary: Adds a collection of specified context or general conditions to the agent's registered handoffs. It takes a list of condition objects and adds them to an internal set for future evaluation.*


### register_input_guardrail (method, L4517-L4523, parent: ConversableAgent)

> *Summary: Adds a specified `Guardrail` object to the agent's list of input validators. This allows the agent to enforce specific constraints on incoming prompts before processing them.*


### register_input_guardrails (method, L4525-L4531, parent: ConversableAgent)

> *Summary: Adds a collection of `Guardrail` objects to the agent's internal list, enabling subsequent input validation checks against these registered rules.*


### register_output_guardrail (method, L4533-L4539, parent: ConversableAgent)

> *Summary: Adds a specified `Guardrail` object to the agent's list of output validators. This allows the agent to enforce specific constraints on its generated responses after they are produced.*


### register_output_guardrails (method, L4541-L4547, parent: ConversableAgent)

> *Summary: Adds a collection of `Guardrail` objects to the agent's internal list, enabling subsequent output validation checks against these registered rules.*


### run_input_guardrails (method, L4549-L4560, parent: ConversableAgent)

> *Summary: Checks a list of input messages against configured guardrails sequentially. It returns the result of the first activated guardrail, or `None` if no guardrails are triggered.*


### run_output_guardrails (method, L4562-L4573, parent: ConversableAgent)

> *Summary: This method iterates through configured output guardrails, checking the agent's generated reply (string or dictionary) against each one. It returns the result of the first activated guardrail, or `None` if no guardrails are triggered.*


### register_function (function, L4577-L4601)

> *Summary: This utility registers a given function to be both proposed by one agent and executed by another. It wraps the provided function with metadata specifying its name and a descriptive prompt for LLM interpretation.*


### normilize_message_to_oai (function, L4604-L4650)

> *Summary: Transforms an input message (dict or string) into the specific dictionary format required by OpenAI APIs. It selectively copies relevant fields like content and tool calls, adjusts roles based on message type or overrides, and ensures necessary fields are present before returning a success flag and the formatted message.*


### message_to_dict (function, L4653-L4663)

> *Summary: Transforms an input that can be a string or a dictionary into a standardized dictionary format. If the input is a string, it wraps it in a `{"content": ...}` structure; otherwise, it returns the input as-is if it's already a dictionary, or attempts to cast other types to a dictionary.*

