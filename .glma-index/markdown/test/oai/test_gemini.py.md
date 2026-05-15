# test/oai/test_gemini.py

3 function(s): test_gemini_llm_config_entry, test_gemini_llm_config_entry_thinking_level, test_gemini_llm_config_entry_thinking_config. 1 class(es): TestGeminiClient. 57 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_gemini_llm_config_entry | function |  |
| test_gemini_llm_config_entry_thinking_level | function |  |
| test_gemini_llm_config_entry_thinking_config | function |  |
| TestGeminiClient | class |  |

## Chunks

### test_gemini_llm_config_entry (function, L32-L55)

> *Summary: This test verifies that a `GeminiLLMConfigEntry` object correctly serializes its configuration parameters into a dictionary. It then asserts that wrapping this entry within an `LLMConfig` structure produces the expected list-based output format.*


### test_gemini_llm_config_entry_thinking_level (function, L59-L67)

> *Summary: This test verifies that a `GeminiLLMConfigEntry` correctly stores and exposes any provided `thinking_level`. It instantiates the configuration with a given level and asserts that the resulting dictionary contains the exact same value for "thinking\_level".*


### test_gemini_llm_config_entry_thinking_config (function, L70-L82)

> *Summary: This test verifies that a `GeminiLLMConfigEntry` object correctly serializes its thinking configuration parameters. It asserts that the resulting dictionary contains the expected boolean, integer, and string values for thought inclusion, budget, and level.*


### TestGeminiClient (class, L86-L1997)

> *Summary: This test suite verifies the functionality of a Gemini client wrapper, covering initialization logic for various authentication methods (API key, Google credentials, VertexAI). It extensively tests message format conversions between OAI and Gemini standards, handles complex features like function calling with nested parameters, streaming responses, cost calculation, and advanced thought signature tracking across different execution environments.*


### mock_response (method, L89-L98, parent: TestGeminiClient)

> *Summary: This method returns a class constructor that creates mock response objects containing simulated data like generated text, choice details, usage statistics, and associated costs for testing API interactions. It allows tests to simulate various successful or structured responses from an AI service.*


### gemini_client (method, L101-L105, parent: TestGeminiClient)

> *Summary: Instantiates and returns a `GeminiClient` object, configuring it with a predefined system message instructing the model to act as a helpful AI assistant. It uses a placeholder API key for initialization.*


### gemini_google_auth_default_client (method, L108-L112, parent: TestGeminiClient)

> *Summary: This method initializes and returns a `GeminiClient` instance, configuring it with a predefined system message instructing the model to act as a helpful AI assistant. It takes no arguments but produces a ready-to-use client object.*


### gemini_client_with_credentials (method, L115-L117, parent: TestGeminiClient)

> *Summary: This method constructs and returns a `GeminiClient` instance, injecting a mocked set of credentials for testing purposes. It simulates the initialization process by using a `MagicMock` object to represent the required credential input.*


### test_compute_location_initialization (method, L120-L124, parent: TestGeminiClient)

> *Summary: This test asserts that instantiating a `GeminiClient` with both a provided API key and a specified compute location raises an `AssertionError`. It verifies the client's initialization logic enforces constraints on input parameters.*


### test_project_initialization (method, L127-L131, parent: TestGeminiClient)

> *Summary: This test asserts that instantiating a `GeminiClient` with provided, but likely invalid or incomplete, credentials will raise an `AssertionError`. It verifies the client's initialization logic correctly fails when specific configuration parameters are supplied.*


### test_valid_initialization (method, L133-L134, parent: TestGeminiClient)

> *Summary: Verifies that the provided `gemini_client` object has its `api_key` attribute correctly set to `"fake_api_key"` during initialization testing. This confirms proper configuration of the client's authentication credential.*


### test_google_application_credentials_initialization (method, L136-L140, parent: TestGeminiClient)

> *Summary: This test verifies that initializing a `GeminiClient` with specific credentials correctly sets the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to the provided JSON file. It asserts this environment variable matches the input credential path.*


