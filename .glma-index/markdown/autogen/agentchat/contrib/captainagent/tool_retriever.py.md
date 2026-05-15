# autogen/agentchat/contrib/captainagent/tool_retriever.py

5 function(s): format_ag2_tool, _wrap_function, get_full_tool_description, _wrap_function, find_callables. 2 class(es): ToolBuilder, LocalExecutorWithTools. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolBuilder | class |  |
| LocalExecutorWithTools | class |  |
| format_ag2_tool | function |  |
| _wrap_function | function |  |
| get_full_tool_description | function |  |
| _wrap_function | function |  |
| find_callables | function |  |

## Chunks

### ToolBuilder (class, L32-L122)

> *Summary: This class initializes a tool retriever by loading descriptions from a corpus or user-defined sources and encoding them into embeddings using a Sentence Transformer. It provides methods to retrieve relevant tools based on a query, bind the available functions to an assistant agent's system message, and configure a user proxy agent with code execution capabilities for running those tools.*


### __init__ (method, L43-L58, parent: ToolBuilder)

> *Summary: Initializes a retriever by loading tool descriptions from a specified corpus root, either from a TSV file or directly from provided tools. It then encodes these documents into embeddings using a specified SentenceTransformer model for similarity search capabilities.*


### retrieve (method, L60-L69, parent: ToolBuilder)

> *Summary: Takes a text query and an optional count to perform semantic search against stored embeddings. It returns a list of relevant textual snippets from the underlying DataFrame based on the similarity scores found.*


### bind (method, L71-L76, parent: ToolBuilder)

> *Summary: This method modifies an agent's system message by appending a tool prompt, which incorporates provided function definitions. It updates the agent with this augmented system message to make it aware of available tools.*


### bind_user_proxy (method, L78-L122, parent: ToolBuilder)

> *Summary: This method configures a `UserProxyAgent` to enable code execution by injecting an appropriate executor based on the provided tool root. If the input is a string path, it finds functions within that path and uses a `LocalCommandLineCodeExecutor`; otherwise, if the input is a list of tools, it initializes a `LocalExecutorWithTools`. It returns a newly configured `UserProxyAgent` instance with the updated execution settings.*


### LocalExecutorWithTools (class, L125-L228)

> *Summary: This class executes Python code blocks within a specified working directory, injecting provided tools directly into the execution environment by mapping tool names to their functions. It takes a list of `CodeBlock` objects as input and returns a `CodeResult` containing the combined standard output/error logs and an exit code reflecting successful or failed execution.*


### code_extractor (method, L162-L164, parent: LocalExecutorWithTools)

> *Summary: Provides access to an experimental `MarkdownCodeExtractor` instance, allowing the agent to extract code from markdown content. This method returns a configured object capable of performing code extraction tasks.*


### __init__ (method, L166-L170, parent: LocalExecutorWithTools)

> *Summary: Initializes the retriever by accepting an optional list of `Tool` objects and a working directory path. It ensures the specified working directory exists before storing these inputs as instance attributes.*


### execute_code_blocks (method, L172-L224, parent: LocalExecutorWithTools)

> *Summary: Executes a list of provided `CodeBlock` objects sequentially by saving each to a temporary file and running it within an isolated environment containing injected tools. It aggregates the standard output and error streams from all executions into a single result object detailing the final exit code and combined logs.*


### restart (method, L226-L228, parent: LocalExecutorWithTools)

> *Summary: This method performs no operation as it simply passes, indicating that restarting the stateless code executor requires no specific actions.*


### format_ag2_tool (function, L232-L254)

> *Summary: Generates a string representation of a `Tool` object, transforming it into a specific function definition format suitable for an AG2 environment. It takes a `Tool` instance and outputs a formatted Python code block detailing the tool's signature, description, and expected arguments.*


### _wrap_function (function, L257-L274)

> *Summary: This utility wraps a given function to ensure its return value is serialized into JSON format. It transparently handles both synchronous and asynchronous execution of the wrapped function while preserving metadata.*


### get_full_tool_description (function, L278-L296)

> *Summary: Reads a Python file to dynamically execute its contents and retrieve the signature and documentation of the main function defined within it. It returns a formatted string containing the function definition, including its signature and docstring.*


### _wrap_function (function, L299-L316)

> *Summary: This utility wraps a given function to ensure its return value is serialized into JSON format. It correctly handles both synchronous and asynchronous execution paths of the original function.*


### find_callables (function, L319-L334)

> *Summary: Scans a given directory recursively to discover all functions or methods defined within Python files. It dynamically imports each `.py` file and collects any callable objects found, returning them as a list of references.*

