# autogen/beta/network/hub/listener.py

2 class(es): HubListener, BaseHubListener. 18 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| HubListener | class |  |
| BaseHubListener | class |  |

## Chunks

### HubListener (class, L40-L175)

> *Summary: Defines an observer protocol for reacting to various state transitions within a communication hub. Implementations receive asynchronous callbacks for events like envelope posting/rejection, channel lifecycle changes, agent identity updates, and task status changes.*


### on_envelope_posted (method, L47-L52, parent: HubListener)

> *Summary: Receives a validated `Envelope` and associated `ChannelMetadata` to signify that the message has been successfully processed through validation, Write-Ahead Log appending, folding, and dispatching. This method handles the completion of the envelope's lifecycle within the network hub.*


### on_envelope_rejected (method, L54-L65, parent: HubListener)

> *Summary: Handles an envelope that was rejected by the network before being written to the Write-Ahead Log. It receives the rejected `Envelope` and a specific `NetworkError` reason, allowing consumers to track rejection rates for monitoring or alerting.*


### on_dispatch_failed (method, L67-L79, parent: HubListener)

> *Summary: Handles failures when an accepted message envelope fails to deliver to a specific recipient. It receives the failed `Envelope`, the target `recipient_id`, and the exception `reason` to log or manage the delivery error, while noting that the sender's initial post operation remains successful due to WAL commitment.*


### on_channel_event (method, L81-L93, parent: HubListener)

> *Summary: Handles lifecycle events for a specific channel by receiving the `channel_id`, an event type (`kind`), and associated data in the `payload`. It processes various state changes such as opening, closing, or participant modifications.*


### on_agent_event (method, L95-L108, parent: HubListener)

> *Summary: Receives an asynchronous event from a specific agent, identifying the event type and carrying associated data in a dictionary payload. This method handles lifecycle events such as registration, unregistration, or observation recording.*


### on_expectation_fired (method, L110-L121, parent: HubListener)

> *Summary: When an expectation evaluator signals a violation for a specific channel and expectation, this method is called. It processes the received `channel_id`, `expectation`, and `violation` objects to handle the emitted event.*


### on_turn_failed (method, L123-L137, parent: HubListener)

> *Summary: This asynchronous handler receives notification when processing an inbound message fails due to an exception. It captures errors from agent requests or envelope building without sending a reply, allowing the application logic to decide on recovery actions like retrying or escalating.*


### on_task_event (method, L139-L152, parent: HubListener)

> *Summary: Receives lifecycle events for a specific task, identified by `task_id`, detailing its state change (`kind`) and associated data (`payload`). This method processes various states like "started," "completed," or "failed" to manage the task's progression within the system.*


### on_inbox_pressure (method, L154-L167, parent: HubListener)

> *Summary: This asynchronous method signals when an agent's inbox exceeds its high-water mark, receiving the agent ID, current pending count, and capacity as input. It triggers only once per crossing event, allowing external systems to implement backpressure or alerts based on this state change.*


### BaseHubListener (class, L182-L210)

> *Summary: Provides a default, no-operation implementation for handling various asynchronous events within the hub system. Developers should override specific methods to react to inputs like posted envelopes, rejected messages, or channel/agent activity.*


### on_envelope_posted (method, L185-L186, parent: BaseHubListener)

> *Summary: This asynchronous method receives an `envelope` and associated `metadata`, currently serving as a placeholder that returns nothing. It is intended to handle the event when an envelope has been posted.*


### on_envelope_rejected (method, L188-L189, parent: BaseHubListener)

> *Summary: This asynchronous method handles the rejection of a message envelope. It accepts an `envelope` and a `reason` as input but currently performs no action, returning nothing.*


### on_dispatch_failed (method, L191-L192, parent: BaseHubListener)

> *Summary: This asynchronous method handles dispatch failures by accepting an envelope, a recipient ID, and a failure reason as input. It currently returns nothing, indicating no specific action is taken upon receiving a failed dispatch notification.*


### on_channel_event (method, L194-L195, parent: BaseHubListener)

> *Summary: This asynchronous method receives a `channel_id`, event `kind`, and associated `payload` to process incoming channel events. Currently, it does nothing and returns immediately.*


### on_agent_event (method, L197-L198, parent: BaseHubListener)

> *Summary: This asynchronous method receives an agent ID, event type, and associated data. It currently does nothing with the inputs, returning `None`.*


### on_expectation_fired (method, L200-L201, parent: BaseHubListener)

> *Summary: This asynchronous method handles the event when an expectation is triggered within a specific communication channel. It accepts the channel ID, the fired expectation object, and any associated violation details as input, returning nothing upon execution.*


### on_turn_failed (method, L203-L204, parent: BaseHubListener)

> *Summary: This asynchronous method handles the failure of a turn within a communication channel. It accepts identifiers for the channel, agent, and message envelope, along with the exception that caused the failure, but currently performs no action other than returning `None`.*


### on_task_event (method, L206-L207, parent: BaseHubListener)

> *Summary: This asynchronous method receives a `task_id`, event `kind`, and associated `payload` to process lifecycle events related to tasks. Currently, it does nothing but return `None`.*


### on_inbox_pressure (method, L209-L210, parent: BaseHubListener)

> *Summary: This asynchronous method accepts an agent ID, the number of pending items, and a capacity value. It currently does nothing, effectively acting as a placeholder for handling inbox pressure notifications.*

