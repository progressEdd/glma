# autogen/io/step_controller.py

2 class(es): StepController, AsyncStepController. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| StepController | class |  |
| AsyncStepController | class |  |

## Chunks

### StepController (class, L16-L55)

> *Summary: Manages synchronous, step-by-step execution by controlling when a background producer blocks after sending an event. It accepts optional event types to filter which events require manual acknowledgment via the `step()` method from the consumer.*


### __init__ (method, L26-L29, parent: StepController)

> *Summary: Initializes the controller by optionally setting a list of event types to trigger yielding and sets up internal synchronization primitives for state management. It stores these configured events in `self._yield_on` and initializes thread safety mechanisms like `threading.Event`.*


### should_block (method, L31-L39, parent: StepController)

> *Summary: Determines whether to pause execution based on an incoming event. It returns `False` if the controller is terminated, otherwise it yields for all events unless a specific type filter (`self._yield_on`) is set, in which case it only yields for matching types.*


### wait_for_step (method, L41-L46, parent: StepController)

> *Summary: This method blocks execution until a specific step event is signaled, provided the associated condition check permits blocking. It clears and then waits on an internal synchronization primitive (`_step_event`) if `should_block` returns true for the given input event.*


### step (method, L48-L50, parent: StepController)

> *Summary: Signals the controller to proceed to the subsequent event in its sequence. This method is called externally and sets an internal synchronization primitive.*


### terminate (method, L52-L55, parent: StepController)

> *Summary: Sets an internal flag to indicate termination and signals a waiting event, effectively unblocking any producers that are waiting for the controller to shut down.*


### AsyncStepController (class, L58-L95)

> *Summary: Manages sequential execution flow by pausing a background producer until an external consumer explicitly calls `step()` to acknowledge the current event. It uses an internal `asyncio.Event` to block producers based on whether specific event types are configured for yielding.*


### __init__ (method, L68-L71, parent: AsyncStepController)

> *Summary: Initializes the controller by optionally setting a list of event types to monitor for yielding, creating an `asyncio.Event` for signaling, and setting a termination flag to false.*


### should_block (method, L73-L79, parent: AsyncStepController)

> *Summary: Determines whether the controller should pause execution based on an incoming event. It returns `False` if already terminated, otherwise it blocks unless a specific yield type is set and the event does not match that type.*


### wait_for_step (method, L81-L86, parent: AsyncStepController)

> *Summary: This asynchronous method pauses execution until a specific step event is signaled, provided the internal logic dictates blocking based on the input event. It clears and then awaits a dedicated step event to synchronize producer-consumer flow.*


### step (method, L88-L90, parent: AsyncStepController)

> *Summary: Signals the controller to proceed to the next state or event within its workflow. This method is called externally and sets an internal synchronization primitive (`_step_event`).*


### terminate (method, L92-L95, parent: AsyncStepController)

> *Summary: Sets an internal flag to signal termination and triggers a condition variable event, effectively unblocking any waiting producers during a controlled shutdown sequence.*

