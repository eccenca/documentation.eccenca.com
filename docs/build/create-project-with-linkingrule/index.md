---
icon: material/link-variant
subtitle: based on the built in movies example
#hide:
#  - navigation
tags:
  - "1 Beginners Tutorial"
  - KnowledgeGraph
---

# Linking tutorial

## Introduction

The eccenca DataIntegration platform is designed to support the process to "BUILD" a knowledge graph by integrating structured and unstructured data from multiple sources, including on-premises systems and cloud-based services.
The BUILD functionalities include data mapping, transformation, and cleansing tools, as well as DataIntegration and governance support.

This beginner-level tutorial explains how to build a DataIntegration project using linking rules.

The documentation consists of the following steps described in detail below:

1. Create a new project
2. Upload files
3. Create datasets
4. Create a linking task
5. Assemble a linking rule

This tutorial shows how to connect two movie-related data sources and introduces some of Data-Integration’s fundamental functions.
Sources of information are LinkedMDB, the linked data version of the IMDb movie database, and DBpedia, the linked data version of Wikipedia.
Both files contain a list of movies with their names, titles, release dates, and an internal ID for each movie.
The task is to link the two datasets to find out which movie in DBpedia corresponds to which movie in LinkedMDB.

## Sample material

The following material is used in this tutorial, you should download the files and have them at hand throughout the tutorial:

-   [dbpedia.csv](dbpedia.csv)

    !!! info

        ![](preview-dbpedia.png){ width="75%"}

-   [linkedmdb.csv](linkedmdb.csv)

    !!! info

        ![](preview-linkedmdb.png){ width="75%"}

## 1. Create a new project

-   Once logged in to Corporate memory on the right side click on **create.**

    ![image](22.2-create-project.png){ width="75%"}

    The screen gives an overview of the different projects created in your installation of DataIntegration.
    It shows the item type on the left side like a project, workflow, dataset, transform, linking, and task.

-   Click on the **project** on the left side in the item type and double-click on the **project** in the centre.

    ![image](22.2-click-on-project.png){ width="75%"}

-   Type the project name as **Movie links** in the title field and click on **create.**

    ![image](22.2-type-movielink.png){ width="75%"}

!!! note "Step Result"

    The project was created with the name "Movie links," which is displayed in the page top left corner.

    ![image](22.2-project-created.png){ width="75%"}

## 2. Upload the files

-   Click on **add file** on the right side of the page.

    ![image](22.2-click-on-add-files.png){ width="75%"}

-   Click on **drop files here** select the file and click on **open**.

    ![image](22.2-upload-files.png){ width="75%"}

-   Once the file is successfully uploaded click on **close.**

    ![image](22.2-files-uploaded.png){ width="75%"}

-   Repeat the same step to add the file select the next second file and upload it.

!!! note "Step Result"

    The files are uploaded to the project and reflect on the right side as shown below.

    ![image](22.2-files-added.png){ width="75%"}

## 3. Create datasets

-   Click on **create.**

    ![image](22.2-click-on-create.png){ width="75%"}

-   Click on the **dataset** on the left side in the item type and double-click on the **CSV file** in the centre.

    ![image](22.2-click-on-dataset.png){ width="75%"}

-   Type the file name as **dbpedia** in the label field.

    ![image](22.2-type-dbpedia.png){ width="75%"}

-   Tick the option **select file from project** and select the file from the drop-down list of files available in the project.

    ![image](22.2-select-dbpedia-file.png){ width="75%"}

-   Click on **create**.

    ![image](22.2-click-on-create1.png){ width="75%"}

-   Repeat the same step and add another file linkedmdb in the dataset.

-   Create the empty dataset file for extracting both files' links as an output result. Click on the **dataset** on the left side of the item list and double-click on the **CSV** file.

    ![image](22.2-click-on-dataset.png){ width="75%"}

-   Type the label name **links.csv** in the label field.

    ![image](22.2-type-links.png){ width="75%"}

-   Tick the option **create empty file** and select the file name from the drop-down list as **link.csv** then click on **create**.

    ![image](22.2-click-on-emptyfiles.png){ width="75%"}

!!! note "Step result"

    Dataset for both the files dbpedia and linkedmdb has been created, and `link.csv` is created for the output result displayed in the page's center.

    ![image](22.2-dataset-created.png){ width="75%"}

## 4. Create a linking task

-   Click on **create**.

    ![image](22.2-dataset-created.png){ width="75%"}

-   Click on **linking** on the left side in the item type and double-click on **linking** in the center.

    ![image](22.2-click-on-linking.png){ width="75%"}

-   Type the name as **linking** in the label field and select the **source input** data set as a **dbpedia** file.

    ![image](22.2-type-linking.png){ width="75%"}

-   Select the **type** field (it gives the default name) select the same and click on **create**.

    ![image](22.2-select-type-field.png){ width="75%"}

-   In the continuation to the same page go down, select the **target input** dataset as a **linkedmdb** file.

    ![image](22.2-target-input.png){ width="75%"}

-   Select the **type** field (it gives the default name) select the same and click on **create**.

    ![image](22.2-selecttype-field.png){ width="75%"}

-   Select the **output dataset** as **link.csv** file.

    ![image](22.2-select-output.png){ width="75%"}

