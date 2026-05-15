# test/beta/network/test_packet_routing.py

3 function(s): _call, _result, _graph. 1 class(es): TestResolveRouting. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _call | function |  |
| _result | function |  |
| _graph | function |  |
| TestResolveRouting | class |  |

## Chunks

### _call (function, L27-L29)

> *Summary: Constructs a `ToolCallEvent` object by packaging the provided tool name and an optional reason into JSON arguments. It accepts a tool name string and optional identifiers for call ID and reason.*


### _result (function, L32-L40)

> *Summary: Constructs a `ToolResultEvent` using a provided parent ID and optional name/value. The input `value` determines the content of the result payload within the event structure.*


### _graph (function, L43-L50)

> *Summary: Constructs a `TransitionGraph` by creating rules that transition to specific agent targets whenever any provided tool is called. It initializes the graph with a default termination target for unhandled events.*


### TestResolveRouting (class, L53-L200)

> *Summary: This test suite verifies the logic of resolving packet routing based on a sequence of events (calls and results). It confirms that routing defaults to text if no rules match, handles static tool call matches, prioritizes earlier events, and correctly resolves dynamic handoffs using provided name-to-ID mappings.*


### test_no_events_returns_text (method, L54-L57, parent: TestResolveRouting)

> *Summary: When provided with an empty event list and a specific graph structure, this test asserts that the routing resolution returns a dictionary indicating the content type is text.*


### test_no_graph_returns_text (method, L59-L62, parent: TestResolveRouting)

> *Summary: When provided with a list of events and no graph context, this test asserts that the routing resolution returns a dictionary indicating the content type is text. It specifically checks the output structure when the graph input is empty.*


### test_single_static_tool_call_routes (method, L64-L75, parent: TestResolveRouting)

> *Summary: When provided with a single `ToolCallEvent` matching a specific rule, this test verifies that the routing resolves to a handoff action targeting the specified tool and reason. The input is an event list and a graph structure, yielding a dictionary representing the determined routing.*


### test_unmatched_tool_call_returns_text (method, L77-L83, parent: TestResolveRouting)

> *Summary: When a tool call is made with an unrecognized name, the system routes it as text. This test verifies that calling `_resolve_routing` with an event referencing an unknown tool results in a routing output of type `"text"`.*


### test_two_static_tools_first_emit_wins (method, L85-L95, parent: TestResolveRouting)

> *Summary: When two tool calls are emitted concurrently and both match the same routing rules, this test verifies that the system prioritizes and selects the first event received. It asserts that the routing resolution chooses the call originating from "delegate\_a" because it was listed first in the input events.*


### test_dynamic_handoff_resolves_target (method, L97-L114, parent: TestResolveRouting)

> *Summary: This test verifies that when a `ToolResultEvent` containing a `Handoff` object is processed, the routing mechanism correctly resolves the target ID. It inputs a call and a result event into a routing resolver against a graph and asserts the output matches the expected handoff structure with the resolved agent ID.*


### test_dynamic_handoff_unresolved_name_falls_through_to_name (method, L116-L125, parent: TestResolveRouting)

> *Summary: When a handoff target is not found in the provided ID map, this test verifies that the system defaults to using the target's name as the destination. It simulates an unresolved handoff by passing an empty `name_to_id` dictionary and asserts the routing resolves to the original unknown name.*


### test_dynamic_overrides_static_for_same_tool (method, L127-L141, parent: TestResolveRouting)

> *Summary: When a tool call results in a `Handoff`, the dynamic handoff specified in the result overrides any static routing configuration for that specific tool invocation. This test verifies that the resolved routing correctly adopts the target from the returned `Handoff` object.*


### test_dynamic_first_static_second_first_wins (method, L143-L153, parent: TestResolveRouting)

> *Summary: This test verifies that the first received route takes precedence over subsequent ones. It simulates a sequence where a dynamic call is followed by a static call, asserting that the result from the initial dynamic call is chosen for routing.*


### test_static_first_dynamic_second_first_wins (method, L155-L166, parent: TestResolveRouting)

> *Summary: This test verifies that when a static route is presented before a dynamic one, the static route takes precedence. It simulates an event sequence where a static call precedes a dynamic call, asserting that the final resolved routing selects the initial static delegate and lacks a target field.*


### test_string_result_not_handoff (method, L168-L179, parent: TestResolveRouting)

> *Summary: This test verifies that when a tool returns only a plain string result, no dynamic routing is triggered; the system defaults to static routing based on the tool's name. It simulates calling a delegate and receiving a string output to confirm the absence of a target destination in the resolved routing.*


### test_data_input_non_handoff_ignored (method, L181-L192, parent: TestResolveRouting)

> *Summary: When provided with a `DataInput` that does not represent a handoff event, the system resolves routing to `"text"`. This test verifies that non-handoff data inputs are ignored by specialized routing rules when resolving events against a given graph.*


### test_results_without_calls_ignored (method, L194-L200, parent: TestResolveRouting)

> *Summary: When provided with a list of events containing an orphan `ToolResultEvent` that has no corresponding call, the function resolves routing to `"text"`. This demonstrates that uncalled result events do not influence the routing decision.*

