# autogen/coding/daytona_code_executor.py

3 class(es): DaytonaSandboxResources, DaytonaCodeResult, DaytonaCodeExecutor. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DaytonaSandboxResources | class |  |
| DaytonaCodeResult | class |  |
| DaytonaCodeExecutor | class |  |

## Chunks

### DaytonaSandboxResources (class, L54-L69)

> *Summary: Defines resource constraints for a sandbox environment, allowing optional specification of CPU cores, memory (in GB), and disk space (in GB). These limits are only enforced when a custom image is used, not when operating on a snapshot.*


### DaytonaCodeResult (class, L73-L76)

> *Summary: This class extends `CodeResult` to specifically hold results from the Daytona executor. It includes an optional field to store the unique identifier of the execution sandbox used.*


### DaytonaCodeExecutor (class, L80-L429)

> *Summary: Manages a persistent execution environment within a Daytona sandbox, initialized with configuration like API keys and resource limits. It executes code blocks sequentially—using `code_run` for Python or file-based execution via shell commands for other languages—and returns aggregated results upon completion or immediately upon the first failure.*


### __init__ (method, L170-L218, parent: DaytonaCodeExecutor)

> *Summary: Initializes an executor by configuring and creating a Daytona client and sandbox instance based on provided parameters like API keys, target environment, and resource constraints. It automatically registers a cleanup hook to ensure the created sandbox is deleted upon program exit.*


### _create_sandbox (method, L224-L270, parent: DaytonaCodeExecutor)

> *Summary: Constructs a new Daytona sandbox instance, prioritizing an explicit snapshot if available, otherwise using a specified Docker image or the default snapshot. It handles various potential API errors during creation by raising a `RuntimeError`.*


### _normalize_language (method, L272-L275, parent: DaytonaCodeExecutor)

> *Summary: Converts an input language string to a standardized format by lowercasing it and resolving any known alias mappings against a predefined dictionary. It returns the canonical name for the provided language identifier.*


### code_extractor (method, L282-L284, parent: DaytonaCodeExecutor)

> *Summary: Returns an instance of `MarkdownCodeExtractor`, which is the specific tool used internally to extract code from input. This method provides the necessary parsing mechanism for the executor's operation.*


### timeout (method, L287-L289, parent: DaytonaCodeExecutor)

> *Summary: Retrieves the configured execution time limit, which is stored internally as an integer representing seconds. This method provides the duration constraint for code execution.*


### execute_code_blocks (method, L291-L387, parent: DaytonaCodeExecutor)

> *Summary: Executes a sequence of provided code blocks within a sandbox environment, handling Python execution via a dedicated method and other languages by writing to temporary files and running them with external binaries. It stops immediately upon the first failure (timeout, error, or non-zero exit code), otherwise returning all combined outputs on full success.*


### restart (method, L389-L402, parent: DaytonaCodeExecutor)

> *Summary: This method resets the execution environment by deleting the existing sandbox and initializing a new one. It ensures a clean state, clearing all accumulated files and process information when called to start a fresh conversation.*


### delete (method, L408-L423, parent: DaytonaCodeExecutor)

> *Summary: This method safely cleans up and releases all resources associated with the current execution environment. It unregisters its own cleanup hook, then attempts to delete the underlying sandbox, gracefully handling cases where it might already be gone.*


### __enter__ (method, L425-L426, parent: DaytonaCodeExecutor)

> *Summary: When entering a context, this method returns the executor instance itself, allowing for direct use within a `with` statement.*


### __exit__ (method, L428-L429, parent: DaytonaCodeExecutor)

> *Summary: When exiting the context manager, this method ensures cleanup by calling the `delete` method on the instance. It handles any exceptions passed to it without further action.*

