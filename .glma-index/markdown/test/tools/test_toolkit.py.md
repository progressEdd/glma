# test/tools/test_toolkit.py

1 class(es): TestToolkit. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestToolkit | class |  |

## Chunks

### TestToolkit (class, L12-L78)

> *Summary: This class provides a fixture to instantiate and test a `Toolkit` object, which manages callable tools. It verifies core functionalities like adding, retrieving, removing, setting tools, and registering the toolkit with agents for both execution and LLM interaction.*


### toolkit (method, L14-L23, parent: TestToolkit)

> *Summary: Constructs and returns a `Toolkit` instance containing two predefined functions, `f1` and `f2`, which are decorated as tools. These functions currently have no implementation logic.*


### test_len (method, L25-L26, parent: TestToolkit)

> *Summary: Verifies that the provided `Toolkit` instance contains exactly two elements. This assertion checks the size of the toolkit object passed as input.*


### test_get_tool (method, L28-L33, parent: TestToolkit)

> *Summary: Verifies that the toolkit correctly retrieves a specified tool by its identifier and raises a `ValueError` when an unknown tool ID is requested. It asserts the retrieved tool matches expected metadata, such as its description.*


### test_remove_tool (method, L35-L38, parent: TestToolkit)

> *Summary: This test verifies that attempting to retrieve a tool after it has been removed raises a `ValueError`. It calls the toolkit's removal method with "f1" and then asserts that subsequent retrieval of "f1" fails as expected.*


### test_set_tool (method, L40-L48, parent: TestToolkit)

> *Summary: Verifies that a provided `Toolkit` correctly registers and retrieves a function decorated with a specific description. It asserts the tool count increases after registration and confirms the retrieved tool's metadata matches the input.*


### test_register_for_execution (method, L50-L55, parent: TestToolkit)

> *Summary: This test verifies that registering an agent with the toolkit correctly populates its function map. It asserts that after calling `toolkit.register_for_execution`, the agent's internal function map contains exactly two entries.*


### test_register_for_llm (method, L57-L78, parent: TestToolkit)

> *Summary: This test verifies that registering an agent with a toolkit correctly populates the agent's LLM configuration with predefined function schemas. It asserts that the `agent.llm_config["tools"]` matches a specific list of two defined functions (`f1` and `f2`).*

