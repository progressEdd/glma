# test/agentchat/group/test_context_str.py

1 class(es): TestContextStr. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestContextStr | class |  |

## Chunks

### TestContextStr (class, L11-L146)

> *Summary: This test suite verifies the functionality of a class designed to format string templates using provided context data. It tests various scenarios including successful formatting with simple and complex inputs, error handling for missing variables, behavior with empty contexts, and correct substitution across different Python data types.*


### setup (method, L13-L23, parent: TestContextStr)

> *Summary: Initializes test fixtures by creating string templates and corresponding `ContextVariables` instances with predefined data. It then wraps these templates into `ContextStr` objects for use in testing context rendering.*


### test_init (method, L25-L28, parent: TestContextStr)

> *Summary: Verifies that an instance of `ContextStr` correctly stores the provided string template upon initialization. It confirms the internal `template` attribute matches the input value.*


### test_str (method, L30-L37, parent: TestContextStr)

> *Summary: Verifies that an instance of `ContextStr` produces a specific, unformatted string representation when cast to `str`. It confirms this output includes the original template placeholders.*


### test_format_simple (method, L39-L44, parent: TestContextStr)

> *Summary: This test verifies that a simple context string formatting operation produces the expected output, `"Hello, World!"`, when provided with predefined input data. It asserts the resulting formatted string matches the hardcoded expectation.*


### test_format_complex (method, L46-L51, parent: TestContextStr)

> *Summary: This test verifies that a complex context string correctly formats itself when provided with specific input data. It asserts the resulting formatted string matches an expected output containing user ID, item count, and a list of items.*


### test_format_with_error (method, L53-L69, parent: TestContextStr)

> *Summary: This test verifies that `ContextStr` correctly handles formatting when the provided context contains complex, non-directly formatable objects. It asserts that the resulting string uses the object's default string representation instead of failing during the `.format()` call.*


### test_format_missing_variable (method, L71-L79, parent: TestContextStr)

> *Summary: This test verifies that attempting to format a string template containing an undefined variable raises a `KeyError`. It achieves this by initializing a context string with a placeholder and calling the `.format()` method using a context lacking that specific key.*


### test_format_empty_context (method, L81-L94, parent: TestContextStr)

> *Summary: When provided with an empty set of context variables, this test verifies that formatting a string template results in the original template being returned unchanged. It uses a predefined template and an empty `ContextVariables` object to assert this behavior.*


### test_format_no_placeholders (method, L96-L106, parent: TestContextStr)

> *Summary: Verifies that formatting a string containing no placeholders returns the original template unchanged, regardless of the provided context data. It takes a `ContextStr` initialized with a static string and asserts its output matches the input template.*


### test_format_repeated_placeholders (method, L108-L118, parent: TestContextStr)

> *Summary: This test verifies that a template containing multiple identical placeholders correctly substitutes all occurrences using provided context data. It asserts the resulting string matches the expected output after formatting with simple input values.*


### test_format_various_data_types (method, L120-L146, parent: TestContextStr)

> *Summary: This test verifies that a string template containing placeholders for various data types (string, integer, float, boolean, list, dict) formats correctly when provided with corresponding values in a context object. It asserts the resulting formatted string matches the expected output structure.*

