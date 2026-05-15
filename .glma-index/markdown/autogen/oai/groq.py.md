# autogen/oai/groq.py

2 function(s): oai_messages_to_groq_messages, calculate_groq_cost. 3 class(es): GroqEntryDict, GroqLLMConfigEntry, GroqClient. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GroqEntryDict | class |  |
| GroqLLMConfigEntry | class |  |
| GroqClient | class |  |
| oai_messages_to_groq_messages | function |  |
| calculate_groq_cost | function |  |

## Chunks

### GroqEntryDict (class, L52-L60)

> *Summary: This data structure holds configuration parameters specifically for interacting with the Groq LLM provider. It defines fields like penalties, seeding options, streaming control, and tool-calling behavior.*


### GroqLLMConfigEntry (class, L63-L74)

> *Summary: This configuration class defines parameters specific to using the Groq LLM provider, including penalties, seeding options, streaming control, and tool-calling behavior. It inherits from a base configuration and requires subclasses to implement client creation logic.*


### create_client (method, L73-L74, parent: GroqLLMConfigEntry)

> *Summary: This method currently raises a `NotImplementedError`, indicating that the concrete implementation for creating a Groq client has not yet been provided. It requires subclassing to define how to instantiate the necessary client object.*


### GroqClient (class, L77-L290)

> *Summary: This class manages interaction with the Groq API, requiring an API key upon initialization. It provides methods to parse input parameters for Groq, retrieve message content from responses, and calculate usage costs. The primary `create` method sends messages and configuration to Groq, returning a standardized OpenAI-compatible completion object, handling both streaming and non-streaming responses.*


### __init__ (method, L82-L99, parent: GroqClient)

> *Summary: Initializes the client by retrieving the necessary API key from either provided arguments or the `GROQ_API_KEY` environment variable, asserting its presence for operation. It also checks for and warns about unsupported parameters like `response_format`.*


### message_retrieval (method, L101-L107, parent: GroqClient)

> *Summary: Extracts and returns a list containing the `message` content from each choice within the provided API response object. This method ensures the output conforms to the expected structure of OpenAI's ChatCompletion Message objects, particularly for tool/function calling compatibility.*


### cost (method, L109-L110, parent: GroqClient)

> *Summary: Retrieves the monetary cost associated with a given API response object by accessing its `cost` attribute and returns it as a floating-point number.*


### get_usage (method, L113-L122, parent: GroqClient)

> *Summary: Extracts a usage summary dictionary from an API response object. It pulls token counts (prompt, completion, total), the associated cost, and the model name from the input `response`.*


### parse_params (method, L124-L165, parent: GroqClient)

> *Summary: This method takes a dictionary of configuration parameters and validates them against Groq API specifications. It ensures required fields like `model` are present and applies type/range checks to other settings such as `temperature`, `max_tokens`, and `stream`, returning a clean, validated parameter set for the API call.*


### create (method, L168-L290, parent: GroqClient)

> *Summary: This method interfaces with the Groq API to generate chat completions based on provided parameters. It converts input messages and configuration into Groq-specific formats, handles optional tool calling, executes the request (either streaming or non-streaming), and finally wraps the resulting content, usage statistics, and finish reason into a standardized `ChatCompletion` object.*


### oai_messages_to_groq_messages (function, L293-L304)

> *Summary: Transforms a list of messages from OpenAI format to Groq's required structure by deep-copying the input and removing any extraneous `"name"` fields from each message dictionary. The function accepts an OAI message list and returns the transformed Groq-compatible message list.*


### calculate_groq_cost (function, L307-L319)

> *Summary: Determines the monetary cost of a Groq API call based on token counts and the specified model. It uses predefined pricing structures to calculate separate costs for input and output tokens, returning the combined total or issuing a warning if the model is unsupported.*

