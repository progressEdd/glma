# test/beta/response/test_schema.py

8 class(es): TestEmbeddedTypes, TestDataclassSchemas, TestPydanticModelSchemas, TestUnionSchemas, TestNameDescription, TestEnsureSchema, TestRawSchema, TestValidation. 39 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestEmbeddedTypes | class |  |
| TestDataclassSchemas | class |  |
| TestPydanticModelSchemas | class |  |
| TestUnionSchemas | class |  |
| TestNameDescription | class |  |
| TestEnsureSchema | class |  |
| TestRawSchema | class |  |
| TestValidation | class |  |

## Chunks

### TestEmbeddedTypes (class, L20-L148)

> *Summary: This code chunk contains unit tests verifying how different Python types are converted into JSON schemas by a `ResponseSchema` object. It asserts that primitive and container types result in either embedded or non-embedded structures, depending on the type's nature (e.g., basic primitives vs. custom classes).*


### test_primitive_types_not_embedded (method, L54-L61, parent: TestEmbeddedTypes)

> *Summary: Verifies that when a primitive type is used without embedding, the resulting `ResponseSchema` correctly omits embedded type information and matches the provided JSON schema. It takes a class info object and a dictionary representing the schema as input.*


### test_primitive_types_embedded (method, L96-L113, parent: TestEmbeddedTypes)

> *Summary: This test verifies that when embedding primitive types within a response schema, the resulting JSON schema correctly wraps the provided `schema` under a top-level `"data"` property. It asserts the structure of this embedded object to ensure proper serialization for responses containing only one field.*


### test_str_has_no_schema (method, L115-L118, parent: TestEmbeddedTypes)

> *Summary: Verifies that a `ResponseSchema` initialized with the Python `str` type correctly indicates it has no embedded schema while its JSON schema remains unset. This test confirms the expected behavior for primitive types lacking complex structure.*


### test_dict_not_embedded (method, L120-L126, parent: TestEmbeddedTypes)

> *Summary: Verifies that a `ResponseSchema` initialized with `dict[str, int]` correctly sets its embedded type to false and generates a JSON schema allowing any string key mapped to an integer value.*


### test_dataclass_not_embedded (method, L128-L134, parent: TestEmbeddedTypes)

> *Summary: This test verifies that when a dataclass is passed to `ResponseSchema`, the resulting schema does not incorrectly embed the type. It instantiates a simple dataclass and asserts that the internal `_embedded_type` attribute remains unset on the created schema object.*


### test_pydantic_model_not_embedded (method, L136-L141, parent: TestEmbeddedTypes)

> *Summary: This test verifies that a `ResponseSchema` instance, when initialized with a Pydantic model, does not automatically embed the provided type. It asserts that the internal `_embedded_type` attribute remains unset after instantiation.*


### test_typed_dict_not_embedded (method, L143-L148, parent: TestEmbeddedTypes)

> *Summary: Verifies that a `ResponseSchema` initialized with a `TypedDict` does not automatically embed the type. It confirms that the internal `_embedded_type` attribute remains unset when provided with a simple typed dictionary structure.*


### TestDataclassSchemas (class, L151-L215)

> *Summary: This test suite verifies the `ResponseSchema` functionality by instantiating it with various Python dataclasses. It asserts that the resulting schema correctly captures class names, docstrings, JSON structure (including properties and required fields), default values, and nested object references.*


### test_simple_dataclass (method, L152-L170, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly introspects a simple dataclass. It asserts that the schema accurately reflects the class name, docstring, and generates the corresponding JSON Schema structure for its fields.*


### test_dataclass_with_docstring (method, L172-L182, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly extracts the name and docstring description from a dataclass definition. It instantiates the schema using a simple dataclass containing an integer field to confirm metadata extraction works as expected.*


### test_dataclass_with_defaults (method, L184-L196, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly infers the JSON schema from a dataclass containing default values. It asserts that the resulting schema accurately reflects which fields are required and specifies the default value for optional fields like `retries`.*


### test_nested_dataclass (method, L198-L215, parent: TestDataclassSchemas)

> *Summary: This test verifies that a schema generated from a nested dataclass correctly represents the structure in JSON Schema format. It constructs `Person` containing an `Address` and asserts the resulting schema includes definitions for both types and references the nested type correctly.*


### TestPydanticModelSchemas (class, L218-L308)

> *Summary: This test suite verifies the `ResponseSchema`'s ability to correctly generate JSON schemas from various Pydantic models. It tests scenarios including simple fields, field descriptions, docstrings, nested models, enums, and annotated constraints.*


