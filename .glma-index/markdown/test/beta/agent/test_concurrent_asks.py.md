# test/beta/agent/test_concurrent_asks.py

1 class(es): TestSharedStreamSerialization. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestSharedStreamSerialization | class |  |

## Chunks

### TestSharedStreamSerialization (class, L25-L85)

> *Summary: Verifies that concurrent requests to a shared stream do not result in overlapping execution turns, while confirming that distinct streams can safely overlap. It uses asynchronous tools and agents to test serialization behavior under load.*


### test_same_stream_turns_do_not_overlap (method, L26-L56, parent: TestSharedStreamSerialization)

> *Summary: This test verifies that concurrent requests to an agent using the same memory stream do not result in overlapping execution turns. It achieves this by running two `agent.ask` calls concurrently while monitoring an internal counter to ensure only one task is active at any given time.*


### test_distinct_streams_may_overlap (method, L58-L85, parent: TestSharedStreamSerialization)

> *Summary: This test verifies that two concurrent agent requests, each utilizing a shared gated tool, will correctly synchronize and complete only after both have reached the gate condition. It asserts that the internal counter confirms both asynchronous streams successfully passed through the synchronized step.*

