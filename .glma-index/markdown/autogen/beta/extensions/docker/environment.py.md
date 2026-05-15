# autogen/beta/extensions/docker/environment.py

1 class(es): DockerCodeEnvironment. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DockerCodeEnvironment | class |  |

## Chunks

### DockerCodeEnvironment (class, L42-L275)

> *Summary: Manages a persistent Docker container for executing code snippets in a sandboxed environment. It initializes the container lazily upon the first execution request, using `docker exec` for subsequent runs, and handles cleanup automatically or via an explicit `aclose()` method. Inputs include configuration parameters like image name, memory limits, and network mode, while it outputs structured results containing stdout/stderr and exit codes from the executed code.*


### __init__ (method, L88-L117, parent: DockerCodeEnvironment)

> *Summary: Initializes a Docker environment configuration by accepting parameters like image name, environment variables, resource limits (memory/CPU), and networking settings. It sets up internal state including the client connection placeholder, container reference, an asynchronous lock, and flags for cleanup.*


### supported_languages (method, L120-L121, parent: DockerCodeEnvironment)

> *Summary: Returns a tuple containing all the code languages this environment supports, based on an internal list.*


### run (method, L123-L174, parent: DockerCodeEnvironment)

> *Summary: Executes provided code within a Docker container based on the specified language. It handles different execution methods—direct command running for some languages and file-based decoding/execution for others—and manages timeouts by restarting the container if necessary. The function returns a `CodeRunResult` containing the captured output and exit code.*


### _ensure_container (method, L176-L216, parent: DockerCodeEnvironment)

> *Summary: This method ensures a Docker container is running for the environment by checking if one already exists; otherwise, it resolves configuration parameters like image and environment variables from provided context or internal settings. It then uses the Docker client to start a detached container with specified resource limits and returns the active container object.*


### _restart_container (method, L218-L235, parent: DockerCodeEnvironment)

> *Summary: This method stops and then removes the existing container instance under a lock to ensure atomic state management. It handles potential exceptions during the stop and removal processes, allowing for a clean restart of the container later.*


### aclose (method, L237-L261, parent: DockerCodeEnvironment)

> *Summary: This method safely stops and removes the associated Docker container if it exists, while also closing the underlying Docker client connection. It handles potential `NotFound` exceptions gracefully and is idempotent, allowing multiple calls without error.*


### _atexit_close (method, L263-L269, parent: DockerCodeEnvironment)

> *Summary: This method ensures graceful shutdown of the associated container upon program exit by asynchronously calling `aclose()`. It safely handles cases where no container is active and suppresses any exceptions that occur during this final cleanup process.*


### __aenter__ (method, L271-L272, parent: DockerCodeEnvironment)

> *Summary: When used as an asynchronous context manager, this method returns the current environment instance. This allows for setup and teardown operations within `async with` blocks.*


### __aexit__ (method, L274-L275, parent: DockerCodeEnvironment)

> *Summary: When an asynchronous context manager exits, this method ensures the underlying resource is properly closed by calling `aclose()`. It accepts any exception that occurred within the context block as input and returns nothing.*

