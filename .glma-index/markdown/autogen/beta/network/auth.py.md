# autogen/beta/network/auth.py

3 class(es): AuthAdapter, NoAuth, AuthRegistry. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AuthAdapter | class |  |
| NoAuth | class |  |
| AuthRegistry | class |  |

## Chunks

### AuthAdapter (class, L24-L31)

> *Summary: Defines a protocol for authentication adapters that must implement a `validate` method. This adapter takes a `Passport` object and an authorization claim dictionary as input, raising an `AuthError` if validation fails during the connection handshake.*


### validate (method, L29-L31, parent: AuthAdapter)

> *Summary: This asynchronous method checks the validity of a provided `Passport` against a specific `claim`. It raises an `AuthError` if validation fails or returns nothing upon successful verification.*


### NoAuth (class, L34-L40)

> *Summary: This class acts as a no-operation authentication adapter that accepts any provided claims without validation. It implements an asynchronous `validate` method which simply returns immediately upon receiving a `Passport` and a `claim` dictionary.*


### validate (method, L39-L40, parent: NoAuth)

> *Summary: This asynchronous method checks the validity of a provided `Passport` object against a specific claims dictionary. It currently performs no validation and returns immediately.*


### AuthRegistry (class, L43-L72)

> *Summary: This class manages a collection of authentication adapters, mapping scheme strings to their respective implementations. It allows retrieval of an adapter by its scheme or listing all supported schemes, defaulting to a registry containing only `NoAuth` if none is provided.*


### __init__ (method, L54-L56, parent: AuthRegistry)

> *Summary: Initializes the object by mapping provided `AuthAdapter` instances to a dictionary keyed by their authentication scheme. This allows for quick lookups of specific adapter types based on the scheme string.*


### default (method, L59-L63, parent: AuthRegistry)

> *Summary: Provides a cached, lazy-initialized instance of the default authentication registry. It ensures that if no specific authentication mechanism is configured, it returns an instance using only `NoAuth`.*


### get (method, L65-L69, parent: AuthRegistry)

> *Summary: Retrieves a specific authentication adapter based on the provided scheme string. It returns the corresponding `AuthAdapter` or raises an `AuthError` if the scheme is not recognized in the internal adapters map.*


### schemes (method, L71-L72, parent: AuthRegistry)

> *Summary: Returns a list of strings representing the names of all configured authentication adapters available on the instance.*

