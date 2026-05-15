# test/oai/test_client.py

29 function(s): mock_openai_wrapper_fixed_order_default, mock_openai_wrapper_fixed_order_explicit, mock_openai_wrapper_round_robin, test_fixed_order_routing_successful_first_client, test_round_robin_routing, test_round_robin_routing_with_failures, test_config_list_with_pydantic_models, test_config_list_with_dict_items, test_aoai_chat_completion, test_fallback_kwargs and 19 more. 6 class(es): MockModelClient, TestOpenAIClientBadRequestsError, TestDeepSeekPatch, TestGemini, TestCreateV2Client, TestO1. 24 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MockModelClient | class |  |
| mock_openai_wrapper_fixed_order_default | function |  |
| mock_openai_wrapper_fixed_order_explicit | function |  |
| mock_openai_wrapper_round_robin | function |  |
| test_fixed_order_routing_successful_first_client | function |  |
| test_round_robin_routing | function |  |
| test_round_robin_routing_with_failures | function |  |
| test_config_list_with_pydantic_models | function |  |
| test_config_list_with_dict_items | function |  |
| test_aoai_chat_completion | function |  |
| test_fallback_kwargs | function |  |
| test_oai_tool_calling_extraction | function |  |
| test_chat_completion | function |  |
| test_completion | function |  |
| test_cost | function |  |
| test_customized_cost | function |  |
| test_usage_summary | function |  |
| test_log_cache_seed_value | function |  |
| test_legacy_cache | function |  |
| test_no_default_cache | function |  |
| test_cache | function |  |
| test_convert_system_role_to_user | function |  |
| test_openai_llm_config_entry | function |  |
| test_openai_llm_config_entry_with_verbosity | function |  |
| test_azure_llm_config_entry | function |  |
| test_deepseek_llm_config_entry | function |  |
| TestOpenAIClientBadRequestsError | class |  |
| TestDeepSeekPatch | class |  |
| TestGemini | class |  |
| TestCreateV2Client | class |  |
| TestO1 | class |  |
| test_openai_llm_config_entry_extra_headers | function |  |
| test_openai_llm_config_entry_extra_headers_default_none | function |  |
| test_azure_llm_config_entry_extra_headers | function |  |
| test_extra_headers_chat_completion | function |  |

## Chunks

### MockModelClient (class, L52-L97)

> *Summary: This class simulates an API client for testing purposes, accepting a configuration dictionary and an optional name upon initialization. It provides methods to mock successful or failing responses (`create`), extract message content from a response (`message_retrieval`), calculate simulated cost (`cost`), and parse usage details (`get_usage`).*


### __init__ (method, L53-L56, parent: MockModelClient)

> *Summary: Initializes an object by storing a configuration dictionary and an optional name. It also sets up a counter to track subsequent method calls.*


### create (method, L58-L81, parent: MockModelClient)

> *Summary: This method simulates an API call by accepting a dictionary of parameters and returning a mock `ChatCompletion` object if configured to succeed. It increments a call counter and raises an `APIError` if the configuration dictates failure.*


### message_retrieval (method, L83-L84, parent: MockModelClient)

> *Summary: Extracts the content of messages from a structured API response object. It takes a `response` object as input and returns a list containing the string content of each message found within the choices.*


### cost (method, L86-L87, parent: MockModelClient)

> *Summary: Returns a fixed monetary value of $0.02 based on the provided `response` object. This method simulates calculating the operational cost associated with an API interaction.*


### get_usage (method, L90-L97, parent: MockModelClient)

> *Summary: Extracts usage statistics from an API response object, returning a dictionary containing token counts for prompts and completions, total tokens, associated cost, and the model identifier. It safely defaults the cost to zero if the `cost` attribute is missing on the response.*


### mock_openai_wrapper_fixed_order_default (function, L102-L114)

