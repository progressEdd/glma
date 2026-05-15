# test/beta/network/test_channel_pruning.py

5 function(s): _agent, test_adapter_state_retained_after_close_for_analysis, test_channel_locks_pruned_on_close, test_fired_violations_pruned_on_close, test_pruning_under_many_short_channels_keeps_caches_bounded.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_adapter_state_retained_after_close_for_analysis | function |  |
| test_channel_locks_pruned_on_close | function |  |
| test_fired_violations_pruned_on_close | function |  |
| test_pruning_under_many_short_channels_keeps_caches_bounded | function |  |

## Chunks

### _agent (function, L34-L35)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `TestConfig`. This function serves to instantiate test agents for network simulations.*


### test_adapter_state_retained_after_close_for_analysis (function, L39-L70)

> *Summary: This test verifies that the adapter state for a closed channel remains accessible via `hub.adapter_state()` after explicitly closing it, allowing for post-mortem analysis. It sets up two clients communicating through a central hub and asserts that the retrieved state matches the pre-closure snapshot even after all components are shut down.*


### test_channel_locks_pruned_on_close (function, L74-L95)

> *Summary: This test verifies that the internal lock tracking for a communication channel is automatically removed when the channel is explicitly closed via `hub.close_channel`. It confirms this removal persists even after all associated client and hub connections are shut down.*


### test_fired_violations_pruned_on_close (function, L99-L118)

> *Summary: This test verifies that pre-existing "fired violations" entries associated with a channel are automatically removed when the channel is explicitly closed via `hub.close_channel`. It sets up clients and channels, manually injects a violation record, closes the channel, and asserts the record's absence in the store.*


### test_pruning_under_many_short_channels_keeps_caches_bounded (function, L122-L153)

> *Summary: This test verifies that the system correctly cleans up per-channel state after numerous short-lived channels are opened and closed. It confirms that internal caches, such as locks and waiters, remain bounded by asserting they are empty after the channel lifecycle completes.*

