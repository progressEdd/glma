# autogen/io/run_response.py

10 class(es): RunInfoProtocol, Usage, CostBreakdown, Cost, RunResponseProtocol, AsyncRunResponseProtocol, RunResponse, AsyncRunResponse, RunIterResponse, AsyncRunIterResponse. 72 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RunInfoProtocol | class |  |
| Usage | class |  |
| CostBreakdown | class |  |
| Cost | class |  |
| RunResponseProtocol | class |  |
| AsyncRunResponseProtocol | class |  |
| RunResponse | class |  |
| AsyncRunResponse | class |  |
| RunIterResponse | class |  |
| AsyncRunIterResponse | class |  |

## Chunks

### RunInfoProtocol (class, L36-L41)

> *Summary: Defines a contract for objects that represent run information, requiring access to a unique identifier (`uuid`) and an optional reference to the preceding response in a sequence. This protocol ensures consistent structure when handling sequential execution data.*


### uuid (method, L38-L38, parent: RunInfoProtocol)

> *Summary: Generates and returns a unique identifier object (`UUID`) for the instance. This method is called on an existing object to provide it with a distinct ID.*


### above_run (method, L41-L41, parent: RunInfoProtocol)

> *Summary: Retrieves the response object from the preceding execution step, returning it as an optional `RunResponseProtocol` instance.*


### Usage (class, L44-L48)

> *Summary: Defines a data structure to hold usage metrics for an API call. It accepts floating-point cost and integer counts for prompt, completion, and total tokens as inputs, outputting these values in the model instance.*


### CostBreakdown (class, L51-L63)

> *Summary: This class structures cost information by holding a total cost and a dictionary of model usages. It provides a static method to parse raw input dictionaries, extracting the overall cost and mapping remaining entries into individual `Usage` objects for the `models` field.*


### from_raw (method, L56-L63, parent: CostBreakdown)

> *Summary: Constructs a `CostBreakdown` object from raw dictionary input by extracting the total cost and parsing remaining items as individual model usages. It maps keys in the input data (excluding "total\_cost") to instances of the `Usage` class within the resulting structure.*


### Cost (class, L66-L75)

> *Summary: Represents the total cost structure, holding breakdowns for usage both with and without cached inference. It provides a class method to instantiate itself from a raw dictionary input by parsing nested `CostBreakdown` objects.*


### from_raw (method, L71-L75, parent: Cost)

> *Summary: Constructs a `Cost` object from a raw dictionary input by recursively parsing nested cost breakdowns for both cached and non-cached inference usage. It safely handles missing keys in the input data by defaulting to empty dictionaries.*


### RunResponseProtocol (class, L79-L100)

> *Summary: Defines a protocol for objects that represent the results of an execution run. It mandates access to events, messages, summary, context variables, and cost information, while also providing methods to process the response and set UI tools.*


### events (method, L81-L81, parent: RunResponseProtocol)

> *Summary: Returns an iterable collection of `BaseEvent` objects representing the sequence of events that occurred during a process. This method provides access to the historical event stream for inspection or further processing.*


### messages (method, L84-L84, parent: RunResponseProtocol)

> *Summary: Returns an iterable collection of `Message` objects from the instance's state. This method provides access to all stored message history.*


### summary (method, L87-L87, parent: RunResponseProtocol)

> *Summary: Retrieves a string summarizing the current state or results of an interaction. It returns `None` if no summary is available.*


### context_variables (method, L90-L90, parent: RunResponseProtocol)

> *Summary: Retrieves the current set of contextual variables associated with the instance. It returns these variables as a `ContextVariables` object or `None` if none are present.*


### last_speaker (method, L93-L93, parent: RunResponseProtocol)

> *Summary: Retrieves the identity of the most recently speaking participant from the object's state, returning a string or `None` if no speaker has been identified.*


### cost (method, L96-L96, parent: RunResponseProtocol)

> *Summary: Retrieves the associated cost information for the object instance, returning a `Cost` object or `None` if no cost is applicable.*


### process (method, L98-L98, parent: RunResponseProtocol)

> *Summary: This method takes an optional `EventProcessorProtocol` instance and executes the core logic of the class. It is responsible for processing events or managing the state based on the provided processor.*


### set_ui_tools (method, L100-L100, parent: RunResponseProtocol)

> *Summary: This method accepts a list of `Tool` objects and configures the UI with those specific tools. It modifies the internal state to make these tools available for use within the system.*


### AsyncRunResponseProtocol (class, L104-L125)

> *Summary: Defines a protocol for asynchronous run responses, providing access to streamed events, messages, summary, context variables, and cost information. It mandates methods for processing the response asynchronously and setting UI-related tools.*


