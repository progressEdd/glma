# autogen/beta/tools/code/tool.py

1 class(es): SandboxCodeTool. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SandboxCodeTool | class |  |

## Chunks

### SandboxCodeTool (class, L17-L91)

> *Summary: Provides a client-side tool wrapper that executes code using a specified `CodeEnvironment` backend. It accepts the environment instance and optional metadata to expose a single `run_code(code, language)` function capable of running code across various providers.*


### __init__ (method, L52-L74, parent: SandboxCodeTool)

> *Summary: Initializes a code execution tool by wrapping an asynchronous environment runner into a callable function. It configures this function to execute provided code in a specified language and returns the output along with any non-zero exit code information.*


### environment (method, L77-L79, parent: SandboxCodeTool)

> *Summary: Returns the internal `CodeEnvironment` object, which represents the execution context for code operations. This method provides access to the established runtime environment.*


### schemas (method, L81-L82, parent: SandboxCodeTool)

> *Summary: Retrieves a list of schema definitions by calling the underlying tool's `schemas` method with the provided execution context. This acts as a simple proxy to expose the tool's schema information.*


### register (method, L84-L91, parent: SandboxCodeTool)

> *Summary: This method delegates the registration of a tool to an internal object, accepting an exit stack, a context, and optional middleware as inputs. It performs no direct computation but ensures the tool is properly set up within the provided execution environment.*

