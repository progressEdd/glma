# autogen/opentelemetry/instrumentators/a2a.py

1 function(s): instrument_a2a_server.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_a2a_server | function |  |

## Chunks

### instrument_a2a_server (function, L18-L71)

> *Summary: This function wraps an A2A agent server with OpenTelemetry tracing by injecting custom middleware to trace incoming requests and instruments the underlying agent component. It accepts a server instance and a `TracerProvider`, returning the fully instrumented server object.*

