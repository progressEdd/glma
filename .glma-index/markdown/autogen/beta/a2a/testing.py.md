# autogen/beta/a2a/testing.py

3 function(s): make_test_client_factory, make_test_rest_client_factory, pick_free_port.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| make_test_client_factory | function |  |
| make_test_rest_client_factory | function |  |
| pick_free_port | function |  |

## Chunks

### make_test_client_factory (function, L14-L49)

> *Summary: Creates a callable function that produces an `httpx.AsyncClient` configured to communicate with a provided server instance in-process via its Starlette application. This factory is designed for end-to-end testing by bypassing network sockets and using the server's internal JSON-RPC endpoint.*


### make_test_rest_client_factory (function, L52-L74)

> *Summary: Creates a function that yields an `httpx.AsyncClient` configured to communicate via REST with a specified server instance. It builds the necessary Starlette application using the provided server and URL, ensuring the client only interacts through the REST interface.*


### pick_free_port (function, L77-L88)

> *Summary: This function finds an available TCP port on a specified host by binding a temporary socket to port zero. It returns the assigned port number, which is useful for setting up real listening sockets in gRPC tests.*

