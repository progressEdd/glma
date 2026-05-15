# test/beta/tools/conftest.py

2 function(s): context, make_context.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| context | function |  |
| make_context | function |  |

## Chunks

### context (function, L14-L15)

> *Summary: Provides a mock `Context` object, initialized with a mocked stream, for use within tests. This setup ensures test isolation by substituting real I/O streams.*


### make_context (function, L19-L23)

> *Summary: This function returns a factory that creates `Context` objects, accepting arbitrary keyword arguments to populate the context's internal variables. It initializes each returned context with a mocked stream object.*

