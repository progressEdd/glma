# autogen/oai/client.py

1 function(s): log_cache_seed_value. 13 class(es): OpenAIEntryDict, OpenAILLMConfigEntry, AzureOpenAIEntryDict, AzureOpenAILLMConfigEntry, DeepSeekEntryDict, DeepSeekLLMConfigEntry, PlaceHolderClient, OpenAIClient, OpenAIWrapper, OpenAIResponsesEntryDict, OpenAIResponsesLLMConfigEntry, OpenAIV2EntryDict, OpenAIV2LLMConfigEntry. 41 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| log_cache_seed_value | function |  |
| OpenAIEntryDict | class |  |
| OpenAILLMConfigEntry | class |  |
| AzureOpenAIEntryDict | class |  |
| AzureOpenAILLMConfigEntry | class |  |
| DeepSeekEntryDict | class |  |
| DeepSeekLLMConfigEntry | class |  |
| PlaceHolderClient | class |  |
| OpenAIClient | class |  |
| OpenAIWrapper | class |  |
| OpenAIResponsesEntryDict | class |  |
| OpenAIResponsesLLMConfigEntry | class |  |
| OpenAIV2EntryDict | class |  |
| OpenAIV2LLMConfigEntry | class |  |

## Chunks

### log_cache_seed_value (function, L250-L251)

> *Summary: Logs the provided cache seed value and the type of the `ModelClient` instance to debug output. It accepts a seed value (string or integer) and an initialized client object as input, returning nothing.*


### OpenAIEntryDict (class, L254-L265)

> *Summary: This structure defines configuration parameters specifically for OpenAI API interactions. It holds settings like pricing, tool selection, streaming preference, and various request body/header customizations.*


### OpenAILLMConfigEntry (class, L268-L292)

> *Summary: This configuration object defines parameters for an OpenAI-compatible LLM client, allowing users to specify details like pricing, tool usage, streaming behavior, and custom request bodies. It acts as a blueprint that requires subclasses to implement `create_client()` to instantiate a functional model client.*


### create_client (method, L291-L292, parent: OpenAILLMConfigEntry)

> *Summary: This abstract method requires subclasses to implement logic for instantiating and returning a concrete `ModelClient` object. It serves as a contract ensuring all derived classes provide their own client creation mechanism.*


### AzureOpenAIEntryDict (class, L295-L304)

> *Summary: This dictionary structure configures an Azure OpenAI LLM call by specifying the API type and providing various optional parameters. It accepts inputs like authentication providers, streaming preferences, tool usage constraints, and token limits to control model behavior.*


### AzureOpenAILLMConfigEntry (class, L307-L322)

> *Summary: This configuration class defines parameters for interacting with Azure OpenAI services, including authentication methods, streaming settings, and model-specific controls like reasoning effort. It serves as a blueprint that must implement a `create_client` method to instantiate the actual communication client.*


### create_client (method, L321-L322, parent: AzureOpenAILLMConfigEntry)

> *Summary: This method is an abstract placeholder that must be implemented by subclasses to instantiate and return a concrete `ModelClient` object. It signals that the specific client creation logic depends on the inheriting class.*


### DeepSeekEntryDict (class, L325-L330)

> *Summary: This data structure defines configuration parameters specifically for interacting with the DeepSeek LLM API. It requires a base URL, specifies streaming capability, and allows setting the tool choice mode.*


### DeepSeekLLMConfigEntry (class, L333-L345)

> *Summary: This configuration class defines parameters for interacting with the DeepSeek LLM API, including settings like temperature, top\_p, and maximum tokens. It provides a default base URL and specifies the API type as "deepseek," though client creation is intentionally unimplemented here.*


### create_client (method, L344-L345, parent: DeepSeekLLMConfigEntry)

> *Summary: This method requires subclasses to implement client creation logic, raising a `NotImplementedError` if called directly on the base class. It serves as an abstract hook for initializing specific LLM clients based on configuration.*


### PlaceHolderClient (class, L348-L350)

> *Summary: Initializes a client object by accepting and storing a configuration dictionary. This class serves as a placeholder for future API interaction logic.*


### __init__ (method, L349-L350, parent: PlaceHolderClient)

