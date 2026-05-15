# autogen/opentelemetry/instrumentators/agent_instrumentators/tool.py

1 function(s): instrument_execute_function.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_execute_function | function |  |

## Chunks

### instrument_execute_function (function, L14-L93)

> *Summary: This code wraps an `Agent` instance's synchronous and asynchronous function execution methods to trace them using OpenTelemetry. It intercepts calls, creates spans named "execute\_tool [func\_name]", sets relevant metadata like tool name and arguments, executes the original method, and records success or error status in the span before returning the result.*

