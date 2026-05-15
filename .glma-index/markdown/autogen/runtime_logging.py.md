# autogen/runtime_logging.py

10 function(s): start, log_chat_completion, log_new_agent, log_event, log_function_use, log_new_wrapper, log_new_client, stop, get_connection, logging_enabled.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| start | function |  |
| log_chat_completion | function |  |
| log_new_agent | function |  |
| log_event | function |  |
| log_function_use | function |  |
| log_new_wrapper | function |  |
| log_new_client | function |  |
| stop | function |  |
| get_connection | function |  |
| logging_enabled | function |  |

## Chunks

### start (function, L41-L66)

> *Summary: Initializes runtime logging by either using a provided logger or creating one based on the specified type and configuration. It returns a unique session ID upon successful startup, setting a global flag indicating that logging is active.*


### log_chat_completion (function, L69-L86)

> *Summary: This function records the details of a chat completion event by passing various metadata—including IDs, agent information, input/output payloads, caching status, and cost—to a configured logger. It ensures logging only occurs if an `autogen` logger instance is available.*


### log_new_agent (function, L89-L94)

> *Summary: This function logs the initialization of a new agent by passing the `ConversableAgent` instance and its initial arguments to an external logger if it has been configured. It includes a safety check to prevent errors if the global autogen logger is not available.*


### log_event (function, L97-L102)

> *Summary: This function acts as a wrapper to record events using an external logger instance. It accepts a source identifier and an event name, forwarding all provided keyword arguments to the underlying `autogen_logger` if it has been initialized.*


### log_function_use (function, L105-L110)

> *Summary: This utility records when an agent invokes a specific function, capturing the agent identifier, the function object, its input arguments, and the resulting return value. It ensures logging only occurs if the global `autogen_logger` has been initialized.*


### log_new_wrapper (function, L113-L118)

> *Summary: This function acts as a safety wrapper that checks for the existence of an `autogen` logger before passing an `OpenAIWrapper` and its initialization arguments to it. If the logger is missing, it logs an error instead of proceeding with the logging operation.*


### log_new_client (function, L121-L142)

> *Summary: This function logs the initialization of a new client instance by passing the client object, its associated wrapper, and initial arguments to a global logger if it's available. It acts as a simple facade to ensure logging occurs correctly for various supported AI clients.*


### stop (function, L145-L149)

> *Summary: Halts the logging process by calling `stop()` on the global logger instance if it exists, and then sets a global flag to indicate that logging has ceased.*


### get_connection (function, L152-L157)

> *Summary: Retrieves the database connection object from a globally available logger instance, returning `None` if the logger itself has not been initialized. This function acts as a safe accessor to ensure logging infrastructure is present before attempting to fetch the connection.*


### logging_enabled (function, L160-L161)

> *Summary: Checks a global flag to determine if runtime logging is active. Returns `True` if logging is enabled, otherwise `False`.*

