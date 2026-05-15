# autogen/mcp/mcp_proxy/security.py

16 class(es): BaseSecurity, BaseSecurityParameters, UnsupportedSecurityStub, Parameters, APIKeyHeader, Parameters, APIKeyQuery, Parameters, APIKeyCookie, Parameters, HTTPBearer, Parameters, HTTPBasic, Parameters, OAuth2PasswordBearer, Parameters. 40 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BaseSecurity | class |  |
| BaseSecurityParameters | class |  |
| UnsupportedSecurityStub | class |  |
| APIKeyHeader | class |  |
| APIKeyQuery | class |  |
| APIKeyCookie | class |  |
| HTTPBearer | class |  |
| HTTPBasic | class |  |
| OAuth2PasswordBearer | class |  |

## Chunks

### BaseSecurity (class, L19-L79)

> *Summary: This base class defines the structure and validation logic for various security configurations, enforcing that a specified `in_value` is valid for its declared security `type`. It provides static methods to discover, validate, and parse concrete security implementations from schema parameters or environment variables.*


### __post_init__ (method, L27-L41, parent: BaseSecurity)

> *Summary: This method validates the `in_value` attribute against a predefined set of allowed values based on the instance's `type`. It raises a `ValueError` if the provided input value is not permitted for the specified security type.*


### accept (method, L43-L44, parent: BaseSecurity)

> *Summary: Checks if the current instance conforms to the expected security class defined within the provided parameters object. Returns a boolean indicating successful type matching.*


### is_supported (method, L47-L48, parent: BaseSecurity)

> *Summary: Checks if a class matches a specified type and if its `in_value` aligns with the "in" parameter provided in the input schema dictionary. Returns a boolean indicating support based on these two conditions.*


### get_security_class (method, L51-L59, parent: BaseSecurity)

> *Summary: This method iterates through a class's subclasses to find one that supports the given security `type` and `schema_parameters`. It returns the first matching subclass, or an `UnsupportedSecurityStub` if no suitable implementation is found.*


### get_security_parameters (method, L62-L63, parent: BaseSecurity)

> *Summary: Constructs a string representation of the class name, embedding a specific parameter value retrieved from the input dictionary. This acts as a standardized way to expose security configuration details based on provided schema parameters.*


### parse_security_parameters (method, L66-L70, parent: BaseSecurity)

> *Summary: Extracts the security type and associated parameters from an input dictionary. It then uses these to instantiate a specific security class and validates any remaining data against that class's parameter model, returning the structured security configuration.*


### parse_security_parameters_from_env (method, L73-L79, parent: BaseSecurity)

> *Summary: Retrieves the "SECURITY" string from the provided environment dictionary and parses it into a `BaseSecurityParameters` object using an internal parsing method, logging a warning if no such variable exists.*


### BaseSecurityParameters (class, L82-L101)

> *Summary: This abstract class defines the structure for various security configurations, requiring subclasses to implement methods for serialization (`dump`) and applying security logic. It provides utility methods to convert its parameters into a dictionary format suitable for environment variables.*


### apply (method, L85-L90, parent: BaseSecurityParameters)

> *Summary: This method applies security checks to incoming request parameters and body data. It takes query parameters, a body dictionary, and a security object as input, performing necessary validation or transformation internally without returning a value.*


### get_security_class (method, L92-L92, parent: BaseSecurityParameters)

> *Summary: Returns the specific security class instance associated with this object, adhering to the `BaseSecurity` interface. This method provides access to the underlying security implementation details.*


### dump (method, L94-L95, parent: BaseSecurityParameters)

> *Summary: This method requires subclasses to provide a concrete implementation for serializing their state into a dictionary. It currently raises an error if not overridden by derived classes.*


### to_env (method, L97-L101, parent: BaseSecurityParameters)

> *Summary: Converts internal security parameters into an environment-friendly dictionary format. It serializes the object's state using `json.dumps()` and wraps it under the "SECURITY" key.*


### UnsupportedSecurityStub (class, L104-L136)

> *Summary: This stub class represents an unsupported security mechanism, always returning `False` for support checks. It defines parameters that signal the use of this unsupported type when serialized or applied to requests.*


### is_supported (method, L111-L112, parent: UnsupportedSecurityStub)

> *Summary: This method checks if a given class supports a specific type based on provided schema parameters. Currently, it always returns `False` without implementing any actual support logic.*


### accept (method, L114-L117, parent: UnsupportedSecurityStub)

> *Summary: Checks if the current instance matches a specific security class derived from input parameters; if it does, it raises an error indicating unsupported stub usage, otherwise, it returns `False`.*


### Parameters (class, L119-L136, parent: UnsupportedSecurityStub)

