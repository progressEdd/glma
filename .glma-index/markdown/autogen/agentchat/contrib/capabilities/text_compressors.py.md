# autogen/agentchat/contrib/capabilities/text_compressors.py

2 class(es): TextCompressor, LLMLingua. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TextCompressor | class |  |
| LLMLingua | class |  |

## Chunks

### TextCompressor (class, L16-L24)

> *Summary: Defines a contract for any object capable of compressing text strings to optimize agent communication. It requires an implementation of `compress_text` that accepts input text and returns a dictionary detailing the compressed content, original token count, and resulting token count.*


### compress_text (method, L19-L24, parent: TextCompressor)

> *Summary: Accepts a string and optional parameters to perform text compression, returning a dictionary that includes the compressed content, original token count, and resulting token count. This allows for tracking the efficiency of the compression process.*


### LLMLingua (class, L28-L66)

> *Summary: This class wraps a `PromptCompressor` to efficiently reduce the token count of input text. It accepts configuration parameters during initialization and exposes a `compress_text` method that takes a string and returns a dictionary containing the compressed result, using either standard or structured compression based on setup.*


### __init__ (method, L35-L63, parent: LLMLingua)

> *Summary: Initializes a compression utility by instantiating a `PromptCompressor` with specified model and device settings. It then sets an internal method pointer to either the standard or structured prompt compression function based on the provided boolean flag.*


### compress_text (method, L65-L66, parent: LLMLingua)

> *Summary: This method takes a string of text and optional parameters to pass them to an underlying compression mechanism. It returns a dictionary containing the compressed output.*

