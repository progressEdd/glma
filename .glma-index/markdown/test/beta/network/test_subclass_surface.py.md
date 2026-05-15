# test/beta/network/test_subclass_surface.py

9 function(s): _agent, test_subclass_on_envelope_posted_fires_without_listener_registration, test_subclass_hook_runs_alongside_external_listener, test_register_sweeper_runs_periodically, test_register_sweeper_rejects_duplicate_name, test_register_sweeper_rejects_non_positive_interval, test_audit_log_accepts_custom_kinds, test_inbox_pressure_fires_on_crossing_high_water, test_task_mirror_failure_fires_mirror_failed_event.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_subclass_on_envelope_posted_fires_without_listener_registration | function |  |
| test_subclass_hook_runs_alongside_external_listener | function |  |
| test_register_sweeper_runs_periodically | function |  |
| test_register_sweeper_rejects_duplicate_name | function |  |
| test_register_sweeper_rejects_non_positive_interval | function |  |
| test_audit_log_accepts_custom_kinds | function |  |
| test_inbox_pressure_fires_on_crossing_high_water | function |  |
| test_task_mirror_failure_fires_mirror_failed_event | function |  |

## Chunks

### _agent (function, L38-L39)

> *Summary: Creates and returns an `Agent` instance, configuring it using a `TestConfig` object initialized with the provided string replies. The function takes a name and variable arguments of strings as input.*


### test_subclass_on_envelope_posted_fires_without_listener_registration (function, L46-L78)

> *Summary: This test verifies that a custom subclass overriding the `on_envelope_posted` method correctly captures envelope events even when no explicit listener registration occurs. It simulates communication between two agents via a shared hub and asserts that the overridden method successfully records all sent envelopes.*


### test_subclass_hook_runs_alongside_external_listener (function, L82-L118)

> *Summary: This test verifies that both a subclass override and an externally registered listener receive notifications when an agent registers with the system. It initializes a custom Hub and Listener, then simulates an agent registration to assert that both callback mechanisms were triggered.*


### test_register_sweeper_runs_periodically (function, L125-L144)

> *Summary: This test verifies that a registered sweeper function executes at the specified interval and stops executing immediately after being unregistered. It uses an asynchronous event loop to track execution times, asserting multiple runs occur while active and zero or one run occurs after deactivation.*


### test_register_sweeper_rejects_duplicate_name (function, L148-L160)

> *Summary: This test verifies that attempting to register a sweeper with an existing name throws a `ValueError`. It initializes a knowledge store and hub, registers one sweeper, then attempts to register another using the same name within a `pytest.raises` block.*


### test_register_sweeper_rejects_non_positive_interval (function, L164-L176)

> *Summary: This test verifies that the system rejects registration of sweepers when provided with non-positive time intervals. It asserts that attempting to register a sweeper with an interval of zero or a negative value raises a `ValueError`.*


### test_audit_log_accepts_custom_kinds (function, L183-L198)

> *Summary: This test verifies that the audit log accepts and stores custom event types by appending a record with a specific `"kind"` value. It reads all stored records to assert that the provided custom kind is present in the collected set of kinds.*


### test_inbox_pressure_fires_on_crossing_high_water (function, L205-L244)

> *Summary: This test verifies that an inbox pressure listener fires exactly once when the number of pending messages crosses a predefined high-water mark. It simulates two agents communicating, sends four messages to one agent configured with a high-water limit of 3, and asserts the listener captures the event at the threshold crossing.*


### test_task_mirror_failure_fires_mirror_failed_event (function, L251-L275)

> *Summary: This test verifies that a `TaskMirror` correctly emits a `mirror_failed` event when its underlying hub connection fails during task observation. It achieves this by injecting a failure into the hub's observation method and asserting the corresponding event is captured by a registered listener.*

