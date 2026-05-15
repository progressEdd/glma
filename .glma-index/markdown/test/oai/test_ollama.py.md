# test/oai/test_ollama.py

14 function(s): mock_response, ollama_client, ollama_client_maths_format, test_ollama_llm_config_entry, test_initialization, test_parsing_params, test_create_response, test_ollama_client_host_value, test_create_response_with_tool_call, test_manual_tool_calling_parsing and 4 more. 2 class(es): Step, MathReasoning.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Step | class |  |
| MathReasoning | class |  |
| mock_response | function |  |
| ollama_client | function |  |
| ollama_client_maths_format | function |  |
| test_ollama_llm_config_entry | function |  |
| test_initialization | function |  |
| test_parsing_params | function |  |
| test_create_response | function |  |
| test_ollama_client_host_value | function |  |
| test_create_response_with_tool_call | function |  |
| test_manual_tool_calling_parsing | function |  |
| test_oai_messages_to_ollama_messages | function |  |
| test_extract_json_response | function |  |
| test_extract_json_response_client | function |  |
| test_extract_json_response_params | function |  |

## Chunks

### Step (class, L19-L21)

> *Summary: Defines a data structure containing an explanation and the resulting output as strings. This model is used to encapsulate the results of a processing step within the system.*


### MathReasoning (class, L24-L26)

> *Summary: Defines a data structure containing a sequence of reasoning steps and the final calculated answer. It expects an input consisting of a list of `Step` objects and a string for the result.*


### mock_response (function, L31-L40)

> *Summary: Provides a factory function that returns a mock response class capable of simulating API responses with configurable fields like generated text, usage statistics, and model information. This allows for isolated testing of code interacting with an external AI service.*


### ollama_client (function, L44-L51)

> *Summary: Initializes and configures an `OllamaClient` instance, setting internal flags to enable native tool calls while disabling tools within the conversation context. This function returns the configured client object for subsequent use in testing or operations.*


### ollama_client_maths_format (function, L55-L62)

> *Summary: Initializes and configures an `OllamaClient` instance, specifically setting the response format to `MathReasoning`. It also sets internal flags to enable native tool calls while disabling tools within the conversation context.*


### test_ollama_llm_config_entry (function, L65-L89)

> *Summary: This test verifies that an `OllamaLLMConfigEntry` object correctly serializes its configuration parameters into a dictionary. It then asserts that wrapping this entry within an `LLMConfig` structure produces the expected list format for overall configuration.*


### test_initialization (function, L94-L96)

> *Summary: Verifies that the `OllamaClient` can be instantiated successfully even when no API key is provided. This tests the basic initialization path of the client object.*


### test_parsing_params (function, L101-L163)

> *Summary: This test verifies that a client correctly parses input parameters for an Ollama request, handling cases with all specified values, incorrect data types (which should default), and missing required fields like the model name. It asserts correct output structures and confirms exceptions are raised when essential parameters are omitted.*


### test_create_response (function, L169-L197)

> *Summary: This test verifies that a client correctly processes and returns data from an Ollama API call. It mocks the external service's response to assert that the resulting object contains the expected content, ID, model name, and token usage statistics.*


### test_ollama_client_host_value (function, L203-L226)

> *Summary: This test verifies that an `OllamaClient` is correctly initialized when creating a `ConversableAgent`. It asserts that the agent's internal client configuration accurately reflects the provided model name and host URL (`http://localhost:11434`).*


### test_create_response_with_tool_call (function, L232-L288)

> *Summary: This test verifies the system's ability to handle responses containing multiple tool calls from an LLM interaction. It mocks an Ollama client to simulate a response where the model suggests calling both a currency calculator and a weather function, then asserts that these functions are correctly present in the returned object.*


### test_manual_tool_calling_parsing (function, L293-L336)

> *Summary: Verifies the `response_to_tool_call` utility by testing its ability to correctly parse structured JSON arrays containing tool calls from various input strings. It asserts successful parsing for fully and partially embedded JSON, while also confirming it returns `None` when provided with invalid or plain text inputs.*


### test_oai_messages_to_ollama_messages (function, L341-L381)

> *Summary: This test verifies the `oai_messages_to_ollama_messages` conversion logic by asserting several transformations on an input list of OAI-style messages. It confirms that the "name" key is stripped from user messages, a trailing system message is converted to a user message, and a final "Please continue." message is appended if the last message is not user or system role.*


### test_extract_json_response (function, L386-L425)

> *Summary: Verifies that a method correctly parses structured JSON responses from an Ollama client into a `MathReasoning` object, while also asserting that it raises a `ValueError` when provided with malformed or non-JSON input. This test ensures robust handling of both valid and invalid response formats.*


### test_extract_json_response_client (function, L430-L466)

> *Summary: This test verifies a method's ability to parse structured math reasoning from an Ollama client response. It asserts correct parsing of valid JSON input, while also confirming that invalid or non-JSON inputs correctly raise a `ValueError`.*


### test_extract_json_response_params (function, L471-L491)

> *Summary: This test verifies that a set of input parameters, including a specific `MathReasoning` format, are correctly transformed by the client's parsing method. It asserts that the resulting parameter dictionary contains a JSON schema structure matching the expected model definition for the specified format.*

