# autogen/beta/a2a/tasks.py

4 function(s): _resolve_history, cancel_task, get_task, list_tasks. 1 class(es): ListedTasks.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ListedTasks | class |  |
| _resolve_history | function |  |
| cancel_task | function |  |
| get_task | function |  |
| list_tasks | function |  |

## Chunks

### ListedTasks (class, L24-L35)

> *Summary: Represents the structured output from a task listing operation, containing a list of `Task` objects. It also includes pagination metadata like the next page token, the size of the current page, and the total count across all pages.*


### _resolve_history (function, L38-L40)

> *Summary: Determines the effective history length by prioritizing an explicit `override` value; otherwise, it defaults to the configured `config.history_length`. Returns either the provided override or the configuration's default integer value.*


### cancel_task (function, L43-L55)

> *Summary: This asynchronous function cancels a specified task by interacting with the configured service SDK. It accepts configuration, a unique task ID, and optional tenant/metadata to forward during cancellation.*


### get_task (function, L58-L71)

> *Summary: Retrieves a specific task by ID from the configured service using an SDK session. It optionally filters the returned task's history based on a provided length parameter, which is passed to the underlying API call.*


### list_tasks (function, L74-L111)

> *Summary: Retrieves a paginated list of tasks from the system based on various optional filters like status, tenant, and page tokens. It returns a structure containing the current page's tasks along with metadata for subsequent pagination calls.*

