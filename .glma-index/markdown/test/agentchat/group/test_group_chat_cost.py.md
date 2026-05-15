# test/agentchat/group/test_group_chat_cost.py

1 function(s): create_mock_client. 2 class(es): TestGroupChatCostTracking, TestTwoAgentVsGroupChatCostParity. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| create_mock_client | function |  |
| TestGroupChatCostTracking | class |  |
| TestTwoAgentVsGroupChatCostParity | class |  |

## Chunks

### create_mock_client (function, L21-L42)

> *Summary: Generates a mock LLM client object configured with specific usage statistics. It accepts the model name, total cost, and token counts for prompts and completions to populate both `total_usage_summary` and `actual_usage_summary`.*


### TestGroupChatCostTracking (class, L45-L187)

> *Summary: This test suite verifies that group chat mechanisms correctly aggregate the computational costs from all participating agents and the group manager. It ensures that usage summaries accurately reflect the combined token counts and monetary expenses across multiple agents, even when some lack direct LLM clients.*


### test_gather_usage_summary_includes_all_agents (method, L48-L72, parent: TestGroupChatCostTracking)

> *Summary: This test verifies that a function correctly aggregates usage and cost data from a list of mock agents, including those without an associated API client. It asserts the total calculated cost and token counts for specific models across all provided agents.*


### test_initiate_group_chat_cost_includes_all_agents (method, L74-L135, parent: TestGroupChatCostTracking)

> *Summary: This test verifies that the group chat cost calculation correctly aggregates usage from all participating agents when initiating a conversation. It sets up three mock agents with predefined usage and asserts that the final returned cost reflects the sum of all their individual costs (0.6 in this case).*


### test_initiate_group_chat_cost_with_manager_client (method, L137-L187, parent: TestGroupChatCostTracking)

> *Summary: This test verifies that the total LLM cost correctly aggregates the expenses from both an agent and a group manager when initiating a group chat. It mocks the chat initiation process to assert that the final reported cost equals the sum of the individual costs assigned to the agent and the manager.*


### TestTwoAgentVsGroupChatCostParity (class, L190-L253)

> *Summary: These tests verify that cost tracking remains consistent when comparing two-agent conversations against a group chat scenario. They assert that the total calculated cost and token counts match between both setups, ensuring parity regardless of whether agents interact pairwise or within a group structure.*


### test_two_agent_cost_tracking (method, L193-L219, parent: TestTwoAgentVsGroupChatCostParity)

> *Summary: This test verifies that a cost tracking mechanism correctly aggregates usage from two distinct agents during a simulated chat interaction. It asserts that the total calculated cost and token counts accurately reflect the combined inputs and outputs of both mocked agents.*


### test_group_chat_cost_tracking_parity (method, L221-L253, parent: TestTwoAgentVsGroupChatCostParity)

> *Summary: This test verifies that the cost tracking for a group chat remains consistent when including an agent without an LLM client (the manager). It simulates interactions between two agents and a non-contributing manager to assert specific total costs and token counts from the usage summary.*

