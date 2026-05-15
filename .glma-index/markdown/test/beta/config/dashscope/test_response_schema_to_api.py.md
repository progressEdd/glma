# test/beta/config/dashscope/test_response_schema_to_api.py

5 function(s): _embedded_data_schema, test_response_proto_to_format_none_returns_none, test_primitive_schemas_primitive_type, test_union_schemas_union_type, test_raw_schema_from_schema_maps_correctly. 3 class(es): TestDataclassSchemas, TestPydanticModelSchemas, TestDescriptionHandling. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _embedded_data_schema | function |  |
| test_response_proto_to_format_none_returns_none | function |  |
| test_primitive_schemas_primitive_type | function |  |
| TestDataclassSchemas | class |  |
| TestPydanticModelSchemas | class |  |
| test_union_schemas_union_type | function |  |
| TestDescriptionHandling | class |  |
| test_raw_schema_from_schema_maps_correctly | function |  |

## Chunks

### _embedded_data_schema (function, L17-L29)

> *Summary: Wraps an input dictionary into a specific JSON schema structure where the provided data is nested under a `"data"` key. This function generates the schema for responses that conform to a single-field object containing the core response payload.*


### test_response_proto_to_format_none_returns_none (function, L32-L33)

> *Summary: Verifies that passing `None` as input to the conversion function results in a `None` output. This confirms the expected behavior for null or empty responses during API data transformation testing.*


### test_primitive_schemas_primitive_type (function, L44-L63)

> *Summary: This test verifies the serialization of a basic `ResponseSchema` into its API format. It takes a Python type, a name, and an expected inner schema dictionary as input to assert that the resulting structure matches the predefined JSON schema representation.*


### TestDataclassSchemas (class, L66-L105)

> *Summary: This test suite verifies the serialization of Python dataclass structures into API response schemas. It confirms that a simple dataclass correctly maps to a JSON schema object, and also validates how custom descriptions are incorporated when creating the schema from a dataclass.*


### test_simple_dataclass (method, L67-L89, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` built from a simple Python dataclass correctly serializes into the expected JSON schema format. It confirms the structure accurately represents the fields and their corresponding types (string, integer) defined in the input class.*


### test_dataclass_with_description (method, L91-L105, parent: TestDataclassSchemas)

> *Summary: This test verifies that a `ResponseSchema` correctly translates a Python dataclass, including its associated description, into the expected API format. It asserts that the resulting structure contains a JSON schema object with the provided custom description.*


### TestPydanticModelSchemas (class, L108-L149)

> *Summary: This test suite verifies the conversion of Pydantic models into a specific API response format. It asserts that simple and constrained data models are correctly transformed into JSON Schema structures using `response_proto_to_format`.*


### test_simple_model (method, L109-L130, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a defined Pydantic model is correctly converted into the expected API response format. It takes a `ResponseSchema` built from an `Item` model and asserts the resulting structure matches a specific JSON schema representation.*


### test_model_with_field_constraints (method, L132-L149, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a Pydantic model with field constraints (like minimum and maximum values) is correctly translated into the expected JSON Schema format. It takes a schema definition containing a bounded integer field as input and asserts the resulting structure matches the specified constraints in the output.*


### test_union_schemas_union_type (function, L152-L173)

> *Summary: This test verifies that a `ResponseSchema` defined with a union type (`int | str`) is correctly transformed into its corresponding API format. It asserts the resulting structure contains a JSON schema specifying an `anyOf` array for integer and string types under the schema definition.*


### TestDescriptionHandling (class, L176-L199)

> *Summary: Verifies how a `ResponseSchema` is converted into an API format, ensuring that the resulting structure correctly omits or includes a description based on whether it was provided in the input schema. It tests two cases: one with no description and another explicitly including a descriptive string.*


### test_no_description_omitted (method, L177-L186, parent: TestDescriptionHandling)

> *Summary: This test verifies that when a Pydantic model lacks a description, the resulting API format omits the `"description"` field from its JSON schema. It achieves this by passing a simple model without any descriptive metadata to the conversion function.*


### test_description_included (method, L188-L199, parent: TestDescriptionHandling)

> *Summary: Verifies that a `ResponseSchema` containing a description is correctly transformed into the expected API format. It takes a schema object and asserts the resulting dictionary includes both the name and the provided description under the JSON schema structure.*


### test_raw_schema_from_schema_maps_correctly (function, L202-L218)

> *Summary: This test verifies that a `RawSchema` object is correctly transformed into a specific API response format. It takes a raw schema definition and asserts the resulting dictionary structure matches the expected output containing nested JSON schema details.*

