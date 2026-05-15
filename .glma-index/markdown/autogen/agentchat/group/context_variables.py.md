# autogen/agentchat/group/context_variables.py

1 class(es): ContextVariables. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContextVariables | class |  |

## Chunks

### ContextVariables (class, L18-L182)

> *Summary: This class provides a dictionary-like interface for managing and accessing state variables within agentic workflows. It allows setting, getting, removing, and iterating over context data, supporting initialization from an existing dictionary.*


### __init__ (method, L27-L35, parent: ContextVariables)

> *Summary: Initializes an instance by accepting an optional dictionary of context variables. It merges this input with any additional keyword arguments passed to its parent class constructor.*


### get (method, L37-L47, parent: ContextVariables)

> *Summary: Retrieves a specific value from the internal data store using a provided string key. It returns the stored value if present, otherwise it returns an optional specified default value.*


### set (method, L49-L56, parent: ContextVariables)

> *Summary: This method updates an internal data dictionary by associating a given `value` with a specified string `key`. It allows for the dynamic storage and retrieval of context information within the object.*


### remove (method, L58-L70, parent: ContextVariables)

> *Summary: Removes a specified key from the internal data store; returns `True` if the key existed and was deleted, or `False` otherwise.*


### keys (method, L72-L78, parent: ContextVariables)

> *Summary: Retrieves an iterable containing every key present within the agent's internal data structure. This method provides a complete list of available context identifiers.*


### values (method, L80-L86, parent: ContextVariables)

> *Summary: Retrieves an iterable containing every value stored within the agent's internal data dictionary. This method provides read-only access to all associated contextual information.*


### items (method, L88-L94, parent: ContextVariables)

> *Summary: Provides an iterable view of all stored context data as key-value tuples. It accesses and returns the contents of the internal `self.data` dictionary.*


### clear (method, L96-L98, parent: ContextVariables)

> *Summary: Resets the internal state by emptying all stored data within the object's context dictionary. This method takes no input and produces no output, effectively wiping the current session's memory.*


### contains (method, L100-L109, parent: ContextVariables)

> *Summary: Checks for the presence of a specified string key within the object's internal data dictionary. It returns `True` if the key is found and `False` otherwise.*


### update (method, L111-L117, parent: ContextVariables)

> *Summary: Merges the provided dictionary's key-value pairs into the instance's internal data store, effectively updating the context with new information. This method takes a dictionary as input and modifies the object in place without returning a value.*


### to_dict (method, L119-L125, parent: ContextVariables)

> *Summary: Converts the internal data structure holding context variables into a standard Python dictionary. It returns a copy of this data, ensuring the original object remains unmodified.*


### __getitem__ (method, L128-L133, parent: ContextVariables)

> *Summary: Retrieves a stored value from the internal data structure using a string key, raising a `KeyError` if the specified context variable does not exist.*


### __setitem__ (method, L135-L137, parent: ContextVariables)

> *Summary: Allows setting or updating specific data points within the context object using standard dictionary assignment syntax (`context[key] = value`). It directly stores the provided key-value pair into the internal `data` structure.*


### __delitem__ (method, L139-L144, parent: ContextVariables)

> *Summary: Allows removal of a specific context variable from the internal data store using dictionary syntax (`del context[key]`). It raises a `KeyError` if the requested key does not exist in the current context.*


### __contains__ (method, L146-L148, parent: ContextVariables)

> *Summary: Determines membership within the agent's data store by checking if a provided string key exists in its internal dictionary. Returns `True` if the key is present, and `False` otherwise.*


### __len__ (method, L150-L152, parent: ContextVariables)

> *Summary: Returns the total count of stored data items within the context object. This method allows for checking the size of the context using `len()`.*


### __iter__ (method, L154-L157, parent: ContextVariables)

> *Summary: This method allows iteration over the internal data dictionary, yielding each key paired with its corresponding value as a tuple. It effectively exposes all stored context variables for sequential access.*


### __str__ (method, L159-L161, parent: ContextVariables)

> *Summary: Provides a string representation of the `ContextVariables` object by formatting its internal data dictionary. This method is used for debugging and logging purposes, returning a descriptive string like "ContextVariables({...})".*


### __repr__ (method, L163-L165, parent: ContextVariables)

> *Summary: Provides a detailed string representation of the object, showing its internal `data` attribute using its official representation. This is useful for debugging and logging purposes.*


### from_dict (method, L169-L182, parent: ContextVariables)

> *Summary: Instantiates a `ContextVariables` object by accepting a dictionary as input. It uses the provided data to initialize and return a new instance of the class.*