> *Summary: This class defines security parameters for API Key Header authentication. It currently implements no specific logic in its `apply` method and reports itself as an unsupported security type when dumped or queried.*


### apply (method, L122-L128, parent: Parameters)

> *Summary: This method takes query parameters, a request body dictionary, and a security object as input. Its purpose is to apply the specified security rules to the incoming request data, though its current implementation does nothing.*


### get_security_class (method, L130-L131, parent: Parameters)

> *Summary: Returns a placeholder security class instance, indicating that the current object does not implement specific security logic. This method provides a default fallback when concrete security implementation is unavailable.*


### dump (method, L133-L136, parent: Parameters)

> *Summary: Returns a dictionary indicating an unsupported type when called. This method provides no specific data and always returns the same structure.*


### APIKeyHeader (class, L139-L171)

> *Summary: This class implements security using an API key passed in the HTTP header. It modifies the request body dictionary to inject the configured API key value into the `headers` section before execution.*


### Parameters (class, L145-L171, parent: APIKeyHeader)

> *Summary: This class configures API key header security by injecting a specific value into the request body's headers dictionary. It provides methods to retrieve the corresponding `APIKeyHeader` type and serialize its configuration for external use.*


### apply (method, L150-L161, parent: Parameters)

> *Summary: This method injects an API key into the request's headers dictionary within the provided body data. It takes query parameters, a mutable body dictionary, and a security object as input to modify the body in place.*


### get_security_class (method, L163-L164, parent: Parameters)

> *Summary: Returns the specific security implementation class, which is hardcoded to `APIKeyHeader`. This method provides the necessary security context for the proxy.*


### dump (method, L166-L171, parent: Parameters)

> *Summary: This method serializes the object into a dictionary representing an API key configuration. It combines fixed metadata defining it as a header-based API key with the instance's own serialized attributes.*


### APIKeyQuery (class, L174-L207)

> *Summary: This class defines security logic for authenticating via an API key passed in the query parameters. It manages how to inject a predefined `API_KEY` value into the request's query parameters during execution and serializes this configuration for documentation.*


### is_supported (method, L181-L182, parent: APIKeyQuery)

> *Summary: Delegates the support check to its parent class using the provided type and schema parameters. It returns a boolean indicating whether the current implementation supports the given configuration.*


### Parameters (class, L184-L207, parent: APIKeyQuery)

> *Summary: This class defines security parameters for API key authentication, specifically targeting query parameters. It injects the configured `API_KEY` value into the provided query parameters dictionary and can return a structured representation of its configuration.*


### apply (method, L189-L197, parent: Parameters)

> *Summary: This method injects a specific API key value into the query parameters dictionary based on the provided security configuration. It modifies the input `q_params` by adding an entry using the name defined in the security object and the instance's stored value.*


### get_security_class (method, L199-L200, parent: Parameters)

> *Summary: Returns the specific security implementation class, which is hardcoded to `APIKeyQuery`. This method provides a direct reference to the required security mechanism for the proxy.*


### dump (method, L202-L207, parent: Parameters)

> *Summary: This method serializes the object into a dictionary representing an API key parameter. It combines fixed metadata defining it as a query-based API key with the object's own serialized attributes.*


### APIKeyCookie (class, L210-L242)

> *Summary: This class implements security handling for API keys passed via cookies. It modifies the request body dictionary to inject the configured API key value into the `cookies` section before execution.*


### Parameters (class, L216-L242, parent: APIKeyCookie)

> *Summary: This class configures security parameters for API key authentication via cookies. It modifies the request body dictionary to inject the configured API key value into the `cookies` section, and provides methods to retrieve the associated cookie type or serialize its configuration.*


### apply (method, L221-L232, parent: Parameters)

> *Summary: This method injects an API key cookie into the request body dictionary using a provided security object and its associated cookie information. It ensures the "cookies" field exists in the input body before adding the necessary authentication cookie.*


### get_security_class (method, L234-L235, parent: Parameters)

> *Summary: Returns the specific security class instance, which is hardcoded to `APIKeyCookie`, based on the object's internal state. This method provides a direct reference to the active security implementation.*


### dump (method, L237-L242, parent: Parameters)

> *Summary: This method serializes the object into a dictionary representation suitable for API key configuration. It wraps the object's internal state (`self.model_dump()`) within a structure specifying the type as `"apiKey"` and the parameter location as `"cookie"`.*


### HTTPBearer (class, L245-L279)

> *Summary: This class implements HTTP Bearer authentication by defining how to check for support and apply the security scheme. It injects an `Authorization: Bearer <token>` header into the request body when applied.*


### is_supported (method, L252-L253, parent: HTTPBearer)

