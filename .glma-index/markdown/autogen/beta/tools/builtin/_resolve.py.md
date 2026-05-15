# autogen/beta/tools/builtin/_resolve.py

1 function(s): resolve_variable.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| resolve_variable | function |  |

## Chunks

### resolve_variable (function, L11-L29)

> *Summary: This function resolves a `Variable` marker by looking up its name in the provided conversation context's variables. If the key is missing from the context, it attempts to return a predefined default value or execute a default factory; otherwise, it raises a `KeyError`.*

