# autogen/coding/jupyter/embedded_ipython_code_executor.py

1 class(es): EmbeddedIPythonCodeExecutor. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| EmbeddedIPythonCodeExecutor | class |  |

## Chunks

### EmbeddedIPythonCodeExecutor (class, L34-L182)

> *Summary: Manages a stateful execution environment by embedding an IPython kernel, allowing LLM-generated code to run locally with access to previous session variables. It accepts a list of `CodeBlock` inputs and returns an `IPythonCodeResult` containing standard output, saved file paths for images/HTML, or error details upon completion or timeout.*


### _output_dir_must_exist (method, L53-L56, parent: EmbeddedIPythonCodeExecutor)

> *Summary: Validates that a provided string path for an output directory actually exists on the filesystem; raises a `ValueError` if the directory is missing and returns the path otherwise.*


### __init__ (method, L58-L73, parent: EmbeddedIPythonCodeExecutor)

> *Summary: Initializes the executor by validating that the specified kernel is installed and then starts the corresponding Jupyter kernel, establishing a client connection to manage its channels for execution. It stores configuration details like timeout and output directory for subsequent operations.*


### code_extractor (method, L76-L78, parent: EmbeddedIPythonCodeExecutor)

> *Summary: Provides an instance of `MarkdownCodeExtractor` for external use by an agent. This method returns the configured code extraction utility.*


### execute_code_blocks (method, L80-L143, parent: EmbeddedIPythonCodeExecutor)

> *Summary: Executes a sequence of provided code blocks by sending them to an attached IPython kernel and asynchronously collecting the results. It processes various message types from the kernel—including text, images, HTML, and errors—to build a final result object containing all captured outputs and saved file paths.*


### restart (method, L145-L152, parent: EmbeddedIPythonCodeExecutor)

> *Summary: This method terminates the current kernel session, shuts down the existing kernel manager, and then initializes a completely new kernel instance by creating a fresh `KernelManager` and starting its associated client channels. It effectively resets the execution environment for subsequent operations.*


### _save_image (method, L154-L162, parent: EmbeddedIPythonCodeExecutor)

> *Summary: Decodes a base64 encoded string of image data and saves it to a uniquely named PNG file within the configured output directory. It returns the absolute filesystem path to the newly saved image.*


### _save_html (method, L164-L171, parent: EmbeddedIPythonCodeExecutor)

> *Summary: Writes provided HTML string data to a uniquely named file within the configured output directory. It returns the absolute filesystem path of the newly created HTML file.*


### _process_code (method, L173-L182, parent: EmbeddedIPythonCodeExecutor)

> *Summary: This method modifies input code by scanning for lines starting with `! pip install` or `!pip install`. If found, it appends the `-qqq` flag to ensure quiet installation before returning the modified string.*

