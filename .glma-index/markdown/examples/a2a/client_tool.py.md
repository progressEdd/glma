# examples/a2a/client_tool.py

2 function(s): get_local_time, main.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_local_time | function |  |
| main | function |  |

## Chunks

### get_local_time (function, L10-L11)

> *Summary: Retrieves the current system time and returns it as an ISO 8601 formatted string with second precision. This function takes no inputs and outputs a standardized timestamp string.*


### main (function, L14-L21)

> *Summary: Initializes a remote agent configured to communicate with a local service and provides it with access to the `get_local_time` tool. It then queries this remote agent about the local time and prints the resulting response content.*

