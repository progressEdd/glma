# autogen/oai/gemini.py

3 function(s): get_image_data, _format_json_response, calculate_gemini_cost. 3 class(es): GeminiEntryDict, GeminiLLMConfigEntry, GeminiClient. 26 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GeminiEntryDict | class |  |
| GeminiLLMConfigEntry | class |  |
| GeminiClient | class |  |
| get_image_data | function |  |
| _format_json_response | function |  |
| calculate_gemini_cost | function |  |

## Chunks

### GeminiEntryDict (class, L108-L123)

> *Summary: This structure defines configuration parameters for interacting with Gemini models, supporting both AI Studio and Vertex AI endpoints. It accepts various settings like project ID, credentials, streaming preference, safety configurations, and tool definitions to control the LLM interaction.*


### GeminiLLMConfigEntry (class, L126-L155)

> *Summary: This configuration class defines parameters for interacting with Gemini models, supporting both AI Studio and Vertex AI endpoints. It accepts various settings like credentials, safety configurations, pricing tiers, and thought-generation controls to customize the LLM interaction.*


### create_client (method, L154-L155, parent: GeminiLLMConfigEntry)

> *Summary: This method requires subclasses to implement it, as it currently raises a `NotImplementedError`. Its purpose is to instantiate and return a client object for the Gemini LLM configuration.*


### GeminiClient (class, L159-L1066)

> *Summary: This class manages interactions with the Google Gemini API, supporting both direct API key usage and VertexAI integration based on initialization parameters. It handles complex tasks like converting OpenAI-style messages to Gemini format, managing structured JSON output validation, and translating tool definitions for different backend APIs. The primary method, `create`, executes the chat completion request, returning a standardized `ChatCompletion` object regardless of whether streaming or non-streaming was requested.*


### _initialize_vertexai (method, L176-L191, parent: GeminiClient)

> *Summary: Configures the Vertex AI SDK by setting environment variables or passing specific parameters like project ID, location, and credentials. It initializes the `vertexai` library based on the provided configuration dictionary.*


### __init__ (method, L193-L229, parent: GeminiClient)

> *Summary: Initializes the client by prioritizing an explicit `api_key`, falling back to the `GOOGLE_GEMINI_API_KEY` environment variable, or defaulting to Google Cloud authentication (VertexAI) if no key is provided. It configures internal state based on whether an API key or VertexAI credentials are used, and stores parameters like response format and tool call mappings.*


### message_retrieval (method, L231-L237, parent: GeminiClient)

> *Summary: Extracts and returns a list of `ChatCompletionMessage` objects from the provided `ChatCompletion` response. This method specifically iterates over the choices within the response to gather these message objects.*


### cost (method, L239-L240, parent: GeminiClient)

> *Summary: Retrieves the monetary cost associated with a given `ChatCompletion` object. It directly returns the `cost` attribute from the input response.*


### get_usage (method, L243-L252, parent: GeminiClient)

> *Summary: Extracts a dictionary containing token counts (prompt, completion, total), cost, and model name from a `ChatCompletion` object's usage data. This provides a summary of the resource consumption associated with the API response.*


### create (method, L254-L384, parent: GeminiClient)

> *Summary: This method generates a chat completion by configuring and calling the Gemini API (either via Vertex AI or standard API key). It handles various inputs like messages, streaming preferences, tool definitions, and response schema for structured output before processing the resulting response.*


### _extract_parts_from_response (method, L386-L421, parent: GeminiClient)

> *Summary: Processes a raw API response object (either `GenerateContentResponse` or `VertexAIGenerationResponse`) to extract the content parts and determine if an error occurred. It validates candidate counts and specifically checks for recitation or empty content reasons before returning the list of parts and any associated finish reason string.*


### _process_parts (method, L423-L481, parent: GeminiClient)

> *Summary: This method iterates over response parts to extract textual content and function calls from a list of parts. It accumulates the extracted text into a string, populates an external tool call list with structured function call objects (including thought signatures), and returns the aggregated text, the list of tool calls, and a history of previous function calls.*


### _build_chat_completion (method, L483-L532, parent: GeminiClient)

> *Summary: Constructs a `ChatCompletion` object from accumulated response data, tool call information, and token counts. It processes the answer string for JSON formatting if configured and determines the final finish reason based on whether tool calls were present or an error occurred.*


### _process_non_streaming_response (method, L534-L548, parent: GeminiClient)

> *Summary: This method transforms a complete, non-streaming API response into a structured `ChatCompletion` object. It extracts content parts and token usage from the input response to construct and return the final completion object.*


### _process_streaming_response (method, L550-L587, parent: GeminiClient)

> *Summary: Iterates over a streaming response to accumulate text and extract metadata from chunks. It processes each chunk to build up the final `ChatCompletion` object, tracking tokens and any function calls encountered during the stream.*


