# test/beta/stream/redis/test_redis_stream.py

4 function(s): mock_redis, redis_stream, redis_storage, stream_id. 6 class(es): MockRedis, MockPipeline, MockPubSub, TestRedisStorage, TestRedisStream, TestBinaryRoundTrip. 39 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MockRedis | class |  |
| MockPipeline | class |  |
| MockPubSub | class |  |
| mock_redis | function |  |
| redis_stream | function |  |
| redis_storage | function |  |
| stream_id | function |  |
| TestRedisStorage | class |  |
| TestRedisStream | class |  |
| TestBinaryRoundTrip | class |  |

## Chunks

### MockRedis (class, L26-L57)

> *Summary: Provides an in-memory simulation of `redis.asyncio.Redis` for testing purposes. It supports basic Redis operations like pushing data to lists, retrieving ranges, deleting keys, and simulating message publishing across subscribed channels.*


### __init__ (method, L29-L31, parent: MockRedis)

> *Summary: Initializes the object by setting up two internal dictionaries: one to store data mapping strings to lists of bytes, and another to track mock Pub/Sub channels associated with specific keys. These structures are used for managing stream data and subscriptions within the test environment.*


### rpush (method, L33-L34, parent: MockRedis)

> *Summary: Appends a byte value to the end of a list associated with a given string key within the internal data structure. This operation modifies the state by adding the new element to the specified list.*


### lrange (method, L36-L39, parent: MockRedis)

> *Summary: Retrieves a range of elements from a specified key's data structure. It takes the key, a starting index, and an ending index as input, returning a list of byte strings representing the requested slice.*


### delete (method, L41-L42, parent: MockRedis)

> *Summary: Removes a specified key from the internal data store if it exists. It takes a string representing the key as input and returns nothing upon successful deletion.*


### publish (method, L44-L48, parent: MockRedis)

> *Summary: This method broadcasts a given byte message to all registered subscribers for a specific channel. It iterates through the stored subscriber objects and asynchronously delivers the message to each one, returning the total count of recipients.*


### pipeline (method, L50-L51, parent: MockRedis)

> *Summary: Returns a `MockPipeline` instance associated with the current object, optionally configured to act as a transaction. This allows chaining multiple operations before execution.*


### pubsub (method, L53-L54, parent: MockRedis)

> *Summary: Returns a mock PubSub object, initialized with the current instance, to simulate real-time message subscription capabilities.*


### aclose (method, L56-L57, parent: MockRedis)

> *Summary: This method is intended to close resources associated with the object, but currently does nothing (`pass`). It accepts no inputs and returns nothing.*


### MockPipeline (class, L60-L80)

> *Summary: This class simulates a Redis pipeline by buffering commands like `delete` and `rpush`. It accepts a `MockRedis` instance and executes all buffered operations sequentially against that mock object when the `execute` method is called.*


### __init__ (method, L61-L63, parent: MockPipeline)

> *Summary: Initializes the object by storing a provided `MockRedis` instance and setting up an empty list to track operations. This setup prepares the class for simulating Redis interactions.*


### __aenter__ (method, L65-L66, parent: MockPipeline)

> *Summary: When entering an asynchronous context, this method returns the current instance, allowing it to be used within `async with` blocks. This enables resource management or setup for stream testing operations.*


### __aexit__ (method, L68-L69, parent: MockPipeline)

> *Summary: This asynchronous exit method performs no operations upon exiting an async context manager. It is intended to clean up resources managed by the surrounding context block.*


### delete (method, L71-L72, parent: MockPipeline)

> *Summary: This method queues a deletion operation by appending the provided `key` to an internal list of operations. It signals the intent to remove data associated with that specific key.*


### rpush (method, L74-L75, parent: MockPipeline)

> *Summary: This method queues a command to push a byte string onto the right side of a specified Redis key. It records this operation internally without executing it immediately.*


### execute (method, L77-L80, parent: MockPipeline)

> *Summary: Iterates through a list of stored operations and asynchronously executes each one against the underlying Redis client using its corresponding method. After execution, it clears the internal operation queue.*


### MockPubSub (class, L83-L108)

> *Summary: Simulates Redis Pub/Sub behavior, allowing clients to subscribe and unsubscribe from specific channels via an injected `MockRedis` instance. It yields incoming messages asynchronously through the `listen()` coroutine after they are placed into an internal queue by the `_receive()` method.*


