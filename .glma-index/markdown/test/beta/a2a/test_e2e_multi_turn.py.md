# test/beta/a2a/test_e2e_multi_turn.py

1 function(s): test_server_sees_full_history_on_second_turn.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_server_sees_full_history_on_second_turn | function |  |

## Chunks

### test_server_sees_full_history_on_second_turn (function, L19-L35)

> *Summary: This test verifies that the server receives the complete conversation history on a subsequent turn. It sends two sequential messages and asserts that the second call's recorded input includes both the initial prompt and the first model response.*

