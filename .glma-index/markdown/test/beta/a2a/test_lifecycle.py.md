# test/beta/a2a/test_lifecycle.py

2 function(s): _make_spy_factory, test_streamed_chunks_not_duplicated_in_final_message. 6 class(es): _SpyAsyncClient, _AlwaysFailingExecutor, TestHttpxLifecycle, _ChunkingScript, _ChunkingScriptClient, TestCardImmutability. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _SpyAsyncClient | class |  |
| _make_spy_factory | function |  |
| _AlwaysFailingExecutor | class |  |
| TestHttpxLifecycle | class |  |
| _ChunkingScript | class |  |
| _ChunkingScriptClient | class |  |
| test_streamed_chunks_not_duplicated_in_final_message | function |  |
| TestCardImmutability | class |  |

## Chunks

### _SpyAsyncClient (class, L29-L34)

> *Summary: This class inherits from `httpx.AsyncClient` to track the number of times an asynchronous client is closed. It overrides the `aclose` method to increment a class-level counter upon execution before calling the parent's close method.*


### aclose (method, L32-L34, parent: _SpyAsyncClient)

> *Summary: Increments an internal counter for the current type and then calls the parent's asynchronous close method. This ensures proper lifecycle tracking during resource cleanup.*


### _make_spy_factory (function, L37-L43)

> *Summary: Creates and returns a function that generates an asynchronous client configured to spy on requests made to a specific URL within the provided server instance. This factory encapsulates the necessary transport setup for monitoring HTTP interactions.*


### _AlwaysFailingExecutor (class, L46-L60)

> *Summary: This executor simulates a failure by immediately submitting a task and then explicitly calling a `failed()` method on its updater. It accepts a `RequestContext` containing the message and an `EventQueue`, producing no direct output other than triggering the simulated failure within the event queue system.*


### execute (method, L47-L57, parent: _AlwaysFailingExecutor)

> *Summary: This method processes an incoming message from the request context to initiate a background task lifecycle. It generates unique IDs for the task and context, enqueues a "submitted" event, and then runs a dedicated updater to simulate the task's execution and subsequent failure.*


### cancel (method, L59-L60, parent: _AlwaysFailingExecutor)

> *Summary: This method accepts a `RequestContext` and an `EventQueue` to signal cancellation. It currently performs no operations and returns nothing.*


### TestHttpxLifecycle (class, L64-L100)

> *Summary: These tests verify that the HTTPX client associated with an agent is properly closed under various scenarios: after a successful request, when a task fails, and confirming that the close operation is idempotent. The tests use a spy client to assert that `aclose()` is called at least once in both success and failure cases, while only being called once if invoked multiple times.*


### test_client_closes_httpx_after_successful_ask (method, L65-L73, parent: TestHttpxLifecycle)

> *Summary: This test verifies that the HTTPX client is properly closed after a successful request exchange between agents. It initializes a server and client, executes an `ask` operation, and asserts that the underlying spy client's close method was called at least once.*


### test_client_closes_httpx_when_task_fails (method, L75-L90, parent: TestHttpxLifecycle)

> *Summary: This test verifies that the HTTP client is properly closed when an asynchronous task fails during execution. It sets up a failing server and asserts that the underlying `httpx` client's close method was called at least once after the expected failure.*


### test_aclose_is_idempotent (method, L92-L100, parent: TestHttpxLifecycle)

> *Summary: This test verifies that the `aclose` method on an A2A client is idempotent by asserting it is only called once, even when invoked twice consecutively. It initializes a mocked HTTP client and checks the call count after two sequential calls to `aclose()`.*


### _ChunkingScript (class, L103-L114)

> *Summary: This configuration object holds a sequence of string chunks and provides methods to clone itself or instantiate a client capable of processing those chunks. It currently raises an error if asked to create a file-specific client.*


### __init__ (method, L104-L105, parent: _ChunkingScript)

> *Summary: Initializes the object by storing a sequence of string chunks as an internal list. It accepts one input argument, `chunks`, which is converted to a mutable list for subsequent use.*


### copy (method, L107-L108, parent: _ChunkingScript)

> *Summary: Returns a reference to the current instance, effectively creating a shallow copy of the object. This method allows for cloning without duplicating internal state.*


### create (method, L110-L111, parent: _ChunkingScript)

> *Summary: Instantiates and returns a `_ChunkingScriptClient` object, passing the instance's internal list of chunks as input. This method is responsible for creating the client interface based on existing chunk data.*


### create_files_client (method, L113-L114, parent: _ChunkingScript)

> *Summary: This method is intended to initialize or set up necessary files for a client, but currently raises `NotImplementedError` as its functionality has not been defined. It takes no inputs and returns nothing.*


### _ChunkingScriptClient (class, L117-L130)

> *Summary: This client streams a sequence of string chunks to the context, sending each one as a `ModelMessageChunk`. It then returns a final `ModelResponse` containing the concatenation of all input chunks.*


### __init__ (method, L118-L119, parent: _ChunkingScriptClient)

> *Summary: Initializes the object by storing a sequence of string chunks as an internal list. It accepts one input argument, `chunks`, which is converted into the instance's state.*


### __call__ (method, L121-L130, parent: _ChunkingScriptClient)

> *Summary: This method streams a sequence of message chunks to the provided context and then returns a final `ModelResponse` containing the concatenated full message. It accepts a sequence of base events and a context object as input.*


### test_streamed_chunks_not_duplicated_in_final_message (function, L134-L145)

> *Summary: This test verifies that when a server streams content in chunks, the final received message does not contain duplicate data. It sets up an A2A communication between a client configured for streaming and a server sending chunked responses, asserting the final content matches the expected string.*


### TestCardImmutability (class, L149-L196)

> *Summary: These tests verify that building server interfaces (JSONRPC, REST, and gRPC) using an input `Card` object does not mutate the original card's capabilities. Each test initializes a mock agent and server setup to confirm immutability across different transport protocols.*


### test_build_jsonrpc_does_not_mutate_input_card (method, L150-L164, parent: TestCardImmutability)

> *Summary: This test verifies that the `build_jsonrpc` method does not modify the input agent card object. It asserts that the state of the extended agent and push notification capabilities remains unchanged after calling the build function.*


### test_build_rest_does_not_mutate_input_card (method, L166-L180, parent: TestCardImmutability)

> *Summary: This test verifies that the `build_rest` method on an A2A server does not modify the input agent card object. It asserts that specific capabilities within the card remain unchanged after calling `server.build_rest()`.*


### test_build_grpc_does_not_mutate_input_card (method, L182-L196, parent: TestCardImmutability)

> *Summary: This test verifies that the `build_grpc` method does not modify the input agent card object. It initializes an agent and a card, then calls `build_grpc`, asserting that the card's capabilities remain unchanged after the operation.*

