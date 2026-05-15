# test/beta/spec/test_spec.py

6 class(es): Answer, TestFromAgent, TestToAgent, TestRoundTrip, TestBuiltinTools, TestToolkit. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Answer | class |  |
| TestFromAgent | class |  |
| TestToAgent | class |  |
| TestRoundTrip | class |  |
| TestBuiltinTools | class |  |
| TestToolkit | class |  |

## Chunks

### Answer (class, L20-L22)

> *Summary: Represents a structured response containing an integer `value` and a string `reasoning`. It inherits from `BaseModel`, implying it's used for data validation and serialization.*


### TestFromAgent (class, L25-L51)

> *Summary: This test suite verifies the `AgentSpec` creation process by testing how it extracts configuration from an agent object. It confirms that names, prompts, tool lists, and response schemas are correctly parsed and stored within the resulting specification.*


### test_extracts_name_and_prompt (method, L26-L30, parent: TestFromAgent)

> *Summary: This test verifies that an agent, initialized with a specific prompt, correctly generates a specification containing the agent's name and its associated prompt. It asserts that the resulting dictionary matches the expected structure: `{"name": "test_agent", "prompt": ["Be helpful."]}`.*


### test_extracts_tools (method, L32-L36, parent: TestFromAgent)

> *Summary: Given an agent initialized with a list of functions, this test verifies that the resulting `AgentSpec` correctly captures and lists the names of all provided tools. It asserts that the `tool_names` attribute matches the input tool identifiers.*


### test_no_tools (method, L38-L42, parent: TestFromAgent)

> *Summary: This test verifies that an agent initialized with no tools results in a specification object where the list of tool names is empty. It constructs an agent without any capabilities and asserts this state on its derived specification.*


### test_with_response_schema (method, L44-L51, parent: TestFromAgent)

> *Summary: This test verifies that an agent initialized with a specific response schema (`Answer`) correctly exposes and validates that schema via its `AgentSpec`. It asserts the presence and name of the expected response schema within the generated specification.*


### TestToAgent (class, L54-L108)

> *Summary: This suite of tests verifies the `AgentSpec`'s ability to construct an operational agent from a specification, ensuring correct tool resolution, error handling for missing tools, and proper injection of custom configurations like system prompts, hooks, variables, and dependencies. It confirms that the resulting agent accurately reflects the input specifications provided during its creation.*


### test_resolves_tools (method, L55-L65, parent: TestToAgent)

> *Summary: This test verifies that an `AgentSpec` correctly configures an agent by filtering the provided tools to only include those specified in its configuration. It asserts that the resulting agent has the correct name and contains only the expected subset of available tools.*


### test_missing_tool_raises (method, L67-L74, parent: TestToAgent)

> *Summary: This test verifies that attempting to create an agent specification with a tool name not present in the available tools raises a `ToolResolutionError`. It asserts that the error message specifically mentions the missing tool name ("nonexistent").*


### test_manual_spec (method, L76-L87, parent: TestToAgent)

> *Summary: This test verifies the correct instantiation of an agent from a specification object. It confirms that the resulting agent possesses the expected name, system prompt content, and tool count after being initialized with specific tools.*


### test_passes_hitl_hook (method, L89-L96, parent: TestToAgent)

> *Summary: This test verifies that an agent correctly incorporates a provided human-in-the-loop hook during instantiation. It confirms the `_hitl_hook` attribute is set on the resulting agent object when initialized with a custom function.*


### test_passes_variables (method, L98-L102, parent: TestToAgent)

> *Summary: This test verifies that an `Agent` object correctly stores input variables when created from a specification. It asserts that the internal `_agent_variables` attribute matches the provided dictionary during instantiation.*


### test_passes_dependencies (method, L104-L108, parent: TestToAgent)

> *Summary: This test verifies that an `Agent` object correctly stores its specified dependencies after being created from a specification. It asserts that the internal dependency map matches the input dictionary provided during agent instantiation.*


### TestRoundTrip (class, L111-L145)

> *Summary: This code verifies serialization and deserialization for agent specifications and response schemas using JSON. It tests that an `AgentSpec` can be converted to JSON, then accurately reconstructed into a new spec, which in turn correctly recreates the original agent instance with its tools. A separate test confirms that a `ResponseSchemaSpec` maintains its structure and schema integrity when serialized and deserialized.*


### test_json (method, L112-L126, parent: TestRoundTrip)

> *Summary: This test verifies the serialization and deserialization of an `AgentSpec` object to and from JSON. It ensures that after converting the spec to a string, parsing it back results in an identical specification, which can then be successfully reconstructed into a functional agent instance with its tools intact.*


### test_response_schema_spec (method, L128-L145, parent: TestRoundTrip)

> *Summary: This test verifies the serialization and deserialization cycle of a response schema specification. It takes an `Answer` object, converts it to a `ResponseSchemaSpec`, serializes it to JSON, validates it back into a spec, and finally ensures the resulting structure correctly reconstructs the original name and JSON schema when converted back to a `ResponseSchema`.*


### TestBuiltinTools (class, L148-L173)

> *Summary: These tests verify the serialization and resolution logic for an agent configuration. They ensure that an `AgentSpec` correctly reflects available tools when creating an agent, and that a `ToolResolutionError` is raised if a specified tool cannot be found among the provided options.*


### test_serialization (method, L149-L154, parent: TestBuiltinTools)

> *Summary: This test verifies that an agent constructed with specific tools correctly generates a specification containing the names of those tools. It initializes a `WebSearchTool`, creates an agent using it alongside another tool, and asserts the resulting specification lists both tool names.*


### test_resolution (method, L156-L164, parent: TestBuiltinTools)

> *Summary: This test verifies that an agent constructed from a specification correctly incorporates the provided tools. It asserts that the resulting agent object contains exactly two tools: one named "add" and one instance of `WebSearchTool`.*


### test_missing_raises (method, L166-L173, parent: TestBuiltinTools)

> *Summary: This test verifies that attempting to convert a specification into an agent will raise a `ToolResolutionError` if the specified tools are not available in the provided list. It asserts that the error message specifically mentions the missing tool name, "web\_search".*


### TestToolkit (class, L176-L198)

> *Summary: These tests verify the serialization and deserialization of an `Agent` object using `AgentSpec`. Specifically, they confirm that tool lists are correctly preserved when converting between the live agent structure and its specification format, even when tools are implicitly defined or available.*


### test_round_trip (method, L177-L185, parent: TestToolkit)

> *Summary: This test verifies the serialization and deserialization process of an `Agent` object. It creates an agent with specific tools, converts it to a specification, and then reconstructs an agent from that spec, asserting that the tool set remains identical after the round trip.*


### test_unpack_inner_tools (method, L187-L198, parent: TestToolkit)

> *Summary: This test verifies that an `AgentSpec` correctly initializes an agent with a specified set of tools. It constructs the agent using predefined tool instances and asserts that only the expected subset of named tools is present in the resulting agent's tool list.*

