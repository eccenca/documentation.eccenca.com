---
title: "Download Git files"
description: "Download files from a git repository and hand them to the next task."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Download Git files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task reads files from a git repository at one revision and hands them
to the next task in the workflow. It works on the objects of the repository rather
than on a checkout, so only the files it selects are transferred.

Files leave the task as file entities that any file consuming task can read. They are
written into a temporary folder of the container the task runs in, and they are not
deleted afterwards, because the next task reads them only when it gets to them.

This task works in one of two mutually exclusive ways, decided by whether a
Repository URL is configured. Set it, and the task fetches on its own, guided by
the folder, expression and subfolder settings, with the input closed. Leave it
empty, and the input opens instead: it supplies both the repository and the
files to read from it, and the folder and expression settings go unused. This is
how **List Git files** drives this task after the workflow has filtered its
output.

The repository is reached over HTTP(S), which is the only transport these tasks speak;
an SSH address is refused. Reading needs a token with read access to the repository and
no more than that: the `read_repository` scope on GitLab, or a fine grained GitHub token
granting `Contents: Read-only`. A public repository needs no token at all. The user name sent
alongside the token matters on GitLab and not on GitHub, which is why its default is
the value GitLab accepts.

Submodules and files stored with Git LFS are reported as skipped rather than
downloaded, because the repository holds no content for them, only a reference. A
symbolic link is delivered under its own name with the content of the file it points
at; one that points outside the repository is skipped. Reading a commit id rather
than a branch or a tag works only where the server allows fetching an object it does
not advertise.


## Parameter

### Repository URL

The HTTP(S) address of the repository. The address of its web page works as well as its clone URL, with or without a trailing '.git'. Leave it empty to take the repository, and the files to read from it, from the connected input instead - which is how **List Git files** drives this task.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### Access token

An access token that may read the repository. Leave it empty to read a public repository.

- ID: `token`
- Datatype: `password`
- Default Value: `None`



### Revision

The branch, tag or commit id to read. Leave it empty to read the repository's default branch. Ignored when the Repository URL is empty and the input drives file selection instead.

- ID: `ref`
- Datatype: `string`
- Default Value: `None`



### Folder

The folder inside the repository to read from. Leave it empty to start at the top of the repository. Ignored when the Repository URL is empty and the input drives file selection instead.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Regular expression

A regular expression the file name has to match. An empty expression matches every file. Ignored when the Repository URL is empty and the input drives file selection instead.

- ID: `regex`
- Datatype: `string`
- Default Value: `None`



### No subfolder

If enabled, only files directly in the selected folder are used, and its subfolders are left alone. Ignored when the Repository URL is empty and the input drives file selection instead.

- ID: `no_subfolder`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### User name

The user name sent with the access token. GitHub ignores it, GitLab checks it, and the default is the value GitLab accepts for a repository token.

- ID: `username`
- Datatype: `string`
- Default Value: `gitlab-ci-token`