> *Summary: Initializes the client by storing a configuration object passed as an argument. This sets up the necessary parameters for subsequent API interactions.*


### OpenAIClient (class, L354-L773)

> *Summary: This class wraps an OpenAI client to provide a standardized interface for interacting with OpenAI APIs. It handles request modifications like patching messages for specific models (e.g., Deepseek) and manages streaming responses by accumulating chunks into final `ChatCompletion` objects. Key methods include `create` for making API calls, `message_retrieval` for extracting content from responses, and `cost` for calculating usage fees.*


### __init__ (method, L359-L369, parent: OpenAIClient)

> *Summary: Initializes an object by storing an OpenAI or AzureOpenAI client and an optional response format. It performs a warning check if the provided client appears to be configured for OpenAI but lacks a valid API key.*


### message_retrieval (method, L371-L406, parent: OpenAIClient)

> *Summary: Extracts messages from an OpenAI response object, handling both `ChatCompletion` and `Completion` types. It formats the content based on whether tool calls are present or if a specific response format is configured.*


### _is_agent_name_error_message (method, L409-L411, parent: OpenAIClient)

> *Summary: Checks if a given string message matches a specific regex pattern indicating an invalid agent name error from the OpenAI API. Returns `True` if the message conforms to this expected error format, and `False` otherwise.*


### _move_system_message_to_beginning (method, L414-L418, parent: OpenAIClient)

> *Summary: This method rearranges a list of message dictionaries by moving the first encountered system message to the very beginning of the list. It modifies the input list in place and returns nothing.*


### _patch_messages_for_deepseek_reasoner (method, L421-L458, parent: OpenAIClient)

> *Summary: This function modifies message lists specifically for the `deepseek-reasoner` model by ensuring the system message is first and enforcing alternating user/assistant roles between consecutive messages. It also guarantees the final message in the sequence is a "user" message, appending one if necessary.*


### _handle_openai_bad_request_error (method, L461-L484, parent: OpenAIClient)

> *Summary: This decorator wraps a function to catch `openai.BadRequestError` during API calls. If the error response indicates an issue with the agent name, it transforms the exception into a more user-friendly `ValueError` detailing formatting requirements. Otherwise, it re-raises the original `BadRequestError`.*


### _convert_system_role_to_user (method, L487-L490, parent: OpenAIClient)

> *Summary: This utility modifies a list of message dictionaries by iterating through them and changing any message with the `"system"` role to have the `"user"` role. It performs an in-place modification on the provided input list.*


### _add_streaming_usage_to_params (method, L493-L495, parent: OpenAIClient)

> *Summary: If the input parameters indicate streaming is active, this method ensures that usage tracking is included within the stream options dictionary. It modifies the provided parameter dictionary in place to enable this feature.*


### create (method, L497-L708, parent: OpenAIClient)

> *Summary: Executes an OpenAI chat completion request, handling both synchronous and streaming modes based on input parameters. It intelligently processes structured output requests by converting formats and manages special logic for Mistral models and stream chunk aggregation before returning a `ChatCompletion` object.*


### _process_reasoning_model_params (method, L710-L743, parent: OpenAIClient)

> *Summary: This method sanitizes a dictionary of model parameters intended for reasoning models by removing unsupported configuration keys and renaming `max_tokens` to `max_completion_tokens`. It also modifies the structure of messages, converting any 'system' roles to 'user' roles if the specified model is an older version of `o1-mini` or `o1-preview`.*


### cost (method, L745-L763, parent: OpenAIClient)

> *Summary: Calculates the monetary cost of an AI response based on its input and completion token counts. It uses predefined pricing data for the model, returning zero if the model is unrecognized in the configuration.*


### get_usage (method, L766-L773, parent: OpenAIClient)

> *Summary: Extracts token usage and cost details from a chat or completion response object. It returns a dictionary containing the prompt tokens, completion tokens, total tokens, associated cost, and the model name used.*


### OpenAIWrapper (class, L777-L1613)

> *Summary: This class acts as a unified wrapper for interacting with various LLM APIs (OpenAI, Azure, Gemini, etc.). It initializes multiple configured clients based on input configurations and routes requests through them using fixed order or round-robin logic. The primary function is to execute completions, handle caching, apply response filters, and aggregate usage statistics across all active clients.*


