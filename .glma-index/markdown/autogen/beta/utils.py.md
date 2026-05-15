# autogen/beta/utils.py

2 function(s): build_model, _to_async.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| build_model | function |  |
| _to_async | function |  |

## Chunks

### build_model (function, L17-L31)

> *Summary: Creates a callable model wrapper around a given function by converting it to an asynchronous form if necessary. It configures the resulting model with a specific Pydantic serializer and controls result serialization based on input flags.*


### _to_async (function, L34-L54)

> *Summary: Wraps a synchronous or asynchronous function to ensure it can be called within an `async` context. If the input function is synchronous and `sync_to_thread` is true, it executes the function in a separate thread pool; otherwise, it calls the function directly within the async wrapper.*

