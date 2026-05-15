# autogen/agentchat/group/context_str.py

1 class(es): ContextStr. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContextStr | class |  |

## Chunks

### ContextStr (class, L13-L39)

> *Summary: Represents a string template that requires dynamic variable substitution. It accepts a dictionary of context variables and returns the fully formatted string by replacing placeholders like `{var}` within its internal `template` attribute.*


### format (method, L22-L36, parent: ContextStr)

> *Summary: This method takes a `ContextVariables` object and substitutes its values into the instance's template string. It returns the resulting formatted string if context is present, or the original template otherwise.*


### __str__ (method, L38-L39, parent: ContextStr)

> *Summary: Provides a string representation of the object by returning its internal template prefixed with "ContextStr, unformatted: ". This is used for debugging or logging purposes.*

