# test/tools/test_function_utils.py

31 function(s): f, g, a_g, test_get_typed_annotation, test_get_typed_signature, test_get_typed_return_annotation, test_get_parameter_json_schema, test_get_required_params, test_get_default_values, test_get_param_annotations and 21 more. 2 class(es): Currency, NonBaseModelClass. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| f | function |  |
| g | function |  |
| a_g | function |  |
| test_get_typed_annotation | function |  |
| test_get_typed_signature | function |  |
| test_get_typed_return_annotation | function |  |
| test_get_parameter_json_schema | function |  |
| test_get_required_params | function |  |
| test_get_default_values | function |  |
| test_get_param_annotations | function |  |
| test_get_missing_annotations | function |  |
| test_get_parameters | function |  |
| test_get_function_schema_no_return_type | function |  |
| test_get_function_schema_unannotated_with_default | function |  |
| test_get_function_schema_missing | function |  |
| test_get_function_schema | function |  |
| Currency | class |  |
| test_get_function_schema_pydantic | function |  |
| NonBaseModelClass | class |  |
| test_get_load_param_if_needed_function | function |  |
| test_get_load_param_if_needed_function_base_model | function |  |
| test_get_load_param_if_needed_function_annotated_base_model | function |  |
| test_get_load_param_if_needed_function_basic_types | function |  |
| test_get_load_param_if_needed_function_plain_classes | function |  |
| test_get_load_param_if_needed_function_generic_aliases_fixed | function |  |
| test_get_load_param_if_needed_function_other_typing_constructs | function |  |
| test_get_load_param_if_needed_function_annotated_non_base_model | function |  |
| test_get_load_param_if_needed_function_nested_annotated | function |  |
| test_load_basemodels_if_needed_sync | function |  |
| test_load_basemodels_if_needed_async | function |  |
| test_serialize_to_str_with_nonascii | function |  |
| test_serialize_to_json | function |  |
| test_serialize_to_str_list_pydantic | function |  |

## Chunks

### f (function, L36-L37)

> *Summary: Accepts three parameters—`a` (string), `b` (integer defaulting to 2), and `c` (float defaulting to 0.1)—and requires a keyword-only argument `d`. The function currently does not perform any operations.*


### g (function, L40-L47)

> *Summary: Accepts a string `a`, an integer `b` (defaulting to 2), and a float `c` (defaulting to 0.1), along with a dictionary `d`. It is designed to return a string, though its current implementation does nothing.*


### a_g (function, L50-L57)

> *Summary: Accepts a string `a`, an integer `b` (defaulting to 2), and a float `c` (defaulting to 0.1), along with a dictionary `d`. It is designed to return a string, though the current implementation has no logic.*


### test_get_typed_annotation (function, L60-L63)

> *Summary: This test verifies that a utility function correctly retrieves the actual type object from both built-in types (like `str`) and string representations of types (like `"float"`). It asserts that the returned value matches the expected Python type.*


### test_get_typed_signature (function, L66-L68)

> *Summary: This test verifies that a utility function correctly extracts the parameter information from provided functions by comparing its output against Python's built-in `inspect.signature`. It asserts this equivalence for two different example functions, `f` and `g`.*


### test_get_typed_return_annotation (function, L71-L73)

> *Summary: This test verifies that a function designed to extract typed return annotations correctly returns `None` for one input and the expected type (`str`) for another. It asserts the output of the annotation retrieval utility against known values.*


### test_get_parameter_json_schema (function, L76-L109)

> *Summary: This test verifies the `get_parameter_json_schema` utility by asserting its correct behavior when generating JSON schemas for various Python types and models. It checks scenarios involving simple types with or without defaults, custom annotations, nullable fields, and complex Pydantic model structures with default values.*


### test_get_required_params (function, L112-L114)

> *Summary: This test verifies that a utility function correctly identifies the required positional arguments for two predefined functions, `f` and `g`, by inspecting their signatures. It asserts that both functions require parameters named "a" and "d".*


### test_get_default_values (function, L117-L119)

> *Summary: Verifies that the `get_default_values` utility correctly extracts default argument values from function signatures (`f` and `g`). It asserts that both functions yield a specific dictionary containing defaults for keys "b" and "c".*


### test_get_param_annotations (function, L122-L131)

> *Summary: This test verifies that a utility function correctly extracts parameter annotations from a typed function signature. It asserts that the returned dictionary matches the expected mapping of parameter names to their `Annotated` types.*


### test_get_missing_annotations (function, L134-L154)

> *Summary: This test verifies the `get_missing_annotations` utility by checking how it identifies parameters lacking annotations or those that rely on default values. It asserts correct outputs for functions with varying parameter signatures, including cases where missing arguments are identified versus when defaults cover them.*


### test_get_parameters (function, L157-L181)

> *Summary: This test verifies the `get_parameters` utility by inspecting a sample function's signature. It takes the derived required parameters, annotations, and default values to construct and assert against an expected JSON schema structure.*


### test_get_function_schema_no_return_type (function, L184-L196)

> *Summary: This test verifies that when a function lacks a return type annotation, the `get_function_schema` utility logs a specific warning message. It passes a function definition as input and asserts that the logger is called exactly once with the expected advisory string.*


### test_get_function_schema_unannotated_with_default (function, L199-L215)

> *Summary: This test verifies that when a function has unannotated parameters with default values, the schema generation process logs a specific warning. It calls `get_function_schema` on a sample function and asserts that the logger was called exactly once with the expected message detailing the missing annotations for parameters 'b', 'd', and 'e'.*


