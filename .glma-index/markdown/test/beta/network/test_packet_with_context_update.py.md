# test/beta/network/test_packet_with_context_update.py

2 function(s): _agent, _packet. 1 class(es): TestPacketWithContextUpdate. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _packet | function |  |
| TestPacketWithContextUpdate | class |  |

## Chunks

### _agent (function, L45-L46)

> *Summary: Creates and returns an `Agent` instance, configuring it with a specific name and a set of replies passed as variable arguments. The input is the agent's name string and zero or more reply strings, resulting in a fully configured `Agent` object.*


### _packet (function, L49-L82)

> *Summary: Constructs an `Envelope` object representing a network packet by packaging routing information and context updates. It accepts identifiers for the channel and sender, along with optional parameters to define the message's intent (e.g., tool usage, target), variable modifications, and content body.*


### TestPacketWithContextUpdate (class, L86-L291)

> *Summary: This test suite verifies how context updates (setting or deleting variables) within an `EV_PACKET` are processed before the workflow's next speaker selection logic runs. It confirms that setting a variable triggers immediate rule matching based on the new value, while deleting a variable can cause transitions to terminate or change state accordingly.*


### test_set_applied_before_select_next (method, L90-L141, parent: TestPacketWithContextUpdate)

> *Summary: This test verifies that a `ContextEquals` transition correctly triggers when context variables are updated *before* the next agent selection occurs within the same processing fold. It sends a packet containing a context update, asserts the state reflects this new context, and confirms the router selects the appropriate target based on the updated context.*


### test_delete_applied_before_select_next (method, L143-L196, parent: TestPacketWithContextUpdate)

> *Summary: This test verifies that deleting a context variable atomically with a packet causes the workflow to terminate immediately if a transition rule depends on that variable being null. It sets up two agents, initiates a channel with a specific context, sends a packet instructing the deletion of the "route" variable, and asserts that the state transitions to termination based on the cleared context.*


### test_packet_without_context_updates_unchanged (method, L198-L243, parent: TestPacketWithContextUpdate)

> *Summary: This test verifies that an `EV_PACKET` sent with empty context updates maintains the existing channel state and follows standard routing rules. It sets up two agents, initiates a workflow from Alice to Bob, sends a packet, and asserts that the channel's context variables remain unchanged while the expected next speaker is correctly set to Bob.*


### test_dynamic_handoff_target_supersedes_select_next (method, L245-L291, parent: TestPacketWithContextUpdate)

> *Summary: When sending a packet with a pre-resolved `routing.target`, the system prioritizes this explicit target over any routing rules defined in the transition graph. This test verifies that setting `target=b.agent_id` causes the channel's expected next speaker to immediately become agent 'b', bypassing the graph's default path to agent 'a'.*

