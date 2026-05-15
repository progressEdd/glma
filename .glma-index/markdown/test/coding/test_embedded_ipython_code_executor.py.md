# test/coding/test_embedded_ipython_code_executor.py

3 class(es): DockerJupyterExecutor, LocalJupyterCodeExecutor, TestCodeExecutor. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DockerJupyterExecutor | class |  |
| LocalJupyterCodeExecutor | class |  |
| TestCodeExecutor | class |  |

## Chunks

### DockerJupyterExecutor (class, L40-L43)

> *Summary: This class initializes a code executor by instantiating and passing a `DockerJupyterServer` instance to its parent class. It effectively sets up the execution environment using a containerized Jupyter server.*


### __init__ (method, L41-L43, parent: DockerJupyterExecutor)

> *Summary: Initializes the object by instantiating a `DockerJupyterServer` and passing it to the parent class constructor. This sets up the necessary Jupyter server environment for subsequent operations.*


### LocalJupyterCodeExecutor (class, L46-L49)

> *Summary: Initializes a code executor by instantiating and using a `LocalJupyterServer`. This class inherits from `JupyterCodeExecutor` to manage local Jupyter server interactions.*


### __init__ (method, L47-L49, parent: LocalJupyterCodeExecutor)

> *Summary: Initializes the object by instantiating a `LocalJupyterServer` and passing it to the parent class constructor. This sets up the necessary Jupyter server environment for subsequent operations.*


### TestCodeExecutor (class, L75-L244)

> *Summary: This test suite verifies the functionality of various `CodeExecutor` implementations by instantiating them and executing different types of code blocks. It tests core behaviors such as successful execution, handling timeouts, managing state across executions, saving output files (images/HTML), and integration with an agent framework.*


### test_import_utils (method, L76-L77, parent: TestCodeExecutor)

> *Summary: This test method is designed to verify the functionality of import utilities, although it currently contains no implementation. It takes no inputs and returns nothing upon execution.*


### test_is_code_executor (method, L80-L81, parent: TestCodeExecutor)

> *Summary: Verifies that the provided class instance is indeed an instance of `CodeExecutor`. This acts as a type check to ensure correct object instantiation.*


### test_create_dict (method, L83-L86, parent: TestCodeExecutor)

> *Summary: This test verifies that the factory correctly instantiates an `EmbeddedIPythonCodeExecutor` when provided a configuration dictionary specifying `"ipython-embedded"`. It asserts the resulting object's type matches the expected implementation.*


### test_create (method, L89-L92, parent: TestCodeExecutor)

> *Summary: This test verifies that the factory correctly instantiates and returns the provided `CodeExecutor` object when given a configuration dictionary containing it. It asserts that the returned executor instance is identical to the one passed in the input configuration.*


### test_init (method, L95-L105, parent: TestCodeExecutor)

> *Summary: This test verifies the initialization of an executor class by asserting correct default parameter settings and ensuring that instantiation fails with specific `ValueError` exceptions when provided with non-existent output directories or unsupported kernel names. It confirms the constructor enforces valid configuration inputs.*


### test_execute_code_single_code_block (method, L108-L112, parent: TestCodeExecutor)

> *Summary: This test verifies that executing a single Python code block successfully runs the script, resulting in an exit code of zero and capturing the expected output string. It passes a list containing one `CodeBlock` instance to the executor's execution method.*


### test_execute_code_multiple_code_blocks (method, L115-L133, parent: TestCodeExecutor)

> *Summary: This test verifies that an execution engine can process a sequence of distinct code blocks, both independently and sequentially. It asserts correct output based on the combined execution results from multiple Python snippets provided as input.*


### test_execute_code_bash_script (method, L136-L141, parent: TestCodeExecutor)

> *Summary: This test verifies that the code execution mechanism correctly runs a bash script command (`!echo "hello world!"`). It asserts that the execution returns an exit code of zero and captures the expected output string.*


### test_timeout (method, L144-L148, parent: TestCodeExecutor)

> *Summary: This test verifies that the code execution mechanism correctly times out when provided with a long-running script. It executes a block designed to sleep for ten seconds, asserting that the resulting output indicates a timeout occurred within the one-second limit.*


### test_silent_pip_install (method, L151-L160, parent: TestCodeExecutor)

> *Summary: This test verifies how the code execution environment handles `pip install` commands. It asserts that a successful installation yields no output, while an attempt to install a non-existent package results in a specific error message within the captured output.*


### test_restart (method, L163-L172, parent: TestCodeExecutor)

> *Summary: This test verifies the state reset functionality of a code execution environment. It first executes some code, then calls `restart()`, and finally asserts that subsequent code execution fails with a `NameError` because variables from the previous session are cleared.*


### test_save_image (method, L175-L190, parent: TestCodeExecutor)

> *Summary: This test verifies image saving functionality by first installing `matplotlib` within a temporary directory context. It then executes Python code that plots data, asserting that the execution succeeds and an output file containing the generated image is created.*


### test_timeout_preserves_kernel_state (method, L193-L205, parent: TestCodeExecutor)

> *Summary: This test verifies that a code execution environment with a timeout correctly preserves the state between executions. It first runs code to set a variable, then executes a blocking operation causing a timeout, and finally confirms the previously set variable is accessible after the timeout.*


### test_save_html (method, L208-L218, parent: TestCodeExecutor)

> *Summary: This test verifies that the executor correctly saves HTML output when provided with a Python `CodeBlock` containing IPython display commands. It asserts successful execution and confirms the existence and content of the generated output file within a temporary directory.*


### test_conversable_agent_code_execution (method, L221-L244, parent: TestCodeExecutor)

> *Summary: This test verifies that a `ConversableAgent` correctly executes Python code provided within a user message. It sends a prompt containing two code blocks to the agent and asserts that the resulting reply contains the expected output from the executed code (`492`).*

