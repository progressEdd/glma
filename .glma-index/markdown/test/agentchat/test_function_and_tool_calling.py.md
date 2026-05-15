# test/agentchat/test_function_and_tool_calling.py

12 function(s): _tool_func_1, _tool_func_2, _tool_func_error, _a_tool_func_1, _a_tool_func_2, _a_tool_func_error, _get_function_map, _get_error_function_map, test_generate_function_call_reply_on_function_call_message, test_a_generate_function_call_reply_on_function_call_message and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _tool_func_1 | function |  |
| _tool_func_2 | function |  |
| _tool_func_error | function |  |
| _a_tool_func_1 | function |  |
| _a_tool_func_2 | function |  |
| _a_tool_func_error | function |  |
| _get_function_map | function |  |
| _get_error_function_map | function |  |
| test_generate_function_call_reply_on_function_call_message | function |  |
| test_a_generate_function_call_reply_on_function_call_message | function |  |
| test_generate_tool_calls_reply_on_function_call_message | function |  |
| test_a_generate_tool_calls_reply_on_function_call_message | function |  |

## Chunks

### _tool_func_1 (function, L20-L21)

> *Summary: This function accepts two string arguments and returns a formatted string combining those inputs. It serves as a simple mock tool implementation for testing agent capabilities.*


### _tool_func_2 (function, L24-L25)

> *Summary: This function accepts two string arguments and returns a formatted string concatenating the input values with a prefix. It serves as a simple mock tool implementation for testing agent capabilities.*


### _tool_func_error (function, L28-L29)

> *Summary: This helper raises a `RuntimeError` with a specific message when called with two string arguments. It simulates an error condition within a tool function for testing purposes.*


### _a_tool_func_1 (function, L32-L33)

> *Summary: This asynchronous function accepts two string arguments and returns a formatted string containing both inputs. It simulates the behavior of a callable tool or function for testing purposes.*


### _a_tool_func_2 (function, L36-L37)

> *Summary: This asynchronous function accepts two string arguments and returns a formatted string containing both inputs. It simulates a simple tool execution by concatenating the provided strings with a prefix.*


### _a_tool_func_error (function, L40-L41)

> *Summary: This asynchronous function simulates a tool failure by immediately raising a `RuntimeError` when called with two string arguments. It serves to test error handling within the agent's tool-calling mechanism.*


### _get_function_map (function, L207-L229)

> *Summary: Constructs and returns a dictionary mapping tool names to their corresponding callable functions. The returned map's contents depend on whether the functions are asynchronous and if one of the tools should be excluded based on the `drop_tool_2` flag.*


### _get_error_function_map (function, L232-L244)

> *Summary: This utility constructs a mapping of tool function names to their corresponding callable implementations. It selects between success and error versions of the functions based on the `error_on_tool_func_2` flag and whether the functions are asynchronous (`is_function_async`).*


### test_generate_function_call_reply_on_function_call_message (function, L248-L292)

> *Summary: Tests the `generate_function_call_reply` method by simulating various message inputs to an agent. It verifies expected outputs for scenarios including missing functions, valid function calls, malformed JSON, tool usage, plain text messages, and exceptions raised during function execution.*


### test_a_generate_function_call_reply_on_function_call_message (function, L297-L341)

> *Summary: This test verifies the behavior of an agent's function call reply generation by simulating various message inputs. It asserts correct outputs for cases involving no functions defined, valid function calls, malformed JSON, tool use requests, plain text messages, and exceptions raised during function execution.*


### test_generate_tool_calls_reply_on_function_call_message (function, L345-L389)

> *Summary: This test verifies the behavior of an agent's reply generation when processing various message types related to tool and function calls. It asserts correct outputs for cases involving no functions available, multiple successful calls, invalid JSON input, direct function execution, plain text messages, and exceptions raised during function execution.*


### test_a_generate_tool_calls_reply_on_function_call_message (function, L394-L438)

> *Summary: This test verifies the behavior of an agent's reply generation when processing various message types. It asserts expected outcomes—such as successful replies, specific error responses for bad JSON or function execution errors, and non-finished states for text/function use messages—based on the input message list and configured tool map.*

