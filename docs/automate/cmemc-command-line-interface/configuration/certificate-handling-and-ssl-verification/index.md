---
title: "cmemc: Certificate handling and SSL verification"
subtitle: and SSL verification
icon: material/server-security
tags:
    - Security
    - cmemc
---
# Certificate handling and SSL verification

## Introduction

In a reasonable production deployment, all client-accessible Corporate Memory APIs will be securely available as HTTPS endpoints.
This document clarifies how to deal with certificates.
cmemc will validate the certificates of your HTTPS endpoints and indicate validation errors.
If the certificates of your Corporate Memory deployment are based on a common and publicly available Certificate Authority (such as [Let's Encrypt](https://letsencrypt.org/)), cmemc is able to validate your certificates out of the box.

However, in some cases you need to do one of the following:

- provide your own certificates CA bundle in order to allow cmem to trust your servers
- disable SSL verification entirely (for debugging and testing purpose only)

## Provide your own CA bundle

cmemc will validate all used certificates of your HTTPS API endpoints by using a built-in CA bundle that comes from python's [certifi package](https://pypi.org/project/certifi/).

> Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.

If you need to configure a custom CA bundle to use with a specific connection, you can do so by using the `REQUESTS_CA_BUNDLE` key in the config or as an environment variable.

You can validate which CA bundle is used by switching on debugging (`–debug`) and watch for a CA bundle debug line (here, line 10).

``` shell-session title="using the debug mode to watch for the CA bundle"
$ cmemc --debug -c ssltest.eccenca.com graph list
[2020-03-11 17:50:59.135898] Set config to /home/user/Library/Application Support/cmemc/config.ini
[2020-03-11 17:50:59.136284] Config loaded: /home/user/Library/Application Support/cmemc/config.ini
[2020-03-11 17:50:59.137476] Use connection config: ssltest.eccenca.com
[2020-03-11 17:50:59.137564] CMEM_BASE_URI set by config to https://ssltest.eccenca.com
[2020-03-11 17:50:59.137611] REQUESTS_CA_BUNDLE set by config to cacert.pem
[2020-03-11 17:50:59.137718] OAUTH_GRANT_TYPE set by config to client_credentials
[2020-03-11 17:50:59.137760] OAUTH_CLIENT_ID set by config to cmem-service-account
[2020-03-11 17:50:59.137804] OAUTH_CLIENT_SECRET set by config
[2020-03-11 17:50:59.137978] CA bundle loaded from /home/user/cacert.pem
http://di.eccenca.com/project/cmem
urn:elds-backend-access-conditions-graph
```

The CA bundle must be available in PEM format.
You can use the [openssl command line tool](https://www.openssl.org/) to fetch all certificates from an HTTPS URL and create a PEM CA Bundle out of it.

Here is an example line producing the cacert.pem file used in the example above:

``` shell-session
$ openssl s_client -showcerts -connect ssltest.eccenca.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >cacert.pem
$ cat cacert.pem
-----BEGIN CERTIFICATE-----
MIIFyzCCA7MCFDoiAY9Ry8dfH0rS/rINUb6inlvGMA0GCSqGSIb3DQEBCwUAMIGh
[...]
miGId7jMXd24bpfYZSiniC0+SHiCwEmzN818Ss9aIMChymAnV3RRB/UqKLlOMnA=
-----END CERTIFICATE-----
```

## Disabling SSL Verification at all

You can also disable SSL Verification completely by setting the `SSL_VERIFY` key in the config or environment to `false`.

However, this will lead to warnings:
``` shell-session
$ cmemc -c ssltest.eccenca.com graph list
SSL verification is disabled (SSL_VERIFY=False).
http://di.eccenca.com/project/cmem
urn:elds-backend-access-conditions-graph
```

