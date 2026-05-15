# test/beta/events/test_alert.py

2 class(es): TestObserverAlertCreation, TestHaltEvent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestObserverAlertCreation | class |  |
| TestHaltEvent | class |  |

## Chunks

### TestObserverAlertCreation (class, L9-L26)

> *Summary: This test suite verifies the correct initialization and attribute setting of an `ObserverAlert` object. It confirms that alerts can be created with basic string/enum values, accept custom severity strings, and correctly store associated data dictionaries.*


### test_create_alert (method, L10-L15, parent: TestObserverAlertCreation)

> *Summary: This test verifies the correct initialization of an `ObserverAlert` object by asserting that its source, severity, message, and data fields match the provided input values. It confirms the alert is created with specific predefined parameters.*


### test_create_alert_with_data (method, L17-L20, parent: TestObserverAlertCreation)

> *Summary: This test verifies that an `ObserverAlert` object correctly stores provided metadata and severity levels upon instantiation. It confirms the internal state matches the input dictionary for data and the specified string for severity.*


### test_severity_values (method, L22-L26, parent: TestObserverAlertCreation)

> *Summary: Verifies that the predefined `Severity` enum members correctly map to their expected string representations ("info", "warning", "critical", and "fatal"). This test ensures consistent string values for severity levels across the system.*


### TestHaltEvent (class, L29-L33)

> *Summary: This test verifies the correct initialization of a `HaltEvent` instance by asserting that its provided source and reason match the expected values. It confirms the event object correctly stores the input parameters during creation.*


### test_halt_event_creation (method, L30-L33, parent: TestHaltEvent)

> *Summary: This test verifies that a `HaltEvent` object is correctly initialized with specific source and reason strings upon creation. It asserts the integrity of the input values assigned to the event's attributes.*

