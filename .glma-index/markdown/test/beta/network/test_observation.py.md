# test/beta/network/test_observation.py

14 function(s): _agent, test_register_populates_capability_index, test_unregister_removes_from_capability_index, test_capability_index_persisted_to_disk, test_capability_index_rebuilt_on_hydrate, test_record_observation_updates_resume_observed_counters, test_record_observation_adds_unclaimed_capability_to_index, test_record_observation_ignores_non_terminal_state, test_agent_client_set_resume_refreshes_local_cache, test_agent_client_add_example_appends and 4 more. 2 class(es): TestParseSkillFrontmatter, TestRenderFallbackSkill. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| TestParseSkillFrontmatter | class |  |
| TestRenderFallbackSkill | class |  |
| test_register_populates_capability_index | function |  |
| test_unregister_removes_from_capability_index | function |  |
| test_capability_index_persisted_to_disk | function |  |
| test_capability_index_rebuilt_on_hydrate | function |  |
| test_record_observation_updates_resume_observed_counters | function |  |
| test_record_observation_adds_unclaimed_capability_to_index | function |  |
| test_record_observation_ignores_non_terminal_state | function |  |
| test_agent_client_set_resume_refreshes_local_cache | function |  |
| test_agent_client_add_example_appends | function |  |
| test_task_mirror_records_observation_on_capability_tagged_task | function |  |
| test_record_observation_writes_audit_with_observed_source | function |  |
| test_task_capability_survives_hub_hydrate | function |  |
| test_task_mirror_no_observation_when_capability_absent | function |  |

## Chunks

### _agent (function, L49-L50)

> *Summary: Creates and returns an `Agent` instance, configuring it using a provided name and a set of event objects passed as variable arguments.*


### TestParseSkillFrontmatter (class, L56-L82)

> *Summary: This test suite verifies the `parse_skill_frontmatter` function's ability to correctly extract YAML frontmatter from Markdown strings, handling cases with valid data, missing fences, and empty/comment lines. It asserts that the output object contains the parsed metadata in a `frontmatter` dictionary and the remaining content in a `body` string.*


### test_parses_basic_frontmatter_and_body (method, L57-L65, parent: TestParseSkillFrontmatter)

> *Summary: This test verifies that a parsing function correctly extracts YAML frontmatter and the main body content from a Markdown string. It asserts that the extracted dictionary matches expected key-value pairs and that the body contains specific headings.*


### test_no_frontmatter_returns_full_body (method, L67-L71, parent: TestParseSkillFrontmatter)

> *Summary: When provided Markdown without YAML frontmatter, the function returns an empty dictionary for the `frontmatter` and retains the entire input string as the `body`. This verifies that content lacking metadata is processed entirely into the main body section.*


### test_unterminated_frontmatter_returns_full_body (method, L73-L77, parent: TestParseSkillFrontmatter)

> *Summary: When provided Markdown with an incomplete frontmatter block, the function returns an empty dictionary for the frontmatter and includes the entire input string as the body content. This tests how the parser handles malformed YAML headers.*


### test_skips_empty_and_comment_lines (method, L79-L82, parent: TestParseSkillFrontmatter)

> *Summary: This test verifies that the frontmatter parsing function correctly ignores empty lines and comment lines within a Markdown string. It asserts that only valid key-value pairs are extracted into the resulting dictionary.*


### TestRenderFallbackSkill (class, L85-L119)

> *Summary: This test suite verifies the `render_fallback_skill` function's output by asserting specific content is present when rendering a passport and resume. It checks for inclusion of capabilities, domains, summaries, observed track records, and ensures a default description is used for minimal input.*


### test_includes_capabilities_domains_and_summary (method, L86-L99, parent: TestRenderFallbackSkill)

> *Summary: This test verifies that the `render_fallback_skill` function correctly incorporates a passport's name and a resume's capabilities, domains, and summary into the resulting string output. It asserts the presence of specific structured sections like headers and listed items within the generated content.*


### test_includes_observed_track_record (method, L101-L112, parent: TestRenderFallbackSkill)

> *Summary: This test verifies that the rendering function correctly includes a detailed track record section when provided with a `Resume` containing observed statistics. It asserts that specific elements like "Track record," the skill name, and the total count are present in the resulting output string.*


