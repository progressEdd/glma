# test/beta/middleware/test_llm_call.py

3 class(es): MockMiddleware, OrderingMiddleware, TestLLMCallMiddleware. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MockMiddleware | class |  |
| OrderingMiddleware | class |  |
| TestLLMCallMiddleware | class |  |

## Chunks

### MockMiddleware (class, L16-L35)

> *Summary: This middleware intercepts LLM calls by wrapping the execution of the next agent turn within mock entry and exit points. It takes a `MagicMock` object during initialization to record interactions with incoming events and returns the result from the downstream call.*


### __init__ (method, L17-L24, parent: MockMiddleware)

> *Summary: Initializes the test middleware by accepting an event, context, and a mock object. It stores the provided mock for later use during testing operations.*


### on_llm_call (method, L26-L35, parent: MockMiddleware)

> *Summary: This asynchronous method intercepts an LLM call by mocking the initial event before passing control to the next handler. It then un-mocks the state upon receiving the final `ModelResponse` from the downstream execution.*


### OrderingMiddleware (class, L38-L59)

> *Summary: This middleware wraps an LLM call execution by using a provided mock object to track entry and exit points at a specific position. It intercepts the `on_llm_call` event, executes the next handler, and then records the completion of the call via the mock before returning the final response.*


### __init__ (method, L39-L48, parent: OrderingMiddleware)

> *Summary: Initializes an object with a base event, context, a mock object for dependency injection, and a specific integer position. This setup prepares the instance to interact with mocked services during testing.*


### on_llm_call (method, L50-L59, parent: OrderingMiddleware)

> *Summary: This asynchronous method wraps the next agent turn execution by entering and exiting a mock context around the call. It passes along the provided events and context to the downstream handler and returns its resulting `ModelResponse`.*


### TestLLMCallMiddleware (class, L62-L114)

> *Summary: This test suite verifies the behavior of middleware applied to an `Agent`'s LLM calls. It uses mocks and custom middlewares to assert correct call sequences, message mutations, and tracking interactions when the agent processes a prompt.*


### test_creation (method, L64-L74, parent: TestLLMCallMiddleware)

> *Summary: This test verifies the initial interaction when an agent is asked a question. It asserts that the mock middleware's `enter` method was called with the correct input text and that the `exit` method was subsequently called.*


### test_call_sequence (method, L77-L87, parent: TestLLMCallMiddleware)

> *Summary: This test verifies the execution order of middleware components when an agent processes a prompt. It asserts that the `enter` hooks are called sequentially from 1 to 3, and the corresponding `exit` hooks are called in reverse order (3 down to 1).*


### test_incoming_message_mutation (method, L90-L114, parent: TestLLMCallMiddleware)

> *Summary: This test verifies that a custom middleware mutates the input message content by doubling it before an LLM call is made. It asserts that the final tracked request sent to the mock tracking service contains the original input string repeated eight times ($2^3$).*

