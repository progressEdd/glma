# autogen/agentchat/contrib/agent_optimizer.py

1 function(s): execute_func. 1 class(es): AgentOptimizer. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| execute_func | function |  |
| AgentOptimizer | class |  |

## Chunks

### execute_func (function, L151-L172)

> *Summary: This utility wraps a generated function by first conditionally installing necessary packages via `pip`. It then executes the provided code string within a Docker container, capturing and returning the final output or raising an exception if the execution fails.*


### AgentOptimizer (class, L179-L452)

> *Summary: This deprecated class manages the optimization of agent functions by iteratively testing and refining a set of available tools. It accepts LLM configuration and an optimizer model, then uses conversational history and performance feedback to suggest additions or modifications to the function set in its `step()` method.*


### __init__ (method, L188-L237, parent: AgentOptimizer)

> *Summary: Initializes an optimizer agent, which is marked as deprecated, by setting parameters like the maximum actions per step and configuring its LLM access via `llm_config`. It validates that a valid LLM configuration is provided and sets up an `OpenAIWrapper` client using this configuration.*


### record_one_conversation (method, L239-L260, parent: AgentOptimizer)

> *Summary: This method logs a single conversation, accepting the chat history and an optional satisfaction flag. If the flag is missing, it prompts the user for input (1 or 0) before storing both the conversation transcript and its corresponding performance score in internal lists.*


### step (method, L262-L336, parent: AgentOptimizer)

> *Summary: Calculates the performance of recent trials and updates the best set of functions based on this evaluation. It then iteratively prompts an LLM to suggest function modifications (add/revise/remove) against the current best set, finally returning updated registration lists for the LLM and executor agents.*


### reset_optimizer (method, L338-L349, parent: AgentOptimizer)

> *Summary: Clears all stored history and performance metrics for both trial and best-case scenarios. This resets the internal state of the optimizer, preparing it for a new optimization run.*


### _update_function_call (method, L351-L396, parent: AgentOptimizer)

> *Summary: Processes a list of agent actions to update a set of existing functions. It parses the input actions—handling both function additions and removals—and returns a new list of functions reflecting these changes.*


### _construct_intermediate_prompt (method, L398-L417, parent: AgentOptimizer)

> *Summary: Generates two distinct prompt strings by aggregating performance data. It compiles a list of underperforming functions and their scores into one string, and another string summarizing the success/failure statistics from the best conversations.*


### _validate_actions (method, L419-L452, parent: AgentOptimizer)

> *Summary: Checks if a list of proposed actions is valid by ensuring arguments are correctly formatted JSON and that any provided code snippets compile without syntax errors. It also verifies that functions slated for removal actually exist within the set of incumbent functions.*

