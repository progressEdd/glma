# autogen/oai/ollama.py

4 function(s): _format_json_response, response_to_tool_call, _object_to_tool_call, is_valid_tool_call_item. 3 class(es): OllamaEntryDict, OllamaLLMConfigEntry, OllamaClient. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OllamaEntryDict | class |  |
| OllamaLLMConfigEntry | class |  |
| OllamaClient | class |  |
| _format_json_response | function |  |
| response_to_tool_call | function |  |
| _object_to_tool_call | function |  |
| is_valid_tool_call_item | function |  |

## Chunks

### OllamaEntryDict (class, L47-L57)

> *Summary: This structure defines configuration parameters for an Ollama language model connection. It holds settings like the host URL, streaming preference, token limits (`num_predict`, `num_ctx`), and sampling controls (`top_k`, `repeat_penalty`).*


### OllamaLLMConfigEntry (class, L60-L77)

> *Summary: This configuration class defines parameters for interacting with an Ollama language model, including host URL, token limits (`num_predict`), context size (`num_ctx`), and sampling controls like `top_k`. It serves as a blueprint for setting up the connection details before client instantiation.*


### create_client (method, L76-L77, parent: OllamaLLMConfigEntry)

> *Summary: This method currently raises a `NotImplementedError`, indicating that the concrete implementation for creating an Ollama client has not yet been provided. It requires subclassing to define how to instantiate the necessary client object.*


### OllamaClient (class, L80-L536)

> *Summary: This class provides an interface to interact with the Ollama API, handling request parameter validation and message format conversion between its internal representation and Ollama's expected structure. It supports both native and manual tool calling workflows by injecting specific instructions into the conversation history before making calls via `create()`.*


### __init__ (method, L117-L120, parent: OllamaClient)

> *Summary: Initializes an Ollama client instance by optionally accepting a `response_format` to guide structured output generation. This attribute is stored internally for later use during API calls.*


### message_retrieval (method, L122-L128, parent: OllamaClient)

> *Summary: Extracts and returns a list containing the `message` content from each choice within the provided response object. This method ensures compatibility by expecting or returning objects structured like OpenAI's ChatCompletion Message format.*


### cost (method, L130-L131, parent: OllamaClient)

> *Summary: Retrieves the monetary cost associated with a given API response object. It directly returns the `cost` attribute from the input response.*


### get_usage (method, L134-L143, parent: OllamaClient)

> *Summary: Extracts a usage summary dictionary from an API response object by pulling token counts (prompt, completion, total), associated cost, and the model identifier. This function takes a structured `response` object as input and returns a standardized dictionary containing these metrics.*


### parse_params (method, L145-L226, parent: OllamaClient)

> *Summary: Validates and structures input parameters from a dictionary to conform with the Ollama API specification. It extracts required fields like `model`, applies defaults and type checks to optional settings such as `temperature` and `num_ctx`, and constructs the final parameter set, including handling for tool calls and response formats.*


### create (method, L229-L412, parent: OllamaClient)

> *Summary: This method processes a request dictionary to interact with an Ollama endpoint, handling both streaming and non-streaming responses. It manages tool calling logic—either natively via Ollama or manually through text instructions—and converts the resulting data into a standardized `ChatCompletion` object containing content, potential function calls, and token usage statistics.*


### oai_messages_to_ollama_messages (method, L414-L515, parent: OllamaClient)

> *Summary: Transforms a list of OAI-formatted messages into Ollama's required format, handling role adjustments and converting structured tool calls/results into plain text content for the LLM. It modifies system prompts to include function definitions and merges sequential user messages if necessary before ensuring the final message is a user or system type.*


### _convert_json_response (method, L517-L536, parent: OllamaClient)

> *Summary: Parses a string API response, returning it directly if no structured format is specified. Otherwise, it attempts to validate and return the parsed data against a provided Pydantic model, raising an error upon parsing failure.*


### _format_json_response (function, L539-L541)

> *Summary: If the input response adheres to `FormatterProtocol`, this function calls its `.format()` method to generate a structured string; otherwise, it returns the provided fallback answer.*


### response_to_tool_call (function, L545-L600)

> *Summary: Parses a string input to extract and deserialize potential JSON structures, specifically looking for list or object formats. It attempts standard JSON loading, falling back to repair mechanisms like wrapping/unwrapping or handling specific escape sequence errors before returning a structured tool call object if successful, otherwise returns `None`.*


### _object_to_tool_call (function, L603-L646)

> *Summary: Converts a provided object into a list of dictionaries representing valid tool calls. It accepts single dictionaries or lists, attempting to parse string representations within lists if necessary, and returns the structured list upon successful validation, otherwise returning `None`.*


### is_valid_tool_call_item (function, L649-L657)

> *Summary: Validates a dictionary representing a tool call by ensuring it contains a string `name` key and only includes optional `arguments`, rejecting any other keys. It returns `True` if the structure matches the expected format, otherwise `False`.*

