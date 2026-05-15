# test/beta/config/ollama/test_response_schema_to_api.py

6 function(s): _embedded_data_schema, test_none_returns_none, test_primitive_type, test_simple_dataclass, test_union_type, test_no_schema_returns_none. 1 class(es): TestPydanticModelSchemas. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _embedded_data_schema | function |  |
| test_none_returns_none | function |  |
| test_primitive_type | function |  |
| test_simple_dataclass | function |  |
| TestPydanticModelSchemas | class |  |
| test_union_type | function |  |
| test_no_schema_returns_none | function |  |

## Chunks

### _embedded_data_schema (function, L16-L28)

> *Summary: Wraps an input dictionary into a specific JSON schema structure where the original data is nested under a `"data"` key. This function generates the schema for responses that conform to a single-field object containing the embedded content.*


### test_none_returns_none (function, L31-L32)

> *Summary: Verifies that passing `None` as input to the conversion function results in a `None` output. This confirms correct handling of null or empty data during schema transformation.*


### test_primitive_type (function, L43-L56)

> *Summary: This test verifies that a primitive type schema, when converted to the API format via `response_proto_to_format`, correctly embeds its expected inner JSON schema within a specific structure. It asserts the resulting output matches an `IsPartialDict` containing the embedded data and a fixed "title".*


### test_simple_dataclass (function, L59-L75)

> *Summary: This test verifies that a simple dataclass structure is correctly converted into the expected JSON schema format. It takes a `ResponseSchema` built from a `User` dataclass and asserts the output matches a predefined dictionary structure containing property definitions for name (string) and age (integer).*


### TestPydanticModelSchemas (class, L78-L108)

> *Summary: This test suite verifies the conversion of Pydantic models into OpenAPI-like response schemas. It asserts that simple and constrained models are correctly transformed into dictionaries representing JSON schema properties with appropriate types and constraints (e.g., `minimum`, `maximum`).*


### test_simple_model (method, L79-L94, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a provided `ResponseSchema` based on a simple Pydantic model is correctly converted into the expected JSON schema format. It asserts that the resulting structure accurately reflects the defined properties and their corresponding data types (`string` for name, `number` for price).*


### test_model_with_field_constraints (method, L96-L108, parent: TestPydanticModelSchemas)

> *Summary: This test verifies that a Pydantic model with field constraints (like minimum and maximum values) is correctly translated into the expected JSON schema format. It takes a `ResponseSchema` built from a constrained model and asserts its output matches the structure containing those constraint definitions.*


### test_union_type (function, L111-L126)

> *Summary: This test verifies that a `ResponseSchema` defined with a union type (`int | str`) correctly transforms into the expected API format. It asserts that the resulting structure contains an `anyOf` array listing both `"integer"` and `"string"` types within its embedded data schema.*


### test_no_schema_returns_none (function, L129-L137)

> *Summary: When provided with a proto object lacking any schema information, the conversion function returns `None`. This test verifies that the output is null when no structural definition is present in the input.*

