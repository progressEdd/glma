# autogen/beta/middleware/builtin/history_limiter.py

1 function(s): _skip_leading_tool_results. 2 class(es): HistoryLimiter, _HistoryLimiter. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| HistoryLimiter | class |  |
| _HistoryLimiter | class |  |
| _skip_leading_tool_results | function |  |

## Chunks

### HistoryLimiter (class, L12-L19)

> *Summary: This factory creates a middleware that limits the number of stored events based on a provided maximum count. It accepts an integer `max_events` during initialization and returns a concrete limiter instance when called with an event and context.*


### __init__ (method, L13-L16, parent: HistoryLimiter)

> *Summary: Initializes the limiter by setting a maximum event count, ensuring this value is positive to prevent invalid configurations.*


### __call__ (method, L18-L19, parent: HistoryLimiter)

> *Summary: This method acts as a middleware handler, taking an incoming `BaseEvent` and its associated `Context`. It returns a new instance of the history limiter, configured with the event, context, and the stored maximum event limit.*


### _HistoryLimiter (class, L22-L50)

> *Summary: This middleware truncates the message history passed to an LLM call if it exceeds a specified maximum event count. It intelligently trims the sequence by either keeping only the first request or selecting the most recent relevant events while skipping initial tool results.*


### __init__ (method, L25-L27, parent: _HistoryLimiter)

> *Summary: Initializes the limiter with a base event, execution context, and a maximum number of events. It stores this `max_events` value to control the history size.*


### on_llm_call (method, L29-L50, parent: _HistoryLimiter)

> *Summary: This method limits the number of events passed to an LLM call based on a configured maximum. If the event count exceeds the limit, it intelligently trims the sequence by keeping the initial request and the most recent relevant events, or just the tail if the first event isn't a request.*


### _skip_leading_tool_results (function, L53-L56)

> *Summary: Advances an index past any initial sequence of `ToolResultsEvent` objects within a list of events. It returns the index immediately following the last leading tool result found.*

