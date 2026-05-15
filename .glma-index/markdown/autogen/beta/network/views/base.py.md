# autogen/beta/network/views/base.py

1 class(es): ViewPolicy. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ViewPolicy | class |  |

## Chunks

### ViewPolicy (class, L34-L55)

> *Summary: Defines a protocol for per-participant projection logic, requiring implementations to deterministically transform a given Write-Ahead Log (WAL) slice into a list of model events. It accepts the WAL slice, participant ID, channel metadata, and an envelope renderer as inputs, returning the resulting `BaseEvent` objects.*


### project (method, L44-L55, parent: ViewPolicy)

> *Summary: Transforms a slice of received `Envelope` records (`wal`) for a specific participant and channel into a list of structured `BaseEvent` objects, utilizing an external renderer to maintain view neutrality.*

