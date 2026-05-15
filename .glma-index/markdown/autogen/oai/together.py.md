# autogen/oai/together.py

2 function(s): oai_messages_to_together_messages, calculate_together_cost. 3 class(es): TogetherEntryDict, TogetherLLMConfigEntry, TogetherClient. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TogetherEntryDict | class |  |
| TogetherLLMConfigEntry | class |  |
| TogetherClient | class |  |
| oai_messages_to_together_messages | function |  |
| calculate_together_cost | function |  |

## Chunks

### TogetherEntryDict (class, L50-L62)

> *Summary: This structure defines configuration parameters specifically for the Together AI API. It holds settings like streaming preference, sampling controls (e.g., `top_k`, penalties), safety model selection, and tool usage configurations.*


### TogetherLLMConfigEntry (class, L65-L84)

> *Summary: This configuration class defines parameters for interacting with the Together AI API, including token limits, sampling controls (like `top_k` and penalties), and tool-use settings. It serves as a blueprint for configuring LLM calls specific to the "together" provider but requires subclasses to implement client creation.*


### create_client (method, L83-L84, parent: TogetherLLMConfigEntry)

> *Summary: This method requires subclasses to implement logic for instantiating a client object, as it currently raises an error indicating missing implementation. It serves as an abstract hook for creating the necessary external service connection.*


### TogetherClient (class, L87-L261)

> *Summary: This class manages interaction with the Together.AI API, handling authentication via an API key or environment variable. It provides methods to parse input parameters, retrieve usage statistics, and execute chat completions by converting internal message formats into those expected by the external service. The primary output is a standardized `ChatCompletion` object mirroring OpenAI's structure.*


### __init__ (method, L92-L108, parent: TogetherClient)

> *Summary: Initializes a client by prioritizing an explicit `api_key` from keyword arguments, falling back to the `TOGETHER_API_KEY` environment variable if necessary. It validates that an API key is present and issues a warning if unsupported parameters like `response_format` are provided.*


### message_retrieval (method, L110-L116, parent: TogetherClient)

> *Summary: Extracts and returns a list containing the `message` content from each choice within the provided response object. This method ensures compatibility by expecting or returning objects structured like OpenAI's ChatCompletion Message format.*


### cost (method, L118-L119, parent: TogetherClient)

> *Summary: Calculates the monetary cost of a given API response by directly accessing its `cost` attribute and returning it as a float.*


### get_usage (method, L122-L131, parent: TogetherClient)

> *Summary: Extracts a usage summary dictionary from a provided API response object. It returns key metrics including prompt tokens, completion tokens, total tokens, cost, and the model name.*


### parse_params (method, L133-L176, parent: TogetherClient)

> *Summary: This method takes a dictionary of configuration parameters and validates them against expected types, ranges, and defaults for the Together.AI API. It returns a cleaned and validated dictionary containing all necessary API settings, while also issuing warnings if incompatible options like streaming with tools are provided.*


### create (method, L179-L261, parent: TogetherClient)

> *Summary: This method sends a request to the Together.AI API using provided parameters, converting internal message formats and optionally including tools. It returns a standardized `ChatCompletion` object containing the model's response content, usage statistics, and finish reason, handling both streamed and non-streamed responses.*


### oai_messages_to_together_messages (function, L264-L275)

> *Summary: Transforms a list of messages from the OAI format to the Together.AI format by deep-copying the input. It specifically modifies any message with the role `"tool"` to have the role `"user"` before returning the converted list.*


### calculate_together_cost (function, L352-L387)

> *Summary: Determines the inference cost for a specified Together AI model based on input and output token counts. It looks up the appropriate cost per million tokens by matching the model's size against predefined tiers for either chat/language/code or mixture models.*

