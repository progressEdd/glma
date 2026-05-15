# test/io/test_websockets.py

2 class(es): TestTextEvent, TestConsoleIOWithWebsockets. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTextEvent | class |  |
| TestConsoleIOWithWebsockets | class |  |

## Chunks

### TestTextEvent (class, L29-L38)

> *Summary: Represents a text-based event containing a string payload. It initializes with an optional UUID and the required text, and provides a `print` method to output its text content using a specified or default printing function.*


### __init__ (method, L32-L33, parent: TestTextEvent)

> *Summary: Initializes an object by accepting an optional `UUID` and a required string payload. It passes these values up to the parent class constructor for setup.*


### print (method, L35-L38, parent: TestTextEvent)

> *Summary: This method executes a provided callable function, defaulting to the built-in `print`, using the instance's stored text content as input and producing no return value. It serves to output the object's internal state via a customizable logging mechanism.*


### TestConsoleIOWithWebsockets (class, L42-L198)

> *Summary: This test suite verifies WebSocket communication by setting up a server and client connection to exchange messages. The first test validates basic request/response cycles, while the second tests an AI chat interaction using AutoGen agents over the established WebSocket link.*


### test_input_print (method, L43-L104, parent: TestConsoleIOWithWebsockets)

> *Summary: This test verifies bidirectional communication with a WebSocket server by setting up and running the server in a thread. It sends initial messages, asserts received responses match expected values, then sends a final confirmation message to complete the interaction cycle.*


### test_chat (method, L107-L198, parent: TestConsoleIOWithWebsockets)

> *Summary: This test simulates a WebSocket chat session by starting a server and connecting to it. It sends an initial prompt to the server, which then uses AutoGen agents to process the request and stream responses back over the established connection until completion or disconnection.*

