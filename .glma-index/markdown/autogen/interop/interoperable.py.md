# autogen/interop/interoperable.py

1 class(es): Interoperable. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Interoperable | class |  |

## Chunks

### Interoperable (class, L15-L46)

> *Summary: Defines a contract requiring implementers to provide methods for converting an arbitrary tool into a standard `Tool` format and reporting reasons if the conversion is not supported. It mandates two class methods: one for conversion (`convert_tool`) and another for describing unsupported states (`get_unsupported_reason`).*


### convert_tool (method, L23-L35, parent: Interoperable)

> *Summary: This method facilitates transforming an arbitrary input tool into a standardized `Tool` object, accepting additional keyword arguments for the conversion process. It is intended to be implemented by classes conforming to the `Interoperable` protocol.*


### get_unsupported_reason (method, L38-L46, parent: Interoperable)

> *Summary: Retrieves a string explaining why an object implementing the `Interoperable` protocol is not supported. It expects a class as input and returns either a descriptive error message or `None`.*

