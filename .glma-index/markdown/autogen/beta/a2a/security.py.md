# autogen/beta/a2a/security.py

7 function(s): bearer_scheme, http_auth_scheme, api_key_scheme, oauth2_scheme, open_id_connect_scheme, mtls_scheme, require. 2 class(es): Scheme, Requirement. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Scheme | class |  |
| Requirement | class |  |
| bearer_scheme | function |  |
| http_auth_scheme | function |  |
| api_key_scheme | function |  |
| oauth2_scheme | function |  |
| open_id_connect_scheme | function |  |
| mtls_scheme | function |  |
| require | function |  |

## Chunks

### Scheme (class, L21-L34)

> *Summary: Represents a named security configuration that links a card identifier to a specific protocol and optional OAuth2/OIDC scopes. It allows creating modified copies by adding new scopes via the `with_scopes` method.*


### with_scopes (method, L32-L34, parent: Scheme)

> *Summary: Creates and returns a new instance of the scheme object, inheriting all current settings but augmenting them with the provided list of OAuth2 or OIDC scopes. This allows for scope modification without altering the original scheme configuration.*


### Requirement (class, L38-L49)

> *Summary: Represents an AND-set of named schemes that must all be present together as a single security requirement entry. It converts this set of required schemes into the corresponding `SecurityRequirement` protocol buffer format.*


### to_proto (method, L45-L49, parent: Requirement)

> *Summary: Converts the object's internal scheme data into a `SecurityRequirement` protobuf message. It maps each scheme name to a list of its associated scopes within the resulting structure.*


### bearer_scheme (function, L52-L63)

> *Summary: Creates an HTTP authentication scheme for Bearer token authorization. It accepts a name and optional format/description to define how the `Authorization: Bearer <token>` header should be structured.*


### http_auth_scheme (function, L66-L77)

> *Summary: Creates a security scheme object specifically for HTTP authentication. It takes parameters like the name, authentication scheme (e.g., "basic", "bearer"), and an optional bearer format string to define how credentials are handled.*


### api_key_scheme (function, L80-L92)

> *Summary: Creates a security scheme object for API key authentication. It takes the scheme name, the client-sent key identifier, and where that key is located (header, query, or cookie) to define the authorization method.*


### oauth2_scheme (function, L95-L112)

> *Summary: Creates a `Scheme` object that encapsulates OAuth 2.0 authentication details. It takes a name, predefined flow configuration, and optional metadata/description strings to construct the security scheme definition.*


### open_id_connect_scheme (function, L115-L125)

> *Summary: Creates a `Scheme` object representing an OpenID Connect discovery URL. It takes the scheme name, the discovery endpoint URL, and an optional description as inputs to define the security configuration.*


### mtls_scheme (function, L128-L135)

> *Summary: Creates a security scheme specifically for Mutual TLS authentication. It accepts a name and an optional description to define the client-certificate requirement within the returned `Scheme` object.*


### require (function, L138-L154)

> *Summary: Constructs a `Requirement` object by combining one or more input `Scheme` objects using a logical AND operation. This function takes variable schemes and returns a single requirement that must satisfy all provided schemes simultaneously.*

