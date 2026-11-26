# Screen recordings

The scripts in this folder record the short WebM clips that the tutorials embed, one clip per step.
A script drives a headless Chrome through the product, draws a mouse pointer, types at a readable pace and
records the page.
Afterwards the still pauses are shortened and the clip is encoded for the documentation.

When the product changes, adjust the affected click steps and record again.

The pace of a clip follows the rule in
[`.claude/docs-guidelines/repo-conventions.md`, section "Screen recordings"](../../.claude/docs-guidelines/repo-conventions.md#screen-recordings).
The building blocks in `lib/` implement it, so a tutorial script only describes the steps.

## Prerequisites

- Node.js 18 or later, Python 3, Google Chrome or Chromium
- [ffmpeg](https://ffmpeg.org/) with `ffprobe`, built with `libvpx`
- [cmemc](../../docs/automate/cmemc-command-line-interface/index.md), for the scripts that reset the test data
- A test instance of Corporate Memory with the data the tutorial needs.
    Never record against a customer deployment, and never show customer data.

The dependencies are installed into `node_modules/` on the first run, which git ignores.

## Configuration

The scripts read their configuration from environment variables.
`task` loads them from the file `.env` in the root of the repository, which git ignores:

```shell
# the test instance, also used by cmemc in the reset scripts
CMEM_BASE_URI=http://docker.localhost
OAUTH_GRANT_TYPE=password
OAUTH_CLIENT_ID=cmemc
# the account that signs in, in the browser and in cmemc
OAUTH_USER=admin
OAUTH_PASSWORD=admin
# optional
CHROME_PATH=/path/to/chrome    # default: the usual install locations
FFMPEG_PATH=/path/to/ffmpeg    # default: ffmpeg on the PATH; ffprobe is taken from the same folder
TTYD_URL=http://127.0.0.1:7681 # terminal clips only
```

Keep these variables in `.env` instead of exporting them in the shell.
Exported `OAUTH_*` variables leak into other tools started from that shell, for example `docker compose` of a
local Corporate Memory, and break their configuration.

## Record the clips of a tutorial

```shell
task record -- companion-catalog              # all clips
task record -- companion-catalog --dry        # run the steps without recording
task record -- companion-catalog --clips 5,6  # only some clips
task record -- companion-catalog --install    # also copy the clips into the tutorial
```

A run resets the test data first when it includes the first clip, then records the clips in one browser
session, because the clips build on each other.
The results go to `dist/recordings/<tutorial>/`:

- `<prefix><clip>.webm`, the finished clip
- `<prefix><clip>.png`, its poster, the last frame
- `raw/`, the unedited recordings and a screenshot of the end of each clip

With `--install`, the clips and posters are copied into the documentation folder of the tutorial.

Before committing new clips:

- Run with `--dry` first and look at the end screenshots in `raw/`.
- Check the stored result through the API or cmemc, not only on screen.
    A clip can look right and still have saved an incomplete form.
- Watch every clip at full speed, especially the typing.
- Check every AI answer shown in a clip against the data.
    A clip can define a `check`, which records the clip again when the answer is wrong.

## Add a tutorial

1. Create a folder named after the tutorial, for example `change-journal/`.
2. Add `tutorial.js`, which exports:
    - `docs`, the documentation folder of the tutorial
    - `prefix`, the file name prefix of the clips, for example `change-journal-`
    - `clips`, one entry per step with `name`, `run(page)` and optionally `keep`, `tail`, `check(page)` and
      `retries`
    - optionally `setup(page)`, `beforeClip(page, number, first)` and `teardown(page)` for steps off camera
3. Add `reset.sh` if the tutorial creates data, so that every run starts from the same state.
4. Write the steps with the building blocks of `lib/browser.js`: `go`, `find`, `click`, `type` and `glide`.
    `click` moves the pointer visibly and pauses as the pace rule asks, and `type` types long texts faster.

`companion-catalog/tutorial.js` is a complete example, including forms, multiselects and a chat answer that is
checked.
`review-agent-changes/tutorial.js` combines terminal clips of Claude Code with clips in the browser.

## Terminal clips

A terminal clip, for example of Claude Code working through the Build MCP server, is recorded through
[ttyd](https://github.com/tsl0922/ttyd), which serves a terminal as a web page.
`lib/terminal.js` opens it with the DOM renderer, since the default WebGL renderer stays blank in a headless
browser.

Start ttyd only for the recording, bound to the local machine and with input allowed:

```shell
ttyd -i 127.0.0.1 -p 7681 -W zsh -l
```

While ttyd runs, every program on the machine can run commands in that shell through port 7681.
Stop it with Ctrl+C after the recording.

Open the browser with `open({ pointer: false })`: nothing is clicked in a terminal.
The building blocks prepare the terminal off camera:

- `prepare` moves to a neutral working folder and sets the prompt to `$`, so that no user name, path or branch
  name is shown.
- `startClaude` starts Claude Code in its default permission mode, so that the clip shows its permission
  prompts, and without its shell tool (`--disallowedTools Bash`), so that it works only through the Build MCP
  server.
    It confirms the trust question of a new folder and hides the rows of the start screen with the version,
    the account, the plan and promotional notices.
    Claude Code redraws its start screen, so clearing the screen does not remove it.
    With `allowed`, tools such as the read-only tools of the Build MCP server run without a permission prompt,
    so that the clip shows only the prompts of the tools that change something.
    With `disallowed`, further tools are switched off, for example `AskUserQuestion`.
- `exitClaude` ends Claude Code.
    Closing the browser alone leaves the process running under ttyd.

The agent runs on the account of the person recording and uses its quota, once per recording attempt.
