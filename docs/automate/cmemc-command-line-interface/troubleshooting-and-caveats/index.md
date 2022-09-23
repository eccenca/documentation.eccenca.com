---
tags:
  - cmemc
---
# Current:Troubleshooting and Caveats

This page lists and documents possible issues and warnings when working with cmemc.

## Proxy is in the way

If you feel that your systems proxy configuration troubles the communication between cmemc and Corporate Memory, you can disable the usage of any proxy by setting this variable:

``` shell-session
export no_proxy='*'
```

This is due to the [python requests library proxy handling](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies).

> The no_proxy environment variable can be used to specify hosts which shouldn’t be reached via proxy;
> if set, it should be a comma-separated list of hostname suffixes, optionally with :port appended,
> for example cern.ch,ncsa.uiuc.edu,some.host:8080.

## Gateway Time-out

A gateway time-out occurs if your Corporate Memory infrastructure ins not setup correctly.

``` shell-session
$ cmemc -c my-cmem project import my-project.zip my-project
Import file my-project.zip to project my-project ... 504 Server Error: Gateway Time-out for url: https://my-cmem/dataintegration/workspace/projects
```

This can have multiple reasons - please check in the following order:

- `application.yaml` of DataIntegration
- reverse proxy configuration

