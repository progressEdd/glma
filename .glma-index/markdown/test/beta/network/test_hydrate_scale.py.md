# test/beta/network/test_hydrate_scale.py

3 function(s): _agent, test_hydrate_round_trips_many_channels, test_hydrate_refolds_discussion_round_robin_state.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_hydrate_round_trips_many_channels | function |  |
| test_hydrate_refolds_discussion_round_robin_state | function |  |

## Chunks

### _agent (function, L54-L55)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `TestConfig`.*


### test_hydrate_round_trips_many_channels (function, L59-L141)

> *Summary: This test verifies the persistence and round-trip integrity of knowledge store state across multiple conversation channels. It populates a disk store via an active hub, closes it, reopens it to verify agent identities, capabilities, and channel states match the initial configuration, and finally confirms idempotency by hydrating the store twice.*


### test_hydrate_refolds_discussion_round_robin_state (function, L145-L196)

> *Summary: This test verifies that the round-robin state of a multi-party discussion persists correctly across a simulated hub restart. It initializes several agents, sends 50 sequential messages following a defined rotation order, then closes and reopens the hub to assert that the final turn count, expected next speaker, and participant ordering are preserved in the rebuilt state.*

