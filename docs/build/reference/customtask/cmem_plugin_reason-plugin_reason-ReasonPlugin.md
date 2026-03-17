---
title: "Reason"
description: "Performs OWL reasoning."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Reason

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

A task performing OWL reasoning. With an OWL ontology and a data graph as input the reasoning result is written to a specified graph.

## Options

### Data graph IRI

The IRI of the input data graph. The graph IRI is selected from a list of graphs of types `di:Dataset`, `void:Dataset`
and `owl:Ontology`.

### Ontology graph IRI

The IRI of the input ontology graph. The graph IRI is selected from a list of graphs of type`owl:Ontology`.

### Ignore missing imports

If enabled, missing imports (`owl:imports`) in the input graphs are ignored.

### Output graph IRI

The IRI of the output graph for the reasoning result.

⚠️ Existing graphs will be overwritten.

### Reasoner

The following reasoner options are supported:

- [ELK](https://code.google.com/p/elk-reasoner/) (elk)
- [Expression Materializing Reasoner](http://static.javadoc.io/org.geneontology/expression-materializing-reasoner/0.1.3/org/geneontology/reasoner/ExpressionMaterializingReasoner.html) (emr)
- [HermiT](http://www.hermit-reasoner.com/) (hermit)
- [JFact](http://jfact.sourceforge.net/) (jfact)
- [Structural Reasoner](http://owlcs.github.io/owlapi/apidocs_4/org/semanticweb/owlapi/reasoner/structural/StructuralReasoner.html) (structural)
- [Whelk](https://github.com/balhoff/whelk) (whelk)

### Generated Axioms

The plugin provides the following parameters to include inferred axiom generators:

#### Class axiom generators

- **Class inclusion (rdfs:subClassOf)**  
The reasoner will infer assertions about the hierarchy of classes, i.e.

`SubClassOf:` statements.  
If there are classes `Person`, `Student` and `Professor`, such that `Person DisjointUnionOf:
Student, Professor` holds, the reasoner will infer `Student SubClassOf: Person`.  

- **Class equivalence (owl:equivalentClass)**  
The reasoner will infer assertions about the equivalence of classes, i.e.

`EquivalentTo:` statements.  
If there are classes `Person`, `Student` and `Professor`, such that `Person DisjointUnionOf:
Student, Professor` holds, the reasoner will infer `Person EquivalentTo: Student and Professor`.

- **Class disjointness (owl:disjointWith)**  
The reasoner will infer assertions about the disjointness of classes, i.e.

`DisjointClasses:` statements.  
If there are classes `Person`, `Student` and `Professor`, such that `Person DisjointUnionOf:
Student, Professor` holds, the reasoner will infer `DisjointClasses: Student, Professor`.

- **Data property equivalence (owl:equivalentProperty)**  
The reasoner will infer axioms about the equivalence of data properties,

 i.e. `EquivalentProperties` statements.  
If there are data properties `identifier` and `enrollmentNumber`, such that `enrollmentNumber
SubPropertyOf: identifier` and `identifier SubPropertyOf: enrollmentNumber` holds, the reasoner
will infer `Student EquivalentProperties: identifier, enrollmentNumber`.

- **Data property inclusion (rdfs:subPropertyOf)**  
The reasoner will infer axioms about the hierarchy of data properties,

i.e. `SubPropertyOf:` statements.  
If there are data properties `identifier`, `studentIdentifier` and `enrollmentNumber`, such that
`studentIdentifier SubPropertyOf: identifier` and `enrollmentNumber SubPropertyOf:
studentIdentifier` holds, the reasoner will infer `enrollmentNumber SubPropertyOf: identifier`.

#### Individual axiom generators

- **Individual class assertions (rdf:type)**  
The reasoner will infer assertions about the classes of individuals, i.e.

`Types:` statements.  
Assume, there are classes `Person`, `Student` and `University` as well as the property
`enrolledIn`, such that `Student EquivalentTo: Person and enrolledIn some University` holds. For
the individual `John` with the assertions `John Types: Person; Facts: enrolledIn
LeipzigUniversity`, the reasoner will infer `John Types: Student`.

- **Individual property assertions**  
The reasoner will infer assertions about the properties of individuals,

i.e. `Facts:` statements.  
Assume, there are properties `enrolledIn` and `offers`, such that `enrolled SubPropertyChain:
enrolledIn o inverse (offers)` holds. For the individuals `John`and `LeipzigUniversity` with the
assertions `John Facts: enrolledIn KnowledgeRepresentation` and `LeipzigUniversity Facts: offers
KnowledgeRepresentation`,  the reasoner will infer `John Facts: enrolledIn LeipzigUniversity`.

#### Object property axiom generators

- **Object property equivalence (owl:equivalentProperty)**  
The reasoner will infer assertions about the equivalence of object

properties, i.e. `EquivalentTo:` statements.  
If there are object properties `hasAlternativeLecture` and `hasSameTopicAs`, such that
`hasAlternativeLecture Characteristics: Symmetric` and `hasSameTopicAs InverseOf:
hasAlternativeLecture` holds, the reasoner will infer `EquivalentProperties: hasAlternativeLecture,
hasSameTopicAs`.

- **Object property inversion (owl:inverseOf)**  
The reasoner will infer axioms about the inversion about object

properties, i.e. `InverseOf:` statements.  
If there is a object property `hasAlternativeLecture`, such that `hasAlternativeLecture
Characteristics: Symmetric` holds, the reasoner will infer `hasAlternativeLecture InverseOf:
hasAlternativeLecture`.

- **Object property inclusion (rdfs:subPropertyOf)**  
The reasoner will infer axioms about the inclusion of object properties,

i.e. `SubPropertyOf:` statements.  
If there are object properties `enrolledIn`, `studentOf` and `hasStudent`, such that `enrolledIn
SubPropertyOf: studentOf` and `enrolledIn InverseOf: hasStudent` holds, the reasoner will infer
`hasStudent SubPropertyOf: inverse (studentOf)`.

- **Object property ranges (rdfs:range)**  
The reasoner will infer axioms about the ranges of object properties,

i.e. `Range:` statements.  
If there are classes `Student` and `Lecture` as wells as object properties `hasStudent` and
`enrolledIn`, such that `hasStudent Range: Student and enrolledIn some Lecture` holds, the
reasoner will infer `hasStudent Range: Student`.

- **Object property domains (rdfs:domain)**  
The reasoner will infer axioms about the domains of object

properties, i.e. `Domain:` statements.  
If there are classes `Person`, `Student` and `Professor` as wells as the object property
`hasRoleIn`, such that `Professor SubClassOf: Person`, `Student SubClassOf: Person` and
`hasRoleIn Domain: Professor or Student` holds, the reasoner will infer `hasRoleIn Domain: Person`.

### Validate OWL2 profiles

Validate the input ontology against OWL profiles (DL, EL, QL, RL, and Full) and annotate the result graph.

### Process valid OWL profiles from input

If enabled along with the "Validate OWL2 profiles" parameter, the valid profiles, ontology IRI and reasoner option is
taken from the config port input (parameters "valid_profiles", "ontology_graph_iri" and "reasoner") and the OWL2
profiles validation is not done in the plugin. The valid profiles input is a comma-separated string (e.g. "Full,DL").

### Output graph import

Add the triple <output_graph_iri> owl:imports <ontology_graph_iri> into the output graph or add the triple
<ontology_graph_iri> owl:imports <output_graph_iri> into the ontology graph.

### Maximum RAM Percentage

Maximum heap size for the Java virtual machine in the DI container running the reasoning process.

⚠️ Setting the percentage too high may result in an out of memory error.

## Parameter

### Data graph IRI

The IRI of the input data graph.

- ID: `data_graph_iri`
- Datatype: `string`
- Default Value: `None`

### Ontology graph IRI

The IRI of the input ontology graph.

- ID: `ontology_graph_iri`
- Datatype: `string`
- Default Value: `None`

### Ignore missing imports

Ignore missing graphs from the import tree of the input graphs.

- ID: `ignore_missing_imports`
- Datatype: `boolean`
- Default Value: `false`

### Output graph IRI

The IRI of the output graph for the reasoning result. ⚠️ Existing graphs will be overwritten.

- ID: `output_graph_iri`
- Datatype: `string`
- Default Value: `None`

### Reasoner

Reasoner option.

- ID: `reasoner`
- Datatype: `string`
- Default Value: `None`

### Individual class assertions (rdf:type)

The reasoner will infer assertions about the classes of individuals, i.e. `Types:` statements. Assume, there are classes `Person`, `Student` and `University` as well as the property `enrolledIn`, such that `Student EquivalentTo: Person and enrolledIn some University` holds. For the individual `John` with the assertions `John Types: Person; Facts: enrolledIn LeipzigUniversity`, the reasoner will infer `John Types: Student`.

- ID: `class_assertion`
- Datatype: `boolean`
- Default Value: `true`

### Individual property assertions

The reasoner will infer assertions about the properties of individuals, i.e. `Facts:` statements. Assume, there are properties `enrolledIn` and `offers`, such that `enrolled SubPropertyChain: enrolledIn o inverse (offers)` holds. For the individuals `John`and `LeipzigUniversity` with the assertions `John Facts: enrolledIn KnowledgeRepresentation` and `LeipzigUniversity Facts: offers KnowledgeRepresentation`, the reasoner will infer `John Facts: enrolledIn LeipzigUniversity`.

- ID: `property_assertion`
- Datatype: `boolean`
- Default Value: `true`

### Class inclusion (rdfs:subClassOf)

The reasoner will infer assertions about the hierarchy of classes, i.e. `SubClassOf:` statements. If there are classes `Person`, `Student` and `Professor`, such that `Person DisjointUnionOf: Student, Professor` holds, the reasoner will infer `Student SubClassOf: Person`.

- ID: `sub_class`
- Datatype: `boolean`
- Default Value: `false`

### Class equivalence (owl:equivalentClass)

The reasoner will infer assertions about the equivalence of classes, i.e. `EquivalentTo:` statements. If there are classes `Person`, `Student` and `Professor`, such that `Person DisjointUnionOf: Student, Professor` holds, the reasoner will infer `Person EquivalentTo: Student and Professor`.

- ID: `equivalent_class`
- Datatype: `boolean`
- Default Value: `false`

### Class disjointness (owl:disjointWith)

The reasoner will infer assertions about the disjointness of classes, i.e. `DisjointClasses:` statements. If there are classes `Person`, `Student` and `Professor`, such that `Person DisjointUnionOf: Student, Professor` holds, the reasoner will infer `DisjointClasses: Student, Professor`.

- ID: `disjoint_classes`
- Datatype: `boolean`
- Default Value: `false`

### Object property inclusion (rdfs:subPropertyOf)

The reasoner will infer axioms about the inclusion of object properties, i.e. `SubPropertyOf:` statements. If there are object properties `enrolledIn`, `studentOf` and `hasStudent`, such that `enrolledIn SubPropertyOf: studentOf` and `enrolledIn InverseOf: hasStudent` holds, the reasoner will infer `hasStudent SubPropertyOf: inverse (studentOf)`.

- ID: `sub_object_property`
- Datatype: `boolean`
- Default Value: `false`

### Object property equivalence (owl:equivalentProperty)

The reasoner will infer assertions about the equivalence of object properties, i.e. `EquivalentTo:` statements. If there are object properties `hasAlternativeLecture` and `hasSameTopicAs`, such that `hasAlternativeLecture Characteristics: Symmetric` and `hasSameTopicAs InverseOf: hasAlternativeLecture` holds, the reasoner will infer `EquivalentProperties: hasAlternativeLecture, hasSameTopicAs`.

- ID: `equivalent_object_property`
- Datatype: `boolean`
- Default Value: `false`

### Object property domains (rdfs:domain)

The reasoner will infer axioms about the domains of object properties, i.e. `Domain:` statements. If there are classes `Person`, `Student` and `Professor` as wells as the object property `hasRoleIn`, such that `Professor SubClassOf: Person`, `Student SubClassOf: Person` and `hasRoleIn Domain: Professor or Student` holds, the reasoner will infer `hasRoleIn Domain: Person`.

- ID: `object_property_domain`
- Datatype: `boolean`
- Default Value: `false`

### Object property ranges (rdfs:range)

The reasoner will infer axioms about the ranges of object properties, i.e. `Range:` statements. If there are classes `Student` and `Lecture` as wells as object properties `hasStudent` and `enrolledIn`, such that `hasStudent Range: Student and enrolledIn some Lecture` holds, the reasoner will infer `hasStudent Range: Student`.

- ID: `object_property_range`
- Datatype: `boolean`
- Default Value: `false`

### Object property inversion (owl:inverseOf)

The reasoner will infer axioms about the inversion about object properties, i.e. `InverseOf:` statements. If there is a object property `hasAlternativeLecture`, such that `hasAlternativeLecture Characteristics: Symmetric` holds, the reasoner will infer `hasAlternativeLecture InverseOf: hasAlternativeLecture`.

- ID: `inverse_object_properties`
- Datatype: `boolean`
- Default Value: `false`

### Data property inclusion (rdfs:subPropertyOf)

The reasoner will infer axioms about the hierarchy of data properties, i.e. `SubPropertyOf:` statements. If there are data properties `identifier`, `studentIdentifier` and `enrollmentNumber`, such that `studentIdentifier SubPropertyOf: identifier` and `enrollmentNumber SubPropertyOf: studentIdentifier` holds, the reasoner will infer `enrollmentNumber SubPropertyOf: identifier`.

- ID: `sub_data_property`
- Datatype: `boolean`
- Default Value: `false`

### Data property equivalence (owl:equivalentProperty)

The reasoner will infer axioms about the equivalence of data properties, i.e. `EquivalentProperties` statements. If there are data properties `identifier` and `enrollmentNumber`, such that `enrollmentNumber SubPropertyOf: identifier` and `identifier SubPropertyOf: enrollmentNumber` holds, the reasoner will infer `Student EquivalentProperties: identifier, enrollmentNumber`.

- ID: `equivalent_data_properties`
- Datatype: `boolean`
- Default Value: `false`

### Validate OWL2 profiles

Validate the input ontology against OWL profiles (DL, EL, QL, RL, and Full) and annotate the result graph.

- ID: `validate_profile`
- Datatype: `boolean`
- Default Value: `false`

### Output graph import

Add the triple <output_graph_iri> owl:imports <ontology_graph_iri> to the output graph or add the triple <ontology_graph_iri> owl:imports <output_graph_iri> to the ontology graph.

- ID: `imports`
- Datatype: `string`
- Default Value: `none`

### Valid OWL2 profiles

Valid OWL2 profiles for the processed ontology.

- ID: `valid_profiles`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Process valid OWL profiles from input

If enabled along with the "Validate OWL2 profiles" parameter, the valid profiles, ontology IRI and reasoner option is taken from the config port input (parameters "valid_profiles", "ontology_graph_iri" and "reasoner") and the OWL2 profiles validation is not done in the plugin. The valid profiles input is a comma-separated string (e.g. "Full,DL", ).

- ID: `input_profiles`
- Datatype: `boolean`
- Default Value: `false`

### Maximum RAM Percentage

Maximum heap size for the reasoning process in the DI container. ⚠️ Setting the percentage too high may result in an out of memory error.

- ID: `max_ram_percentage`
- Datatype: `Long`
- Default Value: `20`

