# autogen/beta/response/prompted.py

1 class(es): PromptedSchema. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PromptedSchema | class |  |

## Chunks

### PromptedSchema (class, L28-L103)

> *Summary: This class wraps a standard response schema to instruct language models to return JSON matching the schema via system prompts, rather than relying on native structured output support. It accepts an inner schema or type and generates a system prompt containing the JSON schema if one exists, while delegating final validation to the wrapped schema's method.*


### __init__ (method, L48-L54, parent: PromptedSchema)

> *Summary: Initializes a response wrapper by accepting an inner `ResponseProto` object and optionally a string template for prompting. It encapsulates the core response data while providing hooks for prompt-based modifications.*


### __init__ (method, L57-L63, parent: PromptedSchema)

> *Summary: Initializes a response object by wrapping an inner type and optionally accepting a string template for prompting. This sets up the structure needed to generate responses based on the provided context and template.*


### __init__ (method, L66-L72, parent: PromptedSchema)

> *Summary: Initializes a response object by storing an inner `ClassInfo` and optionally accepting a string template for prompting. This sets up the structure needed to generate or process responses based on the provided class information.*


### __init__ (method, L74-L95, parent: PromptedSchema)

> *Summary: Initializes a response object by ensuring the input conforms to a defined schema and extracting its name and description. It constructs a system prompt, incorporating the JSON schema as a string if one is present in the inner structure.*


### validate (method, L97-L103, parent: PromptedSchema)

> *Summary: This method delegates the validation process to an inner component, accepting a response string, a context object, and an optional provider. It returns the validated result of that internal call.*

