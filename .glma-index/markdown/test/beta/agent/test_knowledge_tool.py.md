# test/beta/agent/test_knowledge_tool.py

1 function(s): _knowledge_tool_call. 6 class(es): TestKnowledgeTool, TestExposeToolFlag, TestWriteEventLogFlag, _FailingStore, TestEventLogFailedLifecycle, TestDefaultBootstrap. 19 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _knowledge_tool_call | function |  |
| TestKnowledgeTool | class |  |
| TestExposeToolFlag | class |  |
| TestWriteEventLogFlag | class |  |
| _FailingStore | class |  |
| TestEventLogFailedLifecycle | class |  |
| TestDefaultBootstrap | class |  |

## Chunks

### _knowledge_tool_call (function, L22-L24)

> *Summary: Retrieves the asynchronous callable method associated with the knowledge tool injected into an `Agent` instance. It accesses this by first building the knowledge tool and then extracting the specific model's call function from the resulting structure.*


### TestKnowledgeTool (class, L28-L92)

> *Summary: This test suite verifies the functionality of a knowledge tool by simulating interactions with an agent and an in-memory store. It confirms that read, write, list, delete, and unknown action operations behave as expected when using the provided storage mechanism.*


### test_read_returns_content (method, L29-L35, parent: TestKnowledgeTool)

> *Summary: This test verifies that the agent correctly retrieves content when using a knowledge tool. It writes data to an in-memory store and then asserts that calling the read action on the agent returns the exact stored string.*


### test_read_missing_path_reports_not_found (method, L37-L42, parent: TestKnowledgeTool)

> *Summary: When an agent attempts to read a non-existent file path using the knowledge tool, this test verifies that the resulting output correctly indicates the resource was not found. It uses an in-memory store and asserts the presence of "Not found" in the returned result.*


### test_write_persists_content (method, L44-L50, parent: TestKnowledgeTool)

> *Summary: This test verifies that writing content to the knowledge store persists correctly. It initializes an agent with a memory store, calls the write action, and then asserts both the tool's success message and the retrieved content matches the input.*


### test_write_without_content_reports_error (method, L52-L57, parent: TestKnowledgeTool)

> *Summary: This test verifies that attempting to write a file without providing content results in an error response from the knowledge tool. It initializes an agent with an in-memory store and calls the `write` action on a specified path, asserting the returned result contains an "Error".*


### test_list_includes_skill_md_and_entries (method, L59-L69, parent: TestKnowledgeTool)

> *Summary: When provided with a `MemoryKnowledgeStore` containing files and directories, this test verifies that the agent's knowledge tool correctly lists all contents for a given path. It asserts that both file content and filenames are present in the returned list.*


### test_list_empty_directory (method, L71-L76, parent: TestKnowledgeTool)

> *Summary: This test verifies the behavior of a knowledge tool when querying an empty directory. It initializes an agent with an in-memory store and asserts that the tool returns a message indicating emptiness for the specified path.*


### test_delete_removes_path (method, L78-L85, parent: TestKnowledgeTool)

> *Summary: This test verifies that the knowledge tool successfully removes a specified file from the memory store. It writes data to a path, calls the delete action on an agent using this store, and asserts both the successful deletion message in the result and the absence of the file in the store.*


### test_unknown_action_reports_error (method, L87-L92, parent: TestKnowledgeTool)

> *Summary: This test verifies that the system correctly reports an error when an agent attempts to execute an unknown action. It initializes an agent with a memory store and asserts that the tool call returns a message containing "Unknown action" for the input `"bogus"`.*


### TestExposeToolFlag (class, L96-L137)

> *Summary: These tests verify the behavior of an agent's knowledge tooling based on the `expose_tool` configuration flag. They assert that when `expose_tool=False`, no tools are built or mentioned in bootstrap documents, whereas setting it to true ensures the tool is exposed and included.*


### test_expose_tool_false_skips_auto_tool (method, L99-L105, parent: TestExposeToolFlag)

> *Summary: When initialized with `expose_tool=False`, the agent's knowledge tool construction method returns an empty list. This test verifies that no tools are automatically exposed to the agent under this configuration.*


### test_expose_tool_true_is_default (method, L107-L110, parent: TestExposeToolFlag)

