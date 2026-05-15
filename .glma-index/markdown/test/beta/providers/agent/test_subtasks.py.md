# test/beta/providers/agent/test_subtasks.py

6 function(s): test_run_subtask_auto_injected, test_run_subtasks_parallel, test_subtask_prompt_override, test_actor_as_tool_delegation, test_subtask_cannot_recurse, test_persistent_stream_shares_history.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_run_subtask_auto_injected | function |  |
| test_run_subtasks_parallel | function |  |
| test_subtask_prompt_override | function |  |
| test_actor_as_tool_delegation | function |  |
| test_subtask_cannot_recurse | function |  |
| test_persistent_stream_shares_history | function |  |

## Chunks

### test_run_subtask_auto_injected (function, L23-L51)

> *Summary: This test verifies that an agent, configured to use subtasks, correctly dispatches and completes a spawned task when prompted with a specific question. It asserts that at least one task starts and completes, linking the start and completion events while confirming the final response contains the expected answer.*


### test_run_subtasks_parallel (function, L54-L84)

> *Summary: This test verifies that an agent correctly utilizes a parallel execution capability when prompted with multiple independent questions. It sends a request to the agent and asserts that the resulting stream contains completions for all expected subtasks concurrently.*


### test_subtask_prompt_override (function, L87-L120)

> *Summary: This test verifies that a custom prompt configured via `TaskConfig` successfully overrides the default system prompt for subtasks. It injects a unique watermark token into the override and asserts that this token appears verbatim in the resulting completed subtask outputs, while also confirming the correct answer is present.*


### test_actor_as_tool_delegation (function, L123-L143)

> *Summary: This test verifies that an agent can delegate a task to another agent exposed as a tool. It initializes two agents, one specialized for math and another coordinator, then asserts the coordinator correctly uses the expert's tool to solve a calculation.*


### test_subtask_cannot_recurse (function, L146-L178)

> *Summary: This test verifies that a parent agent cannot recursively spawn subtasks. It intercepts task execution to capture any spawned agents and asserts that the resulting subtask lacks `run_subtask` tools and has no associated task configuration.*


### test_persistent_stream_shares_history (function, L181-L229)

> *Summary: This test verifies that `persistent_stream()` correctly maintains state across multiple tool calls by ensuring both child invocations receive a stream with the identical ID and share the same underlying storage backend. It achieves this by wrapping the stream factory to capture and assert these structural invariants after two sequential agent interactions.*