### _extract_system_instruction (method, L589-L602, parent: GeminiClient)

> *Summary: This method retrieves the system instruction from a list of message dictionaries by checking the first element's role. It handles both string and list-based content formats within that initial "system" message to return the extracted text or `None`.*


### _oai_content_to_gemini_content (method, L604-L716, parent: GeminiClient)

> *Summary: This method transforms an input dictionary representing a message from the AG2 format into a list of parts suitable for the Gemini API. It handles various message types, including text, tool calls (both requests and responses), and multimodal content like images, adjusting output based on whether Vertex AI is being used.*


### _concat_parts (method, L718-L745, parent: GeminiClient)

> *Summary: This method merges adjacent parts in a list if both contain text, concatenating their string content into a single part. It processes the input list of `Part` objects and returns a new list with consolidated parts, ensuring no resulting part has empty text content.*


### _oai_messages_to_gemini_messages (method, L747-L840, parent: GeminiClient)

> *Summary: Transforms a list of OAI-formatted messages into Gemini's `Content` structure, handling text, tool calls, and images. It enforces specific ordering constraints for the resulting sequence by prepending or appending dummy "user" messages if the first or last roles are not user-initiated.*


### _convert_json_response (method, L842-L862, parent: GeminiClient)

> *Summary: Parses a string API response, attempting to extract and validate structured data. If a Pydantic model is configured, it validates the parsed JSON against that schema; otherwise, it returns the raw dictionary if parsing succeeds.*


### _convert_type_null_to_nullable (method, L865-L876, parent: GeminiClient)

> *Summary: Recursively traverses a JSON schema structure to replace any instance of `{"type": "null"}` with `{"nullable": True}`. It handles both dictionary and list structures within the input schema, returning the modified schema object.*


### _check_if_prebuilt_google_search_tool_exists (method, L879-L892, parent: GeminiClient)

> *Summary: Determines if a specific "prebuilt\_google\_search" function is present within a provided list of tools. If found, it returns `True` but raises an error if more than one tool is in the list, enforcing exclusive use for that search capability.*


### _unwrap_references (method, L895-L906, parent: GeminiClient)

> *Summary: This method processes a dictionary of function parameters, specifically unwrapping JSON schema references found within the `properties`. It replaces `$defs` structures with their resolved definitions before returning the modified parameter dictionary.*


### _tools_to_gemini_tools (method, L908-L932, parent: GeminiClient)

> *Summary: Transforms a list of generic tool definitions into Gemini-specific `Tool` objects, adapting the structure based on whether Vertex AI is being used. It handles type conversions and reference unwrapping when operating within the Vertex AI environment.*


### _create_gemini_function_declaration (method, L935-L944, parent: GeminiClient)

> *Summary: Constructs a `FunctionDeclaration` object from a provided tool dictionary. It populates the declaration with the function's name and description, optionally including parameters if they exist in the input structure.*


### _create_gemini_function_declaration_schema (method, L947-L1004, parent: GeminiClient)

> *Summary: Transforms a JSON dictionary, potentially containing `$ref`s, into a structured `Schema` object suitable for Gemini function declarations. It recursively processes types like objects and arrays to build the schema hierarchy, handling basic type mappings and metadata like descriptions and required fields.*


### _create_gemini_function_parameters (method, L1007-L1031, parent: GeminiClient)

> *Summary: This method recursively transforms a dictionary representing function parameters into the specific format required by Gemini. It handles type casing, removes extraneous attributes like "title" and "default," and processes nested structures within properties and items.*


### _to_vertexai_safety_settings (method, L1034-L1058, parent: GeminiClient)

> *Summary: Transforms a list of generic safety settings dictionaries into `VertexAISafetySetting` objects if the input is not already in the expected format. It validates that the categories and thresholds provided match known VertexAI enumerations, logging errors for invalid entries.*


### _to_json_or_str (method, L1061-L1066, parent: GeminiClient)

> *Summary: Attempts to parse an input string as JSON; if successful, it returns the resulting dictionary or object; otherwise, it returns the original string unchanged.*


### get_image_data (function, L1070-L1085)

> *Summary: Retrieves image data from a file path, URL, or base64 string input. It returns the raw binary content or a UTF-8 encoded Base64 string based on the `use_b64` flag.*


### _format_json_response (function, L1088-L1090)

> *Summary: If the received response implements a `FormatterProtocol`, this function calls its `.format()` method to generate a structured string; otherwise, it returns the provided fallback answer directly.*


### calculate_gemini_cost (function, L1093-L1135)

> *Summary: Calculates the estimated monetary cost of using a Gemini model based on input and output token counts and the specified model name. It returns a `float` representing the total cost in millions of dollars, applying different pricing tiers depending on the model version and whether the input tokens exceed 200k.*

