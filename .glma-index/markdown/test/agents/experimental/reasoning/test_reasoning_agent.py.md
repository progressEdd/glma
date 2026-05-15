# test/agents/experimental/reasoning/test_reasoning_agent.py

29 function(s): think_node, reasoning_agent, test_think_node_init, test_think_node_trajectory, test_think_node_str_repr, test_think_node_to_dict, test_think_node_from_dict, test_reasoning_agent_init, test_think_node_with_parent, test_think_node_complex_tree and 19 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| think_node | function |  |
| reasoning_agent | function |  |
| test_think_node_init | function |  |
| test_think_node_trajectory | function |  |
| test_think_node_str_repr | function |  |
| test_think_node_to_dict | function |  |
| test_think_node_from_dict | function |  |
| test_reasoning_agent_init | function |  |
| test_think_node_with_parent | function |  |
| test_think_node_complex_tree | function |  |
| test_think_node_serialization_with_children | function |  |
| helper_test_reasoning_agent_answer | function |  |
| test_visualize_tree_successful_case | function |  |
| test_visualize_tree_render_failure | function |  |
| test_prepare_prompt_multi_message_with_ground_truth | function |  |
| test_code_disabled | function |  |
| test_code_enabled | function |  |
| test_reasoning_agent_code_execution | function |  |
| test_rate_batch_nodes_valid_response | function |  |
| test_rate_batch_nodes_invalid_response | function |  |
| test_execute_node_with_cached_output | function |  |
| test_execute_node_with_terminate_node | function |  |
| test_execute_node_with_python_code_execution_disabled | function |  |
| test_execute_node_with_python_code_execution_enabled | function |  |
| test_execute_node_without_python_code | function |  |
| test_execute_node_with_python_response_from_llm | function |  |
| test_prepare_prompt_single_message | function |  |
| test_prepare_prompt_with_ground_truth | function |  |
| test_prepare_prompt_multi_message | function |  |

## Chunks

### think_node (function, L43-L45)

> *Summary: Instantiates and returns a `ThinkNode` object, pre-populated with predefined test content. This function serves to create a standardized node structure for agent reasoning tests.*


### reasoning_agent (function, L49-L51)

> *Summary: Instantiates a `ReasoningAgent` object, configuring it with the LLM settings provided in the input credentials structure. This function serves to create a testable instance of the agent.*


### test_think_node_init (function, L54-L62)

> *Summary: Verifies that a newly initialized `ThinkNode` object correctly sets its initial state: content matches a predefined test value, value is zero, it has no parent, and all counters (depth, children, visits) are at their default starting points.*


### test_think_node_trajectory (function, L65-L69)

> *Summary: Verifies that a `ThinkNode`'s internal trajectory array correctly initializes with the expected starting prompt line, and confirms this initial line is present in its public trajectory attribute.*


### test_think_node_str_repr (function, L72-L76)

> *Summary: Verifies that the `ThinkNode` object's string and representation outputs match a predefined format based on its internal state. It asserts equality between the generated string/repr and an expected string constructed using test content and node values.*


### test_think_node_to_dict (function, L79-L86)

> *Summary: Verifies that a `ThinkNode` object correctly serializes into a dictionary representation. It asserts specific values for content, value, depth, visits, and children after calling the `to_dict()` method on the input node.*


### test_think_node_from_dict (function, L89-L98)

> *Summary: This test verifies that the `from_dict` method correctly reconstructs a `ThinkNode` object from a provided dictionary input. It asserts that all attributes—content, value, depth, visits, and children—match the values supplied in the test dictionary.*


### test_reasoning_agent_init (function, L103-L109)

> *Summary: Verifies that a newly instantiated `ReasoningAgent` has the expected default configuration, including specific values for its name, maximum depth, beam size, and answer approach. It also confirms that the agent's root node is initialized to `None`.*


### test_think_node_with_parent (function, L112-L120)

> *Summary: This test verifies the structural integrity of a `ThinkNode` by creating a parent and child instance. It asserts that the child correctly references its parent, has a depth of one, is included in the parent's children list, and that the parent contains exactly one child.*


### test_think_node_complex_tree (function, L123-L137)

> *Summary: This test verifies the structural integrity and traversal path of a `ThinkNode` within a multi-level tree. It constructs a small hierarchy, asserting correct child counts, depth levels for each node, and that the deepest node's trajectory correctly captures its ancestors.*


### test_think_node_serialization_with_children (function, L140-L153)

> *Summary: Verifies that a `ThinkNode` structure, including nested children, can be correctly serialized to and deserialized from a dictionary format. It confirms the integrity of the node hierarchy after conversion using `to_dict()` and `from_dict()`.*


### helper_test_reasoning_agent_answer (function, L164-L221)

> *Summary: This helper function tests the `ReasoningAgent`'s termination logic by mocking its LLM responses to simulate a "TERMINATE" signal from an agent. It verifies that the agent successfully stops processing and that the resulting reasoning tree does not exceed the configured maximum depth.*


