---
title: "List Git files"
description: "List the files of a git repository, without transferring their content."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# List Git files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task lists the files a git repository holds at one revision. It reads
the repository over HTTP(S) and transfers the directory listing only, never the
content of a file.

Each file leaves the task as one entity with its repository path, its name, its size
in bytes, its git file mode, the id of its content, the id of the commit that was
read, and this task's own Repository URL. The task takes no input.

The size is the one value that may be missing. A git tree records a name, a mode and
an object id, but not a length, so a file's size is only known once its content has
been transferred. Against a server that supports partial fetching - GitHub and GitLab
both do - this task deliberately does not transfer content, and the size stays empty;
against a server that does not, the content arrives anyway and the size is filled in.

It is usually the first task of a chain: filter its output in the workflow, then
connect it to **Download Git files**, which then fetches exactly the files that
survived the filtering. Leave Download's own Repository URL empty for this -
it then reads the URL from this task's output as well, rather than needing it
configured a second time.

The repository is reached over HTTP(S), which is the only transport these tasks speak;
an SSH address is refused. Reading needs a token with read access to the repository and
no more than that: the `read_repository` scope on GitLab, or a fine grained GitHub token
granting `Contents: Read-only`. A public repository needs no token at all. The user name sent
alongside the token matters on GitLab and not on GitHub, which is why its default is
the value GitLab accepts.

Submodules and files stored with Git LFS are reported as skipped rather than listed,
because neither holds content the repository can hand out. A symbolic link is listed
under its own name, carrying the size and the content id of the file it points at;
one that points outside the repository is skipped. Reading a commit id rather than a
branch or a tag works only where the server allows fetching an object it does not
advertise.

The task reads one revision and nothing around it. It answers no question about
history: when a file last changed, who changed it, or how two revisions differ are
all outside what these tasks do, because none of it can be had without fetching the
history the design deliberately leaves on the server.


## Parameter

### Repository URL

The HTTP(S) address of the repository. The address of its web page works as well as its clone URL, with or without a trailing '.git'.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### Access token

An access token that may read the repository. Leave it empty to read a public repository.

- ID: `token`
- Datatype: `password`
- Default Value: `None`



### Revision

The branch, tag or commit id to read. Leave it empty to read the repository's default branch.

- ID: `ref`
- Datatype: `string`
- Default Value: `None`



### Folder

The folder inside the repository to read from. Leave it empty to start at the top of the repository.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Regular expression

A regular expression the file name has to match. An empty expression matches every file.

- ID: `regex`
- Datatype: `string`
- Default Value: `None`



### No subfolder

If enabled, only files directly in the selected folder are used, and its subfolders are left alone.

- ID: `no_subfolder`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### User name

The user name sent with the access token. GitHub ignores it, GitLab checks it, and the default is the value GitLab accepts for a repository token.

- ID: `username`
- Datatype: `string`
- Default Value: `gitlab-ci-token`
