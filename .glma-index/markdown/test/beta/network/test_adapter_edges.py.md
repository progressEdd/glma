# test/beta/network/test_adapter_edges.py

4 function(s): _agent, _make_metadata, test_validate_send_rejection_does_not_append_to_wal, test_hydrate_refolds_discussion_state_deterministically. 3 class(es): TestConsultingAdapter, TestConversationAdapter, TestDiscussionAdapter. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _make_metadata | function |  |
| TestConsultingAdapter | class |  |
| TestConversationAdapter | class |  |
| TestDiscussionAdapter | class |  |
| test_validate_send_rejection_does_not_append_to_wal | function |  |
| test_hydrate_refolds_discussion_state_deterministically | function |  |

## Chunks

### _agent (function, L45-L46)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `ScriptedConfig`.*


### _make_metadata (function, L49-L68)

> *Summary: Constructs a `ChannelMetadata` object using provided manifest data, creator ID, and a list of participants with assigned roles. It initializes the channel state to active and sets default timestamps for creation and joining.*


### TestConsultingAdapter (class, L71-L205)

> *Summary: This test suite verifies the edge case behavior of a consulting protocol adapter by testing validation rules for creating and sending messages, ensuring deterministic state folding across replays, and confirming the correct transition to a closed state upon completion. It uses `ConsultingAdapter` methods like `validate_create`, `validate_send`, `fold`, and `on_accepted` against various input scenarios.*


### test_validate_create_rejects_three_participants (method, L74-L86, parent: TestConsultingAdapter)

> *Summary: This test verifies that the adapter rejects creation requests when three participants are provided in the metadata. It asserts that calling `validate_create` with a configuration involving Alice (initiator), Bob (respondent), and Carol (participant) raises a `ProtocolError` matching "exactly 2".*


### test_validate_create_rejects_missing_respondent (method, L88-L99, parent: TestConsultingAdapter)

> *Summary: This test verifies that the adapter rejects creation if a required respondent is missing from the metadata input. It asserts that calling `validate_create` with specific participant data raises a `ProtocolError` containing "respondent".*


### test_validate_send_rejects_respondent_first (method, L101-L121, parent: TestConsultingAdapter)

> *Summary: This test verifies that the adapter rejects an outgoing message when a respondent attempts to send first. It simulates a scenario where Bob (the respondent) tries to send an envelope before Alice (the initiator), expecting a `ProtocolError`.*


### test_validate_send_rejects_after_both_replied (method, L123-L142, parent: TestConsultingAdapter)

> *Summary: This test verifies that attempting to send a message when both the initiator and respondent have already replied results in a `ProtocolError`. It uses a pre-configured adapter, metadata defining two participants, and a state indicating completion before calling `validate_send`.*


### test_fold_is_deterministic_under_replay (method, L144-L183, parent: TestConsultingAdapter)

> *Summary: This test verifies that applying a sequence of network events (envelopes) to an initial state results in the same final state when the process is replayed from scratch. It uses a `ConsultingAdapter` instance and asserts equality between two states derived by processing the identical input list twice.*


### test_on_accepted_returns_closed_after_both_replied (method, L185-L205, parent: TestConsultingAdapter)

> *Summary: When the adapter receives an accepted message from a respondent after the initiator has already sent, it transitions the channel to a closed state with the reason set to "consulting\_complete". This test verifies that `on_accepted` correctly handles this final reply scenario.*


### TestConversationAdapter (class, L208-L281)

> *Summary: These tests verify the `ConversationAdapter`'s behavior for validating message sends and processing conversation history. It ensures that sending messages from non-participants is rejected, correctly updates turn counts and speakers when folding text envelopes, and ignores protocol-specific envelopes during state folding.*


### test_validate_send_rejects_non_participant (method, L209-L227, parent: TestConversationAdapter)

> *Summary: This test verifies that the adapter rejects sending an envelope when the sender is not listed as a participant in the metadata. It asserts that calling `validate_send` with an external sender ID raises a `ProtocolError`.*


### test_fold_advances_turn_count_and_speaker (method, L229-L257, parent: TestConversationAdapter)

> *Summary: This test verifies that processing a sequence of communication envelopes correctly updates the conversation state. It confirms that after iterating through three distinct messages from Alice and Bob, the resulting state reflects a turn count of 3, identifies Alice as the last speaker, and records the final envelope ID.*


### test_fold_ignores_protocol_envelopes (method, L259-L281, parent: TestConversationAdapter)

> *Summary: This test verifies that the `ConversationAdapter`'s `fold` method ignores protocol envelopes when processing state transitions. It takes an existing state and a specific envelope (`EV_CHANNEL_OPENED`) as input, asserting that the resulting state remains unchanged.*


### TestDiscussionAdapter (class, L284-L389)

> *Summary: This test suite verifies the validation and folding logic of a discussion protocol adapter. It asserts that creation fails for unsupported configurations or solo participants, validates sending based on turn order, confirms round-robin speaker rotation wraps correctly, and ensures folding remains stable when encountering unknown senders.*


### test_validate_create_rejects_unknown_ordering (method, L285-L297, parent: TestDiscussionAdapter)

> *Summary: This test verifies that the adapter rejects creation requests when an unsupported ordering mechanism is specified in the metadata. It asserts that calling `validate_create` with a manifest containing `"ordering": "weighted"` raises a `ProtocolError`.*


### test_validate_create_rejects_solo (method, L299-L307, parent: TestDiscussionAdapter)

> *Summary: When validating a creation request with only one participant (the creator), the function asserts that a `ProtocolError` is raised because at least two participants are required for the operation. This test confirms the minimum participant requirement enforced by the adapter's validation logic.*


### test_validate_send_rejects_out_of_turn (method, L309-L330, parent: TestDiscussionAdapter)

> *Summary: This test verifies that the adapter rejects an outgoing message when the sender is not the expected next speaker according to the current discussion state. It simulates a scenario where "bob" attempts to send a text event while "alice" is designated as the next speaker, expecting a `ProtocolError`.*


### test_round_robin_rotation_wraps_after_n_turns (method, L332-L360, parent: TestDiscussionAdapter)

> *Summary: This test verifies that the round-robin speaker selection correctly cycles back to the initial participant after a full rotation. It simulates turns among three participants, asserting that the expected next speaker reverts to the first person after the last turn.*


### test_fold_with_unknown_sender_does_not_crash (method, L362-L389, parent: TestDiscussionAdapter)

> *Summary: When processing an envelope from a sender not listed in the participant order, this test verifies that the folding operation returns the input state unchanged. It uses a pre-configured adapter and initial state to simulate receiving an unknown message.*


### test_validate_send_rejection_does_not_append_to_wal (function, L393-L428)

> *Summary: When an agent attempts to send a message that violates protocol rules, this test verifies that the underlying Write-Ahead Log (WAL) remains unchanged. It confirms that a rejected envelope does not get appended to the WAL and that no record of the rejected content exists in the log afterward.*


### test_hydrate_refolds_discussion_state_deterministically (function, L432-L494)

> *Summary: This test verifies that the state of a discussion channel can be deterministically reconstructed after being closed and reopened across two separate Hub instances using a shared disk store. It simulates a multi-agent conversation, captures the live state, closes the system, reopens it with the same data, and asserts that the resulting state matches the original.*

