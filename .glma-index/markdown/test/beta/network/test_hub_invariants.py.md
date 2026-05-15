# test/beta/network/test_hub_invariants.py

19 function(s): _agent, _invoke, _ack_only_handler, test_unregister_deletes_disk_files_so_hydrate_forgets_agent, test_register_rejects_duplicate_name_raises_protocol_error, test_unregister_then_reregister_with_same_name_works, test_create_channel_enforces_max_concurrent_channels, test_observe_task_enforces_max_concurrent_tasks, test_post_envelope_enforces_inbox_max_pending, test_inbox_pending_cleared_on_unregister and 9 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _invoke | function |  |
| _ack_only_handler | function |  |
| test_unregister_deletes_disk_files_so_hydrate_forgets_agent | function |  |
| test_register_rejects_duplicate_name_raises_protocol_error | function |  |
| test_unregister_then_reregister_with_same_name_works | function |  |
| test_create_channel_enforces_max_concurrent_channels | function |  |
| test_observe_task_enforces_max_concurrent_tasks | function |  |
| test_post_envelope_enforces_inbox_max_pending | function |  |
| test_inbox_pending_cleared_on_unregister | function |  |
| test_delegate_returns_target_reply_without_dropping_fast_reply | function |  |
| test_delegate_fails_fast_when_channel_closes_before_reply | function |  |
| test_two_same_name_expectations_both_fire | function |  |
| test_record_observation_dedups_by_task_id | function |  |
| test_concurrency_caps_zero_disables | function |  |
| test_inbox_capacity_does_not_block_protocol_events | function |  |
| test_fired_violations_cleared_on_terminal_channel_transition | function |  |
| test_set_resume_rewrites_by_capability_disk_file | function |  |
| test_delegate_fails_fast_on_channel_expire | function |  |

## Chunks

### _agent (function, L88-L89)

> *Summary: Creates and returns an `Agent` instance, configuring it using a `TestConfig` derived from the provided name and any subsequent event arguments.*


### _invoke (function, L92-L105)

> *Summary: Executes a provided tool with given arguments and optional dependencies to obtain its result. It returns the content or data from the first part of the tool's response if available, otherwise it returns the entire result event.*


### _ack_only_handler (function, L108-L130)

> *Summary: This function generates a handler that automatically sends an acknowledgment (`EV_CHANNEL_INVITE_ACK`) only when it receives a `EV_CHANNEL_INVITE`. It ignores all other incoming events, allowing tests to verify channel opening without triggering further responses.*


### test_unregister_deletes_disk_files_so_hydrate_forgets_agent (function, L137-L178)

> *Summary: This test verifies that calling `unregister` removes all associated identity files from the underlying store. It then confirms that a newly initialized Hub instance using the same store does not recognize the previously unregistered agent.*


### test_register_rejects_duplicate_name_raises_protocol_error (function, L185-L199)

> *Summary: This test verifies that attempting to register an agent with a name already present in the system results in a `ProtocolError`. It initializes a knowledge store and hub, registers one entity, and then asserts that a subsequent registration attempt with the identical name fails as expected.*


### test_unregister_then_reregister_with_same_name_works (function, L203-L217)

> *Summary: This test verifies that explicitly unregistering an agent allows the same identity to rejoin under the same name, resulting in a new unique agent ID. It initializes a Hub and client, registers an agent, unregisters it, and then successfully re-registers it to confirm the name reuse functionality.*


### test_create_channel_enforces_max_concurrent_channels (function, L224-L247)

> *Summary: This test verifies that a user is prevented from opening new channels if they exceed the configured maximum concurrent channel limit. It sets up three clients, limits one client to one active channel, opens one channel for that client, and then asserts an `AccessDeniedError` when attempting to open a second channel.*


### test_observe_task_enforces_max_concurrent_tasks (function, L251-L296)

