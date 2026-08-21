---
title: "cmemc: Troubleshooting and Caveats"
subtitle: and Caveats
icon: material/lightbulb-multiple-outline
tags:
  - cmemc
---
# Troubleshooting and Caveats

This page lists and documents possible issues and warnings when working with cmemc.

## Proxy is in the way

If you feel that your system's proxy configuration negatively impacts the communication between cmemc and Corporate Memory, you can disable using any proxy by setting this variable:

``` shell-session
export no_proxy='*'
```

cmemc uses [httpx](https://www.python-httpx.org/) for its HTTP requests, which picks up the proxy configuration from the environment in the same way as described for [python's urllib](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies).

> The no_proxy environment variable can be used to specify hosts which shouldn’t be reached via proxy;
> if set, it should be a comma-separated list of hostname suffixes, optionally with :port appended,
> for example cern.ch,ncsa.uiuc.edu,some.host:8080.

## Version warnings

cmemc is released together with Corporate Memory and each version is built against a matching backend version.
If you use a cmemc version which is newer than your deployment, it warns you once per run:

``` shell-session
Your DataIntegration version v26.1 is lower than the target version of your cmemc deployment (v26.2).
Some feature may be not supported with this backend.
```

This is a warning, not an error - cmemc continues to work, but commands which rely on newer API endpoints can fail.
Use a cmemc version which matches your deployment to avoid this.

A similar warning is shown when cmemc runs on a python version it was not tested with:

``` shell-session
Warning: You are running cmemc under a non-tested python environment (3.12).
```

cmemc requires **Python 3.13 or newer** and is tested with 3.13 and 3.14.
Refer to the [Installation](../installation/index.md) page for the recommended installation methods.

## Gateway Time-out

A gateway timeout occurs if your Corporate Memory infrastructure is not setup correctly.

``` shell-session
$ cmemc -c my-cmem project import my-project.zip my-project
Import file my-project.zip to project my-project ... 504 Server Error: Gateway Time-out for url: https://my-cmem/dataintegration/workspace/projects
```

This can have multiple reasons - please check in the following order:

- `application.yaml` of DataIntegration
- reverse proxy configuration
