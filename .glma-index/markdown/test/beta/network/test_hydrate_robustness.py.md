# test/beta/network/test_hydrate_robustness.py

12 function(s): _agent, test_hydrate_empty_store_returns_empty, test_hydrate_idempotent, test_hydrate_missing_rule_falls_back_to_default, test_hydrate_missing_skill_returns_none, test_hydrate_skill_deleted_out_of_band, test_hydrate_rebuilds_capability_index_from_resumes, test_hydrate_handles_partial_trailing_line_in_audit_log, test_hydrate_channel_with_unregistered_adapter_keeps_metadata, test_hydrate_channel_metadata_with_no_adapter_state_not_active and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_hydrate_empty_store_returns_empty | function |  |
| test_hydrate_idempotent | function |  |
| test_hydrate_missing_rule_falls_back_to_default | function |  |
| test_hydrate_missing_skill_returns_none | function |  |
| test_hydrate_skill_deleted_out_of_band | function |  |
| test_hydrate_rebuilds_capability_index_from_resumes | function |  |
| test_hydrate_handles_partial_trailing_line_in_audit_log | function |  |
| test_hydrate_channel_with_unregistered_adapter_keeps_metadata | function |  |
| test_hydrate_channel_metadata_with_no_adapter_state_not_active | function |  |
| test_hydrate_resume_observed_stats_survive | function |  |
| test_hydrate_terminal_channel_not_in_active_cache | function |  |

## Chunks

### _agent (function, L53-L54)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `ScriptedConfig`.*


### test_hydrate_empty_store_returns_empty (function, L58-L66)

> *Summary: Verifies that when initializing a knowledge store with no existing data, the system correctly reports zero agents, channels, and tasks. It confirms the initial state of an empty store is accurately reflected by listing operations.*


### test_hydrate_idempotent (function, L70-L90)

> *Summary: This test verifies that hydrating a knowledge store twice yields the same state, ensuring idempotency. It initializes a `Hub` with a disk store, registers an agent via a client, closes the initial connection, and then re-opens the store to confirm the agent is present after a second hydration call.*


### test_hydrate_missing_rule_falls_back_to_default (function, L94-L120)

> *Summary: This test verifies that if a stored agent's rule file is deleted externally, the system correctly hydrates the agent by falling back to the `Rule()` default configuration upon reopening the knowledge store. It achieves this by deleting the specific rule JSON for an existing agent and then asserting the loaded rule matches the expected defaults.*


### test_hydrate_missing_skill_returns_none (function, L124-L139)

> *Summary: This test verifies that retrieving a skill for an agent returns `None` when no corresponding skill data exists in the knowledge store. It initializes two hubs, registers an agent with one, and then attempts to fetch that agent's skill from the second hub, asserting the result is null.*


### test_hydrate_skill_deleted_out_of_band (function, L143-L166)

> *Summary: This test verifies that if a registered skill is deleted from the underlying store after registration, subsequent retrieval attempts will correctly return `None`. It sets up an agent, registers their skill, deletes the skill data externally, and then confirms the knowledge base reflects the deletion.*


### test_hydrate_rebuilds_capability_index_from_resumes (function, L170-L199)

> *Summary: This test verifies that the system can correctly rebuild its capability index from authoritative resume data even after the derived cache is deleted. It registers agents with specific capabilities, then deletes the pre-computed index before re-opening the store to confirm discovery functions still work as expected.*


### test_hydrate_handles_partial_trailing_line_in_audit_log (function, L203-L232)

> *Summary: This test verifies that when an audit log file contains a partially written, truncated trailing line, the `read_all` method correctly raises a JSON decoding error while still successfully emitting all preceding valid records in order. It achieves this by manually corrupting the stored data to simulate a mid-write crash scenario.*


### test_hydrate_channel_with_unregistered_adapter_keeps_metadata (function, L236-L267)

> *Summary: This test verifies that when hydrating a channel in a Hub without registering its specific manifest adapter, the existing metadata is preserved for reading. However, attempting to send an envelope to that channel correctly raises a `ProtocolError` instead of crashing with a `KeyError`.*


### test_hydrate_channel_metadata_with_no_adapter_state_not_active (function, L271-L290)

> *Summary: This test verifies that a loaded channel lacking adapter state is excluded from both active and adapter state tracking within the Hub upon hydration. It simulates opening a conversation between two agents and then asserts that this channel ID does not appear in the newly hydrated Hub's internal state structures.*


### test_hydrate_resume_observed_stats_survive (function, L294-L338)

> *Summary: This test verifies that capability statistics recorded via `record_observation` survive a round-trip across two separate instances of the knowledge store. It initializes an agent, records task observations (including latency), closes the first hub instance, and then reopens a second hub to confirm the observed stats and agent listings are correctly persisted.*


### test_hydrate_terminal_channel_not_in_active_cache (function, L342-L367)

> *Summary: This test verifies that a channel, after being explicitly closed, persists in the store's general channels but is not present in the active channels cache when a new Hub instance loads the data. It confirms that newly opened channels are correctly registered as active upon loading.*

