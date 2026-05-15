# autogen/io/processors/console_event_processor.py

2 function(s): check_type_1, check_type_2. 2 class(es): ConsoleEventProcessor, AsyncConsoleEventProcessor. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ConsoleEventProcessor | class |  |
| AsyncConsoleEventProcessor | class |  |
| check_type_1 | function |  |
| check_type_2 | function |  |

## Chunks

### ConsoleEventProcessor (class, L18-L32)

> *Summary: This processor iterates over events within a `RunResponseProtocol` and handles them based on their type. If an event is an `InputRequestEvent`, it prompts the user for input (handling passwords securely) and sends the response back; otherwise, it prints the event directly to the console.*


### process (method, L19-L21, parent: ConsoleEventProcessor)

> *Summary: Iterates through the `events` contained within a received `RunResponseProtocol`. For each event found, it delegates processing to an internal method.*


### process_event (method, L23-L32, parent: ConsoleEventProcessor)

> *Summary: Handles incoming events by either prompting the user for input (with optional password masking) if it's an `InputRequestEvent`, or printing the event directly otherwise. The method modifies the event content with the user's response when an input request is received.*


### AsyncConsoleEventProcessor (class, L36-L52)

> *Summary: This processor asynchronously consumes events from a response stream, handling input requests by prompting the user via console (using `getpass` for passwords or standard `input`). Non-input events are simply printed to the console.*


### process (method, L37-L39, parent: AsyncConsoleEventProcessor)

> *Summary: Iterates over asynchronous events within a provided response object and processes each one sequentially using an internal method. This handles the stream of events emitted during an asynchronous run.*


### process_event (method, L41-L52, parent: AsyncConsoleEventProcessor)

> *Summary: If the incoming event is an `InputRequestEvent`, this method prompts the user for input—either a standard string or a password via `getpass`—and then sends the collected result back through the event content. Otherwise, it simply prints the event to the console.*


### check_type_1 (function, L57-L58)

> *Summary: This function acts as a type guard, asserting that the input object conforms to `ConsoleEventProcessor` and returning it if the assertion passes. It ensures the provided processor adheres to the expected protocol for subsequent processing steps.*


### check_type_2 (function, L60-L61)

> *Summary: This function acts as a type guard, asserting that the input object conforms to `AsyncConsoleEventProcessor` and returning it as an `AsyncEventProcessorProtocol`. It essentially validates and passes through the event processor instance.*

