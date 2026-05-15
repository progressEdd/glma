# autogen/beta/network/transitions.py

7 function(s): register_target, register_condition, _target_to_dict, _condition_to_dict, _transition_to_dict, _transition_from_dict, _dataclass_args. 16 class(es): WorkflowGraphError, TransitionDecision, TransitionTarget, TransitionCondition, Transition, AgentTarget, RoundRobinTarget, StayTarget, RevertToInitiatorTarget, TerminateTarget, Always, FromSpeaker, ToolCalled, ContextEquals, TransitionRegistry, TransitionGraph. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WorkflowGraphError | class |  |
| TransitionDecision | class |  |
| TransitionTarget | class |  |
| TransitionCondition | class |  |
| Transition | class |  |
| AgentTarget | class |  |
| RoundRobinTarget | class |  |
| StayTarget | class |  |
| RevertToInitiatorTarget | class |  |
| TerminateTarget | class |  |
| Always | class |  |
| FromSpeaker | class |  |
| ToolCalled | class |  |
| ContextEquals | class |  |
| TransitionRegistry | class |  |
| register_target | function |  |
| register_condition | function |  |
| TransitionGraph | class |  |
| _target_to_dict | function |  |
| _condition_to_dict | function |  |
| _transition_to_dict | function |  |
| _transition_from_dict | function |  |
| _dataclass_args | function |  |

## Chunks

### WorkflowGraphError (class, L64-L65)

> *Summary: This exception signals issues during workflow graph operations, specifically when a required component cannot be found in the registry or when the graph data fails to load correctly. It inherits from `NetworkError` and is used for signaling these structural errors.*


### TransitionDecision (class, L69-L78)

> *Summary: Represents a decision dictating the next action for a workflow channel. It specifies either the `next_speaker` to engage or provides a `close_reason` if the channel should terminate.*


### TransitionTarget (class, L81-L90)

> *Summary: Defines a protocol for objects that determine the next step in a workflow. It requires an implementation of `resolve` which takes the current state and envelope to return a `TransitionDecision`.*


### resolve (method, L86-L90, parent: TransitionTarget)

> *Summary: Determines the next action by evaluating a given workflow state and an incoming envelope. It returns a `TransitionDecision` object indicating how the workflow should proceed.*


### TransitionCondition (class, L93-L102)

> *Summary: Defines a protocol for conditions that determine when a workflow transition should fire. It requires an `evaluate` method accepting the current state and envelope to return a boolean result.*


### evaluate (method, L98-L102, parent: TransitionCondition)

> *Summary: Determines if a transition should occur by evaluating the current workflow state against an incoming envelope. It returns a boolean indicating whether the transition is valid based on these inputs.*


### Transition (class, L106-L114)

> *Summary: Represents a single state transition rule defined by a condition and an action. It evaluates conditions based on priority, executing the associated target if the `when` condition is met.*


### AgentTarget (class, L121-L128)

> *Summary: This class resolves a target to a specific agent ID within the workflow context. Given a `WorkflowState` and an `Envelope`, it returns a `TransitionDecision` specifying the next speaker's ID.*


### resolve (method, L127-L128, parent: AgentTarget)

> *Summary: Determines the next action by immediately returning a decision to have the current agent speak next. It takes the current workflow state and an envelope as input, outputting a `TransitionDecision`.*


### RoundRobinTarget (class, L132-L147)

> *Summary: Determines the next participant in a sequence by cycling through a predefined order. It takes the current workflow state and an envelope as input, returning a `TransitionDecision` specifying the next speaker or indicating no participants are available.*


### resolve (method, L137-L147, parent: RoundRobinTarget)

> *Summary: Determines the next speaker in a workflow based on the current state's participant order and who last spoke or sent the envelope. It returns a `TransitionDecision` specifying the next speaker ID, handling cases where no participants are present or when the anchor is not in the defined order.*


### StayTarget (class, L151-L157)

