# autogen/beta/middleware/builtin/tools/approval.py

1 function(s): approval_required.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| approval_required | function |  |

## Chunks

### approval_required (function, L16-L70)

> *Summary: Creates a tool middleware hook that intercepts tool calls to request human approval before execution. It takes a prompt template, denial message, timeout, and an `allow_always` flag as input, returning a function that either executes the call or returns a denied result based on user input.*

