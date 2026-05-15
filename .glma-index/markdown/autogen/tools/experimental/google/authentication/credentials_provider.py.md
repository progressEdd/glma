# autogen/tools/experimental/google/authentication/credentials_provider.py

1 class(es): GoogleCredentialsProvider. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GoogleCredentialsProvider | class |  |

## Chunks

### GoogleCredentialsProvider (class, L20-L35)

> *Summary: Defines a contract for providers that supply Google authentication details. It requires methods to retrieve `Credentials` and expose the associated host and port information.*


### get_credentials (method, L23-L25, parent: GoogleCredentialsProvider)

> *Summary: Retrieves the necessary Google authentication credentials for the instance. It returns an optional `Credentials` object if successful, or `None` otherwise.*


### host (method, L28-L30, parent: GoogleCredentialsProvider)

> *Summary: Retrieves the hostname used as the source for credential retrieval. It returns a string representing that host.*


### port (method, L33-L35, parent: GoogleCredentialsProvider)

> *Summary: Retrieves the network port number used for credential acquisition. It returns an integer representing this specific port.*

