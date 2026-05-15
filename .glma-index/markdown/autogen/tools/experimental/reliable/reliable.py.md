# autogen/tools/experimental/reliable/reliable.py

7 function(s): _configure_llm_for_structured_output, _get_last_non_empty_message_content, _get_reliable_tool_context, _set_reliable_tool_context, get_runner_prompt, get_validator_prompt, reliable_function_wrapper. 7 class(es): ValidationResult, ExecutionAttempt, ReliableToolContext, SuccessfulExecutionParameters, ToolExecutionDetails, ReliableToolError, ReliableTool. 31 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ValidationResult | class |  |
| ExecutionAttempt | class |  |
| ReliableToolContext | class |  |
| SuccessfulExecutionParameters | class |  |
| ToolExecutionDetails | class |  |
| _configure_llm_for_structured_output | function |  |
| _get_last_non_empty_message_content | function |  |
| _get_reliable_tool_context | function |  |
| _set_reliable_tool_context | function |  |
| get_runner_prompt | function |  |
| get_validator_prompt | function |  |
| reliable_function_wrapper | function |  |
| ReliableToolError | class |  |
| ReliableTool | class |  |

## Chunks

### ValidationResult (class, L45-L58)

> *Summary: This data structure encapsulates the outcome of a validation check, holding a boolean result and an explanatory string. It provides methods to return a human-readable status string or its standardized JSON format for system integration.*


### __str__ (method, L52-L54, parent: ValidationResult)

> *Summary: Generates a human-readable string representation of the object, indicating whether validation passed or failed and including any associated justification. The output is a formatted string containing the status and the justification text.*


### format (method, L56-L58, parent: ValidationResult)

> *Summary: Generates a JSON string representation of the object, making it compatible with AutoGen systems. This method uses `model_dump_json()` to serialize the internal state into a standardized format.*


### ExecutionAttempt (class, L61-L82)

> *Summary: This data structure encapsulates the state of a single function execution attempt, storing inputs (arguments/kwargs), timestamps, potential errors, and final results. It provides properties to easily check if the attempt executed without error or passed subsequent validation.*


### did_execute_successfully (method, L75-L77, parent: ExecutionAttempt)

> *Summary: Determines if a previous execution succeeded by checking if the internal `error` attribute is null. Returns a boolean indicating successful completion or failure.*


### did_validate_successfully (method, L80-L82, parent: ExecutionAttempt)

> *Summary: Checks the internal state to determine if a previous validation attempt succeeded. It returns `True` only if a validation result exists and that result indicates success.*


### ReliableToolContext (class, L85-L139)

> *Summary: This context object manages the state and history of a reliable tool execution, tracking inputs like task description and initial ground truth. It provides properties to check completion status, retrieve final results from successful attempts, and generate a summary detailing any failures encountered during the process.*


### attempt_count (method, L100-L102, parent: ReliableToolContext)

> *Summary: Retrieves the total count of execution attempts stored within the object's `attempts` list, returning this integer value.*


### latest_attempt (method, L105-L107, parent: ReliableToolContext)

> *Summary: Retrieves and returns the last recorded execution attempt from a list of attempts, or `None` if no attempts have been made.*


### is_complete_and_successful (method, L110-L113, parent: ReliableToolContext)

> *Summary: Determines if the current process has reached a state where it completed execution and passed validation checks. It returns `True` only if the most recent attempt exists and both its execution and validation were successful.*


### get_final_result_data (method, L115-L119, parent: ReliableToolContext)

> *Summary: Retrieves the `result_data` from the most recent attempt if the process has completed successfully and is validated. Otherwise, it returns `None`.*


### get_final_result_str (method, L121-L125, parent: ReliableToolContext)

> *Summary: Retrieves the final string result if the process has completed successfully and a latest attempt exists. Otherwise, it returns `None`.*


### get_failure_summary (method, L127-L139, parent: ReliableToolContext)

> *Summary: Retrieves a string summarizing the reason for an execution's failure based on its latest attempt. It checks if no attempts were made, if the execution itself failed, or if it succeeded but failed validation, returning a descriptive message for each case.*


### SuccessfulExecutionParameters (class, L142-L147)

> *Summary: This data structure encapsulates the inputs and parameters used when a tool function executes successfully. It stores both positional arguments (`attempt_args`) and keyword arguments (`attempt_kwargs`) from the execution.*


### ToolExecutionDetails (class, L150-L158)

