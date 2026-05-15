# test/agentchat/contrib/capabilities/test_teachable_agent.py

6 function(s): create_teachable_agent, check_agent_response, use_question_answer_phrasing, use_task_advice_pair_phrasing, test_teachability_code_paths, test_teachability_accuracy.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| create_teachable_agent | function |  |
| check_agent_response | function |  |
| use_question_answer_phrasing | function |  |
| use_task_advice_pair_phrasing | function |  |
| test_teachability_code_paths | function |  |
| test_teachability_accuracy | function |  |

## Chunks

### create_teachable_agent (function, L25-L44)

> *Summary: This function constructs and returns a `ConversableAgent` equipped with a `Teachability` capability. It takes credentials for LLM configuration and optional flags to control database resetting and logging verbosity during setup.*


### check_agent_response (function, L47-L55)

> *Summary: This function verifies if a specific `correct_answer` string is present within the content of the agent's last message, which is retrieved using the provided `user` and `teachable_agent`. It returns `1` if the answer is missing (a failure) or `0` if it is found (a success).*


### use_question_answer_phrasing (function, L58-L90)

> *Summary: This function tests if a teachable agent can recall and apply newly learned information across separate chat sessions. It initializes an agent with credentials, teaches it a specific concept via conversation, and then verifies its ability to answer related questions in a fresh chat context by comparing the output against expected values.*


### use_task_advice_pair_phrasing (function, L93-L122)

> *Summary: This function tests if a teachable agent can apply a newly learned skill after being provided with task-advice in an initial chat session. It initializes the agent, first teaches it a specific calculation rule via a hint, and then verifies its ability to correctly perform that same type of calculation in a subsequent, context-free conversation.*


### test_teachability_code_paths (function, L129-L153)

> *Summary: This test function executes unit tests by calling two different phrasing methods (`use_question_answer_phrasing` and `use_task_advice_pair_phrasing`) using provided OpenAI credentials. It aggregates the errors and total tests across trials, reporting a final summary of success or failure percentage.*


### test_teachability_accuracy (function, L159-L188)

> *Summary: This test verifies an agent's ability to learn new information by initiating a chat, providing a fact ("My favorite color is teal."), and then immediately testing if the agent recalls that specific piece of data in a subsequent, context-free conversation. It runs this process multiple times and asserts failure if the agent consistently fails to recall the taught information across all trials.*

