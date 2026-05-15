# test/beta/network/test_observability.py

21 function(s): _agent, test_listener_receives_agent_and_channel_events, test_listener_receives_envelope_posted, test_listener_receives_envelope_rejected_on_access_denied, test_listener_exception_does_not_break_dispatch, test_custom_arbiter_can_deny_send, test_default_arbiter_preserves_rule_based_behavior, test_resolve_unknown_audience_silent_drop_default, test_audit_subscribe_taps_live_stream, test_handler_exception_does_not_crash_channel and 11 more. 3 class(es): _RecordingListener, _DenyArbiter, _DenyAtDelegationDepth. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _RecordingListener | class |  |
| test_listener_receives_agent_and_channel_events | function |  |
| test_listener_receives_envelope_posted | function |  |
| test_listener_receives_envelope_rejected_on_access_denied | function |  |
| test_listener_exception_does_not_break_dispatch | function |  |
| _DenyArbiter | class |  |
| test_custom_arbiter_can_deny_send | function |  |
| test_default_arbiter_preserves_rule_based_behavior | function |  |
| test_resolve_unknown_audience_silent_drop_default | function |  |
| test_audit_subscribe_taps_live_stream | function |  |
| test_handler_exception_does_not_crash_channel | function |  |
| test_health_snapshot_shape | function |  |
| test_hub_logs_state_transitions | function |  |
| test_hub_logs_warning_on_rejection | function |  |
| test_multiple_bad_listeners_do_not_break_dispatch | function |  |
| test_base_hub_arbiter_allows_everything_by_default | function |  |
| _DenyAtDelegationDepth | class |  |
| test_custom_arbiter_authorize_send_overrides_rule_based | function |  |
| test_hub_health_on_populated_hub | function |  |
| test_widened_trap_catches_pre_ask_failures | function |  |
| test_register_human_duplicate_name_raises | function |  |
| test_passport_kind_rejects_typo_at_construction | function |  |
| test_replace_audit_log_swaps_listener_chain | function |  |

## Chunks

### _agent (function, L37-L38)

> *Summary: Creates an `Agent` instance using a provided name and constructs a `TestConfig` object from any subsequent string arguments. This function serves to initialize test agents with specific configurations derived from input replies.*


### _RecordingListener (class, L44-L75)

> *Summary: This listener class captures and stores various system events—such as posted/rejected envelopes, channel/agent activities, and task failures—by implementing specific callback methods from a base hub listener. It accumulates these event details into internal lists for later assertion during testing.*


### __init__ (method, L47-L54, parent: _RecordingListener)

> *Summary: Initializes an object to track various system events by setting up empty lists for recording envelope postings, rejections, channel/agent activities, turn failures, task events, and dispatch failures. These lists serve as internal buffers for observability data collection during testing.*


### on_envelope_posted (method, L56-L57, parent: _RecordingListener)

> *Summary: This method records the event type and sender ID of a posted envelope into an internal list. It accepts an `envelope` object and associated `metadata` as input to track posting activity.*


### on_envelope_rejected (method, L59-L60, parent: _RecordingListener)

> *Summary: Records the rejection of an incoming message by appending its event type and the name of the rejection reason to a list attribute. This method accepts an `envelope` object and a `reason` object as input.*


### on_channel_event (method, L62-L63, parent: _RecordingListener)

> *Summary: This method records an event by appending a tuple containing the event type and associated channel ID to an internal list. It accepts the `channel_id`, event `kind`, and event `payload` as inputs.*


### on_agent_event (method, L65-L66, parent: _RecordingListener)

> *Summary: This method records an event by appending a tuple containing the event type and agent ID to an internal list. It accepts the agent's identifier, the event category, and associated data as input.*


### on_turn_failed (method, L68-L69, parent: _RecordingListener)

> *Summary: Records a failed turn event by appending the channel ID, agent ID, and exception type name to an internal list. This method is called when a turn process encounters an error.*


### on_task_event (method, L71-L72, parent: _RecordingListener)

> *Summary: This method records a task event by appending the event type and associated task ID to an internal list. It accepts a `task_id`, an event `kind`, and an optional `payload` as input.*


### on_dispatch_failed (method, L74-L75, parent: _RecordingListener)

> *Summary: Records a dispatch failure by appending the event type and recipient ID to an internal list when a message delivery attempt fails. This method takes the failed envelope, recipient identifier, and the reason for the failure as input.*


