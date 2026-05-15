# test/oai/test_anthropic.py

47 function(s): mock_completion, anthropic_client, test_anthropic_llm_config_entry, test_initialization_missing_api_key, anthropic_client_with_aws_credentials, anthropic_client_with_vertexai_credentials, test_initialization, test_initialization_with_aws_credentials, test_initialization_with_vertexai_credentials, test_user_agent_header_is_set and 37 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_completion | function |  |
| anthropic_client | function |  |
| test_anthropic_llm_config_entry | function |  |
| test_initialization_missing_api_key | function |  |
| anthropic_client_with_aws_credentials | function |  |
| anthropic_client_with_vertexai_credentials | function |  |
| test_initialization | function |  |
| test_initialization_with_aws_credentials | function |  |
| test_initialization_with_vertexai_credentials | function |  |
| test_user_agent_header_is_set | function |  |
| test_cost_calculation | function |  |
| test_load_config | function |  |
| test_extract_json_response | function |  |
| test_convert_tools_to_functions | function |  |
| test_process_image_content_valid_data_url | function |  |
| test_process_image_content_non_image_type | function |  |
| test_process_message_content_string | function |  |
| test_process_message_content_list | function |  |
| test_oai_messages_to_anthropic_messages | function |  |
| test_oai_messages_to_anthropic_messages_without_role | function |  |
| test_supports_native_structured_outputs | function |  |
| test_has_messages_parse_api | function |  |
| test_transform_schema_for_anthropic | function |  |
| test_transform_schema_preserves_nested_structures | function |  |
| test_create_routes_to_native_or_json_mode | function |  |
| create_mock_anthropic_response | function |  |
| test_native_structured_output_with_parse_api | function |  |
| test_json_mode_fallback_on_native_failure | function |  |
| test_pydantic_model_vs_dict_schema | function |  |
| test_real_native_structured_output_api_call | function |  |
| test_openai_func_to_anthropic_preserves_strict | function |  |
| test_strict_tools_use_standard_api_with_strict | function |  |
| test_legacy_tools_use_standard_api | function |  |
| test_real_strict_tool_use_api_call | function |  |
| test_real_strict_tool_type_enforcement | function |  |
| test_real_combined_strict_tools_and_structured_output | function |  |
| test_real_sdk_version_validation_on_strict_tools | function |  |
| test_real_extended_thinking_api_call | function |  |
| test_real_tools_with_structured_output_beta_api | function |  |
| test_load_config_stream_enabled | function |  |
| test_create_streaming_routes | function |  |
| test_create_standard_no_stream_does_not_route | function |  |
| test_streaming_text_accumulation | function |  |
| test_streaming_tool_call_accumulation | function |  |
| test_streaming_thinking_blocks | function |  |
| test_real_streaming_text | function |  |
| test_real_streaming_with_tools | function |  |

## Chunks

### mock_completion (function, L29-L49)

> *Summary: Returns a class constructor that creates mock objects simulating an AI model's response. These mocks contain predefined attributes like completion text, model name, and token usage statistics for testing purposes.*


### anthropic_client (function, L53-L54)

> *Summary: Instantiates and returns an `AnthropicClient` object, using a placeholder API key for testing purposes. This function provides a configured client instance ready for interaction with the Anthropic API.*


### test_anthropic_llm_config_entry (function, L57-L79)

> *Summary: This test verifies that an `AnthropicLLMConfigEntry` object correctly serializes its configuration parameters, including model name, API key, and generation settings. It further asserts that wrapping this entry within an `LLMConfig` structure results in the expected list format for serialization.*


### test_initialization_missing_api_key (function, L83-L92)

> *Summary: This test verifies that initializing an `AnthropicClient` without necessary environment variables for credentials raises a `ValueError`. It confirms the client can be initialized successfully when an API key is explicitly provided.*


### anthropic_client_with_aws_credentials (function, L96-L102)

> *Summary: Creates and returns an `AnthropicClient` instance configured to use specific AWS credentials and the "us-west-2" region. This function serves as a setup utility for testing interactions with Anthropic while simulating AWS authentication.*


### anthropic_client_with_vertexai_credentials (function, L106-L111)

