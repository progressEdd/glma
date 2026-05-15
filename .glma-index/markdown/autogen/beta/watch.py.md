# autogen/beta/watch.py

1 function(s): _parse_cron_field. 10 class(es): Watch, _BaseWatch, EventWatch, CadenceWatch, IntervalWatch, DelayWatch, AllOf, AnyOf, Sequence, CronWatch. 44 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Watch | class |  |
| _BaseWatch | class |  |
| EventWatch | class |  |
| CadenceWatch | class |  |
| IntervalWatch | class |  |
| DelayWatch | class |  |
| AllOf | class |  |
| AnyOf | class |  |
| Sequence | class |  |
| _parse_cron_field | function |  |
| CronWatch | class |  |

## Chunks

### Watch (class, L33-L48)

> *Summary: Defines a protocol for a condition that monitors a stream, allowing it to be activated (`arm`) with a callback function and subsequently deactivated (`disarm`). It provides properties to identify the watch and check its current armed state.*


### id (method, L37-L37, parent: Watch)

> *Summary: Returns a unique string identifier for the instance. This method provides a consistent way to reference the object within the system.*


### arm (method, L39-L41, parent: Watch)

> *Summary: Initiates event monitoring by subscribing to necessary streams or setting up internal timers based on the provided `Stream` and `WatchCallback`. This method begins the active observation process for the object.*


### disarm (method, L43-L45, parent: Watch)

> *Summary: This method stops the active monitoring process by cleaning up all associated subscriptions and timers. It takes no input and returns nothing, effectively halting observation.*


### is_armed (method, L48-L48, parent: Watch)

> *Summary: Checks the current armed status of an object, returning a boolean indicating whether it is active or not.*


### _BaseWatch (class, L51-L73)

> *Summary: Provides a foundational structure for monitoring mechanisms, initializing with a unique ID and tracking subscription/streaming state. It allows disabling the watch by unsubscribing from any active stream and resetting its armed status.*


### __init__ (method, L54-L58, parent: _BaseWatch)

> *Summary: Initializes an object by generating a unique hexadecimal ID and setting internal state variables for subscription, stream reference, and armed status to their default values. These attributes are used to manage the lifecycle and state of a watched entity.*


### id (method, L61-L62, parent: _BaseWatch)

> *Summary: Returns the unique identifier string associated with the instance. This method provides direct access to the internal `_id` attribute.*


### is_armed (method, L65-L66, parent: _BaseWatch)

> *Summary: Returns a boolean indicating the current armed state of the object by accessing an internal attribute.*


### disarm (method, L68-L73, parent: _BaseWatch)

> *Summary: This method stops monitoring by unsubscribing from the current stream using its subscription ID, then resets both the subscription ID and the stream reference to `None`, finally setting the armed state to false.*


### EventWatch (class, L76-L100)

> *Summary: This class monitors an event stream for events matching a specified condition. When a match occurs, it immediately invokes a provided callback function with the matching event and context.*


### __init__ (method, L85-L90, parent: EventWatch)

> *Summary: Initializes a watcher by accepting either a `Condition` object or a class type; it wraps the input into a `TypeCondition` if necessary and stores this as the internal monitoring criterion. It also initializes an optional callback mechanism for when the condition is met.*


### arm (method, L92-L96, parent: EventWatch)

> *Summary: Sets up event watching by storing the provided stream and callback, then subscribes to the stream using a specific handler and condition. This action activates the watcher, setting an internal armed state to true.*


### _handle_event (method, L98-L100, parent: EventWatch)

> *Summary: When an event occurs, this method invokes a registered callback function, passing the received event and the current context to it. It ensures that the callback execution only proceeds if one has been set.*


### CadenceWatch (class, L103-L189)

> *Summary: This class monitors an event stream, batching events based on either a fixed count ($\text{n}$) or a maximum time interval ($\text{max\_wait}$), or both. It buffers incoming $\text{BaseEvent}$ objects and triggers a callback when the specified condition is met, ensuring at least one of the batching criteria is set during initialization.*


### __init__ (method, L119-L140, parent: CadenceWatch)

> *Summary: Initializes a watch mechanism that requires either a positive cadence interval (`n`) or a maximum wait time (`max_wait`). It sets up internal state, including optional condition checking and an event buffer, preparing for asynchronous monitoring.*


### arm (method, L142-L146, parent: CadenceWatch)

> *Summary: Sets up the internal state by storing a `Stream` and a `WatchCallback`, then subscribes to the stream's cadence events using a specific condition to enable monitoring. This action effectively arms the watcher mechanism.*


### _handle_cadence_event (method, L148-L156, parent: CadenceWatch)

