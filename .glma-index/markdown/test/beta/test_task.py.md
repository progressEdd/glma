# test/beta/test_task.py

3 function(s): _agent, _persisted, _subscribe. 9 class(es): TestTaskState, TestTaskSpec, TestStandaloneLifecycle, TestProgress, TestExpire, TestBoundContext, TestTtl, TestPropertiesBeforeEntry, TestMetadata. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _persisted | function |  |
| _subscribe | function |  |
| TestTaskState | class |  |
| TestTaskSpec | class |  |
| TestStandaloneLifecycle | class |  |
| TestProgress | class |  |
| TestExpire | class |  |
| TestBoundContext | class |  |
| TestTtl | class |  |
| TestPropertiesBeforeEntry | class |  |
| TestMetadata | class |  |

## Chunks

### _agent (function, L29-L31)

> *Summary: Creates and returns an `Agent` instance configured with the "researcher" name and specified Anthropic settings. This function initializes a basic agent object without making any actual model calls.*


### _persisted (function, L34-L40)

> *Summary: Retrieves a list of durably-persisted events from a provided `MemoryStream`. It accesses the stream's history storage to fetch all recorded events, excluding transient types like progress updates or message chunks.*


### _subscribe (function, L43-L51)

> *Summary: This function registers a callback with the provided `MemoryStream` to capture all emitted events, including transient ones. It returns a list that will be populated in real-time as events flow through the stream.*


### TestTaskState (class, L54-L60)

> *Summary: Verifies that the `TERMINAL_TASK_STATES` set correctly includes terminal states like COMPLETED, FAILED, and EXPIRED, while excluding active states such as CREATED and RUNNING. This test ensures proper state management logic for tasks.*


### test_terminal_set (method, L55-L60, parent: TestTaskState)

> *Summary: Verifies that the `TERMINAL_TASK_STATES` set correctly includes `COMPLETED`, `FAILED`, and `EXPIRED`, while excluding initial states like `CREATED` and `RUNNING`. This test ensures the definition of terminal task statuses is accurate.*


### TestTaskSpec (class, L63-L75)

> *Summary: Verifies the default initialization of `TaskSpec`, ensuring titles are set correctly while descriptions and payloads start empty. It also confirms that each instance receives an independent payload dictionary, preventing state leakage between objects.*


### test_defaults (method, L64-L68, parent: TestTaskSpec)

> *Summary: This test verifies that a `TaskSpec` initialized with only a title defaults its description to an empty string and its payload to an empty dictionary. It confirms the provided title is correctly set on the instance.*


### test_payload_isolated (method, L70-L75, parent: TestTaskSpec)

> *Summary: Verifies that modifying the payload of one `TaskSpec` instance does not affect another, ensuring payloads are isolated upon creation. It confirms that adding a key-value pair to `a.payload` leaves `b.payload` unchanged.*


### TestStandaloneLifecycle (class, L78-L160)

> *Summary: This test suite verifies the lifecycle management of standalone tasks by simulating various execution scenarios. It checks that tasks correctly transition through states (RUNNING, COMPLETED, FAILED), records results and errors in persisted streams, and handles idempotent completion attempts.*


### test_clean_exit_auto_completes (method, L82-L93, parent: TestStandaloneLifecycle)

> *Summary: This test verifies that an agent's task successfully completes its lifecycle when running a specified research query. It asserts the task transitions from `RUNNING` to `COMPLETED` and confirms that both `TaskStarted` and `TaskCompleted` events are present in the streamed output.*


### test_explicit_complete_records_result (method, L96-L109, parent: TestStandaloneLifecycle)

> *Summary: This test verifies that when a task is explicitly completed with specific data, the resulting stream correctly emits one `TaskCompleted` event containing the provided result and metadata. It confirms the state transitions and content of the final completion notification.*


### test_complete_is_idempotent (method, L112-L121, parent: TestStandaloneLifecycle)

> *Summary: This test verifies that completing a task multiple times has the same effect as completing it once. It asserts that only one `TaskCompleted` event is persisted when calling `.complete()` sequentially with different arguments.*


### test_exception_emits_task_failed_and_propagates (method, L124-L145, parent: TestStandaloneLifecycle)

> *Summary: This test verifies that when an exception occurs within a task execution context, the task state correctly transitions to `FAILED`, the error is recorded, and a corresponding `TaskFailed` event is emitted through the stream. It asserts that the original exception propagates out of the asynchronous block as expected.*


### test_explicit_fail_with_string (method, L148-L160, parent: TestStandaloneLifecycle)

> *Summary: This test verifies that explicitly failing a task with a string message results in the correct state and metadata. It asserts that the resulting stream contains exactly one `TaskFailed` event whose error attribute matches the provided string.*


### TestProgress (class, L163-L194)

> *Summary: This test verifies that progress updates correctly accumulate into a task's metadata while also emitting corresponding events via a stream. It further asserts that attempting to report progress after a task has been completed results in no emitted progress events.*


### test_progress_accumulates_into_metadata (method, L165-L180, parent: TestProgress)

> *Summary: This test verifies that progress updates provided to an agent task are correctly accumulated into the task's metadata and emitted as distinct events. It confirms that two specific progress calls result in both a combined metadata state and two corresponding `TaskProgress` events being captured.*


### test_progress_after_terminal_is_noop (method, L183-L194, parent: TestProgress)