### test_minimal_resume_renders_default_description (method, L114-L119, parent: TestRenderFallbackSkill)

> *Summary: This test verifies that the fallback skill rendering function produces a default description when provided with a minimal `Passport` and an empty `Resume`. It asserts that both the passport's name and a standard network agent message are present in the resulting string.*


### test_register_populates_capability_index (function, L126-L143)

> *Summary: This test verifies that registering an agent with specific capabilities correctly populates the capability index within the knowledge store. It asserts that querying for registered agents using those capabilities returns the correct agent ID, while queries for non-existent capabilities return empty lists.*


### test_unregister_removes_from_capability_index (function, L147-L169)

> *Summary: This test verifies that unregistering an agent correctly removes it from capability indexes maintained by the `Hub`. It confirms that after removing all agents claiming a specific capability, the corresponding index entry is completely pruned.*


### test_capability_index_persisted_to_disk (function, L173-L191)

> *Summary: This test verifies that capability indices are correctly persisted to disk within a `DiskKnowledgeStore`. It registers an agent with the "debate" capability and then asserts that the store successfully reads back this mapping, confirming persistence.*


### test_capability_index_rebuilt_on_hydrate (function, L195-L220)

> *Summary: This test verifies that the capability index is correctly rebuilt when loading a knowledge store from disk. It registers an agent with both claimed and observed capabilities, closes the initial connection, reopens the store, and asserts that the new hub correctly indexes all previously recorded capabilities for that agent.*


### test_record_observation_updates_resume_observed_counters (function, L227-L265)

> *Summary: This test verifies that recording multiple observations for a specific capability correctly updates the agent's resume statistics within the knowledge store. It asserts that the total count, and individual counts for completed, failed, and expired states, match the recorded inputs, along with checking the latency of the last observation.*


### test_record_observation_adds_unclaimed_capability_to_index (function, L269-L292)

> *Summary: This test verifies that recording an observation with a specific capability correctly adds the agent to the list of agents possessing that capability within the knowledge store. It initializes a local hub, registers an agent without prior claims, records an "emergent" outcome for that agent, and asserts the agent's ID is now listed under the "emergent" capability.*


### test_record_observation_ignores_non_terminal_state (function, L296-L314)

> *Summary: This test verifies that the observation recording mechanism ignores non-terminal state updates. It registers an agent, records a task outcome as `RUNNING`, and asserts that this intermediate state is not included in the retrieved resume data.*


### test_agent_client_set_resume_refreshes_local_cache (function, L321-L343)

> *Summary: This test verifies that updating an agent's resume correctly refreshes the local cache and updates capability indexes within a knowledge store. It confirms that adding or removing claimed capabilities accurately reflects in the system's ability to query agents by those capabilities.*


### test_agent_client_add_example_appends (function, L347-L364)

> *Summary: This test verifies that an agent client correctly appends new examples to a knowledge store via the Hub. It registers an agent, adds two specific resume examples, and then asserts that retrieving the agent's data from the Hub contains both added examples in order.*


### test_task_mirror_records_observation_on_capability_tagged_task (function, L371-L416)

> *Summary: This test verifies that a `TaskMirror` correctly records observations when an agent executes a task tagged with a specific capability. It sets up a communication hub and runs a task using the "analysis" capability, asserting that the central resume state reflects one completed observation for that capability.*


### test_record_observation_writes_audit_with_observed_source (function, L420-L467)

> *Summary: This test verifies that when an observation is recorded on the Hub, it generates an auditable `resume_set` record tagged with `"observed"`. It confirms that both tenant-driven updates and hub-driven observations result in distinct audit entries reflecting their respective sources.*


### test_task_capability_survives_hub_hydrate (function, L471-L519)

> *Summary: This test verifies that a task's capability metadata persists correctly through the hub's persistence layer across restarts. It initializes a task with a specific capability, shuts down and reopens the hub using the same storage, then asserts that the rehydrated task specification retains the original capability value.*


### test_task_mirror_no_observation_when_capability_absent (function, L523-L557)

> *Summary: This test verifies that when an agent performs untagged work, the associated task mirror does not record any observations in the knowledge store. It sets up a communication hub and runs a simple task to assert that the `observed` field remains empty after completion.*

