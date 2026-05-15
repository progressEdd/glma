# autogen/logger/file_logger.py

1 function(s): safe_serialize. 1 class(es): FileLogger. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| safe_serialize | function |  |
| FileLogger | class |  |

## Chunks

### safe_serialize (function, L44-L51)

> *Summary: This function serializes a Python object into a JSON string, using a custom encoder to handle objects that don't natively support JSON serialization by calling their `to_json()` method or marking them as non-serializable. It takes any arbitrary object and returns a string representation.*


### FileLogger (class, L55-L263)

> *Summary: Initializes a persistent logger that writes structured JSON logs to a file within an `autogen_logs` directory, generating a unique session ID upon creation. It provides methods to record various events like chat completions, agent instantiation, and function calls by accepting specific data structures as inputs and writing them to the configured log file.*


### __init__ (method, L56-L74, parent: FileLogger)

> *Summary: Initializes a file logger by creating a unique session ID and ensuring a dedicated log directory exists. It configures the standard Python logger to write INFO-level messages to a specified or default log file within that directory.*


### start (method, L76-L83, parent: FileLogger)

> *Summary: Initializes the logger by recording a start message using the configured session ID, catching any exceptions during this process. It always returns the current `session_id` regardless of whether the logging operation succeeded or failed.*


### log_chat_completion (method, L85-L123, parent: FileLogger)

> *Summary: This method serializes and logs detailed information about a completed chat interaction, including invocation IDs, client/wrapper identifiers, request/response payloads, cost, and timing data. It accepts various inputs describing the interaction and outputs nothing, logging errors if serialization or logging fails.*


### log_new_agent (method, L125-L144, parent: FileLogger)

> *Summary: This method serializes and logs details of a newly instantiated agent, including its ID, name, type, initialization arguments, and thread context. It accepts an `agent` object and optional `init_args`, outputting a structured JSON string via the logger upon success or logging an error if serialization fails.*


### log_event (method, L146-L182, parent: FileLogger)

> *Summary: Accepts a source (Agent or string), an event name, and arbitrary keyword arguments; it serializes these inputs into a structured JSON log entry containing metadata like timestamps and thread IDs before writing the final record to the configured logger. It handles non-serializable data within the keyword arguments by substituting a descriptive placeholder instead of failing.*


### log_new_wrapper (method, L184-L198, parent: FileLogger)

> *Summary: Records the creation of a new wrapper instance by serializing its ID, session context, and initialization arguments into a JSON string. This data is then logged via the internal logger, capturing thread identification for tracking purposes.*


### log_new_client (method, L200-L233, parent: FileLogger)

> *Summary: Records the instantiation of a new AI client by serializing details like its ID, wrapper's ID, session context, and redacted initialization arguments. It outputs this structured log data via an internal logger instance, handling potential logging exceptions gracefully.*


### log_function_use (method, L235-L252, parent: FileLogger)

> *Summary: Records the invocation of a registered function by capturing its source, input arguments, and return value into a JSON string. This data is then logged at the INFO level using the internal logger instance.*


### get_connection (method, L254-L256, parent: FileLogger)

> *Summary: This method does nothing, as the `FileLogger` implementation requires no external database or network connections. It serves as a placeholder to satisfy an interface requirement.*


### stop (method, L258-L263, parent: FileLogger)

> *Summary: Closes all attached `FileHandler` instances on the internal logger and removes them from its list of handlers. This method ensures that file resources are properly released when the logger is shut down.*

