---
icon: material/family-tree
tags:
  - AdvancedTutorial
  - EvaluateTemplate
---
# Evaluate Jinja Template and Send an Email Message

## Introduction

In this tutorial we dynamically produce text with a **Jinja** template and send it in an email after the execution of a workflow. The email message contains information retrieved from a graph. The graph dataset is attached to the email as an N-triples file. In this tutorial, we do not transform data, but send an existing dataset. For tutorials on how to transform data, please refer to one of our other  [tutorials](https://documentation.eccenca.com/22.2/tutorials/) that demonstrate lifting data from a variety of data sources.

!!! Abstract

    The complete tutorial is available as a [project file](tutorial-template.project.zip). You can import the projects:

    - by using the [web interface](/build/introduction-to-the-user-interface) (Create → Project → Import project file) or
    - by using the [command line interface](/automate/cmemc-command-line-interface)

        ```shell
        cmemc -c my-cmem project import tutorial-template.project.zip tutorial-evaluate-template
        ```
    
The documentation consists of the following steps, which are described in detail below.

The following material is used in this tutorial:

- RDF graph containing company information regarding employees, products and services : [company.ttl](company.ttl)


    ```Turtle
    <http://ld.company.org/prod-instances/hw-A181-1118563> a prod:Hardware ;
    rdfs:label "A181-1118563 - Compensator Switch" ;
    prod:compatibleProduct <http://ld.company.org/prod-instances/hw-M558-2275045> ;
    prod:depth_mm 14 ;
    prod:hasCategory <http://ld.company.org/prod-instances/prod-cat-Switch> ;
    prod:hasProductManager <http://ld.company.org/prod-instances/empl-Adolfina.Hoch%40company.org> ;
    prod:height_mm 32 ;
    prod:id "A181-1118563" ;
    prod:name "Compensator Switch" ;
    prod:price <http://ld.company.org/prod-instances/price-hw-A181-1118563-EUR> ;
    prod:weight_g 5 ;
    prod:width_mm 22 .
    ...
    ```


## 1 Upload the Company Graph

The vocabulary contains the classes and properties needed to map the source data into entities in the Knowledge Graph.

1. In Corporate Memory, click **Knowledge Graphs** in the navigation under **Explore** on the left side of the page.

    ![Menu entry EXPLORE > Knowledge Graphs](menu-explore-knowledge-graphs.png){width="40%"}

2. Click on the **+** symbol next to the search field on the top left side of the page.

    ![Add graph](add-graph.png){width="40%"}

3. In the dialog, click **New graph from File**.

    ![Dialog add graph](dialog-new-graph-from-file.png)

4. Drop the file [company.ttl](company.ttl) onto the dialog, or click on **browse** to navigate to the file.

    ![Dialog uoload graph](dialog-upload-graph.png){width="75%"}

5. In the **Target graph URI** field, enter **http://ld.company.org/prod-inst-jinja/** and click **Create option 'http://ld.company.org/prod-inst-jinja/'** 
   
    ![Dialog to register a new vocabulary.](dialog-create-graph.png){width="75%"}
   
6. Tick the **Add new graph** checkbox and click **Upload**.

    ![Dialog to register a new vocabulary.](dialog-create-graph-2.png){width="75%"}



## 2 Create a Project


1. Click **Projects** in the navigation under **Build** on the left side of the page.
   
    ![Menu entry EXPLORE > Projects](menu-explore-projects.png){width="40%"}

2. Click **Create** at the top of the page.  

3. In the **Create new item** window, select **Project** and click **Add**. The Create new item of type Project window appears.

    ![Dialog to create new Knowledge Graph dataset](create-project.png)

4. Fill in the required details (Title) and click **Create**.

    ![Dialog to create new Knowledge Graph dataset](create-project-2.png)


## 3 Create a Knowledge Graph Dataset

The **Knowledge graph** dataset holds the **Company graph** we uploaded earlier.

1. Click **Create** at the top of the page.

    ![Create](create.png){width="30%"}

2. In the **Create new item** window, select **Knowledge Graph** and click **Add**. The **Create new item of type Knowledge Graph** appears.

    ![Create new Knowledge graph dataset](create-knowledge-graph-dataset.png)

3. Fill in the required details, such as **Label** and, for **Graph**, the IRI of the company graph **http://ld.company.org/prod-inst-jinja/**. When finished, click **Create**.

    ![Dialog to create new Knowledge Graph dataset](create-knowledge-graph-dataset-2.png)


## 4 Create a SPARQL Select Query Task Item

The SPARQL select query is used to retrieve the data from the company graph that we want to include in our email.

1. Click **Create** at the top of the page. 

2. On the **Create new item** window, select **SPARQL Select query** and click **Add**. The **Create new item of type SPARQL Select query** window appears.

    ![Create new Select query](add-sparql-select.png)

3. Fill in the required details. In the **Select query** field enter the following query which counts the instances of employees, managers, departments, products, and products that have other compatible products in the database. When finished, click **Create**.

    ```sparql
    PREFIX pv: <http://ld.company.org/prod-vocab/>

    SELECT ?employees
        ?managers
        ?departments
        ?products
        ?product_compatibility
        ?currentDateTime
        ?validation_result
    FROM <http://ld.company.org/prod-inst-jinja/>
    WHERE {
        { SELECT ( COUNT( DISTINCT ?employee ) AS ?employees ) {
            ?employee a pv:Employee } 
        }
        { SELECT ( COUNT( DISTINCT ?manager ) AS ?managers ) {
            ?manager a pv:Manager } 
        }
        { SELECT ( COUNT( DISTINCT ?department ) AS ?departments ) {
            ?department a pv:Department } 
        }
        { SELECT ( COUNT( DISTINCT ?product_) AS ?products ) {
            ?product_ a pv:Hardware } 
        }
        { SELECT ( COUNT( DISTINCT ?comp_product_ ) AS ?product_compatibility ) {
            ?comp_product_  pv:compatibleProduct ?prod } 
        }
        BIND( now() AS ?currentDateTime )
    } 
    ```

    ![Dialog to create new Select query](add-sparql-select-2.png)


## 5 Create an Evaluate Template Task Item

The Jinja template in this item acts as the template for our email message.

1. Click **Create** at the top of the page. 

2. In the **Create new item** window, select **Evaluate template** and click **Add**. The **Create new item of type Evaluate template** appears.

    ![Create new Evaluate template item](create-evaluate-template.png)

3. Fill in the required details, such as **Label** and **Template**. In the **Template** field enter the following Jinja template. Note, that the variable names correspond to those in the SPARQL query we previously created. Select **jinja** in the **Language** field. When finished, click **Create**.

    ```
    Hi,

    attached is the workflow result as an N-Triples file. 
    Timestamp: {{ currentDateTime }}

    Product compatibility:
    {{ product_compatibility }} out of {{ products }} products have compatible alternatives.

    Organization information:
    There are {{ managers }} managers and {{ employees }} employees in {{ departments }} departments.
    ```

    ![Dialog to create new Evaluate template item](create-evaluate-template-2.png)


## 6 Create a Text Dataset

The text dataset holds a text file that will contain the evaluated Jinja template that will be our email message.\*

1. Click **Create** at the top of the page.

2. In the **Create new item** window, select **Text** and click **Add**. The **Create new item of type Text** appears.

    ![Create new text dataset](create-text-dataset.png)

3. Fill in the required details, such as **Label** and **FILE**. Under **FILE**, select **Create empty file** and enter the filename in the **New file name** field. When finished, click **Create**.

    ![Dialog to create new Text dataset](create-text-dataset-2.png)


## 7 Create a Transform

The Transform retrieves the text from the Text dataset to be sent as our email message.

1. Click **Create** at the top of the page.  

2. In the **Create New Item** window, select **Transform** and click **Add**. The **Create new item of type Transform** appears.

    ![Create new Transformation](create-new-transform.png)

3. Fill in the required fields, such as **Label** and **INPUT TASK Dataset**.

    ![Dialog to create new Transform](dialog-create-transform.png)

4. Expand the ![Mapping Button](button-mapping-text.png){width=11%} menu by clicking the arrow on the right side of the page to expand the menu.

5. Click the circular blue **+** icon on the lower right and select **Add value mapping**.

    ![Add a mapping rule](text-mapping-add-rule.png)

6. In the **Target property** field enter _message_ (the parameter name for the email message) and in the **Value path** field enter _text_ (the path for the text in the Text dataset). When finished, click **Save**.\*

    ![Add a value mapping](text-mapping-add-rule-2.png)

## 8 Create a Request RDF Triples Task Item

The **Request RDF triples** task is used to write all tripled from the company graph into an RDF dataset in NTriples serialization.

1. Click **Create** at the top of the page. 

2. In the **Create new item** window, select **Request RDF triples** and click **Add**. The **Create new item of type Request RDF triples** appears.

    ![Create new Request RDF triples task](create-request-rdf-triples-task.png)

3. Fill in the required details, such as **Label** and click **Create**.

    ![Dialog to create new Request RDF triples task](create-request-rdf-triples-task-2.png)


## 9 Create an RDF Dataset

The **RDF** dataset holds an NTriples file that contains the triples requested by the **Request RDF triples** task, which we will send as the email attachment.

1. Click **Create** at the top of the page.

2. In the **Create new item** window, select **RDF** and click **Add**. The **Create new item of type RDF** appears.

    ![Create new RDF dataset](create-rdf-dataset.png)

3. Fill in the required details, such as **Label** and **FILE**. Under **FILE**, select **Create empty file** and enter a filename for the NTriples file in the **New file name** field. When finished, click **Create**.

    ![Dialog to create new RDF dataset](create-rdf-dataset-2.png)

## 10 Create a Send Email Task Item

1. Click **Create** at the top of the page.

2. In the **Create new item** window, select **Send eMail** and click **Add**. The **Create new item of type Send eMail** appears.

    ![Create new RDF dataset](create-send-email.png)

3. Fill in the required details, such as **Label**, your email credentials for sending, and the recipient email address(es). When finished, click **Create**.

    -  Host: The SMTP host, e.g, mail.myProvider.com
    -  Port: The SMTP port
    -  User: The username for the email account
    -  Password: The password for the email account
    -  To: The recipient email address(es)
  
    <br/>

    ![Create new RDF dataset](create-send-email-2.png)


## 11 Create the Workflow

1. Click **Create** at the top of the page. 
   
2. In the **Create new item** window, select **Workflow** and click **Add**. The **Create new item of type Workflow** appears.

    ![Create new Workflow](add-workflow.png)

3. Fill in the required details (Label) and click **Create**.

    ![Dialog to create new Knowledge Graph dataset](add-workflow-2.png)

4. In the workflow editor, arrange and connect the items as shown below. Items can be dragged from the list of items on the left side onto the canvas. To connect the outputs and inputs, click and hold the output on the right side of an item and drag it to the input on the left side of another item.

   -  The **Knowledge Graph dataset** connects to the **Request RDF triples task** and the **SPARQL Select query task**.
   -  The **Request RDF triples task** connects to the **RDF dataset**. It requests all triples from the products graph and sends them to the dataset.
   -  The **RDF dataset** connects to the **Send eMail task**. It holds the NTriples file that will be attached to the email.
   -  The **SPARQL Select query task** connects to the **Evaluate template task**. Note that the graph to be queried is specified in the SPARQL query itself with the FROM clause, while the input only triggers its execution. The query results are sent to its output.
   -  The **Evaluate template task** connects to the **Text dataset**. It receives the SPARQL query results and sends the evaluated Jinja template to its output.
   -  The **Text dataset** connects to the **Transform**. It holds the text file with the evaluated Jinja template and acts as input for the Transform.\*
  
    ![Workflow 1](workflow-1.png)

5. To send the _message_ parameter with our message text as its value to the **Send eMail task** first, enable its config port by checking the box.
    ![Set Config Port](config-port.png){width="55%"}

    Then, connect the output of the **Transform** to the config port located on the top of the **Send eMail task**. The complete workflow now looks as shown below.

    ![Workflow 2](workflow-2.png)

## 12 Execute the Workflow

1. Execute the **Workflow** by clicking the play button.

    ![Workflow](workflow-execute.png){width="40%"}

2. After the workflow has finished you can find an email in the mailbox of the address you specified for the **Send eMail** task.

<sub>\* The _Evaluate template_ operator can also be connected directly to the _Transform_. In this case, omit [§5](#5-create-a-text-dataset) and enter _output_ instead of _text_ for the _Value path_ of the value mapping in the _Transform_ (see [§6.6](#6-create-a-transformation)).</sub>
