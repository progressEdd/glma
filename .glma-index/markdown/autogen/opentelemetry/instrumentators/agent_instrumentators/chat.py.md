# autogen/opentelemetry/instrumentators/agent_instrumentators/chat.py

4 function(s): instrument_initiate_chat, instrument_resume, instrument_run_chat, instrument_initiate_chats.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_initiate_chat | function |  |
| instrument_resume | function |  |
| instrument_run_chat | function |  |
| instrument_initiate_chats | function |  |

## Chunks

### instrument_initiate_chat (function, L20-L154)

> *Summary: Wraps an `Agent` object to instrument its chat initiation methods (`a_initiate_chat` and `initiate_chat`) using OpenTelemetry tracing. It intercepts calls, creates a "conversation" span, extracts metadata like provider, model, input/output messages, cost, and token usage from the method's return value, then returns the modified agent.*


### instrument_resume (function, L157-L176)

> *Summary: Wraps an agent's `a_resume` method to trace it as a resumed conversation span using the provided tracer. It intercepts calls to this method, adds specific OpenTelemetry attributes indicating a resumed conversation, and then executes the original function.*


### instrument_run_chat (function, L179-L244)

> *Summary: Wraps an `Agent` object to instrument its synchronous (`run_chat`) and asynchronous (`a_run_chat`) chat methods using OpenTelemetry tracing. It captures input messages, sets relevant span attributes (like agent name and operation type), executes the original method, and then records the resulting output messages within a conversation span.*


### instrument_initiate_chats (function, L247-L325)

> *Summary: Wraps an `Agent` object's chat initiation methods (`initiate_chats` and `a_initiate_chats`) to inject OpenTelemetry tracing. It takes the agent and a tracer as input, recording details like chat counts, recipients, IDs, and summaries into spans for both synchronous and asynchronous calls.*

