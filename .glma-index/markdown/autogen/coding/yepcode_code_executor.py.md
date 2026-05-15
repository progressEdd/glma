# autogen/coding/yepcode_code_executor.py

2 class(es): YepCodeCodeResult, YepCodeCodeExecutor. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| YepCodeCodeResult | class |  |
| YepCodeCodeExecutor | class |  |

## Chunks

### YepCodeCodeResult (class, L34-L37)

> *Summary: This class extends `CodeResult` to specifically hold results from the YepCode executor. It stores an optional string identifier corresponding to the YepCode execution.*


### YepCodeCodeExecutor (class, L41-L197)

> *Summary: This class executes Python or JavaScript code blocks using a secure, serverless runtime via YepCode. It accepts configuration like an API token and timeout, processes code blocks serially, and returns a consolidated result containing outputs and execution logs upon completion (or immediately if asynchronous).*


### __init__ (method, L65-L99, parent: YepCodeCodeExecutor)

> *Summary: Initializes the executor by validating required dependencies and configuration parameters like API token, timeout, and execution mode. It loads credentials from provided arguments or environment variables before setting up the underlying YepCode execution runner instance.*


### code_extractor (method, L102-L104, parent: YepCodeCodeExecutor)

> *Summary: Provides an instance of `MarkdownCodeExtractor` for external use by an agent. This method returns the configured code extraction utility.*


### timeout (method, L107-L109, parent: YepCodeCodeExecutor)

> *Summary: Retrieves the configured time limit for executing code, returning an integer value stored internally.*


### _normalize_language (method, L111-L119, parent: YepCodeCodeExecutor)

> *Summary: Converts an input language string to a standardized YepCode format by lowercasing it and mapping common variations like "js" or "py" to their canonical forms. It returns the normalized string, which is either the standard name or the original lowercase input if no specific mapping applies.*


### execute_code_blocks (method, L121-L193, parent: YepCodeCodeExecutor)

> *Summary: Processes a list of `CodeBlock` objects, executing them sequentially using an internal runner for supported languages like Python and JavaScript. It returns a `YepCodeCodeResult` containing aggregated outputs or an error status based on the execution outcomes.*


### restart (method, L195-L197, parent: YepCodeCodeExecutor)

> *Summary: This method resets the state of the code executor instance. It takes no arguments and performs an internal reset operation.*

