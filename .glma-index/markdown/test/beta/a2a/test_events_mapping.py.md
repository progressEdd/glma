# test/beta/a2a/test_events_mapping.py

6 class(es): TestAg2ToA2A, TestA2AToSdk, TestSdkToA2A, TestParseTaskArtifact, TestRoundTrip, TestWireMetadata. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAg2ToA2A | class |  |
| TestA2AToSdk | class |  |
| TestSdkToA2A | class |  |
| TestParseTaskArtifact | class |  |
| TestRoundTrip | class |  |
| TestWireMetadata | class |  |

## Chunks

### TestAg2ToA2A (class, L45-L107)

> *Summary: This test suite verifies event mappings between different system states and an A2A format. It confirms that inputs like message chunks, tool calls, or task state changes correctly transform into corresponding structured artifact or status update events for the A2A representation.*


### test_chunk_to_text_artifact (method, L46-L65, parent: TestAg2ToA2A)

> *Summary: This test verifies that a `ModelMessageChunk` input correctly transforms into an `A2ATextArtifact`. It asserts the resulting artifact contains the original text within its parts and matches expected update event details.*


### test_client_call_to_artifact (method, L67-L91, parent: TestAg2ToA2A)

> *Summary: This test verifies that a `ClientToolCallEvent` input correctly transforms into an `A2AToolCallArtifact` output. It asserts the resulting artifact contains the original tool call details wrapped within a specific update structure for task and context tracking.*


### test_task_state_to_status_update (method, L93-L107, parent: TestAg2ToA2A)

> *Summary: This test verifies that a specific task state maps correctly to an `A2ATaskStatusUpdate` event. It inputs a completed task state along with IDs and asserts the resulting event structure matches the expected status update payload.*


### TestA2AToSdk (class, L110-L140)

> *Summary: These tests verify the `a2a_event_to_sdk` function correctly transforms various A2A event structures into their corresponding SDK representations. It validates mappings for artifact updates, status changes (like failure), messages, and task snapshots.*


### test_artifact_update_unwrap (method, L111-L119, parent: TestA2AToSdk)

> *Summary: This test verifies that an artifact update event, generated from a `ModelMessageChunk` input with specific IDs, correctly maps to the `.update` event type when processed by `a2a_event_to_sdk`. It confirms the resulting structure matches the expected SDK representation.*


### test_status_update_unwrap (method, L121-L130, parent: TestA2AToSdk)

> *Summary: This test verifies that a `TaskState` enum value, when converted to a status update event and then mapped to an SDK protocol buffer, results in the expected `TaskStatusUpdateEvent`. It confirms correct serialization of task ID, context ID, and the failed state.*


### test_message_unwrap (method, L132-L135, parent: TestA2AToSdk)

> *Summary: This test verifies that the `a2a_event_to_sdk` function correctly unwraps an A2A message structure into its original SDK `Message` object. It asserts equality between the input wrapped message and the output unwrapped message.*


### test_task_snapshot_unwrap (method, L137-L140, parent: TestA2AToSdk)

> *Summary: This test verifies that the `a2a_event_to_sdk` function correctly unwraps an `A2ATaskSnapshot` containing a `Task` object, returning the original `Task` instance. It asserts equality between the input snapshot's contained task and the output of the conversion function.*


### TestSdkToA2A (class, L143-L222)

> *Summary: This test suite verifies the mapping logic from SDK stream responses to A2A event structures. It asserts that various input events—such as text artifacts, tool call artifacts, status updates, task snapshots, and messages—are correctly parsed into their corresponding A2A representations.*


### test_text_artifact (method, L144-L155, parent: TestSdkToA2A)

> *Summary: This test verifies that a `TaskArtifactUpdateEvent` containing streamed text is correctly parsed into an `A2ATextArtifact`. It asserts the resulting event matches the input update structure and includes the extracted "streamed" text.*


### test_tool_call_artifact (method, L157-L177, parent: TestSdkToA2A)

> *Summary: This test verifies that a `TaskArtifactUpdateEvent` containing a tool call artifact is correctly parsed from a stream response. It asserts the resulting event matches an expected `A2AToolCallArtifact`, confirming proper extraction of the tool call details.*


### test_status_update (method, L179-L188, parent: TestSdkToA2A)

> *Summary: This test verifies that a `TaskStatusUpdateEvent` correctly maps to an `A2ATaskStatusUpdate` object when processed by `parse_stream_response`. It asserts the resulting event matches the expected structure containing the original update and the specific task state.*


### test_task_snapshot (method, L190-L195, parent: TestSdkToA2A)

> *Summary: This test verifies that a `StreamResponse` containing a `Task` object correctly maps to an `A2ATaskSnapshot`. It asserts the resulting event matches the expected snapshot structure.*


