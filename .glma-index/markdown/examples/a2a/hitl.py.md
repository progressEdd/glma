# examples/a2a/hitl.py

2 function(s): hitl_hook, main.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| hitl_hook | function |  |
| main | function |  |

## Chunks

### hitl_hook (function, L7-L8)

> *Summary: This asynchronous function prompts the user for text input from the console and returns the entered string after executing it in a separate thread. It serves as an interactive hook to gather external data during execution.*


### main (function, L11-L18)

> *Summary: Initializes a remote agent configured to communicate with a local service and uses a human-in-the-loop hook for interaction. It then sends the prompt "start" to the agent and prints the resulting response content.*