> *Summary: This function sets up a mock `OpenAIWrapper` instance using a predefined list of configurations, ensuring the internal routing method defaults to `"fixed_order"` when not explicitly set. It then initializes the underlying model clients based on this configuration and returns the fully configured wrapper object.*


### mock_openai_wrapper_fixed_order_explicit (function, L118-L128)

> *Summary: This function sets up an `OpenAIWrapper` instance configured to use a "fixed\_order" routing strategy. It initializes the wrapper with a predefined list of client configurations and manually populates its internal client list for testing purposes, returning the fully configured wrapper object.*


### mock_openai_wrapper_round_robin (function, L132-L142)

> *Summary: This function initializes an `OpenAIWrapper` configured for round-robin routing across three mock client configurations. It then instantiates and injects specific `MockModelClient` instances into the wrapper's internal clients list before returning the fully set up wrapper object.*


### test_fixed_order_routing_successful_first_client (function, L148-L153)

> *Summary: This test verifies that when a request is made, the first configured client receives and processes the message successfully. It asserts that the response content matches expectations and confirms only the initial client was invoked.*


### test_round_robin_routing (function, L156-L187)

> *Summary: This test verifies that the wrapper correctly distributes incoming requests across multiple underlying clients using a round-robin strategy. It asserts that each sequential call targets the next available client in sequence, wrapping around when all clients have been utilized.*


### test_round_robin_routing_with_failures (function, L190-L232)

> *Summary: This test verifies that a round-robin load balancing mechanism correctly routes requests, even when some backend clients fail. It simulates sequential calls, demonstrating how the system skips failed clients and wraps around to the beginning of the client list upon completion.*


### test_config_list_with_pydantic_models (function, L235-L241)

> *Summary: Verifies that the `OpenAIWrapper` correctly processes and stores configuration items derived from an `LLMConfig` instance. It asserts that a list of configurations is populated with the expected model name when initialized with specific settings.*


### test_config_list_with_dict_items (function, L244-L250)

> *Summary: Verifies that the `OpenAIWrapper` correctly processes a list containing dictionaries as configuration items. It initializes the wrapper with a single dictionary entry and asserts its internal configuration matches the input structure.*


### test_aoai_chat_completion (function, L265-L280)

> *Summary: This test verifies the chat completion functionality by initializing an `OpenAIWrapper` with provided credentials and sending a simple query ("2+2="). It executes this test twice: once using a pre-configured list of configurations, and again after manually adjusting the configuration dictionary to simulate a specific deployment scenario.*


### test_fallback_kwargs (function, L285-L287)

> *Summary: Verifies that the keyword-only arguments defined in the constructors of `OpenAI` and `AzureOpenAI` match predefined fallback argument sets. This test ensures consistent handling of optional parameters across both OpenAI and Azure implementations.*


### test_oai_tool_calling_extraction (function, L293-L321)

> *Summary: This test verifies the extraction capability from an OpenAI response generated by calling a defined tool. It sends a user query requesting weather information, including a function definition for `getCurrentWeather`, and then prints both the raw response and the extracted text/completion object.*


### test_chat_completion (function, L326-L330)

> *Summary: This test function initializes an OpenAI wrapper using provided credentials and sends a simple arithmetic query to the API. It then prints both the raw response object and the extracted text content from that response.*


### test_completion (function, L335-L340)

> *Summary: This test function initializes an OpenAI wrapper using provided Azure credentials and sends a simple arithmetic query to the model. It then prints both the raw response object and the extracted text completion from that response.*


### test_cost (function, L352-L356)

> *Summary: This test function initializes an OpenAI wrapper using provided Azure credentials and a cache seed. It sends a simple arithmetic query to the model and prints the resulting cost of the API call.*


### test_customized_cost (function, L361-L370)

> *Summary: This test verifies that a custom price configuration is correctly applied when interacting with an OpenAI client wrapper. It iterates through provided configurations, sets a specific price for each, and asserts the resulting API call cost meets a minimum threshold.*


