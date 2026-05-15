# autogen/llm_clients/openai_responses_v2.py

2 function(s): calculate_image_cost, calculate_token_cost. 6 class(es): OpenAIResponsesV2LLMConfigEntry, ApplyPatchCallOutput, ShellCallOutcome, ShellCommandOutput, ShellCallOutput, OpenAIResponsesV2Client. 54 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OpenAIResponsesV2LLMConfigEntry | class |  |
| ApplyPatchCallOutput | class |  |
| ShellCallOutcome | class |  |
| ShellCommandOutput | class |  |
| ShellCallOutput | class |  |
| calculate_image_cost | function |  |
| calculate_token_cost | function |  |
| OpenAIResponsesV2Client | class |  |

## Chunks

### OpenAIResponsesV2LLMConfigEntry (class, L75-L81)

> *Summary: This configuration entry defines settings for using the OpenAI Responses API V2, which is a stateful implementation. It delegates client creation to an external wrapper instead of implementing it directly.*


### create_client (method, L80-L81, parent: OpenAIResponsesV2LLMConfigEntry)

> *Summary: This method intentionally raises a `NotImplementedError`, deferring client creation to the `OpenAIWrapper`'s registration mechanism. It serves as a placeholder indicating that concrete implementation is handled elsewhere in the wrapper class.*


### ApplyPatchCallOutput (class, L85-L105)

> *Summary: Represents the outcome of an `apply_patch` operation (create, update, or delete file) within a workspace. It holds the unique call ID, success status, and descriptive output message, providing a method to serialize itself into a dictionary format for API input.*


### to_dict (method, L103-L105, parent: ApplyPatchCallOutput)

> *Summary: Converts the object's state into a standard Python dictionary using `asdict`. This is used to prepare the response data for consumption by an external Responses API.*


### ShellCallOutcome (class, L109-L125)

> *Summary: Represents the result of a shell command execution, storing whether it exited normally or timed out. It holds a `type` ("exit" or "timeout") and an optional `exit_code`, providing a method to serialize itself into a dictionary.*


### to_dict (method, L123-L125, parent: ShellCallOutcome)

> *Summary: Converts the object's state into a standard Python dictionary using `asdict`. This is used to prepare the response data for consumption by an external API.*


### ShellCommandOutput (class, L129-L150)

> *Summary: Represents the results of a single shell command execution by storing its standard output, standard error, and completion status. It provides a method to serialize this information into a dictionary format suitable for API input.*


### to_dict (method, L145-L150, parent: ShellCommandOutput)

> *Summary: Converts the object's state into a dictionary suitable for the Responses API input. It includes `stdout` and `stderr`, optionally adding a nested `outcome` dictionary if one exists.*


### ShellCallOutput (class, L154-L187)

> *Summary: Represents the complete payload for a shell tool call response, containing a unique `call_id` and a list of individual command outputs. It can be serialized into a dictionary format suitable for API submission, optionally including a maximum output length constraint.*


### __post_init__ (method, L172-L175, parent: ShellCallOutput)

> *Summary: After initialization, this method ensures the `output` attribute defaults to an empty list if it was not explicitly provided during object creation. This guarantees that subsequent operations can safely iterate over or append to the output collection.*


### to_dict (method, L177-L187, parent: ShellCallOutput)

> *Summary: Converts the object's state into a dictionary structure suitable for an OpenAI Responses API input. It includes `call_id` and `type`, optionally adding `max_output_length` and serializing the `output` commands if present.*


### calculate_image_cost (function, L219-L268)

> *Summary: Determines the monetary cost of generating a single image based on specified model, size, and quality settings. It accepts `model`, `size`, and `quality` strings as input and returns a tuple containing the calculated cost (float) and an error message (string or None).*


### calculate_token_cost (function, L271-L314)

> *Summary: Determines the monetary cost of token usage by accepting a model name, prompt tokens, and completion tokens. It calculates the total USD expense using either provided custom pricing or predefined rates from an internal pricing table.*


### OpenAIResponsesV2Client (class, L317-L2857)

> *Summary: This class provides a comprehensive client for OpenAI's Responses API V2, enabling stateful conversations and supporting rich features like structured output, multimodal content (images), web search, and file operations. It accepts various inputs—including messages or raw input items—and outputs a detailed `UnifiedResponse` containing text, citations, generated images, and usage statistics.*


### __init__ (method, L368-L435, parent: OpenAIResponsesV2Client)

