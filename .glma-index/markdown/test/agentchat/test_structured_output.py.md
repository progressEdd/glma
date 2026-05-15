# test/agentchat/test_structured_output.py

4 function(s): test_structured_output, test_structured_output_global, mock_assistant, test_structured_output_formatting. 3 class(es): ResponseModel, Step, MathReasoning. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ResponseModel | class |  |
| test_structured_output | function |  |
| test_structured_output_global | function |  |
| Step | class |  |
| MathReasoning | class |  |
| mock_assistant | function |  |
| test_structured_output_formatting | function |  |

## Chunks

### ResponseModel (class, L35-L39)

> *Summary: Defines a data structure for structured responses, expecting inputs to contain a question string, short answer string, reasoning string, and a difficulty float. This model ensures consistent output formatting from an agent's response generation process.*


### test_structured_output (function, L55-L84)

> *Summary: This test verifies that an AI agent returns output conforming to a specified JSON structure. It configures an AutoGen chat session with a predefined response format and asserts that the final message content can be successfully validated against a `ResponseModel`.*


### test_structured_output_global (function, L94-L124)

> *Summary: This test verifies that an AI agent, configured with specific LLM settings and a required response format, returns output conforming to a predefined JSON structure after a brief chat exchange. It initiates a conversation using a user proxy and asserts the final message content can be successfully validated against a `ResponseModel`.*


### Step (class, L128-L130)

> *Summary: Defines a data structure containing an explanation and the resulting output as strings. This model is used to represent a single step in a process or sequence.*


### MathReasoning (class, L133-L141)

> *Summary: This model structure holds a sequence of reasoning steps and a final answer string. It provides a `format` method to serialize the structured data into a human-readable, multi-line string detailing each step's explanation and output before presenting the conclusion.*


### format (method, L137-L141, parent: MathReasoning)

> *Summary: Generates a formatted string summarizing the agent's execution by iterating through stored steps and appending the final answer. It takes internal `steps` (containing explanations and outputs) and `final_answer` as input to produce a structured, multi-line output string.*


### mock_assistant (function, L145-L178)

> *Summary: This function creates and configures a mock `AssistantAgent` by injecting predefined credentials that enforce a specific structured JSON response format (`MathReasoning`). It then mocks the underlying OpenAI client to ensure the agent always returns a fixed, structured completion containing steps and a final answer.*


### test_structured_output_formatting (function, L181-L197)

> *Summary: This test verifies that an `AssistantAgent` correctly formats its response when generating structured output during a chat session initiated by a `UserProxyAgent`. It asserts that the last message in the chat history matches a predefined, specific structured string format.*