### test_vertexai_initialization (method, L142-L147, parent: TestGeminiClient)

> *Summary: This test verifies that the `GeminiClient` correctly configures global settings upon instantiation. It asserts that the provided project ID, location, and mocked credentials are accurately stored in the `vertexai_global_config`.*


### test_extract_system_instruction (method, L149-L174, parent: TestGeminiClient)

> *Summary: This test verifies the logic for extracting a system instruction from a list of chat messages. It asserts correct behavior across various inputs, including valid instructions, empty or malformed message lists, and cases where the system message is not the first element.*


### test_gemini_message_handling (method, L176-L209, parent: TestGeminiClient)

> *Summary: This test verifies the conversion of a list of structured messages into the format required by the Gemini API. It takes an input list containing various roles and content, converts it using a client method, and asserts that the resulting structure matches a predefined expected output, checking both role mapping and content accuracy.*


### test_gemini_empty_message_handling (method, L211-L225, parent: TestGeminiClient)

> *Summary: This test verifies that an empty string content within a user message is correctly transformed into the text "empty" when converting messages for the Gemini API. It asserts this transformation occurs for specific instances of empty user inputs in the provided message list.*


### test_gemini_message_without_role_defaults_to_user (method, L227-L242, parent: TestGeminiClient)

> *Summary: This test verifies that when converting a list of messages for Gemini, any message lacking an explicit `role` defaults to the `"user"` role. It confirms this behavior by asserting the roles and content of sample input messages after conversion.*


### test_parallel_function_responses_merged (method, L244-L292, parent: TestGeminiClient)

> *Summary: Verifies that multiple sequential tool responses, which are initially separate messages, are correctly merged into a single `Content` object when converting to Gemini format. It takes a list of mixed role messages (user, assistant with calls, and two distinct tool responses) as input and asserts the resulting structure contains one consolidated content block holding both function responses.*


### test_single_function_response_not_affected (method, L294-L320, parent: TestGeminiClient)

> *Summary: This test verifies that a single function response is correctly processed when converting messages from an OpenAI format to Gemini's internal representation. It takes a list of messages containing a user prompt, an assistant tool call, and the corresponding tool output, asserting the structure and content of the final converted message.*


### test_vertexai_safety_setting_conversion (method, L322-L350, parent: TestGeminiClient)

> *Summary: This test verifies that a list of Gemini-style safety settings is correctly converted into the corresponding Vertex AI format. It takes predefined harm categories and thresholds as input and asserts that the resulting structure matches the expected `VertexAISafetySetting` objects exactly.*


### test_vertexai_default_safety_settings_dict (method, L352-L373, parent: TestGeminiClient)

> *Summary: This test verifies that a dictionary of default Vertex AI safety settings is correctly transformed by the `GeminiClient._to_vertexai_safety_settings` method. It asserts that the resulting structure contains the expected categories and block thresholds for harassment, hate speech, sexually explicit content, and dangerous content.*


### test_vertexai_safety_setting_list (method, L375-L401, parent: TestGeminiClient)

> *Summary: This test verifies that a list of predefined Vertex AI harm categories and thresholds correctly converts into the expected format using a private client method. It asserts both the count and the content equality of the resulting converted safety settings against the initial configuration.*


### test_internal_server_error_retry (method, L405-L414, parent: TestGeminiClient)

> *Summary: This test verifies that the client automatically retries a request when an `InternalServerError` occurs during interaction with the Gemini model. It simulates a failure followed by success, asserting that the final outcome reflects the successful retry mechanism.*


### test_cost_calculation (method, L417-L425, parent: TestGeminiClient)

> *Summary: This test verifies that the cost calculation method returns a positive value when provided with a mocked API response containing token usage and a specified cost. It asserts that the resulting cost is greater than zero based on the mock data.*


### test_create_response_with_text (method, L430-L474, parent: TestGeminiClient)

> *Summary: This test verifies the response structure when interacting with a Gemini client by mocking all external dependencies. It asserts that the returned object contains the expected text content, token counts, and calculated cost based on mocked inputs.*