### __init__ (method, L84-L87, parent: MockPubSub)

> *Summary: Initializes the object by storing a mock Redis connection and setting up an empty list for channels and an asynchronous queue to hold data items. This sets up the necessary state for stream processing operations.*


### subscribe (method, L89-L92, parent: MockPubSub)

> *Summary: Registers a specific Redis channel with the stream handler by adding it to an internal list and notifying the underlying queue system about the subscription request. This method takes a channel name as input and performs no direct return value.*


### unsubscribe (method, L94-L97, parent: MockPubSub)

> *Summary: Removes a specified channel from the active subscriptions managed by the instance. It checks if the channel exists internally, then removes it from both the local tracking set and the underlying Redis pub/sub structure.*


### _receive (method, L99-L100, parent: MockPubSub)

> *Summary: This method accepts raw byte data and asynchronously enqueues it into an internal queue as a message object for further processing. It acts as the ingestion point for incoming stream data.*


### listen (method, L102-L105, parent: MockPubSub)

> *Summary: This method continuously pulls messages from an internal queue and yields each one as it arrives. It functions as a generator to stream incoming data indefinitely.*


### aclose (method, L107-L108, parent: MockPubSub)

> *Summary: This method is intended to close an underlying resource, likely a connection or stream handle, but currently does nothing. It accepts no inputs and returns nothing.*


### mock_redis (function, L114-L115)

> *Summary: Provides a factory function that returns an instance of `MockRedis` for testing purposes. This mock object simulates Redis behavior without requiring a live connection.*


### redis_stream (function, L119-L141)

> *Summary: This generator yields a factory function that creates and configures `RedisStream` instances using provided mock Redis clients for both AIoRedis and storage layers. It allows the caller to dynamically generate multiple stream objects, which are subsequently closed after iteration.*


### redis_storage (function, L145-L155)

> *Summary: This function returns a factory that creates an instance of `RedisStorage` for testing purposes. It configures the storage to use a provided mock Redis client and accepts a serialization parameter from the incoming request.*


### stream_id (function, L159-L160)

> *Summary: Generates a unique identifier using UUID version 4. This function produces a universally unique string suitable for identifying streams or records.*


### TestRedisStorage (class, L163-L215)

> *Summary: These asynchronous tests verify the persistence and manipulation of event histories within a Redis-backed storage mechanism. They test saving, setting (including replacement), dropping, and retrieving empty or populated lists of `ToolCallEvent` objects using a provided stream ID.*


### test_save_and_get_history (method, L164-L177, parent: TestRedisStorage)

> *Summary: This test verifies the persistence and retrieval of a single event within a stream. It saves a `ToolCallEvent` to storage via a memory stream context and then asserts that retrieving the history returns exactly one matching event.*


### test_set_history (method, L179-L191, parent: TestRedisStorage)

> *Summary: This test verifies that a sequence of `ToolCallEvent` objects is correctly persisted and retrieved from storage. It inputs a stream ID and a list of events, asserting that the retrieval returns the exact same events in order.*


### test_set_history_replaces (method, L193-L201, parent: TestRedisStorage)

> *Summary: This test verifies that calling `set_history` multiple times for the same stream ID overwrites the previous entries. It asserts that after setting an initial event and then a subsequent one, only the latest event remains when retrieving the history.*


### test_drop_history (method, L203-L210, parent: TestRedisStorage)

> *Summary: This test verifies that calling `drop_history` successfully clears the stored event history for a given stream ID. It sets initial history, calls the drop method, and then asserts that retrieving the history returns an empty list.*


### test_empty_history (method, L212-L215, parent: TestRedisStorage)

> *Summary: Verifies that retrieving the message history for a given stream ID returns an empty list when no messages exist in the underlying Redis storage. It calls `get_history` on the provided storage object and asserts the result is an empty sequence.*


### TestRedisStream (class, L218-L390)

> *Summary: These tests verify the core functionality of a Redis-backed event streaming system, ensuring events are correctly persisted, broadcast to multiple subscribers across different instances, and handled reliably even when network listeners fail. The methods confirm features like history persistence, filtering subscriptions, and bidirectional communication between stream instances.*


### test_send_event_persists (method, L219-L226, parent: TestRedisStream)

> *Summary: This test verifies that an event sent to a Redis stream is correctly persisted. It sends a `ToolCallEvent` and then asserts that the stream's retrieved history contains exactly one matching event.*