### test_usage_summary (function, L375-L390)

> *Summary: This test verifies the usage tracking functionality of an OpenAI wrapper by making a simple API call and asserting that both actual and total cost summaries are correctly populated with positive values. It further confirms that calling clear methods successfully resets these summary attributes to `None`.*


### test_log_cache_seed_value (function, L395-L447)

> *Summary: This test verifies that the logging mechanism correctly reports when a cached response is used. It mocks an API call and disk cache retrieval to ensure the `OpenAIWrapper` logs the specific seed value provided during the request.*


### test_legacy_cache (function, L453-L512)

> *Summary: This test verifies the functionality of a legacy caching mechanism within an OpenAI wrapper by executing API calls with and without cached responses. It asserts that subsequent calls using the same cache seed return identical results faster than initial "cold" calls, confirming both content consistency and performance improvement across different configuration methods.*


### test_no_default_cache (function, L517-L557)

> *Summary: This test verifies the caching behavior of an OpenAI wrapper by comparing response times and content across three scenarios: no cache, cold cache (first run), and warm cache (subsequent runs). It asserts that the warm cache is faster than both other modes and produces identical results to the cold cache while differing from the uncached result.*


### test_cache (function, L563-L622)

> *Summary: Verifies the functionality of disk-based caching for an OpenAI wrapper by comparing response times and content when making identical API calls with and without a pre-populated cache. It ensures that responses are consistent across runs and that the specified cache directory is used instead of any legacy locations.*


### test_convert_system_role_to_user (function, L626-L636)

> *Summary: This test verifies that the system role message within a list of chat messages is correctly transformed into a user role message. It takes an input list containing one system and one user message, modifies it in place to match the expected structure, and asserts equality.*


### test_openai_llm_config_entry (function, L639-L655)

> *Summary: This test verifies the correct initialization and serialization of an `OpenAILLMConfigEntry` object using a mock API key and model name. It asserts that the configuration correctly holds the specified values and matches the expected dictionary structure upon calling `model_dump()`.*


### test_openai_llm_config_entry_with_verbosity (function, L658-L675)

> *Summary: This test verifies the correct serialization of an `OpenAILLMConfigEntry` instance configured with a specific model and low verbosity. It asserts that the resulting dictionary matches the expected structure, including API type, model name, and verbosity level.*


### test_azure_llm_config_entry (function, L678-L699)

> *Summary: This test verifies that an `AzureOpenAILLMConfigEntry` object correctly serializes its configuration details, including model name and API credentials. It asserts that the dumped entry matches a predefined expected dictionary structure when wrapped within an `LLMConfig`.*


### test_deepseek_llm_config_entry (function, L702-L725)

> *Summary: This test verifies that a `DeepSeekLLMConfigEntry` object correctly serializes its configuration parameters, including API key and model details. It asserts that the dumped entry matches an expected dictionary structure and further confirms this entry is correctly wrapped within an `LLMConfig`.*


### TestOpenAIClientBadRequestsError (class, L728-L776)

> *Summary: This test suite verifies the error handling logic for bad requests originating from an OpenAI client. It checks if specific error messages, particularly those related to invalid agent names within message structures, correctly trigger a re-raised `ValueError` or remain as an original `openai.BadRequestError`.*


### test_is_agent_name_error_message (method, L729-L733, parent: TestOpenAIClientBadRequestsError)

> *Summary: This test verifies an internal helper method by asserting that specific error strings, formatted to include different indices, are correctly identified as agent name errors. It confirms the function returns `False` for a non-matching string and `True` for the expected pattern variations.*


### test_handle_openai_bad_request_error (method, L752-L776, parent: TestOpenAIClientBadRequestsError)

> *Summary: This test verifies the error handling logic for OpenAI's `BadRequestError`. It simulates an API failure by raising a mock `BadRequestError` and then asserts that the client wrapper either re-raises the original error or transforms it into a `ValueError`, depending on the test configuration.*


