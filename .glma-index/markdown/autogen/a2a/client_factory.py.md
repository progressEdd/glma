# autogen/a2a/client_factory.py

1 function(s): MockClient. 3 class(es): ClientFactory, HttpxClientFactory, EmptyClientFactory. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ClientFactory | class |  |
| HttpxClientFactory | class |  |
| EmptyClientFactory | class |  |
| MockClient | function |  |

## Chunks

### ClientFactory (class, L33-L36)

> *Summary: Defines a contract for factories capable of producing asynchronous and synchronous client instances. It requires methods to instantiate both `AsyncClient` and standard `Client` objects upon invocation or explicit calls.*


### __call__ (method, L34-L34, parent: ClientFactory)

> *Summary: When invoked, this method constructs and returns an `AsyncClient` instance. It acts as a factory to provide the necessary asynchronous client object upon calling the instance.*


### make_sync (method, L36-L36, parent: ClientFactory)

> *Summary: Creates and returns a synchronous client instance based on the object's configuration. This method abstracts the instantiation process to provide a ready-to-use, blocking client object.*


### HttpxClientFactory (class, L40-L138)

> *Summary: This factory creates and configures asynchronous or synchronous HTTP clients based on provided parameters like authentication, headers, timeouts, and protocol settings. It allows users to instantiate a configured client instance by calling the factory object itself.*


### __init__ (method, L87-L132, parent: HttpxClientFactory)

> *Summary: Initializes a client by accepting numerous configuration parameters such as authentication details, request headers, timeouts, and protocol settings. These inputs are stored internally in an `options` dictionary to configure the client's behavior for subsequent requests.*


### __call__ (method, L134-L135, parent: HttpxClientFactory)

> *Summary: When invoked, this method instantiates and returns an `AsyncClient` object using the configuration parameters stored in the instance's options. It acts as a factory to create a ready-to-use asynchronous client based on provided settings.*


### make_sync (method, L137-L138, parent: HttpxClientFactory)

> *Summary: Instantiates and returns a synchronous `Client` object using the configuration parameters stored in the instance's options dictionary.*


### EmptyClientFactory (class, L141-L146)

> *Summary: This factory provides default implementations for creating asynchronous and synchronous clients, both configured with a 30-second timeout. It serves as a basic provider when no specific client configuration is needed.*


### __call__ (method, L142-L143, parent: EmptyClientFactory)

> *Summary: When invoked, this method instantiates and returns a new `AsyncClient` object configured with a 30.0 second timeout. It acts as a factory to provide ready-to-use asynchronous client connections.*


### make_sync (method, L145-L146, parent: EmptyClientFactory)

> *Summary: Instantiates and returns a synchronous `Client` object, configuring it with a default timeout of 30.0 seconds.*


### MockClient (function, L150-L227)

> *Summary: Generates a mock HTTP client factory designed to simulate responses from an A2A agent server for testing. It accepts a response message (string, dict, or Part) and an optional extended card, configuring the mock transport to serve predefined agent cards or return the specified message upon receiving requests.*

