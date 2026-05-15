# test/beta/network/test_context_vars.py

2 function(s): _agent, _post_context_set. 1 class(es): TestContextVars. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _post_context_set | function |  |
| TestContextVars | class |  |

## Chunks

### _agent (function, L40-L41)

> *Summary: Creates an `Agent` instance using a provided name and constructs a `TestConfig` object from any subsequent string arguments. This function serves to initialize test agents with specific configurations based on input replies.*


### _post_context_set (function, L44-L53)

> *Summary: This asynchronous helper constructs and sends an `EV_CONTEXT_SET` envelope via a provided hub. It takes the hub instance, sender ID, channel ID, and arbitrary event data as input to publish the context update.*


### TestContextVars (class, L57-L355)

> *Summary: This test suite verifies the behavior of context variable mutations within a workflow system, ensuring that `EV_CONTEXT_SET` envelopes correctly update state across different scenarios. It tests persistence across folds, sequential setting and deletion of keys, out-of-turn updates by participants, context-driven transition routing, replayability upon hub restart, and confirmation that context setting does not advance the conversation turn.*


### test_set_persists_across_fold (method, L60-L98, parent: TestContextVars)

> *Summary: This test verifies that context variables set by one agent persist across a communication exchange between two agents within the system's knowledge store. It initializes clients, registers agents, establishes a workflow channel, posts a context set to that channel, and then asserts the context is correctly stored in the hub's state for the channel.*


### test_set_then_delete (method, L100-L144, parent: TestContextVars)

> *Summary: This test verifies that context variables can be set and subsequently deleted within a communication channel. It initializes agents, establishes a workflow between them, sends two sequential context updates (one setting keys, the next deleting one while setting another), and asserts the final state of the channel's context variables.*


### test_loose_semantics_any_participant (method, L146-L185, parent: TestContextVars)

> *Summary: This test verifies that a non-current speaker can successfully post context variables to an active channel. It sets up two agents, initiates a workflow from one agent to another, and then asserts that the receiving agent's state reflects the context set by the other participant.*


### test_context_equals_drives_transition (method, L187-L257, parent: TestContextVars)

> *Summary: This test verifies that a `ContextEquals` transition correctly routes an agent's turn to a specific target based on a value set in the shared context (`EV_CONTEXT_SET`). It sets up three agents and a transition graph, then forces the initial agent to set a "route" context key before sending a message, expecting the flow to proceed directly to the designated security agent.*


### test_hydrate_replays_context_vars (method, L259-L313, parent: TestContextVars)

> *Summary: This test verifies that context variables are correctly reconstructed when a communication hub is closed and reopened against the same persistent store. It simulates setting and deleting context data on a channel, then asserts that the state matches after replaying the write-ahead log upon reopening the hub.*


### test_context_set_does_not_advance_turn (method, L315-L355, parent: TestContextVars)

> *Summary: This test verifies that setting context variables via `_post_context_set` does not alter the conversation state. It initializes a multi-agent communication setup, sends a context update from Alice to Bob, and asserts that both the turn count and the expected next speaker remain unchanged after the operation.*

