---
icon: material/laptop
tags:
    - helm
    - kubernetes
---
# Helm deployment

## Introduction

This page describes a docker-compose based orchestration running on your local machine and accessible via browser.

The code examples in this section assumes that you have POSIX-compliant shell (linux, macOS or WSL for Windows).

## Requirements

-   Access credentials to eccenca Artifactory and eccenca Docker Registry → [contact us to get yours](https://eccenca.com/en/contact)
-   [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/) (v1) installed locally
-   [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally
-   At least 4 CPUs and 12GB of RAM (recommended: 16GB) dedicated to docker