### TestDeepSeekPatch (class, L779-L889)

> *Summary: This test suite verifies message manipulation logic for different AI models. It tests functions that reorder system messages to the beginning and specifically patches message structures when using `deepseek-reasoner`, while also ensuring these operations handle messages lacking a defined "role" field gracefully.*


### test_move_system_message_to_beginning (method, L827-L831, parent: TestDeepSeekPatch)

> *Summary: This test verifies that a specific method correctly reorders a list of message dictionaries by moving the system message to the start. It takes an input list and asserts that it matches a predefined, correctly ordered output list.*


### test_patch_messages_for_deepseek_reasoner (method, L841-L865, parent: TestDeepSeekPatch)

> *Summary: This test verifies the message transformation logic for DeepSeek Reasoner by comparing the output of a patching function against an expected structure. It takes initial user/system messages and, based on a flag, either applies specific modifications or returns the input unchanged before asserting equality.*


### test_move_system_message_to_beginning_without_role (method, L867-L876, parent: TestDeepSeekPatch)

> *Summary: Verifies that the system message reordering logic correctly handles input lists containing messages lacking a `role` field. It asserts that the designated system message moves to the front while preserving the relative order of other messages, including those without roles.*


### test_patch_messages_for_deepseek_reasoner_without_role (method, L878-L889, parent: TestDeepSeekPatch)

> *Summary: This test verifies that the message patching logic for `deepseek-reasoner` handles input messages lacking a `"role"` field without raising a `KeyError`. It asserts that the resulting list of patched messages retains at least the original count.*


### TestGemini (class, L892-L911)

> *Summary: These tests verify that a method correctly populates an `openai_config` dictionary with proxy settings when provided, and ensures no proxy is added if the input configuration lacks one. It uses an `OpenAIWrapper` instance initialized with mock client configurations to test this behavior.*


### test_configure_openai_config_for_gemini_updates_proxy (method, L893-L901, parent: TestGemini)

> *Summary: This test verifies that an `OpenAIWrapper` correctly applies proxy settings from a configuration dictionary to its internal OpenAI configuration structure when adapting for Gemini models. It inputs a list of client configurations and a proxy setting, asserting the resulting configuration contains the specified proxy URL.*


### test_configure_openai_config_for_gemini_no_proxy (method, L903-L911, parent: TestGemini)

> *Summary: This test verifies that when configuring an OpenAI-like client for Gemini models without a proxy setting, the resulting configuration dictionary does not contain any proxy information. It initializes a wrapper with a specific model configuration and asserts the absence of proxy keys after calling the internal configuration method.*


### TestCreateV2Client (class, L914-L960)

> *Summary: These tests verify the `_create_v2_client` method's behavior when instantiating a client. It confirms that configuration parameters like API keys, base URLs, and response formats are correctly passed to the provided client constructor, and that the newly created instance is appended to the wrapper's internal list of clients.*


### test_create_v2_client_passes_openai_config_and_response_format (method, L917-L943, parent: TestCreateV2Client)

> *Summary: This test verifies that the internal client creation method correctly passes an `openai_config` dictionary and a `response_format` object to the constructor of a mock V2 client. It asserts that the resulting client instance holds these passed arguments accurately.*


### test_create_v2_client_appends_to_clients_and_returns_instance (method, L945-L960, parent: TestCreateV2Client)

> *Summary: This test verifies that a specific method correctly adds a new client instance to an existing list of clients and returns the newly created object. It takes a minimal client class and configuration dictionary as input, asserting that the returned object matches the expected type and that the internal client list size has increased by one.*


### TestO1 (class, L963-L1097)

> *Summary: This test class verifies the parameter processing and completion functionality for an OAI client wrapper. It tests how unsupported parameters are filtered out while raising warnings, ensures `max_tokens` is correctly mapped to `max_completion_tokens`, validates system message merging based on model type, and executes actual API calls using mock or real clients.*


