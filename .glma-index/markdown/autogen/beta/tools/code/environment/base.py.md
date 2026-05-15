# autogen/beta/tools/code/environment/base.py

2 class(es): CodeRunResult, CodeEnvironment. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CodeRunResult | class |  |
| CodeEnvironment | class |  |

## Chunks

### CodeRunResult (class, L15-L23)

> *Summary: Represents the result of executing a piece of code, storing the combined standard output and error as a string. It also includes an integer exit code following POSIX standards to indicate execution success or failure.*


### CodeEnvironment (class, L27-L58)

> *Summary: Defines a protocol for code execution backends, allowing implementations to run source code in various environments like local subprocesses or remote sandboxes. It requires methods to report supported languages and asynchronously execute provided code given a language and optional conversation context.*


### supported_languages (method, L36-L41, parent: CodeEnvironment)

> *Summary: Returns a tuple of `CodeLanguage` enums indicating which programming languages the current execution environment supports. This list is exposed to the Language Model (LLM) via the tool description.*


### run (method, L43-L58, parent: CodeEnvironment)

> *Summary: Executes provided code string using a specified language, optionally utilizing an active conversation context to resolve variables like tenant credentials. It returns a `CodeRunResult` object detailing the execution outcome.*

