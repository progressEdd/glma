# autogen/agentchat/group/speaker_selection_result.py

1 class(es): SpeakerSelectionResult. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SpeakerSelectionResult | class |  |

## Chunks

### SpeakerSelectionResult (class, L16-L41)

> *Summary: This data structure encapsulates the outcome of a speaker selection process, holding optional fields for an `Agent` name, a termination flag, or a specific selection method string. Its primary method resolves these fields into either the designated `Agent`, a specified selection method string, or `None` to signal conversation completion.*


### get_speaker_selection_result (method, L26-L41, parent: SpeakerSelectionResult)

> *Summary: Determines the outcome of a speaker selection process based on configuration. It returns the matching `Agent` object from the group chat if an agent name is set, otherwise it returns a specified selection method or `None` if termination is explicitly requested. Raises an error if no valid selection criteria are provided.*

