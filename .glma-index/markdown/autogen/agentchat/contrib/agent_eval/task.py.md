# autogen/agentchat/contrib/agent_eval/task.py

1 class(es): Task. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Task | class |  |

## Chunks

### Task (class, L12-L42)

> *Summary: Represents a specific task for agent evaluation by holding its name, description, and examples of both successful and failed responses. It provides methods to generate a system prompt from the task details or parse a `Task` object from a JSON string input.*


### get_sys_message (method, L20-L25, parent: Task)

> *Summary: Generates a system prompt string by combining the task's name, detailed description, and examples of both successful and failed responses. This output is intended to instruct an AI agent on how to perform a specific task.*


### parse_json_str (method, L28-L42, parent: Task)

> *Summary: Converts a JSON string input into a structured `Task` object by extracting the name, description, and response fields from the parsed data. It returns an instance of `Task` containing these extracted attributes.*

