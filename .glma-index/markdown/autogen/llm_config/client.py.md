# autogen/llm_config/client.py

4 class(es): ModelClient, ModelClientResponseProtocol, Choice, Message. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ModelClient | class |  |

## Chunks

### ModelClient (class, L14-L59)

> *Summary: Defines a protocol for an LLM client that must implement methods to create responses, retrieve message content, and calculate costs. It requires the implementation to handle input parameters via `create` and return structured response objects conforming to a defined protocol.*


### ModelClientResponseProtocol (class, L32-L40, parent: ModelClient)

> *Summary: Defines a protocol for the expected structure of an LLM client's response. It mandates that the response contains a model identifier and a sequence of choices, each containing a message with content data.*


### Choice (class, L33-L37, parent: ModelClientResponseProtocol)

> *Summary: Defines a protocol for an object representing a choice, which must contain a `Message` attribute. This message can hold content as a string, dictionary, or list of dictionaries.*


### Message (class, L34-L35, parent: Choice)

> *Summary: Defines a protocol for message objects that must contain a `content` attribute. This content can be a string, dictionary, list of dictionaries, or `None`.*


### create (method, L42-L42, parent: ModelClient)

> *Summary: This method constructs a new model client instance using configuration parameters provided in the `params` dictionary. It returns an object conforming to the `ModelClientResponseProtocol`.*


### message_retrieval (method, L44-L52, parent: ModelClient)

> *Summary: Extracts either a list of strings or a list of structured `Choice.Message` objects from a provided model response. It returns the messages in a format compatible with downstream code, which currently expects OpenAI-like message structures for tool/function calling.*


### cost (method, L54-L54, parent: ModelClient)

> *Summary: Calculates the monetary cost associated with a given model response object. It accepts a `ModelClientResponseProtocol` as input and returns a floating-point number representing the cost.*


### get_usage (method, L57-L59, parent: ModelClient)

> *Summary: Extracts a dictionary containing the usage statistics from a provided model response object. It specifically uses predefined keys to summarize how much the underlying language model was utilized.*

