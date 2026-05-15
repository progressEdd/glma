# autogen/fast_depends/utils.py

13 function(s): asyncify, run_async, run_in_threadpool, solve_generator_async, solve_generator_sync, get_typed_signature, collect_outer_stack_locals, get_typed_annotation, contextmanager_in_threadpool, is_gen_callable and 3 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| asyncify | function |  |
| run_async | function |  |
| run_in_threadpool | function |  |
| solve_generator_async | function |  |
| solve_generator_sync | function |  |
| get_typed_signature | function |  |
| collect_outer_stack_locals | function |  |
| get_typed_annotation | function |  |
| contextmanager_in_threadpool | function |  |
| is_gen_callable | function |  |
| is_async_gen_callable | function |  |
| is_coroutine_callable | function |  |
| async_map | function |  |

## Chunks

### asyncify (function, L29-L36)

> *Summary: Wraps a synchronous function to make it awaitable by executing it in a separate thread pool. It returns the original function if it is already an asynchronous coroutine callable.*


### run_async (function, L39-L47)

> *Summary: Executes a given callable asynchronously, automatically handling whether the function is a coroutine or a standard synchronous function. It returns the result of the execution after awaiting the appropriate mechanism (direct await for coroutines or thread pool execution for sync functions).*


### run_in_threadpool (function, L50-L53)

> *Summary: Executes a synchronous function in a separate thread using `anyio.to_thread.run_sync`. It accepts the callable and its arguments, optionally pre-binding keyword arguments to the function before execution.*


### solve_generator_async (function, L56-L63)

> *Summary: This function asynchronously manages context managers based on the provided callable type. It executes synchronous or asynchronous generators within appropriate threadpool or native async contexts before yielding control to the caller via an `AsyncExitStack`.*


### solve_generator_sync (function, L66-L68)

> *Summary: This function synchronously executes a provided callable within a managed context using an `ExitStack`. It takes arguments and values to pass to the call and returns the context manager's entry point.*


### get_typed_signature (function, L71-L98)

> *Summary: This utility extracts a fully typed function signature and its return type from a callable input. It resolves parameter annotations by inspecting the calling scope's local variables and global namespace to ensure accurate type resolution.*


### collect_outer_stack_locals (function, L101-L114)

> *Summary: Gathers local variables from the call stack, excluding frames originating within the `fast_depends` module. It returns a dictionary containing all collected local variables from outer scopes in reverse order of execution.*


### get_typed_annotation (function, L117-L132)

> *Summary: This utility recursively resolves type annotations by handling string-based `ForwardRef`s and unpacking `Annotated` types. It takes an annotation, global namespace, and local scope as input, returning the fully resolved type object.*


### contextmanager_in_threadpool (function, L136-L147)

> *Summary: This asynchronous utility wraps a context manager to execute its setup and teardown logic within a thread pool. It yields the entered resource while managing exceptions by attempting to run the exit method in the threadpool, ensuring proper cleanup even upon failure.*


### is_gen_callable (function, L150-L154)

> *Summary: Checks if a given callable is a generator function or if its `__call__` attribute points to one. It returns `True` if the input callable behaves as a generator factory.*


### is_async_gen_callable (function, L157-L161)

> *Summary: Checks if a given callable is an asynchronous generator function or if its `__call__` method is one. It returns `True` if the input or its call method matches this specific signature.*


### is_coroutine_callable (function, L164-L172)

> *Summary: Checks if a given callable is an asynchronous function by first excluding classes and then inspecting the callable itself or its `__call__` method for coroutine behavior. Returns `True` if it's a coroutine-based callable, otherwise `False`.*


### async_map (function, L175-L177)

> *Summary: This asynchronous utility applies a given function to every item yielded by an asynchronous iterable. It processes the input items sequentially and yields the results asynchronously.*

