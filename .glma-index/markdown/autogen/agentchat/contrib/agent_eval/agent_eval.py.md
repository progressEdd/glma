# autogen/agentchat/contrib/agent_eval/agent_eval.py

2 function(s): generate_criteria, quantify_criteria.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| generate_criteria | function |  |
| quantify_criteria | function |  |

## Chunks

### generate_criteria (function, L21-L73)

> *Summary: Given LLM configuration, a task object, and optional instructions, this function orchestrates a group chat between agents to generate evaluation criteria for the provided task. It returns a list of `Criterion` objects derived from the final message content of the conversation.*


### quantify_criteria (function, L76-L119)

> *Summary: Evaluates system performance by initiating a chat between a `QuantifierAgent` and a user proxy, using provided criteria, task details, and test case. It returns a dictionary containing the ground truth and the agent's estimated performance assessment derived from the chat output.*

