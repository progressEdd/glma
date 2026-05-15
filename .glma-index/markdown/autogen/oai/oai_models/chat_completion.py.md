# autogen/oai/oai_models/chat_completion.py

4 class(es): ChoiceLogprobs, Choice, ChatCompletion, ChatCompletionExtended.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ChoiceLogprobs | class |  |
| Choice | class |  |
| ChatCompletion | class |  |
| ChatCompletionExtended | class |  |

## Chunks

### ChoiceLogprobs (class, L20-L25)

> *Summary: Represents the token-level probabilities for both accepted and refused content within a chat completion response. It accepts optional lists containing `ChatCompletionTokenLogprob` objects for tracking these values.*


### Choice (class, L28-L46)

> *Summary: Represents a single response option from a model's generation, containing metadata like the reason it stopped (`finish_reason`), its position in a list (`index`), optional log probability data, and the resulting message content. It structures the output of a chat completion request into discrete choices.*


### ChatCompletion (class, L49-L79)

> *Summary: Represents a chat completion response, containing metadata like an ID, creation timestamp, and the model used. It structures the output with a list of choices, usage statistics, and optional service tier or system fingerprint information.*


### ChatCompletionExtended (class, L82-L86)

> *Summary: Extends the base `ChatCompletion` model by adding optional fields for message retrieval, configuration identification, result filtering, and cost tracking. This allows for richer metadata and custom processing around chat completion requests.*

