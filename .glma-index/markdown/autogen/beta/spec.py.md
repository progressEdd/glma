# autogen/beta/spec.py

2 class(es): ResponseSchemaSpec, AgentSpec. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ResponseSchemaSpec | class |  |
| AgentSpec | class |  |

## Chunks

### ResponseSchemaSpec (class, L22-L36)

> *Summary: This class provides a JSON-serializable specification for defining a response schema. It takes a name, optional description, and a JSON schema dictionary as input, outputting a structured `RawSchema` object via its conversion method.*


### to_response_schema (method, L29-L36, parent: ResponseSchemaSpec)

> *Summary: Converts the internal specification object into a `RawSchema` structure. It packages the stored JSON schema, name, and description into the output proto message.*


### AgentSpec (class, L39-L136)

> *Summary: This class serves as a serializable blueprint for an Agent, capturing only its static configuration like name, prompt, and required tools. It can be instantiated from a live `Agent` instance by stripping dynamic components, or it can reconstruct a full `Agent` object given necessary runtime context such as available tools and middleware.*


### from_agent (method, L56-L80, parent: AgentSpec)

> *Summary: Constructs a specification object from an active agent instance by extracting its name, system prompt, available tool names, and response schema. It intentionally discards non-serializable components like dynamic prompts or middleware during this conversion.*


### to_agent (method, L82-L136, parent: AgentSpec)

> *Summary: Constructs an `Agent` instance from a specification object by resolving named tools against a provided set of available tools. It accepts various optional configurations like middleware, observers, and response schemas to fully initialize the agent's behavior.*