### test_vertexai_create_response (method, L479-L527, parent: TestGeminiClient)

> *Summary: This test verifies the response handling for a Gemini API call by mocking the underlying generative model and cost calculation. It asserts that the returned object contains the expected text content, token counts (prompt/completion/total), and matches the mocked calculated cost.*


### test_extract_json_response (method, L529-L577, parent: TestGeminiClient)

> *Summary: Verifies a utility method's ability to deserialize string responses into predefined Pydantic models. It tests successful parsing of valid JSON matching the schema, and asserts that `ValueError` is raised for malformed or non-JSON input strings.*


### nested_function_parameters (method, L580-L619, parent: TestGeminiClient)

> *Summary: Generates a JSON schema object defining the structure for an input containing a main question and an array of subquestions. This schema dictates that the top-level object must contain a `task` property, which in turn requires both a string `question` and an array of objects conforming to the `Subquestion` definition.*


### test_unwrap_references (method, L621-L656, parent: TestGeminiClient)

> *Summary: This test verifies that a dictionary of nested function parameters is correctly unwrapped into a specific JSON schema structure. It asserts that the output matches a predefined object containing a "Task" property with required fields for questions and subquestions.*


### test_generation_config_with_proxy (method, L660-L712, parent: TestGeminiClient)

> *Summary: This test verifies that when a proxy is provided during client creation, the `HttpOptions` are correctly configured with the specified proxy URL. It asserts that both synchronous and asynchronous client arguments include the correct proxy setting while also validating other generation parameters passed to the configuration object.*


### test_create_gemini_function_parameters_with_nested_parameters (method, L714-L743, parent: TestGeminiClient)

> *Summary: This test verifies that the internal function correctly constructs a complex JSON schema for Gemini API parameters when provided with nested input data. It asserts that the generated structure matches a predefined expectation containing nested objects and arrays within the properties definition.*


### test_create_gemini_function_declaration_returns_schema (method, L745-L782, parent: TestGeminiClient)

> *Summary: This test verifies that the internal function declaration creation method correctly produces a `Schema` object for the parameters. It asserts the structure is correct and ensures no Pydantic serialization warnings are generated when dumping the resulting object.*


### test_create_gemini_function_declaration_schema_handles_required_and_enum (method, L784-L803, parent: TestGeminiClient)

> *Summary: This test verifies that the schema creation utility correctly processes JSON input containing both required fields and enumerated string properties. It asserts that the resulting `Schema` object accurately reflects the specified requirements, including the presence of a required field and an enum list for a specific property.*


### test_create_gemini_function_declaration_schema_with_nested_refs (method, L805-L836, parent: TestGeminiClient)

> *Summary: Verifies that the schema creation utility correctly resolves deeply nested `$ref` references within a JSON schema structure. It takes a dictionary containing definitions and properties, returning a `Schema` object where internal references are properly resolved.*


### test_generation_config_with_seed (method, L840-L883, parent: TestGeminiClient)

> *Summary: This test verifies that specific generation parameters, including a `seed`, are correctly translated and passed into the underlying configuration object when calling the Gemini client. It asserts that values like temperature, max tokens, top\_p, and top\_k match the expected inputs in the mock call arguments.*


### test_generation_config_with_thinking_config (method, L888-L930, parent: TestGeminiClient)

> *Summary: Verifies that specific thinking parameters (`include_thoughts` and `thinking_budget`) are correctly packaged into a configuration object and subsequently passed to the generation content settings when calling the Gemini client. It mocks the entire interaction flow, asserting that the generated config matches the expected structure derived from the input arguments.*


### test_generation_config_with_default_thinking_config (method, L935-L973, parent: TestGeminiClient)

> *Summary: This test verifies that a default `ThinkingConfig` is automatically instantiated and supplied when no specific thinking parameters are provided during an API call. It asserts that the mock configuration object receives this default config when interacting with the generative client.*


### test_generation_config_thinking_param_variants (method, L1032-L1077, parent: TestGeminiClient)

