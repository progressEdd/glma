# autogen/beta/extensions/daytona/environment.py

2 class(es): DaytonaResources, DaytonaCodeEnvironment. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DaytonaResources | class |  |
| DaytonaCodeEnvironment | class |  |

## Chunks

### DaytonaResources (class, L50-L59)

> *Summary: Defines resource limits for a Daytona sandbox, specifying optional CPU, memory, and disk constraints. These limits are only enforced when an image is provided to the environment; they are ignored if a snapshot is used instead.*


### DaytonaCodeEnvironment (class, L62-L267)

> *Summary: Manages a Daytona sandbox environment for code execution, lazily creating it upon the first `run` call using specified configuration parameters like API keys or Docker images. It executes provided code against the sandbox, handling various errors and ensuring cleanup via `atexit` or explicit closing methods.*


### __init__ (method, L92-L128, parent: DaytonaCodeEnvironment)

> *Summary: Initializes an environment configuration by accepting optional parameters like API credentials, target specifications, and resource definitions. It validates that either a snapshot or image is provided, sets up internal state variables, and initializes synchronization primitives for managing the connection lifecycle.*


### supported_languages (method, L131-L132, parent: DaytonaCodeEnvironment)

> *Summary: Returns a tuple containing all the code languages that the current environment supports. This method accesses and returns a pre-defined list of language identifiers stored internally.*


### run (method, L134-L171, parent: DaytonaCodeEnvironment)

> *Summary: Executes provided code string based on the specified language, either directly via a sandbox process for Python or by writing and executing it as a temporary file for other languages. It returns a `CodeRunResult` containing the execution output and exit code, handling various errors like timeouts or rate limits during the sandboxed operation.*


### _ensure_sandbox (method, L173-L234, parent: DaytonaCodeEnvironment)

> *Summary: This method ensures a Daytona sandbox exists by first checking for existing state and validating configuration inputs like credentials and image/snapshot selection. It constructs the necessary API client using resolved parameters from the context or instance attributes, then calls the Daytona API to create and return the new sandbox object.*


### aclose (method, L236-L253, parent: DaytonaCodeEnvironment)

> *Summary: This method safely cleans up the environment by unregistering an exit handler, setting a closed flag, and then asynchronously deleting the associated sandbox if it exists. It also attempts to close the connected client, suppressing any exceptions during these cleanup operations.*


### _atexit_close (method, L255-L261, parent: DaytonaCodeEnvironment)

> *Summary: This method ensures the asynchronous sandbox resources are properly closed upon program exit by running `self.aclose()` within an `asyncio` event loop, while suppressing any exceptions that occur during this cleanup process.*


### __aenter__ (method, L263-L264, parent: DaytonaCodeEnvironment)

> *Summary: When used as an asynchronous context manager, this method returns the current environment instance. It allows for setup and teardown logic to be executed around code blocks that interact with the Daytona environment.*


### __aexit__ (method, L266-L267, parent: DaytonaCodeEnvironment)

> *Summary: When an asynchronous context manager exits, this method ensures the associated resources are properly cleaned up by calling `aclose()`. It accepts any exception that occurred within the context block as input and returns nothing.*

