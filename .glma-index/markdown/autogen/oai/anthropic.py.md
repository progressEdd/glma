# autogen/oai/anthropic.py

14 function(s): supports_native_structured_outputs, has_messages_parse_api, _is_text_block, _is_tool_use_block, _is_thinking_block, transform_schema_for_anthropic, _format_json_response, process_image_content, process_message_content, _extract_system_message and 4 more. 3 class(es): AnthropicEntryDict, AnthropicLLMConfigEntry, AnthropicClient. 29 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| supports_native_structured_outputs | function |  |
| has_messages_parse_api | function |  |
| _is_text_block | function |  |
| _is_tool_use_block | function |  |
| _is_thinking_block | function |  |
| transform_schema_for_anthropic | function |  |
| AnthropicEntryDict | class |  |
| AnthropicLLMConfigEntry | class |  |
| AnthropicClient | class |  |
| _format_json_response | function |  |
| process_image_content | function |  |
| process_message_content | function |  |
| _extract_system_message | function |  |
| _convert_tool_call_message | function |  |
| _convert_tool_result_message | function |  |
| oai_messages_to_anthropic_messages | function |  |
| _calculate_cost | function |  |

## Chunks

### supports_native_structured_outputs (function, L152-L201)

> *Summary: Determines if a given Claude model supports native structured outputs, which uses constrained decoding for guaranteed schema compliance over prompting methods like JSON Mode. It returns `True` for specific newer models (e.g., Sonnet 4.5+, Opus 4.1+) and `False` otherwise.*


### has_messages_parse_api (function, L204-L222)

> *Summary: Determines if the installed Anthropic SDK supports structured output via `messages.parse()`. It attempts to import `anthropic.resources.messages` and checks for the presence of a `parse` attribute on the `Messages` class, returning `True` or `False` accordingly.*


### _is_text_block (function, L225-L236)

> *Summary: Determines if a given content object represents text by checking its type against `TextBlock` or, if available, `BetaTextBlock`. It returns `True` if the input matches either of these specific block types.*


### _is_tool_use_block (function, L239-L257)

> *Summary: Determines if a given content object represents a tool use block, supporting both `ToolUseBlock` and optional `BetaToolUseBlock` types. It checks the object's type directly or falls back to inspecting its name as a safety measure.*


### _is_thinking_block (function, L260-L276)

> *Summary: Determines if a given content object represents an extended thinking block. It checks the object's actual type against `ThinkingBlock` and falls back to checking its string name if direct type comparison is inconclusive.*


### transform_schema_for_anthropic (function, L279-L336)

> *Summary: This function modifies a JSON schema dictionary to ensure compatibility with Anthropic's structured output requirements. It recursively strips unsupported constraints like numerical/string length limits and enforces `additionalProperties: False` on all objects within the input schema.*


### AnthropicEntryDict (class, L339-L349)

> *Summary: This dictionary structure holds configuration parameters specifically for Anthropic LLM interactions. It accepts settings like timeouts, stop sequences, streaming preference, pricing details, and optional GCP credentials.*


### AnthropicLLMConfigEntry (class, L352-L374)

> *Summary: This configuration class defines parameters for interacting with the Anthropic API, including standard LLM settings like `max_tokens` and `temperature`, alongside provider-specific options such as `top_k` and `stop_sequences`. It serves as a blueprint for setting up an Anthropic client connection.*


### create_client (method, L373-L374, parent: AnthropicLLMConfigEntry)

> *Summary: This method currently raises a `NotImplementedError`, indicating that the concrete implementation for creating an Anthropic LLM client has not yet been provided. It requires subclassing to define how to instantiate the necessary client object.*


### AnthropicClient (class, L378-L1312)

> *Summary: This class manages interactions with the Anthropic API, abstracting away differences between standard, streaming, native structured output, and legacy JSON mode calls. It handles configuration loading from various sources (API keys, AWS/GCP credentials), parameter preparation, response parsing into an OpenAI-compatible format, and cost calculation.*


### __init__ (method, L381-L438, parent: AnthropicClient)

> *Summary: Initializes an API client by reading configuration parameters from keyword arguments or environment variables for Anthropic, AWS, or GCP credentials. Based on the provided keys, it instantiates and stores the appropriate underlying client object (`Anthropic`, `AnthropicVertex`, or `AnthropicBedrock`).*


### load_config (method, L440-L464, parent: AnthropicClient)

> *Summary: This method constructs a configuration dictionary for the Anthropic API by extracting and validating various parameters from an input dictionary. It ensures required fields like `model` are present and applies default values or validation checks to settings such as temperature, token limits, and streaming behavior before returning the finalized configuration.*


### _remove_none_params (method, L466-L477, parent: AnthropicClient)

