# autogen/logger/logger_utils.py

7 function(s): get_sensitive_exclude_keys, redact, get_current_ts, to_dict, get_event_logger, _stringify, event_print. 1 class(es): EventStreamHandler. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_sensitive_exclude_keys | function |  |
| redact | function |  |
| get_current_ts | function |  |
| to_dict | function |  |
| EventStreamHandler | class |  |
| get_event_logger | function |  |
| _stringify | function |  |
| event_print | function |  |

## Chunks

### get_sensitive_exclude_keys (function, L42-L47)

> *Summary: Returns a tuple containing predefined sensitive keys, including `"self"` and `"__class__"`, to be used when excluding fields from object serialization. This list is augmented by any keys defined in the `SENSITIVE_KEYS` constant.*


### redact (function, L50-L65)

> *Summary: Recursively masks sensitive keys within nested dictionaries and collections by replacing their values with "***REDACTED***". It accepts arbitrary data and a recursion depth limit to prevent infinite loops.*


### get_current_ts (function, L73-L79)

> *Summary: Retrieves the current time formatted as a string, specifically using the UTC timezone and including microseconds. This function outputs a standardized timestamp string for logging purposes.*


### to_dict (function, L82-L115)

> *Summary: Converts various Python objects (like dicts, lists, or instances with `__dict__`) into a dictionary representation. It recursively processes nested structures while allowing specific keys to be excluded and certain types to bypass recursion.*


### EventStreamHandler (class, L118-L132)

> *Summary: This handler extends `StreamHandler` to process log records by formatting them and writing the message along with a potential custom end marker to its configured stream. It ensures the output is flushed if a specific flag on the record indicates it should be immediately visible.*


### __init__ (method, L119-L120, parent: EventStreamHandler)

> *Summary: Initializes the logger by setting its output stream to either a provided `stream` or the standard output (`sys.stdout`). This ensures logging messages are directed to the correct destination upon object creation.*


### emit (method, L122-L132, parent: EventStreamHandler)

> *Summary: This method takes a `logging.LogRecord`, formats it into a message, and writes the resulting string along with an optional ending character to an internal stream. It ensures the stream is flushed if configured and catches any exceptions by calling an error handler.*


### get_event_logger (function, L135-L144)

> *Summary: Retrieves a specific event logger instance, ensuring it has an `EventStreamHandler` writing to standard output if no handlers are currently attached. It configures the logger's level to INFO if it was previously unset and disables propagation before returning the configured logger object.*


### _stringify (function, L147-L148)

> *Summary: Concatenates an iterable of objects into a single string, using the provided separator between each element. It converts every object to its string representation before joining them.*


### event_print (function, L151-L162)

> *Summary: This utility function logs a formatted string derived from variable arguments to a specified logger instance or a default event logger. It accepts optional formatting parameters like separator and ending character, which are passed as extra context during the logging call.*

