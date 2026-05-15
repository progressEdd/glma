# test/beta/network/test_rule_enforcement.py

17 function(s): _agent, test_parse_duration_valid, test_parse_duration_invalid_raises, test_outbound_to_glob_allows_pattern, test_outbound_to_self_send_always_allowed, test_inbound_from_blocks_dispatch_not_post, test_inbound_from_blocks_create_channel_fast_fails, test_delegation_depth_at_cap_accepted_above_rejected, test_delegation_depth_zero_disables_cap, test_max_concurrent_channels_cap_blocks_new_creates and 7 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_parse_duration_valid | function |  |
| test_parse_duration_invalid_raises | function |  |
| test_outbound_to_glob_allows_pattern | function |  |
| test_outbound_to_self_send_always_allowed | function |  |
| test_inbound_from_blocks_dispatch_not_post | function |  |
| test_inbound_from_blocks_create_channel_fast_fails | function |  |
| test_delegation_depth_at_cap_accepted_above_rejected | function |  |
| test_delegation_depth_zero_disables_cap | function |  |
| test_max_concurrent_channels_cap_blocks_new_creates | function |  |
| test_max_concurrent_channels_zero_disables | function |  |
| test_max_concurrent_tasks_blocks_observe | function |  |
| test_inbox_max_pending_rejects_when_full | function |  |
| test_inbox_protocol_events_bypass_capacity | function |  |
| test_channel_ttl_default_drives_expires_at | function |  |
| test_channel_ttl_per_channel_override_wins | function |  |
| test_channel_ttl_zero_no_expiry | function |  |

## Chunks

### _agent (function, L48-L49)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `ScriptedConfig`.*


### test_parse_duration_valid (function, L71-L72)

> *Summary: This test verifies that the `parse_duration` function correctly processes a valid duration string input and returns the expected parsed value. It asserts equality between the function's output and a predefined expected result.*


### test_parse_duration_invalid_raises (function, L76-L78)

> *Summary: Asserts that calling `parse_duration` with an invalid input value raises a `ValueError`. This tests the error handling mechanism for malformed duration strings.*


### test_outbound_to_glob_allows_pattern (function, L85-L124)

> *Summary: This test verifies that an agent's outbound access rule, which restricts communication to patterns like `bot-*`, correctly permits messages to matching recipients while denying messages to others. It sets up a simulated network environment with three agents and confirms that Alice can send messages to Bob but is blocked from sending to Eve.*


### test_outbound_to_self_send_always_allowed (function, L128-L158)

> *Summary: This test verifies that an agent can send messages to itself even if its outbound whitelist explicitly excludes its own ID. It sets up two agents, registers one with a restrictive outbound rule, and then confirms successful channel opening when the target matches the sender's identity under specific registration conditions.*


### test_inbound_from_blocks_dispatch_not_post (function, L162-L209)

> *Summary: This test verifies that an inbound filter correctly prevents a recipient from receiving messages even after the sender's action is successfully recorded in the Write-Ahead Log (WAL). It sets up two agents, blocks one agent from another using `inbound_from`, sends a message, and asserts that while the message exists in the WAL, it never reaches the recipient's handler.*


### test_inbound_from_blocks_create_channel_fast_fails (function, L213-L241)

> *Summary: This test verifies that attempting to create a conversation with an agent whose inbound rules block the creator immediately raises an `AccessDeniedError`. It confirms this pre-flight check prevents silent failures or timeouts when such blocking rules are present.*


### test_delegation_depth_at_cap_accepted_above_rejected (function, L248-L271)

> *Summary: This test verifies that a delegation depth equal to the configured limit is accepted, while any depth exceeding that limit results in an `AccessDeniedError`. It sets up agents with and without specific delegation rules to simulate this boundary condition check.*


### test_delegation_depth_zero_disables_cap (function, L275-L294)

> *Summary: This test verifies that setting `delegation_depth` to zero in a rule effectively disables any depth limitation for message passing. It registers two agents, Alice (with the depth-zero rule) and Bob, then sends a message with an extremely high requested depth from Alice to Bob, expecting it to succeed.*


### test_max_concurrent_channels_cap_blocks_new_creates (function, L301-L329)

> *Summary: This test verifies that a channel limit is enforced by blocking new connections when the maximum concurrent channels are reached. It sets up agents with a limit of two, successfully opens two channels, and then asserts an `AccessDeniedError` upon attempting to open a third before closing one existing channel to allow subsequent connection.*


### test_max_concurrent_channels_zero_disables (function, L333-L355)

> *Summary: This test verifies that an agent configured with a maximum concurrent channel limit of zero will not be able to open any channels, even if other agents are available. It registers one restricted agent and several unrestricted agents, then attempts to open multiple conversations from the restricted agent, asserting that only zero channels are created.*


### test_max_concurrent_tasks_blocks_observe (function, L362-L408)

> *Summary: This test verifies that a configured agent's task concurrency limit is enforced by the knowledge store. It attempts to submit three tasks for an agent limited to two; the third submission raises an `AccessDeniedError`, but subsequent submission succeeds after one of the initial tasks is marked as completed.*


### test_inbox_max_pending_rejects_when_full (function, L415-L446)

> *Summary: This test verifies that sending messages to a recipient whose inbox capacity is reached results in an `InboxFull` exception. It sets up two agents, one with a maximum pending limit of 2, and confirms the third message send fails when the limit is hit.*


### test_inbox_protocol_events_bypass_capacity (function, L450-L474)

> *Summary: This test verifies that critical protocol events, such as invites, are delivered to a recipient even when their inbox capacity limit is reached. It sets up two agents with an inbox block and confirms the channel successfully opens despite the imposed capacity constraint.*


### test_channel_ttl_default_drives_expires_at (function, L481-L503)

> *Summary: This test verifies that a channel opened between two agents, where the initiating agent has a default TTL rule set to one hour, automatically sets an `expires_at` timestamp on the resulting channel metadata. It confirms this expiration time is approximately one hour after creation by calculating the time difference.*


### test_channel_ttl_per_channel_override_wins (function, L507-L527)

> *Summary: This test verifies that a per-channel Time-To-Live (TTL) setting overrides the default TTL configured for an agent's rules. It registers two agents, opens a conversation channel with a specific 30-minute TTL, and asserts the resulting expiration time matches this override.*


### test_channel_ttl_zero_no_expiry (function, L531-L544)

> *Summary: This test verifies that when a channel is opened with a Time-To-Live (TTL) of zero, the resulting channel metadata correctly lacks an `expires_at` timestamp. It sets up a communication environment using a memory store and registers two agents to perform this specific channel creation check.*

