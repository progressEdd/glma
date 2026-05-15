# test/beta/network/test_conversation.py

14 function(s): _agent, _scripted_agent, test_conversation_handshake_transitions_to_active, test_conversation_back_and_forth_multi_turn, test_conversation_explicit_close_terminates, test_conversation_rejects_send_from_non_participant, test_conversation_hydrate_refolds_active_channel, test_default_conversation_adapter_registered_on_open, test_windowed_summary_short_history_passes_through, test_windowed_summary_long_history_prepends_compaction_summary and 4 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _scripted_agent | function |  |
| test_conversation_handshake_transitions_to_active | function |  |
| test_conversation_back_and_forth_multi_turn | function |  |
| test_conversation_explicit_close_terminates | function |  |
| test_conversation_rejects_send_from_non_participant | function |  |
| test_conversation_hydrate_refolds_active_channel | function |  |
| test_default_conversation_adapter_registered_on_open | function |  |
| test_windowed_summary_short_history_passes_through | function |  |
| test_windowed_summary_long_history_prepends_compaction_summary | function |  |
| test_windowed_summary_respects_audience_visibility | function |  |
| _text_envelope | function |  |
| _two_party_metadata | function |  |
| _three_party_metadata | function |  |

## Chunks

### _agent (function, L57-L58)

> *Summary: Creates and returns an `Agent` instance, configuring it using a provided name and a set of event objects passed as variable arguments.*


### _scripted_agent (function, L61-L62)

> *Summary: Creates an `Agent` instance configured to follow a predefined script. It takes a name and a variable number of string replies to define the agent's conversational flow.*


### test_conversation_handshake_transitions_to_active (function, L66-L95)

> *Summary: This test verifies that initiating a conversation between two registered agents successfully transitions the channel state to `ACTIVE`. It confirms this by asserting the correct participants, checking for an empty pending acknowledgments list, and verifying the presence of specific handshake events in the Write-Ahead Log.*


### test_conversation_back_and_forth_multi_turn (function, L99-L148)

> *Summary: This test simulates a multi-turn, bidirectional conversation between two agents by setting up clients and registering scripted participants. It verifies that the exchange proceeds through four specific text messages in sequence and confirms the final state of the communication channel reflects the total turns and last speaker.*


### test_conversation_explicit_close_terminates (function, L152-L183)

> *Summary: This test verifies that explicitly closing a conversation channel immediately transitions it to the `CLOSED` state, regardless of ongoing activity. It confirms this by asserting the final state and then ensuring subsequent messages sent on the closed channel are rejected with a `ProtocolError`.*


### test_conversation_rejects_send_from_non_participant (function, L187-L216)

> *Summary: This test verifies that the system prevents sending messages to a conversation channel from an agent who is not listed as a participant. It sets up three agents, establishes a private chat between two of them, and then attempts to send a message from the third, non-participating agent, expecting a `ProtocolError`.*


### test_conversation_hydrate_refolds_active_channel (function, L220-L254)

> *Summary: This test verifies that when a conversation is opened and partially progressed, closing the hub and reopening it allows the system to correctly hydrate the channel's adapter state from the Write-Ahead Log (WAL). It confirms that the reopened hub accurately reflects the active state, including the turn count and last speaker, of the existing conversation.*


### test_default_conversation_adapter_registered_on_open (function, L258-L264)

> *Summary: This test verifies that the default `ConversationAdapter` is automatically registered when opening a `Hub` instance with a memory store. It asserts that an adapter matching the specified conversation type and version exists within the opened hub's adapters before closing it.*


### test_windowed_summary_short_history_passes_through (function, L268-L289)

> *Summary: This test verifies that when the conversation history is short relative to the window size, the summary projection returns the full transcript instead of a summarized version. It inputs a small list of message envelopes and asserts the output matches the original sequence of requests and messages.*


### test_windowed_summary_long_history_prepends_compaction_summary (function, L293-L316)

> *Summary: This test verifies that when the message history exceeds a defined window size, older messages are summarized into a `CompactionSummary` while recent messages remain as individual inputs. It asserts that the resulting projection contains one summary object and the specified number of verbatim recent message requests.*


### test_windowed_summary_respects_audience_visibility (function, L320-L341)

> *Summary: This test verifies that a windowed summary correctly filters out messages intended for other participants when projected from a specific user's perspective. Given a sequence of messages with varying visibility, it asserts the resulting projection only contains content visible to the target participant ("carol").*


### _text_envelope (function, L344-L360)

> *Summary: Creates an `Envelope` object representing a text message. It constructs the envelope using provided sender, recipient (or derived audience), and the message content, assigning a unique ID based on the sender and text.*


### _two_party_metadata (function, L363-L374)

> *Summary: Constructs a `ChannelMetadata` object representing an active two-party conversation. It takes the initiator and respondent IDs as input to define the participants within the metadata structure.*


### _three_party_metadata (function, L377-L390)

> *Summary: Constructs a `ChannelMetadata` object representing a conversation involving one initiator and multiple other participants. It takes the initiator's ID and a variable list of other participant IDs as input, returning a fully configured metadata structure.*

