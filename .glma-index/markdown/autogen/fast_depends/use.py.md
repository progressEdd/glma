# autogen/fast_depends/use.py

5 function(s): Depends, inject, inject, inject, _wrap_inject. 3 class(es): _InjectWrapper, solve_async_gen, solve_gen. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Depends | function |  |
| _InjectWrapper | class |  |
| inject | function |  |
| inject | function |  |
| inject | function |  |
| _wrap_inject | function |  |
| solve_async_gen | class |  |
| solve_gen | class |  |

## Chunks

### Depends (function, L29-L39)

> *Summary: Wraps a callable dependency function to integrate it with the underlying `model.Depends` mechanism. It accepts the dependency function and optional boolean flags for caching and type casting before returning the configured dependency object.*


### _InjectWrapper (class, L42-L47)

> *Summary: This protocol defines a wrapper that accepts a function and an optional model. Its primary purpose is to return a new callable version of the input function, likely for dependency injection or modification.*


### __call__ (method, L43-L47, parent: _InjectWrapper)

> *Summary: This method wraps a given function, optionally using a specified model. It returns a new callable that incorporates the dependency resolution logic of the wrapper around the original function.*


### inject (function, L51-L59)

> *Summary: This function wraps a target callable to inject dependencies into it. It accepts the function itself and optional parameters like dependency definitions, configuration settings, and override providers to manage how inputs are supplied during execution.*


### inject (function, L63-L71)

> *Summary: This function wraps an existing callable to inject dependencies into it. It accepts the target function and various configuration options like dependency overrides and model wrapping to customize how dependencies are resolved and applied.*


### inject (function, L74-L95)

> *Summary: This function acts as a decorator factory that wraps a target callable to inject dependencies. It accepts configuration parameters like extra dependencies and casting behavior, returning either the wrapper itself or the decorated function.*


### _wrap_inject (function, L98-L178)

> *Summary: This function wraps a callable to inject dependencies into its execution context. It takes dependency overrides and configuration details as input, returning a wrapper that executes the original function using an internally constructed model, handling both synchronous and asynchronous execution paths.*


### solve_async_gen (class, L181-L225)

> *Summary: This asynchronous generator wraps a `CallModel` to iteratively resolve dependencies for a given model call. It yields results from the underlying solver until the iteration is complete, managing necessary async resources via an exit stack.*


### __init__ (method, L184-L194, parent: solve_async_gen)

> *Summary: Initializes the object by storing a specified call model, along with any positional arguments, keyword arguments, and optional configuration overrides. It sets up the necessary components to execute or manage a particular function call.*


### __aiter__ (method, L196-L199, parent: solve_async_gen)

> *Summary: This asynchronous iteration method initializes the internal state by resetting the iterator and setting up an `AsyncExitStack` to manage asynchronous cleanup resources before returning itself as the async iterator.*


### __anext__ (method, L201-L225, parent: solve_async_gen)

> *Summary: This method drives the asynchronous iteration by first initializing an iterator via a call to `self.call` if one hasn't been established. It then repeatedly awaits the next item from this underlying iterator until `StopAsyncIteration` is raised, ensuring proper cleanup of resources upon completion or error.*


### solve_gen (class, L228-L272)

> *Summary: This generator class wraps a model's `solve` method to iteratively yield results from its dependency resolution process. It manages the execution context using an `ExitStack`, allowing consumers to pull successive resolved items until the underlying iterator is exhausted.*


### __init__ (method, L231-L241, parent: solve_gen)

> *Summary: Initializes an object by storing a specified call model, along with any positional arguments, keyword arguments, and optional configuration overrides. It sets up the necessary components to execute or manage a particular function call based on the provided inputs.*


### __iter__ (method, L243-L246, parent: solve_gen)

> *Summary: This method initializes an internal iterator state and sets up a stack context manager to manage the iteration process for dependency resolution. It returns `self`, allowing the object itself to be used in a `for` loop.*


### __next__ (method, L248-L272, parent: solve_gen)

> *Summary: This method acts as an iterator for dependency resolution, yielding results from a solver call if the internal iterator hasn't been initialized. It manages resource cleanup by using an `ExitStack` upon iteration completion or failure.*

