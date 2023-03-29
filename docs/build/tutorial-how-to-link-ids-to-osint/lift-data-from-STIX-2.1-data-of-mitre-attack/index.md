# Build a Knowledge Graph from STIX 2.1 data such as the MITRE ATT&CK® datasets

## Introduction
MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

The MITRE ATT&CK datasets in STIX 2.1 JSON collections are here:
- https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack/enterprise-attack.json
- https://github.com/mitre-attack/attack-stix-data/blob/master/mobile-attack/mobile-attack.json
- https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json

[Structured Threat Information Expression (STIX™)](
https://oasis-open.github.io/cti-documentation/stix/intro.html) is a language and serialization format used to exchange cyber threat intelligence (CTI).

The "ontology" of MITRE ATT&CK with STIX is here: https://github.com/mitre/cti/blob/master/USAGE.md

The objective of this tutorial is not focus on the ontologies. In our use case, we just need to extract several metadata. If the community of STIX wants to resolve their problems, it will be the moment to define a solid ontology. If you are a newbie with the Linked Data technologies, you have to learn to generate in first a functional knowledge graph for your needs before building a perfect ontology for everybody. When you masterize the ontologies, we will modify this first ontology and you could refresh your knowledge graph when you want with Corporate Memory.

This tutorial is written in order to gradually acquire all the skills necessary to build from scratch a knowledge graph with Corporate Memory and update it automatically via Corporate Memory Console.
This tutorial must be completed in order.

Labs:
1. Create a new project for your knowledge graph
2. Import the datasets to convert in RDF
3. Create named graphs of your knowledge graph
4. Create a STIX transformer
5. Create the workflow to transform all STIX data to RDF
6. Create the global graph of your knowledge graph
7. Test the SPARQL query to read the name, the description and the references of one Mitre tag
8. (optional) Create the Void description of knowledge graph 
9. (optional) Update the files via command lines

You can improve this first knowledge graph with these exercises:
1. Create an inference in your knowledge graph via a SPARQL Update query
2. Create an other knowledge graph for CAPEC linked to MITRE ATT&CK

## Labs

### Create a new project for your knowledge graph

### Import the datasets to convert in RDF

### Create named graphs of your knowledge graph

### Create a STIX transformer

![RDF model to describe an instance of type "course-of-action" in MITRE ATT&CK](rdf-model-course-of-action.png)
- extract metadata
- convert link md in html link for the interfaces of SPLUNK

### Create the workflow to transform all STIX data to RDF

### Create the global graph of your knowledge graph

### Test the SPARQL query to read the name, the description and the references of one Mitre tag

![RDF pattern to select a course of action with a mitre tag](rdf-pattern-to-select-a-course-of-action-with-a-mitre-tag.png)

### Create the Void description of knowledge graph 

```
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT DATA {
  GRAPH $outputProperties.uri("graph") {
  	$outputProperties.uri("graph") owl:imports $inputProperties.uri("graph")
  }
}
```

TODO workflow image

```
<http://attack.mitre.org> 
    owl:imports <https://github.com/mitre-attack/attack-stix-data/tree/master/enterprise-attack/enterprise-attack.json>;
    owl:imports <https://github.com/mitre-attack/attack-stix-data/blob/master/mobile-attack/mobile-attack.json>;
    owl:imports <https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json>
    .
```



```
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

TODO workflow image

```
<http://attack.mitre.org> a void:Dataset;
    dcterms:title "MITRE ATT&CK®";
    dcterms:description "MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.";
    void:triples 1000000000 ; 
    void:entities 3400000 .
    .
```

### Update the files via command lines


## Exercices

### Exercice: create an inference in your knowledge graph via a SPARQL Update query
After this tutorial, you want probably to navigate in your new knowledge graph between the relationships of Objects STIX.

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

### Exercice: create an other knowledge graph for CAPEC
The Common Attack Pattern Enumeration and Classification (CAPEC™) effort provides a publicly available catalog of common attack patterns that helps users understand how adversaries exploit weaknesses in applications and other cyber-enabled capabilities.

Dataset: https://github.com/mitre/cti/blob/master/capec/2.1/stix-capec.json

The CAPEC "ontology": https://github.com/mitre/cti/blob/master/USAGE-CAPEC.md

1. Import the CAPEC dataset in Corporate Memory
2. Create the named graph of CAPEC
3. In the workflows of MITRE ATT&CK, insert the CAPEC dataset in the same knowledge graph

## Conclusion
STIX uses JSON syntax and can therefore be converted to RDF via Corporate Memory. Here, we have only extracted a few useful fields for our use case but if you want to import all the data, you will need to import the properties from STIX 2.1, the extended properties in your OSINT dataset and convert the other STIX relationships to RDF statements (like in the final exercice).

