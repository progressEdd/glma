# test/beta/network/test_expectations_boundary.py

7 function(s): _conv_meta, _ctx, _inject_pending_channel, test_handler_exception_does_not_stop_sweeper, test_two_same_name_expectations_with_different_handlers_both_fire, test_unknown_evaluator_name_silently_ignored, test_unknown_handler_name_silently_ignored. 3 class(es): _NoOpAdapter, TestEvaluatorExactBoundary, TestEvaluatorZeroTimeout. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _NoOpAdapter | class |  |
| _conv_meta | function |  |
| _ctx | function |  |
| _inject_pending_channel | function |  |
| TestEvaluatorExactBoundary | class |  |
| TestEvaluatorZeroTimeout | class |  |
| test_handler_exception_does_not_stop_sweeper | function |  |
| test_two_same_name_expectations_with_different_handlers_both_fire | function |  |
| test_unknown_evaluator_name_silently_ignored | function |  |
| test_unknown_handler_name_silently_ignored | function |  |

## Chunks

### _NoOpAdapter (class, L61-L89)

> *Summary: This class provides a minimal adapter implementation for expectation testing, allowing the sweeper to read channel manifests and active channels without executing any validation or state-changing logic. It accepts a `ChannelManifest` upon initialization and returns empty or default values for all operational methods.*


### __init__ (method, L70-L71, parent: _NoOpAdapter)

> *Summary: Initializes an object by storing a provided `ChannelManifest` instance as its internal state. This sets up the necessary context for subsequent operations within the class.*


### initial_state (method, L73-L74, parent: _NoOpAdapter)

> *Summary: Returns an empty dictionary when provided with channel metadata. This method establishes the starting state for a network test scenario.*


### fold (method, L76-L77, parent: _NoOpAdapter)

> *Summary: This method takes an `Envelope` and a dictionary state as input, returning the state dictionary unchanged. It serves to pass the existing state through without modification during a folding operation.*


### validate_create (method, L79-L80, parent: _NoOpAdapter)

> *Summary: This method performs no validation on the provided `ChannelMetadata` object; it simply returns immediately. It accepts one argument of type `ChannelMetadata` and produces no output.*


### validate_send (method, L82-L83, parent: _NoOpAdapter)

> *Summary: This method performs no validation logic, accepting channel metadata, an envelope, and a state dictionary as input. It simply returns immediately without producing any output.*


### on_accepted (method, L85-L86, parent: _NoOpAdapter)

> *Summary: This method accepts channel metadata, an envelope, and a state dictionary as input. It immediately returns a successful `AdapterResult` without performing any further logic.*


### default_view_policy (method, L88-L89, parent: _NoOpAdapter)

> *Summary: This method returns a new `FullTranscript` object when provided with channel metadata and a participant ID. It serves as the default behavior for determining transcript content without specific logic.*


### _conv_meta (function, L92-L110)

> *Summary: Constructs a `ChannelMetadata` object using predefined values for the manifest and participant list. It accepts optional inputs like channel state, creation timestamp, and pending acknowledgments to configure the metadata structure.*


### _ctx (function, L113-L121)

> *Summary: Creates an `ExpectationContext` object by parsing a provided timestamp string into datetime objects and initializing the context with channel metadata and optional Write-Ahead Log data. This function prepares the necessary state for testing network interactions based on the given inputs.*


### _inject_pending_channel (function, L124-L153)

> *Summary: This function manually inserts a `PENDING` channel metadata object into the hub's internal caches. It takes a hub, channel ID, adapter key, clock, and optional pending acknowledgments as input, returning the created `ChannelMetadata`.*


### TestEvaluatorExactBoundary (class, L156-L201)

> *Summary: This test suite verifies that various time-based evaluators correctly trigger violations exactly at specified thresholds, while remaining silent just before those boundaries. It uses evaluator instances with expectations to check for non-null or null violation outputs based on the current time provided in the context.*


### test_acks_within_fires_at_exact_threshold (method, L159-L166, parent: TestEvaluatorExactBoundary)

> *Summary: This test verifies that an `AcksWithinEvaluator` triggers a violation when the elapsed time exactly matches the configured threshold (30 seconds). It uses a specific channel state and checks that the resulting violation correctly identifies "bob" as the violator.*


### test_acks_within_silent_just_under_threshold (method, L168-L174, parent: TestEvaluatorExactBoundary)

> *Summary: This test verifies that acknowledgments are considered within the acceptable timeframe when they occur just under a specified threshold. It evaluates an `AcksWithinEvaluator` against a state where pending ACKs exist, asserting no violation occurs at $29.999$ seconds for a 30-second limit.*


### test_max_silence_fires_at_exact_threshold (method, L176-L181, parent: TestEvaluatorExactBoundary)

> *Summary: This test verifies that the `MaxSilenceEvaluator` triggers a violation when the silence duration exactly meets the configured threshold. It evaluates an expectation set for 60 seconds against a context where one minute has passed since the channel became active.*


### test_reply_within_fires_at_exact_threshold (method, L183-L201, parent: TestEvaluatorExactBoundary)

> *Summary: This test verifies that a `ReplyWithinEvaluator` triggers an alert when the time elapsed exactly matches the configured threshold (60 seconds). It uses a specific metadata and event log to confirm the evaluation correctly identifies the violator ("bob").*


### TestEvaluatorZeroTimeout (class, L204-L220)

> *Summary: This test suite verifies that time-based expectations with a zero timeout fire immediately upon evaluation. It confirms this behavior for both an `AcksWithinEvaluator` and a `MaxSilenceEvaluator` when the current time matches the state's creation or relevant timestamp.*


### test_acks_within_zero_fires_immediately (method, L207-L213, parent: TestEvaluatorZeroTimeout)

> *Summary: This test verifies that an `AcksWithinEvaluator` immediately triggers a violation when the specified time threshold is zero. It evaluates an expectation configured for zero seconds against a pending channel state, asserting that a violation object is returned instantly.*


### test_max_silence_zero_fires_immediately (method, L215-L220, parent: TestEvaluatorZeroTimeout)

> *Summary: When evaluating a `MaxSilenceEvaluator` with an expectation set to zero seconds, the function immediately produces a violation when given active channel metadata and the current time. This confirms that zero silence tolerance triggers an immediate alert.*


### test_handler_exception_does_not_stop_sweeper (function, L224-L275)

> *Summary: This test verifies that a custom violation handler which raises an exception does not crash the main sweeper loop or prevent subsequent ticks from processing correctly. It simulates a single tick where the crashing handler fires, followed by a second tick confirming the handler is suppressed due to deduplication.*


### test_two_same_name_expectations_with_different_handlers_both_fire (function, L279-L340)

> *Summary: This test verifies that when a manifest lists the same expectation name multiple times with different violation handlers, both handlers fire correctly upon crossing their respective thresholds. It simulates time progression to ensure an earlier threshold triggers one handler while a later threshold triggers both handlers for the same named expectation.*


### test_unknown_evaluator_name_silently_ignored (function, L344-L373)

> *Summary: This test verifies that the system gracefully handles an expectation referencing an unregistered evaluator by silently skipping it during a sweep tick. It sets up a mock environment with a bogus channel manifest containing such an expectation and asserts that no exception is raised when ticking the expectations.*


### test_unknown_handler_name_silently_ignored (function, L377-L411)

> *Summary: This test verifies that when an expectation is triggered but no corresponding handler is registered, the system silently ignores the event and continues processing without logging any violations. It simulates a channel event, advances time, calls the tick function, and asserts that the audit log remains empty of violation records.*

