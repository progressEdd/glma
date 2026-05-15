# test/beta/response/test_callable.py

4 class(es): TestNameDescription, TestSchemaGeneration, TestValidation, TestDependencyInjection. 32 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestNameDescription | class |  |
| TestSchemaGeneration | class |  |
| TestValidation | class |  |
| TestDependencyInjection | class |  |

## Chunks

### TestNameDescription (class, L17-L52)

> *Summary: This test suite verifies how the `@response_schema` decorator configures metadata on decorated functions. It checks that function names, custom names, docstrings, and explicit descriptions are correctly assigned to the wrapped callable based on provided arguments or source code attributes.*


### test_name_from_function (method, L18-L23, parent: TestNameDescription)

> *Summary: This method verifies that a decorated function retains its original name after applying the `@response_schema` decorator. It asserts that the callable's `name` attribute matches the defined function name, `"my_parser"`.*


### test_explicit_name (method, L25-L30, parent: TestNameDescription)

> *Summary: This test verifies that a decorated function correctly exposes its specified name. It defines a parser using `@response_schema(name="custom")` and asserts the resulting callable's `name` attribute is set to "custom".*


### test_description_from_docstring (method, L32-L38, parent: TestNameDescription)

> *Summary: This test verifies that the `@response_schema` decorator correctly extracts and assigns the docstring content of a decorated function to its `description` attribute. It passes a string input to the decorated parser, asserting the extracted description matches the expected value.*


### test_explicit_description (method, L40-L45, parent: TestNameDescription)

> *Summary: This test verifies that a decorated function correctly stores and exposes its provided documentation string. It takes a string input, converts it to an integer, and asserts the attached schema description matches the expected value.*


### test_no_docstring_gives_empty_string (method, L47-L52, parent: TestNameDescription)

> *Summary: This test verifies that a function decorated with `@response_schema` returns `None` for its description when no docstring is provided. It calls the decorated asynchronous parser with string input and asserts the resulting metadata property.*


### TestSchemaGeneration (class, L55-L209)

> *Summary: This test suite verifies that a decorator correctly generates JSON schemas for functions based on their input types and annotations. It demonstrates how different Python features—like basic types, dataclasses, unions, multiple parameters, field descriptions, defaults, and dependencies—influence the resulting schema structure.*


### test_single_str_param_no_schema (method, L56-L61, parent: TestSchemaGeneration)

> *Summary: This test verifies that a decorated function expecting a single string parameter, when no schema is provided, correctly results in `None` for its JSON schema attribute. It asserts the absence of a defined schema on the parsed callable.*


### test_single_int_param_generates_schema (method, L63-L78, parent: TestSchemaGeneration)

> *Summary: This test verifies that a function accepting a single integer parameter correctly generates a specific JSON schema. It asserts the resulting schema structure, which expects an object containing a required integer field named "data".*


### test_single_dataclass_param_generates_schema (method, L80-L96, parent: TestSchemaGeneration)

> *Summary: This test verifies that applying the `@response_schema` decorator to a function accepting a single dataclass parameter correctly generates a JSON schema reflecting the input's structure and types. It asserts that the resulting schema accurately describes an object with integer properties for 'x' and 'y'.*


### test_single_union_param_generates_schema (method, L98-L116, parent: TestSchemaGeneration)

> *Summary: This test verifies that a function accepting a union type (`int | str`) correctly generates a JSON schema. The resulting schema should define an object containing a `data` field whose type is specified by an `anyOf` array listing both "integer" and "string".*


### test_multi_params_generates_object_schema (method, L118-L130, parent: TestSchemaGeneration)

> *Summary: This test verifies that a function decorated with `@response_schema` correctly generates a JSON schema when it accepts multiple typed parameters. It asserts the resulting schema defines an object type requiring both a string `name` and an integer `age`.*


### test_multi_params_with_field_descriptions (method, L132-L145, parent: TestSchemaGeneration)

> *Summary: This test verifies that a decorated function correctly generates a JSON schema reflecting its input parameters and their associated field descriptions and default values. It asserts the structure of the generated schema for two annotated arguments, one required and one optional with a default.*


### test_multi_params_with_defaults (method, L147-L160, parent: TestSchemaGeneration)

> *Summary: This test verifies that a decorated function correctly generates a JSON schema reflecting its parameters. It asserts the schema includes a required `name` string and an optional `retries` integer with a default value of 3.*


### test_custom_fields_has_no_effect (method, L162-L180, parent: TestSchemaGeneration)

> *Summary: This test verifies that a decorated function's JSON schema correctly omits fields marked as having no effect, even when they are present in the signature. It asserts that the resulting schema only includes `name` (string) and `age` (integer) as required properties.*


### test_respect_dependencies (method, L182-L200, parent: TestSchemaGeneration)

> *Summary: This test verifies that a decorated function's JSON schema correctly reflects its dependencies. It asserts the structure of the `combine` function's schema, ensuring both string and integer inputs are present as required fields.*


### test_custom_schema_overrides_generated (method, L202-L209, parent: TestSchemaGeneration)

> *Summary: This test verifies that a provided custom JSON schema correctly overrides the generated schema for a decorated parsing function. It asserts that the `parse` callable retains the specified custom schema when initialized with an input string.*


### TestValidation (class, L212-L320)

