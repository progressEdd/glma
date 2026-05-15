# test/beta/tools/test_persistent_stream.py

4 function(s): storage, parent_stream, ctx, _make_agent. 1 class(es): TestPersistentStream. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| storage | function |  |
| parent_stream | function |  |
| ctx | function |  |
| _make_agent | function |  |
| TestPersistentStream | class |  |

## Chunks

### storage (function, L16-L17)

> *Summary: Instantiates and returns a `MemoryStorage` object, providing an in-memory implementation for data persistence testing.*


### parent_stream (function, L21-L22)

> *Summary: Creates a new `MemoryStream` instance, initializing it with the provided `MemoryStorage`. This function acts as a factory to wrap storage within a stream object.*


### ctx (function, L26-L27)

> *Summary: Creates a new `Context` object, initializing it with an existing `MemoryStream` as its stream and an empty dictionary for its dependencies. This function serves to wrap a parent stream into a context structure.*


### _make_agent (function, L30-L33)

> *Summary: Creates and returns a mock object configured to represent an agent, setting its `name` attribute based on the provided string input. This utility function is used internally for testing purposes.*


### TestPersistentStream (class, L36-L90)

> *Summary: These tests verify the behavior of a persistent stream factory by asserting that it produces `MemoryStream` objects, maintains consistent IDs for repeated calls with the same inputs, generates unique IDs for different agents or contexts, and correctly integrates storage backends and dependency tracking within the execution context.*


### test_returns_memory_stream (method, L37-L43, parent: TestPersistentStream)

> *Summary: This test verifies that the stream factory returns an instance of `MemoryStream` when provided with an agent and context. It executes the factory function to obtain the result and asserts its type.*


### test_reuses_same_stream_id_on_second_call (method, L45-L52, parent: TestPersistentStream)

> *Summary: This test verifies that calling the stream factory twice with the same agent and context results in both returned streams sharing the identical ID. It confirms stream identity persistence across sequential calls.*


### test_different_agents_get_different_streams (method, L54-L62, parent: TestPersistentStream)

> *Summary: This test verifies that distinct agents receive unique streams from the persistent stream factory. It instantiates two agents and calls the factory with each agent to confirm their resulting stream IDs are different.*


### test_stores_stream_id_in_dependencies (method, L64-L70, parent: TestPersistentStream)

> *Summary: This test verifies that the generated stream ID is correctly registered within the context's dependencies map. It initializes a persistent stream and asserts that its unique identifier matches the expected entry in `ctx.dependencies`.*


### test_uses_parent_storage_backend (method, L72-L78, parent: TestPersistentStream)

> *Summary: This test verifies that the created stream utilizes the provided `MemoryStorage` instance for its history. It instantiates a stream using a factory and asserts that the stream's internal history points to the input storage object.*


### test_independent_contexts_get_independent_streams (method, L80-L90, parent: TestPersistentStream)

> *Summary: This test verifies that two separate contexts, even when sharing the same underlying storage, produce distinct persistent streams. It confirms that calling the stream factory with different context instances results in uniquely identified streams.*

