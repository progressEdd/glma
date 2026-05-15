# autogen/opentelemetry/instrumentators/agent_instrumentators/code.py

2 function(s): instrument_code_execution, instrument_create_or_get_executor.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| instrument_code_execution | function |  |
| instrument_create_or_get_executor | function |  |

## Chunks

### instrument_code_execution (function, L15-L76)

> *Summary: Wraps a specific method on an `Agent` instance to trace its execution using a provided `Tracer`. It finds the original code execution reply function, replaces it with a traced version that records span attributes like exit code and output, and returns the modified `Agent`.*


### instrument_create_or_get_executor (function, L79-L104)

> *Summary: This function wraps the `_create_or_get_executor` method on an agent to automatically instrument any dynamically created executors. It replaces the original method with a context manager that applies a provided `instrumentator` to the newly created executor before yielding it.*