### events (method, L106-L106, parent: AsyncRunResponseProtocol)

> *Summary: Returns an asynchronous iterable of `BaseEvent` objects, yielding all recorded events from the instance.*


### messages (method, L109-L109, parent: AsyncRunResponseProtocol)

> *Summary: Retrieves an iterable collection of `Message` objects from the instance. This method is asynchronous and yields all stored message records.*


### summary (method, L112-L112, parent: AsyncRunResponseProtocol)

> *Summary: Retrieves a string summarizing the current state or results of an operation, returning `None` if no summary is available.*


### context_variables (method, L115-L115, parent: AsyncRunResponseProtocol)

> *Summary: Retrieves the current state of contextual variables from the object instance. It returns a `ContextVariables` object if available, or `None` otherwise.*


### last_speaker (method, L118-L118, parent: AsyncRunResponseProtocol)

> *Summary: Retrieves the identity of the most recent speaker from the object's state, returning a string representing the speaker or `None` if no speakers have been recorded.*


### cost (method, L121-L121, parent: AsyncRunResponseProtocol)

> *Summary: Retrieves the associated cost information for the object asynchronously, returning a `Cost` object or `None`.*


### process (method, L123-L123, parent: AsyncRunResponseProtocol)

> *Summary: This asynchronous method takes an optional event processor and handles the core logic for processing responses. It executes internal state changes based on the provided or existing processor context.*


### set_ui_tools (method, L125-L125, parent: AsyncRunResponseProtocol)

> *Summary: This method accepts a list of `Tool` objects and configures the UI with them. It modifies the internal state to make these specified tools available for use within the system.*


### RunResponse (class, L128-L214)

> *Summary: This class encapsulates the state and lifecycle of an execution run, initialized with input streams and participating agents. It processes events from an input queue, yielding them until a `RunCompletionEvent` is received, at which point it populates summary, message history, and cost data.*


### __init__ (method, L129-L141, parent: RunResponse)

> *Summary: Initializes a response runner by storing an input/output stream and a sequence of agents. It sets up internal state variables for tracking messages, context, cost, and the last speaker during execution.*


### _queue_generator (method, L143-L166, parent: RunResponse)

> *Summary: This generator continuously pulls events from a provided queue until it encounters a `RunCompletionEvent`, at which point it extracts and stores final run details like history, summary, and cost. It yields each received event, handling input requests by setting up an output stream callback and raising errors immediately upon receiving an `ErrorEvent`.*


### events (method, L169-L170, parent: RunResponse)

> *Summary: Returns an iterable of `BaseEvent` objects by yielding all events read from the configured input stream. This method acts as a generator to process incoming event data sequentially.*


### messages (method, L173-L174, parent: RunResponse)

> *Summary: Returns an iterable collection of `Message` objects stored internally within the instance. This method provides read access to all recorded message history.*


### summary (method, L177-L178, parent: RunResponse)

> *Summary: Retrieves the pre-computed summary string stored within the instance. It returns this summary or `None` if it hasn't been generated.*


### above_run (method, L181-L182, parent: RunResponse)

> *Summary: Returns `None` as a placeholder for the response object from a preceding run. This method currently has no functional logic.*


### uuid (method, L185-L186, parent: RunResponse)

> *Summary: Returns the unique identifier associated with the object instance as a `UUID` type. This method provides direct access to the internal UUID attribute.*


### context_variables (method, L189-L190, parent: RunResponse)

> *Summary: Retrieves the internal `ContextVariables` object, returning it if it has been initialized or `None` otherwise. This method provides access to the state variables maintained by the instance.*


### last_speaker (method, L193-L194, parent: RunResponse)

> *Summary: Retrieves the speaker who most recently spoke from the object's internal state. Returns a string representing the speaker or `None` if no speaker has been recorded.*


### cost (method, L197-L198, parent: RunResponse)

> *Summary: Retrieves the stored cost associated with the object instance, returning it if present or `None` otherwise.*


### cost (method, L201-L205, parent: RunResponse)

> *Summary: This method updates the internal cost attribute based on the provided input. It accepts either a `Cost` object or a dictionary, converting the latter into a `Cost` instance if necessary before assignment.*


### process (method, L207-L209, parent: RunResponse)

> *Summary: This method ensures an event is processed by either a provided `EventProcessorProtocol` instance or defaults to using a `ConsoleEventProcessor`. It then delegates the actual processing of the current object (`self`) to that chosen processor.*


### set_ui_tools (method, L211-L214, parent: RunResponse)

> *Summary: This method iterates over all agents within the instance and assigns a provided list of `Tool` objects to each one, configuring their available user interface capabilities.*


### AsyncRunResponse (class, L217-L307)

