# test/beta/config/gemini/test_response_schema_to_api.py

6 function(s): _embedded_data_schema, test_none_returns_empty, test_primitive_type, test_simple_dataclass, test_union_type, test_no_schema_returns_empty. 1 class(es): TestPydanticModelSchemas. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _embedded_data_schema | function |  |
| test_none_returns_empty | function |  |
| test_primitive_type | function |  |
| test_simple_dataclass | function |  |
| TestPydanticModelSchemas | class |  |
| test_union_type | function |  |
| test_no_schema_returns_empty | function |  |

## Chunks

### _embedded_data_schema (function, L16-L28)

> *Summary: Wraps an input dictionary into a specific JSON schema structure where the original data is nested under a `"data"` key. This function generates the schema for responses that are wrapped in `{"data": ...}` format, typically when embedding is enabled.*


### test_none_returns_empty (function, L31-L32)

> *Summary: Verifies that passing `None` as input to the configuration conversion function results in an empty dictionary output. This confirms correct handling of null or missing data during schema translation.*


### test_primitive_type (function, L43-L58)

> *Summary: This test verifies that a `ResponseSchema` initialized with a primitive type correctly transforms into the expected API configuration structure. It asserts that the resulting dictionary contains `"response_mime_type"` as `"application/json"` and a specific JSON schema under `"response_json_schema"`.*


### test_simple_dataclass (function, L61-L80)

> *Summary: This test verifies that a simple dataclass structure is correctly converted into the expected API configuration format. It takes a `ResponseSchema` built from a dataclass and asserts the resulting dictionary contains the correct JSON schema definition for its fields.*


### TestPydanticModelSchemas (class, L83-L119)

> *Summary: This test suite verifies the conversion of Pydantic models into API response configurations. It asserts that simple and constrained data models are correctly translated into JSON schema structures within the resulting configuration dictionary.*


### test_simple_model (method, L84-L102, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a defined Pydantic model, wrapped in a `ResponseSchema`, correctly translates into the expected API configuration structure. It asserts that the output contains `"application/json"` as the MIME type and a corresponding JSON schema describing the input fields (`name` as string, `price` as number).*


### test_model_with_field_constraints (method, L104-L119, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a Pydantic model with field constraints (like minimum and maximum values) is correctly translated into the expected JSON schema structure when processed by `response_proto_to_config`. It asserts the resulting dictionary matches the schema definition, including the constraint properties.*


### test_union_type (function, L122-L140)

> *Summary: This test verifies that a `ResponseSchema` defined with a union type (`int | str`) correctly transforms into the expected API configuration structure. It asserts that the resulting dictionary contains a JSON schema reflecting an `anyOf` constraint for both integer and string types.*


### test_no_schema_returns_empty (function, L143-L153)

> *Summary: When provided a proto object lacking a `json_schema`, the conversion function returns an empty dictionary. This test verifies that no schema results in an empty configuration output.*

