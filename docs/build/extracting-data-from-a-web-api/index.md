---
icon: material/api
tags:
  - "3 Expert Tutorial"
---
# Extracting data from a Web API

## Introduction

This tutorial shows how you can build a Knowledge Graph based on input data from a Web API.
The tutorial is based on the [GitHub API (v3)](https://developer.github.com/v3/), which we will use to fetch repository data of a certain organization and create a Knowledge Graph from the response.

!!! info

    The complete tutorial is available as a [project file](tutorial-webapi.project.zip). You can import this project:

    - by using the [web interface](../introduction-to-the-user-interface/index.md) (Create → Project → Import project file) or
    - by using the [command line interface](../../automate/cmemc-command-line-interface/index.md)

    ``` shell-session
    $ cmemc -c my-cmem project import tutorial-webapi.project.zip web-api
    ```

In order to get familiar with the API, just fetch an example response with this command:

``` shell-session
$ curl https://api.github.com/orgs/vocol/repos
```

The HTTP Get request retrieves all repositories of a GitHub organization named vocol.

The JSON response includes the data for all repositories (**mobivoc**, **vocol**, ...). You can also download the response file here: [repos.json](repos.json).

``` json
[
    {
        ...
        "id": 22646219,
        "name": "mobivoc",
        ...
    },
    {
        ...
        "id": 22646629,
        "name": "vocol",
        ...
    },
    {
        ...
        "id": 30964669,
        "name": "scor",
        ...
    },
    ...
]
```

## 1 Register a Web API

1. Press the **Create** button (top right) in the data integration workspace and select the type **REST request**.

    ![Create new REST request task](create-new-task-rest.png)

2. Define a **Label, Description** and the **URL** of the Web API. Example input: `https://api.github.com/orgs/vocol/repos`.

    ![REST request task configuration](create-new-task-rest-config.png)

## 2 Create a JSON parser

As we are only interested in the _HTTP Message Body_ which holds the JSON repository data, we first have to parse the _body_ from the entire HTTP response.

1. Press the **Create** button (top right) in the data integration workspace and select the type **Parse JSON.**

    ![Parse JSON task](create-new-task-parse-json.png)

2. Define a **Label**, a **Description**, and the **Input path.** Every other field can keep the default settings. The default input path is always: `<http://silkframework.org/vocab/taskSpec/RestTaskResult/responseBody>`

    ![Parse JSON task configuration](extract-from-api-parse-json-config.png)

## 3 Create a JSON Dataset

To create a JSON-to-RDF-mapping within Corporate Memory, we have to first register an example response from the API (repos.json). Based on the schema of the response, we can then define step-by-step the mappings, which are used to build the Knowledge Graph.

1. Press the **Create** button (top right) in the data integration workspace and select the type **JSON**.

    ![Create JSON dataset](create-new-json-dataset.png)

2. Upload the JSON file [repos.json](repos.json) (API response) as a Dataset into Corporate Memory.

    ![Create JSON dataset, upload data](create-new-json-dataset-upload.png)

## 4 Create a Knowledge Graph

The Knowledge Graph will be used to integrate all data coming from one or more APIs. The Knowledge Graph receives RDF triples from the defined Transformations for each API.

1. Press the Create button (top right) in the data integration workspace and select the type **Knowledge Graph**.

    ![Create Knowledge Graph dataset](create-new-kg-dataset.png)

2. Provide the Knowledge Graph with a **Label** and **Description**, as well as the following (example) **Graph** URI: `http://ld.company.org/repository-data/`

    ![Create Knowledge Graph configuration](create-new-kg-dataset-config.png)

## 5 Create a Transformation

In order to transform the input data from the API, which is structured in our example in JSON, we have to define a mapping to create RDF triples which are then written into the Knowledge Graph.

1. Press the Create button (top right) in the data integration workspace and select the type **Transform**.

    ![Create a transformation](extract-from-api-create-transformation.png)

2. Provide the Transformation with a **Label** and **Description**, configure the **Input Dataset** (Repos.json) as well as the **Output Dataset** (Repository Knowledge Graph).

    ![Transformation task configuration](extract-from-api-create-transformation-config.png)

In order to transform the input data from the API, which is structured in our example in JSON, we have to define a mapping to create RDF triples which are then written into the Knowledge Graph.

1. Press the **Mapping Editor** button in the previously defined Transformation.

    ![Open the transformation](extract-from-api-tf-open.png)

2. In the following screenshots, we provide an example mapping for the data received by the GitHub API. For more complex mappings, we recommend the Tutorial [Lift data from JSON and XML sources](../lift-data-from-json-and-xml-sources/index.md).

    ![Mapping rule example](extract-from-api-tf-rule-1.png)

    ![Mapping rule example](extract-from-api-tf-rule-2.png)

## 6 Create a Workflow

To build a workflow which combines all the elements we previously built, we define now a workflow for (1) requesting the data from the GitHub API, (2) parsing the HTTP response we receive, (3) transforming the JSON data into RDF triples and finally (5) to write the RDF triples into the Knowledge Graph.

1. Press the **Create** button (top right) in the data integration workspace and select the type **Workflow**.

    ![Create a workflow](extract-from-api-create-wf.png)

2. Provide the Transformation with a **Label** and a **Description**.

    ![Workflow configuration](extract-from-api-wf-config.png)

3. Press the **Workflow Editor** button in the menu of the created workflow.

    ![Workflow details view](extract-from-api-wf-created.png)

4. Drag and drop the different items into the Workflow Editor and combine them with one another (see example screenshot). **Save** the workflow, and press the **run symbol** to execute the workflow.

    ![Workflow modeling view](extract-from-api-wf-modelling.png)

5. Validate the result by clicking on the **Workflow** **Report** tab and see the result of your execution. In this example, 15x repositories were found from the GitHub API request.

    ![Workflow execution report](extract-from-api-wf-report.png)

