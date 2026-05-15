# autogen/coding/remyx_code_executor.py

2 class(es): RemyxCodeResult, RemyxCodeExecutor. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RemyxCodeResult | class |  |
| RemyxCodeExecutor | class |  |

## Chunks

### RemyxCodeResult (class, L83-L87)

> *Summary: This class extends `CodeResult` to hold specific metadata about a code execution performed by the Remyx executor. It stores optional fields for an associated arXiv ID and the corresponding paper title.*


### RemyxCodeExecutor (class, L91-L576)

> *Summary: This class executes research paper code by leveraging Docker containers, fetching necessary metadata and images from the Remyx API based on an arXiv ID or a provided image name. It supports interactive exploration via two AI agents—one for execution and one for reasoning—allowing users to run and understand complex scientific code locally.*


### __init__ (method, L148-L225, parent: RemyxCodeExecutor)

> *Summary: Initializes the code execution environment by optionally fetching Docker image and metadata from a provided arXiv ID using RemyxAI. It configures container settings, merges user-provided environment variables with those derived from the asset metadata, and then calls the parent executor's constructor.*


### code_extractor (method, L228-L230, parent: RemyxCodeExecutor)

> *Summary: Provides an instance of `MarkdownCodeExtractor` for external use. This method returns the configured code extraction utility to agents.*


### paper_info (method, L233-L235, parent: RemyxCodeExecutor)

> *Summary: Retrieves the stored asset metadata as a dictionary, or returns `None` if no metadata is present. This method accesses and exposes internal metadata associated with the object instance.*


### execute_code_blocks (method, L237-L295, parent: RemyxCodeExecutor)

> *Summary: Processes a list of `CodeBlock` objects by saving each block to a file with the correct extension and executing it using a containerized command. It returns a result containing the final exit code, aggregated output, and the path to the first executed file.*


### get_paper_context (method, L297-L318, parent: RemyxCodeExecutor)

> *Summary: Retrieves a formatted string containing metadata about the associated paper, including title, arXiv ID, GitHub link, and working directory. It optionally appends reasoning and quickstart hints if they exist in the asset metadata.*


### _build_system_message (method, L320-L346, parent: RemyxCodeExecutor)

> *Summary: Constructs the comprehensive system prompt for exploration agents by combining a paper context, a specified mission goal, and default guidelines. It optionally appends any provided custom guidance or examples to form the final message string.*


### explore (method, L348-L478, parent: RemyxCodeExecutor)

> *Summary: Initiates an AI-driven exploration of a research paper by setting up a two-agent system: one agent proposes experiments, and the other executes them within the paper's environment. It accepts configuration for goals, LLM models/configs, interactivity level, and logging verbosity, returning the complete chat session result.*


### create_agents (method, L480-L548, parent: RemyxCodeExecutor)

> *Summary: This method constructs a two-agent system—an `executor_agent` and a `writer_agent`—without immediately starting an exploration process. It accepts configuration parameters like the goal, LLM model/config, and human interaction mode to customize the agents' behavior before returning both initialized agents as a tuple.*


### __repr__ (method, L550-L554, parent: RemyxCodeExecutor)

> *Summary: Provides a developer-friendly string representation of the executor object, displaying either its `arxiv_id` or the underlying container image name depending on which attribute is set.*


### format_chat_result (method, L557-L576, parent: RemyxCodeExecutor)

> *Summary: This method takes a `ChatResult` object and delegates the task of converting it into a human-readable string summary to an internal utility function. It serves as a wrapper for formatting chat interaction results from exploration or initiation processes.*

