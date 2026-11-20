---
icon: eccenca/application-dataintegration
---
# Introduction to the user interface

This page provides a short introduction to the BUILD / Data Integration workspace incl. projects and different tasks.

## Workbench

The workbench is the main entry point to the BUILD interface and provides a list view of your work, structured in _projects_.

![The Build workbench listing projects, datasets and workflows with the item type facets on the left](build-ui-workbench.png){ class="bordered" }

On the left-hand side, a facet list provides an overview of different item types:

- **Projects** are the main structure and consist of datasets, workflows and different tasks (transformations, linking and other tasks)
- **Datasets** are registered data sources from files or endpoints, or internally managed.
- **Transform** tasks take an input dataset and execute a (hierarchical) set of mapping and transformation rules, and generate data for an output dataset.
- **Linking** tasks compare entities from two datasets according to (hierarchical) sets of comparators and generate links between these datasets in an output (link) dataset.
- **Workflows** can combine all items in a project in order to create a structured work plan which can be executed on demand, controlled remotely (e.g. via [cmemc](../../automate/cmemc-command-line-interface/index.md)) or executed from a [scheduler](../../automate/scheduling-workflows/index.md).

The interface can be used to browse from a global level to a project level as well as to search for items globally and project wide.

Click **Create new** in the header to create any kind of Build item:

![](build-ui-datasets.png)

## Projects

The project is the main concept to structure the work in Build.
In the workbench, projects are created, imported, exported and deleted.

Each project is self-contained and holds all relevant parts, such as the following:

- the raw **data resources** (local or remote data files) that form the starting point for your work
- the **datasets** that provide uniform access to different kinds of data resources
- **transformation tasks** to transform datasets (e.g., from one format or schema to another)
- **linking tasks** to integrate different datasets
- **workflows** to orchestrate the different tasks
- definitions of **URI prefixes** used in the project

Resources, datasets, tasks and other parts of a project can be added and configured from within the workspace. By clicking the `Show Details` button on any item in a project, you can ‘look inside’ and define the actual transformation or linking rules, or assemble the actual workflow.

### Project view

Selecting a project in the workbench opens the project view.

![The project view of the Product Catalog project with its contents and the cards on the right](build-ui-project.png){ class="bordered" }

The project view shows the following areas:

- **Summary:** the label and description of the project
- **Contents:** the items of the project, with a search field and facets
- **Configuration:** the prefixes of the project
- **Project variables:** the [variables](../variables/index.md) of the project
- **Activities:** the activities of the project and their state
- **Changes:** the number of recorded changes and of changes made by an agent that await review, see [Change journal](../change-journal/index.md)
- **Files:** the files uploaded to the project

### Import a project

A project exported as a project file can be imported into the workbench.
To import a project, follow these steps:

1. Click **Create new** in the header.
2. Select **Project** and click **Add**.
3. Click **Import project file**.
4. Upload the project file.
    The **Project import** dialog shows the label and the description of the imported project.
5. Select an **Import destination**:
    - **Use original project ID** imports the project under the identifier stored in the project file.
    - **Generate a new project ID** imports the project under a new identifier.
    - **Use a custom project ID** imports the project under the identifier entered in the **Project identifier** field.

    ![The Project import dialog with the import destinations and the warning about an existing project](build-ui-project-import.png){ class="bordered" width="70%" }

6. Click **Import project**.

If a project with the selected identifier already exists, the dialog shows a warning.
Select **Replace existing project** and click **Replace existing project** to overwrite the existing project, or select another import destination.
Click **Open existing project page** to inspect the existing project first.

## Datasets

Selecting a dataset in a project or from the search results opens the dataset details view.

![](build-ui-dataset-preview.png)

Here you have the following options:

- Change the meta data of the dataset (**Summary** - label and description, top left main area),
- Change the **Configuration** parameters of the dataset (lower right side area),
- Browse to other **Related Items**, such as transforms, linking or workflow tasks which use this dataset (top right side area),
- Get a **Data Preview** as well as generate and view **profiling information** (lower left main area).

