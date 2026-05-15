# test/oai/test_cohere.py

6 function(s): cohere_client, test_cohere_llm_config_entry, test_initialization_missing_api_key, test_initialization, test_calculate_cohere_cost, test_load_config.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| cohere_client | function |  |
| test_cohere_llm_config_entry | function |  |
| test_initialization_missing_api_key | function |  |
| test_initialization | function |  |
| test_calculate_cohere_cost | function |  |
| test_load_config | function |  |

## Chunks

### cohere_client (function, L18-L19)

> *Summary: Instantiates and returns a `CohereClient` object, using a placeholder API key for testing purposes. This function serves to provide a configured client instance for interaction with the Cohere service during tests.*


### test_cohere_llm_config_entry (function, L22-L46)

> *Summary: This test verifies that a `CohereLLMConfigEntry` object correctly serializes its configuration parameters, including model name and temperature. It further asserts that wrapping this entry within an `LLMConfig` structure produces the expected list format for overall configuration storage.*


### test_initialization_missing_api_key (function, L50-L58)

> *Summary: This test verifies that instantiating a `CohereClient` without an API key, either through environment variables or direct input, raises an `AssertionError`. It confirms the client correctly enforces the presence of a required authentication key during initialization.*


### test_initialization (function, L62-L63)

> *Summary: Verifies that a provided `CohereClient` instance has its `api_key` attribute correctly initialized to `"dummy_api_key"`. This test ensures proper configuration upon client instantiation.*


### test_calculate_cohere_cost (function, L67-L71)

> *Summary: Verifies the `calculate_cohere_cost` function by asserting expected costs for specific token counts and models. It confirms that zero tokens result in zero cost and checks a known calculation for non-zero inputs.*


### test_load_config (function, L75-L87)

> *Summary: Verifies that the client's parameter parsing method correctly transforms a set of input configuration parameters into an expected output structure. It confirms specific key mappings and value preservation during this transformation process.*

