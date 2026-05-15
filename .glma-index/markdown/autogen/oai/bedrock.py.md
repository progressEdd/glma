# autogen/oai/bedrock.py

8 function(s): extract_system_messages, oai_messages_to_bedrock_messages, parse_content_parts, parse_image, format_tools, format_tool_calls, convert_stop_reason_to_finish_reason, calculate_cost. 3 class(es): BedrockEntryDict, BedrockLLMConfigEntry, BedrockClient. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BedrockEntryDict | class |  |
| BedrockLLMConfigEntry | class |  |
| BedrockClient | class |  |
| extract_system_messages | function |  |
| oai_messages_to_bedrock_messages | function |  |
| parse_content_parts | function |  |
| parse_image | function |  |
| format_tools | function |  |
| format_tool_calls | function |  |
| convert_stop_reason_to_finish_reason | function |  |
| calculate_cost | function |  |

## Chunks

### BedrockEntryDict (class, L55-L72)

> *Summary: This structure defines configuration parameters for interacting with Amazon Bedrock. It accepts AWS credentials and region details, along with various generation settings like `top_k`, `seed`, and operational modes such as `"standard"` or `"adaptive"`.*


### BedrockLLMConfigEntry (class, L75-L101)

> *Summary: This configuration class holds parameters specific to interacting with AWS Bedrock, including region, optional AWS credentials, and various generation settings like `top_k` and `mode`. It provides serialization for sensitive AWS secrets and requires subclasses to implement a method for creating the necessary client.*


### serialize_aws_secrets (method, L97-L98, parent: BedrockLLMConfigEntry)

> *Summary: Retrieves the raw secret value from a `SecretStr` object and returns it as a string. This method is used to expose the underlying sensitive data stored in the secret object.*


### create_client (method, L100-L101, parent: BedrockLLMConfigEntry)

> *Summary: This method requires subclasses to implement it, as it serves as a placeholder for creating the specific Bedrock LLM client instance based on configuration. It currently raises an error if not overridden.*


### BedrockClient (class, L105-L567)

> *Summary: This class manages interaction with Amazon Bedrock's Converse API, initializing itself with AWS credentials and configuration parameters like region and timeouts. It handles complex tasks such as parsing input parameters, constructing the necessary request payload (including support for custom tools and structured JSON output), executing the API call via `boto3`, and finally processing the response into a standardized completion object.*


### __init__ (method, L112-L168, parent: BedrockClient)

> *Summary: Configures an Amazon Bedrock client by accepting AWS credentials and configuration parameters like region, timeouts, and retry settings from arguments or environment variables. It initializes the `boto3` runtime client for interacting with the Bedrock service based on whether explicit credentials are provided.*


### _get_response_format_schema (method, L170-L194, parent: BedrockClient)

> *Summary: This method normalizes a provided response format, which can be a Pydantic model or a dictionary, into a standardized JSON schema. It ensures the resulting schema is an object type and guarantees the presence of `properties` and `required` keys for consistent structure.*


### _normalize_pydantic_schema_to_dict (method, L196-L270, parent: BedrockClient)

> *Summary: Converts a Pydantic model or its JSON schema into a flat dictionary format by recursively resolving all internal `$ref` pointers and removing the `$defs` section. It accepts either a `BaseModel` class or an existing schema dictionary as input, returning a simplified, reference-free schema dictionary.*


### _create_structured_output_tool (method, L272-L291, parent: BedrockClient)

> *Summary: This method transforms a desired response structure, provided as either a Pydantic model or a JSON schema dictionary, into a standardized tool definition for Amazon Bedrock. It first derives and normalizes the underlying schema before packaging it into a function-calling tool format.*


### _merge_tools_with_structured_output (method, L293-L307, parent: BedrockClient)

> *Summary: Combines a list of provided user tools with a specific structured output tool definition. It returns a dictionary formatted for Bedrock, containing all merged tools under the "tools" key.*


### _extract_structured_output_from_tool_call (method, L309-L326, parent: BedrockClient)

> *Summary: Parses a list of `ChatCompletionMessageToolCall` objects to find and extract the JSON arguments associated with a specific "__structured_output" function. It returns the resulting Python dictionary if found, or `None` otherwise, raising an error upon JSON decoding failure.*


