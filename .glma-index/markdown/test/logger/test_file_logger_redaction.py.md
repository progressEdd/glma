# test/logger/test_file_logger_redaction.py

1 class(es): TestRedactSensitiveKeys. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestRedactSensitiveKeys | class |  |

## Chunks

### TestRedactSensitiveKeys (class, L19-L204)

> *Summary: This test suite verifies the functionality of a redaction utility by testing its behavior across various data structures. It ensures that sensitive keys (like `api_key`, `password`) are replaced with "***REDACTED***" in dictionaries, while correctly handling nested objects, lists, tuples, and respecting recursion depth limits.*


### test_api_key_redacted (method, L26-L30, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that a redaction function correctly masks sensitive API keys within a dictionary while preserving other data fields. It takes an input dictionary containing both a key and non-sensitive data, asserting the output has the key replaced with "***REDACTED***".*


### test_unknown_key_not_redacted (method, L32-L37, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that keys not explicitly listed as sensitive are passed through the redaction process unchanged. It takes a dictionary containing known and unknown keys, calls the `_redact` function, and asserts that all original values remain in the output.*


### test_azure_ad_token_redacted (method, L39-L42, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that sensitive data within a dictionary is correctly masked by the redaction utility. It passes a dictionary containing an Azure AD token and asserts that the token field is replaced with "***REDACTED***".*


### test_hyphenated_api_key_redacted (method, L44-L48, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that API keys using a hyphenated format are correctly redacted. It passes a dictionary containing an `"api-key"` and asserts the corresponding value in the output is replaced with `***REDACTED***`.*


### test_password_redacted (method, L50-L53, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that a password field within an input dictionary is correctly masked by the `_redact` function. It asserts that the output dictionary's "password" key contains the string "***REDACTED***".*


### test_specific_token_keys_redacted (method, L55-L61, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that sensitive keys like `access_token` and `refresh_token` are correctly replaced with a redaction marker when passed to the `_redact` function. It asserts that all specified token fields in the input dictionary are redacted in the returned result.*


### test_azure_ad_token_variants_redacted (method, L63-L68, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that specific sensitive keys, `azure_ad_token` and `azure_ad_token_provider`, are correctly replaced with a redaction marker when passed to the `_redact` function. It asserts that both input values are transformed into "***REDACTED***" in the returned dictionary.*


### test_base_url_not_redacted (method, L70-L74, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that the `base_url` field, which is considered non-sensitive, remains unchanged after passing a dictionary through the redaction function. It asserts that the input URL matches the output URL in the resulting data structure.*


### test_llm_token_params_not_redacted (method, L76-L87, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that specific LLM parameters containing "token" are intentionally excluded from redaction. It passes a dictionary of token-related values to the `_redact` function and asserts that the output remains identical to the input.*


### test_non_sensitive_keys_unchanged (method, L89-L92, parent: TestRedactSensitiveKeys)

> *Summary: Verifies that keys deemed non-sensitive remain unaltered after passing a dictionary through the redaction process. It asserts that the output dictionary is identical to the input when no sensitive information is present.*


### test_exact_key_variants_redacted (method, L94-L100, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that the redaction function correctly masks values associated with exact key variants like `api_key`, `api-key`, and `apikey`. It asserts that all provided keys are replaced with the standard "***REDACTED***" string.*


### test_remaining_sensitive_keys_redacted (method, L102-L114, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that all keys defined as sensitive within the system are completely replaced with "***REDACTED***". It passes a dictionary containing various secret values to the redaction function and asserts every original key maps to the redacted string in the output.*


### test_case_insensitive_matching (method, L116-L122, parent: TestRedactSensitiveKeys)

> *Summary: Verifies that the redaction process correctly masks sensitive values regardless of case in the input dictionary keys. It takes a dictionary containing various key-value pairs and asserts all corresponding values are replaced with `***REDACTED***`.*


### test_nested_sensitive_key_redacted (method, L128-L132, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that the redaction utility correctly masks a sensitive key nested within a dictionary structure. It takes a dictionary containing an API key and asserts that only the specified key is replaced with "***REDACTED***", while other values remain unchanged.*


### test_doubly_nested_redacted (method, L134-L137, parent: TestRedactSensitiveKeys)

> *Summary: Tests the redaction utility by passing a deeply nested dictionary containing sensitive data. It asserts that the specific secret value within the structure is replaced with "***REDACTED***".*


### test_list_with_dicts_redacted (method, L143-L147, parent: TestRedactSensitiveKeys)

> *Summary: Tests the redaction utility by passing a list containing dictionaries, asserting that sensitive values like `"api_key"` are replaced with `***REDACTED***` while non-sensitive data remains unchanged.*


### test_list_type_preserved (method, L149-L152, parent: TestRedactSensitiveKeys)

> *Summary: Verifies that the redaction process maintains the input data structure's type. It takes a list of dictionaries as input and asserts the output is also a list.*


### test_tuple_type_preserved (method, L154-L158, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that the redaction function preserves the input data structure's type. It passes a tuple containing dictionaries and asserts the output is still a tuple while confirming sensitive data within it has been redacted.*


### test_depth_limit_prevents_infinite_recursion (method, L164-L174, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that the redaction function handles deeply nested data structures (over 10 levels) by ensuring it completes execution without triggering a `RecursionError`. It constructs a dictionary with 20 nested layers and asserts the output is still a dictionary.*


### test_default_depth_is_ten (method, L176-L191, parent: TestRedactSensitiveKeys)

> *Summary: This test verifies that when a data structure's target field resides at or beyond the default redaction depth of ten, the sensitive value remains unredacted. It constructs a nested dictionary and asserts that an `api_key` placed at depth 11 is returned as its original string value after processing by the redaction function.*


### test_scalar_string_unchanged (method, L197-L198, parent: TestRedactSensitiveKeys)

> *Summary: Verifies that a simple, non-sensitive scalar string remains unaltered when passed through the redaction function. It asserts the output matches the input for this basic test case.*


### test_none_unchanged (method, L200-L201, parent: TestRedactSensitiveKeys)

> *Summary: Verifies that passing `None` to the redaction function results in `None` being returned, ensuring no modification occurs for null inputs.*


### test_integer_unchanged (method, L203-L204, parent: TestRedactSensitiveKeys)

> *Summary: Verifies that the redaction function leaves integer inputs unchanged. It asserts that passing the integer `42` results in the same value being returned.*

