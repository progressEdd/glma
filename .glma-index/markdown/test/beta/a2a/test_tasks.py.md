# test/beta/a2a/test_tasks.py

2 class(es): TestAdmin, TestPushCRUD. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAdmin | class |  |
| TestPushCRUD | class |  |

## Chunks

### TestAdmin (class, L24-L69)

> *Summary: This test suite verifies the core functionality of a task management system by interacting with an in-memory store. It tests retrieving specific tasks, validating the structure returned by listing all tasks, and confirming that canceling an active task correctly updates its state to canceled.*


### test_get_task_returns_completed_task (method, L25-L36, parent: TestAdmin)

> *Summary: This test verifies that retrieving a task returns the correct object when provided with an existing task ID from a list of tasks. It initializes a client, lists available tasks, and then fetches one specific task to assert its identity matches the input.*


### test_list_tasks_returns_listed_tasks_dataclass (method, L38-L52, parent: TestAdmin)

> *Summary: This test verifies that the `list_tasks` function returns a `ListedTasks` dataclass containing at least one task when called against an in-memory store. It asserts the structure and types of the returned object's pagination and size attributes.*


### test_cancel_active_task_marks_it_cancelled (method, L54-L69, parent: TestAdmin)

> *Summary: This test verifies that canceling an active task correctly updates its state to "CANCELED." It sets up a prompt executor, simulates interaction leading to an active task, cancels the task by ID, and then asserts the retrieved task reflects the canceled status.*


### TestPushCRUD (class, L73-L102)

> *Summary: This test verifies the full CRUD lifecycle for push notification configurations associated with a specific task. It creates, lists, retrieves, and then deletes a configuration using an in-memory store setup to ensure data persistence and correct API behavior.*


### test_create_get_list_delete (method, L74-L102, parent: TestPushCRUD)

> *Summary: This test verifies the full lifecycle of push notification configurations by creating a configuration for an existing task, asserting its existence and details via listing and fetching, and finally deleting it to confirm removal. It uses mock in-memory stores to simulate client interactions during this CRUD operation sequence.*