### test_send_notifies_subscribers (method, L228-L241, parent: TestRedisStream)

> *Summary: This test verifies that sending an event to a Redis stream correctly notifies all subscribed listeners. It subscribes a callback, sends a `ToolCallEvent`, and asserts that exactly one notification matching the sent event's name is received.*


### test_send_multiple_events (method, L243-L254, parent: TestRedisStream)

> *Summary: This test verifies that sending multiple distinct events to a Redis stream results in all events being recorded. It sends one `ToolCallEvent` and one `ModelMessage`, then asserts the stream history contains exactly two entries.*


### test_history_persists_across_instances (method, L256-L267, parent: TestRedisStream)

> *Summary: This test verifies that event history persists across multiple instances of a Redis stream interface. It sends an event to one stream instance and then retrieves the complete event log from a newly created, but identically configured, second instance.*


### test_no_duplicate_persistence (method, L269-L283, parent: TestRedisStream)

> *Summary: This test verifies that events are persisted exactly once by sending an event to a Redis stream instance and then asserting the history contains only one entry, even when two identical stream objects are created for the same prefix and ID. It confirms the persistence mechanism prevents duplicate recording of sent data.*


### test_cross_instance_pubsub (method, L285-L304, parent: TestRedisStream)

> *Summary: This test verifies that published events on one Redis stream instance are successfully received by a subscriber connected to another instance using the same prefix. It sends a `ToolCallEvent` via `stream1` and asserts that `stream2` captures exactly one matching event after a short delay.*


### test_bidirectional_pubsub (method, L306-L334, parent: TestRedisStream)

> *Summary: This test verifies bidirectional communication between two instances sharing the same Redis stream prefix. It sends messages from both streams and asserts that each instance successfully receives its own message plus the message sent by the other instance, while also checking the total event history.*


### test_where_filter_with_pubsub (method, L336-L349, parent: TestRedisStream)

> *Summary: This test verifies that a stream correctly filters events when using pub/sub delivery. It subscribes to `ToolCallEvent`s, sends both a matching and non-matching event, and asserts that only the intended `ToolCallEvent` is captured by the listener.*


### test_multiple_subscribers_same_instance (method, L351-L368, parent: TestRedisStream)

> *Summary: This test verifies that a single stream instance correctly broadcasts events to multiple registered subscribers. It sends one event and asserts that all three distinct callback lists receive exactly one copy of the event.*


### test_local_dispatch_survives_listener_failure (method, L370-L390, parent: TestRedisStream)

> *Summary: This test verifies that local event dispatch continues to function even after the primary pub/sub listener task has been intentionally cancelled. It sends an event while the listener is down, asserting that the locally dispatched event is successfully received by the subscription callback.*


### TestBinaryRoundTrip (class, L393-L466)

> *Summary: This test suite verifies that various event types—including those containing raw binary data (like images), Gemini tool calls, Anthropic tool uses, and OpenAI reasoning events—persist correctly when stored in Redis and retrieved later. It ensures the integrity of complex nested structures across different provider-specific event formats during a round trip.*


### test_image_input_round_trip (method, L396-L406, parent: TestBinaryRoundTrip)

> *Summary: This test verifies that raw byte data from an `ImageInput` object is correctly persisted and retrieved from Redis storage. It serializes a sample PNG byte string into the storage and asserts that the retrieved object contains the exact original bytes as a `bytes` type.*


### test_gemini_server_tool_call_event (method, L408-L426, parent: TestBinaryRoundTrip)

> *Summary: This test verifies that a `GeminiServerToolCallEvent` containing a Google GenAI `Part` object is correctly stored and retrieved from Redis. It asserts that the retrieved event retains its structure, specifically confirming the presence and content of the embedded text part.*


### test_anthropic_server_tool_call_event (method, L428-L447, parent: TestBinaryRoundTrip)

> *Summary: This test verifies that an `AnthropicServerToolCallEvent` correctly serializes and deserializes a specific tool use block structure using Redis storage. It creates an event, saves it to the stream history, and then retrieves it to assert its content matches the original input.*


### test_openai_reasoning_event (method, L449-L466, parent: TestBinaryRoundTrip)

> *Summary: This test verifies that an `OpenAIReasoningEvent` persists correctly through storage operations. It serializes a specific reasoning event into Redis and then retrieves it to assert that the object type and its internal item details are preserved upon retrieval.*

