# autogen/llm_clients/openai_completions_client.py

1 class(es): OpenAICompletionsClient. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OpenAICompletionsClient | class |  |

## Chunks

### OpenAICompletionsClient (class, L53-L632)

> *Summary: This client interfaces with the OpenAI Chat Completions API to provide rich responses that preserve advanced features like reasoning blocks and tool calls. It accepts request parameters (like model name, messages, and tools) and returns a `UnifiedResponse` object containing structured data, usage metrics, and calculated cost.*


### __init__ (method, L85-L126, parent: OpenAICompletionsClient)

> *Summary: Initializes an OpenAI API client instance using provided credentials and configuration parameters like base URL and timeout. It also stores a dictionary containing predefined token costs for various OpenAI models to facilitate cost tracking.*


### create (method, L128-L174, parent: OpenAICompletionsClient)

> *Summary: This method sends a completion request to the OpenAI API using provided parameters, handling specific logic for reasoning models and Pydantic response formats. It returns a `UnifiedResponse` object that preserves all rich features from the underlying API call.*


### _is_pydantic_model (method, L176-L193, parent: OpenAICompletionsClient)

> *Summary: Determines if a given object is a Pydantic `BaseModel` class rather than an instance. It achieves this by checking if the object is both a class and a subclass of `pydantic.BaseModel`, handling potential import errors gracefully.*


### _is_reasoning_model (method, L195-L207, parent: OpenAICompletionsClient)

> *Summary: Determines if a provided model string qualifies as a specific type of reasoning model by checking if it begins with "o1" or "o3". Returns `True` only if the input model is present and matches these prefixes.*


### _process_reasoning_model_params (method, L209-L283, parent: OpenAICompletionsClient)

> *Summary: Modifies request parameters for specific reasoning models by removing unsupported settings like `temperature` and blocking features such as tools or streaming if the model doesn't support them. It also handles token conversion from `max_tokens` to `max_completion_tokens` and adapts system messages for older model versions.*


### _transform_response (method, L285-L431, parent: OpenAICompletionsClient)

> *Summary: Transforms a raw OpenAI API response into a standardized `UnifiedResponse` structure. It processes various message components like text, reasoning blocks, tool calls, and parsed objects based on the input model and parsing flag, ensuring forward compatibility by capturing unknown fields as generic content.*


### create_v1_compatible (method, L433-L476, parent: OpenAICompletionsClient)

> *Summary: This method generates a response in an older, backward-compatible format by calling the primary completion function first. It transforms the rich output into a flattened dictionary structure, sacrificing advanced features like reasoning blocks and citations for compatibility with legacy codebases.*


### cost (method, L478-L508, parent: OpenAICompletionsClient)

> *Summary: Calculates the monetary cost of an API call based on token usage provided in a response object. It retrieves prompt and completion token counts, then applies model-specific or default per-token pricing to return the total cost in USD.*


### get_usage (method, L511-L529, parent: OpenAICompletionsClient)

> *Summary: Extracts token usage and cost metrics from a `UnifiedResponse` object. It returns a dictionary containing the prompt tokens, completion tokens, total tokens, associated cost, and the model name used in the request.*


### message_retrieval (method, L531-L594, parent: OpenAICompletionsClient)

> *Summary: Extracts messages from a `UnifiedResponse`, returning a list of strings for simple text responses or a list of dictionaries conforming to OpenAI's ChatCompletion format when tool calls or complex multimodal content is present. It processes each message in the response, conditionally formatting it based on its content type.*


### _convert_to_openai_content_array (method, L596-L632, parent: OpenAICompletionsClient)

> *Summary: Transforms a `UnifiedMessage` containing various content types (text, image, audio, video) into the specific list-of-dictionaries format required by OpenAI's API. It maps text and images directly while falling back to text representation for unsupported audio and video inputs.*

