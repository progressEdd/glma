# cli/tests/test_serve.py

2 function(s): _make_discovered, _make_run_result. 2 class(es): TestBuildRestApp, TestServeCommand. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_discovered | function |  |
| _make_run_result | function |  |
| TestBuildRestApp | class |  |
| TestServeCommand | class |  |

## Chunks

### _make_discovered (function, L30-L39)

> *Summary: Creates a basic `DiscoveredAgent` instance suitable for testing purposes. It accepts an agent kind and optional list of names, defaulting to "agent" and `["test"]`.*


### _make_run_result (function, L42-L51)

> *Summary: Constructs a `RunResult` object by merging provided keyword arguments with predefined default values for output, turn count, elapsed time, and agent names. It ensures the resulting object has sensible defaults if no specific parameters are supplied during creation.*


### TestBuildRestApp (class, L60-L127)

> *Summary: This test suite verifies the functionality of a FastAPI application factory by instantiating it with optional agent discovery data. It asserts that core endpoints like `/health`, `/agents`, and `/chat` behave as expected, including validating API responses and ensuring the chat endpoint correctly invokes an external execution runner.*


### _build_app (method, L70-L77, parent: TestBuildRestApp)

> *Summary: Constructs a test client by first ensuring an agent discovery object exists, either from input or by generating a default one. It then builds the REST application using this discovered data and wraps it in a `TestClient` for testing purposes.*


### test_app_has_expected_routes (method, L79-L84, parent: TestBuildRestApp)

> *Summary: This test verifies that the application exposes specific endpoints by inspecting its registered routes. It builds the app instance, extracts all defined paths, and asserts the presence of `/health`, `/agents`, and `/chat`.*


### test_health_returns_ok (method, L86-L90, parent: TestBuildRestApp)

> *Summary: This test verifies that the application's `/health` endpoint returns a successful HTTP status code (200) and a JSON body indicating an "ok" status when accessed via the built client.*


### test_agents_returns_agent_list (method, L92-L100, parent: TestBuildRestApp)

> *Summary: Given a discovery dictionary containing specified agents, this test verifies that the `/agents` endpoint returns a 200 status code and a JSON list containing all expected agent objects. It asserts the correct count and structure of the returned agent data.*


### test_chat_endpoint_calls_execute (method, L102-L113, parent: TestBuildRestApp)

> *Summary: This test verifies that a POST request to the `/chat` endpoint correctly triggers the `execute` function with specific inputs and returns a successful response containing expected structured data like output, turn count, and timing information. It asserts that the underlying execution logic was called exactly once during the API interaction.*


### test_chat_endpoint_forwards_max_turns (method, L115-L122, parent: TestBuildRestApp)

> *Summary: This test verifies that the `/chat` endpoint correctly passes the `max_turns` parameter from the incoming JSON request to the underlying execution logic. It asserts that the mocked runner function receives this value, either in its keyword arguments or positional arguments.*


### test_chat_endpoint_rejects_missing_message (method, L124-L127, parent: TestBuildRestApp)

> *Summary: When a POST request is sent to the `/chat` endpoint with an empty JSON body, it asserts that the API returns a `422 Unprocessable Entity` status code due to missing required message data.*


### TestServeCommand (class, L135-L170)

> *Summary: This test suite validates the early-exit validation logic for the `serve` command by invoking the application with specific inputs. It asserts that the command fails (exits with code 1) when provided an unknown protocol or a non-existent file, and verifies that the `--playground` flag displays a "coming soon" message even if agent discovery fails.*


### test_serve_rejects_unknown_protocol (method, L142-L145, parent: TestServeCommand)

> *Summary: This test verifies that the serving command rejects execution when an unrecognized protocol is provided as input. It asserts that the process exits with a non-zero code and outputs an error message indicating an unknown protocol.*


### test_serve_requires_file_to_exist (method, L148-L152, parent: TestServeCommand)

> *Summary: This test verifies that the serving command fails when the specified agent file does not exist. It asserts that the invocation returns a non-zero exit code and includes an error message indicating the file was not found.*


### test_serve_playground_shows_coming_soon (method, L155-L170, parent: TestServeCommand)

> *Summary: When invoking the `serve` command with the `--playground` flag, this test verifies that a "coming soon" message is displayed even if agent discovery fails by raising a `ValueError`. It achieves this by mocking the discovery mechanism and ensuring the output contains the expected placeholder text.*

