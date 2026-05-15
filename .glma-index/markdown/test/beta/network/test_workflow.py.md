# test/beta/network/test_workflow.py

11 function(s): _agent, _state, _routing_packet, _envelope, test_default_workflow_adapter_registered_on_open, test_workflow_round_robin_advances_through_participants, test_workflow_sequence_pipeline_terminates_after_last_step, test_workflow_swarm_with_tool_handoff_and_revert, test_workflow_manager_as_initiator_auto_pattern, test_workflow_hydrate_recovers_expected_next_speaker and 1 more. 5 class(es): TestBuiltInTargets, TestBuiltInConditions, TestTransitionGraphSerialization, TestRegistry, TestGraphFactories. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _state | function |  |
| _routing_packet | function |  |
| _envelope | function |  |
| TestBuiltInTargets | class |  |
| TestBuiltInConditions | class |  |
| TestTransitionGraphSerialization | class |  |
| TestRegistry | class |  |
| TestGraphFactories | class |  |
| test_default_workflow_adapter_registered_on_open | function |  |
| test_workflow_round_robin_advances_through_participants | function |  |
| test_workflow_sequence_pipeline_terminates_after_last_step | function |  |
| test_workflow_swarm_with_tool_handoff_and_revert | function |  |
| test_workflow_manager_as_initiator_auto_pattern | function |  |
| test_workflow_hydrate_recovers_expected_next_speaker | function |  |
| test_workflow_validate_create_rejects_missing_graph | function |  |

## Chunks

### _agent (function, L62-L63)

> *Summary: Creates and returns an `Agent` instance, configuring it using a provided name and a set of event objects passed as variable arguments.*


### _state (function, L66-L78)

> *Summary: Constructs a `WorkflowState` object using provided participant order, the ID of the last speaker, the creator's identifier, and the current turn count. It serves to encapsulate the state information for a workflow process.*


### _routing_packet (function, L81-L89)

> *Summary: Creates a standardized `EV_PACKET` payload to simulate a framework-driven handoff between tools. It accepts the target tool name and an optional reason string, returning a dictionary structured for routing events.*


### _envelope (function, L92-L110)

> *Summary: Constructs an `Envelope` object based on the specified event type and sender. It populates the envelope's internal data structure with different content depending on whether the event is text, a packet, or another type.*


### TestBuiltInTargets (class, L116-L150)

> *Summary: This test suite verifies the behavior of various agent targeting strategies by simulating state transitions. It checks how different targets (like `RoundRobinTarget`, `StayTarget`, and `RevertToInitiatorTarget`) determine the next speaker or termination reason based on provided conversation states and envelopes.*


### test_agent_target_resolves_to_named_agent (method, L117-L119, parent: TestBuiltInTargets)

> *Summary: When given a target agent and the current state/envelope, this test verifies that the resolution process correctly identifies the next speaker as "bob." It asserts the resulting `TransitionDecision` matches the expected outcome.*


### test_round_robin_advances_through_order (method, L121-L129, parent: TestBuiltInTargets)

> *Summary: This test verifies that a round-robin targeting mechanism correctly cycles through a predefined list of speakers. It asserts that after the last speaker in the sequence, the target resolves to the first speaker, and between others, it moves sequentially.*


### test_round_robin_with_no_participants_terminates (method, L131-L134, parent: TestBuiltInTargets)

> *Summary: When the round-robin resolver receives a state with no participants, it resolves to a target where `next_speaker` is null and the closing reason is explicitly set to `"no_participants"`. This confirms the termination behavior for empty participant sets.*


### test_stay_target_keeps_current_speaker (method, L136-L138, parent: TestBuiltInTargets)

> *Summary: When resolving a `StayTarget` with a specified order and the last speaker being "bob," this test asserts that the resulting target maintains "bob" as its next speaker.*


### test_revert_to_initiator (method, L140-L145, parent: TestBuiltInTargets)

> *Summary: This test verifies that a `RevertToInitiatorTarget` correctly identifies the original initiator as the next speaker. It takes a state defining an order and creator, along with an envelope specifying the last speaker, to assert the correct return value.*


### test_terminate_carries_reason (method, L147-L150, parent: TestBuiltInTargets)

> *Summary: This test verifies that when a termination message with the reason "done" is processed, the resulting state has no next speaker and correctly stores "done" as the closing reason. It uses mock states and envelopes to simulate the workflow execution.*


### TestBuiltInConditions (class, L153-L168)

> *Summary: This test suite verifies the correct evaluation of built-in condition checks against simulated state and envelope inputs. It confirms that conditions like `Always`, `FromSpeaker`, and `ToolCalled` behave as expected based on the provided context, including handling different event types in envelopes.*


### test_always_fires (method, L154-L155, parent: TestBuiltInConditions)

> *Summary: Asserts that the `Always` condition evaluates to true when provided with a specific state and envelope for "alice". This confirms the unconditional nature of the `Always` check.*


### test_from_speaker_matches_sender (method, L157-L159, parent: TestBuiltInConditions)

> *Summary: Verifies that a `FromSpeaker` check correctly evaluates to true when the sender in the envelope matches the specified speaker, and false otherwise. It tests this behavior using predefined state and envelope inputs.*


### test_tool_called_matches_routing_tool_in_packet (method, L161-L164, parent: TestBuiltInConditions)

> *Summary: This test verifies that a specific tool call, "transfer\_to\_eng," is correctly recognized within a packet event context. It asserts that the `ToolCalled` evaluator returns true for the expected tool and false for an unexpected one ("escalate").*


### test_tool_called_ignores_non_packet_envelopes (method, L166-L168, parent: TestBuiltInConditions)

