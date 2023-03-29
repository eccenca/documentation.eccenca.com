# Contributing

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing to the eccenca Corporate Memory documention project.

## How Can I Contribute?

### Report Bugs

If you found a bug and its easy to fix, you can just click the edit button and fix it yourself sending a pull request 🤓.
However, you can also [file a bug](https://github.com/eccenca/documentation.eccenca.com/issues/new?assignees=&labels=bug&template=bug.yml&title=%5BBug%5D%3A+) in the [issue tracker](https://github.com/eccenca/documentation.eccenca.com/issues) of this project.

### Suggest Enhancements

You always can [suggest enhancements](https://github.com/eccenca/documentation.eccenca.com/issues/new?assignees=&labels=enhancement&template=request.yml&title=%5BRequest%5D%3A+) in the [issue tracker](https://github.com/eccenca/documentation.eccenca.com/issues) of this project.

### Send Pull Requests

We are open for contributions via pull request.
Try to test your contribution locally before pushing your changes.

## What should I know before I get started?

<details>
  <summary>Extend section</summary>

This documentation project is made with [mkdocs](https://www.mkdocs.org/) and the [material theme for mkdocs](https://squidfunk.github.io/mkdocs-material/).
The documentation is written in [markdown](https://commonmark.org/) and the project dependency management is done by [poetry](https://python-poetry.org/).
We suggest to use a specialized markdown editor such as [obsidian](https://obsidian.md/) if you plan to not just fix a typo.

The following tools you need locally to get started:

-   [poetry](https://python-poetry.org/)
-   [task](https://taskfile.dev/)
-   git, markdown editor

On a few OS distributions (e.g. Arch Linux) the tool/binary is named `go-task`.

The following shell session demonstrates the local workflow (after you forked the repository):

``` shell-session
$ git clone <your repository fork>
Cloning into 'documentation.eccenca.com'...
...
$ cd documentation.eccenca.com/
$ task serve
task: [install] poetry install
Creating virtualenv in ...
Installing dependencies from lock file

Package operations: 62 installs, 0 updates, 0 removals
...
task: [serve] poetry run mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 20.03 seconds
INFO     -  [16:25:36] Watching paths for changes: 'docs', 'mkdocs.yml', 'overrides'
INFO     -  [16:25:36] Serving on http://127.0.0.1:8000/
```

After that, you can go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and start changing / adding files in the docs directory.
Changes are served live on localhost.

Note that some python packages need corresponding C libraries, which you may have to install as well.
Have a look at the [mkdocs-material documentation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/?h=cairo#dependencies) and the [build plan](https://github.com/eccenca/documentation.eccenca.com/blob/main/.github/workflows/test.yml#L54) for a list.
</details>

## General Repository rules

<details>
  <summary>Extend section</summary>

-   always create a directory + `index.md`, e.g. `my-topic/index.md` ([Example](https://github.com/eccenca/documentation.eccenca.com/tree/main/docs/automate/cmemc-command-line-interface))
-   add new pages to the `.pages` file to add them in the right order and with correct title to the menu ([Example](https://github.com/eccenca/documentation.eccenca.com/blob/main/docs/automate/cmemc-command-line-interface/.pages))
-   put images side by side to the `index.md` ([Example](https://github.com/eccenca/documentation.eccenca.com/tree/main/docs/release-notes/corporate-memory-22-1))
-   do not use images for icons esp. icons from the application
    -   use eccenca icons, e.g. [:eccenca-application-queries:](https://github.com/eccenca/documentation.eccenca.com/blob/main/overrides/.icons/eccenca/application-queries.svg) -> [list](https://github.com/eccenca/documentation.eccenca.com/tree/main/overrides/.icons/eccenca)
    -   use theme icons where no eccenca icon is available -> [list](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search)
-   name image files properly (not just `Screenshot.xxx.png`, [Example](https://github.com/eccenca/documentation.eccenca.com/tree/main/docs/release-notes/corporate-memory-22-1))
-   used advanced features where suitable
    -   [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage) (esp. use notes and warnings where needed) -> see Admonition section for more details
    -   [Code Blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#usage) (e.g. enable highlightning and add a title)
    -   [Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage) (to structure complex pages)
-   code blocks:
    -   do not use line numbers except you refer to it in the text
    -   use correct syntax highlightning (often used: `shell-session`, `bash`, `sparql`, `turtle`, `json`) -> [list of syntax IDs](https://pygments.org/docs/lexers/)
    -   do not confuse `shell-session` with `bash` (the first is a terminal output, the latter a script syntax)
    -   when using `shell-session`, use `$` as the prompt
-   Links:
    -   do not use absolute links for internal documents, e.g. `https://documentation.eccenca.com/latest/...`
    -   do not use base-relative links, e.g. `/automate/...`
    -   use relative links to `index.md` files

</details>

## Admonitions

<details>
  <summary>Extend section</summary>

|Admonition Name|Used For |Example|
|---------------|---------|-------|
|Info |Information in documentation provides details about a topic or process that the reader needs to know. It is usually essential and relevant to the main subject of the document.|Statement annotations provide a way to express knowledge about statements. This group is dedicated to properties that configure the Statement Annotation feature|
|Note |A note provides additional details that may or may not be directly related to the main topic. It could be an explanation, clarification, or an aside that the writer thinks would be helpful for the reader to know.|The graph selection drop-down might or might not be visible depending the existence of an (optional) EasyNav Module configuration. In case no specific module configuration exists or non has not has been set for the current workspace the graph selection will be shown. A EasyNav Module configuration pre-configures a graph. Thus, the dropdown will not be shown if such has been configured for the current workspace.|
|Abstract|An abstract is a brief summary that provides an overview of the main points or contents of a document. It typically appears at the beginning of a document and is intended to give the reader an idea of what to expect from the document.|This tutorial explores the benefits of using cloud computing in enterprise organizations. It discusses the advantages of cloud computing over traditional on-premises infrastructure, and provides guidance for migrating to the cloud.|
|Warning|It is used to convey the seriousness of the risk and the importance of taking necessary precautions to avoid harm.|If the remote file resource is used in more than one dataset, the other datasets are also affected by this command.|
|Tip|A tip is a type of admonition in documentation that provides a helpful suggestion or best practice related to the content of the document. It is typically used to guide the reader towards a more efficient or effective way of using a product or service, or to provide additional insights or recommendations.|We have the suggestion option as well; click on the +icon and select the suggestion mapping.|
|Success|Success admonitions are a type of documentation element used to highlight successful outcomes or positive results associated with a particular task, process, or feature|Graph is created successfully.|
|Bug|A bug admonition include a description of the bug or issue, as well as steps that the user can take to avoid or work around the problem. It may also include information about when the bug will be fixed or patched, if applicable.|Users may experience issues with the file saving feature when running this software on Windows 10. To avoid data loss or corruption, be sure to save your work frequently and consider using an external backup device. Our development team is working to resolve this issue in the next software update.|
|Example|The example admonition is typically used in instructional or educational documents to clarify complex concepts or demonstrate how to perform a specific task.|To create a new email account, click on the "Sign Up" button on the homepage and enter your name, email address, and desired password. Be sure to choose a strong password with a mix of uppercase and lowercase letters, numbers, and special characters. Once you have entered your information, click "Create Account" to complete the process.|
|Task|The Task admonition type is used to describe a series of steps or tasks required to complete a process or action. Clear and concise descriptions of each step, along with any relevant details or instructions, should be included. It's helpful to use images or diagrams to illustrate the process. Overall, The Task admonition is useful for providing detailed instructions to readers.|Loading Data  into a CMEM involves 3 steps: </br> 1. Connect to the database. </br> 2. Choose the data file and appropriate file type. </br> 3. Run workflow to import.|

</details>

## Images (esp. Screenshots)

<details>
  <summary>Extend section</summary>

-   do not use a cluttered desktop
-   do not show other esp. personal project artifacts then relevant for the tutorial / feature to show
-   select cropping area carefully (omit backgrounds, lines on the edges, etc.)
-   use the same or a similar area for similar screens
-   all relevant elements should be clearly visible and not be truncated
-   irrelevant elements / details should be omitted completely and not be half visible
-   crop scrollbars (they can make edges look unclean, especially if a scrollbar is directly on an edge)
-   keep an equal distance of all visible elements to the edges of the screenshot

</details>
