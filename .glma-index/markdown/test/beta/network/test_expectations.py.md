# test/beta/network/test_expectations.py

12 function(s): _agent, _silent_handler, _conv_metadata, _envelope, _ctx, test_auto_close_handler_terminates_channel_with_audit, test_audit_handler_records_without_envelope_or_close, test_notify_channel_handler_broadcasts_envelope, test_violation_dedup_within_channel_lifetime, test_audit_log_records_register_and_unregister and 2 more. 3 class(es): TestAcksWithinEvaluator, TestReplyWithinEvaluator, TestMaxSilenceEvaluator. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _silent_handler | function |  |
| _conv_metadata | function |  |
| _envelope | function |  |
| _ctx | function |  |
| TestAcksWithinEvaluator | class |  |
| TestReplyWithinEvaluator | class |  |
| TestMaxSilenceEvaluator | class |  |
| test_auto_close_handler_terminates_channel_with_audit | function |  |
| test_audit_handler_records_without_envelope_or_close | function |  |
| test_notify_channel_handler_broadcasts_envelope | function |  |
| test_violation_dedup_within_channel_lifetime | function |  |
| test_audit_log_records_register_and_unregister | function |  |
| test_audit_log_records_set_resume_skill_rule | function |  |
| test_audit_log_writer_round_trips | function |  |

## Chunks

### _agent (function, L73-L74)

> *Summary: Creates and returns an `Agent` instance, configuring it using a `TestConfig` derived from the provided name and any subsequent event objects.*


### _silent_handler (function, L77-L82)

> *Summary: This asynchronous function acts as a no-operation handler, accepting an `Envelope` input and returning nothing. Its purpose is to simulate a participant that intentionally ignores incoming messages for testing scenarios requiring non-response.*


### _conv_metadata (function, L85-L104)

> *Summary: Constructs a standardized `ChannelMetadata` object for testing two-party conversations. It accepts optional parameters like channel state, creation timestamp, and pending acknowledgments to configure the metadata structure.*


### _envelope (function, L107-L123)

> *Summary: Constructs an `Envelope` object representing a message event. It takes sender ID, the message content, creation timestamp, and optional audience list as inputs to generate a structured envelope instance.*


### _ctx (function, L126-L139)

> *Summary: Creates an `ExpectationContext` object by taking channel metadata and optional Write-Ahead Log (WAL) data. It initializes the context with provided timestamps and converts the input time string into a datetime object for internal use.*


### TestAcksWithinEvaluator (class, L145-L194)

> *Summary: These tests verify the `AcksWithinEvaluator`'s behavior by simulating various scenarios. It checks if the evaluator correctly identifies violations when pending acknowledgments exceed a specified time threshold, and confirms it remains silent otherwise (e.g., within the threshold or when no pending ACKs exist).*


### test_fires_after_threshold_with_pending_acks (method, L146-L161, parent: TestAcksWithinEvaluator)

> *Summary: This test verifies that an `AcksWithinEvaluator` correctly identifies a violation when pending acknowledgments exist and the time threshold is exceeded. It inputs metadata indicating a `PENDING` state with specific pending IDs, evaluates it against a 30-second expectation, and asserts that a violation object is returned targeting those pending IDs.*


### test_silent_within_threshold (method, L163-L176, parent: TestAcksWithinEvaluator)

> *Summary: This test verifies that an `AcksWithinEvaluator` correctly reports no violation when the elapsed time (30 seconds) is less than the configured threshold (60 seconds). It uses mock metadata and a specific expectation to assert that the evaluation returns `None`.*


### test_silent_when_no_pending_acks (method, L178-L186, parent: TestAcksWithinEvaluator)

> *Summary: When provided with metadata indicating a `PENDING` state and no pending acknowledgments, the evaluator should return no violation for an "acks\_within" expectation set to 30 seconds. This test confirms that the system remains silent when there are no outstanding acknowledgments to check against.*


### test_silent_when_channel_active (method, L188-L194, parent: TestAcksWithinEvaluator)

> *Summary: When the channel state is active and no pending acknowledgments exist, this test verifies that an evaluator does not raise any violations. It confirms silent operation by asserting that the evaluation returns `None`.*


### TestReplyWithinEvaluator (class, L197-L240)

> *Summary: This test suite verifies the `ReplyWithinEvaluator`'s logic for determining if a participant has failed to respond within a specified time window. It uses various scenarios, providing message logs and a current timestamp as input, to assert whether violations occur or not.*


