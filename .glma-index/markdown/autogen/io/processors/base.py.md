# autogen/io/processors/base.py

2 class(es): EventProcessorProtocol, AsyncEventProcessorProtocol. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| EventProcessorProtocol | class |  |
| AsyncEventProcessorProtocol | class |  |

## Chunks

### EventProcessorProtocol (class, L15-L16)

> *Summary: Defines a contract for event processors that must implement a `process` method. This method accepts a `RunResponseProtocol` object as input and performs some action without returning a value.*


### process (method, L16-L16, parent: EventProcessorProtocol)

> *Summary: This method accepts a `RunResponseProtocol` object as input and performs some internal processing on it without returning a value. It is responsible for handling the results of a run operation.*


### AsyncEventProcessorProtocol (class, L20-L21)

> *Summary: Defines an asynchronous interface requiring a `process` method that accepts an `AsyncRunResponseProtocol` and returns nothing. This protocol dictates how event processing should occur asynchronously within the system.*


### process (method, L21-L21, parent: AsyncEventProcessorProtocol)

> *Summary: This asynchronous method takes an `AsyncRunResponseProtocol` object as input and processes it internally without returning a value. It is responsible for handling the received run response data.*

