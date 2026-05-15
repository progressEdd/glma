# test/beta/tools/test_task.py

3 function(s): _make_parent_context, test_self_delegation, test_run_subtask_description_advertises_parallel_invocation. 10 class(es): TestRunTask, TestSpecialistDelegation, TestLifecycleEvents, TestStreamFactory, TestVariablesPropagation, TestSubtaskOptOut, TestSubtaskInheritance, TestSubtaskNoRecursion, TestParallelSubtasks, TestHitlPropagation. 31 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_parent_context | function |  |
| TestRunTask | class |  |
| TestSpecialistDelegation | class |  |
| test_self_delegation | function |  |
| TestLifecycleEvents | class |  |
| TestStreamFactory | class |  |
| TestVariablesPropagation | class |  |
| TestSubtaskOptOut | class |  |
| TestSubtaskInheritance | class |  |
| TestSubtaskNoRecursion | class |  |
| TestParallelSubtasks | class |  |
| test_run_subtask_description_advertises_parallel_invocation | function |  |
| TestHitlPropagation | class |  |

## Chunks

### _make_parent_context (function, L31-L41)

> *Summary: Constructs a basic `Context` object, using provided dictionaries for dependencies and variables, to serve as a minimal parent context for testing task execution. It defaults to empty dictionaries if no inputs are supplied.*


### TestRunTask (class, L44-L130)

> *Summary: This code chunk contains several asynchronous tests verifying the functionality of a task execution system. It validates scenarios including successful runs, context injection into prompts, handling agent failures, using custom output streams, passing dependencies to tools, and default stream creation.*


### test_basic (method, L46-L54, parent: TestRunTask)

> *Summary: This test verifies basic task execution by initializing an agent with a predefined successful response and running it with a specific objective. It asserts that the returned result correctly indicates completion, matches the expected output message, and retains the original objective.*


### test_with_context (method, L57-L70, parent: TestRunTask)

> *Summary: This test verifies that provided context is correctly appended to the objective when running a task with an agent. It asserts that the resulting model request includes both the original prompt and the supplied context string.*


### test_failure (method, L73-L82, parent: TestRunTask)

> *Summary: When an agent configured to produce no responses is executed via `run_task`, the resulting task object will indicate it was not completed, contain an error, and have a null result. This test verifies that the system correctly handles failure scenarios where the agent halts prematurely.*


### test_with_custom_stream (method, L85-L97, parent: TestRunTask)

> *Summary: This test verifies that the `run_task` function correctly utilizes a provided stream instead of generating an internal one. It asserts that the returned result reflects the custom stream and contains recorded events, including at least one `ModelRequest`.*


### test_with_dependencies (method, L100-L117, parent: TestRunTask)

> *Summary: This test verifies that an agent correctly utilizes dependencies passed through its context when executing a tool. It initializes an agent with a database name dependency and asserts the task completes successfully after calling the `get_db_name` tool.*


### test_default_stream (method, L120-L130, parent: TestRunTask)

> *Summary: This test verifies that when no stream argument is provided, the `run_task` function defaults to using a `MemoryStream`. It asserts that the resulting task completes successfully and provides a non-empty event history via its stream.*


### TestSpecialistDelegation (class, L133-L272)

> *Summary: These asynchronous tests verify various delegation patterns for an `Agent` coordinator, demonstrating how it can utilize specialized agents via methods like `as_tool` or `subagent_tool`. The code confirms successful task execution, context passing to sub-tasks, and sequential orchestration involving multiple specialist agents.*


### test_via_as_tool (method, L135-L152, parent: TestSpecialistDelegation)

> *Summary: This test simulates a multi-agent workflow where a coordinator delegates a research task to a specialized researcher agent via a tool call. It asserts that the final response from the coordinator correctly incorporates the findings returned by the delegated agent.*


### test_via_subagent_tool (method, L155-L172, parent: TestSpecialistDelegation)

> *Summary: This test verifies that a coordinating agent can successfully delegate a task to a specialized subagent via a tool call. It initializes both agents and asserts that the final response from the coordinator reflects the outcome provided by the researcher agent.*


### test_with_context_param (method, L175-L200, parent: TestSpecialistDelegation)

> *Summary: This test verifies that an agent can pass contextual information to a subordinate task via a tool parameter. It initializes two agents, runs the coordinator's query, and asserts that the context provided during the initial call is correctly included in the sub-task's model request.*


### test_with_tools (method, L203-L236, parent: TestSpecialistDelegation)

> *Summary: This test verifies that a coordinating agent correctly utilizes a specialized sub-agent equipped with its own tools during task execution. It asserts that the final response matches expectations and confirms that the underlying process involved calling the nested `lookup` tool.*


### test_multiple_specialists (method, L239-L272, parent: TestSpecialistDelegation)

