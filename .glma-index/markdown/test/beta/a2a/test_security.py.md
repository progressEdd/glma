# test/beta/a2a/test_security.py

3 function(s): test_http_auth_scheme_basic, test_open_id_connect_scheme, test_mtls_scheme. 5 class(es): TestBearerScheme, TestApiKeyScheme, TestOAuth2Scheme, TestWithScopes, TestRequire. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestBearerScheme | class |  |
| test_http_auth_scheme_basic | function |  |
| TestApiKeyScheme | class |  |
| TestOAuth2Scheme | class |  |
| test_open_id_connect_scheme | function |  |
| test_mtls_scheme | function |  |
| TestWithScopes | class |  |
| TestRequire | class |  |

## Chunks

### TestBearerScheme (class, L30-L53)

> *Summary: Verifies that the `bearer_scheme` factory correctly constructs a `Scheme` object, either defaulting to JWT or accepting custom formats and descriptions for bearer authentication. It tests how the function initializes security schemes based on provided arguments.*


### test_defaults_to_jwt (method, L31-L39, parent: TestBearerScheme)

> *Summary: This test verifies that a default `bearer` scheme correctly configures itself to use JWT as the authentication format. It asserts that the resulting security scheme object matches an expected structure containing the "bearer" HTTP authentication scheme with "JWT" specified for the bearer format.*


### test_custom_format_and_description (method, L41-L53, parent: TestBearerScheme)

> *Summary: This test verifies that a custom scheme object is correctly constructed when initialized with specific parameters. It asserts the resulting structure matches an expected `SecurityScheme` containing an `HTTPAuthSecurityScheme` configured for bearer authentication with opaque format and a given description.*


### test_http_auth_scheme_basic (function, L56-L64)

> *Summary: This test verifies the correct construction of an HTTP authentication scheme using the "basic" method. It asserts that a created `Scheme` object accurately reflects the provided name and nested security details.*


### TestApiKeyScheme (class, L67-L86)

> *Summary: These tests verify the correct construction of API key security schemes when initializing them with different locations. They assert that the resulting `Scheme` object accurately reflects whether the key is expected in a header or as a query parameter.*


### test_header_default (method, L68-L76, parent: TestApiKeyScheme)

> *Summary: This test verifies that the `api_key_scheme` function correctly constructs a specific security scheme object. It asserts that the resulting structure matches an expected configuration using "api-key" as the name and "X-API-Key" in the header location.*


### test_query_location (method, L78-L86, parent: TestApiKeyScheme)

> *Summary: This test verifies the correct construction of a security scheme where an API key is expected to be passed via a query parameter. It asserts that the resulting `Scheme` object matches the expected structure containing an `APIKeySecurityScheme` configured for "query" location.*


### TestOAuth2Scheme (class, L89-L116)

> *Summary: Verifies the correct construction of OAuth 2.0 security schemes by testing initialization with client credentials and authorization code flows, including optional metadata URLs. It asserts that the resulting scheme object accurately reflects the provided flow configurations.*


### test_with_client_credentials_flow (method, L90-L97, parent: TestOAuth2Scheme)

> *Summary: This test verifies the correct construction of an OAuth 2.0 security scheme using client credentials flow. It asserts that a defined `OAuthFlows` object, containing a specific token URL, results in the expected `SecurityScheme` structure when passed to the `oauth2_scheme` helper.*


### test_with_authorization_code_flow_and_metadata_url (method, L99-L116, parent: TestOAuth2Scheme)

> *Summary: This test verifies the correct construction of an OAuth 2.0 security scheme configuration. It asserts that a defined `OAuthFlows` structure, including specific authorization and token URLs, is correctly encapsulated within a `SecurityScheme` object when initialized with metadata URL information.*


### test_open_id_connect_scheme (function, L119-L129)

> *Summary: This test verifies that the `open_id_connect_scheme` function correctly constructs a `Scheme` object containing an `OpenIdConnectSecurityScheme`. It asserts that the resulting structure matches the expected configuration using provided name and URL inputs.*


### test_mtls_scheme (function, L132-L140)

> *Summary: This test verifies the correct construction of a security scheme configured for Mutual TLS. It asserts that an input name and description correctly result in a `Scheme` object containing a `MutualTlsSecurityScheme`.*


### TestWithScopes (class, L143-L158)

> *Summary: This class tests the behavior of an OAuth scheme object when scopes are added or modified. It verifies that adding scopes creates a new, distinct instance with the specified scopes while leaving the original object unchanged.*


### test_attaches_scopes (method, L144-L151, parent: TestWithScopes)

> *Summary: This test verifies that applying specific scopes to an OAuth scheme correctly modifies the resulting object. It asserts that the new object retains the original name and scheme while accurately containing the provided list of scopes.*


### test_returns_a_copy (method, L153-L158, parent: TestWithScopes)

> *Summary: This test verifies that applying scopes to an OAuth object does not modify the original scope list, ensuring a copy is returned or used internally. It initializes an OAuth scheme with no scopes and asserts that its `scopes` attribute remains empty after calling `with_scopes("read")`.*


### TestRequire (class, L161-L202)

> *Summary: These tests verify the `require` function's behavior when accepting one or more authentication schemes as input. It confirms that the resulting requirement object correctly aggregates these schemes, handles scope additions for specific OAuth flows, and preserves scheme names regardless of their format.*


### test_single_scheme (method, L162-L167, parent: TestRequire)

> *Summary: This test verifies that a requirement object correctly accepts and stores a single scheme, specifically the "bearer" type. It asserts that the resulting `Requirement` instance contains only the provided bearer scheme in its list of schemes.*


### test_multiple_schemes_and (method, L169-L175, parent: TestRequire)

> *Summary: This test verifies that a requirement object correctly aggregates multiple authentication schemes. It constructs and asserts an instance containing both a bearer token scheme and an API key scheme.*


### test_scheme_with_scopes (method, L177-L183, parent: TestRequire)

> *Summary: This test verifies that an OAuth scheme, when configured with specific scopes ("read" and "write"), correctly exposes those scopes in its generated protocol definition. It asserts that the `list` within the scheme's structure contains exactly these specified scope strings.*


### test_mix_scoped_and_unscoped (method, L185-L194, parent: TestRequire)

> *Summary: This test verifies that a request requiring both bearer and OAuth schemes correctly merges them into a protocol representation. It asserts that the resulting proto contains both scheme types, with the OAuth scheme specifically listing the "read" scope while the bearer scheme lists no scopes.*


### test_non_identifier_scheme_name (method, L196-L202, parent: TestRequire)

> *Summary: This test verifies that a scheme name provided without an identifier results in an empty list within the generated protocol structure. It constructs a bearer scheme with a non-identifier name and asserts the corresponding entry in the proto object has no listed schemes.*

