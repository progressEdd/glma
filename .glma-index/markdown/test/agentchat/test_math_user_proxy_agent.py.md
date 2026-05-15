# test/agentchat/test_math_user_proxy_agent.py

6 function(s): test_math_user_proxy_agent, test_add_remove_print, test_math_user_proxy_agent_no_pydantic_deprecation_warning, test_execute_one_python_code, test_execute_one_wolfram_query, test_generate_prompt.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_math_user_proxy_agent | function |  |
| test_add_remove_print | function |  |
| test_math_user_proxy_agent_no_pydantic_deprecation_warning | function |  |
| test_execute_one_python_code | function |  |
| test_execute_one_wolfram_query | function |  |
| test_generate_prompt | function |  |

## Chunks

### test_math_user_proxy_agent (function, L26-L50)

> *Summary: This test function sets up an `AssistantAgent` and a `MathUserProxyAgent` to simulate a mathematical problem-solving conversation. It initiates a chat with the math problem "$x^3=125$. What is x?" and asserts the resulting summary and history from the interaction.*


### test_add_remove_print (function, L53-L64)

> *Summary: This test verifies helper functions designed to manipulate Python code strings. It asserts that one function correctly appends a `print` statement to the last line of provided code, and another function successfully removes all non-indented `print` statements from a given code block while preserving indented ones.*


### test_math_user_proxy_agent_no_pydantic_deprecation_warning (function, L67-L79)

> *Summary: This test verifies that importing and reloading the `MathUserProxyAgent` module does not trigger any `PydanticDeprecatedSince20` warnings. It achieves this by temporarily capturing all emitted warnings during the import process and asserting their absence.*


### test_execute_one_python_code (function, L86-L110)

> *Summary: This test verifies the `MathUserProxyAgent`'s ability to execute Python code by passing strings as input. It asserts expected outputs for cases with no print statements, runtime errors, successful variable execution, and overly long output responses.*


### test_execute_one_wolfram_query (function, L113-L122)

> *Summary: This test verifies the execution of a single Wolfram query by initializing an agent and calling `execute_one_wolfram_query` with a mathematical expression string. It handles potential exceptions, such as missing API keys or uninstalled packages, to gracefully skip the test if dependencies are not met.*


### test_generate_prompt (function, L125-L130)

> *Summary: This test verifies that the agent's message generator incorporates a specific customization when provided with input data. It asserts that the generated prompt string contains the substring "customized" based on the provided configuration.*

