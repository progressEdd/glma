# test/tools/test_dependency_injection.py

3 class(es): TestRemoveInjectedParamsFromSignature, MyContext, TestHelperFunctions. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestRemoveInjectedParamsFromSignature | class |  |
| TestHelperFunctions | class |  |

## Chunks

### TestRemoveInjectedParamsFromSignature (class, L27-L191)

> *Summary: This test suite verifies that a utility function correctly strips dependency injection annotations and parameters from a given function's signature. It uses various example functions with different combinations of `Depends` and context types to assert the resulting simplified signature only contains non-injected arguments, like `a: int`.*


### MyContext (class, L28-L29, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This class inherits from `BaseContext` and `BaseModel`, adding an integer attribute named `b`. It serves as a context object with basic data storage capabilities.*


### f_with_annotated (method, L31-L37, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This method accepts an integer and two context objects—one injected with specific dependencies and another annotated for type checking—and returns the sum of the input integer and a value from the dependency-injected context. It asserts that the chat context is of the expected type before performing the addition.*


### f_with_annotated_async (method, L39-L45, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This asynchronous method accepts an integer and two dependency-injected objects—one for general context with a specific configuration (`b=2`) and one for chat context. It validates the chat context type and returns the sum of the input integer and the configured value from the general context object.*


### f_without_annotated (method, L48-L54, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This function accepts an integer and a `ChatContext` object as inputs, along with a dependency-injected `MyContext`. It validates the `ChatContext` type and returns the sum of the input integer and the `b` attribute from the injected context.*


### f_without_annotated_async (method, L57-L63, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This asynchronous function accepts an integer and a `ChatContext`, while automatically injecting a `MyContext` instance with `b=3`. It returns the sum of the input integer and the injected context's `b` attribute.*


### f_without_annotated_and_depends (method, L66-L70, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This method takes an integer `a` and a context object `ctx` (defaulting to one with `b=4`) as input. It returns the sum of `a` and the value of `ctx.b`.*


### f_without_annotated_and_depends_async (method, L73-L77, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This asynchronous method takes an integer and a context object as input, returning the sum of the integer and the context's `b` attribute. It demonstrates a function that lacks dependency annotations while still utilizing provided context data.*


### f_without_MyContext (method, L80-L84, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This function accepts an integer `a` and another integer `ctx`, which is derived by adding 2 to the input `a`. It returns the sum of these two provided integers.*


### f_without_MyContext_async (method, L87-L91, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This asynchronous function takes an integer `a` and another integer `ctx`, which is derived by adding 2 to the input `a`. It returns the sum of these two integers.*


### f_with_default_depends (method, L94-L98, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This method accepts an integer `a` and a context value derived from a default dependency function that adds two to the input `a`. It returns the sum of the initial integer and the calculated context value.*


### f_with_default_depends_async (method, L101-L105, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This asynchronous function accepts an integer `a` and a dependency `ctx`, which is calculated by adding 2 to the input `a`. It returns the sum of the initial input `a` and the resolved dependency value `ctx`.*


### setup (method, L108-L122, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: Initializes the test fixture by setting up a predefined list of expected tool definitions, specifically containing one function schema with an integer parameter named 'a'. This structure is used to validate dependency injection scenarios within tests.*


### f_all_params (method, L125-L136, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This function accepts various inputs, including primitive types and dependencies resolved from context providers. It demonstrates how different dependency injection mechanisms—like explicit `Depends` calls with arguments or simple constructor injection—are utilized to populate its parameters before returning the value of parameter `a`.*


### test_is_base_context_param (method, L138-L148, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This test verifies the `_is_context_param` helper function by inspecting the signature of a target method (`self.f_all_params`). It asserts that specific parameters are correctly identified as context parameters or not, based on their expected behavior.*


### test_is_chat_context_param (method, L150-L156, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This test verifies the `_is_context_param` utility function against a set of parameters from an inspected function signature. It asserts that specific parameters (`ctx1`, `ctx3`, `ctx4`) are not instances of `ChatContext`, while others (`ctx6`, `ctx7`) correctly are.*


### test_get_chat_context_params (method, L158-L160, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This test verifies that the `get_context_params` function correctly extracts specific context parameters (`"ctx6"`, `"ctx7"`) from a provided set of all parameters when targeting the `ChatContext` subclass. It asserts that the returned list matches the expected values.*


### test_is_depends_param (method, L162-L172, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This test verifies the `_is_depends_param` utility function by inspecting a function's signature. It asserts that parameters without dependency annotations return `False`, while those explicitly annotated with `Depends` correctly return `True`.*


### test_remove_injected_params_from_signature (method, L189-L191, parent: TestRemoveInjectedParamsFromSignature)

> *Summary: This test verifies that a utility function correctly strips injected parameters from a given callable's signature. It asserts that the resulting function's signature matches an expected format, specifically `(a: int) -> int`.*


### TestHelperFunctions (class, L194-L241)

> *Summary: This class provides helper methods and tests to validate how metadata annotations are correctly processed by introspection utilities. It specifically verifies that string metadata attached to function parameters is accurately reflected in the resulting field descriptions, and that return type annotations are correctly converted to `Any`.*


### f_sync (method, L195-L200, parent: TestHelperFunctions)

> *Summary: This function accepts three integer inputs—two required and one optional with type annotation metadata—and returns the sum of the first two arguments. It performs simple addition on `a` and `b`, ignoring the value of `c`.*


### f_async (method, L202-L207, parent: TestHelperFunctions)

> *Summary: This asynchronous method accepts three integer inputs—one standard, one annotated with a specific description, and an optional third annotated input. It calculates and returns the sum of the first two provided integers.*


### test_string_metadata_to_description_field (method, L216-L230, parent: TestHelperFunctions)

> *Summary: This test verifies that metadata attached to function arguments is correctly exposed as a `Field` object with the expected description string. It inspects type hints from a provided callable to assert the presence and content of this metadata for different Python versions.*


### test_set_return_annotation_to_any (method, L239-L241, parent: TestHelperFunctions)

> *Summary: This test verifies that a utility function correctly modifies the return type annotation of a given callable to `Any`. It takes a function as input and asserts that the resulting function's signature reflects this change.*

