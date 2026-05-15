# cli/src/ag2_cli/commands/replay.py

17 function(s): _session_path, save_session, load_session, list_sessions, delete_session, create_session_id, record_from_run_result, _render_event, _render_session_header, replay_list and 7 more. 3 class(es): SessionEvent, SessionMeta, Session.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SessionEvent | class |  |
| SessionMeta | class |  |
| Session | class |  |
| _session_path | function |  |
| save_session | function |  |
| load_session | function |  |
| list_sessions | function |  |
| delete_session | function |  |
| create_session_id | function |  |
| record_from_run_result | function |  |
| _render_event | function |  |
| _render_session_header | function |  |
| replay_list | function |  |
| replay_show | function |  |
| replay_step | function |  |
| replay_branch | function |  |
| replay_compare | function |  |
| replay_export | function |  |
| replay_delete | function |  |
| replay_clear | function |  |

## Chunks

### SessionEvent (class, L37-L46)

> *Summary: Represents a single interaction within a recorded session by storing details like turn number, speaker identity, content, and role. It also includes timestamps and optional metadata for tracking event timing and context.*


### SessionMeta (class, L50-L61)

> *Summary: This class serves as a data structure to hold metadata about a recorded session. It stores details such as the session ID, associated agent files and names, creation time, turn count, duration, costs, and input/final output messages.*


### Session (class, L65-L69)

> *Summary: Represents a fully captured recording, holding metadata and an ordered list of events. It initializes with no events by default, allowing it to accumulate session data.*


### _session_path (function, L77-L78)

> *Summary: Constructs the full file path for a session's JSON data given its unique identifier. It combines a predefined sessions directory with the provided ID to return a `Path` object.*


### save_session (function, L81-L90)

> *Summary: This function serializes a `Session` object into a JSON file within the designated sessions directory. It takes a session as input and returns the absolute `Path` to the saved file containing its metadata and event history.*


### load_session (function, L93-L113)

> *Summary: Retrieves a `Session` object by its ID, first checking the exact file path. If not found, it searches for matching files and handles ambiguity or absence by exiting with an error if multiple or no matches are found.*


### list_sessions (function, L116-L128)

> *Summary: Retrieves a list of session metadata objects by scanning the designated sessions directory for JSON files. It parses each valid file, sorts them newest first, and returns a list containing `SessionMeta` instances.*


### delete_session (function, L131-L142)

> *Summary: Removes a session file based on its ID, first checking for an exact match at a derived path. If not found, it attempts to delete the single matching file within the sessions directory using a wildcard prefix search.*


### create_session_id (function, L150-L152)

> *Summary: Generates a unique, time-stamped string identifier by combining the current UTC date and time with a short hexadecimal segment from a UUID. This function produces a human-readable session ID suitable for tracking replay sessions.*


### record_from_run_result (function, L155-L194)

> *Summary: Transforms a `RunResult` object and an input message into a structured `Session`. It extracts conversation history to build event logs, calculates the total cost from the result's cost structure, and packages everything into a complete session object.*


### _render_event (function, L202-L224)

> *Summary: Generates a `Panel` object from a `SessionEvent`, styling it based on the event's role (user, tool, system). It constructs the panel content using the event's text, turn/speaker information as the title, and optional timing or tool call details in the subtitle.*


### _render_session_header (function, L227-L249)

> *Summary: Generates a formatted `Panel` displaying key metadata from a session object. It takes a `SessionMeta` instance as input and outputs a styled panel containing details like session ID, agent names, turn count, duration, optional cost, and a preview of the input message.*


### replay_list (function, L258-L297)

> *Summary: Retrieves and displays a paginated list of recorded sessions, limited by an optional `--limit` argument. It fetches session metadata, formats it into a structured table showing ID, agent, turns, duration, and date, and prints the results to the console.*


### replay_show (function, L301-L317)

> *Summary: Loads a recorded session using a provided ID or prefix and then prints its metadata header followed by each individual event from the session to the console.*


### replay_step (function, L321-L372)

> *Summary: Loads a recorded session using a provided session ID and enters an interactive loop to step through its events. Users can navigate forward, backward, jump to a specific turn number, or quit the playback.*


### replay_branch (function, L376-L487)

> *Summary: This function takes a session ID and an optional turn number and message to create a new branch of the existing conversation. It replays prior turns to rebuild context, executes the agent with the specified or derived new message, and saves the resulting branched session history.*


### replay_compare (function, L491-L542)

> *Summary: This function compares two loaded sessions by taking two session IDs as input. It outputs a side-by-side comparison displaying metadata (like agent file, turns, duration, and cost) in a table, followed by rendering corresponding events from both sessions across multiple lines.*


### replay_export (function, L546-L619)

> *Summary: This function exports a loaded session transcript based on the specified format (`md`, `json`, or `html`). It takes a required session ID, an optional output path, and generates structured content which is either printed to standard output or written to the provided file.*


### replay_delete (function, L623-L635)

> *Summary: This function deletes a recorded session identified by the provided `session_id`. It calls an underlying deletion service and prints a success or error message based on whether the session was successfully removed.*


### replay_clear (function, L639-L653)

> *Summary: This function deletes all JSON files within the configured sessions directory if it exists. It iterates through and unlinks every file found, reporting the total number of cleared sessions upon completion.*

