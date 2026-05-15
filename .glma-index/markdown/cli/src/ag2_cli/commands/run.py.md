# cli/src/ag2_cli/commands/run.py

7 function(s): _on_print, _on_event, _display_header, _display_summary, _discover, run_cmd, chat_cmd.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _on_print | function |  |
| _on_event | function |  |
| _display_header | function |  |
| _display_summary | function |  |
| _discover | function |  |
| run_cmd | function |  |
| chat_cmd | function |  |

## Chunks

### _on_print (function, L24-L28)

> *Summary: This helper function takes a string and forwards it to the Rich console for real-time display, ensuring that only non-empty lines are printed. It acts as an output sink for AG2's print statements.*


### _on_event (function, L31-L67)

> *Summary: This function processes structured AG2 events by rendering them to the console using Rich formatting. It inspects the event type—such as `TextEvent`, `ToolCallEvent`, or `ToolResponseEvent`—and prints appropriate visual representations based on the event's content and sender information.*


### _display_header (function, L75-L95)

> *Summary: Generates and prints a formatted header panel to the console using agent discovery information. It dynamically sets a subtitle based on whether the discovered entity is the main entry point, a collection of agents, or a single agent.*


### _display_summary (function, L98-L126)

> *Summary: This function formats and prints a summary footer after an execution run based on a `RunResult` object. It displays metrics like turns, elapsed time, total cost (including token counts if available), the last speaker, and any encountered errors in a styled table format.*


### _discover (function, L129-L148)

> *Summary: Reads an agent file path and determines the discovery method based on the file extension. If it's YAML, it loads configuration and builds agents from that; otherwise, it attempts to discover agents directly from the file content, handling potential errors by exiting.*


### run_cmd (function, L156-L215)

> *Summary: Executes an agent or team defined by a file path, optionally accepting an input message from arguments or standard input. It runs the simulation up to a specified turn limit and outputs either a live-rendered summary or a structured JSON object containing results, turns, and timing information.*


### chat_cmd (function, L218-L373)

> *Summary: Initiates an interactive terminal chat session, either with a specified agent file or by creating an ad-hoc assistant using a provided LLM model and system prompt. It processes user input turn-by-turn, displaying results and tracking costs, and optionally saves the entire conversation history to a replayable session upon exit.*

