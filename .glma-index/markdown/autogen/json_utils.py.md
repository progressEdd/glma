# autogen/json_utils.py

1 function(s): resolve_json_references.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| resolve_json_references | function |  |

## Chunks

### resolve_json_references (function, L16-L42)

> *Summary: This function takes a JSON schema containing internal references and resolves them by utilizing a `RefResolver` and `Draft7Validator`. It recursively traverses the resolved schema, replacing all `$ref` pointers with their actual content to produce a fully expanded schema dictionary.*

