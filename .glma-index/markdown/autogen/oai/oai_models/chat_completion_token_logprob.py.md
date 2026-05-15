# autogen/oai/oai_models/chat_completion_token_logprob.py

2 class(es): TopLogprob, ChatCompletionTokenLogprob.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TopLogprob | class |  |
| ChatCompletionTokenLogprob | class |  |

## Chunks

### TopLogprob (class, L15-L33)

> *Summary: Represents a single token's information from a model output, containing the token string, optional UTF-8 byte representation, and its associated log probability. The `logprob` field holds the actual probability if the token is highly likely, or a sentinel value of `-9999.0` otherwise.*


### ChatCompletionTokenLogprob (class, L36-L62)

> *Summary: Represents a single token's information from a chat completion response, containing the token string, optional UTF-8 byte representation, and its log probability. It also includes a list detailing the most likely tokens and their associated probabilities at that position.*

