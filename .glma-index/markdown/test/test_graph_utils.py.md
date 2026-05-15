# test/test_graph_utils.py

4 class(es): FakeAgent, TestHelpers, TestGraphUtilCheckGraphValidity, TestGraphUtilInvertDisallowedToAllowed. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FakeAgent | class |  |
| TestHelpers | class |  |
| TestGraphUtilCheckGraphValidity | class |  |
| TestGraphUtilInvertDisallowedToAllowed | class |  |

## Chunks

### FakeAgent (class, L15-L21)

> *Summary: This class simulates an agent by storing a provided name upon instantiation. It exposes this stored name via a read-only property for external access.*


### __init__ (method, L16-L17, parent: FakeAgent)

> *Summary: Initializes an object by storing a provided string as its internal name attribute. This sets up the basic identity for the instance upon creation.*


### name (method, L20-L21, parent: FakeAgent)

> *Summary: Returns the stored name attribute of the object as a string. This method provides read access to the instance's designated name.*


### TestHelpers (class, L24-L41)

> *Summary: This helper class tests a graph utility function to verify the presence of self-loops within transition dictionaries. It passes two different transition structures—one without and one with self-loops—to assert the correct boolean output from the underlying graph logic.*


### test_has_self_loops (method, L25-L41, parent: TestHelpers)

> *Summary: This test verifies the `has_self_loops` utility by checking two transition dictionaries: one without self-loops and another containing them. It asserts that the function correctly identifies the presence of a self-loop in the latter case.*


### TestGraphUtilCheckGraphValidity (class, L44-L115)

> *Summary: This test suite verifies the `check_graph_validity` function by asserting correct behavior for various graph structures. It tests that the function raises errors for invalid inputs (like unknown agents or incorrect types) and issues specific warnings when the input dictionary contains isolated nodes, mismatched agent sets, or duplicate transitions.*


### test_valid_structure (method, L45-L48, parent: TestGraphUtilCheckGraphValidity)

> *Summary: Verifies that a graph structure is valid by passing a dictionary where every agent can transition to all other agents (including itself). The function confirms the integrity of the provided speaker transition map against the list of defined agents.*


### test_graph_with_invalid_structure (method, L50-L55, parent: TestGraphUtilCheckGraphValidity)

> *Summary: Asserts that `check_graph_validity` raises a `ValueError` when the input graph contains references to an agent not present in the provided list of known agents. This tests the function's validation against structural inconsistencies.*


### test_graph_with_invalid_string (method, L57-L63, parent: TestGraphUtilCheckGraphValidity)

> *Summary: This test verifies that the graph validity checker raises a `ValueError` when provided with a dictionary where agent identifiers are strings instead of actual Agent objects. It confirms the function correctly rejects improperly typed inputs during graph validation.*


### test_graph_with_invalid_key (method, L65-L68, parent: TestGraphUtilCheckGraphValidity)

> *Summary: Asserts that passing a graph dictionary containing an invalid key to the validity checker raises a `ValueError`. The function takes a graph structure and a list of agent objects as input, expecting an exception upon failure.*


### test_isolated_agent_nodes_warning (method, L71-L82, parent: TestGraphUtilCheckGraphValidity)

> *Summary: This test verifies that a warning is logged when an agent within the provided graph structure has no outgoing transitions. It passes a dictionary mapping agents to their allowed next speakers and asserts that the log output contains the word "isolated."*


### test_warning_for_mismatch_in_agents (method, L85-L99, parent: TestGraphUtilCheckGraphValidity)

> *Summary: This test verifies that a warning is logged when the provided agent transition dictionary contains references to agents not present in the official list of agents. It passes a set of known agents and a dictionary where one entry includes an extra, unknown agent object.*


### test_warning_for_duplicate_agents (method, L102-L115, parent: TestGraphUtilCheckGraphValidity)

> *Summary: This test verifies that the graph utility emits a `WARNING` when provided with transition rules containing duplicate agent references within the adjacency lists. It passes a dictionary mapping agents to lists of allowed transitions and asserts that the warning message includes the term "duplicate".*


### TestGraphUtilInvertDisallowedToAllowed (class, L118-L171)

> *Summary: These tests verify the `invert_disallowed_to_allowed` utility function by checking its behavior across various graph states. It takes a disallowed adjacency list representation and a list of all agents as input, returning an allowed adjacency list where connections are inverted based on the provided constraints.*


### test_basic_functionality (method, L119-L130, parent: TestGraphUtilInvertDisallowedToAllowed)

> *Summary: This test verifies the `invert_disallowed_to_allowed` utility by taking a graph representing disallowed connections and an agent list as input. It asserts that the function correctly transforms the disallowed structure into the expected allowed graph representation.*


### test_empty_disallowed_graph (method, L132-L143, parent: TestGraphUtilInvertDisallowedToAllowed)

> *Summary: When provided with an empty graph structure and a list of agents, this test verifies that the function correctly transforms it into a fully connected allowed graph where every agent is connected to all others. The input is an empty dictionary representing disallowed connections, and the output is a complete adjacency list for all specified agents.*


### test_fully_disallowed_graph (method, L145-L157, parent: TestGraphUtilInvertDisallowedToAllowed)

> *Summary: When provided with a graph where all connections are disallowed, this function inverts the structure to return an empty adjacency list for every agent. It takes a dictionary representing the disallowed graph and a list of agents as input, yielding a new dictionary showing no allowed connections.*


### test_disallowed_graph_with_nonexistent_agent (method, L159-L171, parent: TestGraphUtilInvertDisallowedToAllowed)

> *Summary: When provided with a graph containing references to agents not present in the allowed agent list, this test verifies that the inversion process ignores those nonexistent entries and correctly constructs the resulting fully connected graph among the valid agents. It asserts that the output matches an expected structure where every existing agent connects to all others.*

