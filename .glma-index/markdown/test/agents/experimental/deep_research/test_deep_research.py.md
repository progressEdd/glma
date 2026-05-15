# test/agents/experimental/deep_research/test_deep_research.py

1 class(es): TestDeepResearchAgent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDeepResearchAgent | class |  |

## Chunks

### TestDeepResearchAgent (class, L20-L73)

> *Summary: This test suite verifies the initialization and end-to-end functionality of a `DeepResearchAgent`. It asserts that the agent is correctly configured with specific tools and then executes a research query, validating that the resulting summary contains expected keywords.*


### test__init__ (method, L21-L44, parent: TestDeepResearchAgent)

> *Summary: This test verifies the initialization of a `DeepResearchAgent` by instantiating it with mock credentials and asserting its type, name, and that its configuration correctly includes a specific tool definition for delegating research tasks. It confirms the agent's internal state matches the expected structure based on the provided inputs.*


### test_end2end (method, L48-L73, parent: TestDeepResearchAgent)

> *Summary: This test executes an end-to-end workflow using a `DeepResearchAgent` to answer a specific question about the AG2 framework founders. It asserts that the agent's final summary is a string starting with "Answer confirmed:" and contains either "wang" or "wu".*