A dataset represents an abstraction over raw data. In order to work with data, you have to make it available in the form of a dataset. A dataset provides a source or destination for the different kinds of tasks. I.e., it may be used to read entities for transformation or linking, and it can be used to write transformed entities and generated links.

There is a range of different dataset types for different kinds of source data. Important dataset types include:

- **Knowledge Graph** - Read RDF from or write RDF to a Knowledge Graph embedded in eccenca Corporate Memory.
- **CSV** - Read from or write to an CSV file.
- **XML** - Read from or write to an XML file.
- **JSON** - Read from or write to a JSON file.
- **JDBC endpoint** - Connect to an existing JDBC endpoint.
- **Variable dataset** - Dataset that acts as a placeholder in workflows and is replaced at request time.
- **Excel** - Read from or write to an Excel workbook in Open XML format (XLSX).
- **Multi CSV ZIP** - Reads from or writes to multiple CSV files from/to a single ZIP file.

Other options include:

- **Internal dataset** - Dataset for storing entities between workflow steps.
- **RDF** - Dataset which retrieves and writes all entities from/to an RDF file. The dataset is loaded in-memory and thus the size is restricted by the available memory. Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead.
- **SPARQL endpoint** - Connect to an existing SPARQL endpoint.
- **In-memory dataset** - A dataset that holds all data in-memory.
- **Avro** - Read from or write to an Apache Avro file.
- **ORC** - Read from or write to an Apache ORC file.
- **Parquet** - Read from or write to an Apache Parquet file.
- **Hive database** - Read from or write to an embedded Apache Hive endpoint.
- **SQL endpoint** - Provides a JDBC endpoint that exposes workflow or transformation results as tables, which can be queried using SQL.
- **Neo4j** - Connect to an existing Neo4j property graph database system.

## Transform tasks

The purpose of transform tasks is to transform datasets (e.g., from one format or schema to another). More specifically, Transform Tasks create Knowledge Graphs out of raw data sources.

Selecting a transform task in a project or from the search results opens the transform task details view.

![](build-ui-transform.png)<!-- TODO: update img -->

Here you have the following options:

- Change the metadata of the transformation task (**Summary** - label and description, top left main area)
- Change the **Configuration** parameters of the transformation task (lower right side area),
- Browse to other **Related Items**, such as used datasets or workflows using this task (top right side area),
- Open the **Mapping Editor** in order to change the transformation rules,
- **Evaluate the Transformation** to check for issues with the rules,
- **Execute the Transformation rules** in order to create new data,
- **Clone** the task, creating a new transform task with the same rules.

## Linking tasks

The purpose of linking tasks is to integrate two datasets (source and target) by generating a linkset that contains links from the source to the target dataset.

Selecting a linking task in a project or from the search results opens the transform task details view.

![](build-ui-linking.png) <!-- TODO: update img -->

Here you have the following options:

- Change the metadata of the linking task (**Summary** - label and description, top left main area),
- Change the **Configuration** parameters of the linking task (lower right side area),
- Browse to other **Related Items**, such as used datasets or workflows using this task (top right side area),
- Open the **Linking Editor** in order to change the comparison rules,
- **Evaluate the Linking** to check for issues with the rules,
- **Execute the Linking task** in order to create a linkset,
- **Clone** the task, creating a new linking task with the same comparisons.

As in the case of transform tasks, the output linkset of a linking task can either be written directly to an output dataset, or provide the input to another task if integrated into a workflow.

## Workflows

For projects that go beyond one or two simple transform or linking tasks, you can create complex workflows. In a workflow, you can orchestrate datasets, transform tasks and linking tasks via connections between their inputs and outputs, and in this way perform complex tasks.

Selecting a workflow in a project or from the search results opens the workflow details view.

![](build-ui-workflow.png)

Here you have the following options:

- Change the metadata of the linking task (**Summary** - label and description, top left main area)
- Browse to **Related Items**, such as used datasets and tasks (top right side area),
- Open the **Worflow Editor** in order to change the workflow (here you can as well start the workflow),
- **Clone** the workflow creating a new workflow with the same task.