### test_get_function_schema_missing (function, L218-L230)

> *Summary: This test verifies that `get_function_schema` raises a `TypeError` when a function parameter lacks an annotation and has no default value. It asserts the error message correctly identifies the missing annotated parameter ('b') in the provided function signature.*


### test_get_function_schema (function, L233-L268)

> *Summary: This test verifies that a function schema generator correctly produces a specific JSON structure based on provided metadata and the target function object. It asserts equality between the generated schema from two different input functions against a predefined expected dictionary.*


### Currency (class, L274-L276)

> *Summary: Defines a data structure representing monetary values, requiring a `currency` symbol and an associated `amount`. It enforces that the amount defaults to 100.0 if not explicitly provided.*


### test_get_function_schema_pydantic (function, L279-L334)

> *Summary: This test verifies that a decorated function correctly generates a Pydantic-compliant JSON schema. It takes a Python function with annotated arguments and asserts the resulting structure matches an expected dictionary format detailing parameters and descriptions.*


### NonBaseModelClass (class, L340-L342)

> *Summary: This class initializes an object by accepting a single integer argument and storing it as an instance attribute named `value`. It serves as a simple data container for an integer input.*


### __init__ (method, L341-L342, parent: NonBaseModelClass)

> *Summary: Initializes an object by storing a single integer provided as input into its internal `value` attribute.*


### test_get_load_param_if_needed_function (function, L345-L354)

> *Summary: This test verifies the behavior of a function that conditionally loads parameters based on provided metadata and input data. It asserts that when no specific parameter is requested, it returns `None`, but correctly constructs an object from input data when a parameter definition is supplied.*


### test_get_load_param_if_needed_function_base_model (function, L357-L364)

> *Summary: This test verifies that the parameter loading function correctly returns a callable loader for `BaseModel` subclasses like `Currency`. It confirms the returned loader can successfully instantiate and return an object matching the provided input data structure.*


### test_get_load_param_if_needed_function_annotated_base_model (function, L367-L374)

> *Summary: This test verifies that a parameter loading function correctly handles `Annotated` types wrapping a `BaseModel`. It asserts that the returned loader is callable and successfully instantiates an object matching the provided data and type hint.*


### test_get_load_param_if_needed_function_basic_types (function, L377-L384)

> *Summary: This test verifies that the utility function returns `None` when provided with standard Python built-in types like `str`, `int`, and `float`. It confirms the function correctly handles basic, non-custom types as input.*


### test_get_load_param_if_needed_function_plain_classes (function, L387-L391)

> *Summary: This test verifies that the `get_load_param_if_needed_function` correctly returns `None` when provided with standard Python classes or specific enum types, rather than model-like structures. It asserts this behavior for a generic non-BaseModel class and an `Enum`.*


### test_get_load_param_if_needed_function_generic_aliases_fixed (function, L394-L399)

> *Summary: This test verifies that the `get_load_param_if_needed_function` correctly returns `None` when provided with various generic type hints like `list[str]`, `dict[str, int]`, and containers holding custom models. It ensures proper handling of complex type structures without triggering errors.*


### test_get_load_param_if_needed_function_other_typing_constructs (function, L402-L412)

> *Summary: This test verifies that the `get_load_param_if_needed_function` utility returns `None` when provided with various complex or non-function typing constructs. It specifically checks types like `Any`, unions (`str | int`), callable objects, and basic collection types (`list`, `dict`).*


### test_get_load_param_if_needed_function_annotated_non_base_model (function, L415-L418)

> *Summary: This test verifies that the `get_load_param_if_needed_function` correctly returns `None` when provided with types wrapped in `Annotated`, specifically for string and list-of-integers annotations. It confirms the function handles these annotated non-base model structures as expected.*


### test_get_load_param_if_needed_function_nested_annotated (function, L421-L428)

> *Summary: This test verifies that a parameter loading function correctly extracts and instantiates a `BaseModel` even when it is wrapped within nested `Annotated` types. It confirms the returned loader is callable and produces an instance matching the expected data structure.*


### test_load_basemodels_if_needed_sync (function, L431-L445)

> *Summary: This test verifies that a decorated function, which conditionally loads base models, executes synchronously when called with specific currency inputs. It asserts the returned tuple contains correctly instantiated `Currency` and `CurrencySymbol` objects matching the provided arguments.*


### test_load_basemodels_if_needed_async (function, L449-L463)

> *Summary: This test verifies that a decorated asynchronous function correctly loads base models when necessary, accepting a `Currency` and an optional `CurrencySymbol`. It asserts the returned tuple contains the expected `Currency` object with its original values and the specified `CurrencySymbol`.*


### test_serialize_to_str_with_nonascii (function, L466-L467)

> *Summary: Verifies that the serialization function correctly handles and preserves non-ASCII characters, specifically Chinese text. It asserts that passing `"中文"` results in the exact string `"中文"`.*


### test_serialize_to_json (function, L470-L481)

> *Summary: This test verifies that the `serialize_to_str` function correctly converts various Python types—strings, integers, lists, dictionaries, and Pydantic models—into their string representations. It asserts specific expected outputs for these diverse input structures.*


### test_serialize_to_str_list_pydantic (function, L484-L493)

> *Summary: This test verifies that a list of Pydantic model instances is correctly serialized into a specific string format. It takes a list of `A` models and asserts the output matches a JSON-like string representation containing dictionaries for each instance.*

