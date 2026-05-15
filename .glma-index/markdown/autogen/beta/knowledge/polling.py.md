# autogen/beta/knowledge/polling.py

1 class(es): PollingChangeWatcher. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PollingChangeWatcher | class |  |

## Chunks

### PollingChangeWatcher (class, L12-L88)

> *Summary: This class monitors a backend store for changes under a specified prefix by periodically polling it at a set interval. It initializes with a backend, prefix, and an asynchronous callback, then runs a loop that compares the current snapshot against the last known state, dispatching notifications to the callback whenever a key is added, modified, or deleted.*


### __init__ (method, L33-L47, parent: PollingChangeWatcher)

> *Summary: Initializes a polling mechanism by storing the data source backend, a string prefix, and a change callback. It also sets up an asynchronous task placeholder and configures the polling interval to be at least 0.05 seconds.*


### start (method, L49-L51, parent: PollingChangeWatcher)

> *Summary: Initializes the polling mechanism by fetching the latest version list from the backend for a given prefix and then starts an asynchronous background task to continuously monitor changes.*


### _run (method, L53-L72, parent: PollingChangeWatcher)

> *Summary: Periodically polls a backend for version updates under a specified prefix. It compares the fetched versions against a stored snapshot, triggering notifications for any new or deleted paths before updating its internal state.*


### _safe_fire (method, L74-L78, parent: PollingChangeWatcher)

> *Summary: This method asynchronously executes a registered callback function using a provided file path. It wraps the execution in a `try...except` block to ensure that any exceptions thrown by the callback do not halt the watching process.*


### close (method, L80-L88, parent: PollingChangeWatcher)

> *Summary: This method safely shuts down the polling mechanism by setting an internal closed flag and canceling any running background task. It ensures that if the task is canceled, it handles potential `CancelledError` exceptions gracefully before clearing the task reference.*

