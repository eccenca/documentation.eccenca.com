---
title: "OAuth2 Authentication"
description: "Provide an OAuth2 access token for other tasks (via config port)."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# OAuth2 Authentication
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Provide an OAuth2 access token for other tasks (via config port).

This task uses the provided client or user credentials and runs an OAuth2
authorization to the given service URL. It will fetch the output and provide the
token in a way that it can be used by other tasks to access the service.

Note: The consuming task needs to have the parameter `oauth_access_token` in order to
to use the output this task. You need to connect this task to the
**config port** of the consuming task.


## Parameter

### Grant Type

Select the used OAuth Grant Type in order to specify how this plugin gets a valid token. Depending on the value of this parameter, other authentication related parameter will become mandatory or obsolete. The following values can be used: - `client_credentials`: - this refers to the OAuth 2.0 Client Credentials Grant Type. Mandatory parameter for this grant type are Client ID and Client Secret. - `password` - this refers to the OAuth 2.0 Password Grant Type. Mandatory variables for this grant type are Client ID, User name and Password.

- Datatype: `string`
- Default Value: `client_credentials`



### Token Endpoint

This is the OpenID Connect (OIDC) OAuth 2.0 token endpoint location (a HTTP(S) URL).

- Datatype: `string`
- Default Value: `None`



### Client ID

The Client ID obtained during registration.

- Datatype: `string`
- Default Value: `None`



### Client Secret

The Client Secret obtained during registration.

- Datatype: `string`
- Default Value: `None`



### Username

The user account name used for authentication.

- Datatype: `string`
- Default Value: `None`



### Password

The user account password.

- Datatype: `string`
- Default Value: `None`