### test_fires_when_addressed_participant_silent (method, L198-L209, parent: TestReplyWithinEvaluator)

> *Summary: This test verifies that a reply expectation fires when the addressed participant remains silent. It sets up an initial message to "bob" and asserts that the `ReplyWithinEvaluator` detects a violation after a specified time if no response is received from bob.*


### test_silent_when_reply_within_threshold (method, L211-L224, parent: TestReplyWithinEvaluator)

> *Summary: This test verifies that no violation is reported when a reply occurs within the specified time threshold. It simulates a conversation where both messages are recent enough to fall inside the 60-second evaluation window, expecting the evaluator to return `None`.*


### test_originally_addressed_party_not_violator_after_reply (method, L226-L240, parent: TestReplyWithinEvaluator)

> *Summary: This test verifies that when an original recipient replies, they are not flagged as a violator even if the reply occurs after a specified time threshold. It simulates message exchange between Alice and Bob and asserts that only the initial sender (Alice) is marked as violating the "reply within" rule.*


### TestMaxSilenceEvaluator (class, L243-L263)

> *Summary: Tests verify the `MaxSilenceEvaluator`'s behavior by checking if it correctly triggers a violation when no activity occurs for a specified duration, and conversely, does not trigger one if recent activity exists. It takes an expectation defining silence thresholds and context data (metadata, wall logs, current time) as input to produce a potential violation object or `None`.*


### test_fires_when_channel_silent_past_threshold (method, L244-L255, parent: TestMaxSilenceEvaluator)

> *Summary: This test verifies that a silence evaluation triggers when no messages are present for a specified duration. It uses a `MaxSilenceEvaluator` against a context containing an empty write-ahead log and asserts that a violation object is returned.*


### test_silent_when_recent_activity (method, L257-L263, parent: TestMaxSilenceEvaluator)

> *Summary: This test verifies that the `MaxSilenceEvaluator` remains silent when recent activity exists. It evaluates an expectation against a context containing metadata and a single recent log entry, asserting no violation occurs.*


### test_auto_close_handler_terminates_channel_with_audit (function, L270-L321)

> *Summary: This test verifies that a channel automatically closes and records an audit entry when the `acks_within` timeout expires without receiving acknowledgments. It sets up two clients, initiates communication, advances time past the configured threshold, and asserts the resulting channel state is `CLOSED` with the correct violation reason in the audit log.*


### test_audit_handler_records_without_envelope_or_close (function, L325-L359)

> *Summary: This test verifies that the audit handler correctly logs an expectation violation when a conversation exceeds a silence threshold, even if no explicit envelope or close event is present in the write-ahead log. It sets up two agents, initiates a timed conversation, advances time past the defined silence limit, and asserts exactly one "max\_silence" violation record appears in the audit log.*


### test_notify_channel_handler_broadcasts_envelope (function, L363-L417)

> *Summary: This test verifies that a custom `notify_channel` handler correctly broadcasts an envelope when a defined expectation, specifically "max\_silence," is violated after advancing the clock. It sets up a simulated network environment with two agents and asserts that exactly one violation envelope is recorded in the Write-Ahead Log (WAL) while the channel remains active.*


### test_violation_dedup_within_channel_lifetime (function, L421-L447)

> *Summary: This test verifies that the system deduplicates identical expectation violations occurring within a single channel's lifetime. It simulates multiple consecutive ticks and asserts that only one violation record is logged for the same event across those ticks.*


### test_audit_log_records_register_and_unregister (function, L454-L469)

> *Summary: This test verifies that the system correctly logs both agent registration and unregistration events to the audit log. It initializes a memory store, registers an agent via a client, unregisters it through the hub, and then asserts that corresponding audit records exist in the log.*


### test_audit_log_records_set_resume_skill_rule (function, L473-L494)

> *Summary: This test verifies that setting a resume, skill, and rule for an agent correctly generates corresponding entries in the audit log. It initializes a knowledge store and hub, performs the updates via a client, and asserts that all three expected audit record types are present after the operations.*


### test_audit_log_writer_round_trips (function, L498-L508)

> *Summary: This test verifies that an `AuditLog` correctly persists and retrieves log entries. It appends two JSON objects to the log using a memory store and asserts that `read_all()` returns them in the exact order they were written.*

