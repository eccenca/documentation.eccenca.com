---
title: "Validate OWL consistency"
description: "Validates the consistency of an OWL ontology."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Validate OWL consistency

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

A task validating the consistency of an OWL ontology and generating an explanation if inconsistencies are found.
The plugin outputs the explanation as text in Markdown format on the path "markdown", the ontology IRI on the path
"ontology_graph_iri", and, if enabled, the valid OWL2 profiles on the path "valid_profiles" as a comma-separated string.

## Options

### Ontology graph IRI

The IRI of the input ontology graph. The graph IRI is selected from a list of graphs of type`owl:Ontology`.

### Ignore missing imports

If enabled, missing imports (`owl:imports`) in the input graphs are ignored.

### Reasoner

The following reasoner options are supported:

- [ELK](https://code.google.com/p/elk-reasoner/) (elk)
- [Expression Materializing Reasoner](http://static.javadoc.io/org.geneontology/expression-materializing-reasoner/0.1.3/org/geneontology/reasoner/ExpressionMaterializingReasoner.html) (emr)
- [HermiT](http://www.hermit-reasoner.com/) (hermit)
- [JFact](http://jfact.sourceforge.net/) (jfact)
- [Structural Reasoner](http://owlcs.github.io/owlapi/apidocs_4/org/semanticweb/owlapi/reasoner/structural/StructuralReasoner.html) (structural)
- [Whelk](https://github.com/balhoff/whelk) (whelk)

### Produce output graph

If enabled, an explanation graph is created.

### Output graph IRI

The IRI of the output graph for the reasoning result.

⚠️ Existing graphs will be overwritten.

### Write markdown explanation file

If enabled, an explanation markdown file is written to the project.

### Output filename

The filename of the Markdown file with the explanation of inconsistencies.

⚠️ Existing files will be overwritten.

### Stop at inconsistencies

Raise an error if inconsistencies are found. If enabled, the plugin does not output entities.

### Validate OWL2 profiles

Validate the input ontology against OWL profiles (DL, EL, QL, RL, and Full) and annotate the result graph.

### Mode

Mode _inconsistency_ generates an explanation for an inconsistent ontology.  
Mode _unsatisfiability_ generates explanations for many unsatisfiable classes at once.

### Output entities

Output entities. The plugin outputs the explanation as text in Markdown format on the path "markdown", the ontology IRI
on the path "ontology_graph_iri", the reasoner option on the path "reasoner", and, if enabled, the valid OWL2 profiles
on the path "valid_profiles".

### Maximum RAM Percentage

Maximum heap size for the Java virtual machine in the DI container running the reasoning process.

⚠️ Setting the percentage too high may result in an out of memory error.

## Parameter

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

The IRI of the output graph for the inconsistency validation. ⚠️ Existing graphs will be overwritten.

- ID: `output_graph_iri`
- Datatype: `string`
- Default Value: `None`

### Output entities

Output entities. The plugin outputs the explanation as text in Markdown format on the path "markdown", the ontology IRI on the path "ontology_graph_iri", the reasoner option on the path "reasoner", and, if enabled, the valid OWL2 profiles on the path "valid_profiles".

- ID: `output_entities`
- Datatype: `boolean`
- Default Value: `false`

### Reasoner

Reasoner option.

- ID: `reasoner`
- Datatype: `string`
- Default Value: `None`

### Output filename

The filename of the Markdown file with the explanation of inconsistencies. ⚠️ Existing files will be overwritten.

- ID: `md_filename`
- Datatype: `string`
- Default Value: `None`

### Mode

Mode "inconsistency" generates an explanation for an inconsistent ontology. Mode "unsatisfiability" generates explanations for many unsatisfiable classes at once.

- ID: `mode`
- Datatype: `string`
- Default Value: `inconsistency`

### Validate OWL2 profiles

Validate the input ontology against OWL profiles (DL, EL, QL, RL, and Full) and annotate the result graph.

- ID: `validate_profile`
- Datatype: `boolean`
- Default Value: `false`

### Stop at inconsistencies

Raise an error if inconsistencies are found. If enabled, the plugin does not output entities.

- ID: `stop_at_inconsistencies`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Maximum RAM Percentage

Maximum heap size for the reasoning process in the DI container. ⚠️ Setting the percentage too high may result in an out of memory error.

- ID: `max_ram_percentage`
- Datatype: `Long`
- Default Value: `20`

