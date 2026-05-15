# test/agentchat/test_function_call.py

6 function(s): test_eval_math_responses, test_json_extraction, test_execute_function, test_a_execute_function, test_a_execute_function_awaits_awaitable_returned_by_sync_callable, test_update_function.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_eval_math_responses | function |  |
| test_json_extraction | function |  |
| test_execute_function | function |  |
| test_a_execute_function | function |  |
| test_a_execute_function_awaits_awaitable_returned_by_sync_callable | function |  |
| test_update_function | function |  |

## Chunks

### test_eval_math_responses (function, L22-L66)

> *Summary: This test case defines a function schema to evaluate math responses, then sends a prompt containing candidate answers and the true solution to an OpenAI client. It extracts the resulting function call arguments and executes a local evaluation function using those inputs.*


### test_json_extraction (function, L69-L87)

> *Summary: This test verifies the `_format_json_str` method, which standardizes input JSON strings by removing extraneous whitespace and normalizing internal newlines/tabs into escaped characters. It confirms correct formatting across various inputs, including complex structures, empty objects, and embedded quotes.*


### test_execute_function (function, L90-L152)

> *Summary: This test suite verifies the `execute_function` method of a `UserProxyAgent`, ensuring it correctly handles various function call scenarios. It validates successful execution with simple and class methods, while also asserting error handling for invalid function names, malformed JSON arguments, incorrect argument structures, and runtime exceptions.*


### test_a_execute_function (function, L156-L209)

> *Summary: This test suite verifies the `UserProxyAgent`'s ability to execute functions and methods based on provided call specifications. It asserts correct execution for valid calls, while also checking error handling for invalid function names, malformed JSON arguments, and runtime errors within the executed code.*


### test_a_execute_function_awaits_awaitable_returned_by_sync_callable (function, L213-L229)

> *Summary: This test verifies that when a synchronous callable returns an awaitable object, the agent correctly awaits it during function execution. It calls `a_execute_function` with a defined function map and asserts the returned content matches the expected asynchronous calculation.*


### test_update_function (function, L237-L302)

> *Summary: This test verifies how an agent's knowledge of defined functions changes during a chat session. It first adds a function signature, confirms the assistant knows about it, then removes the signature and asserts the assistant no longer references it in subsequent chats, finally testing for expected errors when using invalid `summary_method` arguments.*

