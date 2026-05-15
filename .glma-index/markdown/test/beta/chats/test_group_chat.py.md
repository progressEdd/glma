# test/beta/chats/test_group_chat.py

2 function(s): test_round_robin_pattern, test_handoffs.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_round_robin_pattern | function |  |
| test_handoffs | function |  |

## Chunks

### test_round_robin_pattern (function, L17-L43)

> *Summary: This test verifies that a `RoundRobinPattern` correctly cycles through a list of agents during a group chat simulation. It initiates a chat with a specific message and asserts the resulting conversation history follows the expected sequential turn-taking order among all participating agents.*


### test_handoffs (function, L47-L76)

> *Summary: This test verifies the handoff mechanism within a group chat simulation. It sets up two agents and an initial agent, configuring them to pass control sequentially between each other during a multi-round conversation initiated with a starting message.*