> *Summary: This test verifies that when a `MemoryKnowledgeStore` is provided, the agent automatically exposes one tool. It asserts that the resulting knowledge tool structure contains exactly one element.*


### test_default_bootstrap_omits_tool_instruction_when_unexposed (method, L112-L124, parent: TestExposeToolFlag)

> *Summary: This test verifies that the system's default bootstrap process omits instructions for tools when they are explicitly set to be unexposed. It initializes an agent with a knowledge store and asserts that the main skill document does not mention any non-existent tools.*


### test_default_bootstrap_mentions_tool_when_exposed (method, L126-L137, parent: TestExposeToolFlag)

> *Summary: When an agent is initialized with a memory knowledge store, this test verifies that the default bootstrap process populates the knowledge base with a mention of the available `knowledge` tool. It confirms that reading the root skill file from the store successfully retrieves content containing "knowledge` tool".*


### TestWriteEventLogFlag (class, L141-L168)

> *Summary: This test suite verifies the behavior of event logging when interacting with an agent. It confirms that by default, an agent writes a log file to storage after processing a request, but this writing is skipped if `write_event_log` is explicitly set to `False`.*


### test_default_writes_event_log (method, L144-L155, parent: TestWriteEventLogFlag)

> *Summary: This test verifies that an agent, when queried, correctly writes a log entry to the knowledge store. It initializes in-memory components and asserts that reading from the expected file path yields a non-null result after the agent interaction.*


### test_opt_out_skips_event_log (method, L157-L168, parent: TestWriteEventLogFlag)

> *Summary: This test verifies that when an agent is configured to opt out of event logging, no log file is created for a given interaction stream. It initializes an agent with `write_event_log=False` and asserts the corresponding log path in the knowledge store is empty.*


### _FailingStore (class, L171-L185)

> *Summary: This class inherits from `MemoryKnowledgeStore` to simulate a failure during persistence. It overrides the `write` method to intentionally raise an `OSError` if the target path matches a log file pattern (`LOG_PREFIX` and `.jsonl`).*


### __init__ (method, L179-L180, parent: _FailingStore)

> *Summary: Initializes the object by calling the parent class's constructor, setting up the base state for the knowledge tool agent.*


### write (method, L182-L185, parent: _FailingStore)

> *Summary: This method conditionally overrides the parent's write operation; if the provided `path` starts with a specific log prefix and ends with `.jsonl`, it raises an `OSError`. Otherwise, it delegates the writing of the `content` to the superclass implementation.*


### TestEventLogFailedLifecycle (class, L189-L207)

> *Summary: This test verifies that when the knowledge store fails during an agent's operation, a specific stream event is emitted. It asserts that exactly one `EventLogFailed` event containing an `OSError` and relevant error details is captured from the provided stream after the agent runs.*


### test_failure_emits_stream_event (method, L190-L207, parent: TestEventLogFailedLifecycle)

> *Summary: This test verifies that when the knowledge store fails during an agent's operation, a specific stream event is emitted. It asserts that exactly one failure event, detailing an `OSError` from the failing store, is captured by the provided stream.*


### TestDefaultBootstrap (class, L211-L229)

> *Summary: These tests verify that the `DefaultBootstrap` correctly configures the system's skill documentation based on the `mention_tool` flag. When set to `True`, it ensures the generated `/SKILL.md` includes instructions for using a knowledge tool, while setting it to `False` omits those instructions and specifies no tools are exposed.*


### test_mention_tool_true_includes_tool_instruction (method, L214-L220, parent: TestDefaultBootstrap)

> *Summary: This test verifies that when bootstrapping with the mention tool enabled, the resulting knowledge store contains a skill document (`/SKILL.md`) which explicitly includes instructions to use the `knowledge` tool. It asserts the presence of this specific instruction string within the retrieved content.*


### test_mention_tool_false_omits_tool_instruction (method, L222-L229, parent: TestDefaultBootstrap)

> *Summary: When bootstrapping with the mention tool disabled, this test verifies that the resulting skill document does not contain references to a knowledge tool and instead includes an instruction indicating no tools are available. It confirms the expected content of the root skill file after initialization.*