### openai_kwargs (method, L794-L800, parent: OpenAIWrapper)

> *Summary: If the OpenAI result was successful, it returns a union of keyword-only arguments accepted by both `OpenAI` and `AzureOpenAI` constructors. Otherwise, it provides a predefined set of fallback keyword arguments for both providers.*


### __init__ (method, L805-L884, parent: OpenAIWrapper)

> *Summary: Initializes an OpenAI wrapper by accepting a base configuration and an optional list of override configurations. It sets up internal state, including client lists, routing logic (fixed order or round-robin), and response buffering based on the provided inputs.*


### _separate_openai_config (method, L886-L890, parent: OpenAIWrapper)

> *Summary: This method partitions an input configuration dictionary into two parts: one containing keys relevant to OpenAI settings and another holding all remaining arbitrary keyword arguments. It returns these two dictionaries as a tuple.*


### _separate_create_config (method, L892-L896, parent: OpenAIWrapper)

> *Summary: This method partitions an input configuration dictionary into two separate dictionaries based on a predefined set of allowed extra arguments. It returns the core configuration and the subset containing only the specified extra keyword arguments.*


### _store_response_metadata (method, L898-L920, parent: OpenAIWrapper)

> *Summary: This method manages response metadata by storing details like the generating client and filter status for a given response ID. It uses a fixed-size circular buffer to ensure memory usage remains bounded by automatically discarding the oldest entry when the capacity is reached.*


### _configure_azure_openai (method, L922-L932, parent: OpenAIWrapper)

> *Summary: This method modifies an existing OpenAI configuration dictionary by setting or updating Azure-specific deployment and endpoint details based on provided configurations. It also conditionally injects a default Azure Active Directory token provider if specified in the input settings.*


### _configure_openai_config_for_bedrock (method, L934-L943, parent: OpenAIWrapper)

> *Summary: This method merges AWS credentials and configuration settings from an input `config` dictionary into an existing `openai_config` dictionary. It copies specified required and optional keys, such as access keys and region, to adapt the OpenAI configuration for use with Amazon Bedrock.*


### _configure_openai_config_for_vertextai (method, L945-L950, parent: OpenAIWrapper)

> *Summary: This method merges Google credentials from a configuration dictionary into an existing OpenAI configuration. It specifically copies `gcp_project_id`, `gcp_region`, and `gcp_auth_token` if they are present in the input configuration.*


### _configure_openai_config_for_gemini (method, L952-L957, parent: OpenAIWrapper)

> *Summary: Merges specific configuration settings from a general `config` dictionary into an existing `openai_config` dictionary. It specifically copies values for keys like "proxy" if they exist in the source configuration.*


### _create_v2_client (method, L959-L963, parent: OpenAIWrapper)

> *Summary: Instantiates a V2 model client using provided configuration and response format, then registers it within the object's internal list before returning the newly created client instance.*


### _register_default_client (method, L965-L1077, parent: OpenAIWrapper)

> *Summary: This method configures and registers an LLM client based on the provided `api_type` from a configuration dictionary. It merges user-specific settings with default OpenAI configurations to instantiate various clients (e.g., AzureOpenAI, GeminiClient, AnthropicClient) or defaults to a standard OpenAI client, handling necessary imports and special cases like dot removal for Azure deployment names.*


### register_model_client (method, L1079-L1105, parent: OpenAIWrapper)

> *Summary: This method registers a specific model client class, either by replacing a placeholder instance or by adding it if no existing client of that type is found. It validates registration against the current list of clients and raises errors if the client is already present or not configured in the system settings.*


### instantiate (method, L1108-L1118, parent: OpenAIWrapper)

> *Summary: This method generates a string by applying formatting or calling a callable based on the provided `template` and `context`. It returns the resulting formatted string, or the original template/None if context is missing.*


### _construct_create_params (method, L1120-L1151, parent: OpenAIWrapper)

> *Summary: This method prepares configuration parameters for creation by validating that either a `prompt` or `messages` is provided in the input config. It then instantiates any string templates within the prompt or message contents using an external context, returning the fully prepared parameter dictionary.*


