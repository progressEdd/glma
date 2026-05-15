# autogen/agentchat/group/multi_agent_chat.py

6 function(s): initiate_group_chat, a_initiate_group_chat, run_group_chat, a_run_group_chat, run_group_chat_iter, a_run_group_chat_iter.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| initiate_group_chat | function |  |
| a_initiate_group_chat | function |  |
| run_group_chat | function |  |
| a_run_group_chat | function |  |
| run_group_chat_iter | function |  |
| a_run_group_chat_iter | function |  |

## Chunks

### initiate_group_chat (function, L44-L125)

> *Summary: This function sets up and executes a multi-agent group conversation based on a provided configuration pattern and initial messages. It prepares the agents, applies optional safety policies, runs the chat rounds, calculates the total usage cost across all participating agents, and returns the final chat history, updated context variables, and the last speaker.*


### a_initiate_group_chat (function, L129-L210)

> *Summary: Asynchronously sets up and runs a multi-agent group conversation based on a provided configuration pattern and initial messages. It prepares the necessary agents and context, applies optional safety policies, initiates or resumes the chat session, and returns the final chat history, updated context variables, and the last speaking agent.*


### run_group_chat (function, L214-L283)

> *Summary: Initiates a multi-agent conversation in a background thread using a specified interaction pattern and initial messages. It returns immediately with a `RunResponseProtocol` object that allows monitoring of the asynchronous chat execution, which can be configured with safeguards and masking LLM settings.*


### a_run_group_chat (function, L287-L355)

> *Summary: Executes a multi-agent conversation asynchronously based on a provided interaction pattern and initial messages. It returns an `AsyncRunResponseProtocol` immediately, allowing the caller to monitor events from the background execution of the chat process.*


### run_group_chat_iter (function, L359-L422)

> *Summary: This function initiates and manages a multi-agent group chat execution using an iterator pattern for stepped event processing. It accepts conversation parameters like interaction patterns, initial messages, and optional safety/masking configurations, returning an object that yields events as the chat progresses in a background thread.*


### a_run_group_chat_iter (function, L426-L492)

> *Summary: This function creates an asynchronous iterator that manages a multi-agent group chat simulation. It accepts conversation parameters like initial messages and interaction patterns, running the chat in a background thread to yield events as they occur until completion or interruption.*

