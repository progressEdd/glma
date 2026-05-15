# autogen/agentchat/realtime/experimental/realtime_agent.py

2 class(es): RealtimeAgentCallbacks, RealtimeAgent. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RealtimeAgentCallbacks | class |  |
| RealtimeAgent | class |  |

## Chunks

### RealtimeAgentCallbacks (class, L27-L31)

> *Summary: This class defines callbacks for a realtime agent, specifically providing an `on_observers_ready` hook that executes a checkpoint operation upon readiness. It serves as a mechanism to notify external systems when the agent's observers are initialized.*


### RealtimeAgent (class, L36-L171)

> *Summary: This deprecated class manages real-time voice interactions by initializing a client connection and registering various observers. It accepts configuration like system messages and LLM settings, then runs asynchronously to process incoming events through all registered observers. Developers can register custom functions as tools using a decorator provided by the agent.*


### __init__ (method, L44-L85, parent: RealtimeAgent)

> *Summary: Initializes an experimental agent designed for realtime client interaction, accepting configuration like a name, system message, LLM settings, and various observers. It sets up the necessary realtime client connection and registers default and provided observers to handle real-time events.*


### system_message (method, L88-L90, parent: RealtimeAgent)

> *Summary: Retrieves the predefined system prompt string associated with the agent instance. This method returns the internal `_system_message` attribute as a standard Python string.*


### logger (method, L93-L95, parent: RealtimeAgent)

> *Summary: Retrieves an instance of a logger, defaulting to a globally defined one if no specific logger has been initialized on the object. This provides consistent logging access throughout the agent's lifecycle.*


### realtime_client (method, L98-L100, parent: RealtimeAgent)

> *Summary: Retrieves and returns an instance of the `RealtimeClientProtocol` associated with the agent. This method provides access to the established real-time communication client.*


### registered_realtime_tools (method, L103-L105, parent: RealtimeAgent)

> *Summary: Returns a dictionary containing all currently registered real-time tools. This method provides access to the internal collection of available tools for the agent.*


### register_observer (method, L107-L113, parent: RealtimeAgent)

> *Summary: Adds a provided `RealtimeObserver` instance to the agent's internal list of observers, enabling it to notify this object of real-time events.*


### start_observers (method, L115-L123, parent: RealtimeAgent)

> *Summary: This method initiates asynchronous monitoring by scheduling each registered observer's `run` method on a background task. It then waits for all observers to signal readiness before notifying any registered callbacks that the observation system is active.*


### run (method, L125-L138, parent: RealtimeAgent)

> *Summary: This method initiates the agent's operation by establishing a connection with a real-time client and setting system instructions. It then starts observers and asynchronously processes incoming events from the client, dispatching each event to all registered observers.*


### register_realtime_function (method, L140-L171, parent: RealtimeAgent)

> *Summary: This decorator registers a provided function or tool with the agent's realtime capabilities. It accepts optional names and descriptions to wrap the input into a `Tool` object, which is then stored internally for agent use.*

