# test/fast_depends/test_schema.py

2 function(s): test_base, test_depends. 4 class(es): TestNoType, TestOneArg, TestOneArgWithModel, TestMultiArgs. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_base | function |  |
| TestNoType | class |  |
| TestOneArg | class |  |
| TestOneArgWithModel | class |  |
| TestMultiArgs | class |  |
| test_depends | function |  |

## Chunks

### test_base (function, L20-L25)

> *Summary: This test verifies the output of `get_schema` when provided with a call model generated from a simple function. It asserts that the resulting schema correctly identifies the input as having no defined structure, represented by `{"title": "handler", "type": "null"}`.*


### TestNoType (class, L28-L64)

> *Summary: These tests verify how the schema generation handles functions with no explicit type annotations. They assert that the resulting JSON schema correctly represents input parameters, including cases where defaults are present or when embedding is enabled during schema creation.*


### test_no_type (method, L29-L39, parent: TestNoType)

> *Summary: When provided with a function that accepts one argument but has no explicit type hints, this test asserts the generated JSON schema correctly defines an object requiring a property named "a". The output confirms the structure includes `"properties": {"a": {"title": "A"}}` and `"required": ["a"]`.*


### test_no_type_embedded (method, L41-L46, parent: TestNoType)

> *Summary: When building a call model with `embed=True`, this test asserts that the resulting schema correctly omits type information for functions where no types are explicitly defined. It verifies the structure of the generated schema against an expected dictionary.*


### test_no_type_with_default (method, L48-L57, parent: TestNoType)

> *Summary: This test verifies that a function signature with an optional argument lacking an explicit type results in a JSON schema where the corresponding property is marked as partial. It achieves this by generating and asserting against the schema derived from a simple handler function.*


### test_no_type_with_default_and_embed (method, L59-L64, parent: TestNoType)

> *Summary: This test verifies that when a function argument lacks an explicit type hint but has a default value, the generated schema correctly represents it as a partial dictionary. It asserts that the resulting schema matches `IsPartialDict({"title": "A"})` after embedding is enabled during schema generation.*


### TestOneArg (class, L67-L118)

> *Summary: This test suite verifies the JSON schema generation for functions accepting a single argument. It checks various scenarios including required arguments, optional/nullable inputs, default values, and embedding the schema directly into the function's definition.*


### test_one_arg (method, L68-L78, parent: TestOneArg)

> *Summary: This test verifies that a single-argument function correctly generates a JSON schema. It asserts the resulting schema accurately describes an object requiring one integer property named "a".*


### test_one_arg_with_embed (method, L80-L85, parent: TestOneArg)

> *Summary: This test verifies that when embedding is enabled, the generated schema for a function accepting one integer argument correctly reflects its expected type. It asserts that the resulting schema matches `{"title": "A", "type": "integer"}`.*


### test_one_arg_with_optional (method, L87-L100, parent: TestOneArg)

> *Summary: This test verifies that a function accepting one optional integer argument is correctly represented in the generated JSON schema. It asserts the resulting schema includes an object structure where the single property allows either an integer or null, and it is marked as required.*


### test_one_arg_with_default (method, L102-L111, parent: TestOneArg)

> *Summary: This test verifies that a function accepting one optional integer argument with a default value of zero is correctly represented in the generated JSON schema. It asserts the resulting schema includes the property definition for 'a' with its specified default and type.*


### test_one_arg_with_default_and_embed (method, L113-L118, parent: TestOneArg)

> *Summary: This test verifies the generated schema for a function accepting one optional integer argument with a default value. It asserts that the resulting schema correctly reflects the default value and type information.*


### TestOneArgWithModel (class, L121-L295)

> *Summary: This test suite verifies how a function signature, containing one argument typed by a Pydantic model, is converted into an OpenAPI schema. It tests various scenarios including reference resolution, optional arguments (with and without embedding), and nested models to ensure the generated JSON Schema accurately reflects the input types.*


