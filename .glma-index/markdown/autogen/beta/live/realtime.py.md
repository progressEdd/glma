# autogen/beta/live/realtime.py

2 class(es): RealtimeConfig, LiveAgent. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RealtimeConfig | class |  |
| LiveAgent | class |  |

## Chunks

### RealtimeConfig (class, L28-L49)

> *Summary: Defines a protocol for speech-to-text configurations that manage an open, bidirectional session. It accepts a `ConversationContext` and optional parameters like instructions and tools to initiate an asynchronous context manager that handles real-time audio streaming and transcription events.*


### session (method, L42-L49, parent: RealtimeConfig)

> *Summary: This method initializes a session by accepting a conversation context and optional lists of instructions and tools. It returns an asynchronous context manager that manages the lifecycle of the interaction.*


### LiveAgent (class, L52-L327)

> *Summary: This class manages a realtime Speech-to-Text agent session, initializing with configuration, tools, and prompts. Calling the `run()` async context manager starts the session, yielding a `ConversationContext` that allows peers to interact while handling streaming I/O, tool execution, and prompt resolution based on provided inputs.*


### __init__ (method, L67-L124, parent: LiveAgent)

> *Summary: Initializes a real-time agent by setting its name, configuration, and managing various components like tools, middleware, observers, and plugins. It processes input prompts into system or dynamic prompt lists and sets up serialization and tool execution capabilities.*


### hitl_hook (method, L126-L135, parent: LiveAgent)

> *Summary: Wraps a provided `HumanHook` instance by replacing the internal hook if one already exists, issuing a warning upon override. It returns the original input hook after setting up the wrapper.*


### prompt (method, L138-L141, parent: LiveAgent)

> *Summary: This method accepts an optional function and returns a callable that wraps a `PromptHook`. It is designed to modify or augment the behavior of a hook during prompting.*


### prompt (method, L144-L147, parent: LiveAgent)

> *Summary: This method takes a `PromptHook` object as input and returns a modified `PromptHook`. Its purpose is to process or adjust the hook based on its current state.*


### prompt (method, L149-L159, parent: LiveAgent)

> *Summary: This method returns a decorator or the original hook, depending on whether an input function is provided. If a function is given, it wraps that function to dynamically append its prompt hook to the instance's internal list before returning the wrapped version.*


### tool (method, L162-L171, parent: LiveAgent)

> *Summary: Creates a `Tool` object by wrapping a given callable function. It accepts optional metadata like name, description, and schema, and allows configuration for synchronous execution or middleware chaining.*


### tool (method, L174-L183, parent: LiveAgent)

> *Summary: This method creates a `Tool` object from provided parameters like a function reference, name, description, and schema. It configures the tool's execution behavior via options such as thread synchronization and middleware application.*


### tool (method, L185-L210, parent: LiveAgent)

> *Summary: This method acts as a factory for creating and registering tools. If provided with a callable `function`, it immediately wraps and registers that function as a tool; otherwise, it returns a wrapper function that accepts a callable to create and register the tool upon invocation.*


### add_tool (method, L212-L214, parent: LiveAgent)

> *Summary: Registers a callable or existing `Tool` object with the agent's internal tool list after ensuring it conforms to the expected format using the dependency provider. It returns the instance itself for method chaining.*


### add_middleware (method, L216-L219, parent: LiveAgent)

> *Summary: Appends a provided `MiddlewareFactory` instance to the agent's internal middleware list, ensuring it acts as the innermost wrapper in the processing chain and returns the current agent object for chaining.*


### insert_middleware (method, L221-L224, parent: LiveAgent)

> *Summary: This method prepends a new `MiddlewareFactory` instance to the agent's existing middleware chain by inserting it at index 0. It then returns the modified agent object for chaining operations.*


### add_observer (method, L226-L228, parent: LiveAgent)

> *Summary: Registers a provided `Observer` object to the instance's internal list of observers before execution begins. This allows the system to notify this observer during its operation.*


### run (method, L231-L320, parent: LiveAgent)

> *Summary: Executes the core logic of a real-time agent session by setting up dependencies, tools, and middleware based on provided inputs. It yields a `ConversationContext` asynchronously, managing observer lifecycle events around the main execution flow within a configured session.*


### _resolve_instructions (method, L322-L327, parent: LiveAgent)

> *Summary: This method constructs a complete set of instructions by starting with the system prompt and sequentially appending dynamic content generated by registered hooks based on the provided conversation context. It returns this aggregated list of strings to be used as input for model requests.*

