# test/agentchat/test_anthropic_structured_outputs.py

10 function(s): config_list_sonnet_4_5_structured, test_two_agent_chat_native_structured_output, test_groupchat_structured_output, test_groupchat_defaultpattern_structured_output, test_structured_output_with_format_method, test_structured_output_error_handling, test_strict_tool_use, test_combined_json_output_and_strict_tools, test_tools_openai_format_with_structured_output, test_groupchat_autopattern_tools_with_structured_output. 4 class(es): Step, MathReasoning, AnalysisResult, AgentResponse. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Step | class |  |
| MathReasoning | class |  |
| AnalysisResult | class |  |
| AgentResponse | class |  |
| config_list_sonnet_4_5_structured | function |  |
| test_two_agent_chat_native_structured_output | function |  |
| test_groupchat_structured_output | function |  |
| test_groupchat_defaultpattern_structured_output | function |  |
| test_structured_output_with_format_method | function |  |
| test_structured_output_error_handling | function |  |
| test_strict_tool_use | function |  |
| test_combined_json_output_and_strict_tools | function |  |
| test_tools_openai_format_with_structured_output | function |  |
| test_groupchat_autopattern_tools_with_structured_output | function |  |

## Chunks

### Step (class, L35-L39)

> *Summary: Represents a single stage of mathematical reasoning, holding both an explanatory text and the resulting output. It is structured using Pydantic's `BaseModel` for data validation.*


### MathReasoning (class, L42-L53)

> *Summary: This model defines a structured output format for mathematical problem-solving, requiring a list of `Step` objects and a final answer string as input. It provides a `format` method to serialize this structure into a human-readable string detailing each step and the conclusion.*


### format (method, L48-L53, parent: MathReasoning)

> *Summary: Generates a formatted string representation of the agent's execution history and final result. It iterates over stored steps to build a detailed log, appending the conclusive answer at the end.*


### AnalysisResult (class, L56-L61)

> *Summary: Defines a structured data model to hold the results of an analysis. It requires inputs for a summary string, a list of key findings strings, and a recommendation string as outputs.*


### AgentResponse (class, L64-L70)

> *Summary: Defines a standardized structure for an agent's output, requiring the agent's name, response type, textual content, and a confidence score. This model serves as a generic container for structured responses from agents.*


### config_list_sonnet_4_5_structured (function, L75-L82)

> *Summary: This function takes a list of Anthropic credentials configurations and returns a new list where each configuration is modified to enforce structured output using `MathReasoning`. It iterates over the input list, copies each item, and injects the specific response format into the copy.*


### test_two_agent_chat_native_structured_output (function, L93-L129)

> *Summary: This test verifies a two-agent chat interaction where an assistant uses native structured output capabilities. It initiates a math problem exchange between a user proxy and an assistant, asserting that the final response content is a formatted string containing solution steps and the final answer, rather than raw JSON.*


### test_groupchat_structured_output (function, L140-L221)

> *Summary: This test verifies that a group chat involving multiple specialized agents can successfully generate structured outputs. It configures two agents to respond using specific schemas (`AnalysisResult` and `MathReasoning`) when initiated by a user proxy, asserting that at least one agent produces the expected structured data format during the conversation.*


### test_groupchat_defaultpattern_structured_output (function, L233-L306)

> *Summary: This test verifies that a group chat orchestrated by `DefaultPattern` correctly utilizes and produces structured outputs from specialized agents. It initializes two agents, one expecting an `AnalysisResult` structure and the other an output conforming to `MathReasoning`, then asserts that the resulting conversation history contains evidence of both expected structured formats.*


### test_structured_output_with_format_method (function, L317-L351)

> *Summary: This test verifies that a custom `format()` method is correctly invoked when an LLM agent generates structured output. It initiates a chat with a specific prompt and asserts that the final message content is a formatted string containing steps and the correct calculated result.*


### test_structured_output_error_handling (function, L362-L409)

> *Summary: This test verifies that the system handles errors gracefully when attempting to force a structured output using a complex Pydantic model schema. It initiates a chat with an assistant configured for this complex structure and asserts that no unhandled exceptions occur during execution or validation.*


### test_strict_tool_use (function, L420-L502)

> *Summary: Verifies that enabling `strict=True` on a defined function forces the LLM to generate arguments that strictly adhere to the provided JSON schema. It initiates a chat with an assistant configured for strict tool use and asserts that the resulting tool call contains correctly typed and constrained inputs.*


### test_combined_json_output_and_strict_tools (function, L508-L628)

> *Summary: This test verifies that an LLM agent can successfully utilize Anthropic's features by simultaneously enabling strict tool validation and structured JSON response formatting. It initiates a chat requiring calculation, asserting that the resulting conversation history contains evidence of either a validated tool call or a correctly parsed structured output matching a defined schema.*


### test_tools_openai_format_with_structured_output (function, L634-L781)

> *Summary: This test verifies that the OpenAI tool format (`{"type": "function", ...}`) correctly interfaces with Anthropic's structured outputs beta API, resolving a previous 400 error. It initiates a chat session using a defined calculator tool and asserts that the conversation successfully utilizes either the tool call or generates valid structured output without falling back to JSON mode.*


### test_groupchat_autopattern_tools_with_structured_output (function, L788-L974)

> *Summary: This test verifies that a multi-agent groupchat orchestrated by AutoPattern successfully integrates tools and structured outputs using Anthropic models. It initializes agents with specific output schemas and tool definitions, then executes a complex calculation request to confirm correct interaction without triggering API errors or falling back to JSON mode.*