-   Click on **create**.

    ![image](22.2-linking-click-on-create.png){ width="75%"}

!!! note "Step Result"

    Linking task is created for the project.
    It shows the source path, target path, and operators (transform, comparison, and aggregation) options on the left side of the page.

    ![image](22.2-linking-created.png){ width="75%"}

    It shows the linking editor, linking execution, linking evaluation, and reference link in the centre of the page to create and evaluate the linking rules.

    ![image](22.2-linking-created.png){ width="75%"}

    On the right side of the page, it shows datasets, configuration linking, and configuration linking rules.

    ![image](22.2-linking-created.png){ width="75%"}

## 5. Assemble a linking rule

<!--
the initial rule shown in the screenshots is incomplete.
a rule is only complete if if can be saved and validated.

the initial rule should have the source and target paths for title and a string equality comparator.
-->

!!! success "Task"

    Assemble a linking rule with the linking editor.
    To create a rule to say that movies from dbpedia and linkedmdb should be considered the same if their titles are identical.

### Add source and target paths for the `title`

-   Click on the **source path** and drag the title on the canvas.

    ![image](22.2-click-on-sourcepath.png){ width="75%"}

-   Click on the **target path** and drag the title on the canvas.

    ![image](22.2-click-on-targetpath.png){ width="75%"}

!!! note "Step Result"

    The titles from the source path and target are dragged on the canvas as shown below.

    ![image](22.2-click-on-targetpath.png){ width="75%"}

### Normalize the `title` for a better comparison result

!!! success "Task"

    Let's make this a little better and compare only the lowercase versions of the titles to get around issues with differences in the lower and upper case between the two datasets.

-   Click on **transformation**, type the operator **lowercase**  in the search field and drag the same on the canvas twice.

    ![image](22.2-lowercase.png){ width="75%"}

-   Drag the little dot on the right side of the source path box onto the left dot of the transformation box(lower case) to connect the two with a line (you always must drag from the right side of one element to the left side of another to connect the two).

    ![image](22.2-source-lowercase.png){ width="75%"}

-   Drag the little dot on the right side of the target path box onto the left dot of the transformation box(lower case) to connect the two with a line (you always must drag from the right side of one element to the left side of another to connect the two).

    ![image](22.2-target-lowercase.png){ width="75%"}

!!! note "Step Result"

    The lines connected between the target path title and lowercase as shown below.

    ![image](22.2-target-lowercase.png){ width="75%"}

### Compare the `title` of the movies

!!! success "Task"

    Compare the movie title names of both the data `dbpedia.csv` and `linkedmdb.csv`.

-   Click on **comparison** and type the **equality** in the search field and drag the `string equality` operation onto the canvas.

    ![image](22.2-comparison.png){ width="75%"}

-   Drag the little dot on the right side of both lowercase boxes onto the left dot of the string equality box to connect the two with a line (you always must drag from the right side of one element to the left side of another to connect the two).

    ![image](22.2-lower-string.png){ width="75%"}

!!! note "Step Result"

    The lines are connected between both lowercase operators and string equality operators.

    ![image](22.2-lower-string.png){ width="75%"}

-   Click on **save** on the right side of the page.

    ![image](22.2-comparison-save.png){ width="75%"}

### Linking evaluation

!!! success "Task"

    Now it is time to see your linking rule in action by running it on your datasets.
    So far, we have created a linking rule in which we changed the title names of both files in lowercase and compared the same.
    Now it’s time to generate the links by evaluating them.

-   Click on the **linking evaluation**.

    ![image](22.2-click-on-linking-evaluation.png){ width="75%"}

-   Click on the **play button** to start the evaluation and generate the links.

    ![image](22.2-start-evalute.png){ width="75%"}

!!! note "Step Result"

    The links are generated as shown below. (It allows us to review the links and since DataIntegration does not know which column to use as a unique identifier, it just uses the row number in the `.csv` file to identify each movie.

    ![image](22.2-evalute-result.png){ width="75%"}

-   Click on the down arrow button to **expand** all.

    ![image](22.2-expand-all.png){ width="75%"}

!!! note "Step Result"

    This allows you to see how the linking rule was performed for each link and even the movie name compared in both files.

    ![image](22.2-expand-result.png){ width="75%"}

### Use a filter

!!! success "Task"

    It has a filter feature that helps to find links by movie names.
    An example is shown below.

    Let’s consider the movie name as shaft type **shaft** in the filter it shows the links with the shaft movie names links of both files.

    ![image](22.2-type-shaft.png){ width="75%"}

    Cross-checking in the `dbpedia.csv` and `linkedmdb.csv` data sheet.

    ![image](22.2-shaft-result.png){ width="75%"}

    The movie name is twice in both sheets, but the release dates differ.
    The shaft movie’s original release was in 1971 and the remake was in 2000.
    We have the tick option for the correct rule.

-   Click on the linking execution then click on the **play button** to execute the links (It copies the links to our data file `links.csv` (which is our output file).

    ![image](22.2-start-activity.png){ width="75%"}

!!! note "Step Result"

    The links are executed and copied to the output data file `links.csv` and which shows the count of links on the page.

    ![image](22.2-linking-result.png){ width="75%"}
