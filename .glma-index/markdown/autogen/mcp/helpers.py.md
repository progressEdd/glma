# autogen/mcp/helpers.py

1 function(s): run_streamable_http_client.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| run_streamable_http_client | function |  |

## Chunks

### run_streamable_http_client (function, L13-L45)

> *Summary: This asynchronous generator launches a Python subprocess to run a streamable-http server, allowing the caller to manage its lifecycle. It accepts the server script path and optional environment variables, yielding the running process until it is gracefully terminated or forcefully killed upon exiting the context.*

