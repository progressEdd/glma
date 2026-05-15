# autogen/beta/middleware/builtin/telemetry.py

1 function(s): _get_tracer. 2 class(es): TelemetryMiddleware, _TelemetryMiddlewareInstance. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _get_tracer | function |  |
| TelemetryMiddleware | class |  |
| _TelemetryMiddlewareInstance | class |  |

## Chunks

### _get_tracer (function, L44-L46)

> *Summary: Retrieves a specific tracing object by querying the provided or default `TracerProvider`. This function ensures instrumentation is available for the current module using predefined schema details.*


### TelemetryMiddleware (class, L49-L86)

> *Summary: This middleware intercepts events to emit OpenTelemetry spans for various agent activities like LLM calls and tool executions. It accepts configuration parameters such as a `TracerProvider`, content capture preference, and names for the agent, provider, and model. The primary output is an instance of itself that wraps event processing with telemetry instrumentation.*


### __init__ (method, L62-L75, parent: TelemetryMiddleware)

> *Summary: Initializes a telemetry handler by setting up tracing using an optional `TracerProvider` and configuring data capture settings. It stores specific identifiers like the agent, provider, and model names for subsequent telemetry reporting.*


### __call__ (method, L77-L86, parent: TelemetryMiddleware)

> *Summary: This method constructs and returns a telemetry middleware instance. It takes an incoming event and context as input to initialize the middleware with tracing and configuration details like agent and model names.*


### _TelemetryMiddlewareInstance (class, L89-L265)

> *Summary: This middleware intercepts various agent lifecycle events—like turns, LLM calls, tool executions, and human inputs—to automatically record detailed telemetry data. It uses a provided tracer to create spans, setting attributes for context such as agent/model names, provider details, input content, and usage metrics upon successful execution or error.*


### __init__ (method, L90-L106, parent: _TelemetryMiddlewareInstance)

> *Summary: Initializes a telemetry handler by storing necessary context, tracing tools, and configuration parameters like content capturing status, agent name, and specific model/provider identifiers. This setup prepares the object to record events based on the provided `BaseEvent` and `Context`.*


### on_turn (method, L108-L133, parent: _TelemetryMiddlewareInstance)

> *Summary: This middleware intercepts an agent turn execution to wrap the call within a tracing span for monitoring. It records metadata like agent name, provider, and model onto the span before passing the event and context to the next handler, ensuring exceptions are also recorded.*


### on_llm_call (method, L135-L200, parent: _TelemetryMiddlewareInstance)

> *Summary: This method wraps an LLM call to instrument it with tracing spans, capturing details about the request inputs (if configured) and recording metrics like token usage from the resulting `ModelResponse`. It ensures comprehensive observability by setting various attributes on the span before returning the final response.*


### on_tool_execution (method, L202-L236, parent: _TelemetryMiddlewareInstance)

> *Summary: This middleware intercepts tool execution to trace the operation using OpenTelemetry spans. It records metadata about the tool call and arguments, captures exceptions during execution, and optionally logs the resulting content if it's a successful text input.*


### on_human_input (method, L238-L265, parent: _TelemetryMiddlewareInstance)

> *Summary: This method intercepts human input requests to record telemetry data for tracing and monitoring purposes. It wraps the call to the next hook, capturing the input prompt and the resulting message content if content capture is enabled, before returning the final `HumanMessage`.*

