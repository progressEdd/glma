# test/beta/network/test_client_lifecycle.py

1 function(s): _agent. 1 class(es): TestClientLifecycle. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| TestClientLifecycle | class |  |

## Chunks

### _agent (function, L34-L35)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default `TestConfig`. This function serves to instantiate test agents for network simulations.*


### TestClientLifecycle (class, L39-L105)

> *Summary: This test suite verifies the proper resource cleanup mechanisms for client interactions with a central `Hub`. It confirms that exiting context managers (`async with`) correctly closes clients, unregisters agents from the hub registry, and ensures these cleanup routines execute even when exceptions occur within the managed blocks.*


### test_hub_client_close_runs_on_exit (method, L42-L52, parent: TestClientLifecycle)

> *Summary: This test verifies that the `HubClient` correctly signals closure when exiting its asynchronous context manager. It initializes a hub and client, asserts the client is open before the block, and then confirms it is closed after the block completes.*


### test_agent_client_unregister_runs_on_exit (method, L54-L77, parent: TestClientLifecycle)

> *Summary: This test verifies that an agent client automatically unregisters itself from the central hub registry upon exiting its context manager. It confirms that after the block exits, the agent is marked as locally disconnected and no longer discoverable via the hub.*


### test_cleanup_runs_on_exception (method, L79-L105, parent: TestClientLifecycle)

> *Summary: This test verifies that cleanup methods execute even when an exception occurs within the main execution block. It sets up a client, registers an agent, intentionally raises an error, and then asserts that both the agent's context manager (`__aexit__`) and the client's context manager (`__aexit__`) successfully ran to clean up resources.*

