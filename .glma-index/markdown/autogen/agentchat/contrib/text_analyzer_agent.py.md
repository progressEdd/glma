# autogen/agentchat/contrib/text_analyzer_agent.py

1 class(es): TextAnalyzerAgent. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TextAnalyzerAgent | class |  |

## Chunks

### TextAnalyzerAgent (class, L26-L97)

> *Summary: This deprecated agent analyzes text based on provided instructions by wrapping the input text and instructions into a specific prompt format. It takes messages containing the text to analyze and the analysis instructions as input, returning the LLM-generated analysis string as its output.*


### __init__ (method, L34-L65, parent: TextAnalyzerAgent)

> *Summary: Initializes a text analysis agent, issuing a deprecation warning and setting up its core behavior by registering an internal reply function for processing incoming messages. It accepts configuration parameters like a system message, human input mode, and LLM settings to define its operation.*


### _analyze_in_reply (method, L67-L84, parent: TextAnalyzerAgent)

> *Summary: This method processes two input messages—one containing text and another with instructions—to perform a textual analysis using an underlying LLM call. It returns a boolean indicating success along with the resulting analysis content or structure.*


### analyze_text (method, L86-L97, parent: TextAnalyzerAgent)

> *Summary: This method constructs a prompt by sandwiching input text between specified analysis instructions. It then sends this combined message to an OpenAI model and returns the resulting analysis string from the API response.*

