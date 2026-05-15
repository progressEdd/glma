# autogen/agentchat/remote/retry.py

5 class(es): RetryPolicyManager, RetryPolicy, SleepRetryPolicy, _SleepRetryPolicy, NoRetryPolicy. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RetryPolicyManager | class |  |
| RetryPolicy | class |  |
| SleepRetryPolicy | class |  |
| _SleepRetryPolicy | class |  |
| NoRetryPolicy | class |  |

## Chunks

### RetryPolicyManager (class, L11-L26)

> *Summary: Defines a protocol for managing retry policies using asynchronous context manager methods. It dictates the interface for entering and exiting both synchronous and asynchronous contexts to control retry behavior during operations.*


### __enter__ (method, L12-L13, parent: RetryPolicyManager)

> *Summary: This context manager's entry method performs no operations, serving as a placeholder for resource setup before a `with` block executes. It simply allows the surrounding code to proceed into the protected section.*


### __aenter__ (method, L15-L16, parent: RetryPolicyManager)

> *Summary: This asynchronous context manager's entry method performs no operations upon entering the block. It is designed to manage a resource or state during an asynchronous operation.*


### __exit__ (method, L18-L21, parent: RetryPolicyManager)

> *Summary: This method handles the cleanup after an `with` block exits. It accepts exception details but currently performs no specific action, effectively allowing any exceptions to propagate normally.*


### __aexit__ (method, L23-L26, parent: RetryPolicyManager)

> *Summary: This asynchronous context manager exit method does nothing upon exiting the `async with` block. It accepts exception details but returns no value or boolean to signal further handling.*


### RetryPolicy (class, L29-L30)

> *Summary: Defines a protocol for retry policies, requiring an instance to be callable and return a `RetryPolicyManager`. This allows different implementations of retry logic to be used interchangeably.*


### __call__ (method, L30-L30, parent: RetryPolicy)

> *Summary: This method executes the retry policy manager, likely initiating a process to handle retries based on predefined rules. It returns an instance of `RetryPolicyManager` after execution.*


### SleepRetryPolicy (class, L33-L39)

> *Summary: This policy defines a mechanism to automatically re-attempt operations upon failure. It accepts a fixed interval and maximum count for retries, returning an instance of the concrete retry manager configured with these parameters.*


### __init__ (method, L34-L36, parent: SleepRetryPolicy)

> *Summary: Initializes a retry mechanism by setting the delay between attempts (`retry_interval`) and the maximum number of retries allowed (`retry_count`). These parameters control how often and how many times an operation will be reattempted upon failure.*


### __call__ (method, L38-L39, parent: SleepRetryPolicy)

> *Summary: This method constructs and returns a `SleepRetryPolicy` instance using the stored retry interval and count from the object's state. It effectively wraps the current policy configuration into an executable retry mechanism.*


### _SleepRetryPolicy (class, L42-L78)

> *Summary: This policy manages retries for operations by tracking error counts and pausing execution upon failure. It supports both synchronous (`__exit__`) and asynchronous (`__aexit__`) contexts, suppressing exceptions up to a configured retry limit after waiting the specified interval.*


### __init__ (method, L43-L46, parent: _SleepRetryPolicy)

> *Summary: Initializes a retry mechanism by setting the delay between attempts and the maximum number of retries allowed. It also initializes an internal counter to track the number of errors encountered during operations.*


### __enter__ (method, L48-L49, parent: _SleepRetryPolicy)

> *Summary: This context manager's entry method performs no operations, serving as a placeholder for resource acquisition before a `with` block executes. It simply allows the surrounding code to proceed into the protected section.*


### __aenter__ (method, L51-L52, parent: _SleepRetryPolicy)

> *Summary: When entering an asynchronous context, this method performs no operations. It is designed to be used within an `async with` block for resource management.*


### __exit__ (method, L54-L65, parent: _SleepRetryPolicy)

> *Summary: When an exception occurs, this method increments an error counter and checks if the current count is below a configured retry limit. If it is, it pauses execution for a set interval and returns `True` to suppress the exception, otherwise it allows it to propagate.*


### __aexit__ (method, L67-L78, parent: _SleepRetryPolicy)

> *Summary: When an asynchronous context manager exits due to an exception, this method increments an error counter and determines if the exception should be suppressed based on a configured retry limit. If suppression is warranted, it pauses execution for a set interval before allowing the outer scope to handle the failure.*


### NoRetryPolicy (class, L81-L102)

> *Summary: This class implements a policy that explicitly prevents any retries for operations. It acts as a context manager to wrap asynchronous and synchronous code blocks without altering their execution flow or handling exceptions internally.*


### __enter__ (method, L82-L83, parent: NoRetryPolicy)

> *Summary: When entering a context, this method performs no specific action. It is part of the setup for resource management within the class instance.*


### __aenter__ (method, L85-L86, parent: NoRetryPolicy)

> *Summary: When entering an asynchronous context, this method performs no operations. It is designed to be a placeholder for setup logic within an async context manager.*


### __aexit__ (method, L88-L94, parent: NoRetryPolicy)

> *Summary: This asynchronous context manager exit method does nothing upon exiting the `async with` block. It accepts exception details but returns no value or boolean to control propagation.*


### __exit__ (method, L96-L102, parent: NoRetryPolicy)

> *Summary: This method handles the cleanup after an exception block exits. It accepts exception details and returns `None` to allow exceptions to propagate normally.*

