# test/beta/network/test_workflow_termination.py

1 function(s): _agent. 1 class(es): TestWorkflowTerminationReason. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| TestWorkflowTerminationReason | class |  |

## Chunks

### _agent (function, L40-L42)

> *Summary: Creates an `Agent` instance configured with a `TestConfig`, which is initialized using the provided name and a sequence of reply strings. This setup allows the agent to emit those replies sequentially when queried via `Agent.ask`.*


### TestWorkflowTerminationReason (class, L46-L228)

> *Summary: This test suite verifies the precedence rules for workflow termination within a communication graph, specifically comparing when sequence completion, maximum turn limits, or explicit target terminations take effect. It uses mock agents and a central Hub to simulate various interaction patterns (sequence, round-robin) and asserts that the correct closing reason is reported upon channel closure.*


### test_sequence_closes_with_sequence_complete (method, L49-L89, parent: TestWorkflowTerminationReason)

> *Summary: This test verifies that a workflow sequence correctly terminates when all defined steps are completed. It sets up three agents, defines a transition graph with a specific order, initiates the sequence via a channel send, and asserts that the resulting channel closure reason is "sequence\_complete".*


### test_round_robin_closes_with_max_turns (method, L91-L131, parent: TestWorkflowTerminationReason)

> *Summary: This test verifies that a round-robin workflow terminates correctly when the specified maximum number of turns is reached. It initializes three agents, sets up a `TransitionGraph` with a turn limit of 6, sends an initial kickoff message, and asserts that the resulting channel closes specifically due to reaching the "max\_turns" condition.*


### test_explicit_terminate_target_wins_over_max_turns (method, L133-L183, parent: TestWorkflowTerminationReason)

> *Summary: This test verifies that an explicit `TerminateTarget` overrides a configured `max_turns` limit within a workflow graph. It sets up three agents and a transition graph where the final step explicitly terminates with "custom\_done," asserting this reason is returned even though the turn limit would otherwise trigger.*


### test_max_turns_wins_when_no_terminate_fires (method, L185-L228, parent: TestWorkflowTerminationReason)

> *Summary: This test verifies that a workflow terminates after reaching its `max_turns` limit when no explicit termination condition is met. It sets up two agents in an alternating communication loop within a graph configured with a turn limit of four, asserting the final closure reason is "max\_turns".*

