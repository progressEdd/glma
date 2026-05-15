# autogen/beta/middleware/builtin/logging.py

2 class(es): LoggingMiddleware, _LoggingMiddleware. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LoggingMiddleware | class |  |
| _LoggingMiddleware | class |  |

## Chunks

### LoggingMiddleware (class, L21-L26)

> *Summary: This middleware factory initializes with an optional logger and returns a concrete `_LoggingMiddleware` instance when called. It takes an incoming event and context as input to produce the logging middleware object.*


### __init__ (method, L22-L23, parent: LoggingMiddleware)

> *Summary: Initializes the middleware with an optional `logging.Logger` instance; if none is provided, it defaults to using a standard logger named "autogen".*


### __call__ (method, L25-L26, parent: LoggingMiddleware)

> *Summary: This method acts as a factory, taking an incoming `BaseEvent` and `Context` to instantiate and return a new logging middleware instance using the stored logger. It effectively wraps the event processing with logging capabilities.*


### _LoggingMiddleware (class, L29-L69)

> *Summary: This middleware intercepts and logs key interactions within an agent workflow, specifically tracking LLM calls, tool executions, and overall turns. It takes a logger instance as input and outputs the results of the wrapped operations after logging timing and details for each event.*


### __init__ (method, L32-L34, parent: _LoggingMiddleware)

> *Summary: Initializes the middleware with a specific `BaseEvent`, execution `Context`, and a configured `logging.Logger` instance for internal use. It stores the provided logger object to facilitate logging operations throughout its lifecycle.*


### on_llm_call (method, L36-L47, parent: _LoggingMiddleware)

> *Summary: This middleware intercepts LLM calls to log the incoming event and measure the execution time of the subsequent call. It wraps the original `call_next` function, logging both the input event and the final response along with its duration before returning the result.*


### on_tool_execution (method, L49-L58, parent: _LoggingMiddleware)

> *Summary: This asynchronous method intercepts tool execution flow to log the incoming tool call details and the final returned result. It passes the event and context through to the next handler before logging the outcome.*


### on_turn (method, L60-L69, parent: _LoggingMiddleware)

> *Summary: This middleware intercepts an agent's turn execution, logging the start and end of the process. It passes the incoming event and context to the next handler in the chain and returns its resulting model response.*