> *Summary: Initializes an OpenAI Responses API V2 client by configuring connection parameters like API key and base URL. It sets up various internal states for conversation management, workspace operations, image/web search configurations, cost tracking, and shell execution controls based on provided inputs.*


### _get_previous_response_id (method, L437-L443, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves the stored identifier for the last interaction within the current conversational context. It returns this ID as a string if one exists, or `None` if no previous response has been recorded.*


### _set_previous_response_id (method, L445-L451, parent: OpenAIResponsesV2Client)

> *Summary: Updates the internal state by setting or clearing a `response_id` string within the object. This method modifies the instance's tracking of the last processed response ID.*


### reset_conversation (method, L453-L459, parent: OpenAIResponsesV2Client)

> *Summary: Clears the internal `_previous_response_id` attribute to terminate the current conversational context and initiate a fresh thread. This method is used to switch between distinct conversation states.*


### get_citations (method, L462-L490, parent: OpenAIResponsesV2Client)

> *Summary: Extracts all `CitationContent` objects from a provided `UnifiedResponse`. It iterates through the message content blocks within the response to collect and return a list of these citation objects.*


### get_web_search_calls (method, L493-L521, parent: OpenAIResponsesV2Client)

> *Summary: This function iterates through the messages within a `UnifiedResponse` to extract all content blocks specifically marked as `"web_search_call"`. It returns a list containing these metadata objects, which track performed web searches for debugging or auditing purposes.*


### get_shell_calls (method, L524-L552, parent: OpenAIResponsesV2Client)

> *Summary: This function iterates through the messages within a `UnifiedResponse` to filter and extract all content blocks specifically marked as `"shell_call"`. It returns a list containing these extracted `GenericContent` objects, providing metadata about executed shell commands.*


### get_generated_images (method, L555-L584, parent: OpenAIResponsesV2Client)

> *Summary: Extracts all `ImageContent` objects from a provided `UnifiedResponse`. It iterates through the response's messages and content blocks to collect every image found.*


### get_parsed_content (method, L587-L627, parent: OpenAIResponsesV2Client)

> *Summary: This method extracts structured output from a `UnifiedResponse` by iterating through the message content blocks. It returns the first `GenericContent` block found with the type `"parsed"`, which contains the deserialized data, or `None` if no such content exists.*


### get_parsed_object (method, L630-L655, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves a Pydantic model instance from a `UnifiedResponse` object by first calling a helper method to get the parsed content. It returns this instantiated object if available, otherwise it returns `None`.*


### create_image_content (method, L658-L695, parent: OpenAIResponsesV2Client)

> *Summary: Generates a dictionary structure suitable for multimodal message content by accepting an image URL and an optional detail level. This output is designed to be directly inserted into the `content` array of messages sent to an LLM client.*


### create_multimodal_message (method, L698-L744, parent: OpenAIResponsesV2Client)

> *Summary: Constructs a structured message dictionary suitable for LLM APIs by combining provided text and an optional list of image URLs. It formats the inputs into a `content` array containing distinct text and image objects based on the specified user or assistant role.*


### get_all_images (method, L747-L759, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves every image content block, whether generated or provided as input, from a `UnifiedResponse`. It acts as a semantic alias to call the existing method for extracting generated images.*


### set_image_output_params (method, L761-L815, parent: OpenAIResponsesV2Client)

> *Summary: Configures default parameters for image generation requests by accepting optional inputs like quality, size, background, format, and compression level. These settings are stored internally to apply to all subsequent image tool calls unless explicitly overridden during a request.*


### _build_image_generation_tool_config (method, L817-L857, parent: OpenAIResponsesV2Client)

> *Summary: Constructs a standardized tool configuration dictionary for image generation by merging instance-level parameters with any provided request-specific overrides. It populates the resulting configuration with specified attributes like quality, size, and output format if they are present in the merged settings.*


### get_image_costs (method, L859-L874, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves the accumulated total cost for all images generated by this client instance, which is tracked internally since the API response omits image-specific usage data. It returns this cumulative cost as a floating-point number in USD.*


### reset_image_costs (method, L876-L882, parent: OpenAIResponsesV2Client)

> *Summary: Resets an internal counter tracking accumulated image generation expenses back to zero, allowing for fresh cost tracking in subsequent sessions.*


### get_token_costs (method, L884-L896, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves the accumulated total cost of all tokens consumed by this client instance. It returns this cumulative usage value as a floating-point number representing the cost in USD.*


### reset_token_costs (method, L898-L902, parent: OpenAIResponsesV2Client)

