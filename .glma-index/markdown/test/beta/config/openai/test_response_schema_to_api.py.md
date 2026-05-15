# test/beta/config/openai/test_response_schema_to_api.py

3 function(s): _embedded_data_schema, test_none_returns_none, test_primitive_type. 5 class(es): TestDataclassSchemas, TestPydanticModelSchemas, TestUnionSchemas, TestDescriptionHandling, TestRawSchema. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _embedded_data_schema | function |  |
| test_none_returns_none | function |  |
| test_primitive_type | function |  |
| TestDataclassSchemas | class |  |
| TestPydanticModelSchemas | class |  |
| TestUnionSchemas | class |  |
| TestDescriptionHandling | class |  |
| TestRawSchema | class |  |

## Chunks

### _embedded_data_schema (function, L17-L29)

> *Summary: Constructs a JSON schema that wraps an input dictionary within a top-level `"data"` field. This structure is designed to represent API responses where the core data payload is nested under this specific key.*


### test_none_returns_none (function, L32-L33)

> *Summary: Verifies that passing `None` as input to the conversion function results in a `None` output. This confirms correct handling of null or empty inputs during schema generation from protobufs.*


### test_primitive_type (function, L44-L66)

> *Summary: This test verifies that a basic `ResponseSchema` object correctly serializes into the expected API response structure. It takes a Python type, name, and an inner schema dictionary as input to assert the resulting JSON schema matches predefined expectations.*


### TestDataclassSchemas (class, L69-L108)

> *Summary: This test suite verifies the conversion of Python dataclass structures into API response schemas. It asserts that simple and descriptive dataclasses are correctly transformed into their corresponding JSON schema representations via a provided utility function.*


### test_simple_dataclass (method, L70-L92, parent: TestDataclassSchemas)

> *Summary: This test verifies that a simple dataclass is correctly converted into a structured API response schema. It takes a `ResponseSchema` initialized with the dataclass and asserts the resulting dictionary matches the expected JSON Schema representation for object properties.*


### test_dataclass_with_description (method, L94-L108, parent: TestDataclassSchemas)

> *Summary: This test verifies that a dataclass, when wrapped with a `ResponseSchema` and provided a description, correctly generates a JSON schema structure. It asserts the output matches a dictionary containing `"type": "json_schema"` and a nested schema object reflecting the custom description.*


### TestPydanticModelSchemas (class, L111-L152)

> *Summary: This test suite verifies the conversion of Pydantic models into a specific API response schema format. It asserts that simple and constrained data models are correctly transformed into JSON Schema representations, including handling field constraints like minimum and maximum values.*


### test_simple_model (method, L112-L133, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a defined Pydantic model, wrapped in a `ResponseSchema`, correctly transforms into a specific JSON schema structure. It asserts the output matches an expected dictionary format containing object properties for string and number types.*


### test_model_with_field_constraints (method, L135-L152, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a Pydantic model with field constraints (like minimum and maximum values) is correctly translated into its corresponding JSON schema representation. It asserts the resulting structure matches the expected dictionary containing the `minimum` and `maximum` properties for the constrained field.*


### TestUnionSchemas (class, L155-L201)

> *Summary: This test suite verifies the serialization of Python union and tuple types within a `ResponseSchema` object into a specific JSON schema format. It confirms that unions map to `anyOf` with corresponding primitive types, while tuples also result in an `anyOf` structure.*


### test_union_type (method, L156-L177, parent: TestUnionSchemas)

> *Summary: This test verifies that a `ResponseSchema` defined with a union type (`int | str`) correctly transforms into the expected API schema structure. It asserts that the resulting dictionary contains a JSON Schema object specifying an `anyOf` array containing both "integer" and "string" types.*


### test_tuple_of_types (method, L179-L201, parent: TestUnionSchemas)

> *Summary: This test verifies that a `ResponseSchema` initialized with a tuple of types correctly transforms into a specific API response structure. It asserts the resulting dictionary matches an expected schema containing a JSON Schema definition for handling both integer and number types.*


### TestDescriptionHandling (class, L204-L240)

> *Summary: These tests verify the `response_proto_to_schema` conversion logic, ensuring that a provided schema correctly omits the description if none is given, includes it when present, and uses the specified name for the resulting JSON schema structure. The function takes a `ResponseSchema` object as input and returns a dictionary containing the generated JSON schema representation.*


### test_no_description_omitted (method, L205-L214, parent: TestDescriptionHandling)

> *Summary: This test verifies that when a Pydantic model lacks a description, the resulting API schema omits the `description` field. It takes a simple model and asserts the absence of this key after conversion via `response_proto_to_schema`.*


### test_description_included (method, L216-L227, parent: TestDescriptionHandling)

> *Summary: This test verifies that a `ResponseSchema` object, when converted via `response_proto_to_schema`, correctly produces a dictionary containing the schema type and an embedded JSON schema structure. It confirms that the provided name and description from the input schema are accurately reflected in the output.*


### test_explicit_name_used (method, L229-L240, parent: TestDescriptionHandling)

> *Summary: This test verifies that when a custom name is provided to a `ResponseSchema`, the resulting API schema correctly includes this explicit name within its JSON schema structure. It takes a model and an explicit name as input, asserting the output matches the expected dictionary format containing the specified name.*


### TestRawSchema (class, L243-L278)

> *Summary: This test verifies that a `RawSchema` object is correctly transformed into a structured API response format using `response_proto_to_schema`. It asserts the resulting dictionary structure matches expected outputs for schemas with and without descriptions.*


### test_from_schema_maps_correctly (method, L244-L261, parent: TestRawSchema)

> *Summary: This test verifies that a `RawSchema` object is correctly transformed into a structured API response format. It takes a raw schema definition and asserts the resulting dictionary matches the expected structure containing nested JSON schema details.*


### test_from_schema_no_description (method, L263-L278, parent: TestRawSchema)

> *Summary: This test verifies that a `RawSchema` containing only a basic string type is correctly transformed into the expected API response schema structure. It asserts that the output wraps the input's JSON schema within a specific container format.*

