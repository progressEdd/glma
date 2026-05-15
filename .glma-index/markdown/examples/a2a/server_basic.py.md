# examples/a2a/server_basic.py

2 function(s): calc_add, main.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| calc_add | function |  |
| main | function |  |

## Chunks

### calc_add (function, L12-L13)

> *Summary: This asynchronous function takes two integers as input and returns their sum converted to a string. It performs simple addition on the provided numerical arguments.*


### main (function, L23-L28)

> *Summary: Initializes an A2A server instance using a provided agent and constructs a JSON-RPC ASGI application with a specific card configuration. It then starts serving this application asynchronously on `http://127.0.0.1:8000`.*

