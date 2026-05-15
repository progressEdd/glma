# autogen/tools/experimental/deep_research/deep_research.py

7 class(es): Subquestion, SubquestionAnswer, Task, CompletedTask, InformationCrumb, GatheredInformation, DeepResearchTool. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Subquestion | class |  |
| SubquestionAnswer | class |  |
| Task | class |  |
| CompletedTask | class |  |
| InformationCrumb | class |  |
| GatheredInformation | class |  |
| DeepResearchTool | class |  |

## Chunks

### Subquestion (class, L20-L24)

> *Summary: Represents a single sub-query derived from an original question, holding the string content of that question. It provides a method to format this information into a readable string prefixed with "Question: ".*


### format (method, L23-L24, parent: Subquestion)

> *Summary: Generates a string representation of the object, prepending "Question: " to the stored question text. This method is used to output the core query for display or logging purposes.*


### SubquestionAnswer (class, L27-L31)

> *Summary: This class extends `Subquestion` by adding an `answer` field for storing a string response. Its primary behavior is to format the question and its corresponding answer into a readable, multi-line string output.*


### format (method, L30-L31, parent: SubquestionAnswer)

> *Summary: Generates a formatted string containing the stored question and answer. It combines these two attributes into a single, multi-line output string for presentation.*


### Task (class, L34-L42)

> *Summary: Represents a research task containing an overarching question and a list of related subquestions. It provides a `format` method to serialize the entire structure into a multi-line string for display or processing.*


### format (method, L38-L42, parent: Task)

> *Summary: Generates a structured string representation of the research task and its associated subquestions. It concatenates the main question with formatted strings for each subquestion found in the instance's `subquestions` list.*


### CompletedTask (class, L45-L53)

> *Summary: Represents a completed research task containing the original question and a list of answered subquestions. It provides a `format` method to serialize this structure into a human-readable string output.*


### format (method, L49-L53, parent: CompletedTask)

> *Summary: Generates a structured string representation of the research task and its associated subquestions. It concatenates the main question with formatted strings for each subquestion found in the instance's `subquestions` list.*


### InformationCrumb (class, L56-L60)

> *Summary: This data structure models a piece of gathered information, requiring inputs for the source URL, title, summary, and any specific relevant details. It serves as a standardized container for storing research findings.*


### GatheredInformation (class, L63-L70)

> *Summary: This model encapsulates a list of `InformationCrumb` objects, representing collected data from research sources. It provides a `format` method to serialize this collection into a single, structured string output detailing the URL, title, summary, and relevant information for each item.*


### format (method, L66-L70, parent: GatheredInformation)

> *Summary: Generates a formatted string summarizing gathered information by iterating over stored `info` objects. It concatenates details like URL, title, summary, and relevant text for each item into a single output string.*


### DeepResearchTool (class, L74-L335)

> *Summary: This class orchestrates complex web research by delegating tasks through specialized agent subteams. It accepts a research task string and returns the final synthesized answer after decomposition, answering subquestions via a web surfer, and critical review.*


### __init__ (method, L79-L165, parent: DeepResearchTool)

> *Summary: Initializes a research tool by setting up two specialized agents: one for summarizing answers and another for critically evaluating them. It exposes a function that takes a research task string and executes a multi-step conversation between these agents to produce a final summarized answer.*


### _get_split_question_and_answer_subquestions (method, L170-L239, parent: DeepResearchTool)

> *Summary: This function returns a callable that uses two specialized conversational agents—a decomposition agent and a critic agent—to break down a complex input question into focused subquestions. It orchestrates this process by having the critic evaluate the initial breakdown provided by the agent, ultimately returning the summarized list of derived subquestions.*


### _get_generate_subquestions (method, L242-L275, parent: DeepResearchTool)

> *Summary: This function returns a callable that processes a task by generating and answering subquestions using an LLM tool. It takes the task, LLM configuration, and maximum web steps as input to return a formatted string containing the answers for each generated subquestion.*


### _answer_question (method, L278-L335, parent: DeepResearchTool)

> *Summary: This method orchestrates a research process by initializing and running a `WebSurferAgent` alongside a `WebSurferCritic`. It takes a question and configuration, uses the agents to gather web information and critique it iteratively, and returns the final summarized answer from the chat session.*

