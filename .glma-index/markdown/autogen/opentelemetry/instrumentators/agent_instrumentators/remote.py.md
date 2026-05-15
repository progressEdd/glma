# autogen/opentelemetry/instrumentators/agent_instrumentators/remote.py

1 function(s): instrument_remote_reply.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_remote_reply | function |  |

## Chunks

### instrument_remote_reply (function, L14-L55)

> *Summary: This function modifies an `Agent` instance by wrapping its remote reply method (`a_generate_remote_reply`) with OpenTelemetry tracing. It intercepts calls to this method, creating a span for the "invoke\_agent" operation and injecting trace context into outgoing HTTP requests before executing the original logic.*