> *Summary: Creates and returns an `AnthropicClient` instance, configuring it to use specific Google Cloud credentials (project ID, region, and auth token). This function serves as a factory for initializing the client with predefined dummy authentication details.*


### test_initialization (function, L115-L116)

> *Summary: Verifies that the provided Anthropic client object has its `api_key` attribute correctly initialized to a specific dummy value during setup. This test ensures proper configuration loading for API access.*


### test_initialization_with_aws_credentials (function, L120-L132)

> *Summary: This test verifies that an initialized client, provided with AWS credentials, correctly stores and exposes specific configuration values like access keys, secret keys, session tokens, and region. It asserts these attributes match expected dummy values for validation purposes.*


### test_initialization_with_vertexai_credentials (function, L136-L145)

> *Summary: Verifies that an initialized client, configured with Vertex AI credentials, correctly sets its `gcp_project_id`, `gcp_region`, and `gcp_auth_token` attributes to expected dummy values. This test confirms proper configuration loading when using Google Cloud authentication for the Anthropic client.*


### test_user_agent_header_is_set (function, L149-L194)

> *Summary: Verifies that the `User-Agent` header, formatted with specific version strings, is correctly injected into all three supported Anthropic client types (standard API key, Bedrock, and Vertex) when initializing an `AnthropicClient`. It achieves this by mocking the respective client constructors and asserting the presence and value of the header in the call arguments.*


### test_cost_calculation (function, L199-L208)

> *Summary: This test verifies the cost calculation logic by simulating an API response containing token usage and a model name. It asserts that the calculated cost matches the expected value of $0.002025 based on 10 prompt tokens, 25 completion tokens, and the "claude-opus-4" model.*


### test_load_config (function, L212-L232)

> *Summary: This test verifies that a provided set of configuration parameters is correctly processed and returned by the client's `load_config` method. It asserts that the resulting configuration matches an expected structure containing specific model settings like temperature and token limits.*


### test_extract_json_response (function, L236-L375)

> *Summary: This function tests the JSON extraction capability of an Anthropic client by validating its ability to parse structured data from various message formats. It accepts a `Message` object as input and returns an instance of a defined Pydantic model, raising specific errors if the content is invalid or missing JSON.*


### test_convert_tools_to_functions (function, L379-L442)

> *Summary: This test verifies the conversion of Anthropic-style tool definitions to a standard function format using an `anthropic_client`. It takes a list containing one specific weather tool definition as input and asserts that the output matches a predefined, transformed structure.*


### test_process_image_content_valid_data_url (function, L446-L452)

> *Summary: This test verifies that the image content processing function correctly transforms a dictionary containing a base64 data URL into a structured representation. It takes an input item with a `data:image/png;base64,...` URL and asserts the output matches the expected structure containing the media type and raw base64 data.*


### test_process_image_content_non_image_type (function, L456-L461)

> *Summary: When provided with a content item of type "text," this test verifies that the image processing function returns the input unchanged. It confirms the function correctly handles non-image data types by passing them through without modification.*


### test_process_message_content_string (function, L465-L470)

> *Summary: This test verifies that the `process_message_content` function correctly handles a simple string input within a message dictionary. It asserts that the output matches the original content when processing a basic message structure.*


### test_process_message_content_list (function, L474-L488)

> *Summary: This test verifies that the `process_message_content` function correctly transforms a message containing mixed content types. It takes an input dictionary with text and base64 image URL parts and asserts the output matches the expected structure, converting the image URL into a structured image object.*


### test_oai_messages_to_anthropic_messages (function, L492-L525)

> *Summary: This test verifies the conversion of OpenAI-style messages to Anthropic format. It takes a dictionary containing mixed text and image content for system and user roles, asserting that the output correctly transforms image URLs into base64 encoded structures while simplifying the system message's text component.*


### test_oai_messages_to_anthropic_messages_without_role (function, L528-L544)

> *Summary: Verifies that the conversion function correctly handles OpenAI-style messages lacking a `role` field when transforming them for Anthropic. It asserts that processing succeeds without errors and that the final output adheres to Anthropic's expected message structure, specifically ensuring the last message is marked as "user".*


