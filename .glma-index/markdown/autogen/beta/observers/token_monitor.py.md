# autogen/beta/observers/token_monitor.py

1 class(es): TokenMonitor. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TokenMonitor | class |  |

## Chunks

### TokenMonitor (class, L14-L85)

> *Summary: Tracks cumulative token usage by observing `ModelResponse` and `TaskCompleted` events, accumulating tokens from their respective usages. It emits a `WARNING` alert when the total exceeds a configured threshold or a `CRITICAL` alert if it surpasses a higher limit.*


### __init__ (method, L30-L42, parent: TokenMonitor)

> *Summary: Initializes a token monitoring observer, setting configurable warning and alert thresholds. It tracks the total number of tokens processed and maintains state flags to manage warnings and alerts during execution.*


### total_tokens (method, L45-L46, parent: TokenMonitor)

> *Summary: Returns the accumulated count of all tokens processed by the observer instance. This method provides a read-only view of the token usage tracked internally.*


### process (method, L48-L79, parent: TokenMonitor)

> *Summary: Aggregates token counts from incoming `ModelResponse` and `TaskCompleted` events. It then checks if the accumulated total exceeds predefined warning or critical thresholds, returning an appropriate `ObserverAlert` upon crossing those limits.*


### reset (method, L81-L85, parent: TokenMonitor)

> *Summary: Resets internal state variables, specifically setting total token counts and warning/alert flags back to their initial values. This prepares the monitor object for a new session or measurement period.*