> *Summary: This data structure encapsulates the complete outcome of a tool execution. It stores details like the task performed, overall success status, any failure reason, successful parameter values, and the final context from the reliable tool.*


### _configure_llm_for_structured_output (function, L161-L243)

> *Summary: This function modifies an existing LLM configuration to enforce structured output based on a provided Pydantic model. It validates the inputs, sets the `response_format` field to the specified model, and removes any conflicting keys like `tools` or `functions`, recursively applying this logic if the config contains a list of configurations.*


### _get_last_non_empty_message_content (function, L246-L274)

> *Summary: This utility iterates backward through a list of message dictionaries to find the content of the most recent message that is not empty. It prioritizes returning stripped text content, falling back to joining text parts from multimodal lists or serializing the first non-empty item if no plain text is found.*


### _get_reliable_tool_context (function, L277-L298)

> *Summary: Retrieves and validates a `ReliableToolContext` object using a provided context key from `ContextVariables`. It accepts the data as either a JSON string or an already structured type, raising errors if the key is missing or the data cannot be successfully parsed.*


### _set_reliable_tool_context (function, L301-L321)

> *Summary: This function serializes a `ReliableToolContext` object into a JSON string and stores it within provided context variables under a specified key. It handles serialization errors by logging the failure with partial context information before raising a `ValueError`.*


### get_runner_prompt (function, L324-L341)

> *Summary: Constructs a detailed system prompt for an internal runner agent, instructing it to invoke a specified tool exactly once. It incorporates the task description, base instructions, and context about previous attempts to guide argument selection and require a "hypothesis" summary in the output.*


### get_validator_prompt (function, L344-L368)

> *Summary: Constructs a comprehensive system prompt for an AI validator agent, taking the task description and base validation rules as primary inputs. It dynamically incorporates optional additional requirements to guide the agent in evaluating a final function call result against all provided context.*


### reliable_function_wrapper (function, L371-L513)

> *Summary: This function wraps a provided tool function to add reliability features by injecting `hypothesis` and `context_variables` arguments. It returns a new callable that executes the original logic while managing execution attempts, error handling (routing errors to a runner), and formatting successful results for validation.*


### ReliableToolError (class, L517-L522)

> *Summary: This custom exception signals failures encountered while executing a `ReliableTool`. It accepts an optional `ReliableToolContext` object to store the state of the tool at the time of failure.*


### __init__ (method, L520-L522, parent: ReliableToolError)

> *Summary: Initializes the object with a required string message and an optional `ReliableToolContext`. This sets up the necessary context for subsequent reliable tool operations.*


### ReliableTool (class, L526-L1311)

> *Summary: Wraps an existing function or tool to ensure reliable execution by initiating an internal Group Chat between a Runner and Validator agent. It accepts the core capability, LLM configurations for both agents, and optional context like initial messages or ground truth data to iteratively retry and validate the output against defined criteria. The primary outputs are either the validated result upon success or a `ReliableToolError` detailing the failure reason after exhausting retries.*


### __init__ (method, L529-L699, parent: ReliableTool)

> *Summary: Initializes a wrapper around an existing function or tool to enforce reliability through iterative execution and validation. It accepts configurations for internal Runner and Validator LLMs, along with parameters controlling retry limits, system prompts, and initial context data. The resulting object manages the complex orchestration between these agents to ensure the underlying capability produces a satisfactory result.*


### _define_public_entry_point (method, L701-L729, parent: ReliableTool)

> *Summary: This method generates and returns a callable entry point based on whether asynchronous execution is required and if dynamic validation should be enabled. It wraps the core `self.run` or `self.a_run` methods, providing specific signatures for synchronous/asynchronous calls with or without optional validation prompts.*


### _extract_func_details (method, L731-L753, parent: ReliableTool)

> *Summary: This method processes either a raw callable function or an `autogen.Tool` object to extract its underlying function, name, and description. It intelligently derives the description from existing metadata or falls back to docstrings or a default template if none are present.*


### _setup_validator_agent (method, L755-L772, parent: ReliableTool)

> *Summary: Configures and returns a `ConversableAgent` instance designed to validate outputs. It takes the stored validator LLM configuration as input, processes it using structured output tooling against a `ValidationResult`, and initializes the agent with specific system prompts and settings.*


### _setup_runner_agent (method, L774-L782, parent: ReliableTool)

