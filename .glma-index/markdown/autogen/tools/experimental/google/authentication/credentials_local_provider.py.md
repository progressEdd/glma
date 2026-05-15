# autogen/tools/experimental/google/authentication/credentials_local_provider.py

1 class(es): GoogleCredentialsLocalProvider. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GoogleCredentialsLocalProvider | class |  |

## Chunks

### GoogleCredentialsLocalProvider (class, L23-L91)

> *Summary: This class provides a mechanism to obtain Google API credentials by running a local web server for user authentication. It takes paths for the client secret and optional token files, along with desired scopes and a listening port, returning valid `Credentials` objects after refreshing or initiating a new OAuth flow.*


### __init__ (method, L24-L42, parent: GoogleCredentialsLocalProvider)

> *Summary: Initializes a local Google credentials provider using specified paths for client secrets and optional tokens, along with the required API scopes and a designated port. It stores these configuration parameters to manage credential acquisition locally.*


### host (method, L45-L47, parent: GoogleCredentialsLocalProvider)

> *Summary: Returns the string `"localhost"` to specify the default host for local operations. This method provides a fixed hostname regardless of any input parameters.*


### port (method, L50-L52, parent: GoogleCredentialsLocalProvider)

> *Summary: Retrieves the network port number configured for credential access. It returns an integer representing the designated port.*


### _refresh_or_get_new_credentials (method, L61-L67, parent: GoogleCredentialsLocalProvider)

> *Summary: This method ensures valid credentials by either refreshing existing ones if they are expired and a refresh token is available, or by initiating a new local server flow to obtain fresh credentials otherwise. It returns the resulting `Credentials` object after ensuring its validity.*


### get_credentials (method, L76-L91, parent: GoogleCredentialsLocalProvider)

> *Summary: Retrieves Google credentials by first checking for an existing, valid token file; if none are found or the current ones are expired, it attempts to refresh or obtain new credentials and saves them back to the specified token file. The method returns a `Credentials` object ready for use with Google APIs.*

