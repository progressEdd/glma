# test/llm_clients/test_openai_completions_client_with_fixtures.py

3 function(s): _load_fixture, _create_mock_response_from_fixture, mock_openai_client. 4 class(es): TestOpenAICompletionsClientWithFixtures, TestOpenAICompletionsClientCostWithFixtures, TestOpenAICompletionsClientMessageRetrievalWithFixtures, TestOpenAICompletionsClientV1CompatibleWithFixtures. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _load_fixture | function |  |
| _create_mock_response_from_fixture | function |  |
| mock_openai_client | function |  |
| TestOpenAICompletionsClientWithFixtures | class |  |
| TestOpenAICompletionsClientCostWithFixtures | class |  |
| TestOpenAICompletionsClientMessageRetrievalWithFixtures | class |  |
| TestOpenAICompletionsClientV1CompatibleWithFixtures | class |  |

## Chunks

### _load_fixture (function, L26-L30)

> *Summary: Reads a specified fixture name from the `openai_responses` directory within the test fixtures. It loads and returns the content of that JSON file as a dictionary, simulating an OpenAI response.*


### _create_mock_response_from_fixture (function, L33-L96)

> *Summary: This utility converts a dictionary fixture into a structured, mock object mimicking an OpenAI API response. It processes nested data to construct mock objects for usage statistics, choices (including messages and optional tool calls), and the overall response structure.*


### mock_openai_client (function, L100-L105)

> *Summary: This function sets up a mock instance of the OpenAI client by patching the actual `OpenAI` class within the module. It yields this configured mock object, allowing tests to control responses from the external API calls.*


### TestOpenAICompletionsClientWithFixtures (class, L108-L278)

> *Summary: This test suite verifies the `OpenAICompletionsClient` by executing various scenarios against mocked API responses loaded from fixtures. It confirms correct parsing and extraction of different response types, including simple text, multimodal vision data, tool calls, multi-turn context, system instructions, and multiple image inputs.*


### test_simple_text_response (method, L111-L140, parent: TestOpenAICompletionsClientWithFixtures)

> *Summary: This test verifies the `OpenAICompletionsClient` correctly processes a simple text response from an OpenAI API fixture. It asserts that the returned `UnifiedResponse` contains the expected ID, model name, provider, message content ("4"), and accurately reflects the token usage and calculated cost from the mock data.*


### test_multimodal_vision_response (method, L142-L171, parent: TestOpenAICompletionsClientWithFixtures)

> *Summary: This test verifies the client's ability to process a multimodal vision response from an OpenAI API fixture. It sends a request containing both text and an image URL, asserting that the resulting `UnifiedResponse` correctly extracts and contains the expected textual answer ("blue").*


### test_tool_call_response (method, L173-L200, parent: TestOpenAICompletionsClientWithFixtures)

> *Summary: This test verifies the client's ability to correctly process a response containing tool calls from an OpenAI API fixture. It asserts that the returned object is a `UnifiedResponse`, confirms the finish reason is `"tool_calls"`, and validates that the expected function name and arguments are present in the extracted tool call content.*


### test_multi_turn_context_response (method, L202-L226, parent: TestOpenAICompletionsClientWithFixtures)

> *Summary: This test verifies that the client correctly processes a multi-turn conversation by simulating an API call with historical messages as input. It asserts that the resulting unified response contains the context from previous turns, specifically confirming the mention of "blue."*


### test_system_message_response (method, L228-L250, parent: TestOpenAICompletionsClientWithFixtures)

> *Summary: This test verifies that the client correctly processes a system message when interacting with the OpenAI API using a predefined fixture. It asserts that the resulting unified response is of the correct type, contains one message, and includes the expected answer ("42") within its text content.*


### test_multiple_images_response (method, L252-L278, parent: TestOpenAICompletionsClientWithFixtures)

> *Summary: This test verifies the client's ability to process and return a response when the underlying API provides multiple images in the input prompt. It mocks an OpenAI response containing image data and asserts that the resulting `UnifiedResponse` correctly contains text output.*


### TestOpenAICompletionsClientCostWithFixtures (class, L281-L303)

> *Summary: This test verifies the cost calculation of an OpenAI completions client by using predefined fixture data. It mocks a successful API response and asserts that the resulting object contains a non-zero cost, while also confirming that retrieved usage statistics match the expected values from the fixture.*


### test_cost_calculation_with_real_usage (method, L284-L303, parent: TestOpenAICompletionsClientCostWithFixtures)

> *Summary: This test verifies that the cost calculation accurately reflects real API usage by mocking an OpenAI response based on a predefined fixture. It asserts that the returned object contains a positive cost and that subsequent usage retrieval matches the expected token counts from the fixture.*


### TestOpenAICompletionsClientMessageRetrievalWithFixtures (class, L306-L341)

> *Summary: This test suite verifies the `message_retrieval` functionality of an OpenAI completions client by simulating responses using predefined fixtures. It asserts that the method correctly extracts and structures message content, whether the underlying API response contains simple text or structured tool calls.*


### test_message_retrieval_from_text_fixture (method, L309-L321, parent: TestOpenAICompletionsClientMessageRetrievalWithFixtures)

> *Summary: This test verifies that a client correctly extracts structured messages from a mock OpenAI response loaded via a fixture. It calls the `create` method, then uses `message_retrieval` on the resulting object to assert the correct message content is returned.*


### test_message_retrieval_from_tool_call_fixture (method, L323-L341, parent: TestOpenAICompletionsClientMessageRetrievalWithFixtures)

> *Summary: This test verifies that the client correctly extracts and structures messages from a mocked OpenAI tool call response. It asserts that the resulting message contains the expected role, content structure, and a specific function call within its `tool_calls`.*


### TestOpenAICompletionsClientV1CompatibleWithFixtures (class, L344-L374)

> *Summary: This test verifies that the client correctly formats responses to be compatible with an older V1 standard when using mocked OpenAI API fixtures. It calls a method with specific inputs and asserts that the resulting dictionary adheres to expected structures for ID, model name, object type, choices, and usage details.*


### test_v1_compatible_with_real_response (method, L347-L374, parent: TestOpenAICompletionsClientV1CompatibleWithFixtures)

> *Summary: This test verifies that the client correctly formats a response from an OpenAI mock using a V1-compatible structure. It inputs a request payload and asserts that the resulting dictionary matches expected keys like `id`, `model`, and contains structured `choices` with message content.*

