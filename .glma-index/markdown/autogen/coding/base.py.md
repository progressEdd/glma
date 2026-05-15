# autogen/coding/base.py

6 class(es): CodeBlock, CodeResult, CodeExtractor, CodeExecutor, IPythonCodeResult, CommandLineCodeResult. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CodeBlock | class |  |
| CodeResult | class |  |
| CodeExtractor | class |  |
| CodeExecutor | class |  |
| IPythonCodeResult | class |  |
| CommandLineCodeResult | class |  |

## Chunks

### CodeBlock (class, L21-L26)

> *Summary: Represents an experimental structure for holding executable code. It accepts two string inputs: the actual `code` content and its associated programming `language`.*


### CodeResult (class, L30-L35)

> *Summary: Represents the outcome of running code, holding an integer `exit_code` and a string `output`. It serves as a structured container for capturing execution results.*


### CodeExtractor (class, L39-L53)

> *Summary: Defines an interface for extracting structured code blocks from various message inputs, which can be a string or a list containing text and image parts. It takes the message content as input and returns a list of `CodeBlock` objects representing the extracted code.*


### extract_code_blocks (method, L42-L53, parent: CodeExtractor)

> *Summary: Parses an input string or list of message parts to identify and return a list of structured `CodeBlock` objects. It specifically targets content formatted as code within the provided message data.*


### CodeExecutor (class, L58-L86)

> *Summary: Defines a protocol for an experimental code execution mechanism, requiring implementations to provide a `CodeExtractor` and methods to run a list of `CodeBlock`s into a `CodeResult`, along with a `restart` function. This structure dictates how external code blocks are processed and managed by the executor.*


### code_extractor (method, L62-L64, parent: CodeExecutor)

> *Summary: Returns an instance of a `CodeExtractor` object, which is the specific tool utilized for extracting code within the execution context. This method provides access to the underlying extraction mechanism.*


### execute_code_blocks (method, L66-L77, parent: CodeExecutor)

> *Summary: This method executes a list of provided `CodeBlock` objects and returns a `CodeResult`. It serves as an abstract interface that concrete code executors must implement to perform the actual execution logic.*


### restart (method, L79-L86, parent: CodeExecutor)

> *Summary: When an agent is reset, this experimental method triggers a restart of the underlying code executor. It serves as a hook that concrete code executor implementations must provide.*


### IPythonCodeResult (class, L89-L95)

> *Summary: Represents an experimental result structure specifically for IPython code execution. It holds a list attribute, `output_files`, which tracks any files created by the executed code blocks.*


### CommandLineCodeResult (class, L116-L122)

> *Summary: Represents an experimental result structure specifically for code execution run via a command line. It stores an optional string indicating the path of the file where the executed code was saved.*

