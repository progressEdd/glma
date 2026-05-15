# test/beta/a2a/test_card.py

1 function(s): _agent. 6 class(es): TestCapabilities, TestSecurity, TestProviderAndBranding, TestSkills, TestSkillsAutoDiscovery, TestInterfaceTenants. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| TestCapabilities | class |  |
| TestSecurity | class |  |
| TestProviderAndBranding | class |  |
| TestSkills | class |  |
| TestSkillsAutoDiscovery | class |  |
| TestInterfaceTenants | class |  |

## Chunks

### _agent (function, L25-L26)

> *Summary: Instantiates and returns a configured `Agent` object using the provided test configuration. This function serves to create a standardized agent instance for testing purposes.*


### TestCapabilities (class, L29-L50)

> *Summary: This test suite verifies the correct handling and propagation of card capabilities, specifically for push notifications and streaming. It asserts that default settings are applied correctly when building a card and confirms these settings persist after serialization/deserialization via Protobuf.*


### test_push_notifications_default_false (method, L30-L33, parent: TestCapabilities)

> *Summary: Verifies that a newly built card, initialized with a specific agent and URL, defaults to having push notifications disabled. It asserts the `push_notifications` capability on the resulting card object is set to `False`.*


### test_push_notifications_flag_propagates (method, L35-L38, parent: TestCapabilities)

> *Summary: Verifies that when a card is built with `push_notifications` set to `True`, the resulting card object correctly exposes this capability as `True`. This test confirms flag propagation during card construction using a mock agent and URL.*


### test_streaming_always_true (method, L40-L43, parent: TestCapabilities)

> *Summary: Verifies that a constructed card object, built using an agent and a specific URL, correctly reports `True` for its streaming capability. This test confirms the expected boolean state of the streaming feature on the resulting card instance.*


### test_round_trip_via_protobuf (method, L45-L50, parent: TestCapabilities)

> *Summary: This test verifies the serialization and deserialization process of a card object using Protobuf. It takes a constructed `AgentCard`, serializes it to bytes, and then reconstructs an object from those bytes to assert that specific fields, like push notifications, are correctly preserved.*


### TestSecurity (class, L53-L113)

> *Summary: These tests verify the correct construction and serialization of API card definitions, ensuring that security schemes are correctly derived from requirements, round-trip serialization is preserved, and duplicate scheme definitions are handled appropriately across multiple requirements. The methods primarily use `build_card` with various security configurations (like bearer or OAuth2) to assert the resulting structure of `security_schemes` and `security_requirements`.*


### test_no_security_by_default (method, L54-L58, parent: TestSecurity)

> *Summary: This test verifies that a card built with an agent and a non-secure URL defaults to having no security schemes or requirements. It asserts that the `security_schemes` dictionary is empty and the `security_requirements` list is empty for the resulting card object.*


### test_schemes_auto_derived_from_requirements (method, L60-L74, parent: TestSecurity)

> *Summary: This test verifies that a security card correctly derives and includes the necessary `SecurityScheme` definition for a bearer token when requirements are specified. It asserts that the resulting card's schemes map to the expected JWT authentication scheme and its requirements list contains the corresponding requirement object.*


### test_round_trip_preserves_schemes (method, L76-L83, parent: TestSecurity)

> *Summary: This test verifies that serializing and then deserializing a constructed `AgentCard` object preserves its original state. It specifically checks if the resulting decoded card matches the initial card, ensuring scheme integrity during the round trip.*


### test_oauth2_scoped_requirement (method, L85-L96, parent: TestSecurity)

> *Summary: This test verifies that a card correctly enforces an OAuth2 requirement specifying both "read" and "write" scopes when built with the provided scheme. It asserts that the resulting security requirements list contains the expected scoped requirement proto and the schemes dictionary maps the name to the correct OAuth scheme object.*


### test_scheme_deduped_across_requirements (method, L98-L113, parent: TestSecurity)

> *Summary: This test verifies that a card configuration correctly deduplicates security schemes while maintaining all specified requirements. It asserts that the resulting card object contains only two unique scheme keys ("bearer" and "oauth") despite having three distinct security requirements defined.*


### TestProviderAndBranding (class, L116-L139)

> *Summary: These tests verify that the `build_card` function correctly handles and passes through provider objects, documentation URLs, and icon URLs when constructing a card object. It also confirms default behaviors where omitted optional fields result in empty strings or default provider instances.*


### test_provider_passthrough (method, L117-L121, parent: TestProviderAndBranding)

> *Summary: This test verifies that a constructed card correctly retains the provided `AgentProvider` instance. It initializes an agent provider and then asserts that the resulting card object holds a reference to that exact provider.*