> *Summary: These tests validate the `response_schema` decorator by exercising various serialization and deserialization scenarios. They confirm that functions decorated with this schema can correctly parse inputs from strings (JSON or raw values), handle synchronous/asynchronous execution, manage default arguments, and deserialize complex types like dataclasses and unions.*


### test_sync_str_param (method, L214-L221, parent: TestValidation)

> *Summary: This test verifies that a decorated asynchronous parser correctly converts an input string to an integer. It calls the validated function with `"42"` and asserts the returned value is `42`.*


### test_async_str_param (method, L224-L231, parent: TestValidation)

> *Summary: This test verifies that an asynchronous function decorated with a response schema correctly parses and validates an input string parameter into an integer. It calls the validated async parser with `"42"` and asserts the returned value is `42`.*


### test_single_int_param_deserializes (method, L234-L241, parent: TestValidation)

> *Summary: This test verifies that a function expecting a single integer parameter correctly deserializes input from a JSON string. It calls the decorated function with `{"data": 21}` and asserts the returned value is $42$ (the input multiplied by two).*


### test_single_dataclass_param_deserializes (method, L244-L259, parent: TestValidation)

> *Summary: This test verifies that a function accepting a single dataclass parameter can be successfully deserialized from JSON input. It takes a JSON string containing `x` and `y` values and asserts the resulting string output matches the expected format derived from the parsed dataclass instance.*


### test_single_union_param_deserializes (method, L262-L268, parent: TestValidation)

> *Summary: This test verifies that a function annotated with `response_schema` correctly deserializes input data when the parameter accepts either an integer or a string union type. It asserts successful conversion to a string for both numeric and string inputs provided in JSON format.*


### test_multi_params_with_defaults_uses_default (method, L271-L281, parent: TestValidation)

> *Summary: This test verifies that a decorated asynchronous function correctly uses default parameter values when only required arguments are provided during validation. It calls the decorated `process` function with just the `name`, expecting the output to incorporate the default value of 3 for `retries`.*


### test_multi_params_with_defaults_overridden (method, L284-L294, parent: TestValidation)

> *Summary: This test verifies that a decorated asynchronous function correctly processes input parameters when provided with values overriding default settings. It calls the validated function with JSON containing both `name` and `retries`, asserting the output matches the overridden values.*


### test_multi_params_deserializes_json (method, L297-L307, parent: TestValidation)

> *Summary: This test verifies that a decorated function expecting multiple parameters can successfully deserialize JSON input. It calls the decorated `greet` function with a JSON string containing `"name"` and `"age"` and asserts the returned formatted string matches expectations.*


### test_async_multi_params (method, L310-L320, parent: TestValidation)

> *Summary: This test verifies asynchronous validation of a function expecting multiple parameters. It calls the decorated `greet` coroutine with JSON input containing a name and age, asserting that the returned string matches the expected formatted greeting.*


### TestDependencyInjection (class, L323-L449)

> *Summary: This test suite verifies dependency injection mechanisms for response schemas by executing various parsing functions with predefined contexts. It confirms that parameters can be injected from the context variables, custom-named variables, default values, or external dependencies defined via `Depends`.*


### _make_context (method, L325-L334, parent: TestDependencyInjection)

> *Summary: Creates a new `Context` instance by initializing it with provided variables and dependencies, defaulting to empty dictionaries if none are supplied. This method serves as a factory for setting up the execution context.*


### test_context_injected (method, L337-L346, parent: TestDependencyInjection)

> *Summary: This test verifies that a decorated parsing function correctly incorporates contextual data during validation. It passes a string content and a pre-configured `Context` object to the parser, asserting the output reflects both the input value and the presence of specific variables within the context.*


### test_variable_injected (method, L349-L358, parent: TestDependencyInjection)

> *Summary: This test verifies that a decorated parsing function correctly incorporates variables from a provided execution context. It calls the parser with content and asserts the output string includes the injected language code.*


### test_variable_with_custom_name (method, L361-L370, parent: TestDependencyInjection)

> *Summary: This test verifies that a decorated asynchronous parsing function correctly incorporates custom variable values from the provided context into its output string. It takes content and language as input, returning a formatted string like `"content (language)"`.*


### test_variable_with_default (method, L373-L382, parent: TestDependencyInjection)

> *Summary: This test verifies that a decorated parsing function correctly applies a default value when an optional argument is omitted during validation. It asserts the output string includes the provided content and the default language ("en").*


### test_depends_injected (method, L385-L397, parent: TestDependencyInjection)

> *Summary: This test verifies dependency injection by calling a decorated parsing function with an input string and a dynamically provided suffix. It asserts that the output correctly combines the input content with the injected suffix value.*


### test_all_di_together (method, L400-L418, parent: TestDependencyInjection)

> *Summary: This test verifies a parsing function that constructs a formatted string by joining three components: a stream indicator, the input content, and a language code. It uses dependency injection to supply a separator and asserts the final output matches the expected format based on the provided context.*


### test_di_excluded_from_multi_param_schema (method, L421-L449, parent: TestDependencyInjection)

> *Summary: This test verifies that dependency injection parameters not explicitly defined in the schema are correctly resolved at runtime. It asserts that a function decorated with `@response_schema` only includes `name` and `age` in its JSON schema, while successfully using an injected `lang` parameter from the provided context during validation.*

