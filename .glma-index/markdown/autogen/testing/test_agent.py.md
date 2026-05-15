# autogen/testing/test_agent.py

1 function(s): convert_fake_message. 5 class(es): TestAgent, FakeClient, FakeMessage, FakeChoice, FakeClientResponse. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAgent | class |  |
| FakeClient | class |  |
| convert_fake_message | function |  |
| FakeMessage | class |  |
| FakeChoice | class |  |
| FakeClientResponse | class |  |

## Chunks

### TestAgent (class, L13-L69)

> *Summary: This context manager wraps a `ConversableAgent` to facilitate testing by temporarily replacing its LLM client with a mock that returns predefined messages from an input iterable. Upon exiting the context, it restores the agent's original client and human input mode.*


### __init__ (method, L33-L47, parent: TestAgent)

> *Summary: Initializes a test fixture by capturing the original human input mode and client of a provided `ConversableAgent`. It then sets up a fake client instance, populated with initial messages, for controlled testing.*


### __enter__ (method, L49-L54, parent: TestAgent)

> *Summary: When entering the context, it disables human input mode on the agent and swaps the agent's client with a mocked version for testing purposes. This setup ensures that subsequent operations use the fake client instead of the real one.*


### __exit__ (method, L56-L69, parent: TestAgent)

> *Summary: Restores the agent's human input mode and client to their original states upon exiting a context manager. It specifically handles `StopIteration` exceptions by suppressing message end signals if configured.*


### FakeClient (class, L72-L88)

> *Summary: This class simulates a client interface by iterating over provided messages to generate responses. It allows testing interactions by returning predefined choices from an input iterable when `create` is called, and extracts text or message objects from a simulated response object.*


### __init__ (method, L73-L78, parent: FakeClient)

> *Summary: Initializes the agent by creating an iterator over converted input messages and setting initial usage summary attributes to `None`. This setup allows the agent to process a potentially infinite stream of message inputs.*


### create (method, L80-L82, parent: FakeClient)

> *Summary: This method retrieves the next predefined choice from an internal iterator and wraps it in a `FakeClientResponse` object, simulating a successful API response for testing purposes. It accepts arbitrary keyword arguments but primarily relies on its internal state to generate the output.*


### extract_text_or_completion_object (method, L84-L88, parent: FakeClient)

> *Summary: Retrieves the content from a fake client response by calling its message retrieval function. It returns either a list of strings or a list of fake message objects depending on the response structure.*


### convert_fake_message (function, L91-L95)

> *Summary: Transforms an input that is either a string or a dictionary into a `FakeChoice` object. If the input is a string, it wraps it as content; otherwise, it merges the dictionary contents under the "assistant" role.*


### FakeMessage (class, L98-L99)

> *Summary: Defines a structure for simulating messages, requiring a `content` field that can be either a string or a dictionary. This serves as a mock data type for testing agent interactions.*


### FakeChoice (class, L103-L104)

> *Summary: Represents a mock choice object inheriting from the base protocol's choice structure. It is designed to hold and return a `FakeMessage` instance during testing scenarios.*


### FakeClientResponse (class, L108-L113)

> *Summary: This class simulates a response from a model client, holding a list of fake choices and specifying the model name. It provides a method to retrieve messages by extracting the `message` attribute from each choice within its structure.*


### message_retrieval_function (method, L112-L113, parent: FakeClientResponse)

> *Summary: Retrieves the messages from all available choices within the agent's state. It returns a list containing either strings or `FakeMessage` objects, depending on the internal structure of `self.choices`.*

