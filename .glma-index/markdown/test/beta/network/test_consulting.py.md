# test/beta/network/test_consulting.py

10 function(s): _agent, test_consulting_handshake_transitions_to_active, test_consulting_full_flow_auto_closes, test_consulting_rejects_out_of_order_send, test_consulting_rejects_send_after_complete, test_hub_hydrate_refolds_active_channel, test_consulting_invite_timeout_when_no_handler, _silent_handler, test_default_consulting_adapter_registered_on_open, test_delegate_tool_end_to_end.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_consulting_handshake_transitions_to_active | function |  |
| test_consulting_full_flow_auto_closes | function |  |
| test_consulting_rejects_out_of_order_send | function |  |
| test_consulting_rejects_send_after_complete | function |  |
| test_hub_hydrate_refolds_active_channel | function |  |
| test_consulting_invite_timeout_when_no_handler | function |  |
| _silent_handler | function |  |
| test_default_consulting_adapter_registered_on_open | function |  |
| test_delegate_tool_end_to_end | function |  |

## Chunks

### _agent (function, L45-L46)

> *Summary: Creates and returns an `Agent` instance, configuring it using a `TestConfig` derived from the provided name and any subsequent event objects.*


### test_consulting_handshake_transitions_to_active (function, L50-L76)

> *Summary: This test verifies the successful transition of a consulting channel to an active state after participants are registered and one initiates the channel opening process. It confirms that the necessary invitation, acknowledgment, and opened events are recorded in the Write-Ahead Log (WAL).*


### test_consulting_full_flow_auto_closes (function, L80-L121)

> *Summary: This test simulates a complete consulting interaction where an initiator sends a prompt to a respondent via a dedicated channel. It verifies that the channel automatically closes with a specific reason, and confirms the sequence of text messages exchanged between the two registered agents are correctly recorded in the Write-Ahead Log (WAL).*


### test_consulting_rejects_out_of_order_send (function, L125-L152)

> *Summary: This test verifies that a respondent agent is prevented from sending messages on a consulting channel before the initiator has sent its first envelope. It sets up two agents, establishes a channel, and asserts that attempting to post an out-of-order message raises a `ProtocolError`.*


### test_consulting_rejects_send_after_complete (function, L156-L193)

> *Summary: This test verifies that the system rejects any message sent to a channel after it has been closed. It sets up two agents, initiates a consulting channel between them, waits for the channel to close, and then asserts that attempting to post an envelope to the closed channel raises a `ProtocolError`.*


### test_hub_hydrate_refolds_active_channel (function, L197-L233)

> *Summary: This test verifies that channel state persists across a hub restart by closing and reopening the hub against the same persistent store. It confirms that after reloading, the system correctly reconstructs the adapter's internal state for an active consulting channel, reflecting that one party has initiated but not yet responded.*


### test_consulting_invite_timeout_when_no_handler (function, L237-L262)

> *Summary: This test verifies that an invitation fails with a protocol error if the recipient lacks an auto-acknowledgment handler. It sets up two clients, registers one to ignore invites, and then attempts to open a consulting session from the other client.*


### _silent_handler (function, L265-L266)

> *Summary: This asynchronous function accepts an `Envelope` object and performs no operations, serving as a silent placeholder specifically for testing invitation timeouts.*


### test_default_consulting_adapter_registered_on_open (function, L270-L276)

> *Summary: This test verifies that the default `ConsultingAdapter` is automatically registered when opening a knowledge store via `Hub.open`. It asserts that an adapter matching the "consulting" service at version 1 exists within the opened hub instance.*


### test_delegate_tool_end_to_end (function, L280-L322)

> *Summary: This test simulates an end-to-end delegation workflow where one agent (Alice) uses a `delegate` tool to query another agent (Bob). It verifies that the entire chain—including receiving Bob's response and Alice incorporating it into her final output—executes successfully without making actual external LLM calls.*