> *Summary: This test verifies that calling `task.progress()` after a task has been completed does not emit any progress events. It sets up an agent and context, completes a task, attempts to report late progress, and asserts no `TaskProgress` events are generated.*


### TestExpire (class, L197-L209)

> *Summary: This test verifies that calling the `expire()` method on a task correctly transitions its state to `EXPIRED`. It then asserts that exactly one `TaskExpired` event, matching the task's objective, is emitted from the associated stream.*


### test_expire_emits_task_expired (method, L199-L209, parent: TestExpire)

> *Summary: This test verifies that expiring a running task emits the correct `TaskExpired` event. It initializes an agent, starts a slow task, calls its expire method, and then asserts that exactly one corresponding expiration event is received from the task's stream.*


### TestBoundContext (class, L212-L255)

> *Summary: This test suite verifies how an agent interacts with a provided `ConversationContext` stream, ensuring that task lifecycle events (`TaskStarted`, `TaskProgress`, `TaskCompleted`) are correctly emitted when the context is supplied. It also confirms dependency management within nested tasks, asserting that inner tasks correctly reference their parent's context dependencies and restore the outer scope upon exiting.*


### test_events_fire_on_supplied_stream (method, L216-L229, parent: TestBoundContext)

> *Summary: This test verifies that specific lifecycle events are emitted when an agent task is executed using a provided stream. It asserts the presence of exactly one `TaskStarted`, one `TaskProgress`, and one `TaskCompleted` event after simulating task start, progress update, and completion.*


### test_task_inject_stamped_during_block (method, L232-L241, parent: TestBoundContext)

> *Summary: This test verifies that a task injected into the conversation context remains present during its execution block, but is subsequently removed from the context's dependencies afterward. It uses an agent and a memory stream to simulate this dependency lifecycle check.*


### test_nested_tasks_restore_previous (method, L244-L255, parent: TestBoundContext)

> *Summary: This test verifies that when a nested task structure executes, the context correctly tracks dependencies for both the outer and inner tasks during execution. It asserts that after exiting the scope of the nested tasks, the dependency tracking within the context is cleared.*


### TestTtl (class, L258-L272)

> *Summary: This test suite verifies the time-to-live (TTL) functionality of an agent's tasks. It asserts that setting a `ttl_seconds` populates `expires_at` and `started_at` metadata, while omitting TTL results in `expires_at` being `None`.*


### test_ttl_seconds_populates_expires_at (method, L260-L266, parent: TestTtl)

> *Summary: This test verifies that when a task is created with a Time-To-Live (TTL) in seconds, the resulting task metadata correctly populates `expires_at` and `started_at` timestamps, ensuring the expiration time is after the start time. It uses an asynchronous agent to execute this check.*


### test_no_ttl_leaves_expires_at_none (method, L269-L272, parent: TestTtl)

> *Summary: This test verifies that a task created without a Time-To-Live (TTL) correctly has its `expires_at` metadata set to `None`. It achieves this by acquiring an agent and then using the `task()` method with the identifier "no-ttl".*


### TestPropertiesBeforeEntry (class, L275-L301)

> *Summary: This test suite verifies the initial state and access restrictions of a task object before it has been entered (via `__aenter__`). It asserts that tasks start in a `CREATED` state and raises `RuntimeError` when attempting to access properties like `task_id` or `metadata` prematurely, while also ensuring double entry fails.*


### test_state_returns_created (method, L276-L279, parent: TestPropertiesBeforeEntry)

> *Summary: When an agent creates a new task using the provided identifier, it asserts that the resulting task object's state is `TaskState.CREATED`. This test verifies the initial state upon task creation.*


### test_task_id_raises_before_entry (method, L281-L285, parent: TestPropertiesBeforeEntry)

> *Summary: This test verifies that accessing the `task_id` attribute on a newly created task object raises a `RuntimeError` if the task has not yet been entered (i.e., before its context manager entry). It asserts that the raised exception specifically matches the "before \_\_aenter\_\_" message.*


### test_metadata_raises_before_entry (method, L287-L291, parent: TestPropertiesBeforeEntry)

> *Summary: This test verifies that accessing the metadata of a task before it has been entered raises a `RuntimeError`. It achieves this by calling `agent.task("not-yet-entered")` and then attempting to access `.metadata` within a `pytest.raises` context.*


### test_double_enter_raises (method, L294-L301, parent: TestPropertiesBeforeEntry)

> *Summary: This test verifies that attempting to enter a "once-only" task twice raises a `RuntimeError` containing the message "already entered". It achieves this by first successfully entering the task and then immediately trying to re-enter it within a `pytest.raises` context manager.*


### TestMetadata (class, L304-L316)

> *Summary: This test class verifies the metadata associated with tasks executed by an agent. It asserts that a specific owner ID is set for an ownership task and confirms that custom payloads are correctly passed through to the task's metadata.*


### test_owner_id_is_agent_name (method, L306-L310, parent: TestMetadata)

> *Summary: This test verifies that when an agent performs a specific task, the resulting task metadata correctly identifies the owner ID and matches the task's title. It asserts that `task.metadata.owner_id` is `"researcher"` and `task.metadata.spec.title` is `"ownership"`.*


### test_payload_passed_through (method, L313-L316, parent: TestMetadata)

> *Summary: This test verifies that a specified input payload, `{"capability": "search"}`, is correctly passed through and stored in the metadata of an agent task. It asserts that the task's specification contains the exact initial payload provided.*