### test_simple_model (method, L219-L234, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly generates a JSON schema from a Pydantic model. It asserts the resulting schema accurately reflects the input model's fields, types, and required status.*


### test_model_with_field_descriptions (method, L236-L248, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly generates JSON schema properties, including the descriptions provided via `Field()` annotations on Pydantic models. It asserts that the resulting schema accurately reflects these field-level metadata descriptions for both string and annotated integer fields.*


### test_model_with_docstring (method, L250-L258, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly captures the docstring from an embedded Pydantic model. It instantiates the schema with a custom model and asserts that its description matches the model's documentation string.*


### test_model_with_nested_model (method, L260-L274, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly generates JSON Schema when provided with a model containing nested structures. It asserts the schema's name and checks the structure of its `$defs`, ensuring the nested `Coord` model is properly defined within the output.*


### test_model_with_enum_field (method, L276-L296, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a Pydantic model containing an `Enum` field correctly generates a JSON schema. It asserts the resulting schema includes the enum values under `$defs` for type validation.*


### test_model_with_annotated_constraints (method, L298-L308, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a Pydantic model incorporating `Annotated` constraints correctly generates the corresponding JSON schema. It asserts that the generated schema includes `"minimum"` and `"maximum"` keywords reflecting the defined bounds on an integer field.*


### TestUnionSchemas (class, L311-L350)

> *Summary: This test suite verifies the JSON Schema generation for union types, both using Python type hints and dataclass structures. It asserts that a `ResponseSchema` correctly translates unions into an `"anyOf"` structure or defines component schemas when dealing with custom classes.*


### test_union_schema (method, L327-L331, parent: TestUnionSchemas)

> *Summary: This test verifies that a `ResponseSchema` initialized for a union type correctly sets its JSON schema to contain an `anyOf` array matching the provided list of types. It asserts both the schema's name and the structure of its underlying JSON representation.*


### test_union_with_dataclass (method, L333-L350, parent: TestUnionSchemas)

> *Summary: This test verifies the JSON schema generation for a union type defined using dataclasses. It asserts that the resulting schema correctly defines the named union members, "Error" and "Success," within its definitions section.*


### TestNameDescription (class, L353-L404)

> *Summary: This test suite verifies how a `ResponseSchema` constructs metadata by prioritizing explicit names and descriptions over class titles or docstrings when initializing with various inputs. It also confirms that certain metadata fields are correctly omitted from the final generated JSON schema.*


### test_explicit_name_overrides_title (method, L354-L360, parent: TestNameDescription)

> *Summary: This test verifies that an explicitly provided `name` overrides the default title when initializing a `ResponseSchema`. It asserts that the resulting schema's `name` attribute matches the custom string passed during instantiation.*


### test_name_from_class_title (method, L362-L368, parent: TestNameDescription)

> *Summary: This method verifies that an instance of `ResponseSchema`, when initialized with a class inheriting from `BaseModel`, correctly extracts the class name as its `name` attribute. It confirms the schema accurately reflects the input model's identity.*


### test_fallback_name (method, L370-L374, parent: TestNameDescription)

> *Summary: When initialized with a primitive type like `int`, the response schema defaults its name to `"ResponseSchema"` because the provided type lacks a specific title attribute. This test verifies that the fallback mechanism correctly assigns the default name in such cases.*


### test_explicit_description (method, L376-L382, parent: TestNameDescription)

> *Summary: Verifies that a `ResponseSchema` correctly stores and exposes an explicit string description provided during its initialization using a sample Pydantic model. The test confirms the stored description matches the input value.*


### test_schema_description_overrides_docstring (method, L384-L393, parent: TestNameDescription)

> *Summary: When initializing a `ResponseSchema` with a model and an explicit description, the provided string overrides any docstring present on the underlying Pydantic model. This test verifies that the custom description takes precedence in the resulting schema object.*


### test_metadata_popped_from_schema (method, L395-L404, parent: TestNameDescription)

> *Summary: This test verifies that metadata fields like "title" and "description" are excluded from the generated JSON schema when initializing a `ResponseSchema` with a Pydantic model. It asserts the absence of these specific keys in the resulting schema dictionary.*


### TestEnsureSchema (class, L407-L451)

> *Summary: This test suite verifies the `ensure_schema` method of a response schema utility. It confirms that the method correctly handles `None`, returns existing instances unchanged, and wraps primitive or union types into a structured `ResponseSchema` with appropriate JSON schema definitions.*