> *Summary: Asserts that a specific tool call evaluation returns `False` when provided with a non-packet envelope (`text_env`) and an order state. This verifies the system correctly ignores or rejects operations intended for packet envelopes when given different input types.*


### TestTransitionGraphSerialization (class, L174-L230)

> *Summary: This test suite verifies the serialization and deserialization of a `TransitionGraph` object using dictionary conversion and string dumping. It confirms that graph structure, transitions, priorities, and specific target/condition details are correctly preserved across these round-trip operations, while also asserting that loading fails gracefully when encountering unknown targets or conditions.*


### test_round_trip_via_to_dict (method, L175-L198, parent: TestTransitionGraphSerialization)

> *Summary: This test verifies that a `TransitionGraph` can be serialized to a dictionary and successfully deserialized back into an identical object. It confirms that all structural elements, including initial speaker, maximum turns, default target, transition count, priorities, and specific condition details like tool names, are preserved during the round trip.*


### test_round_trip_via_dumps_string (method, L200-L204, parent: TestTransitionGraphSerialization)

> *Summary: Verifies that a `TransitionGraph` object can be serialized to a string and then successfully deserialized back into an identical state, checking key properties like the initial speaker and maximum turns. This tests the integrity of the serialization/deserialization process for graph data.*


### test_unknown_target_name_raises (method, L206-L214, parent: TestTransitionGraphSerialization)

> *Summary: This test verifies that attempting to load a workflow configuration with an undefined default target name raises a `WorkflowGraphError`. It passes a dictionary containing the invalid target and asserts the specific error message is raised during graph loading.*


### test_unknown_condition_name_raises (method, L216-L230, parent: TestTransitionGraphSerialization)

> *Summary: This test verifies that attempting to load a workflow definition containing an unrecognized transition condition name raises a `WorkflowGraphError`. It passes a dictionary structure with an invalid "when" clause to the `TransitionGraph.loads` method and asserts the expected exception is raised.*


### TestRegistry (class, L233-L253)

> *Summary: This test verifies that custom, dataclass-based targets are correctly serialized and deserialized within a `TransitionGraph`. It registers a specific target type and asserts that the default target remains intact after saving and reloading the graph structure.*


### test_register_custom_target_extends_serialization (method, L234-L253, parent: TestRegistry)

> *Summary: This test verifies that a custom dataclass target, registered with the system, is correctly serialized and deserialized within a `TransitionGraph`. It asserts that the default target object retains its specific state (`seconds=42`) after being converted to and from a dictionary representation.*


### TestGraphFactories (class, L256-L272)

> *Summary: This test suite verifies the correct construction of `TransitionGraph` instances using factory methods. It asserts that round-robin and sequence factories correctly set initial speakers, maximum turns, and the corresponding transition logic based on provided speaker lists.*


### test_round_robin_factory (method, L257-L261, parent: TestGraphFactories)

> *Summary: This test verifies the creation of a `TransitionGraph` using a round-robin strategy with specified speakers and turn limits. It asserts that the resulting graph correctly sets the initial speaker, maximum turns, and contains the appropriate round-robin transition rule.*


### test_sequence_factory (method, L263-L272, parent: TestGraphFactories)

> *Summary: This test verifies that the `TransitionGraph` correctly constructs a sequence-based graph from an input list of speakers. It asserts the initial speaker, the number and content of transitions between consecutive agents, and the total maximum turns based on the input length.*


### test_default_workflow_adapter_registered_on_open (function, L279-L283)

> *Summary: This test verifies that the default workflow adapter is correctly registered when opening a `Hub` instance using an in-memory store. It asserts the presence of the expected `WorkflowAdapter` within the hub's adapters after initialization and ensures proper cleanup by closing the hub.*


### test_workflow_round_robin_advances_through_participants (function, L287-L341)

> *Summary: This test verifies that a round-robin workflow correctly cycles through three registered agents (Alice, Bob, Carol). It confirms the state transitions and rejects any messages sent out of sequence according to the defined turn order.*


### test_workflow_sequence_pipeline_terminates_after_last_step (function, L345-L386)

> *Summary: This test verifies that a sequential workflow pipeline correctly terminates after the last step is executed. It initializes agents and constructs a `TransitionGraph` sequence, then sends messages through the channel until the expected "sequence\_complete" closure reason is observed on the resulting channel state.*


### test_workflow_swarm_with_tool_handoff_and_revert (function, L390-L467)

> *Summary: This test simulates a multi-agent workflow where an initial agent ("triage") hands off control to another ("eng") via a specific tool call, and then the second agent's response triggers a reversion back to the initiator. It verifies that the state transitions correctly through handoff, reply, and final channel closure using a defined transition graph.*


### test_workflow_manager_as_initiator_auto_pattern (function, L471-L527)

> *Summary: This test verifies an automated workflow where the manager initiates communication, and all respondents are configured to automatically revert control back to the manager after responding. It simulates a sequence of messages between three registered agents to confirm the expected turn-taking behavior dictated by the `RevertToInitiatorTarget`.*


### test_workflow_hydrate_recovers_expected_next_speaker (function, L531-L598)

> *Summary: This test verifies that a workflow's expected next speaker is correctly recovered after the central hub process restarts. It simulates an agent handoff to another agent and then reopens the system against the same persistent store to confirm the state integrity.*


### test_workflow_validate_create_rejects_missing_graph (function, L602-L621)

> *Summary: This test verifies that attempting to create a workflow channel without providing a graph results in a `ProtocolError`. It sets up two agents, Alice and Bob, within an in-memory knowledge store and then calls the creation method with missing graph information.*

