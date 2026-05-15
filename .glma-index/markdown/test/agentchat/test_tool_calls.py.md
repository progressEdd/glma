# test/agentchat/test_tool_calls.py

5 function(s): test_eval_math_responses, test_eval_math_responses_api_style_function, test_update_tool, test_multi_tool_call, test_async_multi_tool_call.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_eval_math_responses | function |  |
| test_eval_math_responses_api_style_function | function |  |
| test_update_tool | function |  |
| test_multi_tool_call | function |  |
| test_async_multi_tool_call | function |  |

## Chunks

### test_eval_math_responses (function, L25-L74)

> *Summary: This test verifies the model's ability to use a specific function tool for evaluating math responses. It sends a user prompt containing candidate answers and a true solution, then asserts that the model correctly invokes the `eval_math_responses` function with the provided data before executing it.*


### test_eval_math_responses_api_style_function (function, L80-L125)

> *Summary: This test case verifies the ability of an LLM to correctly invoke a predefined function for evaluating math responses. It sends a user prompt containing candidate answers and a true solution, then extracts the structured function call arguments from the model's response before executing the actual evaluation logic.*


### test_update_tool (function, L134-L184)

> *Summary: This test verifies that an agent can dynamically add and remove tool signatures using `update_tool_signature`. It initiates chats to confirm the model recognizes a newly added function, and then confirms it no longer references the function after it has been explicitly removed.*


### test_multi_tool_call (function, L188-L279)

> *Summary: This test verifies that an agent correctly processes a message containing multiple requested tool calls. It simulates receiving three distinct function calls, asserting that the system responds with the results for each call, including one simulated failure.*


### test_async_multi_tool_call (function, L284-L383)

> *Summary: This test verifies asynchronous handling of multiple tool calls by simulating an agent receiving a message containing three function call requests. It asserts that the system correctly processes responses for the first two tools while reporting an error for the third, unknown tool.*

