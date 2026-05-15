# test/agentchat/test_event_streaming.py

12 function(s): test_single_agent_sync, test_single_agent_async, test_two_agents_sync, test_two_agents_async, test_group_chat_sync, test_group_chat_async, test_swarm_sync, test_swarm_async, test_sequential_sync, test_sequential_async and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_single_agent_sync | function |  |
| test_single_agent_async | function |  |
| test_two_agents_sync | function |  |
| test_two_agents_async | function |  |
| test_group_chat_sync | function |  |
| test_group_chat_async | function |  |
| test_swarm_sync | function |  |
| test_swarm_async | function |  |
| test_sequential_sync | function |  |
| test_sequential_async | function |  |
| test_run_group_chat_sync | function |  |
| test_run_group_chat_async | function |  |

## Chunks

### test_single_agent_sync (function, L21-L40)

> *Summary: This test verifies synchronous interaction with a single conversational agent configured to respond poetically. It sends an initial prompt and asserts that the resulting response contains a summary, two messages, and correctly identifies the agent as the last speaker.*


### test_single_agent_async (function, L45-L64)

> *Summary: This test verifies the asynchronous execution of a single conversational agent configured with a specific system prompt and LLM settings. It sends an initial message to the agent, consumes streaming events by responding with "exit," and then asserts that the resulting run contains a summary, two messages, and correctly identifies the last speaker as the agent.*


### test_two_agents_sync (function, L68-L97)

> *Summary: This test simulates a synchronous conversation between two specialized AI agents, Jack and Emma, who are comedians in a duo act. It verifies that the interaction completes successfully by asserting the final speaker is one of the participants, a summary exists, messages were exchanged, and cost information was recorded.*


### test_two_agents_async (function, L102-L135)

> *Summary: This asynchronous test simulates a two-agent comedy routine by initializing two specialized `ConversableAgent` instances with distinct roles and constraints. It executes a conversation starting with an initial prompt from Jack to Emma, then asserts that the resulting run produces a summary, contains messages, and correctly identifies the last speaker.*


### test_group_chat_sync (function, L139-L187)

> *Summary: This test sets up a multi-agent group chat involving a teacher, planner, and reviewer to collaboratively create lesson plans based on an initial prompt. It executes the conversation via a manager that terminates upon receiving "DONE!" and asserts that the resulting response contains a summary, messages, and a valid last speaker.*


### test_group_chat_async (function, L192-L240)

> *Summary: This asynchronous test sets up a group chat involving three specialized AI agents—a planner, a reviewer, and a teacher—managed by a central manager that terminates upon receiving "DONE!". It initiates a conversation with the teacher agent and asserts that the resulting interaction produces a summary, contains messages, and concludes with one of the defined speakers.*


### test_swarm_sync (function, L245-L294)

> *Summary: This test function sets up and executes a multi-agent swarm simulation involving a lesson planner, reviewer, and teacher agents using OpenAI credentials. It initiates a conversation about the solar system and asserts that the resulting response contains a summary, messages, and ends with one of the participating agents speaking.*


### test_swarm_async (function, L300-L350)

> *Summary: This asynchronous test sets up a multi-agent system where specialized AI agents (planner, reviewer, teacher) collaborate to develop a lesson plan based on an initial user prompt about the solar system. It executes this "swarm" process and asserts that the resulting output contains a summary, messages, and a final speaker from one of the participating agents.*


### test_sequential_sync (function, L355-L428)

> *Summary: This test executes a predefined sequence of tasks across three specialized AI agents—a financial assistant, a researcher, and a writer—orchestrated by a user proxy. It verifies that the multi-step process completes successfully, resulting in non-empty messages, a defined last speaker, a generated summary, and recorded costs for each interaction.*


### test_sequential_async (function, L434-L506)

> *Summary: This test executes a multi-stage workflow by sequentially running tasks across three specialized AI agents (Financial Assistant, Researcher, Writer). It initiates the process with initial financial queries, followed by research based on those results, and finally generates a blog post using all prior information, asserting successful completion and data integrity.*


### test_run_group_chat_sync (function, L510-L562)

> *Summary: This test sets up a multi-agent system with specialized roles (triage, tech, general) to process a user query. It executes the group chat simulation using `run_group_chat` and asserts that the resulting response contains expected data structures, message history, and all participating agents.*


### test_run_group_chat_async (function, L567-L619)

> *Summary: This test sets up a multi-agent conversation system with specialized roles (triage, tech, general) to process a user query asynchronously. It executes the group chat pattern and asserts that the resulting response contains expected messages, agent participation, and cost information.*

