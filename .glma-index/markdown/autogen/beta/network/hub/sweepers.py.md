# autogen/beta/network/hub/sweepers.py

1 class(es): _IntervalSweeper. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _IntervalSweeper | class |  |

## Chunks

### _IntervalSweeper (class, L22-L76)

> *Summary: This class manages a recurring background task that executes a provided coroutine at a fixed interval. It starts the loop by spawning an asyncio task and safely stops it by cancelling the running task, ensuring exceptions within the executed function do not terminate the sweeper itself.*


### __init__ (method, L29-L40, parent: _IntervalSweeper)

> *Summary: Initializes a sweeper object by storing its unique name, the execution frequency, and the asynchronous function to run periodically. It sets up internal state variables for managing the running task and stopping condition.*


### name (method, L43-L44, parent: _IntervalSweeper)

> *Summary: Returns the internal name attribute of the object as a string. This method provides a direct accessor for the instance's designated name.*


### start (method, L46-L50, parent: _IntervalSweeper)

> *Summary: Initiates the sweeper's main asynchronous loop if it hasn't already been started, ensuring idempotency by checking for an existing task before creating a new one.*


### _loop (method, L52-L66, parent: _IntervalSweeper)

> *Summary: This asynchronous method runs in a continuous loop, periodically executing a provided function (`self._fn`) after an interval delay. It gracefully handles cancellation requests and swallows any exceptions during the execution of the main task to ensure the loop itself remains active.*


### stop (method, L68-L76, parent: _IntervalSweeper)

> *Summary: Sets an internal flag to signal termination and then cancels the associated asynchronous task. It safely awaits the cancellation of that task, ensuring cleanup by setting the task reference to `None` afterward.*