> *Summary: Creates and returns a `ConversableAgent` instance configured to act as the execution runner. It initializes this agent using a deep copy of the stored LLM configuration and sets its human input mode to never.*


### _setup_runner_tool (method, L784-L792, parent: ReliableTool)

> *Summary: This method configures and registers an internal `Tool` instance using the object's original function name as a prefix for its identifier. It wraps the core logic within a wrapper function and attaches this tool to the associated runner for execution.*


### _register_internal_hooks (method, L794-L801, parent: ReliableTool)

> *Summary: This method configures internal validation and execution hooks by registering specific callback functions with the validator and runner components. It ensures that message processing is intercepted before sending and replying to enforce structured output and function call integrity.*


### _validator_structured_output_hook (method, L803-L824, parent: ReliableTool)

> *Summary: This method validates an incoming message from an agent by attempting to parse it as a structured JSON object using `ValidationResult`. It logs the success or failure of the parsing and updates the context based on the result before returning the validated data as a JSON string.*


### _set_validator_handoff (method, L826-L832, parent: ReliableTool)

> *Summary: This method configures the next step for a validator agent based on validation success. If validation fails, it directs the agent to the runner; otherwise, it instructs the agent to terminate.*


### _try_update_context_validation (method, L834-L852, parent: ReliableTool)

> *Summary: This method updates the validation state within a specific tool's execution context using a provided `ValidationResult`. It retrieves the relevant context from the sender's variables, overwrites the previous attempt's validation status with the new result, and logs the change.*


### _validator_construct_context_hook (method, L854-L880, parent: ReliableTool)

> *Summary: This method constructs a context list by combining pre-existing tool contexts, injected ground truth messages, and the last non-empty message content from an input history. It returns this aggregated list of messages to be used in validation processes.*


### _ensure_function_call_hook (method, L882-L933, parent: ReliableTool)

> *Summary: If the sender is not this agent, the input message is returned unchanged. Otherwise, it checks for a specific tool call within the message; if one isn't found, it injects a system reminder into the message content and returns a modified dictionary to force a retry by the runner agent.*


### _execute_internal_group_chat (method, L935-L1000, parent: ReliableTool)

> *Summary: This method orchestrates a multi-agent internal group chat by configuring system prompts for the runner and validator agents based on the provided task and validation string. It initializes the conversation history with any existing context or ground truth before executing the chat using `initiate_group_chat` to produce a final reply, updated context variables, and the last responding agent.*


### _prepare_tool_context (method, L1002-L1022, parent: ReliableTool)

> *Summary: This method constructs or updates a `ReliableToolContext` object based on provided task details and optional inputs like messages or ground truth. It initializes the context with these values and registers it within the current execution environment before returning the configured context.*


### _process_run (method, L1024-L1075, parent: ReliableTool)

> *Summary: This method orchestrates the execution of a task by first preparing context and then running an internal group chat simulation using provided inputs like tasks and messages. It returns the final result data if the process completes successfully, or raises a `ReliableToolError` detailing the failure reason otherwise.*


### run (method, L1077-L1093, parent: ReliableTool)

> *Summary: Executes the underlying reliable tool logic by calling an internal processing method. It accepts a task string and optional inputs like context variables, validation prompts, message history, or ground truth data. The function returns the result of the execution, raising an error if called on an asynchronous tool instance.*


### a_run (method, L1095-L1120, parent: ReliableTool)

> *Summary: Executes a synchronous internal processing method asynchronously by offloading it to the event loop's executor. It accepts task details, optional context, validation prompts, messages, and ground truth data as inputs, returning the result of the underlying process.*


### _process_run_with_details (method, L1122-L1244, parent: ReliableTool)

> *Summary: Executes a task by managing and iterating through context variables across internal group chat cycles to ensure reliable tool execution. It accepts inputs like the task name, initial context, validation prompts, messages, and ground truth, returning a `ToolExecutionDetails` object summarizing success status, failure reasons, successful parameters, and the final state of the tool's context.*


### run_and_get_details (method, L1246-L1265, parent: ReliableTool)

> *Summary: This method executes a tool by processing the provided task and optional inputs like context variables or ground truth. It returns detailed execution results after ensuring it is not called synchronously if the underlying tool is asynchronous.*


### a_run_and_get_details (method, L1267-L1311, parent: ReliableTool)

> *Summary: Executes a synchronous tool function asynchronously by running it in an executor thread. It accepts task details like context variables, messages, and ground truth to return comprehensive execution results or a failure object upon exception.*