### test_listener_receives_agent_and_channel_events (function, L79-L104)

> *Summary: This test verifies that a listener correctly captures agent registration and channel lifecycle events when two agents interact via a shared Hub. It simulates agent setup, channel creation/closing between them, and asserts the listener recorded the expected "registered," "created," "opened," and "closed" events.*


### test_listener_receives_envelope_posted (function, L108-L129)

> *Summary: This test verifies that a registered listener correctly receives an envelope when one agent sends a text message to another via the communication hub. It sets up clients, registers agents, establishes a conversation channel, and asserts at least one text event was captured by the listener.*


### test_listener_receives_envelope_rejected_on_access_denied (function, L133-L153)

> *Summary: This test verifies that an attempt to open a communication channel between two agents fails with an `AccessDeniedError` when one agent has an access control rule blocking inbound connections from the other. It sets up a local hub, registers clients, and then attempts to initiate a connection under restricted permissions.*


### test_listener_exception_does_not_break_dispatch (function, L157-L185)

> *Summary: This test verifies that an exception raised by one registered listener does not prevent other listeners from receiving dispatched events. It sets up a hub with both a failing and a successful listener, sends a message, and asserts the success listener processed the event despite the failure.*


### _DenyArbiter (class, L191-L212)

> *Summary: This class implements a denial arbiter that explicitly rejects all outgoing sends while allowing inbound messages and other operations like channel opening and registration. It serves as a test fixture to verify the functionality of the arbiter seam by enforcing strict send restrictions.*


### authorize_send (method, L194-L195, parent: _DenyArbiter)

> *Summary: This method immediately returns a `Deny` object with a custom reason. It accepts an envelope, sender, sender rule, and list of recipients as input but performs no actual authorization logic.*


### authorize_inbox (method, L197-L198, parent: _DenyArbiter)

> *Summary: This method unconditionally returns an `Allow` object when provided with an envelope, recipient, recipient rule, and pending state. It serves as a simple authorization check that always permits access.*


### authorize_dispatch (method, L200-L201, parent: _DenyArbiter)

> *Summary: This method unconditionally returns an `Allow` object when called with an envelope, sender, recipient, and a recipient rule. It serves as a simple authorization check that always permits the action.*


### authorize_channel_open (method, L203-L206, parent: _DenyArbiter)

> *Summary: This method unconditionally returns an `Allow` object. It accepts various parameters related to channel creation authorization, including manifests, creators, and associated rulesets.*


### authorize_register (method, L208-L209, parent: _DenyArbiter)

> *Summary: This method accepts a `passport`, `resume`, and `rule` as input to immediately return an `Allow()` object. It serves as a simple authorization check that always permits access without performing complex validation.*


### resolve_unknown_audience (method, L211-L212, parent: _DenyArbiter)

> *Summary: This asynchronous method accepts an `envelope` and a list of `unknown_ids`, returning `None` without performing any observable action. It serves as a placeholder or default handler for resolving audiences that are not recognized.*


### test_custom_arbiter_can_deny_send (function, L216-L238)

> *Summary: This test verifies that a custom arbiter can successfully block message transmission after a communication channel is established. It sets up two agents, opens a conversation between them, injects a denial arbiter, and asserts that sending a message results in an `AccessDeniedError`.*


### test_default_arbiter_preserves_rule_based_behavior (function, L242-L264)

> *Summary: This test verifies that the default arbiter enforces rule-based access control by rejecting a message sent from Alice to Bob after Alice's outbound permissions are restricted to only "carol". It sets up two agents, opens a channel between them, modifies one agent's rules, and asserts an `AccessDeniedError` upon attempting communication outside the allowed scope.*


### test_resolve_unknown_audience_silent_drop_default (function, L268-L287)

> *Summary: This test verifies that the default arbiter silently discards messages intended for an unknown audience ID while still accepting envelopes containing known recipients. It sets up a communication channel between two agents and sends a message targeting both a valid recipient and a non-existent one to confirm this behavior.*


### test_audit_subscribe_taps_live_stream (function, L294-L312)

> *Summary: This test verifies that subscribing to the audit log captures agent registration events when a client connects and registers with the hub. It initializes a memory store, opens a hub, subscribes a tap function to the audit log, simulates an agent registering via a client, and asserts the expected event is captured.*


### test_handler_exception_does_not_crash_channel (function, L319-L352)