> *Summary: Checks if a class matches a specified type and if its internal value aligns with the "scheme" parameter provided in the input dictionary. Returns a boolean indicating support based on these two conditions.*


### Parameters (class, L255-L279, parent: HTTPBearer)

> *Summary: This class implements HTTP Bearer security by injecting an `Authorization: Bearer <token>` header into the request body's headers dictionary during application. It provides methods to retrieve the corresponding `HTTPBearer` security type and serialize its configuration for external use.*


### apply (method, L260-L269, parent: Parameters)

> *Summary: This method injects an authorization header into the request body dictionary using a bearer token derived from the instance's value. It ensures the "headers" key exists within the input `body_dict` before adding the security credential.*


### get_security_class (method, L271-L272, parent: Parameters)

> *Summary: Returns the `HTTPBearer` class, which defines the security mechanism for this proxy component. This method provides a direct reference to the required security implementation type.*


### dump (method, L274-L279, parent: Parameters)

> *Summary: This method serializes the object into a dictionary representation suitable for HTTP requests. It combines fixed security parameters, specifically setting the scheme to "bearer," with all attributes from the instance itself.*


### HTTPBasic (class, L282-L320)

> *Summary: This class implements HTTP Basic authentication by encoding a provided username and password into a Base64 string to set the `Authorization` header. It supports checking if it's applicable based on type and scheme parameters, and its parameters handle applying these credentials to request bodies.*


### is_supported (method, L289-L290, parent: HTTPBasic)

> *Summary: Checks if a class matches a specified type and if its internal value aligns with the "scheme" parameter provided in the input dictionary. Returns a boolean indicating support based on these two conditions.*


### Parameters (class, L292-L320, parent: HTTPBasic)

> *Summary: This class implements HTTP Basic authentication by encoding provided username and password into a Base64 string. It modifies the input body dictionary to inject this encoded credential into the `Authorization` header, returning an object describing its configuration for serialization.*


### apply (method, L298-L310, parent: Parameters)

> *Summary: This method injects basic HTTP authentication credentials into the request body's headers. It takes query parameters, a body dictionary, and a security object as input, modifying the body to include an `Authorization` header using Base64 encoding of the stored username and password.*


### get_security_class (method, L312-L313, parent: Parameters)

> *Summary: Returns the `HTTPBasic` class, which represents the security mechanism used by this proxy component. This method provides a direct reference to the configured security implementation.*


### dump (method, L315-L320, parent: Parameters)

> *Summary: This method serializes the object's state into a dictionary representation suitable for HTTP basic authentication. It combines fixed metadata with the object's current attributes via `model_dump()`.*


### OAuth2PasswordBearer (class, L323-L399)

> *Summary: This class defines the logic for OAuth2 Password Bearer authentication, handling security parameter generation and token acquisition. It takes credentials (username/password) and a token URL as input to automatically fetch an access token and apply it as a `Bearer` header to requests.*


### is_supported (method, L331-L332, parent: OAuth2PasswordBearer)

> *Summary: Checks if a given class supports a specific type while also verifying the presence of a "password" key within the provided schema parameters' flows. Returns `True` only if both conditions are met.*


### get_security_parameters (method, L335-L338, parent: OAuth2PasswordBearer)

> *Summary: Constructs a string representation of security parameters by extracting the name and constructing a full token URL from provided schema details. This output is formatted to instantiate a class using the retrieved values.*


### Parameters (class, L340-L399, parent: OAuth2PasswordBearer)

> *Summary: This class implements OAuth2 Password Bearer security by holding credentials like username and password. It can automatically fetch an access token using a provided `token_url` via the `get_token` method, which is then applied to requests in the `apply` method by setting the Authorization header.*


### get_token (method, L360-L371, parent: Parameters)

> *Summary: This method retrieves an access token by making a POST request to the provided `token_url`, using stored credentials (`self.username` and `self.password`) as input. It returns the extracted `"access_token"` string from the JSON response upon successful authentication.*


### apply (method, L373-L387, parent: Parameters)

> *Summary: This method injects an authorization header into the request body dictionary using a stored bearer token. It first ensures a token is available, fetching it if necessary via a configured token URL, and then adds the `Authorization: Bearer <token>` header to the provided input.*


### get_security_class (method, L389-L390, parent: Parameters)

> *Summary: Returns the `OAuth2PasswordBearer` class, which defines the security scheme for authentication within the proxy. This method provides a specific type reference based on the object's configuration.*


### dump (method, L392-L399, parent: Parameters)

> *Summary: Generates a dictionary representation of the current security configuration. It packages OAuth2 details, including token URLs and credentials like username, password, or bearer tokens, into a structured output.*

