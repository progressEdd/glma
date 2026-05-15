# autogen/io/base.py

6 class(es): OutputStream, InputStream, AsyncInputStream, IOStreamProtocol, AsyncIOStreamProtocol, IOStream. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OutputStream | class |  |
| InputStream | class |  |
| AsyncInputStream | class |  |
| IOStreamProtocol | class |  |
| AsyncIOStreamProtocol | class |  |
| IOStream | class |  |

## Chunks

### OutputStream (class, L23-L41)

> *Summary: Defines a protocol for an object capable of handling output, requiring methods to print arbitrary data with formatting options and send structured `BaseEvent` messages. It serves as a contract for any stream implementation used by the system.*


### print (method, L24-L33, parent: OutputStream)

> *Summary: This method outputs provided data objects to the standard stream, allowing customization of separators, line endings, and flushing behavior. It accepts variable arguments for the content to be displayed.*


### send (method, L35-L41, parent: OutputStream)

> *Summary: Transmits a `BaseEvent` object to the configured output stream. This method handles the serialization and dispatching of event data.*


### InputStream (class, L46-L58)

> *Summary: Defines an interface for reading data from an input source. It requires an `input` method that accepts an optional prompt string and a boolean flag to indicate password mode, returning the resulting line as a string.*


### input (method, L47-L58, parent: InputStream)

> *Summary: Reads a single line of text from standard input, optionally displaying a prompt and masking the input if `password` is set to true. It returns the captured string from the user's entry.*


### AsyncInputStream (class, L63-L75)

> *Summary: Defines an asynchronous protocol for reading data from an input source. It requires an `input` method that accepts an optional prompt string and a password flag, returning the read line as a string.*


### input (method, L64-L75, parent: AsyncInputStream)

> *Summary: Asynchronously reads a line of text from standard input, optionally displaying a prompt and masking the input if `password` is set to true. It returns the captured string from the user's input.*


### IOStreamProtocol (class, L80-L81)

> *Summary: Defines a standard interface that combines reading and writing capabilities for I/O operations. It serves as a contract ensuring any implementing class supports both input and output stream behaviors.*


### AsyncIOStreamProtocol (class, L86-L87)

> *Summary: Defines a protocol that combines asynchronous input and output stream capabilities. It serves as a contract for objects intended to handle streaming data asynchronously.*


### IOStream (class, L94-L151)

> *Summary: Provides a protocol and mechanisms for managing default input/output streams across different execution contexts. It allows setting a global default stream or temporarily overriding the current context's stream using a context manager, falling back to the global default if no specific context stream is set.*


### set_global_default (method, L103-L109, parent: IOStream)

> *Summary: This method updates a global configuration by assigning a provided `IOStream` instance as the system's default input or output stream. It modifies the internal state of the `IOStream` class to reflect this new default.*


### get_global_default (method, L112-L120, parent: IOStream)

> *Summary: Retrieves the system-wide default I/O stream instance, raising an error if no such default has been previously configured.*


### get_default (method, L123-L134, parent: IOStream)

> *Summary: Retrieves the system's designated input/output stream, falling back to a globally defined default if the primary stream is unavailable. It ensures that the retrieved stream is set as the current context's default before returning it.*


### set_default (method, L138-L151, parent: IOStream)

> *Summary: This method configures the global default I/O stream by temporarily setting a provided stream and ensuring it is restored afterward, yielding control during the operation. It takes an `IOStream` object as input and returns an iterator that completes after the stream has been successfully set and reset.*