> *Summary: This test verifies that various thinking parameters are correctly propagated through the system. It calls a client method with input arguments and then asserts that both the `ThinkingConfig` and `GenerateContentConfig` mocks were called with the expected parameter values derived from the inputs.*


### test_vertexai_generation_config_with_seed (method, L1081-L1123, parent: TestGeminiClient)

> *Summary: This test verifies that the `seed` parameter is correctly forwarded when creating a configuration for VertexAI generation. It calls a client method with specific parameters and asserts that the underlying generation config object was invoked with the expected values, including the seed, temperature, and token limits.*


### test_check_if_prebuilt_google_search_tool_exists (method, L1126-L1149, parent: TestGeminiClient)

> *Summary: This test verifies if a specific prebuilt Google Search tool is present within a list of provided tools. It asserts that the internal checking mechanism correctly identifies the presence or absence of the tool based on its name.*


### test_tools_to_gemini_tools (method, L1152-L1182, parent: TestGeminiClient)

> *Summary: This test verifies the conversion of a standard function-calling tool definition into a Gemini-specific `Tool` object structure. It passes a list containing one function tool and asserts that the resulting structure matches an expected `Tool` instance, depending on whether the input name is "prebuilt\_google\_search".*


### test_response_format_uses_response_json_schema_for_non_vertexai (method, L1186-L1232, parent: TestGeminiClient)

> *Summary: Verifies that when interacting with a non-VertexAI endpoint, the API call correctly utilizes `response_json_schema` instead of `response_schema` for structured output. It simulates a chat interaction using Pydantic models to confirm the correct schema parameter is passed during client creation.*


### test_response_format_uses_response_schema_for_vertexai (method, L1236-L1277, parent: TestGeminiClient)

> *Summary: This test verifies that when interacting with VertexAI, the API call correctly utilizes `response_schema` instead of `response_json_schema` for structured output. It mocks a successful Gemini response and asserts that the configuration passed to the client includes `response_schema` while excluding `response_json_schema`.*


### test_thought_signature_initialized_in_init (method, L1279-L1283, parent: TestGeminiClient)

> *Summary: Verifies that the `gemini_client` object possesses a `tool_call_thought_signatures` attribute upon initialization, confirming it is an empty dictionary. This test ensures the internal structure for thought signature mapping is correctly set up during object creation.*


### test_thought_signature_captured_from_response (method, L1287-L1336, parent: TestGeminiClient)

> *Summary: This test verifies that the `thought_signature` is correctly captured from a mocked Gemini response when function calls are involved. It simulates a response containing a function call part with a specific signature and asserts that this signature is stored internally against the corresponding tool call ID.*


### test_thought_signature_retained_across_calls (method, L1340-L1442, parent: TestGeminiClient)

> *Summary: This test verifies that the `thought_signature` associated with a function call is correctly persisted across sequential API calls to the Gemini model. It simulates an initial tool-calling response, captures the signature, and then confirms its retention after sending back the simulated tool execution result in a subsequent request.*


### test_thought_signature_included_in_reconstructed_parts (method, L1444-L1478, parent: TestGeminiClient)

> *Summary: This test verifies that a specific `thought_signature` associated with a tool call is correctly embedded when converting an OAI-style message into Gemini content parts. It inputs a message containing a function call and asserts the resulting `Part` object includes the expected signature bytes.*


### test_thought_signature_none_when_not_present (method, L1480-L1507, parent: TestGeminiClient)

> *Summary: Verifies that the generated content part has a `None` `thought_signature` when the input function map lacks signature information. It processes an assistant message containing a tool call and asserts the resulting Gemini content part reflects this absence.*


### test_thought_signature_captured_from_vertex_part_via_to_dict (method, L1509-L1531, parent: TestGeminiClient)

> *Summary: This test verifies that the `thought_signature` from a Vertex-like part is correctly extracted when accessed via its `to_dict()` method, rather than being available as a direct attribute. It mocks a part object to simulate this behavior and asserts that the signature is captured and decoded correctly within the client's internal tracking mechanism.*


