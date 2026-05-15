# test/beta/config/openai/test_response_schema_to_responses_api.py

5 function(s): _embedded_data_schema, test_none_returns_none, test_primitive_type, test_union_type, test_raw_schema_maps_correctly. 4 class(es): TestDataclassSchemas, TestPydanticModelSchemas, TestAdditionalPropertiesFalse, TestDescriptionHandling. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _embedded_data_schema | function |  |
| test_none_returns_none | function |  |
| test_primitive_type | function |  |
| TestDataclassSchemas | class |  |
| TestPydanticModelSchemas | class |  |
| test_union_type | function |  |
| TestAdditionalPropertiesFalse | class |  |
| TestDescriptionHandling | class |  |
| test_raw_schema_maps_correctly | function |  |

## Chunks

### _embedded_data_schema (function, L17-L29)

> *Summary: Constructs a JSON schema that wraps an input dictionary within a top-level `"data"` field. This structure is used to define the expected response format when embedding data, ensuring the output conforms to a specific object shape.*


### test_none_returns_none (function, L32-L33)

> *Summary: Verifies that passing `None` as input to the configuration conversion function results in a `None` output. This confirms expected behavior when no configuration data is provided.*


### test_primitive_type (function, L44-L59)

> *Summary: This test verifies that a `ResponseSchema` initialized with a primitive type correctly serializes to a specific configuration structure. It asserts the resulting dictionary matches an expected format containing JSON schema details for the given name.*


### TestDataclassSchemas (class, L62-L100)

> *Summary: This test suite verifies the serialization of Python dataclass schemas into a specific configuration format. It confirms that simple data structures are correctly translated to JSON schema properties and that custom descriptions on the schema are preserved in the output.*


### test_simple_dataclass (method, L63-L85, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` built from a simple dataclass correctly serializes into the expected JSON schema format. It takes a dataclass definition as input and asserts the resulting dictionary structure matches the OpenAPI specification for object properties.*


### test_dataclass_with_description (method, L87-L100, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly serializes the provided dataclass structure and its associated description. It asserts that calling `response_proto_to_text_config` on this schema yields a dictionary containing the specified description under the "format" key.*


### TestPydanticModelSchemas (class, L103-L143)

> *Summary: This test suite verifies the serialization of Pydantic models into a specific response configuration format. It asserts that simple and constrained data models are correctly transformed into JSON schema representations using `response_proto_to_text_config`.*


### test_simple_model (method, L104-L125, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a `ResponseSchema` built from a simple Pydantic model correctly serializes into the expected JSON structure for API configuration. It takes a schema object and asserts the resulting dictionary matches the predefined OpenAPI-like format, including property types.*


### test_model_with_field_constraints (method, L127-L143, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a response schema correctly translates Python type hints with field constraints (like minimum and maximum values) into the corresponding JSON schema structure. It takes a `ResponseSchema` built from a model containing an annotated integer and asserts the resulting configuration matches the expected constrained format.*


### test_union_type (function, L146-L154)

> *Summary: This test verifies how a union type schema (`int | str`) is serialized into the expected JSON structure. It asserts that the resulting configuration correctly embeds the union within the `data` object of the response proto conversion.*


### TestAdditionalPropertiesFalse (class, L157-L195)

> *Summary: This test suite verifies that the `response_proto_to_text_config` function correctly enforces `additionalProperties: false` on object schemas within a response configuration. It tests this behavior for top-level, nested objects, and confirms it is omitted when dealing with primitive types.*


### test_added_to_top_level_object (method, L160-L170, parent: TestAdditionalPropertiesFalse)

> *Summary: When provided with a `ResponseSchema` wrapping a simple dataclass, this test verifies that the conversion function produces a specific structure indicating the schema is nested under a top-level object. The input schema results in an output dictionary containing `"schema"` and `"additionalProperties": False`.*


### test_added_to_nested_objects (method, L172-L187, parent: TestAdditionalPropertiesFalse)

> *Summary: This test verifies that when a schema containing nested objects is processed, the resulting structure correctly enforces strictness on additional properties within those definitions. It asserts that any defined object schemas in the output's `$defs` section explicitly set `additionalProperties` to `False`.*


### test_not_added_to_primitives_raw (method, L189-L195, parent: TestAdditionalPropertiesFalse)

> *Summary: When converting a `RawSchema` containing only a primitive type, the resulting configuration should not include an `"additionalProperties"` field within its schema definition. This test verifies that simple schemas are correctly processed without unnecessary property constraints being added.*


### TestDescriptionHandling (class, L198-L220)

> *Summary: This test suite verifies the serialization logic for response schemas, ensuring that a schema without a description omits it from the output configuration. It also confirms that when a description is provided in the input `ResponseSchema`, it is correctly included in the resulting text configuration dictionary.*


### test_no_description_omitted (method, L199-L208, parent: TestDescriptionHandling)

> *Summary: This test verifies that when a schema lacks a description field, the resulting configuration output omits the `"description"` key from its format section. It achieves this by passing a simple Pydantic model without any descriptive metadata to the conversion function.*


### test_description_included (method, L210-L220, parent: TestDescriptionHandling)

> *Summary: When provided with a `ResponseSchema` containing a description, this test verifies that the conversion function correctly maps the schema into a dictionary structure including both the name and the associated description. The expected output is a dictionary where the format field contains an object mirroring the input's metadata.*


### test_raw_schema_maps_correctly (function, L223-L240)

> *Summary: This test verifies that a `RawSchema` object is correctly transformed into a structured configuration dictionary. It takes a raw JSON schema definition and asserts the resulting output matches an expected structure containing the original schema, name, and description.*

