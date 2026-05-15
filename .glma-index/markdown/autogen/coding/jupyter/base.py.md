# autogen/coding/jupyter/base.py

2 class(es): JupyterConnectionInfo, JupyterConnectable. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| JupyterConnectionInfo | class |  |
| JupyterConnectable | class |  |

## Chunks

### JupyterConnectionInfo (class, L15-L25)

> *Summary: This structure holds configuration details necessary to connect to a Jupyter gateway server. It accepts host, HTTPS flag, optional port, and an optional authentication token as inputs.*


### JupyterConnectable (class, L30-L36)

> *Summary: Defines a protocol requiring an object to expose its `connection_info` as a property, which must return a `JupyterConnectionInfo`. This establishes a contract for objects capable of representing a Jupyter connection.*


### connection_info (method, L34-L36, parent: JupyterConnectable)

> *Summary: Retrieves and returns a structured object containing details about the current Jupyter connection. This method requires no input parameters to execute.*

