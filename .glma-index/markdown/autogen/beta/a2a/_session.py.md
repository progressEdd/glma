# autogen/beta/a2a/_session.py

2 function(s): with_tenant, open_session.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| with_tenant | function |  |
| open_session | function |  |

## Chunks

### with_tenant (function, L15-L26)

> *Summary: This function injects a `tenant` identifier into the provided keyword arguments based on an explicit override or the configuration setting. It prioritizes the `override` value, and only adds the key to the returned dictionary if a tenant is actually specified.*


### open_session (function, L30-L58)

> *Summary: This asynchronous generator establishes a temporary A2A SDK client for single RPC calls by first creating an `httpx` client and resolving the necessary agent card. It yields the configured SDK instance, ensuring the underlying HTTP client is properly closed upon exiting the context manager.*

