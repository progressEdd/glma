# autogen/tools/experimental/google/authentication/credentials_hosted_provider.py

1 class(es): GoogleCredenentialsHostedProvider. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GoogleCredenentialsHostedProvider | class |  |

## Chunks

### GoogleCredenentialsHostedProvider (class, L18-L43)

> *Summary: This provider class is designed to fetch Google credentials from a specified host and port, accepting additional configuration via keyword arguments. Currently, it serves as an unimplemented abstract base for future credential retrieval logic.*


### __init__ (method, L19-L30, parent: GoogleCredenentialsHostedProvider)

> *Summary: Initializes a credentials provider by storing the required `host`, optional `port`, and arbitrary keyword arguments. Currently, it raises a `NotImplementedError` as the functionality has not been built out.*


### host (method, L33-L35, parent: GoogleCredenentialsHostedProvider)

> *Summary: Retrieves the configured hostname used by this provider instance. It returns a string representing the source of the credentials.*


### port (method, L38-L40, parent: GoogleCredenentialsHostedProvider)

> *Summary: Retrieves the network port number configured for credential retrieval from an internal instance variable. This method returns a single integer representing the designated port.*


### get_credentials (method, L42-L43, parent: GoogleCredenentialsHostedProvider)

> *Summary: This method is intended to retrieve authentication credentials, but currently raises a `NotImplementedError` as the functionality has not been built. It expects no input and is designed to return an object of type `Credentials`.*