> *Summary: This test verifies that the `observe_task` method rejects new tasks for an agent if they exceed a predefined maximum concurrency limit set by a rule. It simulates observing one running task, then attempts to observe a second one which fails with an `AccessDeniedError`, before successfully observing a third task after the first one is marked as completed.*


### test_post_envelope_enforces_inbox_max_pending (function, L300-L353)

> *Summary: This test verifies that the system rejects incoming messages when a recipient's inbox reaches its configured capacity limit. It simulates Alice sending messages to Bob, asserts an `InboxFull` error upon exceeding two pending messages, and then confirms subsequent delivery after Bob sends a message that decrements his pending count.*


### test_inbox_pending_cleared_on_unregister (function, L357-L388)

> *Summary: This test verifies that when an agent is unregistered, its pending inbox count is cleared from the central hub's state. It simulates sending a message to an agent and then unregistering that agent to confirm the inbox counter resets to zero.*


### test_delegate_returns_target_reply_without_dropping_fast_reply (function, L395-L419)

> *Summary: This test verifies that a delegate correctly forwards and receives the target's reply without dropping it, even when the response arrives immediately after the initial message is sent. It sets up two agents, invokes a delegate tool targeting one agent from another, and asserts the expected answer is present in the final result.*


### test_delegate_fails_fast_when_channel_closes_before_reply (function, L423-L469)

> *Summary: This test verifies that a delegate immediately fails when the communication channel closes before receiving a reply from the target agent. It sets up two agents, initiates an interaction, and concurrently closes the active channel to assert the function returns quickly with a "channel closed" error instead of timing out for 300 seconds.*


### test_two_same_name_expectations_both_fire (function, L476-L543)

> *Summary: This test verifies that a system correctly fires multiple violation handlers when two expectations share the same name but have different `on_violation` configurations within one manifest. It asserts that both registered handlers are triggered exactly once upon the first clock tick after the threshold is crossed, and not again on subsequent ticks at the same time.*


### test_record_observation_dedups_by_task_id (function, L550-L589)

> *Summary: This test verifies that recording the same observation with an identical `task_id` multiple times only increments the total count once within a knowledge store. It confirms that subsequent observations with different `task_id`s correctly update both the total and specific outcome counts for a given capability.*


### test_concurrency_caps_zero_disables (function, L596-L631)

> *Summary: Verifies that setting `max_concurrent_channels` and `max_concurrent_tasks` to zero effectively disables the respective concurrency limits within a Hub system. It confirms that opening multiple conversations and observing several tasks proceeds without raising exceptions under these relaxed constraints.*


### test_inbox_capacity_does_not_block_protocol_events (function, L635-L681)

> *Summary: This test verifies that protocol events, like new channel invites, are processed even when an agent's substantive inbox is at capacity. It sets up a capped recipient and confirms that opening a new channel succeeds despite the existing pending messages.*


### test_fired_violations_cleared_on_terminal_channel_transition (function, L685-L737)

> *Summary: This test verifies that the internal tracking of fired violations is correctly cleared when a channel transitions to a terminal state. It initializes a `Hub` with a specific manifest and metadata for a channel, simulates an expectation violation, and then asserts that the violation record disappears after the channel is closed.*


### test_set_resume_rewrites_by_capability_disk_file (function, L741-L773)

> *Summary: This test verifies that updating an agent's resume via `set_resume` correctly synchronizes the in-memory capability index with a persistent disk cache (`/registry/by_capability.json`). It confirms that adding, updating (adding new claims), and removing capabilities accurately reflect changes in the stored JSON structure.*


### test_delegate_fails_fast_on_channel_expire (function, L777-L830)

> *Summary: This test verifies that when a consulting channel expires due to its TTL while the delegate is waiting for a reply, it fails fast by returning an `Error: ... channel closed: ttl_expired` instead of timing out after 300 seconds. It achieves this by manually advancing time and triggering the expiration mechanism during an active invocation.*

