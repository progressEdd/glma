# autogen/opentelemetry/instrumentators/agent.py

1 function(s): instrument_agent.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_agent | function |  |

## Chunks

### instrument_agent (function, L29-L82)

> *Summary: This function modifies an existing `Agent` instance to emit OpenTelemetry spans for various operations like chat initiation, reply generation, and tool execution. It takes the agent and a `TracerProvider` as input and returns the same, now instrumented, agent object.*

