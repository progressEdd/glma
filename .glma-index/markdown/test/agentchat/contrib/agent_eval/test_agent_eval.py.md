# test/agentchat/contrib/agent_eval/test_agent_eval.py

4 function(s): remove_ground_truth, task, test_generate_criteria, test_quantify_criteria.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| remove_ground_truth | function |  |
| task | function |  |
| test_generate_criteria | function |  |
| test_quantify_criteria | function |  |

## Chunks

### remove_ground_truth (function, L20-L26)

> *Summary: This function processes a JSON string representing a test case, removing specific fields like `is_correct`, `correct_ans`, and `check_result`. It returns the modified test details as a string along with the value of the removed `is_correct` field.*


### task (function, L30-L41)

> *Summary: This function constructs a `Task` object for math problem solving by reading sample successful and failed responses from local files. It returns this configured task object, which defines the evaluation criteria for the system's performance on such problems.*


### test_generate_criteria (function, L45-L51)

> *Summary: This test verifies that the `generate_criteria` function successfully produces a non-empty list of criteria when provided with a specific task and Azure credentials. It asserts that each generated criterion contains both a description, name, and accepted values.*


### test_quantify_criteria (function, L56-L73)

> *Summary: This test verifies the `quantify_criteria` function by loading sample criteria and a test case. It passes these inputs along with Azure credentials to assert that the resulting quantification contains both actual success metrics and estimated performance data.*

