# autogen/opentelemetry/instrumentators/agent_instrumentators/reply.py

2 function(s): instrument_generate_reply, instrument_generate_oai_reply.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_generate_reply | function |  |
| instrument_generate_oai_reply | function |  |

## Chunks

### instrument_generate_reply (function, L25-L102)

> *Summary: Wraps an `Agent` object by instrumenting its asynchronous (`a_generate_reply`) and synchronous (`generate_reply`) methods to create OpenTelemetry spans. It captures metadata like the agent's name, LLM provider/model, input messages, and output reply within these spans before returning the modified agent.*


### instrument_generate_oai_reply (function, L105-L171)

> *Summary: Wraps the `a_generate_oai_reply` method to ensure OpenTelemetry context is correctly propagated when execution moves to a separate thread via `run_in_executor`. It captures the current tracing context before offloading the call and attaches it within the executor thread, returning the modified agent instance.*

