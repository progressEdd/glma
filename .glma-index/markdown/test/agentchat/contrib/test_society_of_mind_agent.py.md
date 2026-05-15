# test/agentchat/contrib/test_society_of_mind_agent.py

4 function(s): test_society_of_mind_agent, test_custom_preparer, test_function_calling, test_tool_use.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_society_of_mind_agent | function |  |
| test_custom_preparer | function |  |
| test_function_calling | function |  |
| test_tool_use | function |  |

## Chunks

### test_society_of_mind_agent (function, L17-L145)

> *Summary: Tests the interaction flow of a Society of Mind agent within an AutoGen group chat setup. It verifies message sequencing, termination conditions, and state persistence across multiple conversational rounds initiated by an external agent.*


### test_custom_preparer (function, L148-L204)

> *Summary: This test function sets up a group chat involving three agents and an external agent, then verifies the behavior of a custom message preparer. It asserts that after an initial external message, the conversation progresses through specific predefined messages before the preparer returns a success string.*


### test_function_calling (function, L208-L279)

> *Summary: This test sets up a multi-agent conversation involving an external agent, two conversational agents (Alice and Bob), and a terminating agent. It specifically tests if Alice, configured to use function calling, correctly invokes the `reverse_print` function registered by Bob when prompted by the external agent.*


### test_tool_use (function, L283-L333)

> *Summary: This test sets up a multi-agent conversation environment using `autogen` to verify tool usage capabilities. It initializes several agents, registers a string reversal function as a tool for one agent, and then triggers the system by having an external agent invoke that tool via another specialized agent.*

