---
title: "Introduction: How to use this documentation"
---

# How to use this documentation

This documentation describes eccenca Corporate Memory from first contact to operation in production.
It is organized by what is being done with the product, not by the parts of the user interface.

## Two ways in

- **New to eccenca Corporate Memory**: follow the introduction on [Home](../../index.md).
  It leads from what the product is for to getting access and a first tutorial.
- **Familiar with eccenca Corporate Memory**: go straight to a section in the main menu, such as **Build** or **Explore**.
  Each section has an overview that lists everything it contains.

## How the documentation is structured

The main sections follow the path that data takes through eccenca Corporate Memory.
Each section overview names its intended audience next to :octicons-people-24:.

| Section | What it covers | Intended audience |
| --- | --- | --- |
| :material-star: [Build](../../build/index.md) | Turning source data from files, databases, APIs and streams into a Knowledge Graph. | Linked Data Experts |
| :material-star: [Explore](../../explore-and-author/index.md) | Browsing, querying, editing and validating the Knowledge Graph. | Linked Data Experts and Domain Experts |
| :material-star: [Consume](../../consume/index.md) | Providing data from the Knowledge Graph to other applications and tools. | Linked Data Experts |
| :material-star: [Distribution](../../distribution/index.md) | Discovering, installing and managing ready-made Marketplace Packages. | All eccenca Corporate Memory users |
| :material-star-outline: [Deploy and Configure](../../deploy-and-configure/index.md) | Installing, configuring and upgrading eccenca Corporate Memory. | Deployment Engineers and System Administrators |
| :material-star-outline: [Automate](../../automate/index.md) | Scheduling workflows, continuous integration and delivery, and the `cmemc` command line client. | Linked Data Experts and Deployment Engineers |
| :material-star-outline: [Develop](../../develop/index.md) | Extending eccenca Corporate Memory with plugins and packages, and accessing it through its APIs. | Software Developers and Linked Data Experts |
| :material-calendar: [Release Notes](../../release-notes/2026/corporate-memory-26-2/index.md) | Changes and enhancements in each version. | All eccenca Corporate Memory users |

<!-- TODO confirm the meaning of the two star icons with the team -->
A filled star :material-star: marks the sections about working with data and the Knowledge Graph.
An outlined star :material-star-outline: marks the sections about operating, automating and extending eccenca Corporate Memory.

The overviews of Build, Explore, Consume and Distribution show a diagram of the product architecture.
The highlighted area marks the part of the product the section describes.

**Home** introduces eccenca Corporate Memory and the ideas behind it.
**Learn** collects the tutorials and the training material of all sections in one place.

## Four types of content

Each topic in this documentation serves one of four purposes.
In the menu of **Build**, for example, the topics are grouped by these types.

| Type | Answers the question | Example in Build |
| --- | --- | --- |
| **Foundations** | How does it work, and why? | [Cool IRIs](../../build/cool-iris/index.md) |
| **Tutorials** | How is a complete result reached, step by step? | [Lift data from tabular data](../../build/lift-data-from-tabular-data-such-as-csv-xslx-or-database-tables/index.md) |
| **Guides** | How is a specific feature used in an existing project? | [Workflows](../../build/workflows/index.md) |
| **Reference** | What exactly does an operator, a parameter or an option do? | [Task and Operator Reference](../../build/reference/index.md) |

Choose the type by the current goal:

- To understand a concept before working with it, read a **Foundations** topic.
- To learn a feature by example, follow a **Tutorial** from start to finish.
  A tutorial brings its own sample data and works on an empty project.
- To get a task done in an existing project, use a **Guide**.
  A guide assumes that the concepts are known.
- To look up a single detail, use the **Reference**.
  It is not meant to be read from top to bottom.

### Tutorials in a section and in Learn

The tutorials in a section focus on the features of that section.
[Learn › Tutorials](../../tutorials/index.md) lists the tutorials of all sections, grouped by level: beginner, advanced and expert.

[Learn › Training](../../training/index.md) contains the material of the eccenca Corporate Memory training.
Its modules cover the theory behind eccenca Corporate Memory, such as RDF, SPARQL and ontology modeling, and link to the tutorials for the hands-on sessions.

## Where to start by role

- **Linked Data Experts and data engineers** start in [Build](../../build/index.md), with the **Foundations** and a tutorial.
- **Domain Experts and business users** start in [Explore](../../explore-and-author/index.md).
- **Software Developers** start in [Develop](../../develop/index.md).
- **Deployment Engineers and System Administrators** start in [Deploy and Configure](../../deploy-and-configure/index.md).

## How to find a topic

- **Search**: the search field in the header searches all sections of the selected version.
  A search result opens with all occurrences of the search term highlighted.
- **Tags**: tags such as `BeginnersTutorial` group related content across sections.
  The tags of a topic appear next to the breadcrumb at the top.
  Select a tag to see all topics that carry it, or open the [tag index](../../tags.md).
- **Breadcrumb**: the path above each heading shows where a topic sits in the structure.
  Select an entry to go up one or more levels.

## Versions

The documentation is published separately for each release of eccenca Corporate Memory.
The version `latest` is the documentation of the most recent release.

<!-- [needs-instance] confirm position and label of the version selector on documentation.eccenca.com -->
To read the documentation that matches a deployment, select its version from the version selector in the header.
The version of a deployment is shown in the user interface of eccenca Corporate Memory.
<!-- [needs-instance] name the exact place in the product where the version is shown -->

Features, labels and steps can differ between versions.
When the product does not match a description, check the selected version first.

## How to read the content

### Text formatting

- **Bold text** marks elements of the user interface, spelled exactly as in the product, for example **Create**.
- `Monospace text` marks values to enter or select, file names and technical identifiers, for example `CMEM_BASE_URI`.

### Boxes

Colored boxes set information apart from the main text.

!!! info

    Background information or context.

!!! note

    A detail worth knowing that is not essential for the task.

!!! tip

    A shortcut or a better way to reach the same result.

!!! warning

    An action that can cause data loss or an unexpected result.

!!! example

    A sample, often collapsed, such as a query or a configuration file.

## Help inside eccenca Corporate Memory

<!-- [needs-instance] verify where the context help sits in the current release and how it links to this documentation -->
eccenca Corporate Memory provides context help for the main functions of its workspaces.
Select :material-help-circle-outline: to open it.

## When the documentation is not enough

### Get help

<!-- TODO support and contact channels to be clarified -->

### Report missing or unclear content

Each topic ends with a **Comments** area.
Use it to report a mistake, an unclear explanation or a missing topic.
Commenting requires a GitHub account.
The comments are public and are stored as discussions in the [documentation repository](https://github.com/eccenca/documentation.eccenca.com/discussions).
