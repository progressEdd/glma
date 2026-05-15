# autogen/beta/middleware/builtin/token_limiter.py

2 class(es): TokenLimiter, _TokenLimiter. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TokenLimiter | class |  |
| _TokenLimiter | class |  |

## Chunks

### TokenLimiter (class, L12-L27)

> *Summary: This middleware factory creates a token limiter that truncates message history to stay within a specified character budget. It accepts `max_tokens` and an optional `chars_per_token` factor to calculate the maximum allowed characters before returning the actual limiting middleware instance.*


### __init__ (method, L19-L24, parent: TokenLimiter)

> *Summary: Initializes a token limiter by setting the maximum allowed character count based on provided `max_tokens` and `chars_per_token`. It validates that both input parameters are positive integers to prevent invalid configurations.*


### __call__ (method, L26-L27, parent: TokenLimiter)

> *Summary: This method acts as a middleware handler, taking an incoming `event` and `context`. It returns a new token limiter instance configured with the maximum character limit stored in the object.*


### _TokenLimiter (class, L30-L74)

> *Summary: This middleware intercepts LLM calls to enforce a maximum character limit on the input event sequence. It calculates the total length of all events and, if exceeded, it intelligently trims the sequence by prioritizing retaining recent events while skipping initial tool results. The output is a potentially truncated list of events passed to the next handler in the chain.*


### __init__ (method, L31-L38, parent: _TokenLimiter)

> *Summary: Initializes a token limiter middleware by setting the maximum allowed character count. It accepts an event, context, and the `max_chars` integer as inputs to configure its throttling behavior.*


### _skip_leading_tool_results (method, L41-L44, parent: _TokenLimiter)

> *Summary: Advances an index past any initial sequence of `ToolResultsEvent`s within a list of events. It takes the event sequence and a starting index as input, returning the index immediately following the last leading tool result.*


### on_llm_call (method, L46-L74, parent: _TokenLimiter)

> *Summary: This method intercepts LLM calls to enforce a character limit on the input events. It calculates which events to retain by iterating backward from the end, ensuring the total length stays under `self._max_chars` while prioritizing keeping recent events. The resulting trimmed list of events is then passed to the next stage in the call chain.*