> *Summary: This class manages the lifecycle and results of an asynchronous run by consuming events from an input stream. It yields various `BaseEvent` types, captures final state information like messages, summary, and cost upon receiving a completion event, and provides properties to access this collected data.*


### __init__ (method, L218-L230, parent: AsyncRunResponse)

> *Summary: Initializes a response runner by storing an asynchronous I/O stream and a sequence of agents. It sets up internal state variables for tracking messages, context, cost, and the last speaker during execution.*


### _queue_generator (method, L232-L259, parent: AsyncRunResponse)

> *Summary: This asynchronous generator consumes events from an `asyncio.Queue`, yielding each one until a `RunCompletionEvent` is encountered or an error occurs. Upon completion, it extracts and stores the conversation history, summary, cost, and context variables into the instance's state.*


### events (method, L262-L263, parent: AsyncRunResponse)

> *Summary: Yields an asynchronous iterable of `BaseEvent` objects by consuming the input stream from the associated I/O interface. This method exposes all incoming events as they are read from the source.*


### messages (method, L266-L267, parent: AsyncRunResponse)

> *Summary: Returns an iterable collection of `Message` objects stored internally within the instance. This method provides read access to all recorded message history.*


### summary (method, L270-L271, parent: AsyncRunResponse)

> *Summary: Retrieves the pre-computed summary string from the instance's internal state, returning `None` if no summary has been generated.*


### above_run (method, L274-L275, parent: AsyncRunResponse)

> *Summary: Returns `None` as a placeholder for the response object from a preceding run. This method currently has no functional logic.*


### uuid (method, L278-L279, parent: AsyncRunResponse)

> *Summary: Returns the unique identifier associated with the object instance as a `UUID` type. This method provides direct access to the internal UUID attribute.*


### context_variables (method, L282-L283, parent: AsyncRunResponse)

> *Summary: Retrieves the internal `ContextVariables` object associated with the instance. It returns this object if it has been set, otherwise it returns `None`.*


### last_speaker (method, L286-L287, parent: AsyncRunResponse)

> *Summary: Retrieves the speaker who most recently spoke from the instance's internal state. It returns that speaker's identifier as a string or `None` if no speaker has been recorded.*


### cost (method, L290-L291, parent: AsyncRunResponse)

> *Summary: Retrieves the stored cost associated with the object instance, returning it if present or `None` otherwise.*


### cost (method, L294-L298, parent: AsyncRunResponse)

> *Summary: This method updates the internal cost attribute based on the provided input. If the input is a dictionary, it converts it into a `Cost` object; otherwise, it assigns the input directly as the cost.*


### process (method, L300-L302, parent: AsyncRunResponse)

> *Summary: This method ensures an event is processed by either a provided asynchronous processor or a default console processor. It then awaits the execution of the processing logic on that chosen processor instance.*


### set_ui_tools (method, L304-L307, parent: AsyncRunResponse)

> *Summary: This method iterates over all agents within the instance and assigns a provided list of `Tool` objects to each one, configuring their available user interface capabilities.*


### RunIterResponse (class, L310-L456)

> *Summary: Provides an iterator interface to step through asynchronous agent execution by running a background thread that yields events upon request. It accepts a thread-starting function, desired event types, and involved agents, yielding `BaseEvent`s until completion or error, while storing final run data like summary and cost.*


### __init__ (method, L324-L354, parent: RunIterResponse)

> *Summary: Initializes an iterator response object by storing functions and agent lists, setting up a `StepController` and `ThreadIOStream`. It prepares internal state variables to track the execution flow, messages, costs, and final summary of the process.*


### __iter__ (method, L356-L358, parent: RunIterResponse)

> *Summary: This method provides an iterable interface to access all contained events. It returns a generator that yields each `BaseEvent` sequentially from the object's internal state.*


### _generator (method, L360-L400, parent: RunIterResponse)

> *Summary: This method lazily starts a background thread to continuously pull events from an input stream. It yields events, handles completion or errors by returning or raising exceptions, and ensures the step controller is terminated upon exiting the loop.*


### _extract_completion_data (method, L402-L411, parent: RunIterResponse)

> *Summary: This method processes a `RunCompletionEvent` to populate internal state variables. It extracts the message history, last speaker, summary, context variables, and cost information from the event's content.*


### iostream (method, L414-L416, parent: RunIterResponse)

> *Summary: Returns the internal `ThreadIOStream` object associated with the current response. This provides access to the underlying input/output mechanism for the response handling.*


### agents (method, L419-L421, parent: RunIterResponse)

> *Summary: Returns a sequence of all `Agent` objects participating in the current conversation. This method accesses and provides the internal list of registered agents.*


### summary (method, L424-L426, parent: RunIterResponse)

