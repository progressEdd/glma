# test/beta/config/openai/test_openai_responses_usage.py

1 class(es): TestNormalizeUsage. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestNormalizeUsage | class |  |

## Chunks

### TestNormalizeUsage (class, L13-L63)

> *Summary: This test suite verifies the `normalize_responses_usage` function's ability to transform a detailed `ResponseUsage` object into a simplified `Usage` structure. It confirms correct mapping of input/output tokens and accurately extracts specific token counts like cached reads or reasoning contributions into designated fields.*


### test_normalizes_input_output_keys (method, L14-L29, parent: TestNormalizeUsage)

> *Summary: This test verifies that a `ResponseUsage` object is correctly transformed into a standardized `Usage` structure. It takes an instance containing token counts and details as input and asserts the output matches the expected normalized format with specific key mappings.*


### test_lifts_cached_tokens (method, L31-L46, parent: TestNormalizeUsage)

> *Summary: This test verifies that the `normalize_responses_usage` function correctly transforms a detailed usage object. It takes an input structure specifying token counts and cached tokens, returning a standardized usage object with separated prompt and completion token fields.*


### test_lifts_reasoning_tokens (method, L48-L63, parent: TestNormalizeUsage)

> *Summary: This test verifies the `normalize_responses_usage` function by providing a specific usage object with detailed token counts. It asserts that the normalization correctly maps input and output tokens to standard prompt/completion fields while adjusting for cached and reasoning token details.*