> *Summary: This method buffers incoming events and, if the buffer reaches a predefined count ($\text{self.\_n}$), it immediately fires an event after canceling any active timer. Otherwise, it starts or ensures a background timer task to fire an event after a maximum waiting period ($\text{self.\_max\_wait}$) if one isn't already running.*


### _wait_and_fire (method, L158-L171, parent: CadenceWatch)

> *Summary: This asynchronous method periodically waits for a specified duration, then fires buffered events if data exists. It continuously loops until the buffer is empty or the task is cancelled, ensuring all pending stream events are processed.*


### _fire (method, L173-L178, parent: CadenceWatch)

> *Summary: When a buffer contains data and a callback is set, this method extracts all buffered items into a batch, clears the internal buffer, and asynchronously invokes the registered callback with the collected batch and context.*


### _cancel_timer (method, L180-L183, parent: CadenceWatch)

> *Summary: This method safely stops an active background timer task by calling `cancel()` on the stored task object and then resetting the reference to `None`. It ensures that only a valid, non-null timer task is attempted for cancellation.*


### disarm (method, L185-L189, parent: CadenceWatch)

> *Summary: Stops any active timers and clears internal buffers, then resets the callback mechanism before calling the parent class's disarm method. This effectively halts all ongoing operations managed by the object.*


### IntervalWatch (class, L192-L228)

> *Summary: This class periodically triggers a callback function at a specified time interval. It takes an initial delay in seconds and, when armed with a stream and callback, runs an asynchronous loop that wakes up every $\text{seconds}$ to execute the provided watcher logic. Disarming cancels the running background task.*


### __init__ (method, L200-L205, parent: IntervalWatch)

> *Summary: Initializes the watcher with a specified duration in seconds, setting up internal state for an asynchronous task, a callback handler, and execution context. This object is designed to monitor or wait for events over the provided time interval.*


### arm (method, L207-L211, parent: IntervalWatch)

> *Summary: Sets up the internal state to monitor a given `Stream` using a provided `WatchCallback`. It immediately starts an asynchronous background task to execute the monitoring logic.*


### _run (method, L213-L221, parent: IntervalWatch)

> *Summary: Periodically executes a registered callback function by sleeping for a configured interval and then invoking the provided callback with context derived from the stream. It handles potential exceptions during the callback execution, logging any failures encountered.*


### disarm (method, L223-L228, parent: IntervalWatch)

> *Summary: Cancels any active task associated with the object and clears its callback handler. This method effectively stops ongoing operations managed by the instance.*


### DelayWatch (class, L231-L264)

> *Summary: This class schedules a callback to execute once after a specified delay. It takes a stream and a callback, starts an asynchronous task that waits for the duration, then invokes the callback with context before automatically disarming itself.*


### __init__ (method, L239-L242, parent: DelayWatch)

> *Summary: Initializes the object by storing a specified duration in seconds and setting up an internal placeholder for an asynchronous task. This sets the necessary parameters for subsequent scheduling or monitoring operations.*


### arm (method, L244-L247, parent: DelayWatch)

> *Summary: Sets the internal stream and flags the watcher as active, then initiates an asynchronous background task to run the core watching logic using the provided stream and callback.*


### _run (method, L249-L258, parent: DelayWatch)

> *Summary: After a specified delay, this method executes the provided callback with an empty list and a context object derived from the stream. It ensures that the watch mechanism is automatically disabled upon completion or if any exception occurs during execution.*


### disarm (method, L260-L264, parent: DelayWatch)

> *Summary: Cancels any active background task associated with the object and then calls the parent class's disarm method. This ensures that ongoing operations are stopped when the object is shut down.*


### AllOf (class, L267-L311)

> *Summary: This class monitors a set of input watches and triggers its callback only when every single sub-watch has fired at least once since the last trigger. It aggregates all events from the firing sub-watches into a combined list before invoking the provided callback.*


### __init__ (method, L278-L283, parent: AllOf)

> *Summary: Initializes the watcher with a variable number of `Watch` objects and sets up internal state to track fired events, buffer incoming events, and hold an optional callback function. This structure allows the object to monitor multiple sources and process asynchronous event notifications.*


### arm (method, L285-L292, parent: AllOf)

> *Summary: Sets up the watcher to monitor a specific stream and callback, clearing previous state before enabling all registered sub-watches on that stream. This prepares the object for receiving events from the provided `Stream`.*


### _handle_sub_watch (method, L294-L303, parent: AllOf)

> *Summary: When a new event arrives for a specific watch ID, this method buffers the events and marks that watch as fired. If all registered watches have reported at least one event, it aggregates all buffered events across all watches and executes a callback function with the combined list.*


