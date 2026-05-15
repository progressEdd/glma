# autogen/oai/oai_models/completion_usage.py

3 class(es): CompletionTokensDetails, PromptTokensDetails, CompletionUsage.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CompletionTokensDetails | class |  |
| PromptTokensDetails | class |  |
| CompletionUsage | class |  |

## Chunks

### CompletionTokensDetails (class, L15-L34)

> *Summary: This data structure holds detailed token counts related to model completions and predictions. It accepts optional integers representing accepted prediction tokens, audio input tokens, reasoning tokens, and rejected prediction tokens.*


### PromptTokensDetails (class, L37-L42)

> *Summary: This data structure holds token counts for an input prompt, specifically tracking audio and cached tokens. It serves as a container to pass these usage metrics around within the system.*


### CompletionUsage (class, L45-L59)

> *Summary: This model structure holds usage statistics for an AI request, capturing counts for generated completion tokens, input prompt tokens, and the overall total. It optionally includes detailed breakdowns for both the completion and the prompt token usage.*

