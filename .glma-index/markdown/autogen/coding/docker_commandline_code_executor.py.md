# autogen/coding/docker_commandline_code_executor.py

1 function(s): _wait_for_ready. 1 class(es): DockerCommandLineCodeExecutor. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _wait_for_ready | function |  |
| DockerCommandLineCodeExecutor | class |  |

## Chunks

### _wait_for_ready (function, L32-L40)

> *Summary: This function polls a provided container object until its status becomes "running" or a specified timeout is reached. If the container does not reach the running state within the allotted time, it raises an error indicating startup failure.*


### DockerCommandLineCodeExecutor (class, L48-L297)

> *Summary: Executes code blocks by saving them to files within a Docker container and running the corresponding command line interpreter inside it. It accepts configuration for the Docker image, execution policies per language, and manages the container lifecycle via context management methods. The primary output is a result object containing the combined standard output, final exit code, and path of the first executed file.*


### __init__ (method, L63-L196, parent: DockerCommandLineCodeExecutor)

> *Summary: Initializes a Docker-based code executor by pulling or using a specified image, creating and starting a container with defined volumes and settings. It configures cleanup routines to stop and remove the container upon exit, while also setting up execution policies for supported languages like Python and shell scripts.*


### timeout (method, L199-L201, parent: DockerCommandLineCodeExecutor)

> *Summary: Retrieves the configured time limit for code execution from an internal attribute. This method returns an integer representing the specified timeout duration.*


### work_dir (method, L204-L206, parent: DockerCommandLineCodeExecutor)

> *Summary: Returns the current working directory as a `Path` object, which is used to define where code execution takes place. This method provides access to the internal state tracking the execution environment's location.*


### bind_dir (method, L209-L211, parent: DockerCommandLineCodeExecutor)

> *Summary: Returns the configured path to the directory that will be mounted into the code execution container. This method provides access to the designated input/output location for running code within a Docker environment.*


### code_extractor (method, L214-L216, parent: DockerCommandLineCodeExecutor)

> *Summary: Provides an instance of `MarkdownCodeExtractor` for agents to utilize when extracting code from content. This method returns the configured extractor object.*


### execute_code_blocks (method, L218-L276, parent: DockerCommandLineCodeExecutor)

> *Summary: Processes a list of `CodeBlock` objects by saving each to a temporary file and executing it within a container environment based on the specified language. It returns a result containing the aggregated output, final exit code, and the path to the first executed file.*


### restart (method, L278-L282, parent: DockerCommandLineCodeExecutor)

> *Summary: This method attempts to restart the underlying Docker container instance. It raises a `ValueError` if the container fails to reach a "running" state after the restart attempt, providing logs for debugging.*


### stop (method, L284-L286, parent: DockerCommandLineCodeExecutor)

> *Summary: This method performs an experimental cleanup operation to halt the execution of the code environment. It triggers a private cleanup routine to terminate any running processes or resources associated with the executor.*


### __enter__ (method, L288-L289, parent: DockerCommandLineCodeExecutor)

> *Summary: When entering a context, this method returns the current instance itself, allowing for chained operations within a `with` block.*


### __exit__ (method, L291-L297, parent: DockerCommandLineCodeExecutor)

> *Summary: When an exception occurs within the context manager, this method ensures that the underlying process is terminated by calling `self.stop()`. It handles cleanup regardless of whether an error was raised or not.*

