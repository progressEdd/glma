# test/beta/network/test_bridge_drives_workflow.py

2 function(s): test_bridge_drives_workflow_via_layer2_envelope_helpers, test_bridge_uses_module_level_default_helper_directly.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_bridge_drives_workflow_via_layer2_envelope_helpers | function |  |
| test_bridge_uses_module_level_default_helper_directly | function |  |

## Chunks

### test_bridge_drives_workflow_via_layer2_envelope_helpers (function, L44-L126)

> *Summary: This test verifies a workflow progression between two participants, Alice and Bob, using only low-level envelope posting without involving LLM agents or tools. It demonstrates how building and posting specific packet envelopes advances the channel state through defined transitions (Alice $\to$ Bob $\to$ Alice).*


### test_bridge_uses_module_level_default_helper_directly (function, L130-L180)

> *Summary: This test verifies that a communication bridge can directly utilize a module-level helper to construct an envelope without needing to resolve or interact with a specific channel adapter. It sets up two agents, initiates a workflow channel between them, manually builds the packet envelope using the default function, posts it via the hub, and asserts the expected state transition occurs on the receiving end.*