> *Summary: This class dictates that the next speaker should be the same as the last one who spoke, defaulting to the current sender if no previous speaker is recorded in the state. It returns a `TransitionDecision` specifying this continuous speaking turn.*


### resolve (method, L156-L157, parent: StayTarget)

> *Summary: Determines the next speaker for a workflow transition by prioritizing the last speaker in the current state, falling back to the sender ID from the incoming message envelope if no previous speaker is recorded. It returns a `TransitionDecision` object specifying this determined next speaker.*


### RevertToInitiatorTarget (class, L161-L167)

> *Summary: This class determines the next speaker in a workflow by reverting control back to the original channel creator. It takes the current workflow state and an envelope as input, returning a decision that sets the `next_speaker` to the state's creator ID.*


### resolve (method, L166-L167, parent: RevertToInitiatorTarget)

> *Summary: Determines the next speaker in a workflow by returning a `TransitionDecision` object that sets the next speaker to the current state's creator ID, given a `WorkflowState` and an `Envelope`.*


### TerminateTarget (class, L171-L178)

> *Summary: This class signals the end of a communication channel by returning a `TransitionDecision` that sets the next speaker to `None` and specifies a closing reason. It uses a default "after\_work" reason but allows for customization via its instance attribute.*


### resolve (method, L177-L178, parent: TerminateTarget)

> *Summary: This method determines the next transition by returning a `TransitionDecision` object that specifies no next speaker and uses the instance's stored reason for closing. It takes a current workflow state and an envelope as input to make this decision.*


### Always (class, L185-L191)

> *Summary: This class always returns `True` when evaluated against a workflow state and envelope. It serves as a transition condition that is perpetually met.*


### evaluate (method, L190-L191, parent: Always)

> *Summary: This method checks the validity of a transition by accepting a `WorkflowState` and an `Envelope`. It currently always returns `True`, indicating that any provided state and envelope are considered valid for progression.*


### FromSpeaker (class, L195-L202)

> *Summary: This class evaluates whether a given `Envelope` originated from a specific agent identified by `agent_id`. It returns `True` if the envelope's sender ID matches the stored agent ID, signaling that the event is relevant to this speaker.*


### evaluate (method, L201-L202, parent: FromSpeaker)

> *Summary: Checks if the sender ID in an incoming `Envelope` matches the agent's own ID. Returns a boolean indicating whether the message originated from this specific agent.*


### ToolCalled (class, L206-L222)

> *Summary: This class checks if a received packet envelope's routing data matches a specific tool name. It returns `True` only if the envelope is an `EV_PACKET` and its routing field contains the matching `tool_name`.*


### evaluate (method, L218-L222, parent: ToolCalled)

> *Summary: Checks if an incoming event is a packet and, if so, verifies that the associated routing data specifies this object's tool name. Returns `True` only when both conditions are met.*


### ContextEquals (class, L226-L240)

> *Summary: This condition evaluates whether a specific key within the workflow's context variables matches a predefined value. It returns `True` if the retrieved context variable equals the target value, treating missing keys as `None`.*


### evaluate (method, L239-L240, parent: ContextEquals)

> *Summary: Checks if the current workflow state's context variable matches a predefined value associated with this transition key. Returns `True` if the values match, otherwise `False`.*


### TransitionRegistry (class, L262-L316)

> *Summary: Manages and provides access to built-in and custom transition targets and conditions, initialized with standard types. It allows registration of new target/condition classes and deserializes them from dictionary data structures into instantiated objects.*


### __init__ (method, L279-L281, parent: TransitionRegistry)

> *Summary: Initializes the object by populating internal dictionaries with built-in target and condition classes, mapping their names to the respective class types. This sets up available transition targets and conditions for later use within the system.*


### default (method, L284-L294, parent: TransitionRegistry)

> *Summary: Provides access to the globally shared, lazily initialized instance of a transition registry class. This method ensures only one default registry exists across the module's scope and allows external registration helpers to modify it.*


