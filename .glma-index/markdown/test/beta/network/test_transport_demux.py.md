# test/beta/network/test_transport_demux.py

8 function(s): _agent, test_multiple_agents_share_single_hub_client_endpoint, test_targeted_envelope_delivered_to_only_named_recipient, test_broadcast_envelope_delivered_to_all_non_sender, test_unregister_cleans_endpoint_binding, test_two_hub_clients_share_one_hub_isolated_endpoints, test_hub_client_close_shuts_down_link, test_hub_close_idempotent_after_endpoint_attached.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_multiple_agents_share_single_hub_client_endpoint | function |  |
| test_targeted_envelope_delivered_to_only_named_recipient | function |  |
| test_broadcast_envelope_delivered_to_all_non_sender | function |  |
| test_unregister_cleans_endpoint_binding | function |  |
| test_two_hub_clients_share_one_hub_isolated_endpoints | function |  |
| test_hub_client_close_shuts_down_link | function |  |
| test_hub_close_idempotent_after_endpoint_attached | function |  |

## Chunks

### _agent (function, L35-L36)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `ScriptedConfig`.*


### test_multiple_agents_share_single_hub_client_endpoint (function, L40-L61)

> *Summary: This test verifies that multiple agents registered through a single `HubClient` share the same underlying network endpoint managed by the `Hub`. It confirms that all registered agent IDs are correctly mapped to this shared endpoint and vice-versa.*


### test_targeted_envelope_delivered_to_only_named_recipient (function, L65-L118)

> *Summary: This test verifies that messages explicitly addressed to a specific recipient are delivered only to that intended party, even when multiple identities share the same client instance. It sets up three agents and sends a targeted message to one, asserting that only the designated recipient receives it while others do not.*


### test_broadcast_envelope_delivered_to_all_non_sender (function, L122-L168)

> *Summary: This test verifies that a broadcast envelope sent with `audience=None` is delivered to all registered participants except the sender. It sets up three agents, sends a message from one agent through a channel, and asserts that only the intended recipients receive the message while the sender does not.*


### test_unregister_cleans_endpoint_binding (function, L172-L195)

> *Summary: This test verifies that when an agent unregisters, its mapping to any endpoint is correctly removed from the system's internal state. It confirms that after calling `unregister()` on one agent, only that specific agent's binding disappears while other agents remain associated with the shared endpoint.*


### test_two_hub_clients_share_one_hub_isolated_endpoints (function, L199-L239)

> *Summary: This test verifies that two distinct `HubClient` instances sharing a single `Hub` receive separate endpoints for their registered agents. It confirms that messages sent from one client's agent are correctly delivered to the intended recipient while maintaining strict isolation between the clients' internal state and communication channels.*


### test_hub_client_close_shuts_down_link (function, L243-L256)

> *Summary: This test verifies that calling `HubClient.close()` terminates the underlying link's receive loop. It asserts that any subsequent registration attempts on the closed client will raise a `RuntimeError`.*


### test_hub_close_idempotent_after_endpoint_attached (function, L260-L269)

> *Summary: This test verifies that calling the `close()` method on a Hub twice is safe and idempotent, even after an endpoint has been attached to it. It initializes a Hub, registers a client, closes the client, and then calls `hub.close()` a second time without error.*

