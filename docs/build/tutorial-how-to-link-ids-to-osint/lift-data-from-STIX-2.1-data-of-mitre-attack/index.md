# Build a Knowledge Graph from STIX 2.1 data such as the MITRE ATT&CK® datasets

## Introduction
MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

The MITRE ATT&CK datasets in STIX 2.1 JSON collections are here:

* [enterprise-attack.json](https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack/enterprise-attack.json)
* [mobile-attack.json](https://github.com/mitre-attack/attack-stix-data/blob/master/mobile-attack/mobile-attack.json)
* [ics-attack.json](https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json)

[Structured Threat Information Expression (STIX™)](
https://oasis-open.github.io/cti-documentation/stix/intro.html) is a language and serialization format used to exchange cyber threat intelligence (CTI).

The "ontology" of MITRE ATT&CK with STIX is here: [https://github.com/mitre/cti/blob/master/USAGE.md](https://github.com/mitre/cti/blob/master/USAGE.md)

The objective of this tutorial is not focus on the ontologies. In our use case, we just need to extract several metadata. If the community of STIX wants to resolve their problems, it will be the moment to define a solid ontology. If you are a newbie with the Linked Data technologies, you have to learn to generate in first a functional knowledge graph for your needs before building a perfect ontology for everybody. When you masterize the ontologies, we will modify this first ontology and you could refresh your knowledge graph when you want with Corporate Memory.

This tutorial is written in order to gradually acquire all the skills necessary to build from scratch a knowledge graph with Corporate Memory and update it automatically via Corporate Memory Console.
This tutorial must be completed in order.

Labs:

1. Create a new project for your knowledge graph
2. Import the datasets to convert in RDF
3. Create named graphs of your knowledge graph
4. Create a RDF transformer for STIX 2.1
5. Create the workflow to transform all STIX datasets to RDF
6. Create the global named graph of your knowledge graph
7. Test the SPARQL query to obtain the name, the description and the references of a Mitre tag
8. (optional) Create the Void description of knowledge graph 
9. (optional) Refresh your knowledge graph automatically

You can improve this first knowledge graph with these exercises:

1. Create an inference in your knowledge graph via a SPARQL Update query
2. Create an other knowledge graph for CAPEC linked to MITRE ATT&CK

## Labs

### Create a project

For each type of dataset, you can create an new project with all the tools necessary to convert this dataset in a knowledge graph.

![](23-1-create-project.gif)

### Import datasets

MITRE ATT&CK® has 3 domains (TODO insert link): Entreprise, Mobile and ICS.

Each domain dataset is saved in GitHub:

* [enterprise-attack.json](https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack/enterprise-attack.json)
* [mobile-attack.json](https://github.com/mitre-attack/attack-stix-data/blob/master/mobile-attack/mobile-attack.json)
* [ics-attack.json](https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json)

1. Download these 3 files
2. Create for each JSON file, a JSON dataset:
![](23-1-import-JSON.gif)

!!! Tip

    Give a short name at each dataset/transformer/etc in Corporate Memory to recognize it easily in the workflow view. For example, we will use "MA Entreprise (JSON)" like label and "MITRE ATT&CK® Entreprise dataset STIX 2.1" like description for the Entreprise dataset and so "MA Mobile (JSON)" for Mobile, "MA ICS (JSON)" for ICS, etc.

!!! Success

    Now, you can see these JSON datasets in Corporate Memory:
    ![](23-1-import-JSON-result.png)


### Create named graphs

!!! Info

    A knowledge graph is an abstract concept. Concretly in a triplestore or a RDF graph database via Corporate Memory, the database saves each RDF triple of graph in a named graph or RDF dataset in Corporate Memory. A graph named is a set of triples. So, a knowledge graph can be composed by one or several named graphs.


!!! Tip

    A named graph can be modify without affecting the other named graphs. Each dataset of Mitre can be updated at any moment, so we are going to create a specific named graph for each Mitre dataset to simplify the update of each dataset in your knowledge graph.

    A good practice is to name the named graph by the URI of its real source on the Web, so the labels and graph names of your RDF datasets can be:

    * Entreprise domain
  
        - Label: MA Entreprise (knowledge graph)
        - Graph name: https://github.com/mitre-attack/attack-stix-data/raw/master/enterprise-attack/enterprise-attack.json
  
    * Mobile domain
  
        - Label: MA Mobile (knowledge graph)
        - Graph name: https://github.com/mitre-attack/attack-stix-data/raw/master/mobile-attack/mobile-attack.json
  
    * ICS domain
  
        - Label: MA ICS (knowledge graph)
        - Graph name: https://github.com/mitre-attack/attack-stix-data/raw/master/ics-attack/ics-attack.json


Create one RDF datasets for each Mitre dataset:

1. Add component "RDF dataset"
2. Put a label
3. Put a URI of named graph
4. Enable "Clear graph before workflow execution"
   
![](23-1-create-RDF-dataset.gif)

!!! Success

    Now, you can see these RDF datasets in Corporate Memory:
    ![](23-1-create-RDF-dataset-result.png)

!!! Tip

    The consequence of the option "Clear graph before workflow execution" is the named graph will be deleted (with all its triples) before receiving new triples  when you use this named graph like an output in a workflow and also in the transformer task (in the next step).

    This option is to use only for the graphs which will generate automatically by Corporate Memory.


### Create a transformer

!!! Tip

    There are not bad manners to build a knowledge graph but there are knowledge graphs useless or very hard to use by the analysts or developers in their missions.

    Without having all queries necessary in their missions, your knowledge will continue to evolve to sastify all needs of your users.

    With Corporate Memory, you can develop progressively your vocabularies RDFS or your ontologies OWL to describes your knowledge graph.

    If it's your first knowledge graph, the best manner to start is with RDFS vocabularies because you can develop it like you develop classes and their instances in an object oriented language. It's exactly the same manner to describe the world. Of course, there are differences but you can start a first functional knowledge graph without being an expert.

    Here, you will create all classes and attributes necessary in your use case case. Not more, not less. So, we are adding each STIX object in your knowledge base with its STIX type, its label, its description and its references. Each reference can have an url, a label, a description and an external ID, like Mitre ID or CAPEC ID.

    In UML, you can represent your targeted model like that: here a RDF model to describe an instance of type "course-of-action" in MITRE ATT&CK

    (todo refresh)
    ![RDF model to describe an instance of type "course-of-action" in MITRE ATT&CK](rdf-model-course-of-action.png)

    The SPARQL query for this model can be specify in UML with a RDF pattern: here a RDF pattern to select the "course-of-action" objects with a known Mitre ID
    

    (todo refresh)
    ![RDF pattern to select the "course-of-action" objects with a knowed Mitre ID](rdf-pattern-to-select-a-course-of-action-with-a-mitre-tag.png)

    Without an official vocabulary and its official prefix, we are using the documentation on the Web of its datasets: [[enterprise-attack.json](https://github.com/mitre/cti/blob/master/USAGE.md)](https://github.com/mitre/cti/blob/master/USAGE.md)

    So, to make a prefix, we choosed a short name, for example "ctia", and the IRI will build with the Web address of its documentation with a # at the end (to link to anchors of attributes in the Web page, if they exist):

    ```turtle
    prefix ctia: <https://github.com/mitre/cti/blob/master/USAGE.md#>
    ```

1. Create the prefix of your vocabulary:
      ```turtle
      prefix ctia: <https://github.com/mitre/cti/blob/master/USAGE.md#>
      ```

![](23-1-create-prefix.gif)

2. Create the (Mitre) STIX 2.1 transformer

This transformer will be a component of your worflow. You could reuse it in several workflows in other projects. To create a new transformer, you need to give this:

- Label: STIX 2.1 transformer
- Input: MA Entreprise (JSON)
- Output: MA Entreprise (knowledge graph)

![](23-1-create-transformer.gif)

!!! Tip

    In your use case, there is only this transformer to build this named graph, so there is no consequence on the final knowledge graph when we test this transformer on this graph (automatically cleared after each execution of transformer). However, a good practice is to create a tempory graph in ouput for each transformer, so your final knowledge graph is not affected during the modification of your transformer before executing the workflows with this transformer. In this case, you need to hide this tempory graph of your users.

    You can create a transformer for several syntaxes in input: JSON, XML, CSV, etc. If your format does not exist in Corporate Memory, you can convert your data in JSON before importing this data in Corporate Memory.

!!! Info

    STIX gives the possibility to extend its syntaxes. Mitre uses this possibility. So, in theory, if we need to import all the data, we can extend this transformer at all STIX attributes and add the Mitre attributes described in its [documentation](https://github.com/mitre/cti/blob/master/USAGE.md).

3. Study the tree of STIX data
   
```json
{
    "type": "bundle",
    "id": "bundle--19413d5e-67e5-4a48-a4c8-afb06b7954de",
    "spec_version": "2.1",
    "objects": [
        {
            "type": "x-mitre-collection",
            "id": "x-mitre-collection--1f5f1533-f617-4ca8-9ab4-6a02367fa019",
            "name": "Enterprise ATT&CK",
            "description": "ATT&CK for Enterprise provides a knowledge base of real-world adversary behavior targeting traditional enterprise networks. ATT&CK for Enterprise covers the following platforms: Windows, macOS, Linux, PRE, Office 365, Google Workspace, IaaS, Network, and Containers.",
            ...
        },
        {
            "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
            "type": "attack-pattern",
            "name": "Extra Window Memory Injection",
            "description": "Adversaries may inject malicious code..." ,
            "external_references": [
                {
                    "source_name": "mitre-attack",
                    "external_id": "T1055.011",
                    "url": "https://attack.mitre.org/techniques/T1055/011"
                },
                {
                    "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
                    "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
                    "source_name": "Microsoft Window Classes"
                },...
```

To extract STIX objects with its type, its label, its description and its references, we need to navigate via a root object of type "bundle" before touching the STIX objects. Each object has an ID we suppose unique in all Mitre datasets to generate IRI of all objects. We use your prefix ctia to build the class name and the properties of your RDFS vocabulary. Here, we build the vocabulary of manner agile for your use case because Mitre had not proposed a RDFS vocabulary for its datasets.

4. Create the root object and give it an unique IRI:

- RDF type: ctia:Object
- IRI pattern: https://github.com/mitre-attack/attack-stix-data#{id}
   
![](23-1-extract-root-object.gif)

!!! Tip

    You can develop an IRI from scratch in the IRI formula editor, like here or directly in the form and improve it after, if necessary (see an example in the next step).

    The important is to test the result in the evaluation view.

!!! Success

        During the development of a transformer, you can test your transformation and check all the steps.

        ![](23-1-see-steps-during-a-transformation.png)

5. Link the sub-objects to their root with their IRI and the property ctia:object:
   
- RDF property: ctia:object
- RDF type: ctia:Object
- IRI pattern: https://github.com/mitre-attack/attack-stix-data#{id}

![](23-1-extract-objects.gif)

!!! Tip

    The RDFS classes start by an uppercase and the property by a lowercase and apply the camel case notation, if possible. The objective is to create cool IRI, ie. lisible IDs for humans and unique on the Web.

    There are exceptions, like Wikidata which prefers to use a number for their IRI but with a explicit label in all languages.

    Moreover, if there is no clear ontology in your domain, the best is to take the name of parameters of the source (here json). So, we will use the property, like `ctia:external_id` with underscore because it's the convention of Mitre in its datasets. If Mitre defines a best RDF ontology, we will modify simply your transformer to respect their new ontology.

!!! Tip

    We could limit the number of objects to import, if you add conditions in the formula editor with the field "type" of objects, for example.

1. Extract now their type, label and description with these properties for example:

- ctia:type
- rdfs:label
- ctia:description

![](23-1-extract-properties.gif)

!!! Tip

     STIX type doesn't apply the camel case and doesn't start by an uppercase. We prefers to create a specific property ctia:type for this reason.

     You can reuse a vocabulary already in Corporate Memory (like rdfs) but you are also free to develop a new vocabulary on the fly with your prefixes.

!!! Success

    Now, you can see these RDF datasets in Corporate Memory:
    ![](23-1-create-RDF-dataset-result.png)

7. At the end of the last step, we saw the dataset uses the syntax of Markdown to define a Web link. In the interface of SPLUNK, we need to use the HTML syntax. Modify the formula for the description with the operator "regex replace".

- Regex:  `\[([^\[\]]*)\]\(([^\(\)]*)\)`
- Replace: `<a href='$2' target='blank'>$1</a>`
  
(TODO bug in the interface need to remake the gif)
![](23-1-regex-replace.gif) 


!!! Success
        (TODO bug in the interface, make gif with example)
        ![](23-1-regex-replace.png)

!!! Tip

    At any moment, you will modify your vocabulary according to your needs that you will find during your development. You need to modify this transformer and relaunch all your workflows which use this transformer.

8. Via the same method, we are linking the references objects to their STIX objects via the property `ctia:external_references`.

ctia:Reference object has these properties:

- rdf:type (ctia:Reference)
- ctia:source_name
- ctia:description
- ctia:url
- ctia:external_id

ctia:Reference object has like IRI in the graph its own url.

(TODO bug in the interface need to remake the gif don't forget ctia:external_id)
![](23-1-extract-references.gif)

!!! Success

    To test your transformer, you need to develop one or several SPARQL queries with the RDF pattern which will use in your use case. You are developing this query in the SPARQL editor:

    ![](23-1-sparql-query.gif)

    ```sparql
    #Test 1 transformer STIX 2.1

    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ctia: <https://github.com/mitre/cti/blob/master/USAGE.md#>

    SELECT 
    ?title ?description 
    (GROUP_CONCAT(?link; separator="<br/>") as ?references)
    FROM <https://github.com/mitre-attack/attack-stix-data/raw/master/enterprise-attack/enterprise-attack.json>
    WHERE {
    {
        ?resource ctia:type ctia:course-of-action .
    } union {
        ?resource ctia:type ctia:attack-pattern .
    }

    ?resource rdfs:label ?title ;
                ctia:description ?description ;
                ctia:external_references ?mitre_url .

    ?mitre_url ctia:external_id  "T1490" ;
                ctia:source_name  "mitre-attack" .

    OPTIONAL { 
        ?resource ctia:external_references [
                ctia:url ?reference_url ;
                ctia:source_name ?reference_label ;
                ctia:description ?reference_description 
                ] .
        BIND( CONCAT("<a ref=",STR(?reference_url),"\">",?reference_label,": ",?reference_description ,"</a>") as ?link)
    }
    }
    GROUP BY ?title ?description 
    ```

### Create a workflow

You have now a STIX transformer. We are building here a workflow to apply this transformer for all datasets in same time.

1. Create a workflow with a name, for example "MITRE ATT&CK® workflow"
2. Insert the input JSON dataset
3. Insert the output RDF dataset
3. Insert the transformer
4. Link all components
5. Execute the workflow
6. Save it

(TODO remake the gif when the bug in "URI fix" wil be fixed.)
    ![](23-1-extract-references.gif)

Do the same operations for the three datasets.

!!! Success

    At the end, the workflow looks like that:

    (TODO remake when the bug in "URI fix" wil be fixed.)
    ![](23-1-success-worflow.png)

### Create a global named graph

To simplify the requests by a SPARQL query on your knowledge graph, we are offering the possibility to request all data of these 3 datasets in same time.

We are showing SPARQL tasks, another important feature available in Corporate Memory: the SPARQL tasks with Jinja template

1. Create a RDF dataset

    - Label: MITRE ATT&CK®  (knowledge graph)
    - URI (name of graph): https://attack.mitre.org

2. Create a SPARQL Update task

```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT DATA {
  GRAPH $outputProperties.uri("graph") {
  	$outputProperties.uri("graph") owl:imports $inputProperties.uri("graph")
  }
}
```

!!! Note

    TODO explain 
    $outputProperties.uri("graph")
    $inputProperties.uri("graph")

3. In the same workflow add one SPARQL task for each RDF datasets and in output add the RDF dataset "MITRE ATT&CK®". Execute it and save it.

TODO workflow image


!!! Success

    In the Turtle view of RDF dataset "MITRE ATT&CK®", you can see the triples inserted by your SPARQL query.
    ```turtle
    <http://attack.mitre.org> 
        owl:imports <https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack/enterprise-attack.json>;
        owl:imports <https://github.com/mitre-attack/attack-stix-data/blob/master/mobile-attack/mobile-attack.json>;
        owl:imports <https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json>
        .
    ```

### Test with a SPARQL query



### Create the Void description

Here, the new SPARQL tasks are inserting automatically all the metadata to import the named graphs in this global graph and add a [VoID](https://www.w3.org/TR/void/) description with the statistics of your final knowledge graph.

!!! Info

    [VoID](https://www.w3.org/TR/void/) is an RDF Schema vocabulary for expressing metadata about RDF datasets. t is intended as a bridge between the publishers and users of RDF data.




4. In the same workflow, insert a new SPARQL task with this query to calculate the statistics:

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dcterms: <http://purl.org/dc/terms/>
prefix void: <http://rdfs.org/ns/void#>

INSERT 
{ GRAPH $outputProperties.uri("graph") {
      $outputProperties.uri("graph") a void:Dataset;
          rdfs:label  "MITRE ATT&CK®";
          rdfs:comment  "MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.";
          void:triples ?triples ; 
          void:entities ?entities .
	}
}
USING $outputProperties.uri("graph")
WHERE
  { 
   {
    SELECT (COUNT(DISTINCT ?resource) as ?entities)
    WHERE {
      ?resource a ?class .
    }
  }
  {
    SELECT (COUNT(?s) as ?triples)
    WHERE {
          ?s ?p ?o .
    }
  }
}
```

This query uses the graph in output of workflow to replace the variable `$outputProperties.uri("graph")`. The work This SPARQL task is connected after the dataset

TODO workflow image

!!! Success

    ```turtle
    <http://attack.mitre.org> a void:Dataset;
        dcterms:title "MITRE ATT&CK®";
        dcterms:description "MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.";
        void:triples 1000000000 ; 
        void:entities 3400000 ;
            owl:imports <https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack/enterprise-attack.json>;
            owl:imports <https://github.com/mitre-attack/attack-stix-data/blob/master/mobile-attack/mobile-attack.json>;
            owl:imports <https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json>.
        .
    ```

### Refresh all automatically

1. Find your JSON datasets IDs and your workflow ID
2. execute these command lines

```bash
wget...
cmemc dataset download --replace DATASET_ID OUTPUT_PATH
cmemc workflow execute --wait WORKFLOW_ID
```

3. Create a scheduler in your cron

## Exercices

### Improve the search by text

Corporate Memory indexes some properties automatically, like rdfs:label. Without these properties, it's not easy to find the objects by a search by text. To facilite the research of references, like the mitre id, you are adding the property rdfs:label to reference objects.

1. Open the transformer STIX in your project
2. Add the property rdfs:label to references.
   
![](23-1-model-with-rdfslabel.png)

3. Write the rule in Corporate Memory to build the label of references, like in the RDF model. Try to do this rule alone before to see the response, here:

![](23-1-extract-rdfslabel.png)

!!! Success

        You can test the result when you search the Mitre ID via the explorer:

        <image src="23-1-success-extract-rdfslabel.png" width="60%" height="60%" align="center"/>


### Create an inference

After this tutorial, you want probably to navigate in your new knowledge graph between the relationships of Objects STIX. You need to create inferences in your knowledge graph via SPARQL Update queries.

TODO insert the view easynav with the icons of STIX ???

Apply these operations in Corporate Memory:
1. In the STIX transformer, import also the fields: ctia:source_ref, ctia:target_ref and ctia:relationship_type.
2. Create a new SPARQL Update task "convert STIX relationships to rdf statements" with this code:
```
PREFIX ctia: <https://github.com/mitre/cti/blob/master/USAGE.md#>

INSERT 
  { 
     GRAPH  $outputProperties.uri("graph") {
    			?source  ?property ?target .
       } 
  }
WHERE
  { 
     GRAPH  $inputProperties.uri("graph") {
      ?relationship
         ctia:type ctia:relationship ;
         ctia:source_ref ?source ;
         ctia:target_ref ?target ;
         ctia:relationship_type ?property .
    }
}
```
This SPARQL query create explicitly the STIX links in the knowledge graph. Here, we create a new inference via a simple query.
3. Create a new Knowledge graph dataset "STIX inferences" and import it, like other datasets, via the workflow "generate the global knowledge graph".
4. calculate also the "STIX inferences" dataset
  - In the workflow "Transform all STIX data to RDF", insert the task "convert STIX relationships to rdf statements" and the dataset "STIX inferences"
  - After all others tasks in this workflow, execute the task "convert STIX relationships to rdf statements" and save the inferences in the dataset "STIX inferences"
5. (TODO add STIX icon in CMEM)
6. You can now navigate in EasyNav

### Add the CAPEC dataset
The Common Attack Pattern Enumeration and Classification (CAPEC™) effort provides a publicly available catalog of common attack patterns that helps users understand how adversaries exploit weaknesses in applications and other cyber-enabled capabilities.

Dataset: https://github.com/mitre/cti/blob/master/capec/2.1/stix-capec.json

The CAPEC "ontology": https://github.com/mitre/cti/blob/master/USAGE-CAPEC.md

1. Import the CAPEC dataset in Corporate Memory
2. Create the named graph of CAPEC
3. In the workflows of MITRE ATT&CK, insert the CAPEC dataset in the same knowledge graph
4. Modify the transformer to support the references to CAPEC dataset from MITRE datasets.

## Conclusion
STIX uses JSON syntax and can therefore be converted to RDF via Corporate Memory. Here, we have only extracted a few useful fields for our use case but if you want to import all the data, you will need to import the properties from STIX 2.1, the extended properties in your OSINT dataset and convert the other STIX relationships to RDF statements (like in the final exercice).

## Ressources

- [RDF schemas (Model, pattern, etc)](RDF_model_and_pattern.drawio)