> *Summary: Resets internal counters tracking accumulated token usage for prompts and completions back to zero. This method is used to clear the cost history associated with an LLM client instance.*


### get_total_costs (method, L904-L914, parent: OpenAIResponsesV2Client)

> *Summary: Calculates the aggregate expense by summing stored token and image costs. It returns this total as a floating-point number representing the cumulative cost in USD.*


### reset_all_costs (method, L916-L924, parent: OpenAIResponsesV2Client)

> *Summary: This method resets all internal cost tracking variables, including token and image costs, to zero. It also clears the cumulative counts for prompt and completion tokens.*


### get_cumulative_usage (method, L926-L944, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves a dictionary containing aggregated usage statistics from the client's internal counters. It combines total prompt and completion tokens, along with associated token and image costs to provide overall consumption metrics.*


### set_custom_price (method, L946-L966, parent: OpenAIResponsesV2Client)

> *Summary: This method allows overriding the standard OpenAI pricing by accepting and storing custom rates for input and output tokens per thousand. It updates an internal attribute to use these specified USD values in subsequent cost calculations.*


### clear_custom_price (method, L968-L970, parent: OpenAIResponsesV2Client)

> *Summary: Resets the instance's custom pricing configuration to `None`, causing subsequent operations to revert to using the standard OpenAI price table.*


### get_apply_patch_calls (method, L973-L1001, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves a list of `GenericContent` blocks specifically marked as `"apply_patch_call"` from a provided `UnifiedResponse`. This allows developers to extract metadata detailing file modification operations performed during an API call.*


### _apply_patch_operation (method, L1003-L1132, parent: OpenAIResponsesV2Client)

> *Summary: Executes a file modification (create, update, or delete) on a workspace using the `WorkspaceEditor` tool based on a provided operation dictionary. It handles both synchronous and asynchronous execution paths, returning an output structure containing the call ID, status, and result message.*


### _extract_apply_patch_calls (method, L1134-L1169, parent: OpenAIResponsesV2Client)

> *Summary: Scans a list of messages to locate and extract all instances of `apply_patch_call` objects, which represent file operations. It returns a dictionary mapping each call's ID to its corresponding patch call data.*


### _execute_apply_patch_calls (method, L1171-L1217, parent: OpenAIResponsesV2Client)

> *Summary: Processes a dictionary of patch calls by executing each file operation using the configured tools and workspace context. It returns a list containing the resulting output dictionaries for each successfully executed patch call.*


### _extract_shell_calls (method, L1219-L1254, parent: OpenAIResponsesV2Client)

> *Summary: Scans a list of messages to locate and extract all embedded `shell_call` items, whether they are within the message content or in the `tool_calls`. It returns a dictionary mapping each unique call ID to its corresponding shell call data.*


### _execute_shell_calls (method, L1256-L1311, parent: OpenAIResponsesV2Client)

> *Summary: Processes a dictionary of shell call requests by executing each command within a sandboxed environment. It takes configuration like allowed paths and command lists to control execution and returns a list of structured output dictionaries for each successful operation.*


### _execute_shell_operation (method, L1313-L1463, parent: OpenAIResponsesV2Client)

> *Summary: Executes a list of shell commands using an internal `ShellExecutor`, applying configurable sandboxing, whitelisting, and filtering rules. It accepts command details from an input dictionary and returns a structured `ShellCallOutput` containing the standard output, error streams, and execution status for each command.*


### set_shell_params (method, L1465-L1504, parent: OpenAIResponsesV2Client)

> *Summary: Configures the shell execution environment by setting whitelists, blacklists, and filtering rules for commands. It accepts optional lists of allowed/denied commands, a boolean to enable filtering, and dangerous pattern tuples, then resets the underlying executor to apply these new settings.*


### _get_delta_messages (method, L1506-L1540, parent: OpenAIResponsesV2Client)

> *Summary: This method filters a list of messages to return only the "delta" messages—those that have arrived since the last fully completed response. It iterates backward through the input, stopping when it encounters a message marked as completed and not containing any `apply_patch_call` items.*


### _convert_image_to_input_block (method, L1542-L1594, parent: OpenAIResponsesV2Client)

> *Summary: Transforms various input formats for image content—including Responses API, Chat Completions, direct URLs, and Base64 data URIs—into the standardized `input_image` block required by the Responses API. It accepts a dictionary containing diverse image representations and returns the correctly structured block or `None` upon failure.*


