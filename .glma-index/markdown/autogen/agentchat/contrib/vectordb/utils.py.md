# autogen/agentchat/contrib/vectordb/utils.py

3 function(s): get_logger, filter_results_by_distance, chroma_results_to_query_results. 1 class(es): ColoredLogger. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ColoredLogger | class |  |
| get_logger | function |  |
| filter_results_by_distance | function |  |
| chroma_results_to_query_results | function |  |

## Chunks

### ColoredLogger (class, L15-L35)

> *Summary: Extends the standard Python `logging.Logger` to output messages with ANSI colors. It wraps all logging methods (`debug`, `info`, etc.) to apply specified or default colors using an external coloring utility before passing them to the parent logger.*


### __init__ (method, L16-L17, parent: ColoredLogger)

> *Summary: Initializes a logger instance with a specified name and an optional logging level. It inherits the base logger's configuration from its parent class.*


### debug (method, L19-L20, parent: ColoredLogger)

> *Summary: This method forwards a message to the parent's debug function after applying ANSI color formatting to the input string. It allows for colored logging output during debugging operations.*


### info (method, L22-L23, parent: ColoredLogger)

> *Summary: This method wraps the parent's `info` function to display a message with optional color formatting. It accepts a string message and forwards any additional arguments or keyword arguments to the superclass implementation.*


### warning (method, L25-L26, parent: ColoredLogger)

> *Summary: This method wraps the parent's `warning` function to automatically apply colorization to the provided message. It accepts a message string and optional arguments for styling before passing them up the inheritance chain.*


### error (method, L28-L29, parent: ColoredLogger)

> *Summary: This method wraps the parent's `error` function to display a formatted error message. It accepts a message and optional arguments, applying a specified color for visual emphasis in the output.*


### critical (method, L31-L32, parent: ColoredLogger)

> *Summary: This method wraps the parent's `critical` logging function to ensure the provided message is colored before outputting it. It accepts a message string and optional arguments for formatting.*


### fatal (method, L34-L35, parent: ColoredLogger)

> *Summary: This method wraps the parent's `fatal` function to output a message with a specified color. It takes a message string and optional arguments/keyword arguments for formatting.*


### get_logger (function, L38-L44)

> *Summary: Creates and configures a custom, colorized logger instance for a given name and log level. It attaches a stream handler with a standard timestamped formatter to output logs to the console.*


### filter_results_by_distance (function, L50-L63)

> *Summary: This function filters a list of query results based on a specified maximum distance. It takes `QueryResults` and an optional `distance_threshold`, returning a new set of results containing only entries whose associated distances are strictly less than the threshold if one is provided.*


### chroma_results_to_query_results (function, L66-L126)

> *Summary: Transforms a dictionary containing vector database results (features and distances) into a structured list of tuples for query output. It iterates through the provided data, pairing feature values from various keys with corresponding distances specified by `special_key`.*

