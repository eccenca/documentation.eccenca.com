---
title: "Upload Git files"
description: "Commit the files of the preceding task into a git repository."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Upload Git files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task commits the files it receives into a folder of a git repository
and pushes them, as one commit per execution. It builds the commit from the objects
of the repository rather than from a checkout, so nothing is cloned.

Files arrive on the input from any task that produces files. The task hands nothing
on: it is the last step of its chain, and it has no output.

It is the counterpart of **Download Git files**, and a workflow that reads a
repository, changes something and writes the result back usually ends here.

The repository is reached over HTTP(S), which is the only transport this task speaks; an
SSH address is refused. Committing needs a token with write access: the
`write_repository` scope on GitLab, or a fine grained GitHub token granting
`Contents: Read and write`. On GitLab the token's role has to allow pushing to the target
branch as well, which a protected branch restricts to maintainers by default, and the
user name sent alongside the token is checked, which is why its default is the value
GitLab accepts. The
*Check connection* action asks the server for a write handshake and reports what it
answered, so a token that is not sufficient can be found before a workflow runs.

Every file is committed under its own name in the target folder; a folder structure
it carried before is not reproduced, and two files that would end up under the same
name abort the execution before anything is written. When the files are identical to
what the repository already holds, no commit is created at all. Files excluded by the
repository's ignore rules are committed unless that is switched off. A branch that
moved while the task was working is not overwritten: the same files are applied to
the new tip and pushed again, and the task fails rather than discarding the other
change. A push the repository refuses - a protected branch, or a hook that declines
it - fails with the reason the server gave, and nothing is committed.

The task writes a branch and stops there. It opens no merge request and no pull
request, it creates no tag and no release, and the commits it writes are not signed.
A file committed into a path the repository tracks with Git LFS is stored as ordinary
content rather than as an LFS pointer, so do not point this task at such a path.


## Parameter

### Repository URL

The HTTP(S) address of the repository. The address of its web page works as well as its clone URL, with or without a trailing '.git'.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### Access token

An access token that may write to the repository.

- ID: `token`
- Datatype: `password`
- Default Value: `None`



### Branch

The branch to commit to. It is created from the repository's default branch when it does not exist yet. Leave it empty to commit to the default branch.

- ID: `ref`
- Datatype: `string`
- Default Value: `None`



### Folder

The folder inside the repository to commit into. Leave it empty to commit at the top of the repository.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Commit message

The message of the commit this task creates.

- ID: `commit_message`
- Datatype: `multiline string`
- Default Value: `Update files from an eccenca Corporate Memory workflow`



### Remove obsolete files

If enabled, files lying directly in the target folder that were not part of this execution are deleted in the same commit. Its subfolders, and everything outside it, are never touched.

- ID: `remove_obsolete`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### User name

The user name sent with the access token. GitHub ignores it, GitLab checks it, and the default is the value GitLab accepts for a repository token.

- ID: `username`
- Datatype: `string`
- Default Value: `gitlab-ci-token`



### Honor ignore rules

If enabled, a file excluded by the repository's .gitignore is reported and left out instead of being committed.

- ID: `honor_gitignore`
- Datatype: `boolean`
- Default Value: `false`



### Author name

The name the commit is attributed to. Left empty, the name of the user who runs the workflow is used where the deployment provides it.

- ID: `author_name`
- Datatype: `string`
- Default Value: `None`



### Author mail address

The mail address the commit is attributed to. Left empty, the address of the user who runs the workflow is used where the deployment provides it.

- ID: `author_mail`
- Datatype: `string`
- Default Value: `None`
