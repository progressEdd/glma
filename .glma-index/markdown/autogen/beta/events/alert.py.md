# autogen/beta/events/alert.py

3 class(es): Severity, ObserverAlert, HaltEvent.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Severity | class |  |
| ObserverAlert | class |  |
| HaltEvent | class |  |

## Chunks

### Severity (class, L16-L22)

> *Summary: Defines an enumeration of severity levels (`INFO`, `WARNING`, `CRITICAL`, `FATAL`) for observer alerts. It inherits from `str` and `Enum`, allowing these levels to be used as string values.*


### ObserverAlert (class, L25-L35)

> *Summary: Represents a structured notification originating from an observer. It carries the source name, severity level, a descriptive message, and optional structured data for consumption by alert policies.*


### HaltEvent (class, L38-L43)

> *Summary: Represents an event signaling that the system has stopped due to a critical failure. It carries the reason for halting, the source of the issue, and a list of associated alerts.*

