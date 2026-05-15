# autogen/beta/tools/subagents/run_task.py

3 function(s): _reply_usage, _make_hitl_bridge, run_task. 1 class(es): TaskResult.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TaskResult | class |  |
| _reply_usage | function |  |
| _make_hitl_bridge | function |  |
| run_task | function |  |

## Chunks

### TaskResult (class, L24-L31)

> *Summary: Represents the outcome of a task execution, holding identifiers, objectives, and the final result or error. It encapsulates status flags like completion and provides metrics on resource usage.*


### _reply_usage (function, L34-L38)

> *Summary: Extracts structured usage information from an `AgentReply` object; if the reply or its response lacks usage data, it returns a default empty `Usage` instance.*


### _make_hitl_bridge (function, L41-L53)

> *Summary: This function creates and returns an asynchronous bridge handler that forwards `HumanInputRequest` events from a child stream to the provided parent context's stream. It captures the parent context at definition time to avoid performance overhead during runtime execution.*


### run_task (function, L56-L153)

> *Summary: Executes an agent as a subordinate task using a given objective and optional context, returning a `TaskResult`. It manages lifecycle events (start/complete/fail) on the parent stream and handles human input requests by bridging them to the parent's stream if the agent lacks its own hook.*

