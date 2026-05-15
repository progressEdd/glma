# test/messages/test_client_messages.py

2 class(es): TestChangeUsageSummaryMessage, TestStreamMessage. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestChangeUsageSummaryMessage | class |  |
| TestStreamMessage | class |  |

## Chunks

### TestChangeUsageSummaryMessage (class, L14-L17)

> *Summary: This test verifies that an instance created with a `UsageSummaryMessage` structure correctly inherits from the `UsageSummaryEvent`. It takes a UUID as input and asserts the resulting object's type.*


### test_deprecation (method, L15-L17, parent: TestChangeUsageSummaryMessage)

> *Summary: This test verifies that an instance of `UsageSummaryMessage`, initialized with a UUID and null usage summaries, correctly inherits from the `UsageSummaryEvent` base class. It confirms the expected type relationship for message handling.*


### TestStreamMessage (class, L20-L23)

> *Summary: This method verifies that an instance created from a `StreamMessage` object correctly inherits from the `StreamEvent` class. It takes a UUID as input and asserts the type of the resulting message object.*


### test_deprecation (method, L21-L23, parent: TestStreamMessage)

> *Summary: Asserts that an instance created from a `StreamMessage` object is correctly recognized as a `StreamEvent`. It takes a UUID as input to construct and test the message type.*

