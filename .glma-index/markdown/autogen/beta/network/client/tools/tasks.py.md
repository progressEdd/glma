# autogen/beta/network/client/tools/tasks.py

2 function(s): _task_summary, make_tasks_tool.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _task_summary | function |  |
| make_tasks_tool | function |  |

## Chunks

### _task_summary (function, L42-L56)

> *Summary: Constructs a dictionary summarizing task metadata by extracting key attributes like ID, owner, title, state, and timestamps from the input `meta` object. This function provides a structured overview of a specific task's current status and history.*


### make_tasks_tool (function, L59-L152)

> *Summary: Generates a callable tool that manages the lifecycle of background tasks by accepting an `action` string and various optional parameters. It allows for actions like updating task progress, completing tasks, listing active/all tasks based on scope, checking a specific task's status, or waiting until a task reaches a terminal state within a timeout.*

