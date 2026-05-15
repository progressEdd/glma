# autogen/agentchat/group/llm_condition.py

3 class(es): LLMCondition, StringLLMCondition, ContextStrLLMCondition. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LLMCondition | class |  |
| StringLLMCondition | class |  |
| ContextStrLLMCondition | class |  |

## Chunks

### LLMCondition (class, L18-L31)

> *Summary: Defines a protocol for conditions that require an LLM evaluation. It mandates a `get_prompt` method which accepts an agent and conversation history, returning the specific prompt string for the LLM to process.*


### get_prompt (method, L21-L31, parent: LLMCondition)

> *Summary: This method is intended to generate a string prompt for an LLM based on a specific agent and the existing message history. It currently raises `NotImplementedError`, requiring derived classes to provide the actual implementation logic.*


### StringLLMCondition (class, L34-L61)

> *Summary: This class implements a simple LLM evaluation condition by holding and returning a fixed string prompt. It accepts a `prompt` string during initialization and provides this exact string when queried, ignoring the agent or message history provided at runtime.*


### __init__ (method, L42-L49, parent: StringLLMCondition)

> *Summary: Initializes an object by accepting a required static prompt string and optional keyword arguments for its parent class. This sets up the core evaluation context using the provided prompt.*


### get_prompt (method, L51-L61, parent: StringLLMCondition)

> *Summary: Retrieves a predefined, static prompt string from the instance's configuration. It accepts an agent and message history as input but ignores them to return only the stored prompt text.*


### ContextStrLLMCondition (class, L64-L93)

> *Summary: This class evaluates a condition based on a string template containing context variable placeholders. It takes a `ContextStr` object and an agent, then substitutes the agent's context variables into the string to produce the final prompt for evaluation.*


### __init__ (method, L73-L80, parent: ContextStrLLMCondition)

> *Summary: Initializes an instance by accepting a `ContextStr` object containing variable placeholders and optional additional keyword arguments. It passes these inputs directly to its parent class constructor.*


### get_prompt (method, L82-L93, parent: ContextStrLLMCondition)

> *Summary: Retrieves a formatted string by substituting placeholders in a predefined template using the context variables from a specified agent. It returns the resulting prompt or an empty string if formatting fails.*

