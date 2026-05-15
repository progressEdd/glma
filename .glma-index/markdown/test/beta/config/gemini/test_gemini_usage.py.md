# test/beta/config/gemini/test_gemini_usage.py

1 function(s): _make_metadata. 1 class(es): TestNormalizeUsage. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_metadata | function |  |
| TestNormalizeUsage | class |  |

## Chunks

### _make_metadata (function, L13-L20)

> *Summary: Creates a mock object populated with specified token counts for prompt, candidates, total, and optional cached or thought content. This utility simulates usage metrics for testing Gemini API interactions.*


### TestNormalizeUsage (class, L23-L84)

> *Summary: This test suite verifies that the `normalize_usage` function correctly transforms raw usage metadata into a standardized `Usage` object. It checks various scenarios, including handling optional fields like cache reads and thinking tokens, managing `None` or zero values for different metrics, and ensuring robustness against incomplete input structures.*


### test_normalizes_to_standard_keys (method, L24-L26, parent: TestNormalizeUsage)

> *Summary: This test verifies that a usage object generated from arbitrary metadata is correctly normalized. It asserts the resulting `Usage` object contains specific token counts for prompt, completion, and total tokens.*


### test_includes_cache_read_tokens (method, L28-L35, parent: TestNormalizeUsage)

> *Summary: This test verifies that the usage calculation correctly incorporates cached read tokens when metadata indicates a cache hit. It asserts the resulting `Usage` object contains specific values for prompt, completion, total, and the provided cache read input tokens.*


### test_no_cache_key_when_none (method, L37-L39, parent: TestNormalizeUsage)

> *Summary: When provided with `None` for caching metadata, this test asserts that the resulting usage object's cache read input tokens attribute remains `None`. This verifies correct handling of absent caching information during usage normalization.*


### test_no_cache_key_when_zero (method, L41-L43, parent: TestNormalizeUsage)

> *Summary: When provided with a cached value of zero, the function processes metadata to ensure no cache read input tokens are generated in the resulting usage object. This verifies that zero-value inputs correctly bypass caching mechanisms.*


### test_handles_none_token_counts_on_streaming_chunks (method, L45-L50, parent: TestNormalizeUsage)

> *Summary: Verifies that the usage normalization process correctly handles `None` values within metadata emitted during streaming chunks. It asserts that when input parameters are all `None`, the resulting usage object is empty and evaluates to `False`.*


### test_handles_partial_token_counts (method, L52-L54, parent: TestNormalizeUsage)

> *Summary: Validates that the `normalize_usage` function correctly processes metadata where only prompt token counts are provided. It asserts the output matches a `Usage` object containing exactly 50 prompt tokens when given input specifying this value.*


### test_includes_thinking_tokens (method, L56-L63, parent: TestNormalizeUsage)

> *Summary: This test verifies that the usage calculation correctly incorporates tokens designated as "thoughts." It asserts that when metadata includes 296 thinking tokens, the resulting `Usage` object accurately reflects this value alongside standard prompt and completion token counts.*


### test_no_thinking_key_when_none (method, L65-L67, parent: TestNormalizeUsage)

> *Summary: Verifies that when no thoughts are provided in the metadata, the resulting usage object correctly sets `thinking_tokens` to `None`. This test confirms proper handling of null input for thought tracking during usage normalization.*


### test_no_thinking_key_when_zero (method, L69-L71, parent: TestNormalizeUsage)

> *Summary: When provided with zero thoughts in the metadata, this test asserts that the resulting usage object's `thinking_tokens` attribute is set to `None`. It verifies correct handling of a zero-value input for thought tokens during normalization.*


### test_handles_metadata_without_thoughts_field (method, L73-L84, parent: TestNormalizeUsage)

> *Summary: This test verifies that the `normalize_usage` function correctly handles usage metadata when the `thoughts_token_count` field is absent from the input mock object. It asserts that the resulting structure's `thinking_tokens` attribute remains `None` under these conditions.*

