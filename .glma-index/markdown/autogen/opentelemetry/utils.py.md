# autogen/opentelemetry/utils.py

9 function(s): message_to_otel, messages_to_otel, reply_to_otel_message, aggregate_usage, get_provider_name, get_model_name, get_provider_from_config_list, get_model_from_config_list, set_llm_request_params.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| message_to_otel | function |  |
| messages_to_otel | function |  |
| reply_to_otel_message | function |  |
| aggregate_usage | function |  |
| get_provider_name | function |  |
| get_model_name | function |  |
| get_provider_from_config_list | function |  |
| get_model_from_config_list | function |  |
| set_llm_request_params | function |  |

## Chunks

### message_to_otel (function, L14-L70)

> *Summary: Transforms a message dictionary from an AG2/OpenAI format into the OTEL GenAI semantic convention structure. It processes inputs based on the message's `role` (user, assistant, or tool) to correctly map text content, tool calls, and tool responses into the standardized `parts` list.*


### messages_to_otel (function, L73-L75)

> *Summary: Transforms a list of internal message dictionaries into the OpenTelemetry (OTEL) format by applying a per-message conversion. It takes a list of arbitrary message dicts as input and returns a new list containing the OTEL-formatted versions.*


### reply_to_otel_message (function, L78-L101)

> *Summary: Transforms an agent's response—which can be a string, dictionary, or `None`—into a list of OpenTelemetry message dictionaries. It handles simple text replies and structured responses containing content or tool calls by mapping them to the required OTEL format.*


### aggregate_usage (function, L104-L123)

> *Summary: Calculates the total prompt and completion token counts across several models provided in a dictionary structure. It returns a tuple containing a comma-separated list of all involved model names, the aggregated input tokens, and the aggregated output tokens, or `None` if no usage data is supplied.*


### get_provider_name (function, L143-L162)

> *Summary: This function extracts the OpenTelemetry-standard provider name from an agent's LLM configuration object. It inspects the agent for `llm_config` and then uses the `api_type` of the first configuration entry to return a standardized string or `None` if any required configuration is missing.*


### get_model_name (function, L165-L178)

> *Summary: Retrieves the model identifier from an agent's LLM configuration structure. It returns the string name of the configured model if present, otherwise it yields `None`.*


### get_provider_from_config_list (function, L181-L193)

> *Summary: This utility extracts the OpenTelemetry provider name from a list of configuration dictionaries. It defaults to `"openai"` if the input list is empty or if no `api_type` is found in the first element, otherwise it maps the detected type using a predefined dictionary.*


### get_model_from_config_list (function, L196-L204)

> *Summary: Retrieves the model name from the initial configuration dictionary within a provided list of configurations. It returns the string value associated with the "model" key or `None` if the list is empty or the key is missing in the first element.*


### set_llm_request_params (function, L207-L222)

> *Summary: This utility function attaches specific LLM generation parameters (like temperature or max tokens) to an OpenTelemetry span. It iterates through a predefined list of keys, setting the corresponding attribute on the provided span if the key exists and has a non-null value in the input configuration dictionary.*