### test_thought_signature_replayed_on_vertex_same_agent (method, L1533-L1568, parent: TestGeminiClient)

> *Summary: This test verifies that when simulating a tool call on Vertex, the generated content correctly includes a `thought_signature`. It sets up a specific signature and asserts that the resulting Gemini content object contains this signature, ensuring compatibility with Vertex's requirements for replayed function calls.*


### test_thought_signature_replayed_on_vertex_cross_agent (method, L1570-L1598, parent: TestGeminiClient)

> *Summary: This test verifies that the Vertex implementation correctly preserves a base64 encoded `thought_signature` when simulating a cross-agent handoff where the receiving client has an empty instance state. It constructs a message containing this signature and asserts that it is successfully passed through the content conversion process intact.*


### test_thought_signature_embedded_in_tool_call_for_cross_agent (method, L1602-L1662, parent: TestGeminiClient)

> *Summary: This test verifies that a `thought_signature` is correctly base64-encoded and embedded within the returned tool call object when interacting with a generative client. It asserts that this signature is accessible both directly on the tool call structure and stored internally by the client for cross-agent routing purposes.*


### test_thought_signature_reconstructed_from_tool_call_dict_cross_agent (method, L1664-L1704, parent: TestGeminiClient)

> *Summary: This test verifies that a thought signature embedded in a `tool_call` dictionary can be correctly reconstructed when processing messages between agents. It simulates Agent B receiving a message where the signature is present in the tool call but missing from its local state, asserting that the decoding process retrieves the original byte signature.*


### test_thought_signature_instance_dict_fallback_when_not_in_tool_call (method, L1706-L1738, parent: TestGeminiClient)

> *Summary: Verifies that when a tool call lacks an explicit signature in its structure, the system correctly falls back to retrieving the thought signature from the agent's instance dictionary. It takes a message containing a tool call ID and asserts that the resulting content object contains the expected signature retrieved from the client's internal map.*


### test_thought_signature_not_embedded_when_absent (method, L1740-L1758, parent: TestGeminiClient)

> *Summary: This test verifies that when a model response part lacks a `thought_signature`, the processing logic correctly omits this signature from the resulting tool call structure. It simulates an input with no thought signature and asserts that the output tool call does not possess that attribute.*


### test_streaming_text_response (method, L1762-L1804, parent: TestGeminiClient)

> *Summary: This test verifies that a streaming API call correctly aggregates text chunks from an iterator and reports final usage statistics. It mocks the generative client to return a sequence of predefined response chunks, asserting the final concatenated content and token counts are accurate.*


### test_streaming_with_tool_calls (method, L1808-L1847, parent: TestGeminiClient)

> *Summary: Verifies that streaming responses correctly handle the initial output when a function call is requested by the model. It simulates receiving a stream chunk containing a `tool_calls` structure and asserts the resulting message reflects this invocation.*


### test_streaming_emits_stream_events (method, L1851-L1889, parent: TestGeminiClient)

> *Summary: Verifies that streaming events are correctly emitted when interacting with a Gemini client. It mocks the API response to simulate streamed chunks containing specific text content and asserts that this content is passed through the output stream interface.*


### test_non_streaming_does_not_call_send_message_stream (method, L1893-L1924, parent: TestGeminiClient)

> *Summary: This test verifies that when a request is made with `stream=False`, the underlying client calls the non-streaming `send_message` method instead of `send_message_stream`. It mocks the Gemini client and response objects to assert this specific call behavior.*


### test_oai_content_to_gemini_content_missing_content_key (method, L1926-L1952, parent: TestGeminiClient)

> *Summary: This test verifies that the conversion utility handles input messages lacking a `content` key by serializing non-role fields into a JSON text part. It asserts that the resulting output correctly contains this structured data, while omitting the original role information.*


### test_vertexai_streaming (method, L1957-L1997, parent: TestGeminiClient)

> *Summary: This test verifies that the VertexAI client correctly invokes `send_message` with `stream=True` when streaming is requested. It mocks a response stream containing specific content chunks to assert the correct behavior of the underlying API call.*

