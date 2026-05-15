# test/tools/experimental/deep_research/test_deep_research.py

1 class(es): TestDeepResearchTool. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDeepResearchTool | class |  |

## Chunks

### TestDeepResearchTool (class, L21-L181)

> *Summary: This test suite verifies the functionality of `DeepResearchTool` by asserting its schema correctness and testing various methods like generating subquestions, answering a single question, splitting questions into subquestions for answering, and delegating research tasks. It uses mock credentials to simulate LLM interactions across different OpenAI models.*


### test__init__ (method, L22-L38, parent: TestDeepResearchTool)

> *Summary: This test verifies the initialization of a `DeepResearchTool` instance using provided credentials. It asserts that the resulting tool is correctly typed, has the expected name, and possesses a predefined function schema for delegating research tasks.*


### test_get_generate_subquestions (method, L40-L99, parent: TestDeepResearchTool)

> *Summary: This test verifies that a specific function call correctly configures an `AssistantAgent` with the necessary tool definition for generating subquestions. It asserts that the agent's LLM configuration includes a function schema matching the expected structure, which takes an original question and returns a list of derived subquestions.*


### test_answer_question (method, L103-L113, parent: TestDeepResearchTool)

> *Summary: This test verifies the `DeepResearchTool._answer_question` method by passing a specific question and LLM configuration to it. It asserts that the returned string starts with "Answer confirmed:" and contains either "wang" or "wu".*


### test_get_split_question_and_answer_subquestions (method, L116-L136, parent: TestDeepResearchTool)

> *Summary: This test verifies the functionality of splitting a main question into subquestions and subsequently answering them using an LLM tool. It calls the split function with configuration parameters and then executes it, asserting that the final result is a string starting with "Subquestions answered:" after mocking the answer-fetching mechanism.*


### test_delegate_research_task (method, L139-L181, parent: TestDeepResearchTool)

> *Summary: This test verifies the functionality of a research tool by mocking its subquestion splitting mechanism to return predefined answers for specific questions. It then executes the tool with multiple tasks, asserting that the returned string results are correctly formatted and contain expected keywords from the mocked responses.*

