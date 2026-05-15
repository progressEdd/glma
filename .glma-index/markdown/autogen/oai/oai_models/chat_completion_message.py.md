# autogen/oai/oai_models/chat_completion_message.py

4 class(es): AnnotationURLCitation, Annotation, FunctionCall, ChatCompletionMessage.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AnnotationURLCitation | class |  |
| Annotation | class |  |
| FunctionCall | class |  |
| ChatCompletionMessage | class |  |

## Chunks

### AnnotationURLCitation (class, L24-L35)

> *Summary: Represents a reference to an external web source within a message, storing its start and end indices, along with the resource's title and full URL. It is designed to structure citation metadata for use in AI model outputs.*


### Annotation (class, L38-L43)

> *Summary: Defines a data structure for representing a specific type of annotation, which must be `"url_citation"`. It requires an associated `AnnotationURLCitation` object to hold the necessary URL information.*


### FunctionCall (class, L46-L56)

> *Summary: Represents a request to execute a specific function with provided arguments. It holds the function's name and its parameters as a JSON string, requiring external validation due to potential model inaccuracies.*


### ChatCompletionMessage (class, L59-L97)

> *Summary: Represents a single message within a chat completion exchange, holding content (string, structured dict, or multimodal list), role, and optional metadata like refusals, annotations, audio data, or tool/function call instructions. It structures the input/output for conversational AI interactions.*

