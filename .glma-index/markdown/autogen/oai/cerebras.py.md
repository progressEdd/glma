# autogen/oai/cerebras.py

2 function(s): oai_messages_to_cerebras_messages, calculate_cerebras_cost. 3 class(es): CerebrasEntryDict, CerebrasLLMConfigEntry, CerebrasClient. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CerebrasEntryDict | class |  |
| CerebrasLLMConfigEntry | class |  |
| CerebrasClient | class |  |
| oai_messages_to_cerebras_messages | function |  |
| calculate_cerebras_cost | function |  |

## Chunks

### CerebrasEntryDict (class, L51-L57)

> *Summary: This dictionary structure configures an LLM instance specifically for Cerebras, holding parameters like a random seed, streaming preference, tool visibility rules, and the required method for selecting tools. It inherits from `LLMConfigEntryDict` to maintain configuration consistency across different model types.*


### CerebrasLLMConfigEntry (class, L60-L72)

> *Summary: This configuration class defines parameters for interacting with a Cerebras LLM, including settings like temperature, seed, and tool usage behavior. It inherits from a base configuration and requires subclasses to implement client creation logic.*


### create_client (method, L71-L72, parent: CerebrasLLMConfigEntry)

> *Summary: This method explicitly raises a `NotImplementedError`, indicating that the concrete implementation for creating a Cerebras LLM client must be provided by subclasses. It serves as an abstract placeholder for client instantiation logic.*


### CerebrasClient (class, L75-L273)

> *Summary: This class provides an interface to interact with the Cerebras API for chat completions. It initializes by requiring an API key and offers methods to retrieve message content, calculate usage costs, and parse configuration parameters from input dictionaries. The primary `create` method handles both streaming and non-streaming requests, translating inputs into Cerebras format and returning a standardized OpenAI-compatible `ChatCompletion` object.*


### __init__ (method, L80-L95, parent: CerebrasClient)

> *Summary: Initializes the client by requiring an API key, either provided directly or retrieved from the `CEREBRAS_API_KEY` environment variable. It validates the presence of this key and issues a warning if unsupported response format arguments are passed during setup.*


### message_retrieval (method, L97-L103, parent: CerebrasClient)

> *Summary: Extracts and returns a list containing the `message` content from every choice within a given chat completion response object. This method ensures compatibility by returning objects structured like OpenAI's standard message format, especially when handling tool or function calls.*


### cost (method, L105-L107, parent: CerebrasClient)

> *Summary: Retrieves the associated monetary cost from a provided `ChatCompletion` object. It returns this value as a floating-point number, which was injected into the completion object during its creation.*


### get_usage (method, L110-L119, parent: CerebrasClient)

> *Summary: Extracts a dictionary summarizing the token usage and cost from a `ChatCompletion` object. It returns specific metrics including prompt tokens, completion tokens, total tokens, associated cost, and the model name used in the response.*


### parse_params (method, L121-L145, parent: CerebrasClient)

> *Summary: This method takes a dictionary of configuration parameters and validates them against expected types and ranges for the Cerebras API. It returns a cleaned and validated dictionary containing necessary settings like `model`, `max_tokens`, and `temperature`.*


### create (method, L148-L273, parent: CerebrasClient)

> *Summary: This method constructs and sends a chat completion request to the Cerebras API after transforming input parameters and messages from an internal format. It handles both streaming and non-streaming responses, extracting content, tool calls, and token usage before packaging everything into a standardized `ChatCompletion` object for output.*


### oai_messages_to_cerebras_messages (function, L276-L287)

> *Summary: Transforms a list of messages from an OAI format to Cerebras's required structure by deep-copying the input and removing any `"name"` field present in each message dictionary. The function accepts a list of dictionaries and returns a modified list of dictionaries adhering to the target format.*


### calculate_cerebras_cost (function, L290-L302)

> *Summary: Determines the monetary cost of an AI completion based on input and output token counts using Cerebras pricing structures. It accepts token counts and a model name, returning the calculated total cost in dollars or a warning if the model is unsupported.*