> *Summary: Retrieves a pre-computed string summarizing the entire conversation history. This method returns the stored summary or `None` if one hasn't been generated yet.*


### messages (method, L429-L431, parent: RunIterResponse)

> *Summary: Returns the complete sequence of `LLMMessageType` objects representing the conversation history once processing is finished. This method provides access to all recorded interactions within the current session.*


### context_variables (method, L434-L436, parent: RunIterResponse)

> *Summary: Retrieves the final set of context variables populated during a process. It returns these variables as a `ContextVariables` object or `None`.*


### last_speaker (method, L439-L441, parent: RunIterResponse)

> *Summary: Retrieves the identity of the final participant in a conversation history. It returns this string identifier only after the iteration process has concluded.*


### cost (method, L444-L446, parent: RunIterResponse)

> *Summary: Retrieves the accumulated cost associated with the execution, returning it as a `Cost` object or `None` if not yet available. This method accesses an internal state variable (`self._cost`) that is populated upon completion of an iteration.*


### uuid (method, L449-L451, parent: RunIterResponse)

> *Summary: Returns the unique identifier assigned to the current execution instance. This method accesses and returns the internal `_uuid` attribute as a `UUID` object.*


### set_ui_tools (method, L453-L456, parent: RunIterResponse)

> *Summary: This method iterates over all internal agents and assigns a provided list of `Tool` objects to each one, configuring their available user interface capabilities.*


### AsyncRunIterResponse (class, L459-L609)

> *Summary: Provides an asynchronous iterator interface to stream execution events from a background thread, allowing step-by-step monitoring of agent runs. It takes a thread starting function, event filtering criteria, and involved agents as input, yielding `BaseEvent`s until completion or error, and exposes final run data like summary and cost via properties.*


### __init__ (method, L476-L506, parent: AsyncRunIterResponse)

> *Summary: Initializes an asynchronous response iterator by accepting a thread starting function, event filtering criteria, and a list of agents. It sets up internal components like a step controller and I/O stream to manage the background process execution.*


### __aiter__ (method, L508-L510, parent: AsyncRunIterResponse)

> *Summary: This method returns an asynchronous generator that yields `BaseEvent` objects from the internal generator. It allows for asynchronous iteration over the events contained within the object.*


### _generator (method, L512-L553, parent: AsyncRunIterResponse)

> *Summary: This asynchronous generator yields events from a background thread, lazily starting that thread upon first iteration. It continuously polls for events, yielding input requests immediately while handling completion or raising errors as appropriate before ensuring the thread controller is terminated upon exit.*


### _extract_completion_data (method, L555-L564, parent: AsyncRunIterResponse)

> *Summary: This method processes a `RunCompletionEvent` to populate internal state variables. It extracts the message history, last speaker, summary, context variables, and cost information from the event's content.*


### iostream (method, L567-L569, parent: AsyncRunIterResponse)

> *Summary: Returns the internal `ThreadIOStream` object associated with the current response. This provides access to the input/output stream handling for the response context.*


### agents (method, L572-L574, parent: AsyncRunIterResponse)

> *Summary: Returns a sequence of all `Agent` objects participating in the current conversation. This method accesses and provides the internal list of associated agents.*


### summary (method, L577-L579, parent: AsyncRunIterResponse)

> *Summary: Retrieves a pre-computed string summarizing the entire conversation history. This method returns the stored summary or `None` if one hasn't been generated yet.*


### messages (method, L582-L584, parent: AsyncRunIterResponse)

> *Summary: Retrieves the complete sequence of `LLMMessageType` objects that constitute the conversation history after an iteration has finished. This method returns the internal list of messages stored within the object.*


### context_variables (method, L587-L589, parent: AsyncRunIterResponse)

> *Summary: Retrieves the final set of context variables populated during an iteration process. It returns these variables as a `ContextVariables` object or `None`.*


### last_speaker (method, L592-L594, parent: AsyncRunIterResponse)

> *Summary: Retrieves the identity of the final participant in a conversation history. It returns this string identifier only after the iteration process has concluded.*


### cost (method, L597-L599, parent: AsyncRunIterResponse)

> *Summary: Retrieves the accumulated cost associated with a process, returning it as a `Cost` object or `None` if not yet available. This method accesses an internal state variable (`self._cost`) upon request.*


### uuid (method, L602-L604, parent: AsyncRunIterResponse)

> *Summary: Returns the unique identifier assigned to the current execution instance as a `UUID` object. This method provides a stable reference point for tracking the specific run.*


### set_ui_tools (method, L606-L609, parent: AsyncRunIterResponse)

> *Summary: This method iterates over all internal agents and assigns a provided list of `Tool` objects to each one, configuring their available user interface capabilities.*

