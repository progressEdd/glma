# test/beta/config/gemini/test_tool_call_event.py

2 function(s): test_thought_signature_round_trip, test_thought_signature_defaults_to_none.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_thought_signature_round_trip | function |  |
| test_thought_signature_defaults_to_none | function |  |

## Chunks

### test_thought_signature_round_trip (function, L9-L22)

> *Summary: This test verifies the serialization and deserialization process for a `GeminiToolCallEvent`. It takes an event initialized with a specific byte signature and asserts that after round-tripping through serialization/deserialization, the resulting object is of the correct type and retains the original byte signature.*


### test_thought_signature_defaults_to_none (function, L25-L28)

> *Summary: Verifies that a newly instantiated `GeminiToolCallEvent` object has its `thought_signature` attribute set to `None` by default when initialized with basic tool call details.*

