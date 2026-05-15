# autogen/coding/jupyter/jupyter_code_executor.py

1 class(es): JupyterCodeExecutor. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| JupyterCodeExecutor | class |  |

## Chunks

### JupyterCodeExecutor (class, L25-L154)

> *Summary: Manages stateful code execution by connecting to a Jupyter server and running blocks of code within a specific kernel. It accepts connection details, executes the provided `CodeBlock` list via the kernel client, and returns an execution result containing outputs and paths to saved image/HTML files. The object can also restart or stop the active kernel session.*


### __init__ (method, L26-L71, parent: JupyterCodeExecutor)

> *Summary: Initializes a stateful code executor by connecting to a specified Jupyter server, selecting a kernel, and starting the execution environment. It validates inputs like timeout and directory existence before establishing connections and ensuring the requested kernel is available.*


### code_extractor (method, L74-L76, parent: JupyterCodeExecutor)

> *Summary: Provides an instance of `MarkdownCodeExtractor` for external use by an agent. This method returns the configured code extraction utility.*


### execute_code_blocks (method, L78-L118, parent: JupyterCodeExecutor)

> *Summary: Executes a sequence of provided code blocks by sending them to the Jupyter kernel. It aggregates execution results, saving image and HTML data to files while returning a summary object containing all captured outputs and file paths upon successful completion.*


### restart (method, L120-L123, parent: JupyterCodeExecutor)

> *Summary: This method initiates a kernel restart within the Jupyter environment using the stored client and kernel ID. It then updates the internal kernel client reference to reflect the newly restarted state.*


### _save_image (method, L125-L133, parent: JupyterCodeExecutor)

> *Summary: Decodes a base64 encoded string of image data and saves it to a uniquely named PNG file within the configured output directory. It returns the absolute filesystem path to the newly saved image.*


### _save_html (method, L135-L142, parent: JupyterCodeExecutor)

> *Summary: Writes provided HTML string data to a uniquely named file within the configured output directory. It returns the absolute filesystem path of the newly created HTML file.*


### stop (method, L144-L146, parent: JupyterCodeExecutor)

> *Summary: This method terminates the associated Jupyter kernel by calling `delete_kernel` on the underlying client using the stored kernel ID. It performs a cleanup action to stop the running execution environment.*


### __enter__ (method, L148-L149, parent: JupyterCodeExecutor)

> *Summary: When entering a context, this method returns the current instance itself. This allows for seamless use within a `with` statement block.*


### __exit__ (method, L151-L154, parent: JupyterCodeExecutor)

> *Summary: When an execution context exits, this method calls `self.stop()` to halt any ongoing operations. It accepts exception details as input but performs no return value.*

