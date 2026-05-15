# test/beta/config/openai/test_openai_usage.py

1 class(es): TestNormalizeUsage. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestNormalizeUsage | class |  |

## Chunks

### TestNormalizeUsage (class, L13-L47)

> *Summary: This test suite verifies the `normalize_usage` function's behavior when transforming a `CompletionUsage` object into a simplified `Usage` object. It ensures that cached token information from nested details is correctly extracted, handled as `None` if absent or null, and accurately reflected in the output structure.*


### test_lifts_cached_tokens (method, L14-L27, parent: TestNormalizeUsage)

> *Summary: This test verifies that the `normalize_usage` function correctly transforms a `CompletionUsage` object containing cached token details into a standard `Usage` object. It asserts that the input's `prompt_tokens_details.cached_tokens` value is mapped to the output's `cache_read_input_tokens`.*


### test_no_details_no_cache_key (method, L29-L32, parent: TestNormalizeUsage)

> *Summary: This test verifies that when provided with usage details lacking specific input token information, the normalization process correctly sets the `cache_read_input_tokens` to `None`. It takes a `CompletionUsage` object as input and asserts the resulting normalized object's state.*


### test_details_with_zero_cached_tokens (method, L34-L42, parent: TestNormalizeUsage)

> *Summary: When provided with usage details where the prompt tokens have zero cached values, this test asserts that the normalized output reflects no input token caching was read. It verifies the `cache_read_input_tokens` field is set to zero after processing the input structure.*


### test_none_details (method, L44-L47, parent: TestNormalizeUsage)

> *Summary: When provided with usage details where `prompt_tokens_details` is `None`, the normalization function returns a structure indicating no cached input tokens were read. This test verifies that the output correctly reflects the absence of detailed prompt token information.*

