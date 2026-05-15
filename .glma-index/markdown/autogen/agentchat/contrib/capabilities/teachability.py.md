# autogen/agentchat/contrib/capabilities/teachability.py

2 class(es): Teachability, MemoStore. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Teachability | class |  |
| MemoStore | class |  |

## Chunks

### Teachability (class, L23-L240)

> *Summary: Provides an agent capability that uses a vector database to allow agents to learn and recall user-provided knowledge from conversations. It hooks into message processing to both store new teachings (as question/answer or task/advice pairs) and retrieve relevant memories to augment the current message context before sending it to the agent.*


### __init__ (method, L39-L67, parent: Teachability)

> *Summary: Initializes a teachability component by setting configuration parameters like verbosity, database path, and retrieval limits. It then instantiates a `MemoStore` to manage the agent's knowledge base based on these inputs.*


### add_to_agent (method, L69-L89, parent: Teachability)

> *Summary: This method integrates teachability into a specified agent by setting it as the agent's reference, registering a message processing hook, and configuring an internal `TextAnalyzerAgent`. It ensures the agent has an LLM configuration and modifies the agent's system message to enable memory of user teachings.*


### prepopulate_db (method, L91-L93, parent: Teachability)

> *Summary: Initializes the memo store by adding several predefined entries into the database. This method ensures the system has some initial data available for testing or demonstration purposes.*


### process_last_received_message (method, L95-L108, parent: Teachability)

> *Summary: This method enriches an incoming message by first retrieving relevant past memos from storage if available, and then analyzes the message to store any new teachings as future memos. It returns the potentially augmented message content.*


### _consider_memo_storage (method, L110-L166, parent: Teachability)

> *Summary: Determines if a user comment contains actionable advice or new knowledge by querying the agent's analysis capabilities. It extracts problem-solution pairs or question-answer pairs from the input and stores them in a vector database, saving changes to disk if any memos were added.*


### _consider_memo_retrieval (method, L168-L199, parent: Teachability)

> *Summary: Determines if relevant knowledge should be retrieved from a database based on an input comment. It first searches using the comment directly, and if the comment implies a task, it extracts and generalizes that task to perform a secondary memo retrieval before returning the original comment augmented with all found memos.*


### _retrieve_relevant_memos (method, L201-L217, parent: Teachability)

> *Summary: Retrieves semantically related memos from a database based on an input string, using configured limits and thresholds. If no relevant memos are found, it prints a warning and displays the single closest memo to the user.*


### _concatenate_memo_texts (method, L219-L229, parent: Teachability)

> *Summary: Combines a list of memory strings into one formatted string, prefixed with a header. It returns this concatenated text to be included in the chat context, optionally printing a notification if verbosity is enabled.*


### _analyze (method, L231-L240, parent: Teachability)

> *Summary: This method delegates text analysis to a specialized agent by first sending the input text and then sending specific instructions for that analysis. It returns the content of the final response received from the analyzer agent.*


### MemoStore (class, L244-L393)

> *Summary: This class manages persistent memory for a teachable agent by storing input/output pairs as vectors in a ChromaDB instance. It allows adding new memoized examples, retrieving the nearest or related memories based on a query text and distance threshold, and persisting all data to disk upon initialization or reset.*


### __init__ (method, L252-L288, parent: MemoStore)

> *Summary: Initializes a teachability agent by setting verbosity and database paths, then loads or creates a persistent ChromaDB collection for memories. It optionally loads an associated memo dictionary from disk based on the `reset` flag before finalizing setup.*


### list_memos (method, L290-L300, parent: MemoStore)

> *Summary: This method iterates over the stored memo dictionary, printing a formatted list of all entries. For each entry, it displays the unique ID along with its associated input and output texts to the console.*


### _save_memos (method, L302-L305, parent: MemoStore)

> *Summary: Persists the agent's internal text dictionary (`self.uid_text_dict`) to a specified file path using Python's `pickle` module for serialization. This method ensures that learned or recorded information is saved to disk upon execution.*


### reset_db (method, L307-L313, parent: MemoStore)

> *Summary: This method clears all existing data from the in-memory and disk database by deleting the "memos" collection and then recreating it. It also resets internal state variables, including a dictionary used for storing user IDs and text.*


### add_input_output_pair (method, L315-L328, parent: MemoStore)

> *Summary: This method stores a new input-output example by adding the input text to the vector database and saving both texts in an internal dictionary, incrementing a memo ID for tracking. It optionally prints confirmation details or lists all stored memos based on verbosity settings.*


### get_nearest_memo (method, L330-L343, parent: MemoStore)

> *Summary: Retrieves the most semantically similar memory pair from a vector database based on an input query string. It returns the original input text, the corresponding output text, and the similarity distance found in the database.*


### get_related_memos (method, L345-L365, parent: MemoStore)

> *Summary: This method queries a vector database using a text query to find related memo pairs based on a specified similarity threshold and maximum result count. It returns a list of tuples containing the input text, corresponding output text, and the calculated distance for each retrieved memo that meets the criteria.*


### prepopulate (method, L367-L393, parent: MemoStore)

> *Summary: This method injects a predefined set of sample input-output pairs into the vector database for initial testing and retrieval demonstration. It iterates over hardcoded examples, calling `add_input_output_pair` for each one before saving the memory state.*

