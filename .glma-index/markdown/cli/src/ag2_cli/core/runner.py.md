# cli/src/ag2_cli/core/runner.py

3 function(s): _drain_events, _extract_chat_result, execute. 2 class(es): RunResult, CliIOStream. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RunResult | class |  |
| CliIOStream | class |  |
| _drain_events | function |  |
| _extract_chat_result | function |  |
| execute | function |  |

## Chunks

### RunResult (class, L22-L32)

> *Summary: This class structures the outcome of an agent execution. It holds various metrics such as output, turn count, cost, elapsed time, error logs, and a detailed history of interactions.*


### CliIOStream (class, L35-L60)

> *Summary: This class wraps standard I/O operations to funnel agent events and print statements into provided callback functions. It accepts optional `on_print` and `on_event` handlers, routing output via its `print()` and `send()` methods, while the `input()` method always returns an empty string.*


### __init__ (method, L42-L48, parent: CliIOStream)

> *Summary: Initializes the runner by accepting optional callback functions for printing output and handling events. These callbacks are stored internally to be invoked during execution.*


### print (method, L50-L53, parent: CliIOStream)

> *Summary: This method formats a variable number of input objects into a single string, joining them with a specified separator. It then optionally passes this resulting text to an internal callback function if enabled.*


### send (method, L55-L57, parent: CliIOStream)

> *Summary: When called with a `message`, this method immediately triggers an event handler if one is registered. It passes the received message directly to the configured callback function.*


### input (method, L59-L60, parent: CliIOStream)

> *Summary: This method simulates user input by accepting an optional prompt string and a boolean flag for password masking. It currently returns an empty string as a placeholder implementation.*


### _drain_events (function, L63-L76)

> *Summary: Processes a `RunResponse` by iterating through its events, invoking an optional callback for each event, and automatically responding to "input\_request" events with an exit command. Finally, it populates the `RunResult` object with summary data, message count, cost, and last speaker information from the response.*


### _extract_chat_result (function, L79-L95)

> *Summary: This function processes a returned object (`ret`) to populate a `RunResult` structure. It extracts chat history and cost if the return type has specific attributes, or sets the output directly if the return is a string.*


### execute (function, L98-L207)

> *Summary: Executes a discovered agent or group of agents based on its type, taking an input message and optional callbacks for printing or events. It manages execution flow—whether running a main function, a single agent, or a multi-agent chat—and returns a `RunResult` containing the output, history, timing, and any errors encountered.*

