# test/beta/ag_ui/test_empty_chunks.py

6 class(es): _StreamingClient, _StreamingConfig, _NonStreamingEmptyClient, _NonStreamingEmptyConfig, TestEmptyModelMessageChunk, TestEmptyModelMessage. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _StreamingClient | class |  |
| _StreamingConfig | class |  |
| _NonStreamingEmptyClient | class |  |
| _NonStreamingEmptyConfig | class |  |
| TestEmptyModelMessageChunk | class |  |
| TestEmptyModelMessage | class |  |

## Chunks

### _StreamingClient (class, L41-L63)

> *Summary: This client simulates a streaming LLM response by iterating over provided string chunks and sending them as `ModelMessageChunk` events to the context. After emitting all chunks, it sends a final complete `ModelMessage` containing the concatenated text before returning the overall response object.*


### __init__ (method, L46-L47, parent: _StreamingClient)

> *Summary: Initializes the object by storing any provided string arguments as a tuple in the `chunks` attribute. This allows the instance to hold zero or more input strings.*


### __call__ (method, L49-L63, parent: _StreamingClient)

> *Summary: Iterates over stored chunks, sending each one as a `ModelMessageChunk` to the context asynchronously. Finally, it joins all chunks into a complete message and sends that final message before returning a response object.*


### _StreamingConfig (class, L66-L77)

> *Summary: This configuration object stores a variable number of string chunks and provides methods to clone itself or instantiate a `_StreamingClient` using those stored chunks. It explicitly prevents the creation of a file-based client instance.*


### __init__ (method, L67-L68, parent: _StreamingConfig)

> *Summary: Initializes the object by accepting a variable number of string arguments and storing them in an instance attribute named `chunks`. This method sets up the internal state with the provided chunk strings.*


### copy (method, L70-L71, parent: _StreamingConfig)

> *Summary: This method returns a reference to the current instance, effectively creating a shallow copy of the object it is called on. It serves as an identity operation for cloning purposes within the class structure.*


### create (method, L73-L74, parent: _StreamingConfig)

> *Summary: Instantiates and returns a `_StreamingClient` object, passing all the stored chunk data from the instance as arguments to its constructor.*


### create_files_client (method, L76-L77, parent: _StreamingConfig)

> *Summary: This method is intended to initialize a client for file creation operations but currently raises `NotImplementedError`. It takes no arguments and returns nothing.*


### _NonStreamingEmptyClient (class, L80-L92)

> *Summary: This client simulates a non-streaming LLM response by sending a single empty `ModelMessage` to the provided context. It accepts a sequence of events and context, returning a `ModelResponse` containing that empty message and no tool calls.*


### __call__ (method, L84-L92, parent: _NonStreamingEmptyClient)

> *Summary: When invoked with a sequence of events and a context, this method immediately sends an empty message to the context and returns a response containing that empty message and no tool calls. It serves as a handler for scenarios requiring a null or initial response without processing input messages.*


### _NonStreamingEmptyConfig (class, L95-L103)

> *Summary: This configuration object represents an empty, non-streaming setup. It provides methods to return itself when copied and instantiate a corresponding client upon creation, while explicitly disallowing file client instantiation.*


### copy (method, L96-L97, parent: _NonStreamingEmptyConfig)

> *Summary: This method returns a reference to the current instance, effectively creating a shallow copy of the object. It takes no arguments and outputs an object of the same type as itself.*


### create (method, L99-L100, parent: _NonStreamingEmptyConfig)

> *Summary: Instantiates and returns a new instance of the `_NonStreamingEmptyClient` object. This method serves to provide an empty, non-streaming client implementation.*


### create_files_client (method, L102-L103, parent: _NonStreamingEmptyConfig)

> *Summary: This method is intended to instantiate a client for file creation operations but currently raises `NotImplementedError`. It takes no arguments and returns nothing.*


### TestEmptyModelMessageChunk (class, L106-L136)

> *Summary: This test suite verifies how the streaming UI handles message chunks, ensuring that an initial empty chunk does not incorrectly trigger a text message start. It also confirms that empty chunks occurring between non-empty segments are effectively ignored and do not result in any content events with an empty delta.*


### test_empty_chunk_does_not_open_text_message (method, L107-L122, parent: TestEmptyModelMessageChunk)

> *Summary: This test verifies that an initial empty data chunk does not trigger a text message start event when streaming agent responses. It asserts that only the subsequent non-empty chunk correctly initiates and provides the content for the single resulting text message.*


### test_empty_chunk_between_real_chunks_dropped (method, L124-L136, parent: TestEmptyModelMessageChunk)

> *Summary: This test verifies that when processing a stream containing real text chunks separated by empty ones, only the non-empty content deltas are collected. It asserts that the resulting list of content deltas matches the expected sequence from the input configuration and confirms no empty delta is ever present in the output events.*


### TestEmptyModelMessage (class, L139-L149)

> *Summary: Verifies that when an agent is initialized with empty configuration and receives a standard user message, the resulting stream emits no text-related events. It confirms the absence of `TEXT_MESSAGE_CHUNK`, `TEXT_MESSAGE_CONTENT`, and `TEXT_MESSAGE_START` events during processing.*


### test_empty_non_streaming_message_emits_no_text_event (method, L140-L149, parent: TestEmptyModelMessage)

> *Summary: When processing a non-streaming message with empty chunks, this test verifies that no text-related events are emitted by the stream. It confirms the absence of `TEXT_MESSAGE_CHUNK`, `TEXT_MESSAGE_CONTENT`, and `TEXT_MESSAGE_START` events after running an input through the agent's UI stream.*

