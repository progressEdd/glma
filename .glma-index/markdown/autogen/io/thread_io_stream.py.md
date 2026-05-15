# autogen/io/thread_io_stream.py

2 function(s): check_type_1, check_type_2. 2 class(es): ThreadIOStream, AsyncThreadIOStream. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ThreadIOStream | class |  |
| AsyncThreadIOStream | class |  |
| check_type_1 | function |  |
| check_type_2 | function |  |

## Chunks

### ThreadIOStream (class, L18-L40)

> *Summary: Manages asynchronous communication between threads using internal `queue.Queue` objects for sending and receiving data. It allows external code to send messages via `send()` or request input via `input()`, optionally blocking based on a provided step controller.*


### __init__ (method, L19-L22, parent: ThreadIOStream)

> *Summary: Initializes a stream handler by creating internal input and output queues, optionally accepting a `StepController` object to manage the streaming process.*


### input (method, L24-L26, parent: ThreadIOStream)

> *Summary: Sends an input request event containing a prompt and optional password to the connected stream, then blocks until it receives and returns the corresponding string output from that stream.*


### print (method, L28-L30, parent: ThreadIOStream)

> *Summary: This method wraps standard Python printing functionality by converting the input objects into a `PrintEvent` and then sending that event through the stream's internal mechanism. It effectively pipes console output data to be transmitted via the stream.*


### send (method, L32-L36, parent: ThreadIOStream)

> *Summary: Pushes a message onto an internal input stream and, if a step controller exists, blocks the caller until that controller acknowledges receipt of the message. This ensures synchronized data transfer between components.*


### input_stream (method, L39-L40, parent: ThreadIOStream)

> *Summary: Returns the internal `queue.Queue` object used for receiving input data from the stream. This provides external access to the buffered input queue managed by the instance.*


### AsyncThreadIOStream (class, L43-L61)

> *Summary: Manages asynchronous communication between threads by using internal `AsyncQueue`s for sending and receiving messages. It provides methods to send structured events (`send`), print formatted output (`print`), and asynchronously retrieve input from the stream (`input`).*


### __init__ (method, L44-L46, parent: AsyncThreadIOStream)

> *Summary: Initializes the stream by creating two asynchronous queues, one for receiving input and another for sending output. These queues manage the data flow between different parts of the system.*


### input (method, L48-L50, parent: AsyncThreadIOStream)

> *Summary: Sends an input request containing a prompt and optional password to the underlying stream, then asynchronously waits for and returns the corresponding response string from that stream.*


### print (method, L52-L54, parent: AsyncThreadIOStream)

> *Summary: This method wraps standard Python printing functionality by converting the input objects into a `PrintEvent` and then sending that event through the stream's communication mechanism. It effectively pipes console output events to the underlying system for transmission.*


### send (method, L56-L57, parent: AsyncThreadIOStream)

> *Summary: This method immediately places a given message into the internal input stream without blocking. It acts as a non-blocking producer for data destined for the thread's processing queue.*


### input_stream (method, L60-L61, parent: AsyncThreadIOStream)

> *Summary: Returns the internal asynchronous queue used for receiving input data. This method provides access to the stream where incoming messages are buffered.*


### check_type_1 (function, L66-L67)

> *Summary: This function asserts that the input object is an instance of `ThreadIOStream` and returns it as a conforming `IOStreamProtocol`. It acts as a type guard to ensure compatibility with stream protocols.*


### check_type_2 (function, L69-L70)

> *Summary: This function asserts that the input object conforms to `AsyncThreadIOStream` and returns it as an `AsyncIOStreamProtocol`. It acts as a type-checking wrapper, ensuring compatibility with a broader stream protocol.*

