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
pipx install cmem-cmemc
```

## ... via docker image

This topic is described on a [stand-alone page](../invocation/docker-image/index.md).

!!! Note

    Once you have installed cmemc, you need to configure a connection with a [config file](../configuration/file-based-configuration/index.md) or learn how to [use environment variables](../configuration/environment-based-configuration/index.md) to control cmemc.
