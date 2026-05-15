# test/beta/network/test_audit_and_lifecycle.py

8 function(s): _agent, test_post_envelope_rejects_envelope_above_delegation_depth, test_delegation_depth_zero_disables_cap, test_post_envelope_after_hydrate_without_adapter_state_raises_protocol_error, test_expectation_tick_processes_all_channels_when_one_auto_closes, test_audit_log_records_channel_created_and_closed, test_audit_log_records_channel_expired_on_ttl_sweep, test_audit_log_records_task_terminated_on_channel_cascade.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_post_envelope_rejects_envelope_above_delegation_depth | function |  |
| test_delegation_depth_zero_disables_cap | function |  |
| test_post_envelope_after_hydrate_without_adapter_state_raises_protocol_error | function |  |
| test_expectation_tick_processes_all_channels_when_one_auto_closes | function |  |
| test_audit_log_records_channel_created_and_closed | function |  |
| test_audit_log_records_channel_expired_on_ttl_sweep | function |  |
| test_audit_log_records_task_terminated_on_channel_cascade | function |  |

## Chunks

### _agent (function, L52-L53)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `TestConfig`. This helper function is used to set up test agents.*


### test_post_envelope_rejects_envelope_above_delegation_depth (function, L60-L100)

> *Summary: This test verifies that the Hub rejects an incoming envelope if its specified `depth` exceeds a sender's configured delegation depth limit. It confirms rejection for a depth of 3 when the limit is set to 2, while successfully accepting an envelope at the exact limit (depth=2).*


### test_delegation_depth_zero_disables_cap (function, L104-L129)

> *Summary: This test verifies that setting `delegation_depth=0` in a rule allows for arbitrarily deep message envelopes. It simulates communication between two agents, sending a deeply nested envelope to confirm the cap is disabled as expected.*


### test_post_envelope_after_hydrate_without_adapter_state_raises_protocol_error (function, L136-L196)

> *Summary: When a channel is loaded from storage without its corresponding adapter present, the system keeps it dormant; subsequently registering the adapter and attempting to post an envelope triggers a `ProtocolError` if no adapter state exists for that channel. This test verifies that stale envelopes are rejected with a specific error rather than failing silently or with a generic key error.*


### test_expectation_tick_processes_all_channels_when_one_auto_closes (function, L203-L270)

> *Summary: This test verifies that when one channel's expectation triggers an `auto_close`, other channels on the same processing tick are still evaluated for violations. It sets up a system where two concurrent conversations violate a silence threshold simultaneously, ensuring both closures and violations are correctly logged in a single tick cycle.*


### test_audit_log_records_channel_created_and_closed (function, L277-L303)

> *Summary: This test verifies that the system's audit log correctly records both the creation and explicit closure of a communication channel between two registered agents. It initializes a hub, registers clients, opens a channel, closes it, and then asserts the presence and details of the corresponding `CHANNEL_CREATED` and `CHANNEL_CLOSED` entries in the audit log.*


### test_audit_log_records_channel_expired_on_ttl_sweep (function, L307-L334)

> *Summary: This test verifies that when a channel's Time-To-Live (TTL) expires, the system emits an `channel_expired` audit record instead of a `channel_closed` one. It simulates agent registration and channel creation, advances time past the TTL, triggers the sweep, and asserts the presence of exactly one "ttl\_expired" audit entry for the specific channel.*


### test_audit_log_records_task_terminated_on_channel_cascade (function, L338-L379)

> *Summary: This test verifies that when a channel is closed due to a cascade, any associated running tasks are correctly recorded in the audit log as terminated with an `EXPIRED` outcome and carrying their specified capability. It sets up two agents, creates a task under their conversation channel, closes the channel explicitly, and then asserts the presence and details of the resulting termination record.*

