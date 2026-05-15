# test/beta/config/anthropic/test_response_schema_to_api.py

4 function(s): _embedded_data_schema, test_response_proto_to_output_config_none_returns_none, test_primitive_schemas_primitive_type, test_no_json_schema_returns_none. 6 class(es): TestDataclassSchemas, TestPydanticModelSchemas, TestUnionSchemas, TestAdditionalPropertiesFalse, TestDescriptionHandling, TestRawSchema. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _embedded_data_schema | function |  |
| test_response_proto_to_output_config_none_returns_none | function |  |
| test_primitive_schemas_primitive_type | function |  |
| TestDataclassSchemas | class |  |
| TestPydanticModelSchemas | class |  |
| TestUnionSchemas | class |  |
| TestAdditionalPropertiesFalse | class |  |
| TestDescriptionHandling | class |  |
| TestRawSchema | class |  |
| test_no_json_schema_returns_none | function |  |

## Chunks

### _embedded_data_schema (function, L17-L29)

> *Summary: Wraps an input dictionary into a specific JSON schema structure where the original content is nested under a `"data"` key. This function generates the schema for responses that conform to a single-field object containing the embedded data.*


### test_response_proto_to_output_config_none_returns_none (function, L32-L33)

> *Summary: Verifies that passing `None` as input to the conversion function results in a `None` output. This test ensures graceful handling of null inputs during schema transformation.*


### test_primitive_schemas_primitive_type (function, L44-L61)

> *Summary: This test verifies that a `ResponseSchema` object, initialized with a primitive type and name, correctly transforms into an output configuration dictionary. It asserts the resulting structure matches a predefined format containing a JSON schema derived from the input inner schema.*


### TestDataclassSchemas (class, L64-L102)

> *Summary: This test suite verifies the conversion of Python dataclass schemas into API configuration formats. It asserts that a simple dataclass correctly maps to a JSON schema structure, while also checking how descriptions are handled during this transformation.*


### test_simple_dataclass (method, L65-L87, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` built from a simple Python dataclass correctly generates the expected JSON schema structure. It takes a dataclass definition as input and asserts the resulting configuration matches the standard OpenAPI/JSON Schema representation for that data structure.*


### test_dataclass_with_description (method, L89-L102, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` constructed from a dataclass with a description correctly generates an output configuration. It asserts the resulting structure matches a specific dictionary format indicating JSON schema usage.*


### TestPydanticModelSchemas (class, L105-L146)

> *Summary: This test suite verifies the conversion of Pydantic models into API response configuration schemas. It asserts that simple and constrained data models are correctly translated into JSON Schema format using a provided utility function.*


### test_simple_model (method, L106-L127, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a provided `ResponseSchema` based on a simple Pydantic model correctly transforms into the expected API configuration structure. It asserts that the output contains a JSON schema definition matching the input model's fields and types.*


### test_model_with_field_constraints (method, L129-L146, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly translates Python model constraints (like minimum and maximum values) into the corresponding JSON Schema format. It takes a Pydantic model with field bounds as input and asserts the resulting configuration matches the expected schema structure.*


### TestUnionSchemas (class, L149-L167)

> *Summary: This test verifies how `ResponseSchema` objects representing union types (`int | str`) and tuples of types (`(int, float)`) are converted into a specific output configuration structure. It asserts that both schema variations result in an output dictionary containing a nested object with `"type": "object"` and `"additionalProperties": False`.*


### test_union_type (method, L150-L158, parent: TestUnionSchemas)

> *Summary: This test verifies how a union type schema (`int | str`) is transformed by the `response_proto_to_output_config` function. It asserts that the resulting configuration correctly embeds the union within an object structure, specifically showing `"type": "object"` and disabling additional properties.*


### test_tuple_of_types (method, L160-L167, parent: TestUnionSchemas)

> *Summary: When provided with a `ResponseSchema` containing a tuple of types, this test verifies that the conversion function produces an output configuration representing an object schema with no additional properties. The input is a schema defined with multiple primitive types, and the expected output confirms its structure as a partial dictionary representation of a JSON object type.*


### TestAdditionalPropertiesFalse (class, L170-L217)

> *Summary: Verifies that the `response_proto_to_output_config` conversion correctly enforces `"additionalProperties": false` on object schemas when transforming Anthropic response protos. It tests this behavior for top-level, nested objects, and confirms it is omitted for raw primitive types while being added to embedded primitives wrapped as objects.*


### test_added_to_top_level_object (method, L173-L183, parent: TestAdditionalPropertiesFalse)

> *Summary: This test verifies that a schema derived from a simple dataclass is correctly transformed into an output configuration structure. It asserts the resulting dictionary matches a specific expected format, ensuring properties are nested as anticipated.*


### test_added_to_nested_objects (method, L185-L200, parent: TestAdditionalPropertiesFalse)

> *Summary: This test verifies that when a Pydantic model containing nested objects is converted to an API response schema, the resulting definition correctly enforces strictness by setting `additionalProperties` to `False` within any defined object schemas. It uses nested `BaseModel` classes as input to validate this structural constraint in the output configuration.*


### test_not_added_to_primitives_raw (method, L202-L208, parent: TestAdditionalPropertiesFalse)

> *Summary: When converting a `RawSchema` containing only a primitive type, the resulting configuration should omit the `"additionalProperties"` field within its schema definition. This test verifies that simple schemas are not unnecessarily augmented during the conversion process.*


### test_embedded_primitive_gets_additional_properties (method, L210-L217, parent: TestAdditionalPropertiesFalse)

> *Summary: When converting a primitive schema into the output configuration, this test verifies that an embedded primitive results in an object wrapper where `additionalProperties` is explicitly set to `False`. It confirms the structure of the resulting dictionary representation.*


### TestDescriptionHandling (class, L220-L244)

> *Summary: Verifies how a `ResponseSchema` object is transformed into an API configuration for Anthropic. It confirms that when the input schema lacks or has metadata like names and descriptions, the resulting output structure correctly omits these fields as per the Anthropic API specification.*


### test_no_description_not_in_output (method, L221-L233, parent: TestDescriptionHandling)

> *Summary: Verifies that the schema conversion process correctly handles a `ResponseSchema` lacking a description field. It asserts that the resulting output configuration only contains the expected JSON schema format information, ignoring the missing description.*


### test_description_not_passed_to_api (method, L235-L244, parent: TestDescriptionHandling)

> *Summary: When converting a `ResponseSchema` object to the Anthropic output configuration format, this test verifies that metadata like `name` and `description` are omitted from the resulting structure. It asserts that the generated dictionary does not contain these specific keys within its "format" section.*


### TestRawSchema (class, L247-L277)

> *Summary: This test verifies that a `RawSchema` object, constructed with JSON schema definitions, is correctly transformed into an output configuration dictionary. It asserts the resulting structure matches expected formats for both complex and simple schemas.*


### test_from_schema_maps_correctly (method, L248-L262, parent: TestRawSchema)

> *Summary: This test verifies that a `RawSchema` input is correctly transformed into an output configuration dictionary. It asserts the resulting structure matches the expected format containing the original JSON schema under a `"schema"` key.*


### test_from_schema_no_description (method, L264-L277, parent: TestRawSchema)

> *Summary: This test verifies that a `RawSchema` lacking a description correctly transforms into an output configuration. It asserts the resulting structure contains a JSON schema definition for a simple string type.*


### test_no_json_schema_returns_none (function, L280-L288)

> *Summary: When provided with a proto object lacking a JSON schema, the conversion function returns `None`. This test verifies that the output configuration defaults to null when schema information is absent.*

