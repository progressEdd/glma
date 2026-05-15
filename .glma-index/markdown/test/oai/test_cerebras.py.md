# test/oai/test_cerebras.py

9 function(s): mock_response, cerebras_client, test_cerebras_llm_config_entry, test_initialization, test_valid_initialization, test_parsing_params, test_cost_calculation, test_create_response, test_create_response_with_tool_call.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_response | function |  |
| cerebras_client | function |  |
| test_cerebras_llm_config_entry | function |  |
| test_initialization | function |  |
| test_valid_initialization | function |  |
| test_parsing_params | function |  |
| test_cost_calculation | function |  |
| test_create_response | function |  |
| test_create_response_with_tool_call | function |  |

## Chunks

### mock_response (function, L18-L27)

> *Summary: Provides a factory function that returns a mock response class capable of simulating API responses with configurable fields like text, choices, usage, cost, and model name. This allows for testing interactions without making actual external calls.*


### cerebras_client (function, L31-L32)

> *Summary: Instantiates and returns a `CerebrasClient` object, using a placeholder API key for testing purposes. This function serves to provide a configured client instance for interacting with the Cerebras service.*


### test_cerebras_llm_config_entry (function, L35-L61)

> *Summary: This test verifies that a `CerebrasLLMConfigEntry` object correctly serializes its configuration parameters, including API key, model name, and generation settings. It further asserts that wrapping this entry in an `LLMConfig` structure produces the expected list format for configuration storage.*


### test_initialization (function, L66-L77)

> *Summary: This test verifies that instantiating a client without an API key raises an `AssertionError` containing a specific message, while successfully creating the client when an API key is provided. It confirms proper initialization behavior based on configuration presence.*


### test_valid_initialization (function, L82-L83)

> *Summary: Verifies that the provided client object has its `api_key` attribute correctly initialized to `"fake_api_key"` during setup. This test confirms proper configuration loading for the Cerebras client.*


### test_parsing_params (function, L88-L156)

> *Summary: This test verifies a parameter parsing utility by passing various input dictionaries to it, asserting that the output correctly applies defaults or handles type/range errors as expected. It specifically checks scenarios including full parameter sets, minimal inputs, incorrect data types, out-of-bounds values, and missing required fields like the model name.*


### test_cost_calculation (function, L161-L178)

> *Summary: This test verifies the cost calculation logic by feeding it token counts and a model name from a mocked API response. It asserts that the function's output matches an expected value derived from predefined per-token pricing rates for prompt and completion tokens.*


### test_create_response (function, L184-L212)

> *Summary: This test verifies that a client correctly processes and structures a mock response from a Cerebras API call. It inputs specific message history and model parameters to assert that the returned object contains the expected content, ID, model name, and token usage statistics from the mocked service.*


### test_create_response_with_tool_call (function, L218-L278)

> *Summary: This test verifies that a client correctly processes and returns a model response containing multiple tool calls when provided with function definitions. It mocks the API interaction to assert that the resulting response structure includes specific function names (`currency_calculator` and `get_weather`) within the message content.*

