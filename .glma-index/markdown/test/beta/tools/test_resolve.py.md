# test/beta/tools/test_resolve.py

6 class(es): TestResolveVariable, TestWebSearchToolVariable, TestWebFetchToolVariable, TestShellToolVariable, TestImageGenerationToolVariable, TestMCPServerToolVariable. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestResolveVariable | class |  |
| TestWebSearchToolVariable | class |  |
| TestWebFetchToolVariable | class |  |
| TestShellToolVariable | class |  |
| TestImageGenerationToolVariable | class |  |
| TestMCPServerToolVariable | class |  |

## Chunks

### TestResolveVariable (class, L19-L53)

> *Summary: This suite of tests verifies the `resolve_variable` function's behavior when retrieving values from a provided context. It confirms correct handling for passthrough values, fetching from context, applying defaults and default factories, respecting context precedence, and raising errors for missing keys.*


### test_passthrough (method, L20-L23, parent: TestResolveVariable)

> *Summary: Verifies that the `resolve_variable` function correctly returns its input unchanged for various types, including strings, integers, and `None`. This test ensures a basic passthrough behavior across different data types.*


### test_from_context (method, L25-L31, parent: TestResolveVariable)

> *Summary: Given a context creation function and a user location, this method resolves the `user_location` variable within that context. It asserts that the resolved value matches the original input location object.*


### test_default (method, L33-L38, parent: TestResolveVariable)

> *Summary: This test verifies that when a variable resolution fails to find a value, it correctly returns the provided `UserLocation` fallback object. It calls `resolve_variable` with a defined default and asserts the output matches that default.*


### test_default_factory (method, L40-L43, parent: TestResolveVariable)

> *Summary: This test verifies that when a variable is initialized with `default_factory=dict`, the resolution process returns an empty dictionary. It calls `resolve_variable` using a `Variable` instance configured this way and asserts the output matches `{}`.*


### test_context_takes_precedence_over_default (method, L45-L49, parent: TestResolveVariable)

> *Summary: When resolving a variable with a specified default, this test confirms that the provided context overrides the default value. It asserts that if the context sets `"mode"` to `"fast"`, the resolved value is `"fast"` instead of the default `"slow"`.*


### test_missing_raises (method, L51-L53, parent: TestResolveVariable)

> *Summary: Asserts that calling `resolve_variable` with a variable key not present in the provided context raises a `KeyError` containing "user\_location". This verifies the function's error handling when required context data is absent.*


### TestWebSearchToolVariable (class, L56-L73)

> *Summary: This test verifies that a `WebSearchTool` correctly resolves its required `UserLocation` variable from the provided context when available. It also asserts that calling the schema method raises a `KeyError` if the specified location variable is missing from the context.*


### test_resolved (method, L58-L66, parent: TestWebSearchToolVariable)

> *Summary: This test verifies that a `WebSearchTool` correctly resolves its input location from the provided context. It asserts that the resulting tool schema contains the expected `UserLocation` object passed into the context creation function.*


### test_missing_raises (method, L69-L73, parent: TestWebSearchToolVariable)

> *Summary: This test verifies that attempting to retrieve schemas from a `WebSearchTool` when the required "loc" variable is missing raises a `KeyError`. It asserts that the error message specifically contains "loc".*


### TestWebFetchToolVariable (class, L76-L92)

> *Summary: This test suite verifies the behavior of a `WebFetchTool` when its parameters are defined using variables. It asserts that if a variable is provided in the context, the tool correctly resolves and uses its value, while also confirming it raises a `KeyError` if the required variable is missing from the context.*


### test_resolved (method, L78-L85, parent: TestWebFetchToolVariable)

> *Summary: This test verifies that a `WebFetchTool` correctly resolves its configuration when provided with a context object. It asserts that the resulting schema accurately reflects the limit set in the input context.*


### test_missing_raises (method, L88-L92, parent: TestWebFetchToolVariable)

> *Summary: This test verifies that calling the `schemas` method on a `WebFetchTool` raises a `KeyError` if the required "limit" variable is missing from the provided context. It asserts that the error message specifically contains "limit".*


### TestShellToolVariable (class, L95-L112)

> *Summary: This test verifies the behavior of a shell tool when resolving environment variables. It asserts that schemas are correctly returned using an existing environment context and confirms that a `KeyError` is raised if the required environment variable is missing from the provided context.*


### test_resolved (method, L97-L105, parent: TestShellToolVariable)

> *Summary: This test verifies that a `ShellTool` correctly resolves its schema when provided with a context and environment. It asserts that the returned schema is of type `ShellToolSchema` and correctly references the input environment.*


### test_missing_raises (method, L108-L112, parent: TestShellToolVariable)

> *Summary: This test verifies that calling the `schemas` method on a `ShellTool` raises a `KeyError` if the required "env" variable is missing from the provided context. It asserts that the raised exception specifically matches the key name "env".*


### TestImageGenerationToolVariable (class, L115-L132)

> *Summary: This test verifies that an image generation tool correctly resolves variable inputs from a provided context during schema retrieval. It asserts successful resolution when variables are present and confirms a `KeyError` is raised if required variables are missing from the context.*


### test_resolved (method, L117-L125, parent: TestImageGenerationToolVariable)

> *Summary: This test verifies that an `ImageGenerationTool` correctly generates a schema when provided with a context containing specific image dimensions. It asserts that the resulting schema accurately reflects the configured quality and size parameters from the input context.*


### test_missing_raises (method, L128-L132, parent: TestImageGenerationToolVariable)

> *Summary: This test verifies that calling the `schemas` method on an `ImageGenerationTool` raises a `KeyError` if the required `partial_images` variable is missing from the provided context. It asserts that the error message specifically contains "partial\_images".*


### TestMCPServerToolVariable (class, L135-L151)

> *Summary: This test suite verifies the behavior of an `MCPServerTool` when resolving its configuration from a provided context. It asserts that schemas are correctly resolved using a specified URL and confirms that attempting to resolve with a missing variable raises a `KeyError`.*


### test_resolved (method, L137-L144, parent: TestMCPServerToolVariable)

> *Summary: This test verifies that the `MCPServerTool` correctly retrieves and validates its schema when provided with a specific context URL. It asserts that the returned schema object is of the expected type and contains the correct server URL from the input context.*


### test_missing_raises (method, L147-L151, parent: TestMCPServerToolVariable)

> *Summary: This test verifies that calling the `schemas` method on an `MCPServerTool` raises a `KeyError` if the required "url" variable is missing from the provided context. It asserts this specific exception occurs when attempting to retrieve schemas without the necessary configuration.*