### test_visualize_tree_successful_case (function, L226-L270)

> *Summary: This test verifies the successful visualization of a sample tree structure by asserting that a mock `Digraph` object is initialized and populated correctly. It confirms that nodes are added with specific content and attributes, edges connect them as expected, and the final rendering method is called with predefined parameters.*


### test_visualize_tree_render_failure (function, L275-L288)

> *Summary: This test verifies the error handling when a tree visualization fails during rendering. It mocks the graph object to raise an exception upon calling `render()` and asserts that specific error messages are printed to standard output.*


### test_prepare_prompt_multi_message_with_ground_truth (function, L292-L329)

> *Summary: Verifies that when multiple messages are passed to `_process_prompt`, it correctly utilizes a prompt rewriter and splits content containing a `GROUND_TRUTH` marker. It asserts that the resulting prompt matches a predefined simulation and that the extracted ground truth starts with "GROUND\_TRUTH" and contains expected information.*


### test_code_disabled (function, L332-L337)

> *Summary: Verifies that a `ReasoningAgent` instance has code execution disabled and no user proxy assigned by default. It asserts the absence of configuration for code execution and a null state for the user proxy.*


### test_code_enabled (function, L340-L352)

> *Summary: Verifies that the `ReasoningAgent` correctly initializes its internal state when provided with specific configuration settings. It asserts that code execution configurations are present in both the agent and its user proxy components after instantiation.*


### test_reasoning_agent_code_execution (function, L356-L441)

> *Summary: This test verifies that a `ReasoningAgent` correctly executes code when prompted. It mocks LLM and code execution responses to simulate a workflow where the agent generates Python code, runs it via a proxy, and returns the final result.*


### test_rate_batch_nodes_valid_response (function, L444-L473)

> *Summary: This test verifies the agent's ability to correctly process and apply ratings from an external LLM response when batch grading is enabled. It inputs a list of `ThinkNode` objects and asserts that the returned rewards match expected values based on the mocked rating output.*


### test_rate_batch_nodes_invalid_response (function, L476-L495)

> *Summary: When an LLM returns an invalid response during batch grading, this test verifies that the reasoning agent assigns a neutral reward of $0.0$ to all provided nodes. It achieves this by mocking the `generate_oai_reply` method to simulate a specific, non-ideal output from the AI.*


### test_execute_node_with_cached_output (function, L498-L511)

> *Summary: This test verifies that the `ReasoningAgent` returns a node's pre-existing output when executing it. It sets an output on a `ThinkNode` and asserts that calling `agent.execute_node()` retrieves this cached value instead of recomputing it.*


### test_execute_node_with_terminate_node (function, L514-L525)

> *Summary: This test verifies that executing a `ThinkNode` configured to terminate immediately results in no return value from the agent's execution method. It initializes a `ReasoningAgent` and passes it a specific termination node for testing purposes.*


### test_execute_node_with_python_code_execution_disabled (function, L528-L544)

> *Summary: When Python code execution is explicitly disabled for the agent, calling `execute_node` with a node containing code results in a specific error message being returned instead of executing the code. This test verifies that the agent correctly reports when its capability to run embedded Python is turned off.*


### test_execute_node_with_python_code_execution_enabled (function, L547-L566)

> *Summary: This test verifies that an agent correctly sends Python code to a mocked execution endpoint and processes the returned output. It asserts that the final response from executing a `ThinkNode` containing code matches the mock return value.*


### test_execute_node_without_python_code (function, L570-L590)

> *Summary: This test verifies that the reasoning agent correctly processes a node containing only natural language content, not executable code. It simulates an LLM response to confirm the agent returns the expected answer from the mocked output.*


### test_execute_node_with_python_response_from_llm (function, L594-L616)

> *Summary: This test verifies that when an LLM mistakenly outputs Python code within its response, the agent correctly intercepts it. It asserts that the `execute_node` method returns a specific instructional message prompting the user to provide valid code snippets.*


### test_prepare_prompt_single_message (function, L619-L634)

> *Summary: Verifies that when a `ReasoningAgent` receives a single user message without prior history, its internal processing method returns the raw message content as the generated prompt and no ground truth. This confirms correct handling for initial, standalone prompts.*


### test_prepare_prompt_with_ground_truth (function, L637-L656)

> *Summary: This test verifies that the prompt processing logic correctly separates input content when a `GROUND_TRUTH` marker is present in the user message. It asserts that the resulting prompt contains the initial text and the extracted ground truth starts with the expected marker while also containing specific answer data.*


### test_prepare_prompt_multi_message (function, L659-L694)

> *Summary: When given a list of messages, this test verifies that the agent's prompt processing method utilizes the prompt rewriter by mocking the underlying AI response to return a specific, rewritten prompt structure. It asserts that the resulting processed prompt matches the simulated rewrite and that no ground truth was generated.*