> *Summary: This test verifies a coordinator agent's ability to sequentially delegate tasks to multiple specialized agents. It initiates a request, asserts the final response matches expectations, and confirms that both delegated tasks were correctly started and completed in order.*


### test_self_delegation (function, L276-L292)

> *Summary: This test verifies that an agent can delegate a task to a copy of itself by registering the inner agent as a tool. When prompted, the outer agent uses this self-delegation tool, resulting in the final response from the inner agent being returned.*


### TestLifecycleEvents (class, L295-L385)

> *Summary: These asynchronous tests verify the lifecycle events emitted by an agent system when tasks are executed. They confirm that `TaskStarted`, `TaskCompleted`, and `TaskFailed` events correctly appear on parent streams, contain expected data (like objectives or results), and maintain stream references for detailed history inspection.*


### test_on_parent_stream (method, L297-L327, parent: TestLifecycleEvents)

> *Summary: This test verifies that when a coordinator agent delegates a task to a researcher agent, both `TaskStarted` and `TaskCompleted` events are correctly emitted onto the parent stream. It asserts that these events accurately reflect the delegated objective and the final result returned by the researcher.*


### test_completed_has_stream_reference (method, L330-L356, parent: TestLifecycleEvents)

> *Summary: This test verifies that when a task completes, the resulting `TaskCompleted` object correctly references the stream of its subordinate task. It simulates an agent interaction flow to confirm this stream reference exists and contains relevant request/response events from the sub-task's history.*


### test_failure_event (method, L359-L385, parent: TestLifecycleEvents)

> *Summary: This test verifies that when an agent configured to fail is invoked by a coordinator, the parent stream correctly emits a `TaskFailed` event. It asserts that exactly one such failure event occurs, correctly identifying the failing agent and containing the expected error details.*


### TestStreamFactory (class, L388-L479)

> *Summary: This test suite verifies that a stream factory correctly provides fresh `MemoryStream` instances for each sub-task invocation when configuring an agent's tools. It asserts that the factory creates exactly one or multiple streams based on the task complexity and confirms that events are recorded within these generated streams.*


### test_creates_fresh_stream (method, L390-L416, parent: TestStreamFactory)

> *Summary: This test verifies that the stream factory generates a new `MemoryStream` instance every time it's called by the agent system. It initializes an agent coordinator with a worker tool configured to use this stream factory and asserts that exactly one stream is created during execution, containing at least one `ModelRequest` event.*


### test_multiple_calls (method, L419-L453, parent: TestStreamFactory)

> *Summary: This test verifies that when an agent is asked to perform multiple tasks sequentially, each invocation receives its own dedicated stream. It confirms this by asserting that two distinct streams are created and that the corresponding model requests within those streams correctly contain "Task A" and "Task B".*


### test_defaults_to_memory_stream (method, L456-L479, parent: TestStreamFactory)

> *Summary: This test verifies that when no stream factory is provided, sub-tasks default to using a `MemoryStream`. It initializes an agent coordinator with a worker tool and asserts that the resulting task history contains events from the spawned sub-task.*


### TestVariablesPropagation (class, L482-L540)

> *Summary: This test suite verifies variable propagation and isolation within an agent system. It confirms that a worker can correctly read context variables passed to it by the coordinator, and also ensures that mutations made by child tasks do not inadvertently modify the parent's state due to isolated execution contexts.*


### test_propagates_variables (method, L484-L509, parent: TestVariablesPropagation)

> *Summary: This test verifies that a variable provided to the main agent is correctly propagated through a nested worker agent. It sets up two agents, one calling a tool that reads a context variable, and another coordinating this call, asserting the correct input value was passed to the underlying tool mock.*


### test_child_mutations_do_not_leak_to_parent (method, L512-L540, parent: TestVariablesPropagation)

> *Summary: This test verifies that mutations made within a child task remain isolated and do not affect the parent context. It executes a worker agent with a mutation tool against a parent context, asserting that the initial state of the parent's variables remains unchanged after execution.*


### TestSubtaskOptOut (class, L544-L564)

> *Summary: These tests verify that an `Agent` instance defaults to having no subtask tools unless explicitly configured otherwise. It confirms that setting `tasks=False` disables the tools, while providing a configuration object enables specific subtask functions like `"run_subtask"`.*


### test_default_actor_has_no_subtask_tools (method, L545-L550, parent: TestSubtaskOptOut)

> *Summary: Verifies that a newly instantiated `Agent` object, by default, possesses no subtask tools. It checks if the set of function names returned by calling `_build_subtask_tools()` is empty.*


### test_explicit_disabled_actor_has_no_subtask_tools (method, L552-L557, parent: TestSubtaskOptOut)

> *Summary: When an agent is initialized with `tasks=False`, this test verifies that the method responsible for building subtask tools returns no available tool names. It asserts that the set of function names derived from the agent's subtask tools is empty.*


### test_taskconfig_actor_has_subtask_tools (method, L559-L564, parent: TestSubtaskOptOut)

