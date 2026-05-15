# autogen/coding/jupyter/local_jupyter_server.py

2 class(es): LocalJupyterServer, GenerateToken. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LocalJupyterServer | class |  |

## Chunks

### LocalJupyterServer (class, L27-L164)

> *Summary: Instantiates and runs a local Jupyter Kernel Gateway server as a detached subprocess, configured with specified IP, token, and logging settings. It blocks until the server starts successfully, automatically determining the port if one isn't provided, and provides methods to retrieve connection details or stop the running process upon exiting a context manager.*


### GenerateToken (class, L28-L29, parent: LocalJupyterServer)

> *Summary: This class is a placeholder intended to generate tokens, suggesting it will handle the creation of authentication or session identifiers for Jupyter environments. Its current implementation has no functionality.*


### __init__ (method, L31-L141, parent: LocalJupyterServer)

> *Summary: Initializes and launches a local Jupyter Kernel Gateway server as a detached subprocess, configuring its IP, authentication token, logging behavior, and port. It validates the presence of `jupyter_kernel_gateway` and blocks until the server successfully starts, extracting the assigned port if one wasn't provided.*


### stop (method, L143-L149, parent: LocalJupyterServer)

> *Summary: Terminates the running subprocess by sending an appropriate interrupt signal ($\text{Ctrl+C}$ on Windows, $\text{SIGINT}$ otherwise). It then waits for the process to fully exit before completing.*


### connection_info (method, L152-L153, parent: LocalJupyterServer)

> *Summary: Returns a `JupyterConnectionInfo` object containing the server's IP address, port, and authentication token for local access. It hardcodes HTTPS to be disabled in the returned connection details.*


### get_client (method, L155-L156, parent: LocalJupyterServer)

> *Summary: Instantiates and returns a `JupyterClient` object using the connection details stored within the instance. This provides an interface to interact with the local Jupyter server.*


### __enter__ (method, L158-L159, parent: LocalJupyterServer)

> *Summary: When entering a context, this method returns the current instance itself. This allows for direct use of the object within a `with` statement block.*


### __exit__ (method, L161-L164, parent: LocalJupyterServer)

> *Summary: When the context manager exits, this method ensures a clean shutdown by calling the `stop()` method on the instance. It handles cleanup regardless of whether an exception occurred during the managed block.*

