# test/agentchat/contrib/agent_eval/test_criterion.py

3 function(s): test_parse_json_str, test_write_json, test_write_parse_compatibility.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_parse_json_str | function |  |
| test_write_json | function |  |
| test_write_parse_compatibility | function |  |

## Chunks

### test_parse_json_str (function, L12-L20)

> *Summary: This test verifies that a JSON string read from a sample file can be successfully parsed into a list of `Criterion` objects. It asserts that the resulting structure contains six criteria, and specifically checks the name and description of the first criterion.*


### test_write_json (function, L23-L49)

> *Summary: This test verifies that a list of `Criterion` objects is correctly serialized into a JSON string format. It takes two sample criteria instances as input and asserts the resulting output matches a predefined, structured JSON representation.*


### test_write_parse_compatibility (function, L52-L65)

> *Summary: Verifies that the JSON serialization and deserialization of `Criterion` objects are compatible. It takes a list of `Criterion` instances, converts them to a JSON string, and then parses that string back into a list of `Criterion` objects for structural validation.*

