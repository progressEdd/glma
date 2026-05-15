# test/beta/middleware/builtins/test_llm_retry.py

4 function(s): test_llm_retry_calls_next_once_when_successful, test_llm_retry_retries_matching_errors_until_success, test_llm_retry_raises_after_exhausting_retries, test_llm_retry_does_not_retry_non_matching_errors. 2 class(es): TransientError, PermanentError.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TransientError | class |  |
| PermanentError | class |  |
| test_llm_retry_calls_next_once_when_successful | function |  |
| test_llm_retry_retries_matching_errors_until_success | function |  |
| test_llm_retry_raises_after_exhausting_retries | function |  |
| test_llm_retry_does_not_retry_non_matching_errors | function |  |

## Chunks

### TransientError (class, L14-L15)

> *Summary: Represents a temporary error condition that might resolve itself upon retrying an operation. It inherits from the base `Exception` class for standard Python error handling.*


### PermanentError (class, L18-L19)

> *Summary: Represents an unrecoverable error condition by inheriting from the base `Exception` class. This custom exception signals that retrying operations will not resolve the issue.*


### test_llm_retry_calls_next_once_when_successful (function, L23-L34)

> *Summary: This test verifies that the retry middleware executes the underlying LLM call exactly once when the initial attempt succeeds. It passes a mock object and input events to simulate a successful response from the LLM service.*


### test_llm_retry_retries_matching_errors_until_success (function, L38-L54)

> *Summary: This test verifies that a retry middleware successfully executes an LLM call until it succeeds after encountering transient errors. It simulates three calls, raising `TransientError` twice before the third attempt returns a successful `ModelResponse`.*


### test_llm_retry_raises_after_exhausting_retries (function, L58-L69)

> *Summary: This test verifies that the retry mechanism correctly raises an exception after exhausting all configured retries. It simulates a failing LLM call within a `RetryMiddleware` and asserts that the underlying function is called exactly one more time than the maximum allowed retries plus the initial attempt.*


### test_llm_retry_does_not_retry_non_matching_errors (function, L73-L84)

> *Summary: This test verifies that the `RetryMiddleware` correctly stops execution and raises an error when a non-transient exception occurs during an LLM call. It asserts that the underlying mock function is called exactly once, confirming no retries were attempted for the permanent error.*

