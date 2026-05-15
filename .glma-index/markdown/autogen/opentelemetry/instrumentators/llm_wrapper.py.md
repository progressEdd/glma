# autogen/opentelemetry/instrumentators/llm_wrapper.py

2 function(s): instrument_llm_wrapper, _set_llm_response_attributes.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_llm_wrapper | function |  |
| _set_llm_response_attributes | function |  |

## Chunks

### instrument_llm_wrapper (function, L26-L114)

> *Summary: This function patches `OpenAIWrapper.create` to wrap LLM API calls with OpenTelemetry spans, capturing provider, model, token usage, and response metadata. It accepts a tracer provider and an optional flag to include sensitive input/output messages in the span attributes.*


### _set_llm_response_attributes (function, L117-L155)

> *Summary: This function enriches an OpenTelemetry span with metadata derived from a language model response object. It extracts and sets attributes for the model name, token usage (input/output), finish reasons, cost, and optionally, detailed output messages including tool calls.*

