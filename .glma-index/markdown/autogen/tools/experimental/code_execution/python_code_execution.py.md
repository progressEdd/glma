# autogen/tools/experimental/code_execution/python_code_execution.py

1 class(es): PythonCodeExecutionTool. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PythonCodeExecutionTool | class |  |

## Chunks

### PythonCodeExecutionTool (class, L21-L93)

> *Summary: This class provides a mechanism to execute Python code within a specified environment, accepting the code and a list of required libraries as input. It returns the execution result after respecting a configured timeout, while issuing a deprecation warning for its use.*


### __init__ (method, L24-L85, parent: PythonCodeExecutionTool)

> *Summary: Initializes a tool for executing Python code, accepting optional timeout, working directory, and environment configurations. It internally defines an asynchronous execution function that takes code and required libraries to run within the specified environment, returning the execution result.*


### _get_script_directory (method, L87-L93, parent: PythonCodeExecutionTool)

> *Summary: Determines the directory for script execution by first checking if a valid `working_directory` is set; otherwise, it creates and returns a unique temporary directory.*