> *Summary: This test verifies that an exception raised within an agent's request handling does not terminate the communication channel. It sets up a multi-client environment, intentionally causes one agent to fail during an interaction, and then confirms subsequent messages can still be successfully sent through the surviving channel.*


### test_health_snapshot_shape (function, L359-L391)

> *Summary: This test verifies the structure and content of a health snapshot by initializing a knowledge store, opening a hub, and registering two agents that establish one conversation channel. It asserts that the resulting snapshot correctly reflects the number of registered agents, active channels, and accumulated audit log data after these operations.*


### test_hub_logs_state_transitions (function, L398-L414)

> *Summary: This test verifies that registering agents with the Hub correctly logs state transitions by setting logging to INFO level and asserting the presence of "agent registered" messages after registration calls. It initializes a memory store, opens the Hub, sets up two clients, registers them, and then cleans up all resources.*


### test_hub_logs_warning_on_rejection (function, L418-L436)

> *Summary: This test verifies that the hub logs a warning when an agent's message is rejected due to access rules. It sets up two connected agents, applies a blocking rule to one agent, and asserts that sending a message to the blocked agent triggers a logged "post\_envelope rejected" warning.*


### test_multiple_bad_listeners_do_not_break_dispatch (function, L443-L470)

> *Summary: This test verifies that a message dispatch mechanism continues to function correctly even when some registered listeners raise exceptions. It registers multiple faulty listeners alongside one functional listener and asserts the good listener is invoked after sending a message through the system.*


### test_base_hub_arbiter_allows_everything_by_default (function, L474-L495)

> *Summary: This test verifies that the default arbiter permits all traffic, even when a restrictive inbound-block rule is applied to one participant. It sets up a communication scenario between two clients and asserts that an envelope can successfully be sent across the channel despite the blocking configuration.*


### _DenyAtDelegationDepth (class, L498-L507)

> *Summary: This arbiter enforces a maximum message depth by checking the `envelope.depth` against a configured limit (`_cap`). If the depth exceeds this cap, it returns a `Deny` action; otherwise, it permits the send with an `Allow`.*


### __init__ (method, L501-L502, parent: _DenyAtDelegationDepth)

> *Summary: Initializes an object by setting a capacity limit provided as an integer argument. This sets the internal state for subsequent operations within the instance.*


### authorize_send (method, L504-L507, parent: _DenyAtDelegationDepth)

> *Summary: Checks if the message's depth exceeds a predefined capacity limit (`self._cap`). If it does, it returns a `Deny` object with an explanatory reason; otherwise, it permits sending by returning an `Allow` object.*


### test_custom_arbiter_authorize_send_overrides_rule_based (function, L511-L531)

> *Summary: This test verifies that a custom arbiter denying based on envelope depth successfully blocks subsequent messages sent over an established channel. It sets up two agents, opens a conversation between them, installs the restrictive arbiter, and asserts that sending any message results in an `AccessDeniedError`.*


### test_hub_health_on_populated_hub (function, L535-L562)

> *Summary: This test verifies the health metrics of a `Hub` when it is actively managing multiple registered agents and established communication channels. It initializes the system with five agents, creates three specific connections between them, and then asserts that the hub's reported counts for registered agents, active channels, and audit log size are correct.*


### test_widened_trap_catches_pre_ask_failures (function, L566-L603)

> *Summary: This test verifies that a failure during view projection, caused by a mocked bad view, is correctly caught and routed through the observability surface via `on_turn_failed`. It simulates communication between two agents where an intentional runtime error in view rendering triggers this failure handling while ensuring the channel remains functional afterward.*


### test_register_human_duplicate_name_raises (function, L607-L617)

> *Summary: This test verifies that attempting to register a human with an existing name throws a `NetworkError`. It initializes a local knowledge store and client, registers one human, and then asserts the subsequent registration attempt fails as expected.*


### test_passport_kind_rejects_typo_at_construction (function, L620-L623)

> *Summary: Asserts that attempting to instantiate a `Passport` object with an invalid or misspelled value for the `kind` attribute raises a `ValueError`. This verifies the input validation logic enforces allowed values during object creation.*


### test_replace_audit_log_swaps_listener_chain (function, L627-L651)

> *Summary: This test verifies that a tenant-supplied `AuditLog` can successfully replace the default logging mechanism within a `Hub`. It confirms that events registered via a client are correctly captured by the custom audit log listener, maintaining expected event semantics.*

