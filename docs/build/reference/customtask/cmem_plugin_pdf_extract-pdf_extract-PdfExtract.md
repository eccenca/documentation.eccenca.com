---
title: "Extract from PDF files"
description: "Extract text and tables from PDF files"
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Extract from PDF files
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

A task to extract text and tables from PDF files.

## Output format

The output is a JSON string on the path `pdf_extract_output`. The format depends on the
["Combine the results from all files into a single value"](#parameter_doc_all_files) parameter.


### Output one entity/value per file

```
{
  "metadata": {
    "Filename": "sample.pdf",
    "Title": "Sample Report",
    "Author": "eccenca GmbH",
    ...
  },
  "pages": [
    {
      "page_number": 1,
      "text": "This is digital text from the PDF.",
      "tables": [...]
    },
    {
      "page_number": 2,
      "text": "",
      "tables": []
    },
    ...
  ]
}
```


### Output one entity/value for all files

```
[
    {
        "metadata": {"Filename": "file1.pdf", ...},
        "pages": [...]
    },
    {
        "metadata": {"Filename": "file2.pdf", ...},
        "pages": [...]
    },
    ...
]
```

## Input format

This task can either work with project files when a regular expression is being used or with
entities coming from another task or dataset. 
The input must be file entities following the [FileEntitySchema](https://github.com/eccenca/cmem-plugin-base/blob/main/cmem_plugin_base/dataintegration/typed_entities/file.py).
If a regular expression is set, the input ports will close and no connection will be possible.


## Parameters

**<a id="parameter_doc_regex">File name regex filter</a>**

Regular expression used to filter the resources of the project to be processed. Only matching file names will be included in the extraction.

**<a id="page_selection">Page selection</a>**

Comma-separated page numbers or ranges (e.g., 1,2-5,7) for page selection. Files that do not contain any of the specified pages will return
empty results with the information logged. If no page selection is specified, all pages will be processed.

**<a id="parameter_doc_all_files">Combine the results from all files into a single value</a>**

If set to "Combine", the results of all files will be combined into a single output value. If set to "Don't combine", each file result will be output in a separate entity.

**<a id="parameter_doc_error_handling">Error Handling Mode</a>**

Specifies how errors during PDF extraction should be handled.  
- *Ignore*: Log errors and continue processing, returning empty or error-marked results.  
- *Raise on errors*: Raise an error when extraction fails.  
- *Raise on errors and warnings*: Treat any warning from the underlying PDF extraction module (pdfplumber) when extracting text and tables from pages as an error if empty results are returned.

**<a id="parameter_doc_table_strategy">Table extraction strategy</a>**

Method used to detect tables in PDF pages. For further explanation click [here](https://github.com/jsvine/pdfplumber/blob/stable/README.md#extracting-tables).

Available strategies include:  
- *lines*: Uses detected lines in the PDF layout to find table boundaries.  
- *text*: Relies on text alignment and spacing.
- *lattice*: Best for machine-generated perfect grids.
- *sparse*: Best for tables with minimal text content.
- *custom*: Allows custom settings to be provided via the advanced parameter below.

**<a id="parameter_doc_custom_table_strategy">Custom table extraction strategy</a>**

Defines a custom table extraction strategy using YAML syntax. Only used if "custom" is selected as the table strategy.

**<a id="parameter_doc_text_strategy">Text extraction strategy</a>**

Method used to extract text in PDF pages. For further explanation click [here](https://github.com/jsvine/pdfplumber/blob/stable/README.md#extracting-text). 

Available strategies include:
- *default*: Balanced for most digital PDFs.
- *raw*: Extract the PDFs with no merging of text fragments.
- *scanned*: Best for scanned PDFs as it merges text more agressively.
- *layout*: Layout-aware extraction for complex/multi-column documents

**<a id="parameter_doc_max_processes">Maximum number of processes for processing files</a>**

Defines the maximum number of processes to use for concurrent file processing. By default, this is set to (number of virtual cores - 1).


## Test regular expression

Clicking the "Test regex pattern" button displays the files in the current project that match the regular expression
specified with the ["File name regex filter"](#parameter_doc_regex) parameter.
This does not display the files if there is another dataset or task connected to the input
as the entities are not known before execution.


## Parameter

### File name regex filter

Regular expression for filtering resources of the project. If this parameter is set, the input port will be closed and project files will be compared against the regular expression.

- Datatype: `string`
- Default Value: `None`



### Combine the results from all files into a single value

If set to 'Combine', the results of all files will be combined into a single output value. If set to 'Don't combine', each file result will be output in a separate entity.

- Datatype: `string`
- Default Value: `no_combine`



### Page selection

Comma-separated page numbers or ranges (e.g., 1,2-5,7) for page selection. Files that do not contain any of the specified pages will return empty results with the information logged. If no page selection is specified, all pages will be processed.

- Datatype: `string`
- Default Value: `None`



### Error Handling Mode

The mode in which errors during the extraction are handled. If set to "Ignore", it will log errors and continue, returning empty or error-marked results for files. When "Raise on errors and warnings" is selected, any warning from the underlying PDF extraction module when extracting text and tables from pages is treated as an error if empty results are returned.

- Datatype: `string`
- Default Value: `raise_on_error`



### Table extraction strategy

Specifies the method used to detect tables in the PDF page. Options include "lines" and "text", each using different cues (such as lines or text alignment) to find tables. If "Custom" is selected, a custom setting needs to defined under advanced options.

- Datatype: `string`
- Default Value: `lines`



### Text extraction strategy

Specifies how text is extracted from a PDF page. Options include "raw", "layout", and others, each interpreting character positions and formatting differently to control how text is grouped and ordered.

- Datatype: `string`
- Default Value: `default`



### Custom table extraction strategy

Custom table extraction strategy in YAML format.

- Datatype: `multiline string`
- Default Value: `# edge_min_length: 3
# explicit_horizontal_lines: []
# explicit_vertical_lines: []
# horizontal_strategy: lines
# intersection_tolerance: 3
# intersection_x_tolerance: 3
# intersection_y_tolerance: 3
# join_tolerance: 3
# join_x_tolerance: 3
# join_y_tolerance: 3
# min_words_horizontal: 1
# min_words_vertical: 3
# snap_tolerance: 3
# snap_x_tolerance: 3
# snap_y_tolerance: 3
# text_settings:
#   extra_attrs: []
#   horizontal_ltr: true
#   keep_blank_chars: false
#   use_text_flow: false
#   vertical_ttb: true
#   x_tolerance: 2
#   y_tolerance: 2
# vertical_strategy: lines`



### Custom_text_strategy

Custom text extraction strategy in YAML format.

- Datatype: `multiline string`
- Default Value: `# extra_attrs: []
# horizontal_ltr: true
# keep_blank_chars: false
# layout: false
# split_at_punctuation: false
# use_text_flow: false
# vertical_ttb: true
# x_density: 7.25
# x_tolerance: 1
# y_density: 13
# y_tolerance: 1`



### Maximum number of processes for processing files

The maximum number of processes to use for processing multiple files concurrently. The default is (number of virtual cores)-1.

- Datatype: `Long`
- Default Value: `9`



