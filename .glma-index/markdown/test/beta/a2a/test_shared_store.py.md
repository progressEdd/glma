# test/beta/a2a/test_shared_store.py

3 function(s): test_default_task_store_is_materialised_eagerly, test_user_task_store_is_preserved, test_task_store_persists_across_build_calls.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_default_task_store_is_materialised_eagerly | function |  |
| test_user_task_store_is_preserved | function |  |
| test_task_store_persists_across_build_calls | function |  |

## Chunks

### test_default_task_store_is_materialised_eagerly (function, L16-L18)

> *Summary: Verifies that the default task store within an initialized `A2AServer` instance is immediately materialized as a `TaskStore`. It confirms the correct type of the internal task storage mechanism upon server setup.*


### test_user_task_store_is_preserved (function, L21-L24)

> *Summary: Verifies that the `A2AServer` instance correctly holds a reference to the provided `InMemoryTaskStore`. It confirms the server's internal task store attribute matches the input store object.*


### test_task_store_persists_across_build_calls (function, L28-L40)

> *Summary: This test verifies that the task store maintains its state across server build operations. It initializes a client/server pair, checks for existing tasks, forces a server rebuild, and then asserts that the set of task IDs remains unchanged after the rebuild.*