### _validate_and_format_structured_output (method, L328-L361, parent: BedrockClient)

> *Summary: This method validates and formats input dictionary data based on a configured response format, which can be a JSON string or a Pydantic model. It returns the validated data either as a formatted string via a protocol implementation or as a JSON string.*


### message_retrieval (method, L363-L365, parent: BedrockClient)

> *Summary: Extracts a list of message objects from an API response structure by iterating over its `choices`. This method takes a response object as input and returns a list containing only the message content from each choice.*


### parse_custom_params (method, L367-L371, parent: BedrockClient)

> *Summary: Determines if the client supports system prompts by checking for the `supports_system_prompts` key within the input parameters dictionary, defaulting to `True`. This flag controls whether a separate system message parameter is used in API requests.*


### parse_params (method, L373-L461, parent: BedrockClient)

> *Summary: This method processes an input dictionary of parameters to separate them into two distinct sets: `base_params` and `additional_params`. It validates common inference settings like temperature and max tokens for the base set, while collecting model-specific or extra fields into the additional set before returning both dictionaries.*


### create (method, L463-L552, parent: BedrockClient)

> *Summary: Executes inference against Amazon Bedrock using provided parameters to generate a chat completion response. It processes input messages and optional tools/response formats, constructs the necessary API request, calls `bedrock_runtime.converse`, and then parses the resulting output into a structured `ChatCompletion` object.*


### cost (method, L554-L556, parent: BedrockClient)

> *Summary: Calculates the monetary expense associated with a `ChatCompletion` object by using the provided prompt tokens, completion tokens, and model name in an external cost calculation function. Returns the total calculated cost as a floating-point number.*


### get_usage (method, L559-L567, parent: BedrockClient)

> *Summary: Extracts token counts (prompt, completion, total) and associated cost and model name from a provided API response object. It returns these metrics as a dictionary for easy consumption.*


### extract_system_messages (function, L570-L590)

> *Summary: This function filters a list of messages to find and extract the content from any system-role messages. It returns a list containing the extracted text, handling both string and structured content formats for the system message.*


### oai_messages_to_bedrock_messages (function, L593-L722)

> *Summary: Transforms messages from an OAI format into AWS Bedrock's required structure, ensuring strict alternation between user and assistant roles by inserting placeholder continuation messages as necessary. It handles conversions for tool calls and tool results based on whether tools are enabled and if system prompts are supported.*


### parse_content_parts (function, L725-L753)

> *Summary: This function processes a message dictionary to extract and structure its content parts. It converts a string content into a text part or iterates over list contents, transforming text segments and image URLs into structured `text` or `image` objects respectively.*


### parse_image (function, L756-L781)

> *Summary: This function retrieves raw image data and its MIME type from a provided URL string. It first checks if the input is a base64-encoded data URI; otherwise, it fetches the image via HTTP request and returns the binary content along with the detected or assumed content type.*


### format_tools (function, L784-L841)

> *Summary: Transforms a list of tool definitions, specifically those of type "function," into a standardized dictionary format suitable for Bedrock. It iterates through the input tools, converts function parameters and their schemas into JSON schema properties, and returns a structure containing only the processed tools under the "tools" key.*


### format_tool_calls (function, L844-L861)

> *Summary: Transforms a list of Converse API response objects into a structured list of `ChatCompletionMessageToolCall` instances. It iterates through the input content, extracts specific "toolUse" data, and formats it into the AG2 standard for function calling.*


### convert_stop_reason_to_finish_reason (function, L864-L887)

> *Summary: Transforms a Bedrock-specific `stop_reason` string into a standardized OpenAI-like `finish_reason`. It maps various Bedrock reasons (e.g., "tool\_use", "max\_tokens") to canonical values like "tool\_calls" or "length".*


### calculate_cost (function, L902-L914)

> *Summary: Determines the monetary cost of an AI interaction based on token counts and a specified model ID. It takes input tokens, output tokens, and a model identifier as input, returning the total calculated cost in dollars or zero if the model pricing is unknown.*

