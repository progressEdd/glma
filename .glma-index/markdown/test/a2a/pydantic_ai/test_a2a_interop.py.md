# test/a2a/pydantic_ai/test_a2a_interop.py

1 function(s): test_pydantic_a2a. 2 class(es): CustomTestClient, FakeModel. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_pydantic_a2a | function |  |
| CustomTestClient | class |  |
| FakeModel | class |  |

## Chunks

### test_pydantic_a2a (function, L30-L57)

> *Summary: This test verifies the interoperability between a Pydantic-backed AI agent and another remote agent. It initiates a multi-turn chat from a local agent to a mocked remote agent, asserting that the resulting conversation history matches expected exchanges.*


### CustomTestClient (class, L60-L71)

> *Summary: Extends `TestClient` to provide asynchronous context management for testing. It overrides the standard HTTP methods (`get`, `post`) to ensure they operate asynchronously while inheriting their core functionality from the parent class.*


### __aenter__ (method, L61-L62, parent: CustomTestClient)

> *Summary: When entering an asynchronous context, this method returns the current instance of the test client. This allows for setup or initialization logic to be executed within an `async with` block.*


### __aexit__ (method, L64-L65, parent: CustomTestClient)

> *Summary: This asynchronous context manager method performs no actions upon exiting the block. It simply completes without side effects.*


### get (method, L67-L68, parent: CustomTestClient)

> *Summary: This method acts as a simple proxy, forwarding any arguments received to the parent class's `get` implementation and returning its resulting `Response`. It ensures that standard retrieval behavior from the base class is executed.*


### post (method, L70-L71, parent: CustomTestClient)

> *Summary: This method acts as a simple wrapper around the parent class's `post` implementation. It accepts arbitrary positional and keyword arguments and returns the resulting HTTP response object.*


### FakeModel (class, L74-L92)

> *Summary: This class simulates an AI model interface by providing fixed metadata like a custom name and OpenAI system context. It implements an asynchronous `request` method that accepts messages and parameters but always returns a predefined response containing the text "Hi, I am pydantic agent!".*


### __init__ (method, L75-L76, parent: FakeModel)

> *Summary: Initializes an instance with no arguments, setting up the object for subsequent operations within the test suite.*


### model_name (method, L79-L80, parent: FakeModel)

> *Summary: Returns a hardcoded string `"custom"` representing the name of the AI model instance. This method provides a static identifier for the object it belongs to.*


### system (method, L83-L84, parent: FakeModel)

> *Summary: Returns the string `"openai"` to identify the underlying AI provider being used by the system component.*


### request (method, L86-L92, parent: FakeModel)

> *Summary: This asynchronous method simulates an API call by accepting a list of messages, optional model settings, and request parameters. It immediately returns a predefined `ModelResponse` containing a fixed text part.*

