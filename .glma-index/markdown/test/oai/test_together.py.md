# test/oai/test_together.py

3 function(s): mock_response, together_client, test_together_llm_config_entry. 1 class(es): TestTogether. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_response | function |  |
| together_client | function |  |
| test_together_llm_config_entry | function |  |
| TestTogether | class |  |

## Chunks

### mock_response (function, L18-L27)

> *Summary: Provides a factory function that returns a class capable of simulating an API response object. This mock object holds structured data like generated text, choice details, usage metrics, and associated costs for testing purposes.*


### together_client (function, L31-L32)

> *Summary: Instantiates and returns a `TogetherClient` object, using a placeholder API key for initialization. This function serves to provide an initialized client instance for testing purposes.*


### test_together_llm_config_entry (function, L35-L56)

> *Summary: This test verifies that an instance of `TogetherLLMConfigEntry`, initialized with specific model and API details, correctly serializes its attributes. It further asserts that wrapping this entry within an `LLMConfig` object results in the expected structure containing a list of configurations.*


### TestTogether (class, L60-L284)

> *Summary: This test suite verifies the functionality of a client for interacting with Together AI, covering initialization checks (requiring an API key), parameter parsing with defaults and type validation, cost calculation from usage metrics, and successful text generation or tool-calling responses via mocked API calls. It ensures correct handling of various input parameters and expected output structures for both standard chat completions and function/tool invocation requests.*


### test_initialization (method, L62-L73, parent: TestTogether)

> *Summary: This test verifies that instantiating a client without an API key raises an `AssertionError` containing a specific message about missing credentials. It then confirms successful initialization when a dummy API key is provided during construction.*


### test_valid_initialization (method, L76-L77, parent: TestTogether)

> *Summary: Verifies that the `TogetherClient` instance is initialized with the expected hardcoded API key value. It asserts that the internal `api_key` attribute matches `"fake_api_key"`.*


### test_parsing_params (method, L80-L157, parent: TestTogether)

> *Summary: This test verifies the parameter parsing logic of a client by passing various input dictionaries to `parse_params`. It asserts that the function correctly handles complete sets, defaults for missing values, type coercion (even with incorrect inputs), and clamping/defaulting for out-of-bounds numerical values.*


### test_cost_calculation (method, L160-L173, parent: TestTogether)

> *Summary: This test verifies the cost calculation function by providing mock API usage data (prompt/completion tokens and model name). It asserts that the calculated cost matches a specific expected value of $0.000018 based on these inputs.*


### test_create_response (method, L177-L209, parent: TestTogether)

> *Summary: This test verifies that a client correctly processes and returns a structured response from an external AI service when mocking its API call. It inputs specific message parameters to the `create` method and asserts that the returned object contains the expected content, ID, model name, and token usage statistics from the mock.*


### test_create_response_with_tool_call (method, L213-L284, parent: TestTogether)

> *Summary: This test verifies the API's behavior when a model responds with a tool call. It simulates an external service returning a specific structure containing a `tool_call` for the `currency_calculator` function, asserting that the resulting response correctly reflects this invocation.*