### mock_oai_client (method, L965-L968, parent: TestO1)

> *Summary: Creates and returns a mocked `OpenAIClient` instance by extracting the API key from the provided mock credentials. It initializes the client using the extracted key with no additional configuration.*


### o1_mini_client (method, L971-L973, parent: TestO1)

> *Summary: This method initializes and returns a generator of `OpenAIWrapper` instances based on the configuration list provided in the input `Credentials`. It uses a fixed seed of 42 for caching during initialization.*


### o1_client (method, L976-L978, parent: TestO1)

> *Summary: This method constructs and returns a generator of `OpenAIWrapper` instances based on the configuration list provided in the input `Credentials`. It initializes these wrappers using the specified configurations and a fixed cache seed.*


### test_reasoning_remove_unsupported_params (method, L980-L1016, parent: TestO1)

> *Summary: This test verifies that an input parameter dictionary is sanitized by removing any keys not supported by the reasoning model, while issuing a `UserWarning` for each removed parameter. It asserts that only explicitly valid parameters remain in the dictionary after processing.*


### test_oai_reasoning_max_tokens_replacement (method, L1018-L1026, parent: TestO1)

> *Summary: This test verifies that the `max_tokens` parameter is correctly transformed into `max_completion_tokens` when processing reasoning model parameters for an OpenAI API type. It asserts that the original key is removed and the new key holds the same value after the transformation.*


### test_oai_reasoning_system_message_handling (method, L1039-L1060, parent: TestO1)

> *Summary: This test verifies how a reasoning system processes input messages based on a configuration flag. It feeds the client a system and user message pair, then asserts whether the system message is merged into the first user message or remains separate depending on the `should_merge` parameter.*


### _test_completion (method, L1062-L1073, parent: TestO1)

> *Summary: This method verifies the functionality of an OpenAI client by sending a list of message dictionaries to it. It asserts that the response is valid, extracts the resulting text or completion object, and confirms the extracted content contains the string "4".*


### test_completion_o1_mini (method, L1084-L1085, parent: TestO1)

> *Summary: This test method verifies the completion functionality by calling a shared testing utility with an `OpenAIWrapper` instance and a list of message dictionaries. It executes the core logic to ensure correct API interaction for mini-sized completions.*


### test_completion_o1 (method, L1096-L1097, parent: TestO1)

> *Summary: This test method verifies the completion functionality by calling a shared testing helper with an `OpenAIWrapper` instance and a list of message dictionaries. It executes the core logic to ensure correct API interaction for completions.*


### test_openai_llm_config_entry_extra_headers (function, L1100-L1108)

> *Summary: Verifies that custom HTTP headers provided during the creation of an `OpenAILLMConfigEntry` are correctly stored within the object's `extra_headers` attribute. It takes a dictionary of headers as input and asserts its equality with the internal state.*


### test_openai_llm_config_entry_extra_headers_default_none (function, L1111-L1117)

> *Summary: Verifies that the `extra_headers` attribute of an `OpenAILLMConfigEntry` instance defaults to `None` when not explicitly provided during initialization. It instantiates a configuration object with minimal required parameters and asserts the default header value.*


### test_azure_llm_config_entry_extra_headers (function, L1120-L1130)

> *Summary: This test verifies that custom HTTP headers provided during the initialization of an `AzureOpenAILLMConfigEntry` are correctly stored within the object's `extra_headers` attribute. It passes a dictionary containing one custom header and asserts its equality against the stored value.*


### test_extra_headers_chat_completion (function, L1135-L1144)

> *Summary: This test verifies that custom HTTP headers are correctly passed to the OpenAI API during a chat completion request. It initializes an `OpenAIWrapper` with configurations containing extra headers and then calls the `create` method, asserting the response is processed correctly.*

