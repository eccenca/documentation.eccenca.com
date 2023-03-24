---
title: "cmemc: Installation"
icon: material/download-circle-outline
tags:
  - cmemc
---
# Installation

cmemc can be installed using the python package from pypi.org, the release package or by pulling the docker image.

## ... via pypi.org

cmemc is available as an [official pypi package](https://pypi.org/project/cmem-cmemc/) so installation can be done with pip or pipx (preferred):

``` shell-session
$ pipx install cmem-cmemc
```

## ... via release package

The cmemc [release package](https://releases.eccenca.com/cmemc/) consists of the following files:

- `cmem_cmemc-vXX.YY.tar.gz` - the source package of cmemc
- `cmem_cmempy-vXX.YY.tar.gz` - the source package of cmempy (the used python API to access Corporate Memory)
- `cmemc_vXX.YY_Manual.pdf` - the cmemc documentation manual (this document)
- `cmemc_vXX.YY_Manual.ttl` - the cmemc documentation as structured data (RDF graph)
- `requirements.txt` - additional requirements needed by cmemc

The following script demonstrates how to install cmemc from these files:

``` shell-session
$ pip install -r requirements.txt
...
$ pip install cmem_cmempy-v22.1.tar.gz
...
$ pip install cmem_cmemc-v22.1.tar.gz
...
$ cmemc --version
cmemc, version 22.1, running under python 3.9.11
```

## ... via docker image

This topic is described on a [stand-alone page](../invocation/docker-image/index.md).


!!! Note

    Once you have installed cmemc, you need to configure a connection with a [config file](../configuration/file-based-configuration/index.md) or learn how to [use environment variables](../configuration/environment-based-configuration/index.md) to control cmemc.

