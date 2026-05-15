# test/beta/network/test_adapter_tools.py

10 function(s): _agent, test_plugin_does_not_attach_say, test_consulting_tools_for_gates_by_turn, test_conversation_tools_for_always_offers_say, test_discussion_tools_for_gates_by_round_robin, test_workflow_tools_for_returns_empty, test_build_text_envelope_default_shape, test_build_packet_envelope_with_handoff, test_build_packet_envelope_with_context_set, test_channels_open_with_seed_message.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_plugin_does_not_attach_say | function |  |
| test_consulting_tools_for_gates_by_turn | function |  |
| test_conversation_tools_for_always_offers_say | function |  |
| test_discussion_tools_for_gates_by_round_robin | function |  |
| test_workflow_tools_for_returns_empty | function |  |
| test_build_text_envelope_default_shape | function |  |
| test_build_packet_envelope_with_handoff | function |  |
| test_build_packet_envelope_with_context_set | function |  |
| test_channels_open_with_seed_message | function |  |

## Chunks

### _agent (function, L39-L40)

> *Summary: Creates an `Agent` instance using a provided name and initializes its configuration with a variable number of string replies. This function constructs the agent object for testing purposes.*


### test_plugin_does_not_attach_say (function, L47-L60)

> *Summary: This test verifies that a registered agent does not automatically gain the "say" tool when interacting with a local hub setup. It initializes necessary components, registers an agent, and asserts the absence of specific tools while confirming the presence of expected identity-level tools.*


### test_consulting_tools_for_gates_by_turn (function, L67-L90)

> *Summary: This test verifies that a consulting adapter correctly determines available tools based on the current turn in a communication channel. It asserts that the initiator receives the "say" tool, while the respondent has no tools when their turn is not active.*


### test_conversation_tools_for_always_offers_say (function, L94-L112)

> *Summary: This test verifies that a `ConversationAdapter` correctly identifies the available tools for two agents in a conversation channel. It asserts that both Alice and Bob are presented with only the "say" tool when queried using their respective agent IDs, channel metadata, and current state.*


### test_discussion_tools_for_gates_by_round_robin (function, L116-L145)

> *Summary: This test verifies that a discussion adapter correctly assigns tools based on round-robin scheduling within a communication channel. It initializes agents and opens a "discussion" channel, then asserts that only the creator agent initially receives the "say" tool while others receive none.*


### test_workflow_tools_for_returns_empty (function, L149-L162)

> *Summary: This test verifies that when no workflow channel is provided, the `WorkflowAdapter` returns an empty list of tools for a registered agent. It sets up a minimal environment using in-memory storage and client connections to execute this check.*


### test_build_text_envelope_default_shape (function, L168-L178)

> *Summary: This test verifies the `build_text_envelope` method by providing a channel ID, sender ID, text content, and audience list as input. It asserts that the resulting envelope correctly contains the expected event type (`EV_TEXT`), data payload, and audience members.*


### test_build_packet_envelope_with_handoff (function, L181-L192)

> *Summary: This test verifies that the `build_packet_envelope` method correctly constructs a packet envelope when a handoff is specified as input. It asserts that the resulting envelope contains the correct event type, body content, and structured routing information detailing the handoff target and reason.*


### test_build_packet_envelope_with_context_set (function, L195-L204)

> *Summary: This test verifies that the `build_packet_envelope` method correctly constructs a packet envelope when context data is provided as input. It asserts that the resulting envelope has the correct event type and that the supplied context dictionary is accurately placed within the event data.*


### test_channels_open_with_seed_message (function, L211-L260)

> *Summary: This test verifies that a channel opens with the specified seed message when an agent requests it via a tool call. It sets up two clients, configures one agent to issue a `channels(open, ...)` call, and then asserts that the resulting channel's event log contains the expected "kickoff" text envelope.*

