# test/beta/network/test_human_client.py

20 function(s): _agent, test_register_human_stamps_kind_and_id, test_register_human_with_default_resume, test_register_rejects_human_kind, test_register_human_rejects_non_human_kind, test_list_agents_filter_by_kind, test_consulting_human_responds_to_agent, test_pull_surface_returns_envelopes_in_order, test_envelopes_iterator_streams_until_disconnect, test_callback_exception_does_not_break_dispatch and 10 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_register_human_stamps_kind_and_id | function |  |
| test_register_human_with_default_resume | function |  |
| test_register_rejects_human_kind | function |  |
| test_register_human_rejects_non_human_kind | function |  |
| test_list_agents_filter_by_kind | function |  |
| test_consulting_human_responds_to_agent | function |  |
| test_pull_surface_returns_envelopes_in_order | function |  |
| test_envelopes_iterator_streams_until_disconnect | function |  |
| test_callback_exception_does_not_break_dispatch | function |  |
| test_human_initiates_consulting | function |  |
| test_discussion_round_robin_with_human | function |  |
| test_receive_chunk_is_noop | function |  |
| test_post_envelope_after_disconnect_raises | function |  |
| test_disconnect_wakes_blocked_next_envelope | function |  |
| test_disconnect_wakes_blocked_envelopes_iterator | function |  |
| test_disconnect_wakes_concurrent_pull_consumers | function |  |
| test_wait_for_channel_event_wakes_on_disconnect | function |  |
| test_disconnect_idempotent | function |  |
| _id_for | function |  |

## Chunks

### _agent (function, L34-L35)

> *Summary: Creates an `Agent` instance using a provided name and constructs a `TestConfig` object from any subsequent string arguments. This function serves to initialize test agents with specific configurations derived from input replies.*


### test_register_human_stamps_kind_and_id (function, L39-L57)

> *Summary: This test verifies the registration of a new human client by initializing necessary components and calling `register_human` with passport and resume data. It asserts that the returned object is correctly typed, has the "human" kind stamped on its passport, and retains the provided summary information.*


### test_register_human_with_default_resume (function, L61-L71)

> *Summary: This test verifies that registering a new human via the client results in the default `Resume` object being assigned to the registered entity. It sets up an in-memory knowledge store and communication links before performing the registration and asserting the state.*


### test_register_rejects_human_kind (function, L75-L89)

> *Summary: This test verifies that attempting to register an agent with the "human" kind fails by raising a `ValueError`. It sets up a local communication environment using in-memory storage and asserts the expected rejection when calling the registration method.*


### test_register_human_rejects_non_human_kind (function, L93-L103)

> *Summary: This test verifies that attempting to register an entity with a non-human `kind` (specifically "agent") using the client raises a `ValueError`. It sets up in-memory components and asserts the expected rejection behavior during registration.*


### test_list_agents_filter_by_kind (function, L107-L125)

> *Summary: This test verifies agent listing functionality by initializing a local hub and client, registering one automated agent and one human user. It then asserts that the `list_agents` method correctly returns subsets of registered entities based on specified kinds ("agent" or "human") or all entities.*


### test_consulting_human_responds_to_agent (function, L129-L170)

> *Summary: This test simulates an agent initiating a consulting session with a human reviewer via a shared communication hub. It verifies that when the human replies to the initial prompt, the channel correctly closes and captures the human's response.*


### test_pull_surface_returns_envelopes_in_order (function, L174-L200)

> *Summary: This test verifies that a client receives substantive messages in the correct sequence after an initial handshake. It sets up two clients, initiates a conversation, sends a text message from one client, and asserts that the other client successfully retrieves that specific text envelope.*


### test_envelopes_iterator_streams_until_disconnect (function, L204-L234)

> *Summary: This test verifies that an envelope iterator streams messages until a disconnection event occurs. It sets up two clients, sends two text messages from one client to the other, and asserts that the receiving client's iterator captures both messages before disconnecting.*


### test_callback_exception_does_not_break_dispatch (function, L238-L278)

> *Summary: This test verifies that an exception raised within a registered callback handler does not prevent subsequent messages from being processed by the client. It simulates communication between two clients, intentionally triggering an error in one handler while ensuring expected data is still received via another handler.*


### test_human_initiates_consulting (function, L282-L313)

> *Summary: This test simulates a human client initiating a consulting session with an agent, verifying that the agent successfully replies to the human's message. It sets up communication channels between two clients and asserts that the expected reply is received by the human after sending an initial status check.*


### test_discussion_round_robin_with_human (function, L317-L380)

> *Summary: This test simulates a round-robin discussion where a human participant only replies when the system indicates it is their turn, mimicking realistic UI behavior. It initializes agents and a human client within a shared hub, sends an initial message, waits for three total text messages, and asserts that the human agent correctly contributed to the conversation sequence.*


### test_receive_chunk_is_noop (function, L384-L397)

> *Summary: This test verifies that calling `receive_chunk` on a registered human client does not raise an exception, simulating the reception of streaming data chunks. It sets up a local communication environment and calls the method with dummy objects to confirm expected non-error behavior.*


### test_post_envelope_after_disconnect_raises (function, L401-L413)

> *Summary: This test verifies that attempting to send a message after a client has disconnected results in a `RuntimeError`. It sets up a communication environment, registers and then disconnects a human client, finally asserting the expected error upon sending data.*


### test_disconnect_wakes_blocked_next_envelope (function, L417-L440)

> *Summary: This test verifies that a consumer waiting for the next envelope is correctly unblocked when the associated human disconnects. It sets up a client, registers a human, initiates a disconnection shortly after, and asserts that calling `next_envelope` raises a "disconnected" error within a timeout.*


### test_disconnect_wakes_blocked_envelopes_iterator (function, L444-L467)

> *Summary: This test verifies that iterating over a human's envelope stream terminates immediately when the client disconnects. It sets up a communication environment, starts consuming envelopes in a background task, forces a disconnection, and asserts that no envelopes were processed before the consumer task completes.*


### test_disconnect_wakes_concurrent_pull_consumers (function, L471-L494)

> *Summary: This test verifies that multiple consumers waiting on a pull queue are all woken up upon a client disconnection. It achieves this by registering several concurrent tasks to await the next envelope, then disconnecting the client and asserting that each task raises a "disconnected" `RuntimeError`.*


### test_wait_for_channel_event_wakes_on_disconnect (function, L498-L523)

> *Summary: This test verifies that a channel waiter wakes up when the associated human client disconnects. It sets up a communication environment, registers a human, and then asserts that calling `wait_for_channel_event` raises a `RuntimeError` upon an intentional disconnection.*


### test_disconnect_idempotent (function, L527-L547)

> *Summary: This test verifies that calling a disconnect method multiple times on a registered human client has no adverse effect, ensuring idempotency. It confirms that only one sentinel is enqueued upon disconnection and that subsequent calls to retrieve the next envelope fail as expected.*


### _id_for (function, L553-L556)

> *Summary: Retrieves the unique agent ID for a given name by first fetching the corresponding agent object from the `HubClient`. It asserts that an agent ID exists before returning it as a string.*