### test_message (method, L197-L202, parent: TestSdkToA2A)

> *Summary: This test verifies that a `Message` object, when processed through `parse_stream_response`, correctly yields an `A2AMessage` instance containing the original message. It confirms the mapping from stream response data to the expected application-specific event structure.*


### test_unknown_artifact_falls_back_to_base (method, L204-L222, parent: TestSdkToA2A)

> *Summary: When processing a stream response containing an artifact with mixed text and opaque JSON data, the system correctly parses it into an `A2ATaskArtifactUpdate` event. This test confirms that unknown or complex artifact extensions fall back to the base update structure when parsing fails specific content checks.*


### TestParseTaskArtifact (class, L225-L273)

> *Summary: This test suite verifies how `parse_task_artifact` converts different artifact types (text and tool call) from a polling snapshot into structured events, asserting specific event structures for both scenarios. It also confirms that the resulting typed view matches what would be produced by streaming processing.*


### test_text_artifact_from_polling_snapshot (method, L226-L243, parent: TestParseTaskArtifact)

> *Summary: This test verifies that when an artifact containing text is processed from a polling snapshot, it generates an `A2ATextArtifact` event. The expected output confirms the artifact's content and sets flags indicating it was not appended and represents the last chunk.*


### test_tool_call_artifact_from_polling_snapshot (method, L245-L265, parent: TestParseTaskArtifact)

> *Summary: This test verifies that an `Artifact` containing a tool call payload correctly translates into an `A2AToolCallArtifact` event. It takes a predefined artifact structure as input and asserts the resulting event matches the expected structure, including the embedded `ToolCallEvent`.*


### test_routes_through_same_classifier_as_streaming (method, L267-L273, parent: TestParseTaskArtifact)

> *Summary: This test verifies that artifacts processed via polling and streaming mechanisms result in objects of the same underlying type. It achieves this by parsing an artifact through both methods and asserting their types match.*


### TestRoundTrip (class, L277-L290)

> *Summary: This test verifies data integrity by serializing a `ModelMessageChunk` into an artifact, then deserializing it back. It confirms that the roundtrip process—from chunk to serialized artifact and back via stream parsing—reconstructs the original input exactly.*


### test_chunk_artifact_roundtrip (method, L278-L290, parent: TestRoundTrip)

> *Summary: This test verifies the roundtrip integrity of chunk artifacts by converting a `ModelMessageChunk` to an artifact, then serializing and deserializing it via event mapping. It asserts that the final parsed structure matches the initial input artifact.*


### TestWireMetadata (class, L293-L351)

> *Summary: These tests verify the correct serialization and data propagation when converting various task events (like status updates or chunk artifacts) into a standardized event structure. They confirm behaviors such as timestamp inclusion, optional metadata handling, and default naming conventions for different input types.*


### test_status_update_timestamp_propagates (method, L294-L303, parent: TestWireMetadata)

> *Summary: This test verifies that a provided UTC timestamp correctly propagates when converting a task state to a status update event. It asserts that the seconds value of the resulting event's timestamp matches the Unix timestamp of the input `datetime` object.*


### test_status_update_omits_timestamp_by_default (method, L305-L308, parent: TestWireMetadata)

> *Summary: When converting a `TaskState` to a status update event, the resulting timestamp defaults to zero seconds if not explicitly provided. This test verifies that the generated event object reflects this default behavior for the timestamp field.*


### test_chunk_artifact_optional_name_and_description (method, L310-L321, parent: TestWireMetadata)

> *Summary: This test verifies that when converting a `ModelMessageChunk` to an event, optional artifact metadata like name and description are correctly preserved in the resulting event structure. It asserts that the provided string values for `name` and `description` match those on the generated artifact object within the event update.*


### test_chunk_artifact_metadata_round_trips_through_struct (method, L323-L332, parent: TestWireMetadata)

> *Summary: This test verifies that artifact metadata survives a round trip through the system structure. It takes a `ModelMessageChunk` and associated metadata, converts it to an event, and then asserts that the original metadata is correctly preserved when converted back from the structured format.*


### test_client_call_artifact_uses_tool_name_by_default (method, L334-L341, parent: TestWireMetadata)

> *Summary: When converting a `ClientToolCallEvent` into an artifact, this test verifies that the resulting artifact's name defaults to the tool's specified name if not otherwise configured. It takes a client call event and task/context IDs as input, asserting the correct naming convention on the output artifact.*


### test_client_call_artifact_name_override (method, L343-L351, parent: TestWireMetadata)

> *Summary: This test verifies that a provided custom name overrides the default artifact name when converting a `ClientToolCallEvent` into an artifact structure. It asserts that the resulting event's update object correctly reflects the specified override name.*