### _convert_messages_to_input (method, L1596-L1686, parent: OpenAIResponsesV2Client)

> *Summary: This method transforms a list of standard chat messages into the specific input format required by the Responses API. It iterates through the messages, converting text and image contents into structured blocks, while also updating external parameters for image generation and appending the resulting items to an output list.*


### _parse_params (method, L1688-L1706, parent: OpenAIResponsesV2Client)

> *Summary: Transforms specific request parameters like `verbosity` and `reasoning_effort` from the input dictionary into nested structures (`text` or `reasoning`) required by the Responses API. It modifies the provided parameter dictionary in place before returning it.*


### _build_web_search_tool_config (method, L1708-L1750, parent: OpenAIResponsesV2Client)

> *Summary: Constructs the configuration dictionary for a web search tool by merging instance-level parameters with optional user-provided settings. It accepts an optional `web_search_config` dict and returns a structured dictionary containing `"type": "web_search"` along with any specified location or context size constraints.*


### set_web_search_params (method, L1752-L1778, parent: OpenAIResponsesV2Client)

> *Summary: Configures default parameters for web search across all subsequent requests by updating an internal dictionary. It accepts optional user location data and a context size ("low", "medium", or "high") to tailor the search behavior.*


### _normalize_messages_for_responses_api (method, L1780-L1854, parent: OpenAIResponsesV2Client)

> *Summary: This method transforms a list of chat messages into the specific format required by the Responses API. It executes file patch calls found within the incoming messages and previous responses, prepending the resulting execution outputs to the normalized message sequence before returning the final structured input.*


### create (method, L1860-L2046, parent: OpenAIResponsesV2Client)

> *Summary: This method initiates an LLM completion request by accepting various parameters like model name, messages, and tool configurations. It intelligently transforms inputs for stateful conversation or structured output before making the call to the underlying client. The function returns a rich `UnifiedResponse` object containing text, citations, images, or parsed data based on the request configuration.*


### _transform_response (method, L2048-L2473, parent: OpenAIResponsesV2Client)

> *Summary: This method converts a raw Responses API response into a standardized `UnifiedResponse` object by iterating through output items. It processes various content types—including text, structured JSON (parsed), function calls, image generations, and web search results—to build the final message content and calculates associated token and image costs for the returned structure.*


### cost (method, L2475-L2492, parent: OpenAIResponsesV2Client)

> *Summary: Retrieves the total monetary cost of an API call from a `UnifiedResponse` object. It returns this combined token and image generation cost as a floating-point number in USD, defaulting to zero if no cost is present.*


### get_usage (method, L2495-L2531, parent: OpenAIResponsesV2Client)

> *Summary: Extracts detailed usage statistics from a `UnifiedResponse` object, returning a dictionary containing token counts (prompt, completion, total), associated costs for tokens and images, the model name, and optionally reasoning tokens.*


### message_retrieval (method, L2533-L2607, parent: OpenAIResponsesV2Client)

> *Summary: Extracts messages from a `UnifiedResponse`, returning a list of strings if all messages are plain text, or a list of structured dictionaries containing roles and complex content (like tool calls or images) otherwise. It processes each message by inspecting its content blocks to determine the appropriate output format.*


### _unified_response_to_chat_completion (method, L2609-L2707, parent: OpenAIResponsesV2Client)

> *Summary: Transforms a detailed `UnifiedResponse` into a backward-compatible `ChatCompletionExtended` object for V1 consumers. It iterates through the response messages, converting various content types (text, reasoning, tool calls, citations, images) into flattened string or structured fields within the output message.*


### create_v1_compatible (method, L2709-L2769, parent: OpenAIResponsesV2Client)

> *Summary: This method takes request parameters and internally calls the primary V2 creation logic, then transforms the resulting unified response into a `ChatCompletionExtended` object. This conversion ensures backward compatibility by presenting the output in the format expected by older V1 interfaces.*


### unified_response_to_v1_messages (method, L2772-L2849, parent: OpenAIResponsesV2Client)

> *Summary: Converts a `UnifiedResponse` object into a V1-compatible message format, returning either a list of simple strings or a list of detailed message dictionaries. It processes the response messages, transforming complex content blocks (like images, tool calls, and citations) into structured dictionary entries while handling plain text as a string.*


### is_v1_compatible (method, L2851-L2857, parent: OpenAIResponsesV2Client)

> *Summary: This method checks the client's capability to operate in a V1 compatible mode, which it always reports as true by design. It returns a boolean indicating support for backward compatibility with an older API version.*

