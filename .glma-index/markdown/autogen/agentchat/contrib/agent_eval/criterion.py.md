# autogen/agentchat/contrib/agent_eval/criterion.py

1 class(es): Criterion. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Criterion | class |  |

## Chunks

### Criterion (class, L14-L43)

> *Summary: This class models an evaluation criterion, holding a name, description, accepted values, and optional sub-criteria. It provides static methods to serialize a list of these criterion objects into a JSON string or deserialize a JSON string back into a list of `Criterion` instances.*


### parse_json_str (method, L23-L31, parent: Criterion)

> *Summary: Converts a JSON string input into a list of `Criterion` objects. It parses the string using `json.loads()` and instantiates each dictionary element as a `Criterion`.*


### write_json (method, L34-L43, parent: Criterion)

> *Summary: Converts a list of `Criterion` objects into a formatted JSON string. It serializes each object's state using its `model_dump()` method and returns the resulting string with an indentation of 2.*

