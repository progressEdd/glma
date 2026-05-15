# test/beta/network/_helpers.py

1 function(s): wait_for_text_count. 3 class(es): _MockClock, ScriptedConfig, _ScriptedClient. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _MockClock | class |  |
| ScriptedConfig | class |  |
| _ScriptedClient | class |  |
| wait_for_text_count | function |  |

## Chunks

### _MockClock (class, L28-L41)

> *Summary: Provides a controllable time source initialized with an ISO timestamp. It returns the current time as an ISO string and allows advancing the internal clock by a specified number of seconds.*


### __init__ (method, L32-L35, parent: _MockClock)

> *Summary: Initializes the object by parsing a provided ISO-formatted string into a timezone-aware `datetime` object, defaulting to UTC if no timezone information is present in the input.*


### __call__ (method, L37-L38, parent: _MockClock)

> *Summary: When invoked, this method returns the current time formatted as an ISO string using an internal `_now` attribute. It acts as a callable interface to retrieve the timestamp.*


### advance (method, L40-L41, parent: _MockClock)

> *Summary: Increments the internal time reference by a specified duration. It takes a `float` representing seconds as input and updates the instance's current time attribute accordingly.*


### ScriptedConfig (class, L44-L76)

> *Summary: This configuration object manages a sequence of predefined string replies, allowing an agent to deterministically respond across multiple turns. It maintains an internal cursor that advances upon each request for a new reply, returning an empty string when all scripted responses have been exhausted.*


### __init__ (method, L58-L60, parent: ScriptedConfig)

> *Summary: Initializes an object to hold a sequence of string replies and sets an internal cursor to zero. It accepts a variable number of strings as input, storing them in the `_replies` list for later access.*


### copy (method, L62-L63, parent: ScriptedConfig)

> *Summary: Returns a reference to the current instance, effectively acting as an identity operation for configuration objects. This method allows for shallow copying or passing the object by reference within tests.*


### create (method, L65-L66, parent: ScriptedConfig)

> *Summary: Instantiates and returns a new `_ScriptedClient` object, passing the current instance as an argument. This method is used to generate a client representation from the existing context.*


### create_files_client (method, L68-L69, parent: ScriptedConfig)

> *Summary: This method explicitly raises a `NotImplementedError` because the current configuration object lacks an integrated Files API. It serves as a placeholder to prevent accidental use of file creation functionality in this context.*


### _next_reply (method, L71-L76, parent: ScriptedConfig)

> *Summary: Retrieves the next stored response from a sequence, advancing an internal cursor upon successful retrieval. Returns an empty string if all replies have already been consumed.*


### _ScriptedClient (class, L79-L92)

> *Summary: This client wraps an LLM interaction by immediately fetching the next reply from its configuration. It takes a sequence of messages and context, sends a single generated message to the context, and returns a response containing that sent message.*


### __init__ (method, L80-L81, parent: _ScriptedClient)

> *Summary: Initializes the object by storing a provided `ScriptedConfig` instance as an internal configuration attribute.*


### __call__ (method, L83-L92, parent: _ScriptedClient)

> *Summary: This asynchronous method sends a pre-determined text reply to the provided `context` using messages derived from its configuration. It returns a `ModelResponse` containing the sent message after successfully dispatching it.*


### wait_for_text_count (function, L95-L115)

> *Summary: This asynchronous function polls a channel's Write-Ahead Log (WAL) until the number of `EV_TEXT` events meets or exceeds an expected count, returning all collected envelopes upon success. If the target count is not reached within the specified timeout, it raises a `TimeoutError`.*

