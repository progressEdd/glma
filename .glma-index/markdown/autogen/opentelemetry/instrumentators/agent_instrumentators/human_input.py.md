# autogen/opentelemetry/instrumentators/agent_instrumentators/human_input.py

1 function(s): instrument_human_input.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_human_input | function |  |

## Chunks

### instrument_human_input (function, L13-L61)

> *Summary: Wraps an `Agent` object to instrument its human input methods (`get_human_input` and `a_get_human_input`) using OpenTelemetry tracing. It intercepts calls, creates spans named "await\_human\_input", sets relevant attributes like the prompt and response, and returns the modified agent instance.*

