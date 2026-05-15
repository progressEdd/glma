# test/beta/network/test_channel_inbox.py

1 function(s): _agent. 1 class(es): TestChannelInboxInvariant. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| TestChannelInboxInvariant | class |  |

## Chunks

### _agent (function, L42-L43)

> *Summary: Creates and returns an `Agent` instance, configuring it using a provided name and a set of event objects passed as variable arguments.*


### TestChannelInboxInvariant (class, L47-L181)

> *Summary: These tests verify that every agent involved in a channel possesses an inbox for it, regardless of how the channel is opened or if custom handlers are used. They confirm invariants like idempotency and successful message handling across asynchronous operations involving channel creation and closure.*


### test_creator_has_inbox_after_open (method, L50-L65, parent: TestChannelInboxInvariant)

> *Summary: This test verifies that a creator agent receives an inbox after successfully opening a communication channel to another registered agent. It sets up a simulated network environment, registers two agents, opens a channel from Alice to Bob, and asserts the channel ID is present in Alice's internal inbox structure.*


### test_default_handler_joiner_has_inbox (method, L67-L84, parent: TestChannelInboxInvariant)

> *Summary: This test verifies that when an agent opens a channel to another agent, the recipient's inbox is created automatically by the default handler upon receiving the invite. It sets up two clients connected via a shared hub and asserts the presence of the new channel in the target client's inbox structure.*


### test_custom_handler_joiner_has_inbox (method, L86-L130, parent: TestChannelInboxInvariant)

> *Summary: Verifies that a joiner with a custom handler still receives an inbox even if the invite is ignored by the handler, demonstrating that the `receive()` hook fires before handler execution. It sets up two clients, initiates an open request from one to the other, and asserts the target client possesses the channel's inbox.*


### test_ensure_channel_inbox_is_idempotent (method, L132-L145, parent: TestChannelInboxInvariant)

> *Summary: This test verifies that calling the `ensure_channel_inbox` method multiple times with the same channel ID returns the exact same object instance. It sets up a local communication environment using an in-memory store and asserts referential equality between two consecutive calls.*


### test_send_sleep_wait_no_race (method, L147-L181, parent: TestChannelInboxInvariant)

> *Summary: This test verifies that a communication sequence remains stable even when an asynchronous sleep occurs between sending a message and waiting for the response. It sets up two agents, sends a message from Alice to Bob, pauses execution, and then asserts that the expected channel closure event is received by Alice without timing out or being dropped due to race conditions.*

