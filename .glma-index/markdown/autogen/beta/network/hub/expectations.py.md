# autogen/beta/network/hub/expectations.py

4 function(s): _parse_iso_seconds, _is_content_event, default_evaluators, default_handlers. 10 class(es): Violation, ExpectationContext, ExpectationEvaluator, ViolationHandler, AcksWithinEvaluator, ReplyWithinEvaluator, MaxSilenceEvaluator, AuditHandler, NotifyChannelHandler, AutoCloseHandler. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Violation | class |  |
| ExpectationContext | class |  |
| ExpectationEvaluator | class |  |
| ViolationHandler | class |  |
| _parse_iso_seconds | function |  |
| _is_content_event | function |  |
| AcksWithinEvaluator | class |  |
| ReplyWithinEvaluator | class |  |
| MaxSilenceEvaluator | class |  |
| AuditHandler | class |  |
| NotifyChannelHandler | class |  |
| AutoCloseHandler | class |  |
| default_evaluators | function |  |
| default_handlers | function |  |

## Chunks

### Violation (class, L63-L73)

> *Summary: Represents the outcome when an evaluator triggers a violation. It stores the associated `Expectation`, a list of participant IDs affected by the violation (or none for channel-wide issues), and any additional diagnostic details.*


### ExpectationContext (class, L77-L84)

> *Summary: Provides a context object containing metadata, current state, a log of events (WAL), and timestamps for every evaluator during a simulation tick. This structure is passed to all evaluators to give them necessary runtime information.*


### ExpectationEvaluator (class, L87-L101)

> *Summary: Defines a protocol for an evaluator that checks if certain conditions are met based on provided metadata and state. It must deterministically return `None` if no violation is present or a `Violation` object otherwise.*


### evaluate (method, L97-L101, parent: ExpectationEvaluator)

> *Summary: This method assesses a given `Expectation` against the provided `ExpectationContext`. It returns either a `Violation` object if the expectation is not met or `None` otherwise.*


### ViolationHandler (class, L104-L121)

> *Summary: Defines a protocol for handling evaluation violations within the hub. Implementations must provide an asynchronous `handle` method that accepts the hub instance, channel ID, and the violation object.*


### handle (method, L116-L121, parent: ViolationHandler)

> *Summary: This asynchronous method processes a detected violation within a specific channel. It takes the hub instance, the channel ID, and the violation object as input to perform its handling logic.*


### _parse_iso_seconds (function, L127-L128)

> *Summary: Converts an ISO formatted string representing a time into a Unix timestamp (float). It takes one string input and returns the corresponding floating-point timestamp.*


### _is_content_event (function, L131-L137)

> *Summary: Determines if an incoming event represents substantive content rather than a protocol or task message. It returns `False` for events starting with "ag2.channel." or "ag2.task.", and only returns `True` if the type is not `EV_EXPECTATION_VIOLATED`.*


### AcksWithinEvaluator (class, L140-L169)

> *Summary: Checks if invitees have acknowledged an invitation within a specified time limit while the channel is in `PENDING` state. If the elapsed time exceeds the threshold and there are pending acknowledgments, it returns a violation listing all non-responding invitee IDs.*


### evaluate (method, L149-L169, parent: AcksWithinEvaluator)

> *Summary: Checks if a specified time threshold has passed and if pending acknowledgments exist within the current context. If both conditions are met, it returns a `Violation` object detailing the failure; otherwise, it returns `None`.*


### ReplyWithinEvaluator (class, L172-L230)

> *Summary: Determines if any participant has failed to reply within a specified time limit after receiving a message. It scans the event log to find the latest incoming and outgoing text events for each agent, then checks if the time elapsed since the last received message exceeds the configured threshold. If violations are found, it returns a `Violation` object listing the non-responsive agents; otherwise, it returns `None`.*


### evaluate (method, L183-L230, parent: ReplyWithinEvaluator)

> *Summary: Checks if a specific communication expectation is violated by participants within the current active channel state. It analyzes the latest sent and received text messages for each participant to determine if the time elapsed since receiving a message exceeds a configured threshold. Returns `None` if no violation occurs, or a `Violation` object detailing the offending agent IDs otherwise.*


### MaxSilenceEvaluator (class, L233-L266)

> *Summary: Determines if a channel has been silent for a specified duration by checking the time since the last content event or channel creation. It returns a `Violation` object if the elapsed time exceeds the configured threshold, otherwise it returns `None`.*


### evaluate (method, L243-L266, parent: MaxSilenceEvaluator)

> *Summary: Checks if a specified time duration has passed since the last content event within an active channel context. It calculates the elapsed time against a threshold defined in the expectation and returns a `Violation` object if the duration is insufficient.*


### AuditHandler (class, L272-L290)

> *Summary: This handler acts as a no-operation sink for audit events, ensuring backward compatibility with older manifests that specify `"audit"` for violation handling. It receives the hub, channel ID, and a `Violation` object but performs no action other than returning immediately.*


### handle (method, L284-L290, parent: AuditHandler)

> *Summary: This asynchronous method processes a detected violation within a specific channel of the hub. It accepts the `Hub` instance, the target `channel_id`, and the `Violation` object as input, returning nothing upon completion.*


### NotifyChannelHandler (class, L293-L324)

> *Summary: This handler broadcasts an `EV_EXPECTATION_VIOLATED` event to all participants in a specified channel, provided the channel is active and not terminal. It constructs an envelope containing details about the violated expectation and the IDs of the violating entities before attempting to post it via the hub.*


### handle (method, L301-L324, parent: NotifyChannelHandler)

> *Summary: When an expectation is violated within a channel, this method constructs and attempts to publish an `EV_EXPECTATION_VIOLATED` envelope via the provided hub. It checks if the channel exists and is not terminal before broadcasting the violation details, including the expectation name and violator IDs.*


### AutoCloseHandler (class, L327-L348)

> *Summary: When an expectation is violated on a channel managed by the Hub, this handler asynchronously closes that channel with a specific reason indicating which expectation failed. It first checks if the channel exists and isn't already terminal before proceeding with the closure attempt.*


### handle (method, L335-L348, parent: AutoCloseHandler)

> *Summary: If a channel exists and is not terminal, this method asynchronously closes the specified channel upon receiving a `Violation` object. The closure reason is derived from the name of the violated expectation.*


### default_evaluators (function, L354-L355)

> *Summary: Returns a list containing three predefined evaluation strategies: one for acknowledging messages, one for checking replies, and one for detecting maximum silence. These evaluators are used to assess the behavior of agents in an automated conversation setup.*


### default_handlers (function, L358-L359)

> *Summary: Returns a predefined list of handler objects, including audit, notification, and automatic closing mechanisms. These handlers are intended to manage various system events or violations within the network hub context.*

