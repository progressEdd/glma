# cli/src/ag2_cli/commands/arena.py

16 function(s): _run_single_case, _run_contender, _load_suites, _resolve_contender_files, _determine_case_winner, _compute_elo, _load_leaderboard, _save_leaderboard, _update_leaderboard, _flat_cases and 6 more. 1 class(es): ContenderResult. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContenderResult | class |  |
| _run_single_case | function |  |
| _run_contender | function |  |
| _load_suites | function |  |
| _resolve_contender_files | function |  |
| _determine_case_winner | function |  |
| _compute_elo | function |  |
| _load_leaderboard | function |  |
| _save_leaderboard | function |  |
| _update_leaderboard | function |  |
| _flat_cases | function |  |
| _display_comparison | function |  |
| arena_compare | function |  |
| arena_models | function |  |
| arena_interactive | function |  |
| arena_leaderboard | function |  |
| arena_reset | function |  |

## Chunks

### ContenderResult (class, L34-L65)

> *Summary: This class aggregates performance metrics for a single contender across multiple evaluation cases. It calculates derived statistics like pass rate, average score, and total elapsed time based on the list of `CaseResult` objects it holds.*


### pass_rate (method, L42-L45, parent: ContenderResult)

> *Summary: Calculates the overall pass rate by dividing the count of successful results within `self.case_results` by the total number of results, returning $0.0$ if no results are present.*


### avg_score (method, L48-L51, parent: ContenderResult)

> *Summary: Calculates the average score from a list of case results, returning $0.0$ if no results are present. It sums all scores within `self.case_results` and divides by the count of those results.*


### avg_elapsed (method, L54-L57, parent: ContenderResult)

> *Summary: Calculates the average execution time across all stored case results. It returns $0.0$ if no results are present, otherwise it computes the mean of the `elapsed` times from each result object.*


### total_elapsed (method, L60-L61, parent: ContenderResult)

> *Summary: Calculates the cumulative time spent across all recorded case results by summing their individual `elapsed` durations. Returns this total duration as a floating-point number.*


### total_cost (method, L64-L65, parent: ContenderResult)

> *Summary: Calculates the aggregate cost by summing the `cost` attribute from all non-null results within the instance's `case_results`. Returns this total as a floating-point number.*


### _run_single_case (function, L73-L98)

> *Summary: Executes a single evaluation case against an agent loaded from a file by first discovering its capabilities. It returns a `CaseResult` containing the execution output, assertion checks, and timing information, or an error result if discovery fails.*


### _run_contender (function, L101-L108)

> *Summary: Executes all evaluation cases for a specified agent file across a list of suites. It aggregates the results from each individual case run into a `ContenderResult` object containing the contender's name and source path.*


### _load_suites (function, L111-L120)

> *Summary: Reads evaluation suites from a specified path, which can be a single YAML file or a directory containing multiple YAML/YML files. It returns a list of `EvalSuite` objects, raising an error if no YAML files are found in a directory.*


### _resolve_contender_files (function, L123-L139)

> *Summary: This function takes a list of potential paths and resolves them into a definitive list of Python file paths. It expands directory inputs to include all `.py` files within, while validating that all provided paths either exist or contain the expected files, raising an error otherwise.*


### _determine_case_winner (function, L147-L176)

> *Summary: This function determines the winner of a case based on provided contender results, prioritizing those who passed. If there's a tie in score among top contenders, it applies a speed-based tiebreaker if the time difference exceeds ten percent; otherwise, it returns `None` for a complete tie.*


### _compute_elo (function, L184-L196)

> *Summary: Calculates the new ELO ratings for two players based on their initial ratings and the match outcome. It takes two float ratings, an optional winner string ('a', 'b', or None for a draw), and a K-factor, returning the updated ratings for both participants as a tuple of floats.*


### _load_leaderboard (function, L199-L202)

> *Summary: Reads the leaderboard data from a predefined file path if it exists; otherwise, returns an empty structure containing agents. This function provides the current state of the leaderboard for use in the CLI application.*


### _save_leaderboard (function, L205-L207)

> *Summary: This function persists a leaderboard dictionary to a JSON file located at `LEADERBOARD_PATH`. It ensures the necessary directory structure exists before writing the formatted data.*


### _update_leaderboard (function, L210-L237)

> *Summary: This function updates the ELO ratings for two competing agents based on the match outcome. It takes the names of both participants and the winner (or `None` for a tie), then loads, modifies, and saves the global leaderboard data.*


### _flat_cases (function, L245-L247)

> *Summary: This function takes a list of `EvalSuite` objects and returns a single, flattened list containing every individual `EvalCase` from all the provided suites. It achieves this by iterating through each suite and extracting its contained cases into one combined list.*


### _display_comparison (function, L250-L358)

> *Summary: Renders a side-by-side comparison table of contenders across evaluation cases and displays a summary panel with pass rates, average scores, and overall winner information. It takes lists of `ContenderResult`s and `EvalSuite`s as input and returns a dictionary mapping contender names to their win counts.*


### arena_compare (function, L367-L442)

> *Summary: Compares multiple agent implementations by running them against a specified set of evaluation cases. It accepts contender files/directories and an evaluation suite file, returning detailed comparison results or a JSON summary based on the provided options.*


### arena_models (function, L446-L518)

> *Summary: Compares a specified agent script across multiple LLM models using evaluation cases loaded from a file or directory. It executes the agent for each model, collects performance metrics like pass rate and cost, and outputs a comparison summary or detailed JSON if requested.*


### arena_interactive (function, L522-L639)

> *Summary: This function facilitates an interactive head-to-head comparison between two specified agent files. It prompts the user for input, runs both agents against that input, displays their outputs, and then asks the human to judge which agent performed better before updating ELO ratings. The process concludes by revealing which file corresponds to Agent A and Agent B.*


### arena_leaderboard (function, L643-L672)

> *Summary: Retrieves and displays a ranked leaderboard of agents based on their ELO scores from past arena sessions. It loads existing leaderboard data, sorts agents by descending ELO, and presents the rank, agent name, ELO, and win/loss/tie record in a formatted table to the console.*


### arena_reset (function, L676-L686)

> *Summary: This function deletes the existing ELO leaderboard file if it is present at the configured path, otherwise it informs the user that no leaderboard exists for resetting. It performs a cleanup operation on the persistent leaderboard data.*