### test_supports_native_structured_outputs (function, L553-L582)

> *Summary: Verifies that the Anthropic model detection logic correctly identifies which Claude versions support native structured outputs. It takes a model name string as input and returns `True` or `False` based on whether the model supports this feature, testing various current and future models against older ones.*


### test_has_messages_parse_api (function, L586-L603)

> *Summary: This test verifies if the Anthropic SDK supports a `messages.parse()` function by calling an introspection helper. It asserts that the helper returns a boolean and, if true, confirms the existence of the `parse` method on the imported stable `Messages` class.*


### test_transform_schema_for_anthropic (function, L607-L636)

> *Summary: This test verifies that a given JSON schema is correctly adapted for Anthropic compatibility. It asserts that unsupported constraints like `minLength`, `maxLength`, and range checks are removed, while ensuring required fields and basic types are preserved and `additionalProperties` defaults to `False`.*


### test_transform_schema_preserves_nested_structures (function, L640-L676)

> *Summary: This test verifies that a schema transformation function correctly maintains complex, nested data structures. It takes an input JSON schema containing objects and arrays as input and asserts that the resulting transformed schema retains these deep structural relationships.*


### test_create_routes_to_native_or_json_mode (function, L680-L728)

> *Summary: This test verifies that the `create` method correctly routes API calls based on model and configuration. It mocks internal methods to assert whether the call is directed to native structured output, JSON mode, or the standard implementation when provided with specific parameters.*


### create_mock_anthropic_response (function, L731-L746)

> *Summary: Generates a predefined mock `Message` object conforming to the Anthropic API structure. This helper returns the structured response if an optional import succeeds, otherwise it returns `None`.*


### test_native_structured_output_with_parse_api (function, L750-L806)

> *Summary: This test verifies that when using native structured output with a Pydantic model, the Anthropic client correctly invokes the stable `messages.parse()` API. It mocks this parsing function to assert that it was called with the expected Pydantic model as the `output_format` parameter and confirms no beta headers are used in the request.*


### test_json_mode_fallback_on_native_failure (function, L810-L831)

> *Summary: This test verifies that when a native structured output call fails, the system attempts to gracefully fall back to JSON Mode for response generation. It mocks the native method to raise an exception and the JSON mode method to succeed, asserting that the overall `create` call handles this failure scenario.*


### test_pydantic_model_vs_dict_schema (function, L835-L861)

> *Summary: Verifies that the client correctly processes response format specifications when provided either as a Pydantic model or a raw dictionary schema. It confirms that both input types result in valid, expected structures for downstream processing.*


### test_real_native_structured_output_api_call (function, L872-L920)

> *Summary: This test executes a real API call to Anthropic's Claude Sonnet 4.5 model, requesting the response adhere to a predefined Pydantic schema for structured math reasoning. It validates that the returned content is correctly parsed against the schema and confirms the mathematical correctness of the final answer derived from the steps.*


### test_openai_func_to_anthropic_preserves_strict (function, L929-L983)

> *Summary: This test verifies that a utility function correctly converts an OpenAI-style tool definition to the Anthropic format, ensuring that the `strict: True` flag is preserved and that schema transformations (like setting `additionalProperties: false`) are applied only when strictness is indicated. It also confirms that non-strict tools retain their original structure without modification.*


### test_strict_tools_use_standard_api_with_strict (function, L987-L1030)

> *Summary: This test verifies that when using strictly defined tools, the client invokes the standard `messages.create()` API endpoint instead of a beta version. It asserts that the mock call was made, no beta headers are present in the request parameters, and the strict flag is correctly passed within the tool definitions.*


### test_legacy_tools_use_standard_api (function, L1034-L1072)

> *Summary: This test verifies that legacy tool calls default to using the standard Anthropic API endpoint. It mocks both the standard and beta message creation methods, then asserts that only the standard method is invoked when processing a request with non-strict function definitions.*


### test_real_strict_tool_use_api_call (function, L1083-L1146)

> *Summary: This test executes a real API call to Anthropic, sending a prompt that requires using a strictly defined calculator tool. It asserts that the response contains a valid tool call, and further verifies that the arguments passed to the tool adhere precisely to the specified types and enum constraints.*


