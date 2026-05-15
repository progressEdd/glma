# autogen/fast_depends/schema.py

2 function(s): get_schema, _move_pydantic_refs.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_schema | function |  |
| _move_pydantic_refs | function |  |

## Chunks

### get_schema (function, L14-L37)

> *Summary: Generates a JSON schema dictionary from a provided `CallModel` instance and its parameters. It optionally resolves internal references, handles empty parameter sets by setting the type to "null," and can embed the schema if only one property exists.*


### _move_pydantic_refs (function, L40-L66)

> *Summary: Recursively traverses a dictionary structure to resolve Pydantic references (`$ref`). It replaces the current object with the referenced definition found within the provided `refs` map if a `$ref` key is encountered.*