### test_none_returns_none (method, L408-L409, parent: TestEnsureSchema)

> *Summary: Verifies that passing `None` to the schema ensuring function results in `None`. This confirms the expected behavior for null input within the response schema validation logic.*


### test_response_proto_returned_as_is (method, L411-L416, parent: TestEnsureSchema)

> *Summary: Verifies that the `ensure_schema` method returns the exact same schema object when it is already in the correct format. It takes an existing `ResponseSchema` instance as input and asserts identity against the returned value.*


### test_type_wrapped_in_response_schema (method, L418-L432, parent: TestEnsureSchema)

> *Summary: This test verifies that wrapping a basic Python type (`int`) within `ResponseSchema.ensure_schema` correctly generates a JSON schema representing an object containing a single integer field named "data". It asserts the resulting structure matches the expected schema definition for this wrapper pattern.*


### test_union_type_wrapped (method, L434-L451, parent: TestEnsureSchema)

> *Summary: This test verifies that wrapping a union type (`int | str`) within `ResponseSchema.ensure_schema` correctly generates a JSON schema object. The resulting schema defines an object with a required "data" field whose value must conform to either an integer or a string.*


### TestRawSchema (class, L454-L483)

> *Summary: This test class verifies the functionality of `ResponseSchema` by asserting correct object creation from JSON schemas with and without descriptions. It also tests asynchronous validation, ensuring that a string input is returned while emitting a specific runtime warning when schema validation fails.*


### test_creation (method, L455-L465, parent: TestRawSchema)

> *Summary: This test verifies that creating a `ResponseSchema` from a provided JSON schema dictionary correctly instantiates a `RawSchema`. It asserts that the resulting object holds the correct name, description, and original schema structure.*


### test_creation_without_description (method, L467-L470, parent: TestRawSchema)

> *Summary: Verifies that when creating a `ResponseSchema` from a schema lacking a description, the resulting object's `description` attribute is correctly set to `None`. It takes a minimal JSON schema as input and asserts the absence of a description on the created instance.*


### test_validate_returns_raw_string_with_warning (method, L473-L483, parent: TestRawSchema)

> *Summary: This test verifies that validating a string schema with an input results in the original raw string being returned while simultaneously issuing a `RuntimeWarning`. It asserts that exactly one warning is captured containing specific error text.*


### TestValidation (class, L487-L553)

> *Summary: This test suite verifies the `ResponseSchema`'s validation logic across various data types and structures. It tests primitive, non-embedded primitives, unions (including embedded/non-embedded cases), dataclasses, Pydantic models, and ensures exceptions are raised for invalid JSON input.*


### test_validate_primitive (method, L496-L499, parent: TestValidation)

> *Summary: This test method validates a primitive JSON input against a specified data type within a `ResponseSchema`. It takes the target type, the raw JSON string, and an expected output object as inputs, asserting that the validation process yields the correct result.*


### test_validate_not_embedded_primitive (method, L509-L512, parent: TestValidation)

> *Summary: This test verifies that a primitive type, when explicitly configured not to be embedded in the response schema, validates correctly against provided JSON input. It asserts that the validation output matches the expected structure for the given type and data.*


### test_validate_union (method, L514-L518, parent: TestValidation)

> *Summary: This test verifies that a union schema accepting either an integer or a string correctly validates and returns the corresponding value from input JSON data. It asserts successful parsing for both numeric and string inputs.*


### test_validate_not_embedded_union (method, L520-L524, parent: TestValidation)

> *Summary: This test verifies that a union schema configured to prevent embedding correctly parses input strings into their respective types. It asserts successful validation and type coercion for both integer and string inputs against the defined `int | str` union.*


### test_validate_dataclass (method, L526-L536, parent: TestValidation)

> *Summary: This test verifies that a `ResponseSchema` correctly validates JSON input against a defined dataclass structure. It takes a JSON string containing integer coordinates and asserts the output matches an instantiated `Point` object.*


### test_validate_pydantic_model (method, L538-L547, parent: TestValidation)

> *Summary: This test verifies that a `ResponseSchema` correctly validates and parses a JSON string against a defined Pydantic model. It takes a JSON input string and asserts the output matches an instantiated version of the expected data model.*


### test_validate_invalid_json_raises (method, L549-L553, parent: TestValidation)

> *Summary: This test verifies that attempting to validate an invalid JSON string against the `ResponseSchema` raises an exception. It uses a schema expecting an integer and passes a non-numeric string as input to trigger the expected failure.*