### test_documentation_and_icon_urls (method, L123-L132, parent: TestProviderAndBranding)

> *Summary: This test verifies that a constructed card object correctly stores the provided documentation and icon URLs when initialized with specific inputs. It asserts equality between the expected URL strings and the values set on the resulting card instance.*


### test_omitted_by_default (method, L134-L139, parent: TestProviderAndBranding)

> *Summary: This test verifies that a newly built card, created with a specific agent and URL, defaults to having empty documentation and icon URLs while correctly setting the provider to `AgentProvider`.*


### TestSkills (class, L142-L170)

> *Summary: These tests verify how a card object's skill set is constructed based on provided inputs. It confirms that the default single skill is used when no custom skills are supplied, custom lists override defaults, and an empty list results in zero skills.*


### test_default_single_skill_from_agent (method, L143-L148, parent: TestSkills)

> *Summary: This test verifies that a card built from a default agent correctly contains exactly one skill object, matching the expected `AgentSkill` structure. It asserts the contents of the `skills` list on the generated card against a predefined single skill instance.*


### test_custom_skills_replace_default (method, L150-L165, parent: TestSkills)

> *Summary: This test verifies that a card object correctly incorporates a provided list of custom `AgentSkill` instances when built using the `build_card` function. It asserts that the resulting card's skill list exactly matches the input list containing defined search and summarize skills.*


### test_empty_skills_list_replaces_default (method, L167-L170, parent: TestSkills)

> *Summary: When provided with an empty list of skills during card construction, the resulting card object's `skills` attribute will be an empty list. This test verifies that no default skills are applied when the input skill list is explicitly empty.*


### TestSkillsAutoDiscovery (class, L173-L220)

> *Summary: These tests verify how an agent's available skills are determined based on its configuration and provided tools. It checks scenarios where skills are automatically discovered from a toolkit, explicitly overridden by user input, or when the system falls back to a default skill if no toolkit is present or contains any skills.*


### test_skills_picked_up_from_skills_toolkit (method, L174-L186, parent: TestSkillsAutoDiscovery)

> *Summary: This test verifies that an agent, initialized with a `SkillsToolkit` pointing to local skills, correctly picks up specific predefined skills. It asserts that the resulting card object contains exactly two expected `AgentSkill` instances: "code-review" and "data-analysis".*


### test_explicit_skills_override_auto_discovery (method, L188-L198, parent: TestSkillsAutoDiscovery)

> *Summary: This test verifies that explicitly provided agent skills take precedence over any automatically discovered skills when building an agent card. It constructs an `Agent` with a specific set of tools and then asserts the resulting card's skill list matches the manually supplied overrides.*


### test_falls_back_to_default_skill_when_no_toolkit (method, L200-L207, parent: TestSkillsAutoDiscovery)

> *Summary: When an agent is initialized without a specific toolkit configuration, this test verifies that the resulting card's skills list defaults to containing only the agent's own base skill. It confirms that no external or specialized skills are added in such a scenario.*


### test_falls_back_when_toolkit_has_no_skills (method, L209-L220, parent: TestSkillsAutoDiscovery)

> *Summary: When an agent is initialized with a skills toolkit lacking specific capabilities, this test verifies that the resulting card correctly lists only the agent's inherent skill. It confirms the fallback mechanism works by asserting the presence of just the base `AgentSkill`.*


### TestInterfaceTenants (class, L223-L252)

> *Summary: This test suite verifies how tenant information is applied to supported interfaces when building a card object. It asserts that tenants are correctly set by default, propagated for specific protocols like JSONRPC, and can be assigned uniquely per transport type.*


### test_no_tenant_by_default (method, L224-L228, parent: TestInterfaceTenants)

> *Summary: This test verifies that when building a card using an agent and a specific URL, the supported interface defaults to having no tenant assigned. It asserts that the `tenant` attribute of the first supported interface is an empty string.*


### test_tenant_propagates_to_jsonrpc_interface (method, L230-L235, parent: TestInterfaceTenants)

> *Summary: This test verifies that a specified tenant context is correctly propagated to the JSON-RPC interface of a constructed card object. It asserts that the retrieved interface's `tenant` attribute matches the input tenant value and its protocol binding is set to JSONRPC.*


### test_tenant_per_transport (method, L237-L252, parent: TestInterfaceTenants)

> *Summary: This test verifies that a constructed card correctly maps transport protocols to their assigned tenants based on the provided configuration. It asserts that specific transports like JSONRPC and GRPC are associated with their designated tenant IDs, while others default to an empty string.*

