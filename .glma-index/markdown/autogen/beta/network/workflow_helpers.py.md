# autogen/beta/network/workflow_helpers.py

3 function(s): _ensure_workflow, set_context, delete_context.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _ensure_workflow | function |  |
| set_context | function |  |
| delete_context | function |  |

## Chunks

### _ensure_workflow (function, L32-L40)

> *Summary: Verifies that the provided `Channel` object is specifically a workflow type by checking its metadata manifest. If it's not a workflow channel, it raises a `RuntimeError`, ensuring helper functions operate only within the correct execution context.*


### set_context (function, L43-L56)

> *Summary: This asynchronous function updates a workflow's context by sending an `EV_CONTEXT_SET` event to the specified channel. It allows any participant to set a key-value pair in the shared context variables, which becomes visible to all after the fold operation.*


### delete_context (function, L59-L70)

> *Summary: This asynchronous function removes a specific workflow context variable from a given channel by sending an `EV_CONTEXT_SET` envelope containing the key to be deleted. It performs no action if the specified key was not previously set in the context.*