> *Summary: This method filters a dictionary of API parameters by removing any entries whose values are `None`. It modifies the input dictionary directly to ensure only valid, non-null arguments are sent to the Anthropic API.*


### _prepare_anthropic_params (method, L479-L524, parent: AnthropicClient)

> *Summary: This method transforms generic request parameters and Anthropic-formatted messages into a final dictionary suitable for an Anthropic API call. It handles the conversion of function/tool definitions from OpenAI format to Anthropic's required structure, assigns system prompts and tools, and cleans up any `None` values before returning the complete parameter set.*


### _process_response_content (method, L526-L616, parent: AnthropicClient)

> *Summary: This method transforms an Anthropic `Message` response into an OpenAI-compatible format by parsing its content blocks. It extracts text, identifies function calls as structured tool calls, and determines the completion status, handling both standard and native structured output scenarios.*


### _log_structured_output_fallback (method, L618-L670, parent: AnthropicClient)

> *Summary: When native structured output fails, this method aggregates detailed error information—including the exception type, model name, and request parameters (sanitized)—into a dictionary. It specifically enriches the log with HTTP status codes or response bodies if the failure is due to a `BadRequestError`, finally logging a warning about the fallback to JSON Mode.*


### cost (method, L672-L674, parent: AnthropicClient)

> *Summary: Calculates the monetary cost of an API response by directly accessing the `cost` attribute from the provided response object. This method returns a floating-point number representing the calculated expense based on Anthropic's pricing structure.*


### api_key (method, L677-L678, parent: AnthropicClient)

> *Summary: Retrieves the stored API key associated with the instance. This method returns the private string used for authentication with the service.*


### aws_access_key (method, L681-L682, parent: AnthropicClient)

> *Summary: Retrieves the stored AWS access key from the instance's internal state. This method provides direct read access to the configured credential.*


### aws_secret_key (method, L685-L686, parent: AnthropicClient)

> *Summary: Retrieves the stored AWS secret key from the instance's internal state. This method provides direct access to the configured credential for AWS operations.*


### aws_session_token (method, L689-L690, parent: AnthropicClient)

> *Summary: Retrieves the stored AWS session token from the instance's internal state. This method provides read access to the authentication credential used for AWS interactions.*


### aws_region (method, L693-L694, parent: AnthropicClient)

> *Summary: Retrieves the configured AWS region from the instance's internal state. This method returns a string representing the active AWS region.*


### gcp_project_id (method, L697-L698, parent: AnthropicClient)

> *Summary: Retrieves the configured Google Cloud Platform project ID from the instance's internal state. This method provides direct access to the stored `_gcp_project_id`.*


### gcp_region (method, L701-L702, parent: AnthropicClient)

> *Summary: Retrieves the configured Google Cloud Platform region from the instance's internal state. This method returns a string representing the active GCP region.*


### gcp_auth_token (method, L705-L706, parent: AnthropicClient)

> *Summary: Retrieves the stored Google Cloud Platform authentication token from the instance's internal state. This method provides access to the necessary credentials for authenticated API calls.*


### create (method, L708-L746, parent: AnthropicClient)

> *Summary: This method generates a chat completion by intelligently routing the request based on desired output structure. It prioritizes native structured outputs for modern models, falling back to JSON Mode or standard text completion if schema compliance fails or is not requested. The input is a parameters dictionary, and it returns an OpenAI-compatible `ChatCompletion` object.*


### _create_standard (method, L748-L765, parent: AnthropicClient)

> *Summary: This method generates a standard, non-streaming chat completion by transforming OpenAI-style messages into Anthropic format. It calls the underlying client to create the response and then processes the result to construct and return a `ChatCompletion` object containing text and tool call information.*


### _create_streaming (method, L767-L915, parent: AnthropicClient)

> *Summary: This method processes streaming responses from the Anthropic API by iterating over raw events to build a complete `ChatCompletion` object. It accumulates text and structured data (like tool calls and thinking blocks) while simultaneously emitting real-time updates via an `IOStream`. The final output is a fully constructed completion containing all accumulated content, usage statistics, and finish reason.*


### _create_with_native_structured_output (method, L917-L983, parent: AnthropicClient)

> *Summary: This method generates a completion by leveraging Anthropic's native structured output feature for guaranteed schema compliance. It transforms the desired response format (Pydantic model or dict) into an Anthropic-compatible schema and then calls either `messages.create` or `messages.parse` based on whether tools are involved, finally returning a standardized `ChatCompletion`.*


### _create_with_json_mode (method, L985-L1019, parent: AnthropicClient)