### disarm (method, L305-L311, parent: AllOf)

> *Summary: This method stops all associated watches by calling `disarm()` on each one, then clears internal state buffers and callbacks before invoking the parent class's disarm logic. It effectively halts the monitoring process managed by the object.*


### AnyOf (class, L314-L345)

> *Summary: This class aggregates multiple sub-watches and triggers its own callback as soon as *any* of the constituent watches fire an event. It manages the lifecycle by arming all internal watches to report to a unified handler, which then invokes the provided callback if set.*


### __init__ (method, L325-L328, parent: AnyOf)

> *Summary: Initializes the object by storing a variable number of `Watch` instances and setting an optional callback function. This sets up the necessary components for monitoring events or changes within the system.*


### arm (method, L330-L335, parent: AnyOf)

> *Summary: Sets the internal stream and callback handlers for watching events. It then iterates through all registered watches, activating each one to report any detected changes back to a designated handler method.*


### _handle_any (method, L337-L339, parent: AnyOf)

> *Summary: This method executes a registered callback function if one exists. It takes a list of `BaseEvent` objects and a `Context` object as input to pass to the callback.*


### disarm (method, L341-L345, parent: AnyOf)

> *Summary: This method iterates through all registered watches and calls their `disarm()` method, then clears the internal callback before invoking the parent class's disarm logic. It effectively stops all associated monitoring activities.*


### Sequence (class, L348-L410)

> *Summary: This class monitors a series of input watches, executing them strictly one after the other. When all constituent watches fire in sequence, it invokes a provided callback with all collected events and then automatically resets to monitor the sequence again.*


### __init__ (method, L363-L368, parent: Sequence)

> *Summary: Initializes the object by accepting a variable number of `Watch` instances, storing them internally. It sets up internal state including an index tracker, an optional callback function, and a list to accumulate all received events.*


### arm (method, L370-L376, parent: Sequence)

> *Summary: Sets up the watcher to monitor a specific `Stream` and execute actions via a `WatchCallback`. It initializes internal state, clears previous event history, and immediately begins monitoring by calling an internal arming method.*


### _arm_current (method, L378-L382, parent: Sequence)

> *Summary: If the watcher is armed and a stream exists, this method activates the watch at the current index using the provided stream and step handler. It ensures that arming only occurs if the current index is within the bounds of the stored watches.*


### _step_handler (method, L384-L402, parent: Sequence)

> *Summary: When triggered with a list of events and context, this method processes the next watch in sequence if armed. It disarms the current watch, advances the index, and either re-arms the next watch or executes a registered callback after all watches have fired sequentially.*


### disarm (method, L404-L410, parent: Sequence)

> *Summary: This method iterates through all registered watches, calling `disarm()` on each one to stop their monitoring. It then resets the internal state by clearing event logs and callbacks before invoking the parent class's disarm logic.*


### _parse_cron_field (function, L416-L432)

> *Summary: Parses a string specification representing cron field values, handling wildcards (`*`), ranges (`-`), steps (`/`), and optional day-of-week names. It returns a set of integers corresponding to the valid time points within the specified minimum and maximum bounds.*


### CronWatch (class, L435-L512)

> *Summary: This class schedules an asynchronous callback to execute based on a standard 5-field cron expression string. It continuously calculates the next matching time from the current moment and sleeps until that time, invoking the provided callback when the schedule is met.*


### __init__ (method, L447-L451, parent: CronWatch)

> *Summary: Initializes a watcher object by storing an input string expression and setting up internal state for managing asynchronous tasks and callbacks. It prepares the instance to monitor changes based on the provided expression.*


### arm (method, L453-L457, parent: CronWatch)

> *Summary: Sets up the internal state to monitor a given `Stream` using a provided `WatchCallback`. It immediately starts an asynchronous background task to execute the monitoring logic.*


### _run (method, L459-L471, parent: CronWatch)

> *Summary: Continuously monitors time to execute a registered callback at predefined intervals. It calculates the necessary delay until the next scheduled execution and then invokes the provided asynchronous callback with the current stream context if one is set.*


### _next_fire_time (method, L473-L505, parent: CronWatch)

> *Summary: Calculates the next scheduled execution time based on a five-field cron expression and a provided current time. It iterates minute by minute forward from one minute after the input time, checking if each candidate matches all specified minute, hour, day of month, month, and day of week constraints; otherwise, it returns a fallback time one hour later.*


### disarm (method, L507-L512, parent: CronWatch)

> *Summary: Cancels any active task associated with the object and clears its callback handler. This method effectively stops ongoing operations managed by the instance.*

