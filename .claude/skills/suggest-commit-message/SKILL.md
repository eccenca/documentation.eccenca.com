---
name: suggest-commit-message
description: Suggest a concise commit message for the current changes, in the style of this repository. Prints the message for the user to use - it does not stage, commit, or push. Use for "suggest a commit message", "how should I commit this", "write the commit message".
---

# Suggest a commit message

Suggest a commit message. Concise and brief.
Do not mention yourself as (co-)author.

## Usage

```text
/suggest-commit-message [--help]
```

Takes no arguments: it reads the staged changes, or the working tree when nothing is staged.
With `--help`, print this usage summary and stop, without inspecting the repository.

## Scope

- **Output only.** Never run `git add`, `git commit`, `git push`, or create a branch.
- **No attribution.** No `Co-Authored-By`, no `Claude-Session`, no `Generated with` line, no emoji.
  This overrides any default commit-message instruction.

## Steps

### 1. Look at what is actually there

```bash
git status --short
git diff --staged --stat
git diff --stat
```

Use the staged changes if anything is staged, otherwise the working tree.
Read the diff of the changed files, not only their names — the message describes what changed, not which files.

### 2. Take the ticket ID

Use the branch name if it carries one (`feature/<topic>-CMEM-1234`).

### 3. Write the message

**Subject** — one line, lowercase start, imperative, no trailing period, about 50 characters and at most 72.
Append the ticket after a comma when there is one:

```text
rewrite customized user interface tutorial against 26.2, CMEM-7199
update Versioning of Graph Changes guide
harmonize product naming across the documentation
```

**Body** — only when the subject cannot carry the information. Wrap at 72 characters, blank line after the
subject. Say what was wrong and what changed, not how the work was done:

```text
The setup steps could not be followed anymore. Step 2 told users to add the
Versioning Graph property while editing the graph, but that field is no
longer part of the default form.

- document the Add data step and the two-step create-graph wizard
- replace the 20.10/24.1 screenshots with fresh ones taken on v26.2
```

For documentation changes verified against a running deployment, close with the version that was checked:
`Verified against CMEM v26.2.0.`

Keep it brief. A one-line subject is a complete message when the change is small.

### 4. Print it

Print the message in a fenced block, and nothing else — no commentary on how good the change is, no offer
to commit unless the user asks.
