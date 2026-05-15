# test/beta/a2a/test_httpx_headers.py

2 function(s): test_factory_client_headers_not_mutated, test_headers_applied_when_no_factory.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_factory_client_headers_not_mutated | function |  |
| test_headers_applied_when_no_factory | function |  |

## Chunks

### test_factory_client_headers_not_mutated (function, L11-L26)

> *Summary: This test verifies that the headers of a shared `httpx.AsyncClient` instance remain unchanged after being passed through a client creation factory function. It asserts that the resulting client object is the original shared instance and its header dictionary matches the initial state.*


### test_headers_applied_when_no_factory (function, L29-L31)

> *Summary: When initialized with a specific header dictionary and no factory, the resulting HTTP client object will correctly contain those headers in its configuration. This test verifies that provided request headers are applied to the client instance.*