### test_real_strict_tool_type_enforcement (function, L1152-L1201)

> *Summary: This test verifies that when using strict mode with an Anthropic client, the model correctly adheres to defined JSON schema types for function arguments. It sends a request specifying a `book_flight` tool and asserts that the resulting arguments contain integers, strings, and valid enumerated values as expected.*


### test_real_combined_strict_tools_and_structured_output (function, L1207-L1282)

> *Summary: This test executes an API call to Anthropic's model, simultaneously configuring both strict function calling and structured JSON output via Pydantic. It asserts that the response contains either valid tool calls adhering to strict typing or content conforming strictly to the defined `CalculationResult` schema.*


### test_real_sdk_version_validation_on_strict_tools (function, L1288-L1320)

> *Summary: This test verifies that the Anthropic client correctly validates the installed SDK version when using strict function calling tools. It attempts to call the API with specific parameters and asserts that no `ImportError` is raised if the SDK meets the required minimum version (0.74.1).*


### test_real_extended_thinking_api_call (function, L1331-L1399)

> *Summary: This test executes a real API call to Anthropic's model, specifically enabling the "extended thinking" feature for complex reasoning problems. It asserts that the returned content includes both the internal thought process (indicated by `[Thinking]`) and the final correct answer ("9").*


### test_real_tools_with_structured_output_beta_api (function, L1405-L1554)

> *Summary: This test verifies that Anthropic's beta API correctly handles the combination of OpenAI-formatted tools and structured output requests without returning a 400 error. It executes two scenarios: first, ensuring tool calls are generated when using both features, and second, confirming the model returns a valid Pydantic structure after processing a simulated tool result.*


### test_load_config_stream_enabled (function, L1563-L1572)

> *Summary: This test verifies that the `stream: True` parameter passed to a client's configuration loading method is correctly retained in the resulting configuration object. It asserts that the returned configuration explicitly has `"stream"` set to `True`.*


### test_create_streaming_routes (function, L1576-L1594)

> *Summary: This test verifies that the standard API call correctly delegates to the streaming implementation when `stream` is set to `True`. It mocks the internal streaming method and asserts that it was called after invoking the standard creation function with streaming parameters.*


### test_create_standard_no_stream_does_not_route (function, L1598-L1617)

> *Summary: This test verifies that the standard message creation method does not invoke the streaming counterpart when `stream` is explicitly set to `False`. It mocks both methods and asserts that the streaming function remains uncalled after executing the standard creation path with non-streaming parameters.*


### test_streaming_text_accumulation (function, L1621-L1706)

> *Summary: This test verifies text accumulation and event emission when processing streamed responses from an Anthropic client mock. It simulates a sequence of streaming events, asserts that the final accumulated content matches the expected string ("Hello world!"), and confirms that specific partial text chunks were correctly emitted via `StreamEvent`s.*


### test_streaming_tool_call_accumulation (function, L1710-L1797)

> *Summary: This test simulates streaming responses from an Anthropic client by mocking a sequence of `tool_use` events. It verifies that the system correctly accumulates partial JSON data across multiple stream chunks to reconstruct a complete tool call, and asserts the final message structure, finish reason, and token usage are correct.*


### test_streaming_thinking_blocks (function, L1801-L1881)

> *Summary: This test simulates streaming responses from an Anthropic client to verify how thinking and text blocks are processed. It mocks the API stream to inject specific events, then asserts that the final combined output starts with `[Thinking]` and contains both the thought process and the final answer.*


### test_real_streaming_text (function, L1892-L1925)

> *Summary: This test verifies the functionality of streaming text responses from the Anthropic API by making a real call with specific parameters. It asserts that the returned object contains valid choices, non-empty content matching expected keywords, and correctly tracks token usage and associated costs.*


### test_real_streaming_with_tools (function, L1931-L1979)

> *Summary: This test verifies the streaming behavior when invoking a model with defined tools. It sends a user prompt requesting a calculation, asserts that the streamed response correctly contains a tool call to the `calculator` function with the expected arguments (add 10 and 5), and confirms the final finish reason is set to "tool\_calls".*

