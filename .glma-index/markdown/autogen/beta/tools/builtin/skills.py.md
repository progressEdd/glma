# autogen/beta/tools/builtin/skills.py

3 class(es): Skill, SkillsToolSchema, SkillsTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Skill | class |  |
| SkillsToolSchema | class |  |
| SkillsTool | class |  |

## Chunks

### Skill (class, L17-L26)

> *Summary: Represents a reference to an external skill managed by a provider, storing its unique identifier and an optional specific version pin. It allows referencing skills like "pptx" or custom IDs while defaulting to the latest available version if no version is specified.*


### SkillsToolSchema (class, L33-L42)

> *Summary: Defines a schema for representing provider-side capabilities that are passed separately from the main tool definitions. It holds a list of `Skill` objects which describe these inherent abilities.*


### SkillsTool (class, L45-L84)

> *Summary: This class registers a set of provider-side skills, accepting skill identifiers as strings or specific `Skill` objects for version control. It exposes these registered skills via schemas and hooks into the agent's event stream to handle tool calls related to those skills.*


### __init__ (method, L65-L67, parent: SkillsTool)

> *Summary: Initializes the object by accepting a variable number of skill identifiers or `Skill` objects. It converts any string inputs into `Skill` instances and stores them internally, while also setting a fixed tool name.*


### schemas (method, L69-L70, parent: SkillsTool)

> *Summary: Retrieves a list of `SkillsToolSchema` objects by packaging the instance's internal skills. It takes a `Context` object as input and returns a list representing the available tools.*


### register (method, L72-L84, parent: SkillsTool)

> *Summary: This method registers a handler to intercept specific tool call events within the execution stream. It uses an `ExitStack` and `Context` to define a scope where a provided asynchronous function will execute when a particular built-in skill tool is called.*