### register_target (method, L296-L298, parent: TransitionRegistry)

> *Summary: Stores a specific `TransitionTarget` class by its name within the object's internal dictionary, overwriting any existing registration for that same class name.*


### register_condition (method, L300-L302, parent: TransitionRegistry)

> *Summary: Adds a specified `TransitionCondition` class to the internal registry using its name as the key, overwriting any existing entry for that name.*


### target_from_dict (method, L304-L310, parent: TransitionRegistry)

> *Summary: Converts a dictionary containing transition data into a specific `TransitionTarget` instance. It retrieves the correct class based on the "name" field and instantiates it using any provided arguments from the dictionary.*


### condition_from_dict (method, L312-L316, parent: TransitionRegistry)

> *Summary: Constructs a `TransitionCondition` object by looking up the class name provided in the input dictionary and instantiating it with any associated arguments. It raises an error if no corresponding condition class is registered for the given name.*


### register_target (function, L319-L325)

> *Summary: This function adds a custom `TransitionTarget` class to the system's default registry. It accepts one argument, a target class type, and performs an in-place registration that overwrites any existing entry for that class name.*


### register_condition (function, L328-L331)

> *Summary: Adds a specified `TransitionCondition` class to the system's default registry, allowing it to be recognized for transition logic. This function takes one input—the condition class—and performs no return value.*


### TransitionGraph (class, L338-L423)

> *Summary: This class manages a conversational flow by defining an initial speaker, a list of state transitions, a default termination point, and an optional turn limit. It supports serialization to/from JSON strings and provides factory methods for creating predefined graph structures like round-robin cycling or sequential pipelines.*


### to_dict (method, L349-L356, parent: TransitionGraph)

> *Summary: Converts the object's state into a serializable dictionary format suitable for JSON. It includes the initial speaker, a list of serialized transitions, the default target, and the maximum number of turns.*


### dumps (method, L358-L360, parent: TransitionGraph)

> *Summary: Serializes the object's dictionary representation into a JSON formatted string, ensuring keys are sorted for consistent output.*


### loads (method, L363-L384, parent: TransitionGraph)

> *Summary: Parses a serialized transition graph, accepting either a JSON string or a Python dictionary as input data. It constructs and returns a `TransitionGraph` instance by deserializing speaker information, transitions, default targets, and maximum turns using the provided or default registry.*


### round_robin (method, L389-L403, parent: TransitionGraph)

> *Summary: Creates a graph structure that cycles through a list of specified participants sequentially. It initializes the process with the first participant and continues until all participants have been addressed or `max_turns` is reached.*


### sequence (method, L406-L423, parent: TransitionGraph)

> *Summary: Creates a linear workflow graph where execution flows sequentially from one step to the next in the provided list. It constructs transitions between consecutive steps and sets the final state to terminate after all defined steps are completed.*


### _target_to_dict (function, L429-L430)

> *Summary: Converts a `TransitionTarget` object into a dictionary representation. It extracts the target's name and serializes its arguments using an internal helper function.*


### _condition_to_dict (function, L433-L434)

> *Summary: Converts a `TransitionCondition` object into a dictionary structure containing the condition's name and its arguments. This is used to serialize or represent the condition for external use.*


### _transition_to_dict (function, L437-L442)

> *Summary: Converts a `Transition` object into a dictionary representation by serializing its `when` condition and `then` target using helper functions, while retaining the transition's priority level. This structure is used to standardize how transitions are represented internally or for external consumption.*


### _transition_from_dict (function, L445-L450)

> *Summary: Constructs a `Transition` object by parsing condition and target definitions from input dictionary data using the provided registry. It also incorporates an optional priority level from the same dictionary.*


### _dataclass_args (function, L453-L458)

> *Summary: Extracts a dictionary representation of an object's instance fields from a dataclass instance, specifically excluding any class-level variables. It returns an empty dictionary if the input object is not a dataclass.*

