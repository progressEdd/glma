# test/beta/network/test_discussion.py

12 function(s): _agent, _scripted_agent, _make_rejecter, test_default_discussion_adapter_registered_on_open, test_discussion_validate_create_rejects_unsupported_ordering, test_discussion_5_way_handshake_transitions_to_active, test_discussion_round_robin_advances_through_participants, test_discussion_rejects_out_of_turn_send, test_discussion_partial_reject_fails_channel, test_discussion_hydrate_refolds_round_robin_state and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _scripted_agent | function |  |
| _make_rejecter | function |  |
| test_default_discussion_adapter_registered_on_open | function |  |
| test_discussion_validate_create_rejects_unsupported_ordering | function |  |
| test_discussion_5_way_handshake_transitions_to_active | function |  |
| test_discussion_round_robin_advances_through_participants | function |  |
| test_discussion_rejects_out_of_turn_send | function |  |
| test_discussion_partial_reject_fails_channel | function |  |
| test_discussion_hydrate_refolds_round_robin_state | function |  |
| test_discussion_llm_driven_round_robin_3_way | function |  |
| _make_auto_acker | function |  |

## Chunks

### _agent (function, L58-L59)

> *Summary: Creates and returns an `Agent` instance, configuring it using a provided name and a set of event objects passed as variable arguments.*


### _scripted_agent (function, L62-L63)

> *Summary: Creates an `Agent` instance configured with a `ScriptedConfig`, using the provided name and a variable number of reply strings as configuration parameters.*


### _make_rejecter (function, L66-L87)

> *Summary: Creates and returns an asynchronous handler function that intercepts incoming envelopes. This handler specifically checks for `EV_CHANNEL_INVITE` events and sends a corresponding rejection envelope back to the sender using the provided client.*


### test_default_discussion_adapter_registered_on_open (function, L91-L97)

> *Summary: This test verifies that the default `DiscussionAdapter` is automatically registered when opening a `Hub`. It initializes a memory store and checks if an adapter matching the discussion type and version exists within the opened hub instance.*


### test_discussion_validate_create_rejects_unsupported_ordering (function, L101-L123)

> *Summary: This test verifies that attempting to create a discussion channel with an unsupported ordering mechanism, specifically `"dynamic"`, raises a `ProtocolError`. It sets up two agents and then calls the hub's creation method while asserting the expected error is thrown for invalid configuration.*


### test_discussion_5_way_handshake_transitions_to_active (function, L127-L167)

> *Summary: This test verifies that a discussion channel successfully transitions to the `ACTIVE` state when five participants auto-acknowledge an invitation. It confirms all expected participants are present, checks the event log for correct invite and acknowledgment counts, and validates the initial speaker order within the channel's internal state.*


### test_discussion_round_robin_advances_through_participants (function, L171-L245)

> *Summary: This test verifies that a discussion channel configured with round-robin ordering correctly cycles through participants in sequence. It simulates manual message sending from Alice, Bob, and Carol to confirm the expected next speaker advances sequentially and wraps around after completing a full cycle.*


### test_discussion_rejects_out_of_turn_send (function, L249-L283)

> *Summary: This test verifies that the system rejects messages sent out of sequence when round-robin ordering is enforced on a discussion channel. It simulates three agents joining a channel and asserts that an attempt by one agent to send a message before others in turn raises a `ProtocolError`.*


### test_discussion_partial_reject_fails_channel (function, L287-L318)

> *Summary: This test verifies that if any participant rejects an invitation during a discussion handshake, the entire channel opening process fails with a `ProtocolError`. It sets up three clients and configures one client to reject all incoming invites before attempting to open a multi-party discussion involving all three.*


### test_discussion_hydrate_refolds_round_robin_state (function, L322-L377)

> *Summary: This test verifies that the round-robin speaking order is correctly persisted and recovered when a discussion hub is closed and reopened against the same persistent store. It initializes three agents, starts a discussion with Alice opening it to Bob and Carol, tears down the hub, and then asserts that the reloaded state correctly identifies Bob as the next expected speaker.*


### test_discussion_llm_driven_round_robin_3_way (function, L381-L440)

> *Summary: This test verifies a three-way, round-robin discussion flow driven by LLMs. It initializes agents and opens a channel configured for round-robin ordering, then asserts that the expected sequence of text messages (Alice 1, Bob 1, Carol 1, Alice 2) is correctly exchanged before halting based on agent script exhaustion.*


### _make_auto_acker (function, L443-L464)

> *Summary: Creates and returns an asynchronous handler function that automatically sends a channel invite acknowledgment (`EV_CHANNEL_INVITE_ACK`) if the received envelope is an invitation, otherwise it silently ignores the message. This utility is designed for tests requiring handshake completion without executing full LLM logic.*

