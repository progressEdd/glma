# test/beta/network/test_hub_races.py

19 function(s): _agent, test_concurrent_register_same_name_serializes, test_reregister_after_unregister_assigns_new_id, test_register_collision_does_not_orphan_files, test_unregister_mid_channel_preserves_wal, test_post_from_unregistered_agent_id_raises, test_bind_unattached_endpoint_raises, test_bind_endpoint_to_unregistered_agent_raises, test_concurrent_posts_same_channel_serialize, test_concurrent_posts_different_channels_independent and 9 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_concurrent_register_same_name_serializes | function |  |
| test_reregister_after_unregister_assigns_new_id | function |  |
| test_register_collision_does_not_orphan_files | function |  |
| test_unregister_mid_channel_preserves_wal | function |  |
| test_post_from_unregistered_agent_id_raises | function |  |
| test_bind_unattached_endpoint_raises | function |  |
| test_bind_endpoint_to_unregistered_agent_raises | function |  |
| test_concurrent_posts_same_channel_serialize | function |  |
| test_concurrent_posts_different_channels_independent | function |  |
| test_post_to_terminal_channel_raises | function |  |
| test_post_to_unknown_channel_raises | function |  |
| test_create_channel_with_unknown_participant_raises | function |  |
| test_create_channel_duplicate_participant_raises | function |  |
| test_create_channel_empty_participants_raises | function |  |
| test_create_channel_unknown_manifest_raises | function |  |
| test_hub_close_idempotent | function |  |
| test_hub_close_with_active_channels_clean_shutdown | function |  |
| test_outbound_access_check_runs_before_channel_check | function |  |

## Chunks

### _agent (function, L38-L45)

> *Summary: Creates an `Agent` instance using a provided name and a default configuration that sends no replies. This setup is specifically designed to allow automatic invitation acknowledgments during testing without triggering reply cascades.*


### test_concurrent_register_same_name_serializes (function, L52-L84)

> *Summary: This test verifies that concurrent registration attempts using the same name are serialized by a lock within the Hub. It asserts that exactly one registration succeeds while the others fail with an "already registered" error, ensuring data consistency across all operations.*


### test_reregister_after_unregister_assigns_new_id (function, L88-L102)

> *Summary: This test verifies that re-registering an agent with the same name after it has been unregistered results in a new, distinct `agent_id`. It initializes a Hub and client, registers an agent, unregisters it, then registers it again to assert ID change.*


### test_register_collision_does_not_orphan_files (function, L106-L121)

> *Summary: This test verifies that attempting to re-register an existing agent fails gracefully without creating orphaned identity files. It registers one agent, then attempts a duplicate registration which raises a `ProtocolError`, finally asserting only the original agent remains listed in the hub.*


### test_unregister_mid_channel_preserves_wal (function, L128-L165)

> *Summary: This test verifies that unregistering a participant from an active channel does not delete the channel's Write-Ahead Log (WAL). It initializes a hub, registers two agents, opens a conversation, sends messages, unregisters one agent, and then asserts that the WAL content remains unchanged while confirming the unregistered agent is no longer discoverable.*


### test_post_from_unregistered_agent_id_raises (function, L169-L192)

> *Summary: This test verifies that posting an envelope using a previously registered but now unregistered agent ID results in a `NotFoundError`. It sets up a hub, registers and unregisters an agent, then attempts to post a message directly via the hub with the stale ID to confirm the rejection mechanism works.*


### test_bind_unattached_endpoint_raises (function, L199-L209)

> *Summary: This test verifies that attempting to bind an endpoint using a non-existent ID raises a `NotFoundError`. It initializes a Hub, registers an agent via a client, and then calls the binding function with an invalid endpoint identifier.*


### test_bind_endpoint_to_unregistered_agent_raises (function, L213-L227)

> *Summary: This test verifies that attempting to bind a network endpoint to an agent ID that has not been registered with the hub raises a `NotFoundError`. It initializes a hub and registers one valid agent before testing the binding operation against a non-existent agent identifier.*


### test_concurrent_posts_same_channel_serialize (function, L234-L263)

> *Summary: This test verifies that concurrent message sends to the same channel are serialized correctly by the Write-Ahead Log (WAL). It initiates five parallel posts from one agent to another and asserts that all messages are recorded uniquely in the WAL in the expected order.*


### test_concurrent_posts_different_channels_independent (function, L267-L294)

> *Summary: This test verifies that concurrent message sending across different communication channels remains independent. It registers multiple agents, opens separate conversations between them, and then concurrently sends messages to distinct recipients via these channels, asserting that each channel's event log correctly contains only its intended messages.*


### test_post_to_terminal_channel_raises (function, L301-L318)

> *Summary: This test verifies that attempting to send a message on a communication channel after it has been closed results in a `ProtocolError`. It sets up a multi-agent environment, establishes and then closes a conversation between two agents, and asserts the failure when sending data post-closure.*


### test_post_to_unknown_channel_raises (function, L322-L340)

> *Summary: This test verifies that attempting to send a message envelope to a non-existent channel ID results in a `NotFoundError`. It sets up a local communication hub, registers an agent, and then asserts the expected exception when sending data to `"no-such-channel"`.*


### test_create_channel_with_unknown_participant_raises (function, L344-L359)

> *Summary: This test verifies that attempting to create a channel with an unknown participant ID results in a `NotFoundError`. It initializes a Hub, registers one agent, and then calls `create_channel` using a non-existent UUID as a participant.*


### test_create_channel_duplicate_participant_raises (function, L363-L384)

> *Summary: This test verifies that attempting to create a channel with a duplicate participant ID immediately raises a `ProtocolError` before any data is persisted. It confirms the failure by asserting that no channels are registered in the hub after the error occurs.*


### test_create_channel_empty_participants_raises (function, L388-L403)

> *Summary: This test verifies that attempting to create a channel with no participants raises a `ProtocolError`. It initializes a Hub and registers one agent before calling the creation method with an empty participant list.*


### test_create_channel_unknown_manifest_raises (function, L407-L423)

> *Summary: This test verifies that attempting to create a channel with an unknown manifest type raises a `NotFoundError`. It sets up a communication hub and registers two agents before calling the creation method with an invalid protocol string.*


### test_hub_close_idempotent (function, L430-L433)

> *Summary: Verifies that calling the `close()` method on a `Hub` instance multiple times has no adverse effects. It opens a hub with specific memory and time-to-live settings, closes it once, and then successfully calls close again without error.*


### test_hub_close_with_active_channels_clean_shutdown (function, L437-L453)

> *Summary: This test verifies that closing a `Hub` instance while active communication channels exist results in a clean shutdown without leaking background endpoint tasks. It registers two agents, initiates a conversation between them, closes the client and the hub, and then asserts all associated endpoint tasks have completed.*


### test_outbound_access_check_runs_before_channel_check (function, L460-L489)

> *Summary: This test verifies that an outbound access denial is checked before channel existence when sending a message. It registers two agents, one with restricted outbound permissions, and asserts that attempting to send an envelope to a non-existent channel immediately raises `AccessDeniedError`.*

