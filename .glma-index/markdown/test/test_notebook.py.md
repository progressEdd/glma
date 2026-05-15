# test/test_notebook.py

13 function(s): run_notebook, test_agentchat_auto_feedback_from_code, _test_oai_completion, test_agentchat_function_call, test_agentchat_function_call_currency_calculator, test_agentchat_function_call_async, _test_agentchat_MathChat, _test_oai_chatgpt_gpt4, test_agentchat_groupchat_finite_state_machine, test_agentchat_cost_token_tracking and 3 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| run_notebook | function |  |
| test_agentchat_auto_feedback_from_code | function |  |
| _test_oai_completion | function |  |
| test_agentchat_function_call | function |  |
| test_agentchat_function_call_currency_calculator | function |  |
| test_agentchat_function_call_async | function |  |
| _test_agentchat_MathChat | function |  |
| _test_oai_chatgpt_gpt4 | function |  |
| test_agentchat_groupchat_finite_state_machine | function |  |
| test_agentchat_cost_token_tracking | function |  |
| test_agentchat_groupchat_stateflow | function |  |
| test_agentchat_grok_sbom_analysisw | function |  |
| test_agentchat_gpt_5_verbosity_example | function |  |

## Chunks

### run_notebook (function, L19-L44)

> *Summary: Executes a Jupyter notebook specified by `input_nb` using the Python 3 kernel and saves the resulting code cell outputs to a text file. Optionally, it can also save the fully executed notebook to `output_nb`.*


### test_agentchat_auto_feedback_from_code (function, L52-L53)

> *Summary: Executes a specific Jupyter notebook, `agentchat_auto_feedback_from_code_execution.ipynb`, to test automatic feedback generation from code execution results. The optional `save` parameter controls whether the resulting notebook is persisted.*


### _test_oai_completion (function, L61-L62)

> *Summary: Executes a specific notebook named "oai\_completion.ipynb" using the `run_notebook` utility, optionally saving the output.*


### test_agentchat_function_call (function, L70-L71)

> *Summary: Executes a specific Jupyter notebook, `agentchat_function_call.ipynb`, to test agent chat function calling capabilities, with an optional flag to persist the output.*


### test_agentchat_function_call_currency_calculator (function, L79-L80)

> *Summary: Executes a specific notebook file, `agentchat_function_call_currency_calculator.ipynb`, to test agent chat functionality involving currency calculations. The optional `save` parameter controls whether the execution results are persisted.*


### test_agentchat_function_call_async (function, L88-L89)

> *Summary: Executes a specific Jupyter notebook file, `agentchat_function_call_async.ipynb`, which tests asynchronous function calling within an agent chat context. The optional `save` parameter controls whether the execution results are persisted.*


### _test_agentchat_MathChat (function, L97-L98)

> *Summary: Executes a specific notebook file, `agentchat_MathChat.ipynb`, using the provided `run_notebook` utility. It optionally saves the execution results based on the `save` parameter.*


### _test_oai_chatgpt_gpt4 (function, L106-L107)

> *Summary: Executes a specific notebook file, `oai_chatgpt_gpt4.ipynb`, optionally saving the results based on the provided boolean flag.*


### test_agentchat_groupchat_finite_state_machine (function, L115-L116)

> *Summary: Executes a specific Jupyter notebook file to test the finite state machine logic for agent group chat scenarios. The function accepts an optional boolean argument to control whether the notebook output is saved.*


### test_agentchat_cost_token_tracking (function, L124-L125)

> *Summary: Executes a specific notebook file, `agentchat_cost_token_tracking.ipynb`, optionally saving the results. This test verifies token cost tracking within an agent chat context.*


### test_agentchat_groupchat_stateflow (function, L133-L134)

> *Summary: Executes a specific notebook file, `agentchat_groupchat_stateflow.ipynb`, to test the group chat state flow logic. It accepts an optional boolean argument to control whether the execution results are saved.*


### test_agentchat_grok_sbom_analysisw (function, L142-L143)

> *Summary: Executes a specific Jupyter notebook, `agentchat_grok_sbom_analysis.ipynb`, optionally saving the output based on the provided boolean flag. This serves as a test case to run and validate the notebook's contents.*


### test_agentchat_gpt_5_verbosity_example (function, L151-L152)

> *Summary: Executes a specific notebook file, `agentchat_gpt-5_verbosity_example.ipynb`, using the provided `run_notebook` utility, with an optional flag to persist the results.*

