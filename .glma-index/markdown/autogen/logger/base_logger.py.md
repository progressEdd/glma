# autogen/logger/base_logger.py

1 class(es): BaseLogger. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BaseLogger | class |  |

## Chunks

### BaseLogger (class, L26-L129)

> *Summary: Defines an abstract interface for logging system activities across various components like agents, wrappers, and API calls. It requires implementations for starting/stopping sessions, logging specific events (e.g., chat completions, agent creation), and providing database connections.*


### start (method, L28-L34, parent: BaseLogger)

> *Summary: Establishes a connection to the logging database and initiates recording, returning a unique string identifier for the active logging session.*


### log_chat_completion (method, L37-L66, parent: BaseLogger)

> *Summary: Records details of an AI chat completion event into the database. It accepts various identifiers, the input request and resulting response, caching status, associated cost, and timing information as inputs to perform its logging action.*


### log_new_agent (method, L69-L76, parent: BaseLogger)

> *Summary: Records the creation of a new conversational agent, accepting the agent instance and its initialization arguments as input. This method performs logging actions related to the agent's instantiation.*


### log_event (method, L79-L87, parent: BaseLogger)

> *Summary: Records an agent-specific event by accepting a source identifier, an event name, and arbitrary keyword arguments containing event details. It processes these inputs internally without returning a value.*


### log_new_wrapper (method, L90-L97, parent: BaseLogger)

> *Summary: Logs the creation of an `OpenAIWrapper` instance, accepting the wrapper object and a dictionary containing its initialization arguments as input. This method serves to record when a new wrapper is instantiated within the system.*


### log_new_client (method, L100-L108, parent: BaseLogger)

> *Summary: Records the instantiation of a new `OpenAIWrapper` instance. It accepts the underlying OpenAI client, the wrapper object itself, and the initialization arguments as input.*


### log_function_use (method, L111-L119, parent: BaseLogger)

> *Summary: Records when a registered function, potentially a tool, is invoked. It takes the event source, function details, input arguments, and the resulting output as inputs, producing no direct return value.*


### stop (method, L122-L124, parent: BaseLogger)

> *Summary: Closes the active connection to the logging database and halts all ongoing logging operations.*


### get_connection (method, L127-L129, parent: BaseLogger)

> *Summary: Retrieves an active connection object for the SQLite logging database. It returns the established `sqlite3.Connection` instance or `None` if one cannot be obtained.*

