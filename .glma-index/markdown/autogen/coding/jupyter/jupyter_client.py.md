# autogen/coding/jupyter/jupyter_client.py

4 class(es): JupyterClient, JupyterKernelClient, ExecutionResult, DataItem. 18 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| JupyterClient | class |  |
| JupyterKernelClient | class |  |

## Chunks

### JupyterClient (class, L30-L96)

> *Summary: This class manages communication with a Jupyter gateway server using HTTP requests and optionally WebSockets. It accepts connection details to perform operations like listing kernels/specs, starting, deleting, or restarting kernels, and retrieving a dedicated client for kernel interaction.*


### __init__ (method, L31-L40, parent: JupyterClient)

> *Summary: Initializes a client to communicate with a Jupyter gateway server using provided connection details. It sets up an HTTP session configured with automatic retries for network resilience.*


### _get_headers (method, L42-L45, parent: JupyterClient)

> *Summary: Retrieves HTTP headers for API requests by checking the stored connection token; returns an empty dictionary if no token is present, otherwise provides an `Authorization` header with the token.*


### _get_api_base_url (method, L47-L50, parent: JupyterClient)

> *Summary: Constructs the base URL for API communication by combining the protocol (HTTP or HTTPS), host, and optional port from connection information. This method returns a fully qualified string representing the server endpoint.*


### _get_ws_base_url (method, L52-L54, parent: JupyterClient)

> *Summary: Constructs the WebSocket base URL by combining the host and port from connection information. It returns a string formatted as `ws://<host>:<port>`.*


### list_kernel_specs (method, L56-L58, parent: JupyterClient)

> *Summary: Fetches and returns a dictionary containing the specifications for all available kernels from the connected Jupyter session via an API GET request. The output maps kernel names to their respective configuration details.*


### list_kernels (method, L60-L62, parent: JupyterClient)

> *Summary: Fetches a list of available Jupyter kernels by making a GET request to the `/api/kernels` endpoint. It returns this data as a list of dictionaries containing kernel information.*


### start_kernel (method, L64-L78, parent: JupyterClient)

> *Summary: Initiates a new computational kernel by sending a POST request to the `/api/kernels` endpoint with a specified kernel specification name. It returns the unique ID assigned to the newly started kernel from the API response.*


### delete_kernel (method, L80-L84, parent: JupyterClient)

> *Summary: Removes a specified Jupyter kernel by sending a DELETE request to the API endpoint using the provided `kernel_id`. It raises an exception if the HTTP request fails.*


### restart_kernel (method, L86-L90, parent: JupyterClient)

> *Summary: Sends a POST request to the Jupyter API endpoint for a specific kernel ID to trigger a kernel restart. It raises an exception if the HTTP response status indicates an error.*


### get_kernel_client (method, L93-L96, parent: JupyterClient)

> *Summary: Establishes a connection to the specified kernel's communication channel by constructing a WebSocket URL and creating a `JupyterKernelClient` instance from it. This method takes a `kernel_id` string as input and returns an active client object for interacting with that kernel.*


### JupyterKernelClient (class, L100-L224)

> *Summary: Manages communication with a Jupyter kernel over a WebSocket connection, handling session setup and teardown via context management. It allows sending code execution requests, receiving structured results (text, images), streaming output, and returning an `ExecutionResult` object upon completion or error.*


### ExecutionResult (class, L104-L112, parent: JupyterKernelClient)

> *Summary: Represents the outcome of a code execution, containing a boolean success flag, textual output, and a list of structured data items with MIME types and content. This structure encapsulates all necessary results from running code within a Jupyter environment.*


### DataItem (class, L106-L108, parent: ExecutionResult)

> *Summary: Represents a piece of data with a specified MIME type and its content as a string. It serves as a container for transmitting structured data within the system.*


### __init__ (method, L114-L116, parent: JupyterKernelClient)

> *Summary: Initializes a client instance by generating a unique session ID and storing the provided `WebSocket` connection object. This sets up the necessary state for communication with a Jupyter environment.*


### __enter__ (method, L118-L119, parent: JupyterKernelClient)

> *Summary: When entering a context manager, this method returns the instance itself, allowing for direct use of the object within a `with` block.*


### __exit__ (method, L121-L124, parent: JupyterKernelClient)

> *Summary: When an `with` block exits, this method ensures the underlying Jupyter client connection is properly terminated by calling the `stop()` method. It handles cleanup regardless of whether an exception occurred within the context manager.*


### stop (method, L126-L127, parent: JupyterKernelClient)

> *Summary: Closes the underlying WebSocket connection managed by the object. This method is called to terminate communication with a remote Jupyter kernel or service.*


### _send_message (method, L129-L148, parent: JupyterKernelClient)

> *Summary: Constructs a structured JSON message containing metadata like session ID, timestamp, and type, then transmits it over the underlying WebSocket connection. It accepts content, channel, and message type as inputs and returns the unique identifier assigned to the sent message.*


### _receive_message (method, L150-L158, parent: JupyterKernelClient)

> *Summary: This method waits for and receives a message from the underlying WebSocket connection, setting a specified timeout first. It decodes any received bytes into UTF-8 and parses the resulting JSON string into a Python dictionary, returning `None` upon a timeout.*


### wait_for_ready (method, L160-L171, parent: JupyterKernelClient)

> *Summary: Sends a kernel info request and then polls for a reply, returning `True` upon receiving the expected `kernel_info_reply` or `False` if a timeout occurs. This method waits until the Jupyter kernel confirms it is ready to receive commands.*


### execute (method, L173-L224, parent: JupyterKernelClient)

> *Summary: Sends a code string to the kernel via an `execute_request` and asynchronously waits for results. It aggregates textual output from `execute_result` and `stream` messages, captures rich media from `display_data`, and returns an `ExecutionResult` upon completion or timeout/error.*

