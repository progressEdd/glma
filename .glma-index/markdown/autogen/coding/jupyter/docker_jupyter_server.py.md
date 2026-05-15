# autogen/coding/jupyter/docker_jupyter_server.py

2 class(es): DockerJupyterServer, GenerateToken. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DockerJupyterServer | class |  |

## Chunks

### DockerJupyterServer (class, L33-L164)

> *Summary: This class manages the lifecycle of a Jupyter kernel gateway server running inside a Docker container. It builds or uses a specified image to launch the container, sets up authentication via an optional token, and exposes connection details for external use. The instance can be used as a context manager to ensure the container is properly stopped upon exiting.*


### GenerateToken (class, L56-L57, parent: DockerJupyterServer)

> *Summary: This class is a placeholder intended to handle the generation of tokens, likely for authentication or session management within a Jupyter environment. It currently has no implemented logic.*


### __init__ (method, L59-L146, parent: DockerJupyterServer)

> *Summary: Initializes and starts a Jupyter kernel gateway server within a Docker container, optionally building the image or using a custom one. It configures environment variables, sets an authentication token, runs the container, waits for it to be ready, and registers cleanup hooks to stop and potentially remove the running instance upon program exit.*


### connection_info (method, L149-L150, parent: DockerJupyterServer)

> *Summary: Returns a `JupyterConnectionInfo` object containing the local host address, HTTP status, and the configured port and authentication token for connecting to the Jupyter server.*


### stop (method, L152-L153, parent: DockerJupyterServer)

> *Summary: Executes a cleanup routine to shut down the Jupyter server instance. This method takes no arguments and performs internal state management for termination.*


### get_client (method, L155-L156, parent: DockerJupyterServer)

> *Summary: Instantiates and returns a `JupyterClient` object using the connection details stored within the instance. This provides an interface to interact with the remote Jupyter server.*


### __enter__ (method, L158-L159, parent: DockerJupyterServer)

> *Summary: When entering a context, this method returns the current instance itself. This allows for chaining operations within a `with` block.*


### __exit__ (method, L161-L164, parent: DockerJupyterServer)

> *Summary: When exiting the context manager, this method ensures a clean shutdown by calling the `stop()` method on the instance. It handles any potential exceptions passed during the exit process without further action.*

