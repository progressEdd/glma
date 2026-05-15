# test/oai/test_groq.py

9 function(s): mock_response, groq_client, test_groq_llm_config_entry, test_initialization, test_valid_initialization, test_parsing_params, test_cost_calculation, test_create_response, test_create_response_with_tool_call.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_response | function |  |
| groq_client | function |  |
| test_groq_llm_config_entry | function |  |
| test_initialization | function |  |
| test_valid_initialization | function |  |
| test_parsing_params | function |  |
| test_cost_calculation | function |  |
| test_create_response | function |  |
| test_create_response_with_tool_call | function |  |

## Chunks

### mock_response (function, L18-L27)

> *Summary: Provides a factory function that returns a mock response class capable of simulating API responses with configurable fields like text, choices, usage, and cost. This allows for isolated testing by providing predefined data structures instead of making actual external calls.*


### groq_client (function, L31-L32)

> *Summary: Instantiates and returns a `GroqClient` object, using a placeholder API key for testing purposes. This function provides the necessary client instance to interact with the Groq service during tests.*


### test_groq_llm_config_entry (function, L35-L55)

> *Summary: This test verifies that a `GroqLLMConfigEntry` object correctly serializes its configuration parameters, including API key and model name. It further asserts that wrapping this entry within an `LLMConfig` structure produces the expected list format for overall configuration.*


### test_initialization (function, L60-L70)

> *Summary: This test verifies that instantiating a client without an API key raises an `AssertionError` containing a specific message about missing credentials. It then confirms successful initialization when a fake API key is provided during instantiation.*


### test_valid_initialization (function, L75-L76)

> *Summary: Verifies that the provided `groq_client` object has its `api_key` attribute correctly set to `"fake_api_key"` during initialization testing. This confirms proper configuration loading for API access.*


### test_parsing_params (function, L81-L157)

> *Summary: This test verifies a parameter parsing utility by passing various input dictionaries to it, checking that the output correctly applies defaults, handles missing required fields (like `model`), and manages out-of-bounds or incorrectly typed values according to expected behavior. It asserts specific outcomes for complete, partial, invalid, and boundary-violating inputs.*


### test_cost_calculation (function, L162-L173)

> *Summary: This test verifies the cost calculation logic by providing a mocked API response containing token usage and model information. It asserts that the calculated Groq cost matches an expected value of $0.000532 based on the input tokens and model name.*


### test_create_response (function, L179-L207)

> *Summary: This test verifies that a client correctly processes and returns a structured response from the Groq API when mocking its chat endpoint. It inputs specific message history and model parameters to assert that the resulting object contains the expected content, ID, model name, and token usage data from the mock response.*


### test_create_response_with_tool_call (function, L213-L269)

> *Summary: This test verifies the system's ability to handle responses containing multiple tool calls from a Groq API interaction. It mocks the client response to assert that the returned object correctly includes predefined function call structures for both currency calculation and weather retrieval.*