### test_base (method, L122-L143, parent: TestOneArgWithModel)

> *Summary: This test verifies that the generated JSON schema correctly represents a function signature where an input model with an integer property `a` is expected. It asserts that the resulting schema accurately defines the structure and references for both the input model and the overall handler object.*


### test_resolved_model (method, L145-L165, parent: TestOneArgWithModel)

> *Summary: This test verifies that when resolving references, the generated JSON schema correctly represents a function handler expecting an input object conforming to a defined `Model` structure. It asserts the resulting schema matches the expected structure for the handler's argument type.*


### test_optional_model (method, L167-L198, parent: TestOneArgWithModel)

> *Summary: This test verifies that the generated JSON schema correctly represents an optional model input. It asserts the schema structure, ensuring the field accepts either a valid object matching the `Model` definition or `null`.*


### test_optional_embedded_model (method, L200-L223, parent: TestOneArgWithModel)

> *Summary: This test verifies that when an optional embedded model is used in a handler, the generated JSON schema correctly represents it as an `anyOf` union between the defined object structure and `null`. It confirms the schema accurately reflects the possibility of receiving either the structured data or no value.*


### test_nested_resolved_model (method, L225-L255, parent: TestOneArgWithModel)

> *Summary: This test verifies that when resolving references, the generated JSON schema correctly represents a nested model structure. It asserts that the resulting schema accurately reflects the hierarchy defined by `Model` containing an instance of `Model2`.*


### test_embedded_model (method, L257-L270, parent: TestOneArgWithModel)

> *Summary: This test verifies that when embedding a model into a call signature, the generated JSON schema correctly reflects the input structure. It asserts that the resulting schema accurately describes an object with an integer property named "a".*


### test_embedded_resolved_model (method, L272-L295, parent: TestOneArgWithModel)

> *Summary: This test verifies that when resolving references and embedding models, the generated JSON schema correctly represents nested structures. It asserts that a schema derived from a handler expecting a composite model accurately reflects its internal object properties.*


### TestMultiArgs (class, L298-L400)

> *Summary: This test suite verifies the functionality of generating OpenAPI schemas from Python function signatures. It demonstrates how to correctly map arguments, handle default values and types, manage embedded models via references, and resolve those references when explicitly requested.*


### test_base (method, L299-L309, parent: TestMultiArgs)

> *Summary: This test verifies that the generated JSON schema correctly reflects the parameters of a simple two-argument function. It asserts that the resulting schema object matches an expected structure defining properties 'a' and 'b' as required fields within an object type.*


### test_types_and_default (method, L311-L324, parent: TestMultiArgs)

> *Summary: This test verifies that the generated JSON schema correctly reflects function parameters and default values. It takes a Python callable with typed arguments (one required string, one optional integer) and asserts the resulting schema accurately describes these types and defaults.*


### test_ignores_embedded (method, L326-L339, parent: TestMultiArgs)

> *Summary: When generating a schema from a function with embedded arguments, this test asserts that the resulting JSON schema correctly includes all parameters as properties. It verifies that the generated structure matches the expected object format derived from the input handler signature.*


### test_model (method, L341-L371, parent: TestMultiArgs)

> *Summary: This test verifies that the generated OpenAPI schema correctly reflects a function signature where one argument is a Pydantic model. It asserts the structure, including nested object definitions and references to the input model's properties.*


### test_resolved_model (method, L373-L400, parent: TestMultiArgs)

> *Summary: This test verifies that the generated OpenAPI schema correctly represents a function signature where one argument is a Pydantic model. It asserts that the resulting schema accurately reflects the input types, including nested object structures and default values from the model definition.*


### test_depends (function, L403-L448)

> *Summary: This test verifies that `get_schema` correctly resolves complex dependency chains, including nested dependencies and custom class usage. It asserts the resulting OpenAPI schema matches an expected structure derived from a handler function with various input dependencies.*