> *Summary: This test verifies that an `Agent` initialized with a `TaskConfig` receives specific subtask tools upon construction. It asserts that the set of available tool names includes both `"run_subtask"` and `"run_subtasks"`.*


### TestSubtaskInheritance (class, L568-L724)

> *Summary: This code tests how tools are inherited by a spawned subtask agent from its parent. It verifies four scenarios: default inheritance, exclusion via `exclude_tools`, restriction via `include_tools` (allowlist), and addition of new capabilities using `extra_tools`.*


### test_subtask_inherits_parent_tools (method, L569-L605, parent: TestSubtaskInheritance)

> *Summary: This test verifies that a spawned subtask inherits the tools available to its parent agent. It configures an agent with a tool, initiates a subtask request, and asserts that the resulting event history from the subtask contains a call to the inherited tool.*


### test_subtask_excludes_via_exclude_tools (method, L607-L660, parent: TestSubtaskInheritance)

> *Summary: This test verifies that excluding specific tools via `TaskConfig` correctly restricts tool availability during subtask execution. It sets up a parent agent with both public and secret tools, then spawns a subtask configured to exclude the secret tool, asserting that only permitted tools are available to the spawned agent.*


### test_subtask_include_tools_allowlist (method, L662-L688, parent: TestSubtaskInheritance)

> *Summary: This test verifies that when a subtask configuration specifies an `include_tools` allowlist, only the named tools are available to the spawned agent. It initializes a parent agent with three tools and spawns a subtask restricted to using only two of those specified tools.*


### test_subtask_extra_tools_added (method, L690-L724, parent: TestSubtaskInheritance)

> *Summary: This test verifies that an agent correctly utilizes tools provided specifically to a nested subtask. It sets up a parent agent with a task configuration that includes extra tools, then asserts that the subtask successfully invokes one of those added tools during execution.*


### TestSubtaskNoRecursion (class, L728-L765)

> *Summary: This test verifies that a spawned subtask agent, when initiated by a parent, does not possess any subtask execution capabilities. It achieves this by mocking the task running mechanism and asserting that the resulting child agent has an empty list of tools and no associated task configuration.*


### test_child_has_no_subtask_tools (method, L729-L765, parent: TestSubtaskNoRecursion)

> *Summary: This test verifies that a spawned subtask agent never possesses any tools for further recursion. It spawns a child agent, intercepts its execution via monkey-patching, and asserts that the resulting child agent has no assigned task configuration and an empty list of subtask tools.*


### TestParallelSubtasks (class, L769-L838)

> *Summary: This test suite verifies the concurrent execution of multiple subtasks dispatched from a single agent turn. It asserts that when an LLM emits several `run_subtask` calls or one `run_subtasks` call with parallel enabled, the executor correctly dispatches and reports individual start/completion events for each independent task.*


### test_parallel_run_subtask_calls_succeed (method, L770-L809, parent: TestParallelSubtasks)

> *Summary: When provided with an assistant message containing multiple `run_subtask` tool calls, this test verifies that the executor dispatches these tasks concurrently. It asserts that for each of the three independent subtasks requested in the input configuration, a corresponding `TaskStarted` and `TaskCompleted` event is emitted during the execution stream.*


### test_run_subtasks_bundles_parallel_dispatch (method, L811-L838, parent: TestParallelSubtasks)

> *Summary: This test verifies that calling a tool to run multiple subtasks in parallel results in the expected number of completion events. It initializes an agent with a configuration triggering two tasks and asserts that exactly two `TaskCompleted` events are recorded from the stream history.*


### test_run_subtask_description_advertises_parallel_invocation (function, L841-L854)

> *Summary: Verifies that the descriptions for single and multiple subtask execution tools explicitly mention "parallel." This ensures language models are instructed to invoke these tools concurrently within a single response rather than sequentially.*


### TestHitlPropagation (class, L857-L936)

> *Summary: These tests verify the priority and usage of Human-in-the-Loop (HITL) hooks between parent and subagents. They assert that a subagent correctly uses its parent's HITL hook when one is available, but prioritizes its own custom hook if it defines one.*


### test_reuses_parent_hitl_hook (method, L859-L893, parent: TestHitlPropagation)

> *Summary: This test verifies that a subagent correctly utilizes the parent agent's Human-in-the-Loop (HITL) hook when requesting input via `ctx.input()`. It sets up a worker needing human approval and a coordinator with a defined HITL hook, asserting that the correct inputs are passed to both the mock tool handler and the HITL hook callback.*


### test_own_hitl_hook_takes_priority (method, L896-L936, parent: TestHitlPropagation)

> *Summary: This test verifies that a subagent's dedicated HITL hook is prioritized over the parent agent's when both are available during execution. It sets up two agents, one with its own tool and HITL hook, and another acting as a coordinator with a separate HITL hook, then asserts that only the subagent's hooks were invoked.*

