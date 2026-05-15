# autogen/agentchat/group/events/transition_events.py

4 class(es): AfterWorksTransitionEvent, OnContextConditionTransitionEvent, OnConditionLLMTransitionEvent, ReplyResultTransitionEvent. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AfterWorksTransitionEvent | class |  |
| OnContextConditionTransitionEvent | class |  |
| OnConditionLLMTransitionEvent | class |  |
| ReplyResultTransitionEvent | class |  |

## Chunks

### AfterWorksTransitionEvent (class, L15-L36)

> *Summary: Represents an event signaling a handoff occurring after work is completed between two agents. It takes the originating agent and the target transition as input and prints a formatted notification detailing this handover.*


### __init__ (method, L23-L24, parent: AfterWorksTransitionEvent)

> *Summary: Initializes an event by storing references to the originating agent and the intended target state for a transition. This sets up the context necessary for tracking movement between agents or states.*


### print (method, L26-L36, parent: AfterWorksTransitionEvent)

> *Summary: This method logs a transition event after an agent handoff by calling the parent's print function and then executing a provided callable with a formatted string indicating the source and target agents. The output is a colored message printed to standard output.*


### OnContextConditionTransitionEvent (class, L40-L61)

> *Summary: Represents a handover event triggered by a context condition change between agents. It takes the originating agent and the target transition as input and prints a formatted notification detailing this handoff.*


### __init__ (method, L48-L49, parent: OnContextConditionTransitionEvent)

> *Summary: Initializes an event by storing references to the originating agent and the intended target for a state change. This object encapsulates the context necessary to track transitions between agents.*


### print (method, L51-L61, parent: OnContextConditionTransitionEvent)

> *Summary: This method logs a transition event when the agent moves between contexts. It calls its parent's print method and then executes a provided callable with a formatted string indicating the source and target agents of the handoff.*


### OnConditionLLMTransitionEvent (class, L65-L86)

> *Summary: Represents an event signaling a handover triggered by an LLM-based condition check between two agents. It stores the originating agent and the designated target for the transition, primarily serving to log this specific type of handoff.*


### __init__ (method, L73-L74, parent: OnConditionLLMTransitionEvent)

> *Summary: Initializes an event object by accepting a `source_agent` and a `transition_target`. This sets up the context for tracking state changes between agents.*


### print (method, L76-L86, parent: OnConditionLLMTransitionEvent)

> *Summary: This method logs a transition event to the console, indicating a handoff between agents based on an LLM condition. It uses a provided callable or defaults to standard printing to display the source and target agent names in blue text.*


### ReplyResultTransitionEvent (class, L90-L111)

> *Summary: This event signals a transition occurring after an agent has received a reply result. It takes the originating `Agent` and the destination `TransitionTarget` as input, and its primary behavior is to print a formatted message indicating this specific state change.*


### __init__ (method, L98-L99, parent: ReplyResultTransitionEvent)

> *Summary: Initializes an event by storing references to the originating agent and the intended target state for a transition. This sets up the context necessary for tracking movement between agents or states.*


### print (method, L101-L111, parent: ReplyResultTransitionEvent)

> *Summary: This method logs a transition event between agents by calling the parent's print function and then executing a provided callable with a formatted string indicating the source and target agent names. It ensures the output is colored blue for visibility during the process.*

