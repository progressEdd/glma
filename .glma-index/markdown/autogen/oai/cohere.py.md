# autogen/oai/cohere.py

4 function(s): _format_json_response, extract_to_cohere_tool_results, calculate_cohere_cost, clean_return_response_format. 5 class(es): CohereEntryDict, CohereLLMConfigEntry, CohereClient, CohereError, CohereRateLimitError. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CohereEntryDict | class |  |
| CohereLLMConfigEntry | class |  |
| CohereClient | class |  |
| _format_json_response | function |  |
| extract_to_cohere_tool_results | function |  |
| calculate_cohere_cost | function |  |
| clean_return_response_format | function |  |
| CohereError | class |  |
| CohereRateLimitError | class |  |

## Chunks

### CohereEntryDict (class, L70-L80)

> *Summary: This structure defines configuration parameters for interacting with the Cohere API. It holds settings such as model-specific constants, penalty values, streaming preferences, and tool usage constraints.*


### CohereLLMConfigEntry (class, L83-L96)

> *Summary: This configuration class defines parameters for interacting with the Cohere API, including settings like temperature control (via penalties), tool usage constraints, and streaming options. It serves as a blueprint for configuring LLM calls specific to Cohere but requires subclasses to implement client creation logic.*


### create_client (method, L95-L96, parent: CohereLLMConfigEntry)

> *Summary: This method requires subclasses to implement logic for instantiating a Cohere client object. It currently raises an error, indicating that the concrete implementation must be provided by derived classes.*


### CohereClient (class, L99-L435)

> *Summary: This class manages interaction with the Cohere API, handling authentication via an API key. It provides methods to retrieve message content, calculate usage costs, and crucially, parses input parameters—including complex structured output definitions from Pydantic models—before executing a chat completion request. The primary function simulates OpenAI's `ChatCompletion` structure by wrapping the raw Cohere response, supporting both streaming and non-streaming calls with integrated tool/function calling logic.*


### __init__ (method, L104-L120, parent: CohereClient)

> *Summary: Initializes a client by retrieving the API key either from provided keyword arguments or the `COHERE_API_KEY` environment variable. It asserts that an API key is present and optionally stores a response format model for structured output handling.*


### message_retrieval (method, L122-L128, parent: CohereClient)

> *Summary: Extracts and returns a list containing the message objects from each choice within the provided API response. This method ensures the output conforms to the structure expected by downstream components, particularly for tool or function calling scenarios.*


### cost (method, L130-L131, parent: CohereClient)

> *Summary: Retrieves the monetary cost associated with an API response by accessing the `cost` attribute of the provided response object. This method returns a floating-point number representing the usage expense.*


### get_usage (method, L134-L143, parent: CohereClient)

> *Summary: Extracts a structured dictionary containing token counts (prompt, completion, total), cost, and model name from an API response object. It specifically pulls usage metrics directly from the provided `response` input.*


### parse_params (method, L145-L240, parent: CohereClient)

> *Summary: This method processes an input dictionary of parameters to generate a validated set suitable for the Cohere API. It enforces required fields like `model`, validates numerical ranges and types for settings such as `temperature` and `max_tokens`, and specifically handles complex Pydantic models in `response_format` by converting them into a structured JSON schema.*


### create (method, L243-L414, parent: CohereClient)

> *Summary: This method translates an input parameter dictionary into a Cohere API request, handling message formatting and tool call structures. It executes the request either synchronously or as a stream, returning a standardized `ChatCompletion` object containing the final answer, token usage, and any generated tool calls.*


### _convert_json_response (method, L416-L435, parent: CohereClient)

> *Summary: Parses a string API response, attempting to validate it against a predefined Pydantic schema if one is configured. It returns the validated object or raises an error if parsing or validation fails.*


### _format_json_response (function, L438-L442)

> *Summary: This helper function formats a received response into a string; it calls the `format()` method on the response object if it adheres to `FormatterProtocol`, otherwise, it uses another utility to format the original answer.*


### extract_to_cohere_tool_results (function, L445-L458)

> *Summary: This function constructs a list of `ToolResult` objects by matching a specific `tool_call_id` within a collection of tool calls. It takes the ID, the content output, and all available tool calls as input to return structured results containing the original call details and the provided output value.*


### calculate_cohere_cost (function, L461-L473)

> *Summary: Determines the monetary cost of a Cohere API call based on token counts and the specified model. It calculates the sum of input and output costs using predefined pricing tiers, issuing a warning if the model is unsupported.*


### clean_return_response_format (function, L476-L482)

> *Summary: This function takes a raw response string, parses it as JSON to correctly handle any escaped characters, and then returns the data serialized back into a compact JSON string format. It effectively cleans up the input by ensuring proper JSON serialization.*


### CohereError (class, L485-L488)

> *Summary: This custom exception serves as the base class for all specific errors originating from interactions with the Cohere API. It inherits directly from Python's built-in `Exception` to allow for structured error handling within the application.*


### CohereRateLimitError (class, L491-L494)

> *Summary: This exception signals that the API usage has hit a predefined request limit. It inherits from `CohereError` and is raised specifically when exceeding the allowed call frequency for the service.*

