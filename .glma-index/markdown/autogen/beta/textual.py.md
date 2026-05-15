# autogen/beta/textual.py

1 function(s): on. 3 class(es): Input, Submitted, TUIAgent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| on | function |  |
| Input | class |  |
| TUIAgent | class |  |

## Chunks

### on (function, L18-L22)

> *Summary: This function acts as a decorator factory that returns a decorator. The returned decorator simply wraps the input function without modifying its behavior or return value.*


### Input (class, L24-L26)

> *Summary: Defines a simple structure, `Submitted`, within the `Input` class to represent submitted data. This serves as a placeholder for holding input values passed into related components.*


### Submitted (class, L25-L26, parent: Input)

> *Summary: Represents a state indicating that an item has been submitted. It serves as a simple marker class without any specific methods or attributes.*


### TUIAgent (class, L35-L109)

> *Summary: This component provides a Textual User Interface for interacting with an `Agent`. It takes an `Agent` instance, displays the conversation history in a scrollable area, and streams responses from the agent directly into the UI as text is generated. When the user submits input, it displays their message, shows a "Thinking..." indicator, and then renders the streaming response from the agent.*


### __init__ (method, L36-L41, parent: TUIAgent)

> *Summary: Initializes the object by storing a reference to an `Agent` instance and setting up a `MemoryStream` for conversational history. It also initializes the conversation state to `None`.*


### on_mount (method, L43-L45, parent: TUIAgent)

> *Summary: When the interface is initialized, it sets the window title to reflect the name of the associated agent and automatically focuses the input field for user queries.*


### compose (method, L47-L53, parent: TUIAgent)

> *Summary: Generates a sequence of UI components for the chat interface, yielding a header displaying the agent's name, a scrollable container for history, and an input field for user messages. This method constructs the visual layout elements required to interact with the agent.*


### input_submitter (method, L56-L109, parent: TUIAgent)

> *Summary: When a user submits text, this method displays the input in the chat history and initiates an asynchronous conversation with the agent. It streams both reasoning updates and final message chunks into dedicated UI blocks until the response is complete, then re-enables the input field.*

