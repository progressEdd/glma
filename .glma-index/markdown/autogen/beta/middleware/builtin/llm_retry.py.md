# autogen/beta/middleware/builtin/llm_retry.py

2 class(es): RetryMiddleware, _RetryMiddleware. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RetryMiddleware | class |  |
| _RetryMiddleware | class |  |

## Chunks

### RetryMiddleware (class, L12-L27)

> *Summary: This factory creates a middleware that wraps an execution to automatically retry upon specific exceptions. It accepts the maximum number of retries and a tuple defining which exception types should trigger a retry.*


### __init__ (method, L13-L19, parent: RetryMiddleware)

> *Summary: Initializes a retry mechanism by setting the maximum number of attempts and specifying which exception types should trigger a retry. It accepts an integer for `max_retries` and a tuple of exception classes for `retry_on`.*


### __call__ (method, L21-L27, parent: RetryMiddleware)

> *Summary: This method wraps the incoming event and context into a `_RetryMiddleware` instance. It configures this middleware with predefined retry limits and conditions specified by the object's attributes.*


### _RetryMiddleware (class, L30-L57)

> *Summary: This middleware intercepts LLM calls to automatically retry the request up to a configured maximum number of times upon encountering specified transient exceptions. It executes the next call in the chain, catching defined errors and re-running until success or exhausting all retries, at which point it raises the last encountered error.*


### __init__ (method, L33-L43, parent: _RetryMiddleware)

> *Summary: Initializes a middleware component to handle LLM retries by setting the maximum number of attempts and specifying which exceptions should trigger a retry. It accepts an event, context, and optional configuration for retry limits and exception types.*


### on_llm_call (method, L45-L57, parent: _RetryMiddleware)

> *Summary: This method wraps an LLM call to automatically retry execution up to a configured maximum number of times upon encountering specific exceptions. It executes the provided `call_next` function, returning its result on success or raising the final encountered exception if all retries fail.*