### create (method, L1153-L1392, parent: OpenAIWrapper)

> *Summary: This method attempts to generate a model completion by iterating through configured clients, applying routing logic like round-robin. It first checks for cache hits using provided or derived keys; if no cache hit occurs, it calls each client's `create` method sequentially until a response passes an optional filter or the last client is reached.*


### _cost_with_customized_price (method, L1395-L1401, parent: OpenAIWrapper)

> *Summary: Calculates the total cost of a completion based on input and output token counts, applying custom per-thousand token pricing provided as an input tuple. It returns this calculated monetary cost as a float.*


### _update_dict_from_chunk (method, L1404-L1435, parent: OpenAIWrapper)

> *Summary: This method appends or sets a value from a `chunk` object into an existing dictionary based on a specified `field`. It supports only string and numeric types for the field's content, raising an error if lists or dictionaries are encountered.*


### _update_function_call_from_chunk (method, L1438-L1466, parent: OpenAIWrapper)

> *Summary: This method merges partial function call data from a chunk into a complete function call dictionary. It takes the chunk, an existing full call (or `None`), and token count as input, returning the updated full call structure and the incremented token count.*


### _update_tool_calls_from_chunk (method, L1469-L1515, parent: OpenAIWrapper)

> *Summary: This method merges incremental tool call data from a chunk into a complete structure. It accepts a `ChoiceDeltaToolCall`, an optional existing full tool call dictionary, and the current token count, returning the updated tool call and the incremented token count.*


### _update_usage (method, L1517-L1548, parent: OpenAIWrapper)

> *Summary: This method aggregates usage statistics by iterating over predefined keys to ensure all necessary metrics are present in the input data. It updates internal `total_usage_summary` and `actual_usage_summary` dictionaries with cost and token counts from the provided usage objects.*


### print_usage_summary (method, L1550-L1568, parent: OpenAIWrapper)

> *Summary: This method generates and sends a usage summary event to the default output stream. It accepts an optional `mode` parameter (string or list of strings) which dictates whether "actual," "total," or both usages are reported.*


### clear_usage_summary (method, L1570-L1573, parent: OpenAIWrapper)

> *Summary: Resets both the total and actual usage summaries within the client instance to `None`. This method is used to clear accumulated usage statistics.*


### extract_text_or_completion_object (method, L1575-L1613, parent: OpenAIWrapper)

> *Summary: This method extracts content from a raw API response by checking for legacy retrieval functions, consulting stored client metadata, or falling back to parsing the `choices` structure. It returns either a list of strings (text content) or a list of dictionaries if tool calls are present in the response.*


### OpenAIResponsesEntryDict (class, L1621-L1625)

> *Summary: This dictionary structure holds configuration for OpenAI responses, specifying the API type as "responses." It allows optional configuration of `tool_choice` and a list of supported `built_in_tools`.*


### OpenAIResponsesLLMConfigEntry (class, L1628-L1659)

> *Summary: This configuration class extends a base LLM entry to specifically target the OpenAI Responses API endpoint. It allows users to configure stateful, tool-enabled interactions by overriding the `api_type` and providing specific parameters for tools and command execution.*


### create_client (method, L1658-L1659, parent: OpenAIResponsesLLMConfigEntry)

> *Summary: This method is a placeholder that explicitly raises an error, indicating its implementation is deferred to the `OpenAIWrapper`'s default client registration mechanism. It does not perform any direct client creation itself.*


### OpenAIV2EntryDict (class, L1662-L1663)

> *Summary: This class defines a configuration structure specifically for OpenAI V2 API interactions. It enforces that the `api_type` field must be set to `"openai_v2"`.*


### OpenAIV2LLMConfigEntry (class, L1666-L1693)

> *Summary: This configuration class defines settings for using the OpenAI V2 client architecture. It enables access to richer response objects, including typed content blocks like reasoning and citations, compared to standard OpenAI clients.*


### create_client (method, L1692-L1693, parent: OpenAIV2LLMConfigEntry)

> *Summary: This method is a placeholder that explicitly raises an error, indicating its implementation is deferred to the `OpenAIWrapper`'s default client registration mechanism. It does not perform any direct client creation itself.*

