# autogen/oai/mistral.py

2 function(s): tool_def_to_mistral, calculate_mistral_cost. 3 class(es): MistralEntryDict, MistralLLMConfigEntry, MistralAIClient. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MistralEntryDict | class |  |
| MistralLLMConfigEntry | class |  |
| MistralAIClient | class |  |
| tool_def_to_mistral | function |  |
| calculate_mistral_cost | function |  |

## Chunks

### MistralEntryDict (class, L54-L61)

> *Summary: This data structure holds configuration parameters specifically for Mistral language models. It accepts settings like prompt safety, random seed, streaming preference, tool visibility rules, and the method for selecting tools.*


### MistralLLMConfigEntry (class, L64-L73)

> *Summary: This configuration class defines parameters specific to using the Mistral LLM, including settings for safety, randomness, streaming, and tool invocation behavior. It inherits from a base configuration and requires subclasses to implement client creation logic.*


### create_client (method, L72-L73, parent: MistralLLMConfigEntry)

> *Summary: This method currently raises a `NotImplementedError`, indicating that the logic for creating a Mistral LLM client has not yet been defined. It requires implementation to function as intended within the configuration entry.*


### MistralAIClient (class, L77-L263)

> *Summary: This class manages interaction with the Mistral AI API, requiring an API key upon initialization. It provides methods to parse input parameters into a format suitable for Mistral, execute chat completions by calling the underlying client, and convert the resulting Mistral response back into a standardized OAI-compatible structure.*


### __init__ (method, L82-L100, parent: MistralAIClient)

> *Summary: Initializes the client by retrieving an API key from either provided arguments or the `MISTRAL_API_KEY` environment variable, asserting its presence. It then instantiates the underlying Mistral client and issues a warning if a unsupported `response_format` is passed during setup.*


### message_retrieval (method, L102-L104, parent: MistralAIClient)

> *Summary: Extracts all message objects from a given `ChatCompletion` response object. It returns either a list of strings (the message content) or a list of `ChatCompletionMessage` objects, depending on the structure of the choices.*


### cost (method, L106-L107, parent: MistralAIClient)

> *Summary: Calculates the monetary cost of a given API response by directly accessing its `cost` attribute and returning it as a float.*


### parse_params (method, L110-L200, parent: MistralAIClient)

> *Summary: This method validates and transforms input parameters for the Mistral.AI API, ensuring required fields like `model` are present and applying defaults to optional settings such as `temperature` and `max_tokens`. It also converts standard message formats, including handling tool calls and system messages, into the specific structure required by Mistral, adding a continuation prompt if necessary.*


### create (method, L203-L251, parent: MistralAIClient)

> *Summary: Takes a dictionary of parameters and communicates with the Mistral AI API to generate a chat completion. It then transforms the raw Mistral response into an OpenAI-compatible `ChatCompletion` object, handling tool calls appropriately during conversion.*


### get_usage (method, L254-L263, parent: MistralAIClient)

> *Summary: Extracts token usage and cost details from a `ChatCompletion` object. It returns a dictionary containing the count of prompt tokens, completion tokens, total tokens, associated cost, and the model name.*


### tool_def_to_mistral (function, L267-L283)

> *Summary: Transforms a list of AG2 tool definition dictionaries into the specific format required by Mistral models. It iterates through the input definitions, extracting function name, description, and parameters to construct the corresponding Mistral tool structure.*


### calculate_mistral_cost (function, L286-L309)

> *Summary: Calculates the monetary cost of a Mistral API call based on input and output token counts and the specified `model_name`. It uses a predefined map to look up per-thousand token rates for various models, returning the total calculated cost or $0 if the model is unsupported.*