> *Summary: Generates a `ChatCompletion` by calling the Anthropic API using prompt-based JSON mode for older models lacking native structured output support. It takes request parameters, calls the underlying client, and then extracts and serializes any JSON found within `<json_response>` tags from the response.*


### _build_chat_completion (method, L1021-L1068, parent: AnthropicClient)

> *Summary: Transforms an Anthropic `Message` response into an OpenAI-compatible `ChatCompletion` object. It constructs the output by packaging the processed message content, tool calls, and usage statistics from the input response and parameters.*


### message_retrieval (method, L1070-L1100, parent: AnthropicClient)

> *Summary: Extracts content from an API response, returning either a list of strings or full message objects depending on the presence of tool/function calls. It uses a `FormatterProtocol` if available to apply custom formatting to the message content before returning it.*


### openai_func_to_anthropic (method, L1103-L1115, parent: AnthropicClient)

> *Summary: Transforms an OpenAI function definition dictionary into the format expected by Anthropic models. It renames the `parameters` key to `input_schema` and conditionally modifies the schema if a `strict` flag is present, ensuring compatibility with Anthropic's structured output requirements.*


### get_usage (method, L1118-L1126, parent: AnthropicClient)

> *Summary: Extracts token counts (prompt, completion, total) and associated cost from a `ChatCompletion` object. It safely handles cases where usage or cost attributes might be missing by defaulting to zero values.*


### convert_tools_to_functions (method, L1129-L1165, parent: AnthropicClient)

> *Summary: Transforms a list of tool definitions into Anthropic-compatible function specifications by recursively updating internal `$ref` paths within property schemas. It processes tools that are explicitly defined as functions and modifies their parameter properties accordingly.*


### _resolve_schema_refs (method, L1167-L1189, parent: AnthropicClient)

> *Summary: Recursively traverses a JSON schema structure to replace `$ref` pointers with their actual definitions found in the provided `defs`. It handles nested dictionaries and lists by applying this resolution process throughout the entire schema.*


### _add_response_format_to_system (method, L1191-L1266, parent: AnthropicClient)

> *Summary: This method modifies client parameters by injecting instructions into the system prompt to enforce structured JSON output from an LLM. It generates a detailed prompt containing the Pydantic model's schema and a concrete example, instructing the model to wrap its final data within `<json_response>` tags.*


### _extract_json_response (method, L1268-L1312, parent: AnthropicClient)

> *Summary: Parses a `Message` object from an API call to extract and validate structured JSON output. It first searches for content within specific tags or falls back to finding the outermost `{...}` structure, then attempts to deserialize it using `json.loads` or validates it against a provided Pydantic model.*


### _format_json_response (function, L1315-L1322)

> *Summary: This utility function serializes a structured output into a JSON string. It checks if the input is already a string, implements a custom formatting method via `FormatterProtocol`, or defaults to dumping the object using its model serialization capabilities.*


### process_image_content (function, L1325-L1351)

> *Summary: Converts an OpenAI-formatted image content item into a Claude-compatible structure. It specifically handles both external URLs and embedded base64 data URLs, returning the transformed dictionary or the original input upon failure.*


### process_message_content (function, L1354-L1376)

> *Summary: This function standardizes message content by accepting a dictionary containing text or a list of mixed types. It processes the input, converting image references into structured data while returning plain strings or lists of processed content objects.*


### _extract_system_message (function, L1379-L1395)

> *Summary: This helper function extracts the content from a system role message and appends it to the `system` parameter within the provided parameters dictionary. It handles both text-only messages and multi-part messages (like those containing images) by concatenating text components appropriately before updating the parameters in place.*


### _convert_tool_call_message (function, L1398-L1452)

> *Summary: Converts an OpenAI-formatted message containing `tool_calls` into Anthropic's `ToolUseBlock` format. It processes the tool calls, potentially inserts a user continuation message based on expected role alternation, and appends the resulting assistant message (either with structured tool uses or a plain text summary) to the provided list.*


### _convert_tool_result_message (function, L1455-L1505)

> *Summary: Transforms an OpenAI-formatted tool result message into Anthropic's `tool_result` format for processing. It appends or modifies messages within a provided list based on whether tools are active and the expected role, returning the count of added results and the updated index of the last tool result.*


### oai_messages_to_anthropic_messages (function, L1509-L1589)

> *Summary: Transforms messages from OpenAI format to Anthropic's required structure, handling role ordering and message type conversions for tool calls and results. It ensures proper conversational flow by inserting placeholder continuation messages if the sequence is interrupted or ends unexpectedly.*


### _calculate_cost (function, L1592-L1604)

> *Summary: Determines the monetary cost of an API call based on token counts and a specified Anthropic model. It uses predefined pricing structures to calculate separate costs for input and output tokens, returning the combined total or issuing a warning if the model is unsupported.*

