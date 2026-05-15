# test/beta/tools/test_execution.py

8 function(s): test_execute, test_execute_sync_without_thread, test_execute_async, test_return_model, test_return_result, test_tool_with_depends, test_tool_get_context, test_tool_get_context_by_random_name. 1 class(es): TestReturnInput. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_execute | function |  |
| test_execute_sync_without_thread | function |  |
| test_execute_async | function |  |
| test_return_model | function |  |
| test_return_result | function |  |
| test_tool_with_depends | function |  |
| test_tool_get_context | function |  |
| test_tool_get_context_by_random_name | function |  |
| TestReturnInput | class |  |

## Chunks

### test_execute (function, L17-L32)

> *Summary: This test verifies the execution flow of a tool by calling a decorated function with specific event and context inputs. It asserts that the returned result matches the expected output and confirms the underlying mock was called exactly once with the correct arguments.*


### test_execute_sync_without_thread (function, L36-L51)

> *Summary: This test verifies synchronous tool execution without threading by calling a decorated function with specific event and context inputs. It asserts that the returned result matches the expected output and that the mock was called correctly with parsed arguments.*


### test_execute_async (function, L55-L70)

> *Summary: This asynchronous test verifies the execution of a mocked tool function by simulating an incoming `ToolCallEvent`. It asserts that the function returns the expected string and that the underlying mock was called exactly once with the correct arguments.*


### test_return_model (function, L74-L91)

> *Summary: This test verifies that a decorated tool function correctly processes input and returns a structured result. It calls the mocked tool with specific arguments and asserts that the returned data matches the expected `Result` model instance.*


### test_return_result (function, L95-L105)

> *Summary: This test verifies that a decorated tool correctly returns its specified output when invoked asynchronously. It calls the mocked function with a `ToolCallEvent` and asserts that the returned `ToolResult` contains the expected string content.*


### test_tool_with_depends (function, L109-L125)

> *Summary: This test verifies a tool execution that relies on a dependency function. It calls `my_func` with specific arguments, expecting the output to be `"111"` after the dependency doubles the input string and it is concatenated with the first argument.*


### test_tool_get_context (function, L129-L142)

> *Summary: This test verifies that a decorated tool function correctly processes input arguments and context data. It calls the mocked tool with specific event and context objects, asserting that the returned string matches the content provided in the context's prompt list.*


### test_tool_get_context_by_random_name (function, L146-L159)

> *Summary: This test verifies that a tool function correctly retrieves and processes context data when invoked with a randomly named tool call event. It asserts the returned string matches the content provided in the mock context's prompt list.*


### TestReturnInput (class, L163-L266)

> *Summary: This test suite verifies how an `Agent` processes and handles various return types from decorated tools. It asserts correct parsing of single or multiple mixed input parts (text, data) returned by a tool call, while also testing error conditions for unsupported types or incorrect part counts.*


### config (method, L165-L171, parent: TestReturnInput)

> *Summary: Returns a `TrackingConfig` object containing a specific `TestConfig`. This configuration is initialized with an event representing a tool call named "my\_func" and the status "done".*


### test_tool_return_input (method, L173-L182, parent: TestReturnInput)

> *Summary: This test verifies that an agent correctly processes the output from a defined tool. It executes the agent's request, then asserts that the resulting `ToolResultEvent` contains the expected `DataInput` structure returned by the mocked function.*


### test_return_multiple_parts (method, L184-L199, parent: TestReturnInput)

> *Summary: This test verifies that an agent correctly processes and returns multiple distinct parts when a callable tool is executed. It asserts that the resulting `ToolResultEvent` contains both text input and structured data input as expected from the mocked tool call.*


### test_return_mixed_parts (method, L201-L216, parent: TestReturnInput)

> *Summary: This test verifies that an agent correctly processes and returns a mixed result from a tool call. It asserts that the resulting message contains both text input and structured data input as expected from the mocked tool execution.*


### test_text_input (method, L218-L226, parent: TestReturnInput)

> *Summary: This test verifies that an agent correctly executes a tool that accepts text input and returns the provided string. It initializes an agent with a mock function, prompts it to call the function, and asserts the response body matches the input text.*


### test_data_input (method, L228-L236, parent: TestReturnInput)

> *Summary: This test verifies that an agent correctly executes a defined tool and processes its output. It initializes an agent with a tool returning specific data, then asserts the agent's response body matches the expected input data structure.*


### test_unsupported_input_type (method, L238-L246, parent: TestReturnInput)

> *Summary: This test verifies that an agent correctly raises a `ValueError` when attempting to execute a tool that receives an unsupported input type. It achieves this by defining a tool expecting an image input and then prompting the agent to call it within a pytest context manager.*


### test_multiple_parts_raises (method, L248-L256, parent: TestReturnInput)

> *Summary: This test verifies that an agent raises a `ValueError` when a tool returns multiple input parts. It achieves this by defining a mock tool returning two distinct `TextInput` objects and then invoking the agent with a prompt to use it.*


### test_llm_not_called_again (method, L258-L266, parent: TestReturnInput)

> *Summary: This test verifies that an LLM-enabled agent calls a registered tool exactly once when prompted to use it. It initializes the agent with a single mockable tool and asserts the call count after executing a prompt.*

