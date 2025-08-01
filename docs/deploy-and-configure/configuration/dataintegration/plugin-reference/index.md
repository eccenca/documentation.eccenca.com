---
title: "DataIntegration: Plugin Reference"
tags:
    - Reference
---
<style>
/* https://github.com/squidfunk/mkdocs-material/discussions/2532 */
/*number of ".md-nav__list" determines the max level of TOC to be displayed in TOC*/
/*e.g. if ".md-nav__list" is repeated 2 times - the headers ###, ####, #####,  ... will not be displayed in TOC*/
.md-sidebar--secondary .md-nav__list .md-nav__list .md-nav__list {display: none}
</style>
<!-- Auto-Generated. Do not edit directly! -->

# Plugin Reference

## Plugin Tasks

The following plugin tasks are available:

### Cancel Workflow

Cancels a workflow if a specified condition is fulfilled.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| typeUri | Uri | The entity type to check the condition on. |  |
| condition | Enum | The cancellation condition | empty |
| invertCondition | boolean | If true, the specified condition will be inverted, i.e., the workflow execution will be cancelled if the condition is not fulfilled. | false |
| failWorkflow | boolean | If true, the workflow execution will fail if the condition is met. If false, the workflow execution would be stopped, but shown as successfull. | false |

The identifier for this plugin is `CancelWorkflow`.

It can be found in the package `com.eccenca.di.workflow.operators.cancel`.



### Concatenate to file

Concatenates values into a file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| path | String | Values from this path will be concatenated. | *no default* |
| mimeType | String | MIME type of the output file. | *empty string* |
| prefix | MultilineStringParameter | Prefix to be written before the first value. |  |
| glue | MultilineStringParameter | Separator to be inserted between concatenated values. |  |
| suffix | MultilineStringParameter | Suffix to be written after the last value. |  |
| charset | String | The file encoding. | UTF-8 |
| fileExtension | String | File extension of the output file. | .tmp |

The identifier for this plugin is `ConcatenateToFile`.

It can be found in the package `com.eccenca.di.concatenate`.



### SQL query

Executes a custom SQL query on the first input dataset and returns the result as its output.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| command | SqlCodeParameter | SQL command. The name of the table in the statement must be 'dataset', regardless the input. |  |

The identifier for this plugin is `CustomSQLExecution`.

It can be found in the package `com.eccenca.di.spark.operator`.



### Distinct by

Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| distinctPath | String | Entities that share this path will be deduplicated. | *no default* |
| resolveDuplicates | Enum | Strategy to resolve duplicates. | keepLast |

The identifier for this plugin is `DistinctBy`.

It can be found in the package `com.eccenca.di.distinct`.



### Parse JSON

Parses an incoming entity as a JSON dataset. Typically, it is used before a transformation task. Takes exactly one input of which only the first entity is processed.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| inputPath | String | The Silk path expression of the input entity that contains the JSON document. If not set, the value of the first defined property will be taken. | *empty string* |
| basePath | String | The path to the elements to be read, starting from the root element, e.g., '/Persons/Person'. If left empty, all direct children of the root element will be read. | *empty string* |
| uriSuffixPattern | String | A URI pattern that is relative to the base URI of the input entity, e.g., /{ID}, where {path} may contain relative paths to elements. This relative part is appended to the input entity URI to construct the full URI pattern. | *empty string* |
| navigateIntoArrays | boolean | Navigate into arrays automatically. If set to false, the `#array` path operator must be used to navigate into arrays. | true |

The identifier for this plugin is `JsonParserOperator`.

It can be found in the package `org.silkframework.plugins.dataset.json`.



### Join tables

Joins a set of inputs into a single table. Expects a list of entity tables and links.
 All entity tables are joined into the first entity table using the provided links.


This plugin does not require any parameters.
The identifier for this plugin is `Merge`.

It can be found in the package `com.eccenca.di.merge`.



### Merge tables

Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links.
 All entity tables have a relation to the first entity table using the provided links.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| multiTableOutput | boolean | test | true |
| pivotTableName | String | Name of the pivot table. | *empty string* |
| mappingNames | String | Name of the mapping tables. Comma separated list. | *empty string* |
| instanceSetNames | String | Name of the tables joined to the pivot. Comma separated list. | *empty string* |

The identifier for this plugin is `MultiTableMerge`.

It can be found in the package `com.eccenca.di.merge`.



### Pivot

The pivot operator takes data in separate rows, aggregates it and converts it into columns.

The operator works on a flat input schema only and creates a flat output schema.

A pivot table is a data summarization that is used to automatically sort, count, total,
or average data in a dataset.
It allows you to view the data from a different perspective.

The following aggregation (summary) functions are available:

- **first** -  Shows the first value (works with numbers and strings)
- **min** - Shows the lowest value (works with numbers and strings)
- **max** - Shows the highest value (works with numbers and strings)
- **sum** - Adds up the values (works with numbers only)
- **average** - Finds the average of the values (works with numbers only)



| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| pivotProperty | String | The pivot column refers to the column in the input data that is used to organize the data along the horizontal axis of the pivot table. | *no default* |
| firstGroupProperty | String | The name of the first group column in the range. All columns starting with this will be grouped. | *no default* |
| lastGroupProperty | String | The name of the last group column in the range. If left empty, only the first column is grouped. | *empty string* |
| valueProperty | String | The property that contains the grouped values that will be aggregated. | *no default* |
| aggregationFunction | Enum | The aggregation function used to aggregate values. | sum |
| uriPrefix | String | Prefix to prepend to all generated pivot columns. | *empty string* |

The identifier for this plugin is `Pivot`.

It can be found in the package `com.eccenca.di.pivot`.



### Execute REST request (deprecated)

Executes a REST request based on fixed configuration and/or input parameters and returns the result as entity.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| url | String | The URL to execute this request against. This can be overwritten at execution time via input. | *empty string* |
| method | String | The HTTP method. One of GET, PUT, POST, PATCH or DELETE | GET |
| accept | String | The accept header String. | *empty string* |
| requestTimeout | int | Request timeout in ms. The overall maximum time the request should take. | 10000 |
| connectionTimeout | int | Connection timeout in ms. The time until which a connection with the remote end must be established. | 5000 |
| readTimeout | int | Read timeout in ms. The max. time a request stays idle, i.e. no data is send or received. | 10000 |
| contentType | String | The content-type header String. This can be set in case of PUT, PATCH or POST. If another content type comes back, the task will fail. | *empty string* |
| content | String | The content that is send with a POST, PATCH or PUT request. For handling this payload dynamically this parameter must be overwritten via the task input. | *empty string* |
| httpHeaders | MultilineStringParameter | Configure additional HTTP headers. One header per line. Each header entry follows the curl syntax. |  |
| readParametersFromInput | boolean | If this is set to true, specific parameters can be overwritten at execution time. Else inputs are ignored. Parameters that can currently be overwritten: url, content | false |
| multipartFileParameter | String | If set to a non-empty String then instead of a normal POST a multipart/form-data file upload request is executed. This value is used as the form parameter name. | *empty string* |
| authorizationHeader | String | The authorization header. This is usually either 'Authorization' or 'Proxy-Authorization'If left empty, no authorization header is sent. | *empty string* |
| authorizationHeaderValue | PasswordParameter | The authorization header value. Usually this has the form 'type secret', e.g. for OAuth 'bearer <insert secret access token>.'This config parameter will be encrypted in the backend. |  |
| acceptAnySslCertificate | boolean | If enabled this will accept any SSL certificate, i.e. make SSL connections unsecure. Only enable if you know what you are doing! | false |

The identifier for this plugin is `RestOperator`.

It can be found in the package `com.eccenca.di.workflow.operators.rest`.



### Scheduler

Executes a workflow at specified intervals.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| task | TaskReference | The name of the workflow to be executed | *no default* |
| interval | Duration | The interval at which the scheduler should run the referenced task. Must be in ISO-8601 duration format PnDTnHnMn.nS | PT15M |
| startTime | String | The time when the scheduled task is run for the first time, e.g., 2017-12-03T10:15:30. If no start time is set, midnight on the day the scheduler is started is assumed. | *empty string* |
| enabled | boolean | Enables or disables the scheduler. | true |
| stopOnError | boolean | If true, this will stop the scheduler, so the failed task is not scheduled again for execution. | false |

The identifier for this plugin is `Scheduler`.

It can be found in the package `com.eccenca.di.scheduler`.



### Search addresses

Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| searchAttributes | StringIterableParameter | List of attributes that contain search terms. Multiple attributes (comma-separated) will be concatenated into a single search. | *no default* |
| limit | IntOptionParameter | Optionally limits the number of results for each search. |  |
| jsonLdContext | ResourceOption | Optional JSON-LD context to be used for converting the returned JSON to RDF. If not provided, a default context will be used. |  |
| additionalParameters | String | Additional URL parameters to be attached to each HTTP search request. Example: '&countrycodes=de&addressdetails=1'. Consult the API documentation for a list of available parameters. | *empty string* |

The identifier for this plugin is `SearchAddresses`.

It can be found in the package `com.eccenca.di.geo`.


**Configuration**

The geocoding service to be queried for searches can be set up in the configuration.
The default configuration is as follows:

    com.eccenca.di.geo = {
      # The URL of the geocoding service
      # url = "https://nominatim.eccenca.com/search"
      url = "https://photon.komoot.de/api"
      # url = https://api-adresse.data.gouv.fr/search

      # Additional URL parameters to be attached to all HTTP search requests. Example: '&countrycodes=de&addressdetails=1'.
      # Will be attached in addition to the parameters set on each search operator directly.
      searchParameters = ""

      # The minimum pause time between subsequent queries
      pauseTime = 1s

      # Number of coordinates to be cached in-memory
      cacheSize = 10
    }

In general, all services adhering to the [Nominatim search API](https://nominatim.org/release-docs/develop/api/Search/) should be usable.
Please note that when using public services, the pause time should be set to avoid overloading.

**Logging**

By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:

    logging.level {
      com.eccenca.di.geo=DEBUG
    }

### Send eMail

Sends an eMail using an SMTP server.
If connected to a dataset that is based on a file in a workflow, it will send that file whenever the workflow is executed
It can be used to send the result of a workflow via Mail.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| host | String | The SMTP host, e.g, mail.myProvider.com | *no default* |
| port | int | The SMTP port | 587 |
| user | String | Username | *empty string* |
| password | PasswordParameter | Password |  |
| from | String | The sender eMail address | *empty string* |
| receiver | String | The email addresses of the receivers. Email addresses are comma separated. Names must be quoted when containing commas.Example: john.smith@example.com, "Doe, John" <john.doe@example.com>, needs no quoting <needs.no.quoting@example.com> | *empty string* |
| cc | String | The CC-receiver eMail address. Email addresses are comma separated. Names must be quoted when containing commas.Example: john.smith@example.com, "Doe, John" <john.doe@example.com>, needs no quoting <needs.no.quoting@example.com> | *empty string* |
| bcc | String | The BCC-receiver eMail address. Email addresses are comma separated. Names must be quoted when containing commas.Example: john.smith@example.com, "Doe, John" <john.doe@example.com>, needs no quoting <needs.no.quoting@example.com> | *empty string* |
| subject | String | The eMail subject | Dataset |
| message | MultilineStringParameter | The eMail text message |  |
| withAttachment | boolean | If enabled a file from the input is attached to the email. A single input to this operator is expected that provides a file, e.g. a file based dataset (XML, JSON etc.). | true |
| sslConnection | boolean | When enabled a SSL/TLS connection will be forced from the start without negotiation with the server. Not to be confused with STARTTLS which upgrades an insecure connection to a SSL/TLS connection, which is done by default.  | false |
| timeout | int | Timeout in milliseconds to establish a connection or wait for a server response. Setting it to 0 or negative number will disable the timeout. | 10000 |
| readParametersFromInput | boolean | When enabled this allows to send multiple e-mails. All e-mail configurations are input via the first operator input with each entry representing a different e-mail. The optional second input can be a file based dataset for the attachment. E-mail parameters that can be overwritten are: from, receiver, cc, bcc, subject and message. | false |
| nrRetries | int | The number of retries per email when send errors are encountered. | 2 |
| delayBetweenDeliveriesMS | int | The delay in milliseconds between sending two consecutive e-mails. This applies to the retry mechanism, but also to sending multiple e-mails. | 2 |

The identifier for this plugin is `SendEMail`.

It can be found in the package `com.eccenca.di.mail`.



### Execute Spark function


Applies a specified Scala function to a specified field. E.g. when the inputField is 'name', the inputFunction is 'any => "Arrrrgh!" and the alias is 'xxx',)'
a query corresponding to 'Function existingField1, existingFiled2, ... "Arrrrgh!" as "xxx"'  will be generated.
If alias is empty the inputField will be overwritten, otherwise a new field will be added and the rest of the schema stays the same.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| function | MultilineStringParameter | Scala function expression. |  |
| inputField | String | Input field. | *empty string* |
| alias | String | Alias. | *no default* |

The identifier for this plugin is `SparkFunction`.

It can be found in the package `com.eccenca.di.spark.operator`.



### Evaluate template

Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| template | TemplateParameter | The template | *no default* |
| language | String | The template language. Currently, Jinja is supported. | jinja |
| outputAttribute | String | The attribute in the output that will hold the evaluated template. | output |
| fullEvaluation | boolean | If enabled, the entire input set will be evaluated at once. The template will receive a hierarchical 'entities' variable that can be iterated over. A single output entity will be generated that contains the evaluated template. | false |
| forwardInputAttributes | boolean | If true, the input attributes will be forwarded to the output. | false |

The identifier for this plugin is `Template`.

It can be found in the package `com.eccenca.di.templating.operators`.


The template operator supports the Jinja templating language. Documentation about Jinja can be found in the official [Template Designer Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/).

Note that support for RDF properties is limited, because Jinja does not support some special characters (in particula colons) in variable names. This makes it impractical to access RDF properties. For this reason, the transformation that precedes the template operator needs to make sure that it generates attributes that are valid Jinja variable names.

#### Default evaluation

By default, the template is evaluated separately for each entity.
For each input entity, a output entity is generated that provides a single output attribute, which contains the evaluated template.

*Limitation*: For the default evaluation, accessing nested paths is not supported. If the preceding transformation contains hierarchical mappings, only the attributes from the root mapping can be accessed.

#### Full evaluation

If 'full evaluation' is enabled, the entire input set will be evaluated at once.

The entities variable will contain all input entities and can be iterated over:

    {% for entity in entities %}
    {{entity.property}}
    {% endfor %}

A single output entity will be generated that contains the evaluated template.

If the input entities are hierarchical (typically the case if the input transformation is hierarchical), each entity will be hierarchical as well.

Example iterating over an sequence of books that each contains a list of chapters:

    {% for book in entities %}
    Book {{book.title}}
    {% for chapter in book.chapter %}
    Chapter {{chapter.chapterNumber}}
    {% endfor %}
    {% endfor %}

In this example, the child mapping defines a `chapter` target property from which it is accessible from the root entities. If the child mapping allows multiple entities, the value of the property will be a list of entities.

### Unpivot

Given a list of table columns, transforms those columns into attribute-value pairs.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| firstPivotProperty | String | The name of the first pivot column in the range. | *no default* |
| lastPivotProperty | String | the name of the last pivot column in the range. If left empty, all columns starting with the first pivot column are used. | *empty string* |
| attributeProperty | String | The URI of the output column used to hold the attribute. | attribute |
| valueProperty | String | The URI of the output column used to hold the value. | value |
| pivotColumns | String | Comma separated list of pivot column names. This property will override all inferred columns of the first two arguments. | *empty string* |

The identifier for this plugin is `Unpivot`.

It can be found in the package `com.eccenca.di.unpivot`.



### Parse XML

Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| inputPath | String | The Silk path expression of the input entity that contains the XML document. If not set, the value of the first defined property will be taken. | *empty string* |
| basePath | String | The path to the elements to be read, starting from the root element, e.g., '/Persons/Person'. If left empty, all direct children of the root element will be read. | *empty string* |
| uriSuffixPattern | String | A URI pattern that is relative to the base URI of the input entity, e.g., /{ID}, where {path} may contain relative paths to elements. This relative part is appended to the input entity URI to construct the full URI pattern. | *empty string* |

The identifier for this plugin is `XmlParserOperator`.

It can be found in the package `org.silkframework.plugins.dataset.xml`.



### Add project files

Adds file resources to the project that are piped into the input port.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| fileName | String | File name of the uploaded file(s). If multiple files are uploaded, an index will be appended to the file name. If left empty, the existing file names will be used. | *empty string* |
| directory | String | Directory to which the files should be written. If left empty, the files will be uploaded to the project root directory. Note that all files will be written to this directory even if they have been read from a different project directory initially. | *empty string* |
| overwriteStrategy | Enum | The strategy to use if a file with the same name already exists. | fail |

The identifier for this plugin is `addProjectFiles`.

It can be found in the package `org.silkframework.dataset.operations`.



### Delete project files

Removes file resources from the project based on a regular expression.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| filesRegex | String | The regex for filtering the file names. The regex needs to match the full path (i.e. from beginning to end, including sub-directories) in order for the file to be deleted. | *no default* |
| outputEntities | boolean | If enabled the operator outputs entities, one entity for each deleted file, with the path of the file as attribute 'filePath'. | false |

The identifier for this plugin is `deleteProjectFiles`.

It can be found in the package `org.silkframework.dataset.operations`.

Removes file resources from the project based on a regular expression (regex).

The project-relative path of each file of the current project is tested against a user given regular expression and the file is deleted if the expression matches this name. The file names include the sub-directory structure if present but do not start with a `/`. The regular expression has to match the full path of the file and is case sensitive.

Given this list of example files of a project:

```
dataset.csv
my-dataset.xml
json/example.json
json/example_new.json
json/data.xml
```

Here are some regular expressions with the expected result:

- The regex `dataset\.csv` deletes only the first file.
- The regex `json/.*` deletes all files in the `json` sub-directory.
- The regex `new` deletes nothing.
- The regex `.*new.*` deletes the file `json/example_new.json` (and all other files with `new` in the path)

We recommend testing your regular expression before using it. [regex101.com](https://regex101.com) is a nice service to test your regular expressions. [This deep-link](https://regex101.com/?testString=dataset.csv%0Amy-dataset.xml%0Ajson/example.json%0Ajson/example_new.json%0Ajson/data.xml&regex=.*new.*) provides a test bed using the example files and the last expression from the list.

### Download file

Downloads a file from a given URL.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| url | String | The URL of the file to be downloaded. | *empty string* |
| accept | String | The accept header String. | *empty string* |
| requestTimeout | int | Request timeout in ms. The overall maximum time the request should take. | 10000 |
| connectionTimeout | int | Connection timeout in ms. The time until which a connection with the remote end must be established. | 5000 |
| readTimeout | int | Read timeout in ms. The max. time a request stays idle, i.e. no data is send or received. | 10000 |
| httpHeaders | MultilineStringParameter | Configure additional HTTP headers. One header per line. Each header entry follows the curl syntax. |  |
| authorizationHeader | String | The authorization header. This is usually either 'Authorization' or 'Proxy-Authorization'If left empty, no authorization header is sent. | *empty string* |
| authorizationHeaderValue | PasswordParameter | The authorization header value. Usually this has the form 'type secret', e.g. for OAuth 'bearer <insert secret access token>.'This config parameter will be encrypted in the backend. |  |

The identifier for this plugin is `downloadFile`.

It can be found in the package `com.eccenca.di.plugins.rest`.



### Upload File to Knowledge Graph

Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| fileNT | Resource | RDF file (N-Triples or Turtle) from the resource repository that should be uploaded to the Knowledge Graph. | *no default* |
| maxChunkSizeInMB | IntOptionParameter | The N-Triples file will be split into multiple chunks if the file size exceeds the max chunk size. For Turtle files this parameter is ignored since no chunking is supported. |  |
| contentType | Enum | The MIME type of the serialization format of the RDF file. | application/n-triples |

The identifier for this plugin is `eccencaDataPlatformGraphStoreFileUploadOperator`.

It can be found in the package `com.eccenca.di.plugins.dataplatform`.



### Execute REST requests


REST operator that fetches and optionally merges data from a REST endpoint.
It supports executing multiple requests either via input entities that each overwrite config parameters or via paging.
If you only need to download a single file, the "Download file" operator might be the better option.
Most features are currently only supported for JSON REST APIs.
From multiple requests the REST operator can produce a merged JSON result, i.e. for JSON it will concatenate all results in a JSON array.
Alternatively multiple results can be written directly to file (of a JSON dataset), either as a merged JSON file or one file per request inside a ZIP file.
By default the output of this operator is an entity with a single property 'result', which is the (concatenated) JSON string.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| url | String | The URL to execute this request against. This can be overwritten at execution time via input. | *empty string* |
| method | Enum | One of the following HTTP methods: GET, POST, PUT, PATCH or DELETE. | GET |
| accept | String | The accept header String. | *empty string* |
| requestTimeout | int | Request timeout in ms. The overall maximum time the request should take. | 10000 |
| connectionTimeout | int | Connection timeout in ms. The time until which a connection with the remote end must be established. | 5000 |
| readTimeout | int | Read timeout in ms. The max. time a request stays idle, i.e. no data is send or received. | 10000 |
| contentType | String | The content-type header String. This can be set in case of PUT or POST. If another content type comes back, the task will fail. | *empty string* |
| content | String | The content that is send with a POST, PUT or PATCH request. For handling this payload dynamically this parameter must be overwritten via the task input. | *empty string* |
| httpHeaders | MultilineStringParameter | Configure additional HTTP headers. One header per line. Each header entry follows the curl syntax. |  |
| readParametersFromInput | boolean | If this is set to true, specific parameters can be overwritten at execution time and one request per overwrite config will be executed. Else inputs are ignored and exactly one request will be executed. Parameters that can currently be overwritten: url, content | false |
| multipartFileParameter | String | If set to a non-empty String then instead of a normal POST a multipart/form-data file upload request is executed. This value is used as the form parameter name. | *empty string* |
| authorizationHeader | String | The authorization header. This is usually either 'Authorization' or 'Proxy-Authorization'If left empty, no authorization header is sent. | *empty string* |
| authorizationHeaderValue | PasswordParameter | The authorization header value. Usually this has the form 'type secret', e.g. for OAuth 'bearer <insert secret access token>.'This config parameter will be encrypted in the backend. |  |
| delayBetweenRequests | int | The delay between requests in milliseconds. | 0 |
| retriesPerRequest | int | How often should a single request be retried if it fails. | 3 |
| abortOnRequestFail | boolean | If a single request fails, i.e. it reaches its max. retry count, should the execution then be aborted or the next requests be executed. | true |
| limit | int | If this is set to a number greater 0, then only this number of input REST configurations will be executed. Mainly used for debugging and executing a subset. | 0 |
| offset | int | How many input entries to skip. | 0 |
| maxFailedRequests | int | If set to greater 0, then the execution will abort if more than the given number of requests have failed. This should be used to fail early. If 'abort on request fail' is set to true, then this option has no effect. | 0 |
| pagingMethod | Enum | \There are two paging methods currently supported:\1. Next page full URL: The JSON response contains the full URL of the next page. This URL will be used for the subsequent request.\2. Next page identifier: The JSON response contains the ID of the next page. This ID will be used as query parameter for the subsequent request.\In both cases the path to the next page value in the response JSON must be defined via the 'Next page JSON path' parameter.\In case of the 'Identifier next page parameter' paging method, also the parameter 'Next page ID query parameter' must be set.\ | none |
| nextPageJsonPath | String | The path to the JSON value containing the next page value of the JSON response, e.g. paging/next. The path syntax follows the Silk path syntax, but only allows forward paths. | *empty string* |
| nextPageIdQueryParameter | String | The query parameter name for the next page ID that should be attached to the next page URI request. This is necessary for the 'Next page identifier' paging method. | *empty string* |
| outputResultAsFile | boolean | \If a file based dataset is connected to the output of the REST operator, then this option can be enabled in order to overwrite the file resource\of the connected dataset. This allows for handling the result of the REST request/s as a normal dataset. If a non-file based dataset\is connected to this operator the execution will fail.\If disabled, a single entity with a single property 'result' will be output that contains the (merged) result.\ | false |
| urlProperty | String | If this is non-empty, a property is created in the root JSON object (if it exists) with the same name that has the request URL as value. This is mostly relevant if the request URL cannot be re-constructed from the response data. Only supported for JSON response data. | *empty string* |

The identifier for this plugin is `eccencaRestOperator`.

It can be found in the package `com.eccenca.di.plugins.rest`.

#### Core parameter overview

- <a id="parameter_doc_url">`URL`</a>: The URL the request will be executed against. This value can be overwritten at execution time when the 'Read parameters from input' option
         is enabled. This value will also be adapted when a paging approach is configured, see the paging section for more details.
- `Method`: One of the following HTTP methods: GET, POST, PUT, PATCH or DELETE.
- `Accept`: The ACCEPT header value for content negotiation, e.g. 'application/json'.
- <a id="parameter_doc_contentType">`Content type`</a>: The CONTENT-TYPE header value. This is usually used for POST, PUT or PATCH requests when the API endpoint
                  supports multiple different MIME types and/or requires a content MIME type to be set. E.g. 'application/json'
- <a id="parameter_doc_content"></a>`Content`: The text content of a POST, PUT or PATCH request. This value can be overwritten at execution time when the
             'Read parameters from input' option is enabled.

#### Authorization

If the request needs authorization following parameters should be set, else there is no authorization header sent.

- `Authorization header`: The header that is used for authorization, usually either 'Authorization' or 'Proxy-Authorization'.
- `Authorization header value`: The secret value for the authorization, i.e. password or token. This value will be encrypted
                                and cannot be accessed in the user interface anymore after saving it.
                                E.g. for OAuth the value would have the following form: `bearer <TOKEN_VALUE>`.

#### Sending multiple requests

In the default configuration a single requests is sent. If multiple requests should be sent with different URLs and/or content,
the configurations for these requests must be defined via the input port of the REST operator.

- <a id="parameter_doc_readParametersFromInput">Read parameters from input</a>:
    The 'URL' and 'Content' parameter values are read from entities that are input via the input
    port of the operator. The property names are 'url' and 'content' and only overwrite the
    original parameter value if defined.

    For each input entity a separate request will be sent.
- <a id="parameter_doc_limit">Limit</a>: If set to a positive number, then only that number of input entities will be processed as requests.
- <a id="parameter_doc_offset">Offset</a>: If set to a positive number, then that many input entities will be ignored before processing them as requests.

If the option 'Read parameters from input' is enabled, it is currently always assumed that multiple requests will be sent.
The responses must either be of type JSON, then the results are merged into a JSON array, or the 'Output result as file'
option must be enabled in order to write a merged JSON or a ZIP file. See section 'Output options' for more details.

#### Paging

If the REST endpoint does not return all results in a single response, multiple requests (one per page) must usually be sent in order
to fetch all results. This is currently only supported for JSON requests.

- <a id="parameter_doc_pagingMethod">`Paging method`</a>:
   There are two paging methods currently supported:

     1. `Next page full URL`: The JSON response contains the full URL of the next page. This URL will be used for the subsequent request URL.
     2. `Next page identifier`: The JSON response contains the ID of the next page. This ID will be used as query parameter value for the subsequent request.

   In both cases the path to the next page value in the response JSON must be defined via the 'Next page JSON path' parameter.
   In case of the 'Next page identifier' paging method, also the parameter 'Next page ID query parameter' must be set.
- <a id="parameter_doc_nextPageJsonPath">`Next page JSON path`</a>: The property path in the result JSON where the 'next page' URL/value is provided.
   E.g. for following response structure, the value for this parameter would be `paging/next`:

   ```
     {
       ...,
       "paging": {
         "next": "Next ID"
       }
     }
   ```
- <a id="parameter_doc_nextPageIdQueryParameter">`Next page ID query parameter`</a>: If the paging method is 'Next page identifier', this defines the query parameter name that should
  be attached to the original request URL in combination with the 'next page' value of the current response in order
  to request the next page.

#### <a id="parameter_doc_httpHeaders">Setting HTTP headers</a>

- `HTTP headers`: This parameter allows to set HTTP headers of the request being made. Each line of the multi-line value should contain a single header, e.g.
  ```
  Accept-Language: en-US,en;q=0.5
  Cache-Control: max-age=0
  ```

#### Sending a multipart HTTP file request

If the content of a POST request should be sent as file content of a multipart HTTP request, instead of the request body,
following parameter must be configured:

- <a id="parameter_doc_multipartFileParameter">`Multi-part file parameter`</a>: If set to a non-empty value then, instead of a normal POST request, a multipart/form-data
                               file upload request will be executed.
                               The value of this parameter is used as the form parameter name.

#### Output options

By default, the response body of a request is output as value of the 'result' property of a single output entity.
If the response body needs to be processed this can e.g. be achieved with the 'Parse JSON' operator. Alternatively
the response/s can be written to a file based dataset. Currently only text based datasets are supported.

The results of multiple requests, see section 'Sending multiple requests' for details, can be written to
a single, merged file (only supported for JSON) or to a ZIP archive, i.e. a file resource that must end in '.zip'.
In the latter case an entry per request is added to the ZIP file.
Currently, the following datasets support the processing of ZIP files: JSON, XML, CSV and RDF file.

- <a id="parameter_doc_outputResultAsFile">`Output result as file`</a>: If enabled, instead of outputting a single entity, the result/s will be written directly
                           to the file of the file-based dataset that is connected to the output of this operator.

If the option 'Read parameters from input' is enabled, it is currently always assumed that multiple requests will be sent.
The responses must either be JSON, then the results are merged into a JSON array or the 'Output result as file'
option must be enabled in order to write a merged JSON or ZIP file.

#### Fine-tuning timeouts

If requests can take a much longer time than what can usually be expected, it is possible to increase the timeouts to
control when a request should eventually fail.

- `Request timeout`: The maximum overall time in milliseconds the request is allowed to take. Default: `10000`.
- `Connection timeout`: The maximum time in milliseconds the request is allowed to establish a connection to the server. Default: `5000`.
- `Read timeout`: The maximum time a request is allowed to stay idle, i.e. the time while it receives no data. Usually this
   should be greater than the time span between the request being sent and the first data being received. Default: `10000`

#### Throttling requests

If a lot of requests are sent via the 'Read parameters from input' option, it can make sense to throttle the number
of requests sent in a specific time span.

- `Delay between requests`: The delay between subsequent requests in milliseconds. Default: `0`.

#### Error handling

Following parameters can be tuned in order to decide when an execution should be considered as failed.

- `Retries per request`: How often a single request configuration (URL, content) should be retried before considering this
                         request configuration as failed. Default: `3`
- `Abort when request fails`: When enabled, if a single request configuration eventually fails, i.e. it reaches its max. retry count,
                              the overall execution of the REST operator will fail.
- `Max failed requests`: If set to a value greater 0, the execution will abort if more than the given number of request configurations
                         have failed (reached max. retries). This can be used if a number of failed requests can be tolerated.
                         When 'Abort when request fails' is enabled, this option is ignored.

#### Propagating the request URL

If having the request URL in the response data is needed, following parameter needs to be configured:

- <a id="parameter_doc_urlProperty">`URL property`</a>: If this parameter is non-empty the request URL will be added to the response JSON object. It will be added as value to
                  a property with the specified name in the root level of the response JSON object.
                  This is mostly relevant if the request URL cannot be re-constructed from the response data. Only supported for JSON responses.

### Get project files

Get file resources from the project.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| fileName | String | The path of the project file to retrieve. Leave empty if the file regex parameter should be used. | *empty string* |
| filesRegex | String | Optional regular expression for retrieving files. The regex needs to match the full path (i.e. from beginning to end, including sub-directories). | *empty string* |

The identifier for this plugin is `getProjectFiles`.

It can be found in the package `org.silkframework.dataset.operations`.



### SPARQL Construct query

A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| query | SparqlCodeParameter | A SPARQL 1.1 construct query | *no default* |
| tempFile | boolean | When copying directly to the same SPARQL Endpoint or when copying large amounts of triples, set to True by default | true |

The identifier for this plugin is `sparqlCopyOperator`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.tasks`.



### SPARQL Select query

A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| selectQuery | SparqlCodeParameter | A SPARQL 1.1 select query | *no default* |
| limit | String | If set to a positive integer, the number of results is limited | *empty string* |
| optionalInputDataset | SparqlEndpointDatasetParameter | An optional SPARQL dataset that can be used for example data, so e.g. the transformation editor shows mapping examples. |  |
| sparqlTimeout | int | SPARQL query timeout (select/update) in milliseconds. A value of zero means that there is no timeout set explicitly. If a value greater zero is specified this overwrites possible default timeouts. | 0 |

The identifier for this plugin is `sparqlSelectOperator`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.tasks`.



### SPARQL Update query

A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template.
The output of this operator should be connected to the SPARQL datasets to which the results should be written. In contrast to the SPARQL select operator, no FROM clause gets injected into the query.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| sparqlUpdateTemplate | SparqlCodeParameter | \This operator takes a SPARQL Update Query Template that depending on the templating mode (Simple/Velocity Engine) supports\a set of templating features, e.g. filling in input values via placeholders in the template.\Example for the 'Simple' mode:\  DELETE DATA { ${<PROP_FROM_ENTITY_SCHEMA1>} rdf:label ${"PROP_FROM_ENTITY_SCHEMA2"} }\  INSERT DATA { ${<PROP_FROM_ENTITY_SCHEMA1>} rdf:label ${"PROP_FROM_ENTITY_SCHEMA3"} }\  \  This will insert the URI serialization of the property value PROP_FROM_ENTITY_SCHEMA1 for the ${<PROP_FROM_ENTITY_SCHEMA1>} expression.\  And it will insert a plain literal serialization for the property values PROP_FROM_ENTITY_SCHEMA2/3 for the template literal expressions.\  It is be possible to write something like ${"PROP"}^^<http://someDatatype> or ${"PROP"}@en.\Example for the 'Velocity Engine' mode:\  DELETE DATA { $row.uri("PROP_FROM_ENTITY_SCHEMA1") rdf:label $row.plainLiteral("PROP_FROM_ENTITY_SCHEMA2") }\  #if ( $row.exists("PROP_FROM_ENTITY_SCHEMA1") )\    INSERT DATA { $row.uri("PROP_FROM_ENTITY_SCHEMA1") rdf:label $row.plainLiteral("PROP_FROM_ENTITY_SCHEMA3") }\  #end\  Input values are accessible via various methods of the 'row' variable:\  - uri(inputPath: String): Renders an input value as URI. Throws exception if the value is no valid URI.\  - plainLiteral(inputPath: String): Renders an input value as plain literal, i.e. escapes problematic characters etc.\  - rawUnsafe(inputPath: String): Renders an input value as is, i.e. no escaping is done. This should only be used – better never – if the input values can be trusted.\  - exists(inputPath: String): Returns true if a value for the input path exists, else false.\  The methods uri, plainLiteral and rawUnsafe throw an exception if no input value is available for the given input path.\  In addition to input values, properties of the input and output tasks can be accessed via the inputProperties and outputProperties objects\  in the same way as the row object, e.g.\    $inputProperties.uri("graph")\  For more information about the Velocity Engine visit http://velocity.apache.org.\     | *no default* |
| batchSize | int | How many entities should be handled in a single update request. | 1 |
| templatingMode | Enum | The templating mode. 'Simple' only allows simple URI and literal insertions, whereas 'Velocity Engine' supports complex templating. See 'Sparql Update Template' parameter description for examples and http://velocity.apache.org for details on the Velocity templates. | simple |

The identifier for this plugin is `sparqlUpdateOperator`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.tasks`.



### Request RDF triples

A task that requests all triples from an RDF dataset.

This plugin does not require any parameters.
The identifier for this plugin is `tripleRequestOperator`.

It can be found in the package `com.eccenca.di.workflow.operators.tripleRequest`.



### Normalize units of measurement

Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation in three columns:
  * The normalized numeric value.
  * The unit symbol of the SI-system-unit pertaining to the value.
  * The origin unit symbol from which it was normalized (so we are able to reverse this action).


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| valueProperties | String | The names (comma-separated) of columns containing numeric values interpreted as quantities of the dimension indicated by the pertaining unit. | *no default* |
| unitProperties | String | The names (comma-separated) of dedicated columns containing the unit symbol for the pertaining value in the value column (the positions in this list have to align with the pertaining value columns). Either this param or 'static unit' has to be set. | *empty string* |
| staticUnits | String | Unit symbols (comma-separated) defining the unit for all values in the pertaining value column. If set, the 'unitProperty' param will be ignored and all values of the value column have to be numbers without unit symbols (the positions in this list have to align with the pertaining value columns). | *empty string* |
| targetUnits | String | Unit symbols (comma-separated) defining the target unit to which the value column will be converted (Note: Make sure the input unit can be converted to the target unit). By default the pertaining SI-base unit will be used as normalization unit (the positions in this list have to align with the pertaining value columns) | *empty string* |
| suppressErrors | boolean | If true, will ignore any parsing or value conversion error and return an empty result (might happen because of unknown unit symbols or non-numbers as values). Beware, the value will be lost completely! | false |
| configFilePath | ResourceOption | An absolute file path for a unit CSV configuration file (for syntax see 'configuration' param). If set, the 'configuration' param will be ignored. |  |
| configuration | MultilineStringParameter | While all SI units and decimal prefixes are supported by default, custom or obsolete units have to be added via this configuration.\       NOTE: when constructing formulae depending on other units defined in the configuration, make sure to order them dependently.\       ALSO: Rational numbers are not supported by the UCUM syntax, express them as a fraction (see 'grain' example below).\      | \# Example configuration, don't forget to remove the '#' in front of each row.\#      CSV COLUMNS:\#       * unit name - the human readable name of the unit\#       * override  - (true|false) if true, any assigned unit to the given symbol will be dropped, else if the unit symbol is already in use, the new definition will be ignored\#       * symbol    - the main symbol used to depict the unit\#       * equals formula - the formula to derive the given unit from already registered units\#       * [all additional columns] - alternative symbols, will be registered for this unit\# Example CSV:\#      unit name, override, symbol, equals formula\#       Are     , true    , are   , 100.m2\#       Denier  , true    , den   , g/(9.km)\#       Grain   , true    , gr    , (45.g)/100\#       Pound   , true    , lb    , (45359237.kg)/100000000 , # , lbm\      |

The identifier for this plugin is `ucumNormalizationTask`.

It can be found in the package `com.eccenca.di.measure`.



### Validate XML

Validates an XML dataset against a provided XML schema (XSD) file.
         Any errors are written to the output. Can be used in conjunction with the `Cancel Workflow` operator in order to stop the workflow if errors have been found."


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | Resource | The XSD file to be used for validating the XML. | *no default* |

The identifier for this plugin is `validateXsdOperator`.

It can be found in the package `org.silkframework.plugins.dataset.xml`.



### XSLT

A task that converts an XML resource via an XSLT script and writes the transformed output into a file resource.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | Resource | The XSLT file to be used for transforming XML. | *no default* |

The identifier for this plugin is `xsltOperator`.

It can be found in the package `org.silkframework.plugins.dataset.xml`.



## Dataset Plugins

The following dataset plugins are available:

### Deprecated

#### SparkSQL view

Use the SQL endpoint dataset instead.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| viewName | String | The name of the view. This specifies the table that can be queried by another virtual dataset or via JDBC (the 'default' schema is used for all virtual datasets). | *no default* |
| query | String | Optional SQL query on the selected table. Has no effect when used as an output dataset. | *empty string* |
| cache | boolean | Optional boolean option that selects if the table should be cached by Spark or not (default = true). | true |
| uriPattern | String | A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property. | *empty string* |
| properties | String | Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line. | *empty string* |
| charset | String | The source internal encoding, e.g., UTF8, ISO-8859-1 | UTF-8 |
| arraySeparator | String | The character that is used to separate the parts of array values. Write "back slash t" to specify the tab character. | | |
| useCompatibleTypes | boolean | If true, basic types will be used for types that otherwise would result in client errors. This mainly that arrays will be stored as Strings separated by the separator defined above. If the view is only for use within a SparkContext, this can be set to false. | true |

The identifier for this plugin is `sparkView`.

It can be found in the package `com.eccenca.di.sql.spark.virtual`.



### Embedded

#### Hive database

Read from or write to an embedded Apache Hive endpoint.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| schema | String | Name of the hive schema or namespace. | *empty string* |
| table | String | Name of the hive table. | *no default* |
| query | String | Optional query for projection and selection (e.g. " SELECT * FROM table WHERE x = true".  | *empty string* |
| uriPattern | String | A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property. | *empty string* |
| properties | String | Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line. | *empty string* |
| charset | String | The source internal encoding, e.g., UTF8, ISO-8859-1 | UTF-8 |

The identifier for this plugin is `Hive`.

It can be found in the package `com.eccenca.di.spark.dataset`.



#### Knowledge Graph

Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| endpoint | String | The named endpoint within the eccenca DataPlatform. | default |
| graph | GraphUriParameter | The URI of the named graph. | *no default* |
| pageSize | int | The number of solutions to be retrieved per SPARQL query. | 100000 |
| pauseTime | int | The number of milliseconds to wait between subsequent query | 0 |
| retryCount | int | The number of retries if a query fails | 3 |
| retryPause | int | The number of milliseconds to wait until a failed query is retried. | 1000 |
| strategy | Enum | The strategy use for retrieving entities: simple: Retrieve all entities using a single query; subQuery: Use a single query, but wrap it for improving the performance on Virtuoso; parallel: Use a separate Query for each entity property. | parallel |
| clearGraphBeforeExecution | boolean | If set to true this will clear the specified graph before executing a workflow that writes to it. Note that this will always use the configured graph and ignore any overwritten values from the config port. | false |
| entityList | MultilineStringParameter | A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace. |  |
| sparqlTimeout | int | SPARQL query timeout (select/update) in milliseconds. A value of zero means that there is no timeout. If a value greater zero is specified this overwrites possible default timeouts. This timeout is also propagated to DataPlatform and may overwrite default timeouts there. | 0 |
| optimizedRetrieve | boolean | Optimized retrieval method to remove load from the underlying triple store. Query parallelism is limited and cheaper queries are executed against the backend. By putting the main work on DataIntegration side, the RDF backend is kept responsive. | true |

The identifier for this plugin is `eccencaDataPlatform`.

It can be found in the package `com.eccenca.di.plugins.dataplatform`.



#### In-memory dataset

A Dataset that holds all data in-memory.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| clearGraphBeforeExecution | boolean | If set to true this will clear this dataset before it is used in a workflow execution. | true |

The identifier for this plugin is `inMemory`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.datasets`.



#### Internal dataset

Dataset for storing entities between workflow steps. The underlying dataset type can be configured using the `dataset.internal.*` configuration parameters.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| graphUri | String | The RDF graph that is used for storing internal data | *null* |

The identifier for this plugin is `internal`.

It can be found in the package `org.silkframework.plugins.dataset`.



#### SQL endpoint

Provides a JDBC endpoint that exposes workflow or transformation results as tables, which can be queried using SQL.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| tableNamePrefix | String | Prefix of the table that will be shared. In the case of complex mappings more than one table will be created. If one name is given it will be used as a prefix for table names. If left empty the table names will be generated from the user name and time stamps and start with 'root', 'object-mapping' | *empty string* |
| cache | boolean | Optional boolean option that selects if the table should be cached by Spark or not (default = true). | true |
| arraySeparator | String | The character that is used to separate  the parts of array values. Write \\t to specify the tab character. | | |
| useCompatibleTypes | boolean | If true, basic types will be used for unusual data types that otherwise may result in client errors. Try switching this on, if a client has weird error messages. (Default = true) | true |
| map | Map | Mapping of column names. Similar to aliases E.g. 'c1:c2' would rename column c1 into c2. |  |

The identifier for this plugin is `sqlEndpoint`.

It can be found in the package `com.eccenca.di.sql.spark.endpoint`.

_SQL endpoint dataset parameters_

The dataset only requires that the _tableNamePrefix_ parameter is given. This will be used as the prefix for the names of the generated tables.
When a set of entities is written to the endpoint _a view is generated for each entity type_ (defined by an 'rdf_type' attribute).
That means that the mapping or data source that are used as input for the SQL endpoint need to have a type or require a user defined type mapping.

The operator has a _compatibility mode_. This mode will avoid complex types such as Arrays. When arrays exist in the input they
are converted to a String using the given _arraySeparator_. This avoids errors and warnings in some Jdbc clients that are unable to
handle typed arrays and may make working with software like Excel easier.

The parameter _aliasMap_ of the endpoint allows the specification of column aliases. The map is a comma separated list of key-value pairs.
Each key and value is denoted by ```key:value```. An example for renaming 2 columns (source1, source2 to target1, target2) in the result would be:
```source1:target1,source2:target2```

Note: Table and column (mapping target) names will be automatically converted to be valid in as many databases as possible.
Table names will be shortened to 128 characters. Only a-z, A-Z, 0-9 and _ are allowed. Others will be replaced with an underscore.
Column names undergo the same transformation but will be converted to lower case as well. The log will inform about changes.
The table names will be generated based on the target type of each mapping.
The user needs to make sure that each object mapping specifies a unique type.
If two object mappings define the same type, only the last one will be written.

_SQL endpoint activity_

See [ActivityDocumentation] for a general description of the Data Integration activities.
The activity will _start_ automatically, when the SQL endpoint is used
as a data sink and Data Integration is configured to make the SQL endpoint accessible remotely.

When the activity is started and _running_ it returns the server status and JDBC URL as its value.

_Stopping_ the activity will drop all views generated by the activity. It can be _restarted_ by rerunning the
workflow containing it as a sink.

_Remote client configuration (via JDBC and ODBC)_

Within Data Integration the SQL endpoint can be used as a source or sink like any other dataset. If the _startThriftServer_ option is set to 'true'
access via JDBC or ODBC is possible.

[ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity) and [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity) drivers can be used to connect to relational databases.

When selecting a version of a driver the client operating system and its type (32bit/64 bit) are the most important factors.
The version of the client drivers sometimes is the same as the server's.
If no version of a driver is given, the newest driver of the vendor should work, as it _should_ be backwards compatible.

Any JDBC or ODBC client can connect to an SQL endpoint dataset. SparkSQL uses the same query processing as Hive, therefore the requirements for the client are:

- A JDBC driver compatible with _Hive 1.2.1_[^hi] (platform independent driver _org.apache.hive.jdbc.HiveDriver_ is needed) or
- A JDBC driver compatible with _Spark 2.3.3_
- A Hive ODBC driver (ODBC driver for the client architecture and operating system needed)

[^hi]: Hive 1.2.1 is [ODPi](https://github.com/odpi/specs/blob/master/ODPi-Runtime.md) runtime compliant

A detailed instruction to connect to a Hive or SparkSQL endpoint with various tools (e.g. SQuirreL, beeline, SQL Developer, ...) can be found at _[Apache HiveServer2 Clients](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients)_.
The database client _[DBeaver](https://dbeaver.io/)_ can connect to the SQL endpoint out of the box.

#### Variable dataset (deprecated)

Dataset that acts as a placeholder in workflows and is replaced at request time. This is deprecated, please use the 'replaceable input/output dataset config' in the node menu of the workflow editor instead.

This plugin does not require any parameters.
The identifier for this plugin is `variableDataset`.

It can be found in the package `org.silkframework.dataset`.



### File

#### Alignment

Writes the alignment format specified at http://alignapi.gforge.inria.fr/format.html.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | The alignment file. | *no default* |

The identifier for this plugin is `alignment`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.datasets`.



#### Avro

Read from or write to an Apache Avro file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | Path (e.g. relative like 'path/filename.avro' or absolute 'hdfs:///path/filename.avro'). | *no default* |
| uriPattern | String | A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property. | *empty string* |
| properties | String | Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line. | *empty string* |
| charset | String | The file encoding, e.g., UTF8, ISO-8859-1 | UTF-8 |

The identifier for this plugin is `avro`.

It can be found in the package `com.eccenca.di.spark.dataset`.



#### CSV

Read from or write to an CSV file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | The CSV file. This may also be a zip archive of multiple CSV files that share the same schema. | *no default* |
| properties | String | Comma-separated list of properties. If not provided, the list of properties is read from the first line. Properties that are no valid (relative or absolute) URIs will be encoded. | *empty string* |
| separator | String | The character that is used to separate values. If not provided, defaults to ',', i.e., comma-separated values. "\\t" for specifying tab-separated values, is also supported. | , |
| arraySeparator | String | The character that is used to separate the parts of array values. Write "\\t" to specify the tab character. | *empty string* |
| quote | String | Character used to quote values. | " |
| uri | String | *Deprecated* A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property. | *empty string* |
| charset | String | The file encoding, e.g., UTF-8, UTF-8-BOM, ISO-8859-1 | UTF-8 |
| regexFilter | String | A regex filter used to match rows from the CSV file. If not set all the rows are used. | *empty string* |
| linesToSkip | int | The number of lines to skip in the beginning, e.g. copyright, meta information etc. | 0 |
| maxCharsPerColumn | int | The maximum characters per column. *Warning*: System will request heap memory of that size (2 bytes per character) when reading the CSV. If there are more characters found, the parser will fail. | 128000 |
| ignoreBadLines | boolean | If set to true then the parser will ignore lines that have syntax errors or do not have to correct number of fields according to the current config. | false |
| quoteEscapeCharacter | String | Escape character to be used inside quotes, used to escape the quote character. It must also be used to escape itself, e.g. by doubling it, e.g. "". If left empty, it defaults to quote. | " |
| zipFileRegex | String | If the input resource is a ZIP file, files inside the file are filtered via this regex. | ^(?!.*[\\/\\\\]\\..*$|^\\..*$).*\\.csv |
| clearBeforeExecution | boolean | If set to true this will clear the specified file before executing a workflow that writes to it. | false |
| trimWhitespaceAndNonPrintableCharacters | boolean | If set to true, this will trim whitespace and non-printable characters from the contents of the CSV dataset. | false |

The identifier for this plugin is `csv`.

It can be found in the package `org.silkframework.plugins.dataset.csv`.



#### Excel

Read from or write to an Excel workbook in Open XML format (XLSX).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | File name inside the resources directory. | *no default* |
| streaming | boolean | Streaming enables reading and writing large Excels files. Warning: Be careful to disable streaming for large datasets (> 10MB), because of high memory consumption. | true |
| linesToSkip | int | The number of lines to skip in the beginning when reading files. | 0 |
| hasHeader | boolean | If true, the first line will be read as the table header, which defines the column names. If false, the first line will be read as data. In that case, the columns need to be adressed using #A, #B, etc. | true |
| outputObjectValues | boolean | Output results from object rules (URIs). | true |

The identifier for this plugin is `excel`.

It can be found in the package `com.eccenca.di.excel`.



#### RDF

Dataset which retrieves and writes all entities from/to an RDF file.
For reading, the dataset is loaded in-memory and thus the size is restricted by the available memory.
Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | The RDF file. This may also be a zip archive of multiple RDF files. | *no default* |
| format | String | Optional RDF format. If left empty, it will be auto-detected based on the file extension. N-Triples is the only format that can be written, while other formats can only be read. | *empty string* |
| graph | String | The graph name to be read. If not provided, the default graph will be used. Must be provided if the format is N-Quads. | *empty string* |
| entityList | MultilineStringParameter | A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace. |  |
| zipFileRegex | String | If the input resource is a ZIP file, files inside the file are filtered via this regex. | .* |

The identifier for this plugin is `file`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.datasets`.



#### JSON

Read from or write to a JSON or JSON Lines file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | JSON file. This may also be a zip archive of multiple JSON files that share the same schema. | *no default* |
| template | JsonCodeParameter | Template for writing JSON. The term {{output}} will be replaced by the written JSON. | {{output}} |
| navigateIntoArrays | boolean | Navigate into arrays automatically. If set to false, the `#array` path operator must be used to navigate into arrays. | true |
| basePath | String | The path to the elements to be read, starting from the root element, e.g., '/Persons/Person'. If left empty, all direct children of the root element will be read. | *empty string* |
| uriPattern | String | A URI pattern, e.g., http://namespace.org/{ID}, where {path} may contain relative paths to elements | *empty string* |
| maxDepth | int | Maximum depth of written JSON. This acts as a safe guard if a recursive structure is written. | 15 |
| streaming | boolean | Streaming allows for reading large JSON files. If streaming is enabled, backward paths are not supported. | true |
| zipFileRegex | String | If the input resource is a ZIP file, files inside the file are filtered via this regex. | ^(?!.*[\\/\\\\]\\..*$|^\\..*$).*\\.jsonl?$ |

The identifier for this plugin is `json`.

It can be found in the package `org.silkframework.plugins.dataset.json`.

Typically, this dataset is used to transform an JSON file to another format, e.g., to RDF.

##### Reading

In addition to plain JSON files, *JSON Lines* files can also be read.

For reading, the JSON dataset supports a number of special paths:
- `#id` Is a special syntax for generating an id for a selected element. It can be used in URI patterns for entities which do not provide an identifier. Examples: `http://example.org/{#id}` or `http://example.org/{/pathToEntity/#id}`.
- `#text` retrieves the text of the selected node.
- The backslash can be used to navigate to the parent JSON node, e.g., `\parent/key`. The name of the backslash key (here `parent`) is ignored.

##### Writing

When writing JSON, all entities need to possess a unique URI. Writing multiple root entities with the same URI will result in multiple entries in the generated JSON. If multiple nested entities with the same URI are written, only the last entity with a given URI will be written.

#### Multi CSV ZIP

Reads from or writes to multiple CSV files from/to a single ZIP file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | Zip file name inside the resources directory/repository. | *no default* |
| separator | String | The character that is used to separate values. If not provided, defaults to ',', i.e., comma-separated values. "\\t" for specifying tab-separated values, is also supported. | , |
| arraySeparator | String | The character that is used to separate the parts of array values. Write "\\t" to specify the tab character. | *empty string* |
| quote | String | Character used to quote values. | " |
| charset | String | The file encoding, e.g., UTF8, ISO-8859-1 | UTF-8 |
| linesToSkip | int | The number of lines to skip in the beginning, e.g. copyright, meta information etc. | 0 |
| maxCharsPerColumn | int | The maximum characters per column. If there are more characters found, the parser will fail. | 128000 |
| ignoreBadLines | boolean | If set to true then the parser will ignore lines that have syntax errors or do not have to correct number of fields according to the current config. | false |
| quoteEscapeCharacter | String | Escape character to be used inside quotes, used to escape the quote character. It must also be used to escape itself, e.g. by doubling it, e.g. "". If left empty, it defaults to quote. | " |
| append | boolean | If 'True' then files in the ZIP archive are only added or updated, all other files in the ZIP stay untouched. If 'False' then a new ZIP file will be created on every dataset write. | true |
| zipFileRegex | String | Filter file paths inside the ZIP file via this regex. By default sub folders or files not ending with .csv are ignored. | ^[^/]*\\.csv$ |
| clearBeforeExecution | boolean | If set to true this will clear the specified file before executing a workflow that writes to it. | true |
| trimWhitespaceAndNonPrintableCharacters | boolean | If set to true, this will trim whitespace and non-printable characters from the contents of the CSV dataset. | false |

The identifier for this plugin is `multiCsv`.

It can be found in the package `com.eccenca.di.plugins.csv`.



#### ORC

Read from or write to an Apache ORC file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | Path (e.g. relative like 'path/filename.orc' or absolute 'hdfs:///path/filename.orc'). | *no default* |
| uriPattern | String | A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property. | *empty string* |
| properties | String | Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line. | *empty string* |
| partition | String | Optional specification of the attribute for output partitioning | *empty string* |
| compression | String | Optional compression algorithm (e.g. snappy, zlib) | snappy |
| charset | String | The file encoding, e.g., UTF8, ISO-8859-1 | UTF-8 |

The identifier for this plugin is `orc`.

It can be found in the package `com.eccenca.di.spark.dataset`.



#### Parquet

Read from or write to an Apache Parquet file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | Path (e.g. relative like 'path/filename.orc' or absolute 'hdfs:///path/filename.parquet'). | *no default* |
| uriPattern | String | A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property. | *empty string* |
| properties | String | Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line. | *empty string* |
| partition | String | Optional specification of the attribute for output partitioning | *empty string* |
| compression | String | Optional compression algorithm (e.g. snappy, zlib) | *empty string* |
| charset | String | The file encoding, e.g., UTF8, ISO-8859-1 | UTF-8 |

The identifier for this plugin is `parquet`.

It can be found in the package `com.eccenca.di.spark.dataset`.



#### XML

Read from or write to an XML file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | The XML file. This may also be a zip archive of multiple XML files that share the same schema. | *no default* |
| basePath | String | The base path when writing XML. For instance: /RootElement/Entity. Should no longer be used for reading XML! Instead, set the base path by specifying it as input type on the subsequent transformation or linking tasks. | *empty string* |
| uriPattern | String | A URI pattern, e.g., http://namespace.org/{ID}, where {path} may contain relative paths to elements | *empty string* |
| outputTemplate | XmlCodeParameter | The output template used for writing XML. Must be valid XML. The generated entity is identified through a processing instruction of the form <?MyEntity?>. | <Root><?Entity?></Root> |
| streaming | boolean | Streaming allows for reading large XML files. | true |
| maxDepth | int | Maximum depth of written XML. This acts as a safe guard if a recursive structure is written. | 15 |
| zipFileRegex | String | If the input resource is a ZIP file, files inside the file are filtered via this regex. | ^(?!.*[\\/\\\\]\\..*$|^\\..*$).*\\.xml$ |

The identifier for this plugin is `xml`.

It can be found in the package `org.silkframework.plugins.dataset.xml`.

Typically, this dataset is used to transform an XML file to another format, e.g., to RDF. It can also be used to generate XML files.

##### Reading

When this dataset is used as an input for another task (e.g., a transformation task), the input type of the consuming task selects the path where the entities to be read are located.

Example:

    <Persons>
      <Person>
        <Name>John Doe</Name>
        <Year>1970</Year>
      </Person>
      <Person>
        <Name>Max Power</Name>
        <Year>1980</Year>
      </Person>
    </Persons>

A transformation for reading all persons of the above XML would set the input type to `/Person`.
The transformation iterates all entities matching the given input path.
In the above example the first entity to be read is:

    <Person>
      <Name>John Doe</Name>
      <Year>1970</Year>
    </Person>

All paths used in the consuming task are relative to this, e.g., the person name can be addressed with the path `/Name`.

Path examples:

- The empty path selects the root element.
- `/Person` selects all persons.
- `/Person[Year = "1970"]` selects all persons which are born in 1970.
- `/#id` Is a special syntax for generating an id for a selected element. It can be used in URI patterns for entities which do not provide an identifier. Examples: `http://example.org/{#id}` or `http://example.org/{/pathToEntity/#id}`.
- The wildcard * enumerates all direct children, e.g., `/Persons/*/Name`.
- The wildcard ** enumerates all direct and indirect children.
- The backslash can be used to navigate to the parent XML node, e.g., `\Persons/SomeHeader`.
- `#text` retrieves the text of the selected node.

##### Writing

When writing XML, all entities need to possess a unique URI. Writing multiple root entities with the same URI will result in multiple entries in the generated XML. If multiple nested entities with the same URI are written, only the last entity with a given URI will be written.

### Remote

#### JDBC endpoint

Connect to an existing JDBC endpoint.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| url | String | JDBC URL, must contain the database as parameter, i.g. with ;database=DBNAME or /database depending on the vendor. | *no default* |
| table | String | Table name. Can be empty if the read-strategy is not set to read the full table. If non-empty it has to contain at least an existing table. | *empty string* |
| sourceQuery | SqlCodeParameter | Source query (e.g. 'SELECT TOP 10 * FROM table WHERE x = true'. Warning: Uses Driver (mySql, HiveQL, MSSql, Postgres) specific syntax. Can be left empty when full tables are loaded. Note: Even if columns with spaces/special characters are named in the query, they need to be referred to URL-encoded in subsequent transformations. |  |
| groupBy | String | Comma separated list of attributes appearing in the outer SELECT clause that should be grouped by. The attributes are matched case-insensitive. All other attributes will be grouped via an aggregation function that depends on the supported DBMS, e.g. (JSON) array aggregation. | *empty string* |
| orderBy | String | Optional column to sort the result set. | *empty string* |
| limit | IntOptionParameter | Optional limit of returned records. This limit should be pushed to the source. No value implies that no limit will be applied. | 10 |
| queryStrategy | Enum | The strategy decides how the source system is queried. | access-complete-table |
| writeStrategy | Enum | If this dataset is written to, it can be selected if data is overwritten or appended.' | default |
| multipleValuesStrategy | Enum | How multiple values per entity property are written. | concatenateValuesStrategy |
| clearTableBeforeExecution | boolean | If set to true this will clear the specified table before executing a workflow that writes to it. | false |
| user | String | Username. Must be empty in some cases e.g. if secret key and client id are used. If non-empty this will also overwrite any value set in the JDBC URL string. | *empty string* |
| password | PasswordParameter | Password. Can be empty in some cases e.g. secret key and client id are used or if it is just an empty string. The password must be set here and cannot be set in the JDBC URL connection string. |  |
| tokenEndpoint | String | URL for retrieving tokens, when using MS SQL Active Directory token based authentication. Can be found in the Azure AD Admin Center under OAuth2 endpoint or cab be constructed with the general endpoint URL combined with the tenant id and the suffix /outh/v2/authortized. | *empty string* |
| spnName | String | Service Principal Name identifying the resource. Usually a static URL like https://database.windows.net. | *empty string* |
| clientId | String | Client id or application id. Client id used for MS SQL token based authentication. String seperated by - char. | *empty string* |
| clientSecret | PasswordParameter | Client secret. Client secret used for MS SQL token based authentication. Can be generated in Azure AD admin center. |  |
| restriction | String | An SQL WHERE clause to filter the records to be retrieved. | *empty string* |
| retries | int | Optional number of retries per query | 0 |
| pause | int | Optional pause between queries in ms. | 2000 |
| charset | String | The source internal encoding, e.g., UTF-8, ISO-8859-1 | UTF-8 |
| forceSparkExecution | boolean | If set to true, Spark will be used for querying the database, even if the local execution manager is configured. | false |

The identifier for this plugin is `Jdbc`.

It can be found in the package `com.eccenca.di.sql.jdbc`.

_General usage_

The JDBC dataset supports connections to Hive, Microsoft SQL Server, MySQL, MariaDB, SnowFlake, Oracle Database, DB2 and PostgreSQL databases.
A login, password and JDBC URL need to be provided.
This dataset supports queries or simply schema and table names to define what to retrieve from a source DB.
When the dataset is used as a sink, queries are ignored and only schema and table parameters are used.
If the dataset is used as a sink for a hierarchical mapping, it behaves similarly to the SqlEndpoint: One table is created per entity type.

The names of the written tables are generated as follows:

- The table name of the root mapping is defined by the table parameter of the dataset.
  If the table name is empty, a name is generated from the first type of the mapping.
  Special characters are removed and the name is truncated to a maximum of 128 characters.
- For each object mapping, the table name is generated from its type.

_JDBC Connection Strings/URLs_

Most of the dataset parameters are passed directly to the driver.
Please make sure that you use the correct syntax for each DBMS, otherwise you may get unintuitive errors.

Here are templates for supported database systems:
```
oracle (external driver needed):
jdbc:oracle:thin:@{host}[:{port}]/{database}

postgres (integrated):
jdbc:postgresql://{host}[:{port}]/[{database}]

MySQL/MariaDB (integrated):
jdbc:{mariadb}://{host}[:{port}]/[{database}]

SnowSQL (external driver needed):
jdbc:snowflake://{AWSAccount}.{AWS region}.snowflakecomputing.com?db={database}&schema={schema}

MSSqlServer (integrated):
jdbc:sqlserver://{host}[:{port}];databaseName={database}

DB2 (external driver needed):
jdbc:db2//{host}[:{port}]/{database}

Trino (external driver needed)
jdbc:trino//{host}:8080/catalog/schema
```

_Read and write strategies_

There are multiple read and write strategies which can be selected depending on the purpose of the dataset in a workflow.

Read strategies decide how the database is queried:

- **full-table**: Queries or wraps a complete table.
  Only the DB schema and table name need to be set.
- **query**: The given source query is passed to the database.
  The table name is not necessary in this case but a valid query in the SQL-dialect of the source database system must be provided.

Write strategies decide how a new table is written:

- **default**: An error will occur if the table exists.
  If not a new one will be created.
- **overwrite**: The old table will be removed and a new one will be created.
- **append**: Data will be appended to the existing table.
  The schema of the data written has to be the same as the existing table schema.

_Optimized Writing_

Usually specific database systems have custom commands for loading large amounts of data, e.g. from a CSV file into a database table.
For some DBMS and specific JDBC dataset configurations we support these optimized methods of loading data.

Supported DBMS:

- MySQL and MariaDB (full support for versions 8.0.19+ and 10.4+, resp.):
  - if older DBMS versions are used some dataset options like 'groupBy' might not be supported but equivalent queries will
  - the same is true when older driver jars then the one provided by eccenca are used
  - both use the MariaDB JDBC driver
  - uses `LOAD DATA LOCAL INFILE` internally
  - only applies when appending data to an existing table and having `Force Spark Execution` disabled
  - Both the server parameter `local_infile` and the client parameter `allowLoadLocalInfile` must be enabled, e.g. by adding `allowLoadLocalInfile=true` to the JDBC URL.
    For MySQL starting with version 8 the `local_infile` parameter is by default disabled!
  - If during writing to a MySQL/MariaDB a `[…] You have an error in your SQL syntax […]` error is encountered make sure ANSIquotes are used.
    `sql_mode=ANSI_QUOTES` can be set via a URL parameter to the JDBC connection string like:

    ```sh
    # MySQL
    jdbc:mysql://<host>:<port, eg. 3306>/<database>?sessionVariables=sql_mode=ANSI_QUOTES

    # MariaDB
    jdbc:mariadb://<host>:<port, eg. 3306>/<database>?sessionVariables=sql_mode=ANSI_QUOTES
    ```

_Registering JDBC drivers_

More 3rd party databases are supported via adding their JDBC drivers to the classpath of Data Integration.
Drivers are usually provided by the database manufactures.
If 32 bit and 64 bit versions are provided the latter is usually needed and should aways equal the bit-level of the JVM.
To make sure that the drivers are loaded correctly, their class name (in case are jar contains multiple drivers) and location in the file system can be set with the `spark.sql.options.jdbc` option in the `dataintegration.conf` configuration file.

An example for adding both the DB2 and MySQL drivers to the Data Integration configuration file `spark.sql.options.*` section:

```raml
spark.sql.options {
  …

  # List of database identifiers to specify user provided JDBC drivers. The second part of the protocol of a JDBC URI (e.g. db2 from
  # jdbc:db2://host:port)  is used to specify the driver. For each protocol on the list a jar classname and optional download
  # location can be provided.
  jdbc.drivers = "db2,mysql"

  # Some database systems use licenses that are to loose or restrictive for us to ship the drivers. Therefore a path
  # to a jar file containing the driver and the name of driver can be specified here.
  jdbc.db2.jar = "/home/user/Jars/db2jcc-db2jcc4.jar"
  jdbc.mysql.jar = "/home/user/drivers/mysql.jar"

  # Name of the actual driver class for each db
  jdbc.db2.name = "com.ibm.db2.jcc.DB2Driver"
  jdbc.mysql.name = "com.mysql.jdbc.Driver"
}
```

_Driver Priority_

In general it will not work to upgrade a JDBC driver by providing an external driver for a database that is already packaged with eccenca Dataintegration.

The driver delivered with eccenca Dataintegration will be prefered. Driver names (configured via e.g. `spark.sql.options.jdbc.drivers = "mssql"`) will be ignored if JDBC URLs starting with, in this example `jdbc:mssql...` , are already supported in the dataset.

_Recommended DBMS versions_

- **Microsoft SQL Server 2017**: Older versions might work, but do not support the `groupBy` parameter.
- **PostgreSQL 9.5**: The `groupBy` parameter needs at least version 8.4.
- **MySQL v8.0.19**: Older versions do not support the `groupBy` parameter.
- **DB2 v11.5.x**: The `groupBy` feature needs at least version 9.7 to function.
- **Oracle 12.2.x**: The `groupBy` feature does not work for versions prior to 11g Release 2.

These limitations are the same for JDBC drivers that are older than the fully supported databases.
Queries can achieve a similar outcome if `groupBy` is not supported.

#### Snowflake JDBC endpoint

Connect to Snowflake JDBC endpoint.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| connection | PluginObjectParameter | Connection parameters |  |
| read | PluginObjectParameter | Parameters related to reading from the database. |  |
| write | PluginObjectParameter | Parameters related to writing to the database. |  |
| queryExecution | PluginObjectParameter | Query execution parameters. |  |

The identifier for this plugin is `SnowflakeJdbc`.

It can be found in the package `com.eccenca.di.sql.jdbc.databases.snowflake`.

This dataset supports connections to the Snowflake JDBC endpoint.

##### <a id="parameter_doc_connection-host">Account URL hostname</a>

The supplied account URL hostname needs to contain the account identifier. Refer to the Snowflake documentation on [account identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier) for details.

##### Reading

Either a table or a queries can be specified to retrieve data from Snowflake.

Read strategies decide how the database is queried:

- **full-table**: Queries or wraps a complete table.
  Only the table name need to be set.
- **query**: The given source query is passed to the database.
  The table name is not necessary in this case but a valid query must be provided.

##### Writing

When the dataset is used as a sink, queries are ignored and only schema and table parameters are used.
If the dataset is used as a sink for a hierarchical mapping, one table is created per entity type.

Write strategies decide how a new table is written:

- **default**: An error will occur if the table exists.
  If not a new one will be created.
- **overwrite**: The old table will be removed and a new one will be created.
- **append**: Data will be appended to the existing table.
  The schema of the data written has to be the same as the existing table schema.

The names of the written tables are generated as follows:

- The table name of the root mapping is defined by the table parameter of the dataset.
  If the table name is empty, a name is generated from the first type of the mapping.
  Special characters are removed and the name is truncated to a maximum of 128 characters.
- For each object mapping, the table name is generated from its type.

#### Excel (Google Drive)

Read data from a remote Google Spreadsheet.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| url | String | Link to the document ('share with anyone having a link' must be enabled, URL parameters will be removed and corrected automatically). | *no default* |
| streaming | boolean | Streaming enables reading and writing large Excels files. Warning: Be careful to disable streaming for large datasets (> 10MB), because of high memory consumption. | true |
| invalidateCacheAfter | Duration | Duration until file based cache is invalidated. | PT5M |
| linesToSkip | int | The number of lines to skip in the beginning when reading files. | 0 |

The identifier for this plugin is `googlespreadsheet`.

It can be found in the package `com.eccenca.di.gdrive`.


The dataset needs the document id of a "share via url" sheet on Google Drive as input.
It will automatically correct the URL and add the "export as xlsx" option to a new URL
that will be used to download an Excel Spreadsheet.
The download will be cached and treated the same way as an xlsx file in the Excel Dataset.

##### Caching

The advanced parameter `invalidateCacheAfter` allows the user to specify a duration of the file cache
after which it is refreshed.
A file based cache is created to avoid CAPTCHAs. During the caching and validation of the URL
access occurs with random wait times between 1 and 5 seconds.
The cache is invalidated after 5 minutes by default.

#### Neo4j

Neo4j graph

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| uri | String | The URL to the Neo4j instance | bolt://localhost:7687 |
| user | String | The Neo4j username for basic authentication. | neo4j |
| password | PasswordParameter | The Neo4j password for basic authentication. | PASSWORD_PARAMETER:UjbuVU/D0L+9QI2jGjfKiQ== |
| database | String | Database (leave empty for default) | *empty string* |
| nodeLabel | String | Neo4j label for all entities to be covered by this dataset. When reading, all nodes with this label will be read. When writing, this label will be added to all generated nodes. If the dataset is cleared, only nodes with this label will be deleted. | Any |
| clearBeforeExecution | boolean | If set to true, all nodes with the specified label will be removed, before executing a workflow that writes to this graph. | true |

The identifier for this plugin is `neo4j`.

It can be found in the package `com.eccenca.di.plugins.neo4j`.


Supports reading and writing Neo4j graphs. The following sections outline how graphs are generated and read back.

For more information about Neo4j, please refer to the [Neo4j documentation](https://neo4j.com/docs/).

##### Nodes

For each entity that is written to a Neo4j dataset, a _node_ will be created.
A property `uri` will be added to each generated node, which holds the URI of the original entity.
In applications, the URI property should be used instead of the node identifiers, which are auto-generated in Neo4j and do not represent stable URIs.

When reading nodes, the entity URIs will be generated based on that property.
At the moment, it's not supported to read nodes that do not provide a `uri` property.

##### Labels

_Labels_ in Neo4j are used to group nodes into sets where all nodes that have a certain _label_ belongs to the same set.
Neo4j _labels_ are comparable with _classes_ in RDF (not to be confused with labels in RDF).

When writing entities to the Neo4j dataset, the following _labels_ will be added to each generated node:

- For each entity _type_ (such as the _type_ set in a mapping), a _label_ will be added to the node in Neo4j.
  Since _types_ in eccenca DataIntegration are usually URIs, they will be converted according to the rules further down.
- The _label_ as configured by the _label_ parameter on the Neo4j dataset itself.
  This is typically used to identify all entities that have been written by a certain Neo4j dataset specification in the project.
  For instance, if two Neo4j dataset specifications are added to a project - both writing to the same Neo4j database - different labels can be set to distinguish both sets of entities.
  In that respect it may be used to model a similar concept as _graphs_ in RDF.

##### Relationships

A relationship connects two nodes in Neo4j.
Hierarchical mappings will generate relationships for all object mappings.

Relationships can be addressed with property paths in mappings.
At the moment, only paths of length 1 are supported, i.e., it's not possible to use non-property paths.

##### Handling of URIs

In eccenca DataIntegration, URIs are typically used to uniquely identify classes and properties.
While URIs are central in RDF, Neo4j does allow arbitrary names and does not have any special support for URIs.

When generating Neo4j labels, properties and relationships, URIs will be shortened according to the following rules.
- If a registered project prefix matches a URI, a name `{prefixName}_{localPart}` will be generated. For instance, `http://xmlns.com/foaf/0.1/name` will become `foaf_name`.
  Note that underscores (`_`) are used instead of colons (`:`) to separate the namespace and the local name.
  The reason is that colons are reserved in the Cypher query language and some tools don't escape properly and fail on databases that use colons in names.
- If no project prefix matches a URI, the URI will be used verbatim. This will look ugly in Neo4j tools, so generally it's recommended to define prefixes for all used namespaces.

When reading generated entities, the URIs of the classes and properties will be reconstructed based on the prefix table of the project. If the prefixes change between writing and reading, different URIs will be generated.

##### RDF vs. Neo4j terminology

Neo4j uses a different terminology than RDF or description logic.
For users familiar with RDF, the following table shows the correspondent terms for some central concepts.
This is meant to help understanding and does not aim to provide a precise mapping as there are semantic differences between Neo4j and RDF.

| RDF | Neo4j |
| --- |--- |
| resource     | node |
| class      | label      |
| datatype property      | property      |
| object property      | relationship |
| graph | Do not exist in Neo4j, but labels can be used to mimic graphs.    |

#### Excel (OneDrive, Office365)

Read data from a remote onedrive or Office365 Spreadsheet.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| url | String | Link to the document ('share with anyone having a link' must be enabled). | *no default* |
| streaming | boolean | Streaming enables reading and writing large Excels files. Warning: Be careful to disable streaming for large datasets (> 10MB), because of high memory consumption. | true |
| invalidateCacheAfter | Duration | Duration until file based cache is invalidated. | PT5M |
| linesToSkip | int | The number of lines to skip in the beginning when reading files. | 0 |

The identifier for this plugin is `office365preadsheet`.

It can be found in the package `com.eccenca.di.office365`.

The dataset needs the URL of a "share via link" sheet on Office 365/OneDrive as input.
It will automatically construct a direct download URL, cache the download file handle it like
an XLSX file in the Excel Dataset.

##### Notes

There are 2 types of URLs that can be shared:
Onedrive links look like `https://1drv.ms/x/s!AucULvzmJ-dsdfsfgaIcyWP_XY_G4w?e=yx65uu`

Onedrive (based one sharepoint, for businesses) links look like `https://eccencagmbh-my.sharepoint.com/:x:/g/personal/person_eccenca_com/EdEMTEw1dclHiEZXyvy8P4YBit8wSyGsiwU5Kt__sQOZzw`

The first type should always work is not recommended for this dataset. The second type requires to set up an application in Microsoft EntraID (formerly Azure Active Directory).
EntraID: https://docs.microsoft.com/azure/active-directory/develop/v2-overview
Instructions and examples can be found here:
https://github.com/Azure-Samples/ms-identity-msal-java-samples/tree/main/3-java-servlet-web-app/1-Authentication/sign-in

After following the steps access to sharepoint/onedrive for business can be setup in the application.conf file for eccenca DataIntegration.

Example:

```conf
com.eccenca.di.office365 = {
    authority = "https://login.microsoftonline.com/a0907dd1-f981-4c98-a8b9-1deb27bcf2cc/"
    clientId = "4d14959d-3c62-4f90-a072-a96ca4b3fa9f"
    secret = "Ceb8Q~QkMMV7TBK-ggB3nh22nUnqoDB1KTmkjj"
    scope = "https://graph.microsoft.com/.default"
    tenantId = "a0907dd1-f981-4c98-a8b9-1deb27bcf2cc"
}
```

##### Caching

The advanced parameter `invalidateCacheAfter` allows the user to specify a duration of the file cache
after which it is refreshed.
A file based cache is created to avoid CAPTCHAs. During the caching and validation of the URL
access occurs with random wait times between 1 and 5 seconds.
The cache is invalidated after 5 minutes by default.

#### SPARQL endpoint

Connect to an existing SPARQL endpoint.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| endpointURI | String | The URI of the SPARQL endpoint, e.g., http://dbpedia.org/sparql | *no default* |
| login | String | Login required for authentication | *null* |
| password | PasswordParameter | Password required for authentication |  |
| graph | String | Only retrieve entities from a specific graph | *null* |
| pageSize | int | The number of solutions to be retrieved per SPARQL query. | 1000 |
| entityList | MultilineStringParameter | A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace. |  |
| pauseTime | int | The number of milliseconds to wait between subsequent query | 0 |
| retryCount | int | The number of retries if a query fails | 3 |
| retryPause | int | The number of milliseconds to wait until a failed query is retried. | 1000 |
| queryParameters | String | Additional parameters to be appended to every request e.g. &soft-limit=1 | *empty string* |
| strategy | Enum | The strategy use for retrieving entities: simple: Retrieve all entities using a single query; subQuery: Use a single query, but wrap it for improving the performance on Virtuoso; parallel: Use a separate Query for each entity property. | parallel |
| useOrderBy | boolean | Include useOrderBy in queries to enforce correct order of values. | true |
| clearGraphBeforeExecution | boolean | If set to true this will clear the specified graph before executing a workflow that writes to it. | false |
| sparqlTimeout | int | SPARQL query timeout (select/update) in milliseconds. A value of zero means that the timeout configured via property is used (e.g. configured via silk.remoteSparqlEndpoint.defaults.read.timeout.ms). To overwrite the configured value specify a value greater than zero. | 0 |

The identifier for this plugin is `sparqlEndpoint`.

It can be found in the package `org.silkframework.plugins.dataset.rdf.datasets`.



### Uncategorized

#### Internal dataset (single graph)

Dataset for storing entities between workflow steps. This variant does use the same graph for all internal datasets in a workflow. The underlying dataset type can be configured using the `dataset.internal.*` configuration parameters.

This plugin does not require any parameters.
The identifier for this plugin is `LocalInternalDataset`.

It can be found in the package `org.silkframework.execution.local`.



#### Binary file

Reads and writes binary files. A typical use-case for this dataset is to process PDF documents or images.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | The file to read or write. | *no default* |
| zipFileRegex | String | If the file is a ZIP file, read files are filtered via this regex. If empty, the zip itself will be returned to readers. | .* |

The identifier for this plugin is `binaryFile`.

It can be found in the package `org.silkframework.plugins.dataset`.

Reads and writes binary files. A typical use-case for this dataset is to process PDF documents or images using workflow operators that accept or output files. If an operator reads from this dataset that does not support files directly (such as transformation or linking tasks), it will only receive the file metadata, which includes the file path.

##### ZIP files

This dataset can be used to compress/decompress ZIP files. If a ZIP file is configured, the behaviour is as follows:
- Writing a ZIP file to this dataset will overwrite the configured ZIP file.
- Writing one or many non-ZIP files will overwrite the dataset file with a ZIP that contains all written files.
- When reading files, the dataset will return all files inside the ZIP that match the configured regex. If the regex is empty, the ZIP file itself will be returned.

##### Replaceable datasets

It can be used with the `replacable input` flag to replace the configured file in a workflow execution request.
Same for the `replacable output` flag, which will return the file content as a result of a workflow execution request.

##### MIME type

The generic MIME type for files of this dataset is `application/octet-stream`.

#### Text

Reads and writes plain text files.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | WritableResource | The plain text file. May also be a zip archive containing multiple text files. | *no default* |
| charset | String | The file encoding, e.g., UTF-8, UTF-8-BOM, ISO-8859-1 | UTF-8 |
| typeName | String | A type name that represents this file. | document |
| property | String | The single property that holds the text. | text |
| zipFileRegex | String | If the input resource is a ZIP file, files inside the file are filtered via this regex. | .* |

The identifier for this plugin is `text`.

It can be found in the package `org.silkframework.plugins.dataset.text`.

Reads and writes plain text files.

##### Writing

All values of each entity will be written as plain text. Multiple values per entity are separated by spaces. Each entity will be written to a new line.

##### Reading

The entire text will be read as a single entity with a single property. Note that even if multiple entities have been written to this dataset before, those would still be read back as a single entity. The default type is `document`, the default path is `text`. Both values can be configured in the advanced section.

## Distance Measures

The following distance measures are available:

### Characterbased

Character-based distance measures compare strings on the character level. They are well suited for handling typographical errors.

#### Is substring

Checks if a source value is a substring of a target value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| reverse | boolean | Reverse source and target inputs | false |

The identifier for this plugin is `isSubstring`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Jaro distance

Matches strings based on the Jaro distance metric.

This plugin does not require any parameters.
The identifier for this plugin is `jaro`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.

The Jaro distance measure calculates the similarity between two strings based on the number and order of common characters, the number of transpositions, and the length of the strings. The Jaro distance is 0 for a perfect match and 1 if there is no similarity between the given strings.

For more information, please refer to: [https://en.wikipedia.org/wiki/Jaro–Winkler_distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance).

##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Jaro-Winkler distance

Matches strings based on the Jaro-Winkler distance measure.

This plugin does not require any parameters.
The identifier for this plugin is `jaroWinkler`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.

The Jaro-Winkler distance measure is a variation of the Jaro distance metric. It takes into account the prefixes of the strings being compared and assigns higher weights to matching prefixes.

For more information, please refer to: [https://en.wikipedia.org/wiki/Jaro–Winkler_distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance).

##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Normalized Levenshtein distance

Normalized Levenshtein distance. Divides the edit distance by the length of the longer string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| qGramsSize | int | The size of the q-grams to be indexed. Setting this to zero will disable indexing. | 2 |
| minChar | char | The minimum character that is used for indexing | 0 |
| maxChar | char | The maximum character that is used for indexing | z |

The identifier for this plugin is `levenshtein`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns 0 for equal strings:

* Input values:
  - Source: `[John]`
  - Target: `[John]`

* Returns: → `0.0`


---
##### Returns 1/4 if two strings of length 4 differ by one edit operation:

* Input values:
  - Source: `[John]`
  - Target: `[Jxhn]`

* Returns: → `0.25`


---
##### Normalizes the edit distance by the length of the longer string:

* Input values:
  - Source: `[John]`
  - Target: `[Jhn]`

* Returns: → `0.25`


---
##### Returns the maximum distance of 1 for completely different strings:

* Input values:
  - Source: `[John]`
  - Target: `[Clara]`

* Returns: → `1.0`

#### Levenshtein distance

Levenshtein distance. Returns a distance value between zero and the size of the string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| qGramsSize | int | The size of the q-grams to be indexed. Setting this to zero will disable indexing. | 2 |
| minChar | char | The minimum character that is used for indexing | 0 |
| maxChar | char | The maximum character that is used for indexing | z |

The identifier for this plugin is `levenshteinDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns 0 for equal strings:

* Input values:
  - Source: `[John]`
  - Target: `[John]`

* Returns: → `0.0`


---
##### Returns 1 for strings that differ by one edit operation:

* Input values:
  - Source: `[John]`
  - Target: `[Jxhn]`

* Returns: → `1.0`


---
##### Returns 3 for strings that differ by three edit operations:

* Input values:
  - Source: `[Saturday]`
  - Target: `[Sunday]`

* Returns: → `3.0`

#### qGrams

String similarity based on q-grams (by default q=2).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| q | int | No description | 2 |
| minChar | char | The minimum character that is used for indexing | 0 |
| maxChar | char | The maximum character that is used for indexing | z |

The identifier for this plugin is `qGrams`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns 0.0 if the input strings are equal:

* Input values:
  - Source: `[abcd]`
  - Target: `[abcd]`

* Returns: → `0.0`


---
##### Returns 1.0 if the input strings do not share a single q-gram:

* Input values:
  - Source: `[abcd]`
  - Target: `[dcba]`

* Returns: → `1.0`


---
##### Returns 1 minus the matching q-grams divided by the total number of q-grams. Generated q-grams in this example: (#a, ab, b#) and (#a, ac, c#):

* Input values:
  - Source: `[ab]`
  - Target: `[ac]`

* Returns: → `0.8`

#### Starts with

Returns success if the first string starts with the second string, failure otherwise.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| reverse | boolean | Reverse source and target values | false |
| minLength | int | The minimum length of the string being contained. | 2 |
| maxLength | int | The potential maximum length of the strings that must match. If the max length is greater  than the length of the string to match, the full string must match. | 2147483647 |

The identifier for this plugin is `startsWith`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Substring comparison

Return 0 to 1 for strong similarity to weak similarity. Based on the paper: Stoilos, Giorgos, Giorgos Stamou, and Stefanos Kollias. "A string metric for ontology alignment." The Semantic Web-ISWC 2005. Springer Berlin Heidelberg, 2005. 624-637.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| granularity | String | The minimum length of a possible substring match. | 3 |

The identifier for this plugin is `substringDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.characterbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

### Equality

#### Constant similarity value

Always returns a constant similarity value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| value | double | No description | 1.0 |

The identifier for this plugin is `constantDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

#### String equality

Checks for equality of the string representation of the given values. Returns success if string values are equal, failure otherwise. For a numeric comparison of values use the 'Numeric Equality' comparator.

This plugin does not require any parameters.
The identifier for this plugin is `equality`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns distance 0, if at least one value matches:

* Input values:
  - Source: `[max, helmut]`
  - Target: `[max]`

* Returns: → `0.0`


---
##### Returns distance 1, if no value matches:

* Input values:
  - Source: `[max, helmut]`
  - Target: `[john]`

* Returns: → `1.0`

#### Greater than

Checks if the source value is greater than the target value. If both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| orEqual | boolean | Accept equal values | false |
| order | Enum | Per default, if both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used. Choose a more specific order for improved performance. | Autodetect |
| reverse | boolean | Reverse source and target inputs | false |

The identifier for this plugin is `greaterThan`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Inequality

Returns success if values are not equal, failure otherwise.

This plugin does not require any parameters.
The identifier for this plugin is `inequality`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns distance 0, if the values are different:

* Input values:
  - Source: `[max]`
  - Target: `[john]`

* Returns: → `0.0`


---
##### Returns distance 1, if the values are equal:

* Input values:
  - Source: `[max]`
  - Target: `[max]`

* Returns: → `1.0`


---
##### If multiple values are provided, returns 0, if at least one value does not match:

* Input values:
  - Source: `[max, helmut]`
  - Target: `[max]`

* Returns: → `0.0`


---
##### If multiple values are provided, returns 1, if all value match:

* Input values:
  - Source: `[max, max]`
  - Target: `[max, max]`

* Returns: → `1.0`

#### Lower than

Checks if the source value is lower than the target value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| orEqual | boolean | Accept equal values | false |
| order | Enum | Per default, if both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used. Choose a more specific order for improved performance. | Autodetect |
| reverse | boolean | Reverse source and target inputs | false |

The identifier for this plugin is `lowerThan`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Numeric equality

Compares values numerically instead of their string representation as the 'String Equality' operator does.
Allows to set the needed precision of the comparison. A value of 0.0 means that the values must represent exactly the same
(floating point) value, values higher than that allow for a margin of tolerance.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| precision | double | The range of tolerance in floating point number comparisons. Must be 0 or a non-negative number smaller than 1. | 0.0 |

The identifier for this plugin is `numericEquality`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns 0 for equal numbers:

* Input values:
  - Source: `[4.2]`
  - Target: `[4.2]`

* Returns: → `0.0`


---
##### Returns 1 if at least one value is not a number:

* Input values:
  - Source: `[1]`
  - Target: `[one]`

* Returns: → `1.0`


---
##### Returns 0 for numbers within the configured precision:

* Parameters
  * *precision*: `0.1`

* Input values:
  - Source: `[1.3]`
  - Target: `[1.35]`

* Returns: → `0.0`


---
##### Returns 1 for numbers outside the configured precision:

* Parameters
  * *precision*: `0.1`

* Input values:
  - Source: `[1.3]`
  - Target: `[1.5]`

* Returns: → `1.0`

#### Relaxed equality

Return success if strings are equal, failure otherwise. Lower/upper case and differences like ö/o, n/ñ, c/ç etc. are treated as equal.

This plugin does not require any parameters.
The identifier for this plugin is `relaxedEquality`.

It can be found in the package `org.silkframework.rule.plugins.distance.equality`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

### Language

#### CJK reading distance

CJK Reading Distance.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| minChar | char | No description | 0 |
| maxChar | char | No description | z |

The identifier for this plugin is `cjkReadingDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.asian`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Korean phoneme distance

Korean phoneme distance.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| minChar | char | No description | 0 |
| maxChar | char | No description | z |

The identifier for this plugin is `koreanPhonemeDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.asian`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Korean translit distance

Transliterated Korean distance.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| minChar | char | No description | 0 |
| maxChar | char | No description | z |

The identifier for this plugin is `koreanTranslitDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.asian`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

### Numeric

#### Compare physical quantities

Computes the distance between two physical quantities.
The distance is normalized to the SI base unit of the dimension.
For instance for lengths, the distance will be in metres.
Comparing incompatible units will yield a validation error.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| numberFormat | String | The IETF BCP 47 language tag, e.g., 'en'. | en |

The identifier for this plugin is `PhysicalQuantitiesDistance`.

It can be found in the package `com.eccenca.di.measure`.

SI units and common derived units are supported. The following section lists all supported units. By default, all quantities are normalized to their base unit. For instance, lengths will be normalized to metres.
##### Supported units

##### Time

Time is expressed in seconds (symbol: `s`).
The following alternative symbols are supported:
* `mo_s`: day*29.53059
* `mo_g`: year/12.0
* `a`: day*365.25
* `min`: min
* `a_g`: year
* `mo`: (day*365.25)/12.0
* `mo_j`: (day*365.25)/12.0
* `a_j`: day*365.25
* `h`: h
* `a_t`: day*365.24219
* `d`: day


##### Length

Length is expressed in metres (symbol: `m`).
The following alternative symbols are supported:
* `in`: c(cm*254.0)
* `nmi`: m*1852.0
* `Ao`: dnm
* `mil`: m(c(cm*254.0))
* `yd`: ((c(cm*254.0))*12.0)*3.0
* `AU`: m*1.49597871E11
* `ft`: (c(cm*254.0))*12.0
* `pc`: m*3.085678E16
* `fth`: ((c(cm*254.0))*12.0)*6.0
* `mi`: ((c(cm*254.0))*12.0)*5280.0
* `hd`: (c(cm*254.0))*4.0


##### Mass

Mass is expressed in kilograms (symbol: `kg`).
The following alternative symbols are supported:
* `lb`: lb
* `ston`: hlb*20.0
* `t`: Mg
* `stone`: lb*14.0
* `u`: AMU
* `gr`: (mg*6479891.0)/100000.0
* `lcwt`: lb*112.0
* `oz`: oz
* `g`: g
* `scwt`: hlb
* `dr`: oz/16.0
* `lton`: (lb*112.0)*20.0


##### Electric current

Electric current is expressed in amperes (symbol: `A`).
The following alternative symbols are supported:
* `Bi`: daA
* `Gb`: cm·(A/m)*250.0/[one?]


##### Temperature

Temperature is expressed in kelvins (symbol: `K`).
The following alternative symbols are supported:
* `Cel`: ℃


##### Amount of substance

Amount of substance is expressed in moles (symbol: `mol`).

##### Luminous intensity

Luminous intensity is expressed in candelas (symbol: `cd`).

##### Area

Area is expressed in square metres (symbol: `m²`).
The following alternative symbols are supported:
* `m2`: m²
* `ar`: hm²
* `syd`: ((c(cm*254.0))*12.0)*3.0²
* `cml`: [one?]/4.0·m(c(cm*254.0))²
* `b`: hfm²
* `sft`: (c(cm*254.0))*12.0²
* `sin`: c(cm*254.0)²


##### Volume

Volume is expressed in cubic metres (symbol: `㎥`).
The following alternative symbols are supported:
* `st`: [㎥?]
* `bf`: (c(cm*254.0)³)*144.0
* `cyd`: ((c(cm*254.0))*12.0)*3.0³
* `cr`: ((c(cm*254.0))*12.0³)*128.0
* `L`: L
* `l`: l
* `cin`: c(cm*254.0)³
* `cft`: (c(cm*254.0))*12.0³
* `m3`: ㎥


##### Energy

Energy is expressed in joules (symbol: `J`).
The following alternative symbols are supported:
* `cal_IT`: (J*41868.0)/10000.0
* `eV`: J*1.602176487E-19
* `cal_m`: (J*419002.0)/100000.0
* `cal`: m(J*4184.0)
* `cal_th`: m(J*4184.0)


##### Angle

Angle is expressed in radians (symbol: `rad`).
The following alternative symbols are supported:
* `circ`: [one?]·rad*2.0
* `gon`: ([one?]·rad/180.0)*0.9
* `deg`: [one?]·rad/180.0
* `'`: ([one?]·rad/180.0)/60.0
* `''`: (([one?]·rad/180.0)/60.0)/60.0


##### Others

- `1/m`, derived units: `Ky`: c(1/m)
- `kg/(m·s)`, derived units: `P`: g/(s·cm)
- `bit/s`, derived units: `Bd`: bit/s
- `bit`, derived units: `By`: bit*8.0
- `Sv`
- `N`
- `Ω`, derived units: `Ohm`: Ω
- `T`, derived units: `G`: T/10000.0
- `sr`, derived units: `sph`: [one?]·sr*4.0
- `F`
- `C/kg`, derived units: `R`: (C/kg)*2.58E-4
- `cd/m²`, derived units: `sb`: cd/cm², `Lmb`: cd/([one?]·cm²)
- `Pa`, derived units: `bar`: Pa*100000.0, `atm`: Pa*101325.0
- `kg/(m·s²)`, derived units: `att`: k(g·(m/s²)*9.80665)/cm²
- `m²/s`, derived units: `St`: cm²/s
- `A/m`, derived units: `Oe`: (A/m)*250.0/[one?]
- `kg·m²/s²`, derived units: `erg`: cm²·g/s²
- `kg/m³`, derived units: `g%`: g/dl
- `mho`
- `V`
- `lx`, derived units: `ph`: lx/10000.0
- `m/s²`, derived units: `Gal`: cm/s², `m/s2`: m/s²
- `m/s`, derived units: `kn`: m*1852.0/h
- `m·kg/s²`, derived units: `gf`: g·(m/s²)*9.80665, `lbf`: lb·(m/s²)*9.80665, `dyn`: cm·g/s²
- `m²/s²`, derived units: `RAD`: cm²·g/(s²·hg), `REM`: cm²·g/(s²·hg)
- `C`
- `Gy`
- `Hz`
- `H`
- `lm`
- `W`
- `Wb`, derived units: `Mx`: Wb/1.0E8
- `Bq`, derived units: `Ci`: Bq*3.7E10
- `S`


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Convert SI unit prefixes:

* Input values:
  - Source: `[1 km]`
  - Target: `[500 m]`

* Returns: → `500.0`


---
##### Convert imperial and metric values:

* Input values:
  - Source: `[1 km]`
  - Target: `[1 mi]`

* Returns: → `609.344`


---
##### Validate if the compared units of measurement are compatible:

* Input values:
  - Source: `[1 km]`
  - Target: `[1 kg]`

* Returns: → `NaN`

#### Date

The distance in days between two dates ('YYYY-MM-DD' format).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| requireMonthAndDay | boolean | If true, no distance value will be generated if months or days are missing (e.g., 2019-11). If false, missing month or day fields will default to 1. | false |

The identifier for this plugin is `date`.

It can be found in the package `org.silkframework.rule.plugins.distance.numeric`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns 0 if both dates are equal:

* Input values:
  - Source: `[2003-03-01]`
  - Target: `[2003-03-01]`

* Returns: → `0.0`


---
##### Returns 1 if both dates are one day apart:

* Input values:
  - Source: `[2003-03-01]`
  - Target: `[2003-03-02]`

* Returns: → `1.0`


---
##### Returns the number of days if both dates are one month apart:

* Input values:
  - Source: `[2003-03-01]`
  - Target: `[2003-04-01]`

* Returns: → `31.0`


---
##### Returns the number of days if both dates are one year apart:

* Input values:
  - Source: `[2018-03-01]`
  - Target: `[2019-03-01]`

* Returns: → `365.0`


---
##### Time of day is ignored:

* Input values:
  - Source: `[2003-03-01]`
  - Target: `[2003-03-01T06:00:00]`

* Returns: → `0.0`


---
##### Missing days are set to 1 by default:

* Input values:
  - Source: `[2003-01]`
  - Target: `[2003-01-01]`

* Returns: → `0.0`


---
##### Missing months are set to 1 by default:

* Input values:
  - Source: `[2003]`
  - Target: `[2003-01-01]`

* Returns: → `0.0`


---
##### Missing months and days are set to 1 by default:

* Input values:
  - Source: `[2018]`
  - Target: `[2019]`

* Returns: → `365.0`


---
##### If 'requireMonthAndDay' is set, dates without a day and month will not match:

* Parameters
  * *requireMonthAndDay*: `true`

* Input values:
  - Source: `[2003]`
  - Target: `[2003-03-01]`

* Returns: → `Infinity`


---
##### If 'requireMonthAndDay' is set, dates without a day will not match:

* Parameters
  * *requireMonthAndDay*: `true`

* Input values:
  - Source: `[2003-12]`
  - Target: `[2003-03-01]`

* Returns: → `Infinity`

#### DateTime

Distance between two date time values (xsd:dateTime format) in seconds.

This plugin does not require any parameters.
The identifier for this plugin is `dateTime`.

It can be found in the package `org.silkframework.rule.plugins.distance.numeric`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Inside numeric interval

Checks if a number is contained inside a numeric interval, such as '1900 - 2000'.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| separator | String | No description | —|–|- |

The identifier for this plugin is `insideNumericInterval`.

It can be found in the package `org.silkframework.rule.plugins.distance.numeric`.


##### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Numeric similarity

Computes the numeric distance between two numbers.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| minValue | double | The minimum number that is used for indexing | -Infinity |
| maxValue | double | The maximum number that is used for indexing | Infinity |

The identifier for this plugin is `num`.

It can be found in the package `org.silkframework.rule.plugins.distance.numeric`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Geographical distance

Computes the geographical distance between two points. Author: Konrad Höffner (MOLE subgroup of Research Group AKSW, University of Leipzig)

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| unit | String | No description | km |

The identifier for this plugin is `wgs84`.

It can be found in the package `org.silkframework.rule.plugins.distance.numeric`.


##### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

### Tokenbased

While character-based distance measures work well for typographical errors, there are a number of tasks where token-base distance measures are better suited:

- Strings where parts are reordered e.g. &ldquo;John Doe&rdquo; and &ldquo;Doe, John&rdquo;
- Texts consisting of multiple words

#### Cosine

Cosine Distance Measure.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| k | int | No description | 3 |

The identifier for this plugin is `cosine`.

It can be found in the package `org.silkframework.rule.plugins.distance.tokenbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

#### Dice coefficient

Dice similarity coefficient.

This plugin does not require any parameters.
The identifier for this plugin is `dice`.

It can be found in the package `org.silkframework.rule.plugins.distance.tokenbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares sets of multiple values.Typically, incoming values are tokenized before being fed into this measure.

#### Jaccard

Jaccard similarity coefficient. Divides the matching tokens by the number of distinct tokens from both inputs.

This plugin does not require any parameters.
The identifier for this plugin is `jaccard`.

It can be found in the package `org.silkframework.rule.plugins.distance.tokenbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares sets of multiple values.Typically, incoming values are tokenized before being fed into this measure.
##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Returns 0 for equal sets of values:

* Input values:
  - Source: `[A, B, C]`
  - Target: `[B, C, A]`

* Returns: → `0.0`


---
##### Returns 1 if there is no overlap between both sets of tokens:

* Input values:
  - Source: `[A, B, C]`
  - Target: `[D, E, F]`

* Returns: → `1.0`


---
##### Returns 0.5 if half of all unique tokens overlap:

* Input values:
  - Source: `[A, B, C]`
  - Target: `[A, B, D]`

* Returns: → `0.5`


---
##### Returns 2/3 if one third of all unique tokens overlap:

* Input values:
  - Source: `[John, Jane]`
  - Target: `[John, Max]`

* Returns: → `0.6666666666666666`

#### Soft Jaccard

Soft Jaccard similarity coefficient. Same as Jaccard distance but values within an levenhstein distance of 'maxDistance' are considered equivalent.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| maxDistance | int | No description | 1 |

The identifier for this plugin is `softjaccard`.

It can be found in the package `org.silkframework.rule.plugins.distance.tokenbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares sets of multiple values.Typically, incoming values are tokenized before being fed into this measure.

#### Token-wise distance

Token-wise string distance using the specified metric.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| ignoreCase | boolean | No description | true |
| metricName | String | No description | levenshtein |
| splitRegex | String | No description | [\\s\\d\\p{Punct}]+ |
| stopwords | String | No description | *empty string* |
| stopwordWeight | double | Weight assigned to stopwords | 0.01 |
| nonStopwordWeight | double | Weight assigned to non-stopwords | 0.1 |
| useIncrementalIdfWeights | boolean | Use incremental IDF weights | false |
| matchThreshold | double | No description | 0.0 |
| orderingImpact | double | No description | 0.0 |
| adjustByTokenLength | boolean | No description | false |

The identifier for this plugin is `tokenwiseDistance`.

It can be found in the package `org.silkframework.rule.plugins.distance.tokenbased`.


##### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Transformations

The following transform and normalization functions are available:

### Combine

#### Concatenate

Concatenates strings from multiple inputs.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| glue | String | Separator to be inserted between two concatenated strings. The text can contain escaped characters \\n, \\t and \\\\ that are replaced by a newline, tab or backslash respectively. | *empty string* |
| missingValuesAsEmptyStrings | boolean | Handle missing values as empty strings. | false |

The identifier for this plugin is `concat`.

It can be found in the package `org.silkframework.rule.plugins.transformer.combine`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[a]`

* Returns:

  → `[a]`


---
##### Example 3:

* Input values:
  1. `[a]`
  2. `[b]`

* Returns:

  → `[ab]`


---
##### Example 4:

* Parameters
  * *glue*: `-`

* Input values:
  1. `[First]`
  2. `[Last]`

* Returns:

  → `[First-Last]`


---
##### Example 5:

* Parameters
  * *glue*: `-`

* Input values:
  1. `[First]`
  2. `[Second, Third]`

* Returns:

  → `[First-Second, First-Third]`


---
##### Example 6:

* Parameters
  * *glue*: `-`

* Input values:
  1. `[First]`
  2. `[]`
  3. `[Second]`

* Returns:

  → `[First--Second]`


---
##### Example 7:

* Parameters
  * *glue*: `-`

* Input values:
  1. `[First]`
  2. `[]`
  3. `[Second]`

* Returns:

  → `[]`


---
##### Example 8:

* Parameters
  * *glue*: `-`
  * *missingValuesAsEmptyStrings*: `true`

* Input values:
  1. `[First]`
  2. `[]`
  3. `[Second]`

* Returns:

  → `[First--Second]`


---
##### Example 9:

* Parameters
  * *glue*: `\n`

* Input values:
  1. `[First]`
  2. `[Second]`

* Returns:

  → `[First
Second]`


---
##### Example 10:

* Parameters
  * *glue*: `\t\\\a`

* Input values:
  1. `[First]`
  2. `[Second]`

* Returns:

  → `[First	\\aSecond]`

#### Concatenate multiple values

Concatenates multiple values received for an input. If applied to multiple inputs, yields at most one value per input. Optionally removes duplicate values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| glue | String | No description | *empty string* |
| removeDuplicates | boolean | No description | false |

The identifier for this plugin is `concatMultiValues`.

It can be found in the package `org.silkframework.rule.plugins.transformer.combine`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[a]`

* Returns:

  → `[a]`


---
##### Example 3:

* Input values:
  1. `[a, b]`

* Returns:

  → `[ab]`


---
##### Example 4:

* Parameters
  * *glue*: `x`

* Input values:
  1. `[a, b]`

* Returns:

  → `[axb]`


---
##### Example 5:

* Input values:
  1. `[a, b]`
  2. `[1, 2]`

* Returns:

  → `[ab, 12]`


---
##### Example 6:

* Parameters
  * *glue*: `\n\t\\`

* Input values:
  1. `[a
	\b, c]`

* Returns:

  → `[a
	\b
	\c]`

#### Concatenate pairwise

Concatenates the values of multiple inputs pairwise.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| glue | String | Separator to be inserted between two concatenated strings. The text can contain escaped characters \\n, \\t and \\\\ that are replaced by a newline, tab or backslash respectively. | *empty string* |

The identifier for this plugin is `concatPairwise`.

It can be found in the package `org.silkframework.rule.plugins.transformer.combine`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Values of two inputs are concatenated pairwise:

* Input values:
  1. `[a, b, c]`
  2. `[1, 2, 3]`

* Returns:

  → `[a1, b2, c3]`


---
##### More than two inputs are supported as well:

* Input values:
  1. `[a, b, c]`
  2. `[1, 2, 3]`
  3. `[x, y, z]`

* Returns:

  → `[a1x, b2y, c3z]`


---
##### If one of the inputs has more values than the other, its remaining values are ignored:

* Input values:
  1. `[a, b, c]`
  2. `[1, 2]`

* Returns:

  → `[a1, b2]`


---
##### Empty input leads to empty output:

* Returns:

  → `[]`


---
##### A single input is just forwarded:

* Input values:
  1. `[a]`

* Returns:

  → `[a]`

#### Merge

Merges the values of all inputs.

This plugin does not require any parameters.
The identifier for this plugin is `merge`.

It can be found in the package `org.silkframework.rule.plugins.transformer.combine`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[a, b]`
  2. `[c]`

* Returns:

  → `[a, b, c]`

### Conditional

#### Contains all of

Accepts two inputs. If the first input contains all of the second input values it returns 'true', else 'false' is returned.

This plugin does not require any parameters.
The identifier for this plugin is `containsAllOf`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conditional`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[A, B, C]`
  2. `[A, B]`

* Returns:

  → `[true]`


---
##### Example 2:

* Input values:
  1. `[A, B, C]`
  2. `[A, D]`

* Returns:

  → `[false]`


---
##### Example 3:

* Input values:
  1. `[A, B, C]`
  2. `[D]`

* Returns:

  → `[false]`


---
##### Example 4:

* Input values:
  1. `[A, B, C]`
  2. `[A, B, C]`

* Returns:

  → `[true]`


---
##### Example 5:

* Input values:
  1. `[A, B, C]`
  2. `[]`

* Returns:

  → `[]`


---
##### Example 6:

* Input values:
  1. `[A]`
  2. `[A]`
  3. `[A]`

* Returns:

  → `[]`


---
##### Example 7:

* Input values:
  1. `[A]`

* Returns:

  → `[]`

#### Contains any of

Accepts two inputs. If the first input contains any of the second input values it returns 'true', else 'false' is returned.

This plugin does not require any parameters.
The identifier for this plugin is `containsAnyOf`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conditional`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[A, B, C]`
  2. `[A, B]`

* Returns:

  → `[true]`


---
##### Example 2:

* Input values:
  1. `[A, B, C]`
  2. `[A, D]`

* Returns:

  → `[true]`


---
##### Example 3:

* Input values:
  1. `[A, B, C]`
  2. `[D]`

* Returns:

  → `[false]`


---
##### Example 4:

* Input values:
  1. `[A, B, C]`
  2. `[A, B, C]`

* Returns:

  → `[true]`


---
##### Example 5:

* Input values:
  1. `[A, B, C]`
  2. `[]`

* Returns:

  → `[]`


---
##### Example 6:

* Input values:
  1. `[A]`
  2. `[A]`
  3. `[A]`

* Returns:

  → `[]`


---
##### Example 7:

* Input values:
  1. `[A]`

* Returns:

  → `[]`

#### If contains

Accepts two or three inputs. If the first input contains the given value, the second input is forwarded. Otherwise, the third input is forwarded (if present).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| search | String | No description | *no default* |

The identifier for this plugin is `ifContains`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conditional`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *search*: `match`

* Input values:
  1. `[matching string]`
  2. `[this is a match]`

* Returns:

  → `[this is a match]`


---
##### Example 2:

* Parameters
  * *search*: `match`

* Input values:
  1. `[different string]`
  2. `[this is a match]`

* Returns:

  → `[]`


---
##### Example 3:

* Parameters
  * *search*: `match`

* Input values:
  1. `[different string]`
  2. `[this is a match]`
  3. `[this is no match]`

* Returns:

  → `[this is no match]`

#### If exists

Accepts two or three inputs. If the first input provides a value, the second input is forwarded. Otherwise, the third input is forwarded (if present).

This plugin does not require any parameters.
The identifier for this plugin is `ifExists`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conditional`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[value]`
  2. `[yes]`
  3. `[no]`

* Returns:

  → `[yes]`


---
##### Example 2:

* Input values:
  1. `[]`
  2. `[yes]`
  3. `[no]`

* Returns:

  → `[no]`


---
##### Example 3:

* Input values:
  1. `[value]`
  2. `[]`

* Returns:

  → `[]`

#### If matches regex

Accepts two or three inputs.
If any value of the first input matches the regex, the second input is forwarded.
Otherwise, the third input is forwarded (if present).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| regex | String | No description | *no default* |
| negate | boolean | No description | false |

The identifier for this plugin is `ifMatchesRegex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conditional`.



#### Negate binary (NOT)

Accepts one input, which is either 'true', '1' or 'false', '0' and negates it.

This plugin does not require any parameters.
The identifier for this plugin is `negateTransformer`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conditional`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[0, 1, false, true, False, True]`

* Returns:

  → `[1, 0, true, false, true, false]`


---
##### Example 2:

* Input values:
  1. `[falsee, true]`

* Returns:

  → `[]`


---
##### Example 3:

* Input values:
  1. `[]`

* Returns:

  → `[]`

### Conversion

#### Convert charset

Convert the string from "sourceCharset" to "targetCharset".

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| sourceCharset | String | No description | ISO-8859-1 |
| targetCharset | String | No description | UTF-8 |

The identifier for this plugin is `convertCharset`.

It can be found in the package `org.silkframework.rule.plugins.transformer.conversion`.



#### Clean HTML

Cleans HTML using a tag white list and allows selection of HTML sections with XPath or CSS selector expressions.
       If the tag or attribute white lists are left empty default white lists will be used (this behaviour can be changed).
       To remove all HTML markup and retain text, keep the defaults and turn off the "Default tags and attributes" toggle.
       The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| tagWhiteList | StringIterableParameter | Tags to keep in the cleaned output. |  |
| attributeWhiteList | StringIterableParameter | Attributes to keep in the cleaned output. |  |
| selectors | StringIterableParameter | CSS or XPath queries for selection of content. CSS selectors can be pipe separated for non-sequential execution. |  |
| method | Enum | Selects use of XPath or CSS selectors. | xPath |
| defaultTagsAndAttributes | boolean | Use defaults for empty tag and attribute whitelists.\If the attribute while list is empty, it will default to: "class", "id", "href", "src"\If the tag while list is empty, it will default to: "a", "b", "blockquote", "br", "caption", "cite", "code", "col", "colgroup", "dd", "div", "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6","i", "img", "li", "ol", "p", "pre", "q", "small", "span", "strike", "strong","sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul". | true |

The identifier for this plugin is `htmlCleaner`.

It can be found in the package `com.eccenca.di.plugins.html`.



### Date

#### Parse date

Parses and normalizes dates in different formats.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| inputDateFormatId | Option | The input date/time format used for parsing the date/time string. | w3c Date |
| alternativeInputFormat | String | An input format string that should be used instead of the selected input format. Java DateFormat string. | *empty string* |
| inputLocale | LocaleOptionParameter | Optional locale for the (alternative) input format. If not set the system's locale will be used or the locale of the input format, if set. |  |
| outputDateFormatId | Option | The output date/time format used for parsing the date/time string. | w3c Date |
| alternativeOutputFormat | String | An output format string that should be used instead of the selected output format. Java DateFormat string. | *empty string* |
| outputLocale | LocaleOptionParameter | Optional locale for the (alternative) output format. If not set the system's locale will be used or the locale of the output format, if set. |  |

The identifier for this plugin is `DateTypeParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *inputDateFormatId*: `German style date format`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[20.03.1999]`

* Returns:

  → `[1999-03-20]`


---
##### Example 2:

* Parameters
  * *inputDateFormatId*: `w3c Date`
  * *outputDateFormatId*: `German style date format`

* Input values:
  1. `[1999-03-20]`

* Returns:

  → `[20.03.1999]`


---
##### Example 3:

* Parameters
  * *inputDateFormatId*: `common ISO8601`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[2017-04-04T00:00:00.000+02:00]`

* Returns:

  → `[2017-04-04]`


---
##### Example 4:

* Parameters
  * *inputDateFormatId*: `common ISO8601`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[2017-04-04T00:00:00+02:00]`

* Returns:

  → `[2017-04-04]`


---
##### Example 5:

* Parameters
  * *inputDateFormatId*: `common ISO8601`
  * *outputDateFormatId*: `dateTime with month abbr. (US)`

* Input values:
  1. `[2021-06-24T14:50:05.895+02:00]`

* Returns:

  → `[24-Jun-2021 14:50:05 +02:00]`


---
##### Example 6:

* Parameters
  * *inputDateFormatId*: `dateTime with month abbr. (US)`
  * *outputDateFormatId*: `dateTime with month abbr. (DE)`

* Input values:
  1. `[24-Dec-2021 14:50:05 +02:00]`

* Returns:

  → `[24-Dez.-2021 14:50:05 +02:00]`


---
##### Example 7:

* Parameters
  * *alternativeInputFormat*: `dd.MM.yyyy HH:mm.ss`
  * *alternativeOutputFormat*: `yyyy-MM-dd'T'HH:mm.ss`

* Input values:
  1. `[20.03.1999 20:34.44]`

* Returns:

  → `[1999-03-20T20:34.44]`


---
##### Example 8:

* Parameters
  * *inputDateFormatId*: `excelDateTime`
  * *outputDateFormatId*: `xsdTime`

* Input values:
  1. `[12:20:00.000]`

* Returns:

  → `[12:20:00.000]`


---
##### Example 9:

* Parameters
  * *inputDateFormatId*: `w3c YearMonth`
  * *outputDateFormatId*: `w3c Month`

* Input values:
  1. `[2020-01]`

* Returns:

  → `[--01]`


---
##### Example 10:

* Parameters
  * *inputDateFormatId*: `w3c MonthDay`
  * *outputDateFormatId*: `w3c Day`

* Input values:
  1. `[--12-31]`

* Returns:

  → `[---31]`


---
##### Example 11:

* Parameters
  * *inputDateFormatId*: `w3c Date`
  * *outputDateFormatId*: `w3c MonthDay`

* Input values:
  1. `[2020-12-31]`

* Returns:

  → `[--12-31]`


---
##### Example 12:

* Parameters
  * *inputDateFormatId*: `w3c MonthDay`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[--12-31]`

* Returns:

  → `[]`


---
##### Example 13:

* Parameters
  * *alternativeInputFormat*: `yyyy-MM-dd HH:mm:ss.SSS`
  * *outputDateFormatId*: `w3cDateTime`

* Input values:
  1. `[2020-02-22 16:34:14.000]`

* Returns:

  → `[2020-02-22T16:34:14]`


---
##### Example 14:

* Parameters
  * *inputDateFormatId*: `dateTime with month abbr. (DE)`
  * *outputDateFormatId*: `dateTime with month abbr. (US)`
  * *inputLocale*: `en_US`
  * *outputLocale*: `de`

* Input values:
  1. `[24-Dec-2021 14:50:05 +02:00]`

* Returns:

  → `[24-Dez.-2021 14:50:05 +02:00]`


---
##### Example 15:

* Parameters
  * *inputDateFormatId*: `dateTime with month abbr. (US)`
  * *outputDateFormatId*: `dateTime with month abbr. (DE)`
  * *inputLocale*: `de`
  * *outputLocale*: `en`

* Input values:
  1. `[24-Dez.-2021 14:50:05 +02:00]`

* Returns:

  → `[24-Dec-2021 14:50:05 +02:00]`


---
##### Example 16:

* Parameters
  * *outputLocale*: `fr`
  * *alternativeInputFormat*: `MMM yyyy`
  * *outputDateFormatId*: `dateTime with month abbr. (DE)`
  * *inputLocale*: `de`
  * *alternativeOutputFormat*: `MMM uuuu`
  * *inputDateFormatId*: `dateTime with month abbr. (US)`

* Input values:
  1. `[Dez. 2021]`

* Returns:

  → `[déc. 2021]`


---
##### Example 17:

* Parameters
  * *alternativeInputFormat*: `MMMM, uuuu`
  * *alternativeOutputFormat*: `MMMM, uuuu`
  * *inputLocale*: `en_US`
  * *outputLocale*: `de`

* Input values:
  1. `[February, 2024]`

* Returns:

  → `[Februar, 2024]`

#### Compare dates

Compares two dates.
Returns 1 if the comparison yields true and 0 otherwise.
If there are multiple dates in both sets, the comparator must be true for all dates.
For instance, {2014-08-02,2014-08-03} < {2014-08-03} yields 0 as not all dates in the first set are smaller than in the second.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| comparator | Enum | No description | < |

The identifier for this plugin is `compareDates`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *comparator*: `<`

* Input values:
  1. `[2017-01-01]`
  2. `[2017-01-02]`

* Returns:

  → `[1]`


---
##### Example 2:

* Parameters
  * *comparator*: `<`

* Input values:
  1. `[2017-01-02]`
  2. `[2017-01-01]`

* Returns:

  → `[0]`


---
##### Example 3:

* Parameters
  * *comparator*: `>`

* Input values:
  1. `[2017-01-02]`
  2. `[2017-01-01]`

* Returns:

  → `[1]`


---
##### Example 4:

* Parameters
  * *comparator*: `>`

* Input values:
  1. `[2017-01-01]`
  2. `[2017-01-02]`

* Returns:

  → `[0]`


---
##### Example 5:

* Parameters
  * *comparator*: `=`

* Input values:
  1. `[2017-01-01]`
  2. `[2017-01-01]`

* Returns:

  → `[1]`


---
##### Example 6:

* Parameters
  * *comparator*: `=`

* Input values:
  1. `[2017-01-02]`
  2. `[2017-01-01]`

* Returns:

  → `[0]`

#### Current date

Outputs the current date.

This plugin does not require any parameters.
The identifier for this plugin is `currentDate`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Date to timestamp

Convert an xsd:dateTime to a timestamp. Returns the passed time since the Unix Epoch (1970-01-01).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| unit | Enum | No description | milliseconds |

The identifier for this plugin is `datetoTimestamp`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[2017-07-03T21:32:52Z]`

* Returns:

  → `[1499117572000]`


---
##### Example 2:

* Input values:
  1. `[2017-07-03T21:32:52+01:00]`

* Returns:

  → `[1499113972000]`


---
##### Example 3:

* Parameters
  * *unit*: `seconds`

* Input values:
  1. `[2017-07-03T21:32:52+01:00]`

* Returns:

  → `[1499113972]`


---
##### Example 4:

* Input values:
  1. `[2017-07-03]`

* Returns:

  → `[1499040000000]`

#### Duration

Computes the time difference between two data times.

This plugin does not require any parameters.
The identifier for this plugin is `duration`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Duration in days

Converts an xsd:duration to days.

This plugin does not require any parameters.
The identifier for this plugin is `durationInDays`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Duration in seconds

Converts an xsd:duration to seconds.

This plugin does not require any parameters.
The identifier for this plugin is `durationInSeconds`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Duration in years

Converts an xsd:duration to years.

This plugin does not require any parameters.
The identifier for this plugin is `durationInYears`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Number to duration

Converts a number to an xsd:duration.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| unit | Enum | No description | day |

The identifier for this plugin is `numberToDuration`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Parse date pattern

Parses a date based on a specified pattern, returning an xsd:date.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| format | String | The date pattern used to parse the input values | dd-MM-yyyy |
| lenient | boolean | If set to true, the parser tries to use heuristics to parse dates with invalid fields (such as a day of zero). | false |
| locale | LocaleOptionParameter | Optional locale for the date format. If not set the system's locale will be used. |  |

The identifier for this plugin is `parseDate`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *format*: `dd.MM.yyyy`

* Input values:
  1. `[03.04.2015]`

* Returns:

  → `[2015-04-03]`


---
##### Example 2:

* Parameters
  * *format*: `dd.MM.yyyy`

* Input values:
  1. `[3.4.2015]`

* Returns:

  → `[2015-04-03]`


---
##### Example 3:

* Parameters
  * *format*: `yyyyMMdd`

* Input values:
  1. `[20150403]`

* Returns:

  → `[2015-04-03]`


---
##### Example 4:

* Parameters
  * *format*: `MMM yyyy`
  * *locale*: `en`

* Input values:
  1. `[May 2024]`

* Returns:

  → `[2024-05-01]`


---
##### Example 5:

* Parameters
  * *format*: `MMM yyyy`
  * *locale*: `de`

* Input values:
  1. `[Mai 2024]`

* Returns:

  → `[2024-05-01]`


---
##### Example 6:

* Parameters
  * *format*: `MMM yyyy`
  * *locale*: `de`

* Input values:
  1. `[May 2024]`

* Returns:

  → `[]`


---
##### Example 7:

* Parameters
  * *format*: `yyyyMMdd`
  * *lenient*: `false`

* Input values:
  1. `[20150000]`

* Returns:

  → `[]`

#### Timestamp to date

Convert a timestamp to xsd:date format. Expects an integer that denotes the passed time since the Unix Epoch (1970-01-01)

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| format | String | Custom output format (e.g., 'yyyy-MM-dd'). If left empty, a full xsd:dateTime (UTC) is returned. | *empty string* |
| unit | Enum | No description | milliseconds |

The identifier for this plugin is `timeToDate`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[1499117572000]`

* Returns:

  → `[2017-07-03T21:32:52Z]`


---
##### Example 2:

* Parameters
  * *format*: `yyyy-MM-dd`

* Input values:
  1. `[1499040000000]`

* Returns:

  → `[2017-07-03]`


---
##### Example 3:

* Parameters
  * *format*: `yyyy-MM-dd`
  * *unit*: `seconds`

* Input values:
  1. `[1499040000]`

* Returns:

  → `[2017-07-03]`

#### Validate date after

Validates if the first input date is after the second input date. Outputs the first input if the validation is successful.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| allowEqual | boolean | Allow both dates to be equal. | false |

The identifier for this plugin is `validateDateAfter`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[2015-04-02]`
  2. `[2015-04-03]`

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[2015-04-04]`
  2. `[2015-04-03]`

* Returns:

  → `[2015-04-04]`


---
##### Example 3:

* Parameters
  * *allowEqual*: `true`

* Input values:
  1. `[2015-04-03]`
  2. `[2015-04-03]`

* Returns:

  → `[2015-04-03]`


---
##### Example 4:

* Parameters
  * *allowEqual*: `false`

* Input values:
  1. `[2015-04-03]`
  2. `[2015-04-03]`

* Returns:

  → `[]`

#### Validate date range

Validates if dates are within a specified range.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| minDate | String | Earliest allowed date in YYYY-MM-DD | *no default* |
| maxDate | String | Latest allowed data in YYYY-MM-DD | *no default* |

The identifier for this plugin is `validateDateRange`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.



#### Validate numeric range

Validates if a number is within a specified range.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| min | double | Minimum allowed number | *no default* |
| max | double | Maximum allowed number | *no default* |

The identifier for this plugin is `validateNumericRange`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.



### Excel

#### Abs

Excel ABS(number): Returns the absolute value of the given number.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ABS |

The identifier for this plugin is `Excel_ABS`.

It can be found in the package `com.eccenca.di.excel`.



#### Acos

Excel ACOS(number): Returns the inverse cosine of the given number in radians.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ACOS |

The identifier for this plugin is `Excel_ACOS`.

It can be found in the package `com.eccenca.di.excel`.



#### Acosh

Excel ACOSH(number): Returns the inverse hyperbolic cosine of the given number in radians.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ACOSH |

The identifier for this plugin is `Excel_ACOSH`.

It can be found in the package `com.eccenca.di.excel`.



#### And

Excel AND(argument1; argument2 ...argument30): Returns TRUE if all the arguments are considered TRUE, and FALSE otherwise.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | AND |

The identifier for this plugin is `Excel_AND`.

It can be found in the package `com.eccenca.di.excel`.



#### Asin

Excel ASIN(number): Returns the inverse sine of the given number in radians.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ASIN |

The identifier for this plugin is `Excel_ASIN`.

It can be found in the package `com.eccenca.di.excel`.



#### Asinh

Excel ASINH(number): Returns the inverse hyperbolic sine of the given number in radians.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ASINH |

The identifier for this plugin is `Excel_ASINH`.

It can be found in the package `com.eccenca.di.excel`.



#### Atan

Excel ATAN(number): Returns the inverse tangent of the given number in radians.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ATAN |

The identifier for this plugin is `Excel_ATAN`.

It can be found in the package `com.eccenca.di.excel`.



#### Atan2

Excel ATAN2(number_x; number_y): Returns the inverse tangent of the specified x and y coordinates. Number_x is the value for the x coordinate. Number_y is the value for the y coordinate.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ATAN2 |

The identifier for this plugin is `Excel_ATAN2`.

It can be found in the package `com.eccenca.di.excel`.



#### Atanh

Excel ATANH(number): Returns the inverse hyperbolic tangent of the given number. (Angle is returned in radians.)

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ATANH |

The identifier for this plugin is `Excel_ATANH`.

It can be found in the package `com.eccenca.di.excel`.



#### Avedev

Excel AVEDEV(number1; number2; ... number_30): Returns the average of the absolute deviations of data points from their mean. Displays the diffusion in a data set. Number_1; number_2; ... number_30 are values or ranges that represent a sample. Each number can also be replaced by a reference.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | AVEDEV |

The identifier for this plugin is `Excel_AVEDEV`.

It can be found in the package `com.eccenca.di.excel`.



#### Average

Excel AVERAGE(number_1; number_2; ... number_30): Returns the average of the arguments. Number_1; number_2; ... number_30 are numerical values or ranges. Text is ignored.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | AVERAGE |

The identifier for this plugin is `Excel_AVERAGE`.

It can be found in the package `com.eccenca.di.excel`.



#### Averagea

Excel AVERAGEA(value_1; value_2; ... value_30): Returns the average of the arguments. The value of a text is 0. Value_1; value_2; ... value_30 are values or ranges.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | AVERAGEA |

The identifier for this plugin is `Excel_AVERAGEA`.

It can be found in the package `com.eccenca.di.excel`.



#### Ceiling

Excel CEILING(number; significance; mode): Rounds the given number to the nearest integer or multiple of significance. Significance is the value to whose multiple of ten the value is to be rounded up (.01, .1, 1, 10, etc.). Mode is an optional value. If it is indicated and non-zero and if the number and significance are negative, rounding up is carried out based on that value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | CEILING |

The identifier for this plugin is `Excel_CEILING`.

It can be found in the package `com.eccenca.di.excel`.



#### Choose

Excel CHOOSE(index; value1; ... value30): Uses an index to return a value from a list of up to 30 values. Index is a reference or number between 1 and 30 indicating which value is to be taken from the list. Value1; ... value30 is the list of values entered as a reference to a cell or as individual values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | CHOOSE |

The identifier for this plugin is `Excel_CHOOSE`.

It can be found in the package `com.eccenca.di.excel`.



#### Clean

Excel CLEAN(text): Removes all non-printing characters from the string. Text refers to the text from which to remove all non-printable characters.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | CLEAN |

The identifier for this plugin is `Excel_CLEAN`.

It can be found in the package `com.eccenca.di.excel`.



#### Code

Excel CODE(text): Returns a numeric code for the first character in a text string. Text is the text for which the code of the first character is to be found.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | CODE |

The identifier for this plugin is `Excel_CODE`.

It can be found in the package `com.eccenca.di.excel`.



#### Combin

Excel COMBIN(count_1; count_2): Returns the number of combinations for a given number of objects. Count_1 is the total number of elements. Count_2 is the selected count from the elements. This is the same as the nCr function on a calculator.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | COMBIN |

The identifier for this plugin is `Excel_COMBIN`.

It can be found in the package `com.eccenca.di.excel`.



#### Correl

Excel CORREL(data_1; data_2): Returns the correlation coefficient between two data sets. Data_1 is the first data set. Data_2 is the second data set.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | CORREL |

The identifier for this plugin is `Excel_CORREL`.

It can be found in the package `com.eccenca.di.excel`.



#### Cos

Excel COS(number): Returns the cosine of the given number (angle in radians).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | COS |

The identifier for this plugin is `Excel_COS`.

It can be found in the package `com.eccenca.di.excel`.



#### Cosh

Excel COSH(number): Returns the hyperbolic cosine of the given number (angle in radians).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | COSH |

The identifier for this plugin is `Excel_COSH`.

It can be found in the package `com.eccenca.di.excel`.



#### Count

Excel COUNT(value_1; value_2; ... value_30): Counts how many numbers are in the list of arguments. Text entries are ignored. Value_1; value_2; ... value_30 are values or ranges which are to be counted.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | COUNT |

The identifier for this plugin is `Excel_COUNT`.

It can be found in the package `com.eccenca.di.excel`.



#### Counta

Excel COUNTA(value_1; value_2; ... value_30): Counts how many values are in the list of arguments. Text entries are also counted, even when they contain an empty string of length 0. If an argument is an array or reference, empty cells within the array or reference are ignored. value_1; value_2; ... value_30 are up to 30 arguments representing the values to be counted.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | COUNTA |

The identifier for this plugin is `Excel_COUNTA`.

It can be found in the package `com.eccenca.di.excel`.



#### Covar

Excel COVAR(data_1; data_2): Returns the covariance of the product of paired deviations. Data_1 is the first data set. Data_2 is the second data set.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | COVAR |

The identifier for this plugin is `Excel_COVAR`.

It can be found in the package `com.eccenca.di.excel`.



#### Degrees

Excel DEGREES(number): Converts the given number in radians to degrees.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | DEGREES |

The identifier for this plugin is `Excel_DEGREES`.

It can be found in the package `com.eccenca.di.excel`.



#### Devsq

Excel DEVSQ(number_1; number_2; ... number_30): Returns the sum of squares of deviations based on a sample mean. Number_1; number_2; ... number_30 are numerical values or ranges representing a sample.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | DEVSQ |

The identifier for this plugin is `Excel_DEVSQ`.

It can be found in the package `com.eccenca.di.excel`.



#### Even

Excel EVEN(number): Rounds the given number up to the nearest even integer.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | EVEN |

The identifier for this plugin is `Excel_EVEN`.

It can be found in the package `com.eccenca.di.excel`.



#### Exact

Excel EXACT(text_1; text_2): Compares two text strings and returns TRUE if they are identical. This function is case- sensitive. Text_1 is the first text to compare. Text_2 is the second text to compare.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | EXACT |

The identifier for this plugin is `Excel_EXACT`.

It can be found in the package `com.eccenca.di.excel`.



#### Exp

Excel EXP(number): Returns e raised to the power of the given number.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | EXP |

The identifier for this plugin is `Excel_EXP`.

It can be found in the package `com.eccenca.di.excel`.



#### Fact

Excel FACT(number): Returns the factorial of the given number.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | FACT |

The identifier for this plugin is `Excel_FACT`.

It can be found in the package `com.eccenca.di.excel`.



#### False

Excel FALSE(): Set the logical value to FALSE. The FALSE() function does not require any arguments.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | FALSE |

The identifier for this plugin is `Excel_FALSE`.

It can be found in the package `com.eccenca.di.excel`.



#### Find

Excel FIND(find_text; text; position): Looks for a string of text within another string. Where to begin the search can also be defined. The search term can be a number or any string of characters. The search is case-sensitive. Find_text is the text to be found. Text is the text where the search takes place. Position (optional) is the position in the text from which the search starts.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | FIND |

The identifier for this plugin is `Excel_FIND`.

It can be found in the package `com.eccenca.di.excel`.



#### Floor

Excel FLOOR(number; significance; mode): Rounds the given number down to the nearest multiple of significance. Significance is the value to whose multiple of ten the number is to be rounded down (.01, .1, 1, 10, etc.). Mode is an optional value. If it is indicated and non-zero and if the number and significance are negative, rounding up is carried out based on that value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | FLOOR |

The identifier for this plugin is `Excel_FLOOR`.

It can be found in the package `com.eccenca.di.excel`.



#### Forecast

Excel FORECAST(value; data_Y; data_X): Extrapolates future values based on existing x and y values. Value is the x value, for which the y value of the linear regression is to be returned. Data_Y is the array or range of known ys. Data_X is the array or range of known xs. Does not work for exponential functions.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | FORECAST |

The identifier for this plugin is `Excel_FORECAST`.

It can be found in the package `com.eccenca.di.excel`.



#### Fv

Excel FV(rate; NPER; PMT; PV; type): Returns the future value of an investment based on periodic, constant payments and a constant interest rate. Rate is the periodic interest rate. NPER is the total number of periods. PMT is the annuity paid regularly per period. PV (optional) is the present cash value of an investment. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | FV |

The identifier for this plugin is `Excel_FV`.

It can be found in the package `com.eccenca.di.excel`.



#### Geomean

Excel GEOMEAN(number_1; number_2; ... number_30): Returns the geometric mean of a sample. Number_1; number_2; ... number_30 are numerical arguments or ranges that represent a random sample.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | GEOMEAN |

The identifier for this plugin is `Excel_GEOMEAN`.

It can be found in the package `com.eccenca.di.excel`.



#### If

Excel IF(test; then_value; otherwise_value): Returns different values based on the test value. Note that in this implementation it will not actually evaluate logical conditions. Then_value is the value that is returned if the test is TRUE. Otherwise_value (optional) is the value that is returned if the test is FALSE.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | IF |

The identifier for this plugin is `Excel_IF`.

It can be found in the package `com.eccenca.di.excel`.



#### Int

Excel INT(number): Rounds the given number down to the nearest integer.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | INT |

The identifier for this plugin is `Excel_INT`.

It can be found in the package `com.eccenca.di.excel`.



#### Intercept

Excel INTERCEPT(data_Y; data_X): Calculates the y-value at which a line will intersect the y-axis by using known x-values and y-values. Data_Y is the dependent set of observations or data. Data_X is the independent set of observations or data. Names, arrays or references containing numbers must be used here. Numbers can also be entered directly.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | INTERCEPT |

The identifier for this plugin is `Excel_INTERCEPT`.

It can be found in the package `com.eccenca.di.excel`.



#### Ipmt

Excel IPMT(rate; period; NPER; PV; FV; type): Calculates the periodic amortization for an investment with regular payments and a constant interest rate. Rate is the periodic interest rate. Period is the period for which the compound interest is calculated. NPER is the total number of periods during which annuity is paid. Period=NPER, if compound interest for the last period is calculated. PV is the present cash value in sequence of payments. FV (optional) is the desired value (future value) at the end of the periods. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | IPMT |

The identifier for this plugin is `Excel_IPMT`.

It can be found in the package `com.eccenca.di.excel`.



#### Irr

Excel IRR(values; guess): Calculates the internal rate of return for an investment. The values represent cash flow values at regular intervals; at least one value must be negative (payments), and at least one value must be positive (income). Values is an array containing the values. Guess (optional) is the estimated value. If you can provide only a few values, you should provide an initial guess to enable the iteration.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | IRR |

The identifier for this plugin is `Excel_IRR`.

It can be found in the package `com.eccenca.di.excel`.



#### Large

Excel LARGE(data; rank_c): Returns the Rank_c-th largest value in a data set. Data is the cell range of data. Rank_c is the ranking of the value (2nd largest, 3rd largest, etc.) written as an integer.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | LARGE |

The identifier for this plugin is `Excel_LARGE`.

It can be found in the package `com.eccenca.di.excel`.



#### Left

Excel LEFT(text; number): Returns the first character or characters in a text string. Text is the text where the initial partial words are to be determined. Number (optional) is the number of characters for the start text. If this parameter is not defined, one character is returned.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | LEFT |

The identifier for this plugin is `Excel_LEFT`.

It can be found in the package `com.eccenca.di.excel`.



#### Ln

Excel LN(number): Returns the natural logarithm based on the constant e of the given number.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | LN |

The identifier for this plugin is `Excel_LN`.

It can be found in the package `com.eccenca.di.excel`.



#### Log

Excel LOG(number; base): Returns the logarithm of the given number to the specified base. Base is the base for the logarithm calculation.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | LOG |

The identifier for this plugin is `Excel_LOG`.

It can be found in the package `com.eccenca.di.excel`.



#### Log10

Excel LOG10(number): Returns the base-10 logarithm of the given number.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | LOG10 |

The identifier for this plugin is `Excel_LOG10`.

It can be found in the package `com.eccenca.di.excel`.



#### Max

Excel MAX(number_1; number_2; ... number_30): Returns the maximum value in a list of arguments. Number_1; number_2; ... number_30 are numerical values or ranges.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MAX |

The identifier for this plugin is `Excel_MAX`.

It can be found in the package `com.eccenca.di.excel`.



#### Maxa

Excel MAXA(value_1; value_2; ... value_30): Returns the maximum value in a list of arguments. Unlike MAX, text can be entered. The value of the text is 0. Value_1; value_2; ... value_30 are values or ranges.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MAXA |

The identifier for this plugin is `Excel_MAXA`.

It can be found in the package `com.eccenca.di.excel`.



#### Median

Excel MEDIAN(number_1; number_2; ... number_30): Returns the median of a set of numbers. Number_1; number_2; ... number_30 are values or ranges, which represent a sample. Each number can also be replaced by a reference.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MEDIAN |

The identifier for this plugin is `Excel_MEDIAN`.

It can be found in the package `com.eccenca.di.excel`.



#### Mid

Excel MID(text; start; number): Returns a text segment of a character string. The parameters specify the starting position and the number of characters. Text is the text containing the characters to extract. Start is the position of the first character in the text to extract. Number is the number of characters in the part of the text.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MID |

The identifier for this plugin is `Excel_MID`.

It can be found in the package `com.eccenca.di.excel`.



#### Min

Excel MIN(number_1; number_2; ... number_30): Returns the minimum value in a list of arguments. Number_1; number_2; ... number_30 are numerical values or ranges.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MIN |

The identifier for this plugin is `Excel_MIN`.

It can be found in the package `com.eccenca.di.excel`.



#### Mina

Excel MINA(value_1; value_2; ... value_30): Returns the minimum value in a list of arguments. Here text can also be entered. The value of the text is 0. Value_1; value_2; ... value_30 are values or ranges.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MINA |

The identifier for this plugin is `Excel_MINA`.

It can be found in the package `com.eccenca.di.excel`.



#### Mirr

Excel MIRR(values; investment; reinvest_rate): Calculates the modified internal rate of return of a series of investments. Values corresponds to the array or the cell reference for cells whose content corresponds to the payments. Investment is the rate of interest of the investments (the negative values of the array) Reinvest_rate is the rate of interest of the reinvestment (the positive values of the array).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MIRR |

The identifier for this plugin is `Excel_MIRR`.

It can be found in the package `com.eccenca.di.excel`.



#### Mod

Excel MOD(dividend; divisor): Returns the remainder after a number is divided by a divisor. Dividend is the number which will be divided by the divisor. Divisor is the number by which to divide the dividend.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MOD |

The identifier for this plugin is `Excel_MOD`.

It can be found in the package `com.eccenca.di.excel`.



#### Mode

Excel MODE(number_1; number_2; ... number_30): Returns the most common value in a data set. Number_1; number_2; ... number_30 are numerical values or ranges. If several values have the same frequency, it returns the smallest value. An error occurs when a value does not appear twice.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | MODE |

The identifier for this plugin is `Excel_MODE`.

It can be found in the package `com.eccenca.di.excel`.



#### Normdist

Excel NORMDIST(number; mean; STDEV; C): Returns the normal distribution for the given Number in the distribution. Mean is the mean value of the distribution. STDEV is the standard deviation of the distribution. C = 0 calculates the density function, and C = 1 calculates the distribution.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NORMDIST |

The identifier for this plugin is `Excel_NORMDIST`.

It can be found in the package `com.eccenca.di.excel`.



#### Norminv

Excel NORMINV(number; mean; STDEV): Returns the inverse of the normal distribution for the given Number in the distribution. Mean is the mean value in the normal distribution. STDEV is the standard deviation of the normal distribution.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NORMINV |

The identifier for this plugin is `Excel_NORMINV`.

It can be found in the package `com.eccenca.di.excel`.



#### Normsdist

Excel NORMSDIST(number): Returns the standard normal cumulative distribution for the given Number.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NORMSDIST |

The identifier for this plugin is `Excel_NORMSDIST`.

It can be found in the package `com.eccenca.di.excel`.



#### Normsinv

Excel NORMSINV(number): Returns the inverse of the standard normal distribution for the given Number, a probability value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NORMSINV |

The identifier for this plugin is `Excel_NORMSINV`.

It can be found in the package `com.eccenca.di.excel`.



#### Not

Excel NOT(logical_value): Reverses the logical value. Logical_value is any value to be reversed.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NOT |

The identifier for this plugin is `Excel_NOT`.

It can be found in the package `com.eccenca.di.excel`.



#### Nper

Excel NPER(rate; PMT; PV; FV; type): Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate. Rate is the periodic interest rate. PMT is the constant annuity paid in each period. PV is the present value (cash value) in a sequence of payments. FV (optional) is the future value, which is reached at the end of the last period. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NPER |

The identifier for this plugin is `Excel_NPER`.

It can be found in the package `com.eccenca.di.excel`.



#### Npv

Excel NPV(Rate; value_1; value_2; ... value_30): Returns the net present value of an investment based on a series of periodic cash flows and a discount rate. Rate is the discount rate for a period. Value_1; value_2;... value_30 are values representing deposits or withdrawals.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | NPV |

The identifier for this plugin is `Excel_NPV`.

It can be found in the package `com.eccenca.di.excel`.



#### Odd

Excel ODD(number): Rounds the given number up to the nearest odd integer.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ODD |

The identifier for this plugin is `Excel_ODD`.

It can be found in the package `com.eccenca.di.excel`.



#### Or

Excel OR(logical_value_1; logical_value_2; ...logical_value_30): Returns TRUE if at least one argument is TRUE. Returns the value FALSE if all the arguments have the logical value FALSE. Logical_value_1; logical_value_2; ...logical_value_30 are conditions to be checked. All conditions can be either TRUE or FALSE. If a range is entered as a parameter, the function uses the value from the range that is in the current column or row.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | OR |

The identifier for this plugin is `Excel_OR`.

It can be found in the package `com.eccenca.di.excel`.



#### Pearson

Excel PEARSON(data_1; data_2): Returns the Pearson product moment correlation coefficient r. Data_1 is the array of the first data set. Data_2 is the array of the second data set.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PEARSON |

The identifier for this plugin is `Excel_PEARSON`.

It can be found in the package `com.eccenca.di.excel`.



#### Percentile

Excel PERCENTILE(data; alpha): Returns the alpha-percentile of data values in an array. Data is the array of data. Alpha is the percentage of the scale between 0 and 1.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PERCENTILE |

The identifier for this plugin is `Excel_PERCENTILE`.

It can be found in the package `com.eccenca.di.excel`.



#### Percentrank

Excel PERCENTRANK(data; value): Returns the percentage rank (percentile) of the given value in a sample. Data is the array of data in the sample.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PERCENTRANK |

The identifier for this plugin is `Excel_PERCENTRANK`.

It can be found in the package `com.eccenca.di.excel`.



#### Pi

Excel PI(): Returns the value of PI to fourteen decimal places.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PI |

The identifier for this plugin is `Excel_PI`.

It can be found in the package `com.eccenca.di.excel`.



#### Pmt

Excel PMT(rate; NPER; PV; FV; type): Returns the periodic payment for an annuity with constant interest rates. Rate is the periodic interest rate. NPER is the number of periods in which annuity is paid. PV is the present value (cash value) in a sequence of payments. FV (optional) is the desired value (future value) to be reached at the end of the periodic payments. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PMT |

The identifier for this plugin is `Excel_PMT`.

It can be found in the package `com.eccenca.di.excel`.



#### Poisson

Excel POISSON(number; mean; C): Returns the Poisson distribution for the given Number. Mean is the middle value of the Poisson distribution. C = 0 calculates the density function, and C = 1 calculates the distribution.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | POISSON |

The identifier for this plugin is `Excel_POISSON`.

It can be found in the package `com.eccenca.di.excel`.



#### Power

Excel POWER(base; power): Returns the result of a number raised to a power. Base is the number that is to be raised to the given power. Power is the exponent by which the base is to be raised.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | POWER |

The identifier for this plugin is `Excel_POWER`.

It can be found in the package `com.eccenca.di.excel`.



#### Ppmt

Excel PPMT(rate; period; NPER; PV; FV; type): Returns for a given period the payment on the principal for an investment that is based on periodic and constant payments and a constant interest rate. Rate is the periodic interest rate. Period is the amortization period. NPER is the total number of periods during which annuity is paid. PV is the present value in the sequence of payments. FV (optional) is the desired (future) value. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PPMT |

The identifier for this plugin is `Excel_PPMT`.

It can be found in the package `com.eccenca.di.excel`.



#### Product

Excel PRODUCT(number 1 to 30): Multiplies all the numbers given as arguments and returns the product. Number 1 to number 30 are up to 30 arguments whose product is to be calculated, separated by semi-colons.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PRODUCT |

The identifier for this plugin is `Excel_PRODUCT`.

It can be found in the package `com.eccenca.di.excel`.



#### Proper

Excel PROPER(text): Capitalizes the first letter in all words of a text string. Text is the text to be converted.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PROPER |

The identifier for this plugin is `Excel_PROPER`.

It can be found in the package `com.eccenca.di.excel`.



#### Pv

Excel PV(rate; NPER; PMT; FV; type): Returns the present value of an investment resulting from a series of regular payments. Rate defines the interest rate per period. NPER is the total number of payment periods. PMT is the regular payment made per period. FV (optional) defines the future value remaining after the final installment has been made. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | PV |

The identifier for this plugin is `Excel_PV`.

It can be found in the package `com.eccenca.di.excel`.



#### Radians

Excel RADIANS(number): Converts the given number in degrees to radians.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | RADIANS |

The identifier for this plugin is `Excel_RADIANS`.

It can be found in the package `com.eccenca.di.excel`.



#### Rand

Excel RAND(): Returns a random number between 0 and 1.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | RAND |

The identifier for this plugin is `Excel_RAND`.

It can be found in the package `com.eccenca.di.excel`.



#### Rank

Excel RANK(value; data; type): Returns the rank of the given Value in a sample. Data is the array or range of data in the sample. Type (optional) is the sequence order, either ascending (0) or descending (1).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | RANK |

The identifier for this plugin is `Excel_RANK`.

It can be found in the package `com.eccenca.di.excel`.



#### Rate

Excel RATE(NPER; PMT; PV; FV; type; guess): Returns the constant interest rate per period of an annuity. NPER is the total number of periods, during which payments are made (payment period). PMT is the constant payment (annuity) paid during each period. PV is the cash value in the sequence of payments. FV (optional) is the future value, which is reached at the end of the periodic payments. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period. Guess (optional) determines the estimated value of the interest with iterative calculation.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | RATE |

The identifier for this plugin is `Excel_RATE`.

It can be found in the package `com.eccenca.di.excel`.



#### Replace

Excel REPLACE(text; position; length; new_text): Replaces part of a text string with a different text string. This function can be used to replace both characters and numbers (which are automatically converted to text). The result of the function is always displayed as text. To perform further calculations with a number which has been replaced by text, convert it back to a number using the VALUE function. Any text containing numbers must be enclosed in quotation marks so it is not interpreted as a number and automatically converted to text. Text is text of which a part will be replaced. Position is the position within the text where the replacement will begin. Length is the number of characters in text to be replaced. New_text is the text which replaces text..

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | REPLACE |

The identifier for this plugin is `Excel_REPLACE`.

It can be found in the package `com.eccenca.di.excel`.



#### Rept

Excel REPT(text; number): Repeats a character string by the given number of copies. Text is the text to be repeated. Number is the number of repetitions. The result can be a maximum of 255 characters.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | REPT |

The identifier for this plugin is `Excel_REPT`.

It can be found in the package `com.eccenca.di.excel`.



#### Right

Excel RIGHT(text; number): Defines the last character or characters in a text string. Text is the text of which the right part is to be determined. Number (optional) is the number of characters from the right part of the text.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | RIGHT |

The identifier for this plugin is `Excel_RIGHT`.

It can be found in the package `com.eccenca.di.excel`.



#### Roman

Excel ROMAN(number; mode): Converts a number into a Roman numeral. The value range must be between 0 and 3999; the modes can be integers from 0 to 4. Number is the number that is to be converted into a Roman numeral. Mode (optional) indicates the degree of simplification. The higher the value, the greater is the simplification of the Roman numeral.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ROMAN |

The identifier for this plugin is `Excel_ROMAN`.

It can be found in the package `com.eccenca.di.excel`.



#### Round

Excel ROUND(number; count): Rounds the given number to a certain number of decimal places according to valid mathematical criteria. Count (optional) is the number of the places to which the value is to be rounded. If the count parameter is negative, only the whole number portion is rounded. It is rounded to the place indicated by the count.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ROUND |

The identifier for this plugin is `Excel_ROUND`.

It can be found in the package `com.eccenca.di.excel`.



#### Rounddown

Excel ROUNDDOWN(number; count): Rounds the given number. Count (optional) is the number of digits to be rounded down to. If the count parameter is negative, only the whole number portion is rounded. It is rounded to the place indicated by the count.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ROUNDDOWN |

The identifier for this plugin is `Excel_ROUNDDOWN`.

It can be found in the package `com.eccenca.di.excel`.



#### Roundup

Excel ROUNDUP(number; count): Rounds the given number up. Count (optional) is the number of digits to which rounding up is to be done. If the count parameter is negative, only the whole number portion is rounded. It is rounded to the place indicated by the count.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | ROUNDUP |

The identifier for this plugin is `Excel_ROUNDUP`.

It can be found in the package `com.eccenca.di.excel`.



#### Search

Excel SEARCH(find_text; text; position): Returns the position of a text segment within a character string. The start of the search can be set as an option. The search text can be a number or any sequence of characters. The search is not case-sensitive. The search supports regular expressions. Find_text is the text to be searched for. Text is the text where the search will take place. Position (optional) is the position in the text where the search is to start.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SEARCH |

The identifier for this plugin is `Excel_SEARCH`.

It can be found in the package `com.eccenca.di.excel`.



#### Sign

Excel SIGN(number): Returns the sign of the given number. The function returns the result 1 for a positive sign,  1 for a negative sign, and 0 for zero.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SIGN |

The identifier for this plugin is `Excel_SIGN`.

It can be found in the package `com.eccenca.di.excel`.



#### Sin

Excel SIN(number): Returns the sine of the given number (angle in radians).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SIN |

The identifier for this plugin is `Excel_SIN`.

It can be found in the package `com.eccenca.di.excel`.



#### Sinh

Excel SINH(number): Returns the hyperbolic sine of the given number (angle in radians).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SINH |

The identifier for this plugin is `Excel_SINH`.

It can be found in the package `com.eccenca.di.excel`.



#### Slope

Excel SLOPE(data_Y; data_X): Returns the slope of the linear regression line. Data_Y is the array or matrix of Y data. Data_X is the array or matrix of X data.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SLOPE |

The identifier for this plugin is `Excel_SLOPE`.

It can be found in the package `com.eccenca.di.excel`.



#### Small

Excel SMALL(data; rank_c): Returns the Rank_c-th smallest value in a data set. Data is the cell range of data. Rank_c is the rank of the value (2nd smallest, 3rd smallest, etc.) written as an integer.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SMALL |

The identifier for this plugin is `Excel_SMALL`.

It can be found in the package `com.eccenca.di.excel`.



#### Sqrt

Excel SQRT(number): Returns the positive square root of the given number. The value of the number must be positive.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SQRT |

The identifier for this plugin is `Excel_SQRT`.

It can be found in the package `com.eccenca.di.excel`.



#### Standardize

Excel STANDARDIZE(number; mean; STDEV): Converts a random variable to a normalized value. Number is the value to be standardized. Mean is the arithmetic mean of the distribution. STDEV is the standard deviation of the distribution.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | STANDARDIZE |

The identifier for this plugin is `Excel_STANDARDIZE`.

It can be found in the package `com.eccenca.di.excel`.



#### Stdev

Excel STDEV(number_1; number_2; ... number_30): Estimates the standard deviation based on a sample. Number_1; number_2; ... number_30 are numerical values or ranges representing a sample based on an entire population.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | STDEV |

The identifier for this plugin is `Excel_STDEV`.

It can be found in the package `com.eccenca.di.excel`.



#### Stdeva

Excel STDEVA(value_1; value_2; ... value_30): Calculates the standard deviation of an estimation based on a sample. Value_1; value_2; ... value_30 are values or ranges representing a sample derived from an entire population. Text has the value 0.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | STDEVA |

The identifier for this plugin is `Excel_STDEVA`.

It can be found in the package `com.eccenca.di.excel`.



#### Stdevp

Excel STDEVP(number_1; number_2; ... number_30): Calculates the standard deviation based on the entire population. Number_1; number_2; ... number_30 are numerical values or ranges representing a sample based on an entire population.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | STDEVP |

The identifier for this plugin is `Excel_STDEVP`.

It can be found in the package `com.eccenca.di.excel`.



#### Stdevpa

Excel STDEVPA(value_1; value_2; ... value_30): Calculates the standard deviation based on the entire population. Value_1; value_2; ... value_30 are values or ranges representing a sample derived from an entire population. Text has the value 0.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | STDEVPA |

The identifier for this plugin is `Excel_STDEVPA`.

It can be found in the package `com.eccenca.di.excel`.



#### Substitute

Excel SUBSTITUTE(text; search_text; new text; occurrence): Substitutes new text for old text in a string. Text is the text in which text segments are to be exchanged. Search_text is the text segment that is to be replaced (a number of times). New text is the text that is to replace the text segment. Occurrence (optional) indicates how many occurrences of the search text are to be replaced. If this parameter is missing, the search text is replaced throughout.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUBSTITUTE |

The identifier for this plugin is `Excel_SUBSTITUTE`.

It can be found in the package `com.eccenca.di.excel`.



#### Sum

Excel SUM(number_1; number_2; ... number_30): Adds all the numbers in a range of cells. Number_1; number_2;... number_30 are up to 30 arguments whose sum is to be calculated. You can also enter a range using cell references.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUM |

The identifier for this plugin is `Excel_SUM`.

It can be found in the package `com.eccenca.di.excel`.



#### Sumproduct

Excel SUMPRODUCT(array 1; array 2; ...array 30): Multiplies corresponding elements in the given arrays, and returns the sum of those products. Array 1; array 2;...array 30 are arrays whose corresponding elements are to be multiplied. At least one array must be part of the argument list. If only one array is given, all array elements are summed.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUMPRODUCT |

The identifier for this plugin is `Excel_SUMPRODUCT`.

It can be found in the package `com.eccenca.di.excel`.



#### Sumsq

Excel SUMSQ(number_1; number_2; ... number_30): Calculates the sum of the squares of numbers (totaling up of the squares of the arguments) Number_1; number_2;... number_30 are up to 30 arguments, the sum of whose squares is to be calculated.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUMSQ |

The identifier for this plugin is `Excel_SUMSQ`.

It can be found in the package `com.eccenca.di.excel`.



#### Sumx2my2

Excel SUMX2MY2(array_X; array_Y): Returns the sum of the difference of squares of corresponding values in two arrays. Array_X is the first array whose elements are to be squared and added. Array_Y is the second array whose elements are to be squared and subtracted.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUMX2MY2 |

The identifier for this plugin is `Excel_SUMX2MY2`.

It can be found in the package `com.eccenca.di.excel`.



#### Sumx2py2

Excel SUMX2PY2(array_X; array_Y): Returns the sum of the sum of squares of corresponding values in two arrays. Array_X is the first array whose arguments are to be squared and added. Array_Y is the second array, whose elements are to be added and squared.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUMX2PY2 |

The identifier for this plugin is `Excel_SUMX2PY2`.

It can be found in the package `com.eccenca.di.excel`.



#### Sumxmy2

Excel SUMXMY2(array_X; array_Y): Adds the squares of the variance between corresponding values in two arrays. Array_X is the first array whose elements are to be subtracted and squared. Array_Y is the second array, whose elements are to be subtracted and squared.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | SUMXMY2 |

The identifier for this plugin is `Excel_SUMXMY2`.

It can be found in the package `com.eccenca.di.excel`.



#### Tan

Excel TAN(number): Returns the tangent of the given number (angle in radians).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | TAN |

The identifier for this plugin is `Excel_TAN`.

It can be found in the package `com.eccenca.di.excel`.



#### Tanh

Excel TANH(number): Returns the hyperbolic tangent of the given number (angle in radians).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | TANH |

The identifier for this plugin is `Excel_TANH`.

It can be found in the package `com.eccenca.di.excel`.



#### Tdist

Excel TDIST(number; degrees_freedom; mode): Returns the t-distribution for the given Number. Degrees_freedom is the number of degrees of freedom for the t-distribution. Mode = 1 returns the one-tailed test, Mode = 2 returns the two-tailed test.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | TDIST |

The identifier for this plugin is `Excel_TDIST`.

It can be found in the package `com.eccenca.di.excel`.



#### True

Excel TRUE(): Sets the logical value to TRUE. The TRUE() function does not require any arguments.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | TRUE |

The identifier for this plugin is `Excel_TRUE`.

It can be found in the package `com.eccenca.di.excel`.



#### Trunc

Excel TRUNC(number; count): Truncates a number to an integer by removing the fractional part of the number according to the precision specified in Tools > Options > OpenOffice.org Calc > Calculate. Number is the number whose decimal places are to be cut off. Count is the number of decimal places which are not cut off.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | TRUNC |

The identifier for this plugin is `Excel_TRUNC`.

It can be found in the package `com.eccenca.di.excel`.



#### Var

Excel VAR(number_1; number_2; ... number_30): Estimates the variance based on a sample. Number_1; number_2; ... number_30 are numerical values or ranges representing a sample based on an entire population.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | VAR |

The identifier for this plugin is `Excel_VAR`.

It can be found in the package `com.eccenca.di.excel`.



#### Vara

Excel VARA(value_1; value_2; ... value_30): Estimates a variance based on a sample. The value of text is 0. Value_1; value_2; ... value_30 are values or ranges representing a sample derived from an entire population. Text has the value 0.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | VARA |

The identifier for this plugin is `Excel_VARA`.

It can be found in the package `com.eccenca.di.excel`.



#### Varp

Excel VARP(Number_1; number_2; ... number_30): Calculates a variance based on the entire population. Number_1; number_2; ... number_30 are numerical values or ranges representing an entire population.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | VARP |

The identifier for this plugin is `Excel_VARP`.

It can be found in the package `com.eccenca.di.excel`.



#### Varpa

Excel VARPA(value_1; value_2; .. .value_30): Calculates the variance based on the entire population. The value of text is 0. Value_1; value_2; ... value_30 are values or ranges representing an entire population.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| functionName | String | The name of the Excel function | VARPA |

The identifier for this plugin is `Excel_VARPA`.

It can be found in the package `com.eccenca.di.excel`.



### Extract

#### Regex extract

Extracts occurrences of a regex "regex" in a string. If there is at least one capture group, it will return the string of the first capture group instead.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| regex | String | Regular expression | *no default* |
| extractAll | boolean | If true, all matches are extracted. If false, only the first match is extracted. | false |

The identifier for this plugin is `regexExtract`.

It can be found in the package `org.silkframework.rule.plugins.transformer.extraction`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### returns the first match:

* Parameters
  * *regex*: `[a-z]{2,4}123`

* Input values:
  1. `[afe123_abc123]`

* Returns:

  → `[afe123]`


---
##### returns all matches, if extractAll = true:

* Parameters
  * *regex*: `[a-z]{2,4}123`
  * *extractAll*: `true`

* Input values:
  1. `[afe123_abc123]`

* Returns:

  → `[afe123, abc123]`


---
##### returns an empty list if nothing matches:

* Parameters
  * *regex*: `^[a-z]{2,4}123`

* Input values:
  1. `[abcdef123]`

* Returns:

  → `[]`


---
##### returns the match of the first capture group that matches:

* Parameters
  * *regex*: `^([a-z]{2,4})123([a-z]+)`

* Input values:
  1. `[abcd123xyz]`

* Returns:

  → `[abcd]`


---
##### Example 5:

* Parameters
  * *regex*: `"bedeutungen"\s*:\s*\[\s*(?:"([^"]*)"(?:\s*,\s*"([^"]*)")*)*\s*\]`

* Input values:
  1. `["bedeutungen" : [ ]]`

* Returns:

  → `[]`

### Filter

#### Filter by length

Removes all strings that are shorter than 'min' characters and longer than 'max' characters.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| min | int | No description | 0 |
| max | int | No description | 2147483647 |

The identifier for this plugin is `filterByLength`.

It can be found in the package `org.silkframework.rule.plugins.transformer.filter`.



#### Filter by regex

Removes all strings that do NOT match a regex. If 'negate' is true, only strings will be removed that match the regex.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| regex | String | No description | *no default* |
| negate | boolean | No description | false |

The identifier for this plugin is `filterByRegex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.filter`.



#### Remove empty values

Removes empty values.

This plugin does not require any parameters.
The identifier for this plugin is `removeEmptyValues`.

It can be found in the package `org.silkframework.rule.plugins.transformer.filter`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[value1, , value2]`

* Returns:

  → `[value1, value2]`


---
##### Example 2:

* Input values:
  1. `[, ]`

* Returns:

  → `[]`

#### Remove stopwords (remote stopword list)

Removes stopwords from all values. The stopword list is retrieved via a http connection (e.g. https://sites.google.com/site/kevinbouge/stopwords-lists/stopwords_de.txt). Each line in the stopword list contains a stopword. The separator defines a regex that is used for detecting words.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| stopWordListUrl | String | No description | *no default* |
| separator | String | No description | [\\s-]+ |

The identifier for this plugin is `removeRemoteStopwords`.

It can be found in the package `org.silkframework.rule.plugins.transformer.filter`.



#### Remove stopwords

Removes stopwords from all values. Each line in the stopword list contains a stopword. The separator defines a regex that is used for detecting words.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| stopwordList | Resource | No description | *no default* |
| separator | String | No description | [\\s-]+ |

The identifier for this plugin is `removeStopwords`.

It can be found in the package `org.silkframework.plugins.filter`.



#### Remove values

Removes values that contain words from a blacklist. The blacklist values are separated with commas.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| blacklist | String | No description | *no default* |

The identifier for this plugin is `removeValues`.

It can be found in the package `org.silkframework.rule.plugins.transformer.filter`.



### Geo

#### Retrieve coordinates

Retrieves geographic coordinates using Nominatim.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| additionalParameters | String | Additional URL parameters to be attached to each HTTP search request. Example: '&countrycodes=de&addressdetails=1'. Consult the API documentation for a list of available parameters. | *empty string* |

The identifier for this plugin is `RetrieveCoordinates`.

It can be found in the package `com.eccenca.di.geo`.


**Configuration**

The geocoding service to be queried for searches can be set up in the configuration.
The default configuration is as follows:

    com.eccenca.di.geo = {
      # The URL of the geocoding service
      # url = "https://nominatim.eccenca.com/search"
      url = "https://photon.komoot.de/api"
      # url = https://api-adresse.data.gouv.fr/search

      # Additional URL parameters to be attached to all HTTP search requests. Example: '&countrycodes=de&addressdetails=1'.
      # Will be attached in addition to the parameters set on each search operator directly.
      searchParameters = ""

      # The minimum pause time between subsequent queries
      pauseTime = 1s

      # Number of coordinates to be cached in-memory
      cacheSize = 10
    }

In general, all services adhering to the [Nominatim search API](https://nominatim.org/release-docs/develop/api/Search/) should be usable.
Please note that when using public services, the pause time should be set to avoid overloading.

**Logging**

By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:

    logging.level {
      com.eccenca.di.geo=DEBUG
    }

#### Retrieve latitude

Retrieves geographic coordinates using Nominatim and returns the latitude.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| additionalParameters | String | Additional URL parameters to be attached to each HTTP search request. Example: '&countrycodes=de&addressdetails=1'. Consult the API documentation for a list of available parameters. | *empty string* |

The identifier for this plugin is `RetrieveLatitude`.

It can be found in the package `com.eccenca.di.geo`.


**Configuration**

The geocoding service to be queried for searches can be set up in the configuration.
The default configuration is as follows:

    com.eccenca.di.geo = {
      # The URL of the geocoding service
      # url = "https://nominatim.eccenca.com/search"
      url = "https://photon.komoot.de/api"
      # url = https://api-adresse.data.gouv.fr/search

      # Additional URL parameters to be attached to all HTTP search requests. Example: '&countrycodes=de&addressdetails=1'.
      # Will be attached in addition to the parameters set on each search operator directly.
      searchParameters = ""

      # The minimum pause time between subsequent queries
      pauseTime = 1s

      # Number of coordinates to be cached in-memory
      cacheSize = 10
    }

In general, all services adhering to the [Nominatim search API](https://nominatim.org/release-docs/develop/api/Search/) should be usable.
Please note that when using public services, the pause time should be set to avoid overloading.

**Logging**

By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:

    logging.level {
      com.eccenca.di.geo=DEBUG
    }

#### Retrieve longitude

Retrieves geographic coordinates using Nominatim and returns the longitude.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| additionalParameters | String | Additional URL parameters to be attached to each HTTP search request. Example: '&countrycodes=de&addressdetails=1'. Consult the API documentation for a list of available parameters. | *empty string* |

The identifier for this plugin is `RetrieveLongitude`.

It can be found in the package `com.eccenca.di.geo`.


**Configuration**

The geocoding service to be queried for searches can be set up in the configuration.
The default configuration is as follows:

    com.eccenca.di.geo = {
      # The URL of the geocoding service
      # url = "https://nominatim.eccenca.com/search"
      url = "https://photon.komoot.de/api"
      # url = https://api-adresse.data.gouv.fr/search

      # Additional URL parameters to be attached to all HTTP search requests. Example: '&countrycodes=de&addressdetails=1'.
      # Will be attached in addition to the parameters set on each search operator directly.
      searchParameters = ""

      # The minimum pause time between subsequent queries
      pauseTime = 1s

      # Number of coordinates to be cached in-memory
      cacheSize = 10
    }

In general, all services adhering to the [Nominatim search API](https://nominatim.org/release-docs/develop/api/Search/) should be usable.
Please note that when using public services, the pause time should be set to avoid overloading.

**Logging**

By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:

    logging.level {
      com.eccenca.di.geo=DEBUG
    }

### Linguistic

#### NYSIIS

NYSIIS phonetic encoding.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| refined | boolean | No description | true |

The identifier for this plugin is `NYSIIS`.

It can be found in the package `org.silkframework.rule.plugins.transformer.linguistic`.



#### Metaphone

Metaphone phonetic encoding.

This plugin does not require any parameters.
The identifier for this plugin is `metaphone`.

It can be found in the package `org.silkframework.rule.plugins.transformer.linguistic`.



#### Normalize chars

Replaces diacritical characters with non-diacritical ones (eg, ö -> o), plus some specialities like transforming æ -> ae, ß -> ss.

This plugin does not require any parameters.
The identifier for this plugin is `normalizeChars`.

It can be found in the package `org.silkframework.rule.plugins.transformer.linguistic`.



#### Soundex

Soundex algorithm.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| refined | boolean | No description | true |

The identifier for this plugin is `soundex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.linguistic`.



#### Stem

Stems a string using the Porter Stemmer.

This plugin does not require any parameters.
The identifier for this plugin is `stem`.

It can be found in the package `org.silkframework.rule.plugins.transformer.linguistic`.



### Metadata

#### File hash

Calculates the hash sum of a file. The hash sum is cached so that subsequent calls to this operator are fast.
Note that initially and every time the specified resource has been updated, this operator might take a long time (depending on the file size).
This operator supports using different hash algorithms from the [Secure Hash Algorithms family](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) (SHA, e.g. SHA256) and two algorithms from the [Message-Digest Algorithm family](https://en.wikipedia.org/wiki/MD5) (MD2 / MD5). Please be aware that some of these algorithms are not secure regarding collision- and other attacks.
Note: This transform operator ignores any inputs.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| file | ResourceOption | File for which the hash sum will be calculated. If left empty, the file of the input dataset is used. |  |
| algorithm | String | The hash algorithm to be used. | SHA256 |

The identifier for this plugin is `fileHash`.

It can be found in the package `org.silkframework.rule.plugins.transformer.metadata`.



#### Input file attributes

Retrieves a metadata attribute from the input file (such as the file name).

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| attribute | Enum | File attribute to be retrieved from the input dataset. | name |

The identifier for this plugin is `inputFileAttributes`.

It can be found in the package `org.silkframework.rule.plugins.transformer.metadata`.



#### Input task attributes

Retrieves individual attributes from the input task (such as the modified date) or the entire task as JSON.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| path | String | Path to retrieve from the JSON, such as 'metadata/modified'. If left empty, the entire JSON will be returned. | *empty string* |

The identifier for this plugin is `inputTaskAttributes`.

It can be found in the package `org.silkframework.serialization.json.transformer`.



### Normalize

#### Strip non-alphabetic characters

Strips all non-alphabetic characters from a string. Spaces are retained.

This plugin does not require any parameters.
The identifier for this plugin is `alphaReduce`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Camel case

Converts a string to camel case. Upper camel case is the default, lower camel case can be chosen.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| isDromedary | boolean | If true, lower camel case (aka. dromedary case) is used, otherwise upper camel case is used. | false |

The identifier for this plugin is `camelCase`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### A sentence with several words is converted to a single word written in UpperCamelCase:

* Parameters
  * *isDromedary*: `false`

* Input values:
  1. `[hello world]`

* Returns:

  → `[HelloWorld]`


---
##### A sentence with several words is converted to a single word written in lowerCamelCase:

* Parameters
  * *isDromedary*: `true`

* Input values:
  1. `[hello world]`

* Returns:

  → `[helloWorld]`


---
##### A single lowercase letter is converted to UpperCamelCase, i.e. capitalized:

* Parameters
  * *isDromedary*: `false`

* Input values:
  1. `[h]`

* Returns:

  → `[H]`


---
##### A single lowercase letter is converted to lowerCamelCase (aka. dromedary case), i.e. uncapitalized:

* Parameters
  * *isDromedary*: `true`

* Input values:
  1. `[h]`

* Returns:

  → `[h]`


---
##### An empty space is removed. The dromedary/lower case is irrelevant here:

* Parameters
  * *isDromedary*: `true`

* Input values:
  1. `[ ]`

* Returns:

  → `[]`


---
##### An empty space is removed. The upper case is irrelevant here:

* Parameters
  * *isDromedary*: `false`

* Input values:
  1. `[ ]`

* Returns:

  → `[]`

#### Capitalize

Capitalizes the string i.e. converts the first character to upper case. If 'allWords' is set to true, all words are capitalized and not only the first character.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| allWords | boolean | No description | false |

The identifier for this plugin is `capitalize`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *allWords*: `false`

* Input values:
  1. `[capitalize me]`

* Returns:

  → `[Capitalize me]`


---
##### Example 2:

* Parameters
  * *allWords*: `true`

* Input values:
  1. `[capitalize me]`

* Returns:

  → `[Capitalize Me]`

#### Extract physical quantity

Extracts physical quantities, such as length or weight values.
Values are expected of the form '{Number}{UnitPrefix}{Symbol}' and are converted to the base unit.

Example:

- Given a value '10km, 3mg'.
- If the symbol parameter is set to 'm', the extracted value is 10000.
- If the symbol parameter is set to 'g', the extracted value is 0.001.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| symbol | String | The symbol of the dimension, e.g., 'm' for meter. | *empty string* |
| numberFormat | String | The IETF BCP 47 language tag, e.g. 'en'. | en |
| filter | String | Only extracts from values that contain the given regex (case-insensitive). | *empty string* |
| index | int | If there are multiple matches, retrieve the value with the given index (zero-based). | 0 |

The identifier for this plugin is `extractPhysicalQuantity`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.



#### Clean HTML

Cleans HTML using a tag white list and allows selection of HTML sections with XPath or CSS selector expressions.
       If the tag or attribute white lists are left empty default white lists will be used (this behaviour can be changed).
       To remove all HTML markup and retain text, keep the defaults and turn off the "Default tags and attributes" toggle.
       The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| tagWhiteList | StringIterableParameter | Tags to keep in the cleaned output. |  |
| attributeWhiteList | StringIterableParameter | Attributes to keep in the cleaned output. |  |
| selectors | StringIterableParameter | CSS or XPath queries for selection of content. CSS selectors can be pipe separated for non-sequential execution. |  |
| method | Enum | Selects use of XPath or CSS selectors. | xPath |
| defaultTagsAndAttributes | boolean | Use defaults for empty tag and attribute whitelists.\If the attribute while list is empty, it will default to: "class", "id", "href", "src"\If the tag while list is empty, it will default to: "a", "b", "blockquote", "br", "caption", "cite", "code", "col", "colgroup", "dd", "div", "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6","i", "img", "li", "ol", "p", "pre", "q", "small", "span", "strike", "strong","sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul". | true |

The identifier for this plugin is `htmlCleaner`.

It can be found in the package `com.eccenca.di.plugins.html`.



#### Lower case

Converts a string to lower case.

This plugin does not require any parameters.
The identifier for this plugin is `lowerCase`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Transforms all values to lower case:

* Input values:
  1. `[JoHN, LeNA]`

* Returns:

  → `[john, lena]`

#### Remove blanks

Remove whitespace from a string.

This plugin does not require any parameters.
The identifier for this plugin is `removeBlanks`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Remove duplicates

Removes duplicated values, making a value sequence distinct.

This plugin does not require any parameters.
The identifier for this plugin is `removeDuplicates`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Remove parentheses

Remove all parentheses including their content, e.g., transforms 'Berlin (City)' -> 'Berlin'.

This plugin does not require any parameters.
The identifier for this plugin is `removeParentheses`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Remove special chars

Remove special characters (including punctuation) from a string.

This plugin does not require any parameters.
The identifier for this plugin is `removeSpecialChars`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Sort words

Sorts all words in each value lexicographically.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| splitRegex | String | The regular expression used to split values into words. | \\s+ |
| glue | String | Separator to be inserted between sorted words. |   |

The identifier for this plugin is `sortWords`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[]`

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[c a b]`

* Returns:

  → `[a b c]`


---
##### Example 3:

* Input values:
  1. `[Hans Hansa    Hamburg, München Marburg]`

* Returns:

  → `[Hamburg Hans Hansa, Marburg München]`

#### Strip URI prefix

Strips the URI prefix and decodes the remainder. Leaves values unchanged which are not a valid URI.

This plugin does not require any parameters.
The identifier for this plugin is `stripUriPrefix`.

It can be found in the package `org.silkframework.rule.plugins.transformer.substring`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[http://example.org/some/path/to/value]`

* Returns:

  → `[value]`


---
##### Example 2:

* Input values:
  1. `[urn:scheme:value]`

* Returns:

  → `[value]`


---
##### Example 3:

* Input values:
  1. `[http://example.org/some/path/to/encoded%20v%C3%A4lue]`

* Returns:

  → `[encoded välue]`


---
##### Example 4:

* Input values:
  1. `[value]`

* Returns:

  → `[value]`

#### Trim

Remove leading and trailing whitespaces.

This plugin does not require any parameters.
The identifier for this plugin is `trim`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Upper case

Converts a string to upper case.

This plugin does not require any parameters.
The identifier for this plugin is `upperCase`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Fix URI

Generates valid absolute URIs from the given values. Already valid absolute URIs are left untouched.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| uriPrefix | String | No description | urn:url-encoded-value: |

The identifier for this plugin is `uriFix`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Non-absolute URIs are prefixed with the configured URI prefix:

* Input values:
  1. `[ab]`

* Returns:

  → `[urn:url-encoded-value:ab]`


---
##### URI reserved characters are encoded:

* Input values:
  1. `[a&b]`

* Returns:

  → `[urn:url-encoded-value:a%26b]`


---
##### Valid absolute URIs are forwarded unchanged:

* Input values:
  1. `[http://example.org/some/path]`

* Returns:

  → `[http://example.org/some/path]`


---
##### Query parameters and fragments are left unchanged:

* Input values:
  1. `[http://example.org/path?query=some+stuff#hashtag]`

* Returns:

  → `[http://example.org/path?query=some+stuff#hashtag]`


---
##### Valid URNs are forwarded unchanged:

* Input values:
  1. `[urn:valid:uri]`

* Returns:

  → `[urn:valid:uri]`


---
##### Special characters are encoded:

* Input values:
  1. `[http://www.broken domain.com/broken weird path äöü/nice/path/andNowSomeFragment#fragmentäöü]`

* Returns:

  → `[http://www.broken%20domain.com/broken%20weird%20path%20%C3%A4%C3%B6%C3%BC/nice/path/andNowSomeFragment#fragment%C3%A4%C3%B6%C3%BC]`


---
##### Hash signs are only encoded if they don't denote a fragment:

* Input values:
  1. `[http://domain/##path#]`

* Returns:

  → `[http://domain/#%23path%23]`


---
##### Invalid URIs are fully encoded:

* Input values:
  1. `[http : invalid URI]`

* Returns:

  → `[urn:url-encoded-value:http+%3A+invalid+URI]`


---
##### Leading and trailing spaces are removed:

* Input values:
  1. `[  http://domain.com/[squareBrackets] ]`

* Returns:

  → `[http://domain.com/%5BsquareBrackets%5D]`


---
##### Example 10:

* Input values:
  1. `[100%]`

* Returns:

  → `[urn:url-encoded-value:100%25]`

#### Encode URL

URL encodes the string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| encoding | String | The character encoding. | UTF-8 |

The identifier for this plugin is `urlEncode`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[ab]`

* Returns:

  → `[ab]`


---
##### Example 2:

* Input values:
  1. `[a&b]`

* Returns:

  → `[a%26b]`


---
##### Example 3:

* Input values:
  1. `[http://example.org/some/path]`

* Returns:

  → `[http%3A%2F%2Fexample.org%2Fsome%2Fpath]`

### Numeric

#### Normalize physical quantity

Normalizes physical quantities.
Can either convert to a configured unit or to SI base units.
For instance for lengths, values will be converted to metres if no target unit is configured.
Will output the pure numeric value without the unit.
If one input is provided, the physical quantities are parsed from the provided strings of the form "1 km".
If two inputs are provided, the numeric values are parsed from the first input and the units are parsed from the second inputs.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| targetUnit | String | Target unit. Can be left empty to convert to the respective SI base units. | *empty string* |
| numberFormat | String | The IETF BCP 47 language tag, e.g., 'en'. | en |

The identifier for this plugin is `PhysicalQuantitiesNormalizer`.

It can be found in the package `com.eccenca.di.measure`.

SI units and common derived units are supported. The following section lists all supported units. By default, all quantities are normalized to their base unit. For instance, lengths will be normalized to metres.
##### Supported units

##### Time

Time is expressed in seconds (symbol: `s`).
The following alternative symbols are supported:
* `mo_s`: day*29.53059
* `mo_g`: year/12.0
* `a`: day*365.25
* `min`: min
* `a_g`: year
* `mo`: (day*365.25)/12.0
* `mo_j`: (day*365.25)/12.0
* `a_j`: day*365.25
* `h`: h
* `a_t`: day*365.24219
* `d`: day


##### Length

Length is expressed in metres (symbol: `m`).
The following alternative symbols are supported:
* `in`: c(cm*254.0)
* `nmi`: m*1852.0
* `Ao`: dnm
* `mil`: m(c(cm*254.0))
* `yd`: ((c(cm*254.0))*12.0)*3.0
* `AU`: m*1.49597871E11
* `ft`: (c(cm*254.0))*12.0
* `pc`: m*3.085678E16
* `fth`: ((c(cm*254.0))*12.0)*6.0
* `mi`: ((c(cm*254.0))*12.0)*5280.0
* `hd`: (c(cm*254.0))*4.0


##### Mass

Mass is expressed in kilograms (symbol: `kg`).
The following alternative symbols are supported:
* `lb`: lb
* `ston`: hlb*20.0
* `t`: Mg
* `stone`: lb*14.0
* `u`: AMU
* `gr`: (mg*6479891.0)/100000.0
* `lcwt`: lb*112.0
* `oz`: oz
* `g`: g
* `scwt`: hlb
* `dr`: oz/16.0
* `lton`: (lb*112.0)*20.0


##### Electric current

Electric current is expressed in amperes (symbol: `A`).
The following alternative symbols are supported:
* `Bi`: daA
* `Gb`: cm·(A/m)*250.0/[one?]


##### Temperature

Temperature is expressed in kelvins (symbol: `K`).
The following alternative symbols are supported:
* `Cel`: ℃


##### Amount of substance

Amount of substance is expressed in moles (symbol: `mol`).

##### Luminous intensity

Luminous intensity is expressed in candelas (symbol: `cd`).

##### Area

Area is expressed in square metres (symbol: `m²`).
The following alternative symbols are supported:
* `m2`: m²
* `ar`: hm²
* `syd`: ((c(cm*254.0))*12.0)*3.0²
* `cml`: [one?]/4.0·m(c(cm*254.0))²
* `b`: hfm²
* `sft`: (c(cm*254.0))*12.0²
* `sin`: c(cm*254.0)²


##### Volume

Volume is expressed in cubic metres (symbol: `㎥`).
The following alternative symbols are supported:
* `st`: [㎥?]
* `bf`: (c(cm*254.0)³)*144.0
* `cyd`: ((c(cm*254.0))*12.0)*3.0³
* `cr`: ((c(cm*254.0))*12.0³)*128.0
* `L`: L
* `l`: l
* `cin`: c(cm*254.0)³
* `cft`: (c(cm*254.0))*12.0³
* `m3`: ㎥


##### Energy

Energy is expressed in joules (symbol: `J`).
The following alternative symbols are supported:
* `cal_IT`: (J*41868.0)/10000.0
* `eV`: J*1.602176487E-19
* `cal_m`: (J*419002.0)/100000.0
* `cal`: m(J*4184.0)
* `cal_th`: m(J*4184.0)


##### Angle

Angle is expressed in radians (symbol: `rad`).
The following alternative symbols are supported:
* `circ`: [one?]·rad*2.0
* `gon`: ([one?]·rad/180.0)*0.9
* `deg`: [one?]·rad/180.0
* `'`: ([one?]·rad/180.0)/60.0
* `''`: (([one?]·rad/180.0)/60.0)/60.0


##### Others

- `1/m`, derived units: `Ky`: c(1/m)
- `kg/(m·s)`, derived units: `P`: g/(s·cm)
- `bit/s`, derived units: `Bd`: bit/s
- `bit`, derived units: `By`: bit*8.0
- `Sv`
- `N`
- `Ω`, derived units: `Ohm`: Ω
- `T`, derived units: `G`: T/10000.0
- `sr`, derived units: `sph`: [one?]·sr*4.0
- `F`
- `C/kg`, derived units: `R`: (C/kg)*2.58E-4
- `cd/m²`, derived units: `sb`: cd/cm², `Lmb`: cd/([one?]·cm²)
- `Pa`, derived units: `bar`: Pa*100000.0, `atm`: Pa*101325.0
- `kg/(m·s²)`, derived units: `att`: k(g·(m/s²)*9.80665)/cm²
- `m²/s`, derived units: `St`: cm²/s
- `A/m`, derived units: `Oe`: (A/m)*250.0/[one?]
- `kg·m²/s²`, derived units: `erg`: cm²·g/s²
- `kg/m³`, derived units: `g%`: g/dl
- `mho`
- `V`
- `lx`, derived units: `ph`: lx/10000.0
- `m/s²`, derived units: `Gal`: cm/s², `m/s2`: m/s²
- `m/s`, derived units: `kn`: m*1852.0/h
- `m·kg/s²`, derived units: `gf`: g·(m/s²)*9.80665, `lbf`: lb·(m/s²)*9.80665, `dyn`: cm·g/s²
- `m²/s²`, derived units: `RAD`: cm²·g/(s²·hg), `REM`: cm²·g/(s²·hg)
- `C`
- `Gy`
- `Hz`
- `H`
- `lm`
- `W`
- `Wb`, derived units: `Mx`: Wb/1.0E8
- `Bq`, derived units: `Ci`: Bq*3.7E10
- `S`


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[1 km]`

* Returns:

  → `[1000.0]`


---
##### Example 2:

* Input values:
  1. `[1.0000     ft]`

* Returns:

  → `[0.3048]`


---
##### Example 3:

* Input values:
  1. `[1.0lb]`

* Returns:

  → `[0.45359237]`


---
##### Example 4:

* Input values:
  1. `[1000000000.0 nm]`

* Returns:

  → `[1.0]`


---
##### Example 5:

* Input values:
  1. `[-1E6 m]`

* Returns:

  → `[-1000000.0]`


---
##### Example 6:

* Parameters
  * *numberFormat*: `de`

* Input values:
  1. `[1.000,5 m]`

* Returns:

  → `[1000.5]`


---
##### Example 7:

* Input values:
  1. `[1,000.5 m]`

* Returns:

  → `[1000.5]`


---
##### Example 8:

* Parameters
  * *targetUnit*: `mi`

* Input values:
  1. `[1 km]`

* Returns:

  → `[0.621371192237334]`


---
##### Example 9:

* Parameters
  * *targetUnit*: `m`

* Input values:
  1. `[1 kg]`

* Returns:

  → `[]`


---
##### Example 10:

* Input values:
  1. `[100.0]`

* Returns:

  → `[]`


---
##### Example 11:

* Input values:
  1. `[1]`
  2. `[km]`

* Returns:

  → `[1000.0]`


---
##### Example 12:

* Input values:
  1. `[1, 10000]`
  2. `[km, mm]`

* Returns:

  → `[1000.0, 10.0]`


---
##### Example 13:

* Input values:
  1. `[1, 10000, 10]`
  2. `[km, mm]`

* Returns:

  → `[]`

#### Aggregate numbers

Aggregates all numbers in this set using a mathematical operation.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| operator | String | One of '+', '*', 'min', 'max', 'average'. | *no default* |

The identifier for this plugin is `aggregateNumbers`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.



#### Compare numbers

Compares the numbers of two sets.
Returns 1 if the comparison yields true and 0 otherwise.
If there are multiple numbers in both sets, the comparator must be true for all numbers.
For instance, {1,2} < {2,3} yields 0 as not all numbers in the first set are smaller than in the second.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| comparator | Enum | No description | < |

The identifier for this plugin is `compareNumbers`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.



#### Count values

Counts the number of values.

This plugin does not require any parameters.
The identifier for this plugin is `count`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[value1]`

* Returns:

  → `[1]`


---
##### Example 2:

* Input values:
  1. `[value1, value2]`

* Returns:

  → `[2]`

#### Extract physical quantity

Extracts physical quantities, such as length or weight values.
Values are expected of the form '{Number}{UnitPrefix}{Symbol}' and are converted to the base unit.

Example:

- Given a value '10km, 3mg'.
- If the symbol parameter is set to 'm', the extracted value is 10000.
- If the symbol parameter is set to 'g', the extracted value is 0.001.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| symbol | String | The symbol of the dimension, e.g., 'm' for meter. | *empty string* |
| numberFormat | String | The IETF BCP 47 language tag, e.g. 'en'. | en |
| filter | String | Only extracts from values that contain the given regex (case-insensitive). | *empty string* |
| index | int | If there are multiple matches, retrieve the value with the given index (zero-based). | 0 |

The identifier for this plugin is `extractPhysicalQuantity`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.



#### Format number


  Formats a number according to a user-defined pattern.
  The pattern syntax is documented at:
  https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| pattern | String | No description | *no default* |
| locale | String | No description | en |

The identifier for this plugin is `formatNumber`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *pattern*: `000`

* Input values:
  1. `[1]`

* Returns:

  → `[001]`


---
##### Example 2:

* Parameters
  * *pattern*: `000000.000`

* Input values:
  1. `[123.78]`

* Returns:

  → `[000123.780]`


---
##### Example 3:

* Parameters
  * *pattern*: `###,###.###`

* Input values:
  1. `[123456.789]`

* Returns:

  → `[123,456.789]`


---
##### Example 4:

* Parameters
  * *pattern*: `###.###,###`
  * *locale*: `de`

* Input values:
  1. `[123456.789]`

* Returns:

  → `[123.456,789]`


---
##### Example 5:

* Parameters
  * *pattern*: `# apples`

* Input values:
  1. `[10]`

* Returns:

  → `[10 apples]`


---
##### Example 6:

* Parameters
  * *pattern*: `000'0'`

* Input values:
  1. `[1]`

* Returns:

  → `[0010]`


---
##### Example 7:

* Parameters
  * *pattern*: `0`

* Input values:
  1. `[1.0]`

* Returns:

  → `[1]`


---
##### Example 8:

* Parameters
  * *pattern*: `0.0`

* Input values:
  1. `[0000123.4]`

* Returns:

  → `[123.4]`

#### Logarithm

Transforms all numbers by applying the logarithm function. Non-numeric values are left unchanged.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| base | int | No description | 10 |

The identifier for this plugin is `log`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.



#### Numeric operation

 Applies a numeric operation to the values of multiple input operators.
 Uses double-precision floating-point numbers for computation.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| operator | String | The operator to be applied to all values. One of '+', '-', '*', '/' | *no default* |

The identifier for this plugin is `numOperation`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *operator*: `+`

* Input values:
  1. `[1]`
  2. `[1]`

* Returns:

  → `[2.0]`


---
##### Example 2:

* Parameters
  * *operator*: `-`

* Input values:
  1. `[1]`
  2. `[1]`

* Returns:

  → `[0.0]`


---
##### Example 3:

* Parameters
  * *operator*: `*`

* Input values:
  1. `[5]`
  2. `[6]`

* Returns:

  → `[30.0]`


---
##### Example 4:

* Parameters
  * *operator*: `/`

* Input values:
  1. `[5]`
  2. `[2]`

* Returns:

  → `[2.5]`


---
##### Example 5:

* Parameters
  * *operator*: `+`

* Input values:
  1. `[1]`
  2. `[no number]`

* Returns:

  → `[]`


---
##### Example 6:

* Parameters
  * *operator*: `*`

* Input values:
  1. `[1]`
  2. `[]`

* Returns:

  → `[1.0]`


---
##### Example 7:

* Parameters
  * *operator*: `+`

* Input values:
  1. `[1, 1]`
  2. `[1]`

* Returns:

  → `[3.0]`

#### Numeric reduce

Strip all non-numeric characters from a string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| keepPunctuation | boolean | No description | true |

The identifier for this plugin is `numReduce`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *keepPunctuation*: `false`

* Input values:
  1. `[some1.2Value]`

* Returns:

  → `[12]`


---
##### Example 2:

* Parameters
  * *keepPunctuation*: `true`

* Input values:
  1. `[some1.2Value]`

* Returns:

  → `[1.2]`

### Parser

#### Parse date

Parses and normalizes dates in different formats.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| inputDateFormatId | Option | The input date/time format used for parsing the date/time string. | w3c Date |
| alternativeInputFormat | String | An input format string that should be used instead of the selected input format. Java DateFormat string. | *empty string* |
| inputLocale | LocaleOptionParameter | Optional locale for the (alternative) input format. If not set the system's locale will be used or the locale of the input format, if set. |  |
| outputDateFormatId | Option | The output date/time format used for parsing the date/time string. | w3c Date |
| alternativeOutputFormat | String | An output format string that should be used instead of the selected output format. Java DateFormat string. | *empty string* |
| outputLocale | LocaleOptionParameter | Optional locale for the (alternative) output format. If not set the system's locale will be used or the locale of the output format, if set. |  |

The identifier for this plugin is `DateTypeParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *inputDateFormatId*: `German style date format`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[20.03.1999]`

* Returns:

  → `[1999-03-20]`


---
##### Example 2:

* Parameters
  * *inputDateFormatId*: `w3c Date`
  * *outputDateFormatId*: `German style date format`

* Input values:
  1. `[1999-03-20]`

* Returns:

  → `[20.03.1999]`


---
##### Example 3:

* Parameters
  * *inputDateFormatId*: `common ISO8601`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[2017-04-04T00:00:00.000+02:00]`

* Returns:

  → `[2017-04-04]`


---
##### Example 4:

* Parameters
  * *inputDateFormatId*: `common ISO8601`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[2017-04-04T00:00:00+02:00]`

* Returns:

  → `[2017-04-04]`


---
##### Example 5:

* Parameters
  * *inputDateFormatId*: `common ISO8601`
  * *outputDateFormatId*: `dateTime with month abbr. (US)`

* Input values:
  1. `[2021-06-24T14:50:05.895+02:00]`

* Returns:

  → `[24-Jun-2021 14:50:05 +02:00]`


---
##### Example 6:

* Parameters
  * *inputDateFormatId*: `dateTime with month abbr. (US)`
  * *outputDateFormatId*: `dateTime with month abbr. (DE)`

* Input values:
  1. `[24-Dec-2021 14:50:05 +02:00]`

* Returns:

  → `[24-Dez.-2021 14:50:05 +02:00]`


---
##### Example 7:

* Parameters
  * *alternativeInputFormat*: `dd.MM.yyyy HH:mm.ss`
  * *alternativeOutputFormat*: `yyyy-MM-dd'T'HH:mm.ss`

* Input values:
  1. `[20.03.1999 20:34.44]`

* Returns:

  → `[1999-03-20T20:34.44]`


---
##### Example 8:

* Parameters
  * *inputDateFormatId*: `excelDateTime`
  * *outputDateFormatId*: `xsdTime`

* Input values:
  1. `[12:20:00.000]`

* Returns:

  → `[12:20:00.000]`


---
##### Example 9:

* Parameters
  * *inputDateFormatId*: `w3c YearMonth`
  * *outputDateFormatId*: `w3c Month`

* Input values:
  1. `[2020-01]`

* Returns:

  → `[--01]`


---
##### Example 10:

* Parameters
  * *inputDateFormatId*: `w3c MonthDay`
  * *outputDateFormatId*: `w3c Day`

* Input values:
  1. `[--12-31]`

* Returns:

  → `[---31]`


---
##### Example 11:

* Parameters
  * *inputDateFormatId*: `w3c Date`
  * *outputDateFormatId*: `w3c MonthDay`

* Input values:
  1. `[2020-12-31]`

* Returns:

  → `[--12-31]`


---
##### Example 12:

* Parameters
  * *inputDateFormatId*: `w3c MonthDay`
  * *outputDateFormatId*: `w3c Date`

* Input values:
  1. `[--12-31]`

* Returns:

  → `[]`


---
##### Example 13:

* Parameters
  * *alternativeInputFormat*: `yyyy-MM-dd HH:mm:ss.SSS`
  * *outputDateFormatId*: `w3cDateTime`

* Input values:
  1. `[2020-02-22 16:34:14.000]`

* Returns:

  → `[2020-02-22T16:34:14]`


---
##### Example 14:

* Parameters
  * *inputDateFormatId*: `dateTime with month abbr. (DE)`
  * *outputDateFormatId*: `dateTime with month abbr. (US)`
  * *inputLocale*: `en_US`
  * *outputLocale*: `de`

* Input values:
  1. `[24-Dec-2021 14:50:05 +02:00]`

* Returns:

  → `[24-Dez.-2021 14:50:05 +02:00]`


---
##### Example 15:

* Parameters
  * *inputDateFormatId*: `dateTime with month abbr. (US)`
  * *outputDateFormatId*: `dateTime with month abbr. (DE)`
  * *inputLocale*: `de`
  * *outputLocale*: `en`

* Input values:
  1. `[24-Dez.-2021 14:50:05 +02:00]`

* Returns:

  → `[24-Dec-2021 14:50:05 +02:00]`


---
##### Example 16:

* Parameters
  * *outputLocale*: `fr`
  * *alternativeInputFormat*: `MMM yyyy`
  * *outputDateFormatId*: `dateTime with month abbr. (DE)`
  * *inputLocale*: `de`
  * *alternativeOutputFormat*: `MMM uuuu`
  * *inputDateFormatId*: `dateTime with month abbr. (US)`

* Input values:
  1. `[Dez. 2021]`

* Returns:

  → `[déc. 2021]`


---
##### Example 17:

* Parameters
  * *alternativeInputFormat*: `MMMM, uuuu`
  * *alternativeOutputFormat*: `MMMM, uuuu`
  * *inputLocale*: `en_US`
  * *outputLocale*: `de`

* Input values:
  1. `[February, 2024]`

* Returns:

  → `[Februar, 2024]`

#### Parse float

Parses and normalizes float values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| commaAsDecimalPoint | boolean | No description | false |
| thousandSeparator | boolean | No description | false |
| bracketsForNegative | boolean | No description | false |

The identifier for this plugin is `FloatTypeParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.



#### Parse geo coordinate

Parses and normalizes geo coordinates.

This plugin does not require any parameters.
The identifier for this plugin is `GeoCoordinateParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.



#### Parse geo location

Parses and normalizes geo locations like continents, countries, states and cities.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| parseTypeId | Enum | What type of location should be parsed. | *no default* |
| fullStateName | boolean | Set to true if the full state name should be output instead of the 2-letter code. | true |

The identifier for this plugin is `GeoLocationParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.



#### Parse integer

Parses integer values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| commaAsDecimalPoint | boolean | Use comma as decimal point (uses a point, otherwise) | false |
| thousandSeparator | boolean | Use comma or point to separate digits | false |

The identifier for this plugin is `IntegerParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.



#### Parse ISIN

Parses International Securities Identification Numbers (ISIN) values and fails if the String is no valid ISIN.

This plugin does not require any parameters.
The identifier for this plugin is `IsinParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.



#### Parse SKOS term

Parses values from a SKOS ontology.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| surfaceFormToRepresentationMapping | Map | No description | *no default* |

The identifier for this plugin is `SkosTypeParser`.

It can be found in the package `com.eccenca.di.schema.discovery.discoverer`.



#### Parse string

Parses string values, basically an identity function.

This plugin does not require any parameters.
The identifier for this plugin is `StringParser`.

It can be found in the package `com.eccenca.di.schema.discovery.parser`.



#### Clean HTML

Cleans HTML using a tag white list and allows selection of HTML sections with XPath or CSS selector expressions.
       If the tag or attribute white lists are left empty default white lists will be used (this behaviour can be changed).
       To remove all HTML markup and retain text, keep the defaults and turn off the "Default tags and attributes" toggle.
       The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| tagWhiteList | StringIterableParameter | Tags to keep in the cleaned output. |  |
| attributeWhiteList | StringIterableParameter | Attributes to keep in the cleaned output. |  |
| selectors | StringIterableParameter | CSS or XPath queries for selection of content. CSS selectors can be pipe separated for non-sequential execution. |  |
| method | Enum | Selects use of XPath or CSS selectors. | xPath |
| defaultTagsAndAttributes | boolean | Use defaults for empty tag and attribute whitelists.\If the attribute while list is empty, it will default to: "class", "id", "href", "src"\If the tag while list is empty, it will default to: "a", "b", "blockquote", "br", "caption", "cite", "code", "col", "colgroup", "dd", "div", "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6","i", "img", "li", "ol", "p", "pre", "q", "small", "span", "strike", "strong","sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul". | true |

The identifier for this plugin is `htmlCleaner`.

It can be found in the package `com.eccenca.di.plugins.html`.



### Replace

#### Excel map

Replaces values based on a map of values read from a file in Open XML format (XLSX).
The XLSX file may contain several sheets of the form:

mapFrom,mapTo
<source string>,<target string>
... and more

An empty string can be created in Excel and alternatives by inserting ="" in the input line of a cell.

If there are multiple values for a single key, all values will be returned for the given key.

Note that the mapping table will be cached in memory. If the Excel file is updated (even while transforming), the map will be reloaded within seconds.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| excelFile | Resource | Excel file inside the resources directory containing one or more sheets with mapping tables. | *no default* |
| sheetName | String | The sheet that contains the mapping table or empty if the first sheet should be taken. | *empty string* |
| skipLines | int | How many rows to skip before reading the mapping table. By default the expected header row is skipped. | 1 |
| strict | boolean | If set to true, the operator throws validation errors for values it cannot map. If set to false, the chosen conflict strategy will be applied for missing values. | true |
| conflictStrategy | Enum | Determines how values that cannot be found in the mapping table are treated. Only has an effect if 'strict' is set to false. If 'retain' is chosen, the original value will be forwarded. If 'remove' is chosen, no value will be output. | retain |

The identifier for this plugin is `excelMap`.

It can be found in the package `com.eccenca.di.excel`.



#### Map

Replaces values based on a map of values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| map | Map | A map of values | *no default* |
| default | String | Default if the map defines no value | *no default* |

The identifier for this plugin is `map`.

It can be found in the package `org.silkframework.rule.plugins.transformer.replace`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *map*: `Key1:Value1,Key2:Value2`
  * *default*: `Undefined`

* Input values:
  1. `[Key1]`

* Returns:

  → `[Value1]`


---
##### Example 2:

* Parameters
  * *map*: `Key1:Value1,Key2:Value2`
  * *default*: `Undefined`

* Input values:
  1. `[Key1X]`

* Returns:

  → `[Undefined]`

#### Map with default


Takes two inputs.
Tries to map the first input based on the map of values parameter config.
If the input value is not found in the map, it takes the value of the second input.
The indexes of the mapped value and the default value match. If there are less default values than
values to map, the last default value is replicated to match the count.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| map | Map | A map of values | *no default* |

The identifier for this plugin is `mapWithDefaultInput`.

It can be found in the package `org.silkframework.rule.plugins.transformer.replace`.



#### Regex replace

Replace all occurrences of a regex "regex" with "replace" in a string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| regex | String | The regular expression to search for | *no default* |
| replace | String | The string that will replace each match | *empty string* |

The identifier for this plugin is `regexReplace`.

It can be found in the package `org.silkframework.rule.plugins.transformer.replace`.



#### Replace

Replace all occurrences of a string "search" with "replace" in a string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| search | String | The string to search for | *no default* |
| replace | String | The string that will replace each match | *no default* |

The identifier for this plugin is `replace`.

It can be found in the package `org.silkframework.rule.plugins.transformer.replace`.



### Selection

#### Coalesce (first non-empty input)

Forwards the first non-empty input, i.e. for which any value(s) exist. A single empty string is considered a value.

This plugin does not require any parameters.
The identifier for this plugin is `coalesce`.

It can be found in the package `org.silkframework.rule.plugins.transformer.selection`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[]`
  2. `[]`
  3. `[]`

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[]`
  2. `[]`

* Returns:

  → `[]`


---
##### Example 3:

* Returns:

  → `[]`


---
##### Example 4:

* Input values:
  1. `[]`
  2. `[first]`
  3. `[second]`

* Returns:

  → `[first]`


---
##### Example 5:

* Input values:
  1. `[]`
  2. `[first A, first B]`
  3. `[second]`

* Returns:

  → `[first A, first B]`


---
##### Example 6:

* Input values:
  1. `[first]`
  2. `[second]`

* Returns:

  → `[first]`

#### Regex selection

This transformer takes 3 inputs.
The first input should have exactly one value that should be passed out again untouched.
The second input has at least two Regex values - two in order to make sense.
The third input should have exactly one value which is checked against the regexes.

The result of the transformer is a sequence with the same length of number of regexes.
For the output value (of the first input) is set to each position in this sequence where
the related regex also matched.

If `oneOnly` is true only the position of the **first** matching regex will be set to the output value.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| oneOnly | boolean | No description | false |

The identifier for this plugin is `regexSelect`.

It can be found in the package `org.silkframework.rule.plugins.transformer.selection`.



### Sequence

#### Count values

Counts the number of values.

This plugin does not require any parameters.
The identifier for this plugin is `count`.

It can be found in the package `org.silkframework.rule.plugins.transformer.numeric`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[value1]`

* Returns:

  → `[1]`


---
##### Example 2:

* Input values:
  1. `[value1, value2]`

* Returns:

  → `[2]`

#### Get value by index

Returns the value found at the specified index. Fails or returns an empty result depending on failIfNoFound is set or not.
       Please be aware that this will work only if the data source supports some kind of ordering like XML or JSON. This
       is probably not a good idea to do with RDF models.

       If emptyStringToEmptyResult is true then instead of a result with an empty String, an empty result is returned.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| index | int | No description | *no default* |
| failIfNotFound | boolean | No description | false |
| emptyStringToEmptyResult | boolean | No description | false |

The identifier for this plugin is `getValueByIndex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.sequence`.



#### Sort

Sorts values lexicographically.

This plugin does not require any parameters.
The identifier for this plugin is `sort`.

It can be found in the package `org.silkframework.rule.plugins.transformer.sequence`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[]`

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[c, a, b]`

* Returns:

  → `[a, b, c]`


---
##### Example 3:

* Input values:
  1. `[Hans, Hansa, Hamburg]`

* Returns:

  → `[Hamburg, Hans, Hansa]`

#### Sequence values to indexes

Transforms the sequence of values to their respective indexes in the sequence.
  Example:
   - ("a", "b", "c") becomes (0, 1, 2)

  If there is more than one input, the values are numbered from the first input on and continued for the next inputs.
  Applied against an RDF source the order might not be deterministic.


This plugin does not require any parameters.
The identifier for this plugin is `toSequenceIndex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.sequence`.



### Substring

#### Strip postfix

Strips a postfix of a string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| postfix | String | No description | *no default* |

The identifier for this plugin is `stripPostfix`.

It can be found in the package `org.silkframework.rule.plugins.transformer.substring`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *postfix*: `Postfix`

* Input values:
  1. `[valuePostfix]`

* Returns:

  → `[value]`


---
##### Example 2:

* Parameters
  * *postfix*: `Postfix`

* Input values:
  1. `[Value]`

* Returns:

  → `[Value]`

#### Strip prefix

Strips a prefix of a string.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| prefix | String | No description | *no default* |

The identifier for this plugin is `stripPrefix`.

It can be found in the package `org.silkframework.rule.plugins.transformer.substring`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *prefix*: `prefix`

* Input values:
  1. `[prefixValue]`

* Returns:

  → `[Value]`


---
##### Example 2:

* Parameters
  * *prefix*: `prefix`

* Input values:
  1. `[ValueWithoutPrefix]`

* Returns:

  → `[ValueWithoutPrefix]`

#### Strip URI prefix

Strips the URI prefix and decodes the remainder. Leaves values unchanged which are not a valid URI.

This plugin does not require any parameters.
The identifier for this plugin is `stripUriPrefix`.

It can be found in the package `org.silkframework.rule.plugins.transformer.substring`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[http://example.org/some/path/to/value]`

* Returns:

  → `[value]`


---
##### Example 2:

* Input values:
  1. `[urn:scheme:value]`

* Returns:

  → `[value]`


---
##### Example 3:

* Input values:
  1. `[http://example.org/some/path/to/encoded%20v%C3%A4lue]`

* Returns:

  → `[encoded välue]`


---
##### Example 4:

* Input values:
  1. `[value]`

* Returns:

  → `[value]`

#### Substring

Returns a substring between 'beginIndex' (inclusive) and 'endIndex' (exclusive).
If 'endIndex' is 0 (default), it is ignored and the entire remaining string starting with 'beginIndex' is returned.
If 'endIndex' is negative, -endIndex characters are removed from the end.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| beginIndex | int | The beginning index, inclusive. | 0 |
| endIndex | int | The end index, exclusive. Ignored if set to 0, i.e., the entire remaining string starting with 'beginIndex' is returned. If negative, -endIndex characters are removed from the end  | 0 |
| stringMustBeInRange | boolean | If true, only strings will be accepted that are within the start and end indices, throwing a validating error if an index is out of range. | true |

The identifier for this plugin is `substring`.

It can be found in the package `org.silkframework.rule.plugins.transformer.substring`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *beginIndex*: `0`
  * *endIndex*: `1`

* Input values:
  1. `[abc]`

* Returns:

  → `[a]`


---
##### Example 2:

* Parameters
  * *beginIndex*: `2`
  * *endIndex*: `3`

* Input values:
  1. `[abc]`

* Returns:

  → `[c]`


---
##### Example 3:

* Parameters
  * *beginIndex*: `3`
  * *endIndex*: `3`

* Input values:
  1. `[abc]`

* Returns:

  → `[]`


---
##### Example 4:

* Parameters
  * *beginIndex*: `2`
  * *endIndex*: `4`

* Input values:
  1. `[abc]`

* Returns:

  → `[c]`


---
##### Example 5:

* Parameters
  * *beginIndex*: `2`
  * *endIndex*: `4`
  * *stringMustBeInRange*: `false`

* Input values:
  1. `[abc]`

* Returns:

  → `[c]`


---
##### Example 6:

* Parameters
  * *beginIndex*: `10`
  * *endIndex*: `20`
  * *stringMustBeInRange*: `false`

* Input values:
  1. `[abc]`

* Returns:

  → `[]`


---
##### Example 7:

* Parameters
  * *beginIndex*: `0`
  * *endIndex*: `-1`

* Input values:
  1. `[abc]`

* Returns:

  → `[ab]`


---
##### Example 8:

* Parameters
  * *beginIndex*: `1`
  * *endIndex*: `0`

* Input values:
  1. `[abc]`

* Returns:

  → `[bc]`

#### Trim

Remove leading and trailing whitespaces.

This plugin does not require any parameters.
The identifier for this plugin is `trim`.

It can be found in the package `org.silkframework.rule.plugins.transformer.normalize`.



#### Until character

Extracts the substring until the character given.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| untilCharacter | char | No description | *no default* |

The identifier for this plugin is `untilCharacter`.

It can be found in the package `org.silkframework.rule.plugins.transformer.substring`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *untilCharacter*: `c`

* Input values:
  1. `[abcde]`

* Returns:

  → `[ab]`


---
##### Example 2:

* Parameters
  * *untilCharacter*: `c`

* Input values:
  1. `[abab]`

* Returns:

  → `[abab]`

### Template

#### Evaluate template

Evaluates a template. Input values can be addressed using the variables 'input1', 'input2', etc. Global variables are available in the 'global' scope, e.g., 'global.myVar'.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| template | TemplateParameter | The template | *no default* |
| language | String | The template language. Currently, Jinja is supported. | jinja |

The identifier for this plugin is `TemplateTransformer`.

It can be found in the package `com.eccenca.di.templating.operators`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *template*: `Hello {{input1}} {{input2}},

How are you today?`

* Input values:
  1. `[John]`
  2. `[Doe]`

* Returns:

  → `[Hello John Doe,

How are you today?]`


---
##### Example 2:

* Parameters
  * *template*: `Hello {{badVariable}} {{input1}}`

* Input values:
  1. `[John]`
  2. `[Doe]`

* Returns:

  → `[]`


---
##### Example 3:

* Parameters
  * *template*: `Hello {{input01}}`

* Returns:

  → `[]`


---
##### Example 4:

* Parameters
  * *template*: `Hello {{input1}}`

* Returns:

  → `[]`


---
##### Example 5:

* Parameters
  * *template*: `Hello {{input1}}`

* Input values:
  1. `[A, B]`

* Returns:

  → `[Hello AB]`


---
##### Example 6:

* Parameters
  * *template*: `Hello {% for value in input1 %}{{value}}, {% endfor %}how are you doing?`

* Input values:
  1. `[Bob, Eve]`

* Returns:

  → `[Hello Bob, Eve, how are you doing?]`

### Tokenization

#### Camel case tokenizer

Tokenizes a camel case string. That is it splits strings between a lower case character and an upper case character.

This plugin does not require any parameters.
The identifier for this plugin is `camelcasetokenizer`.

It can be found in the package `org.silkframework.rule.plugins.transformer.tokenization`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[camelCaseString]`

* Returns:

  → `[camel, Case, String]`


---
##### Example 2:

* Input values:
  1. `[nocamelcase]`

* Returns:

  → `[nocamelcase]`

#### Get value by index

Returns the value found at the specified index. Fails or returns an empty result depending on failIfNoFound is set or not.
       Please be aware that this will work only if the data source supports some kind of ordering like XML or JSON. This
       is probably not a good idea to do with RDF models.

       If emptyStringToEmptyResult is true then instead of a result with an empty String, an empty result is returned.


| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| index | int | No description | *no default* |
| failIfNotFound | boolean | No description | false |
| emptyStringToEmptyResult | boolean | No description | false |

The identifier for this plugin is `getValueByIndex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.sequence`.



#### Tokenize

Tokenizes all input values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| regex | String | The regular expression used to split values. | \\s |

The identifier for this plugin is `tokenize`.

It can be found in the package `org.silkframework.rule.plugins.transformer.tokenization`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### By default, splits values at whitespaces:

* Input values:
  1. `[Hello World]`

* Returns:

  → `[Hello, World]`


---
##### Optionally, splits values at the provided regex:

* Parameters
  * *regex*: `,`

* Input values:
  1. `[.175,.050]`

* Returns:

  → `[.175, .050]`

### Validation

#### Validate date after

Validates if the first input date is after the second input date. Outputs the first input if the validation is successful.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| allowEqual | boolean | Allow both dates to be equal. | false |

The identifier for this plugin is `validateDateAfter`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[2015-04-02]`
  2. `[2015-04-03]`

* Returns:

  → `[]`


---
##### Example 2:

* Input values:
  1. `[2015-04-04]`
  2. `[2015-04-03]`

* Returns:

  → `[2015-04-04]`


---
##### Example 3:

* Parameters
  * *allowEqual*: `true`

* Input values:
  1. `[2015-04-03]`
  2. `[2015-04-03]`

* Returns:

  → `[2015-04-03]`


---
##### Example 4:

* Parameters
  * *allowEqual*: `false`

* Input values:
  1. `[2015-04-03]`
  2. `[2015-04-03]`

* Returns:

  → `[]`

#### Validate date range

Validates if dates are within a specified range.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| minDate | String | Earliest allowed date in YYYY-MM-DD | *no default* |
| maxDate | String | Latest allowed data in YYYY-MM-DD | *no default* |

The identifier for this plugin is `validateDateRange`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.



#### Validate number of values

Validates that the number of values lies in a specified range.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| min | int | Minimum allowed number of values | 0 |
| max | int | Maximum allowed number of values | 1 |

The identifier for this plugin is `validateNumberOfValues`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Parameters
  * *min*: `0`
  * *max*: `1`

* Input values:
  1. `[value1]`

* Returns:

  → `[value1]`


---
##### Example 2:

* Parameters
  * *min*: `0`
  * *max*: `1`

* Input values:
  1. `[value1, value2]`

* Returns:

  → `[]`

#### Validate numeric range

Validates if a number is within a specified range.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| min | double | Minimum allowed number | *no default* |
| max | double | Maximum allowed number | *no default* |

The identifier for this plugin is `validateNumericRange`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.



#### Validate regex

Validates if all values match a regular expression.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| regex | String | regular expression | \\w* |

The identifier for this plugin is `validateRegex`.

It can be found in the package `org.silkframework.rule.plugins.transformer.validation`.



### Value

#### Constant

Generates a constant value.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| value | String | The constant value to be generated | *empty string* |

The identifier for this plugin is `constant`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Always outputs the specified value:

* Parameters
  * *value*: `John`

* Returns:

  → `[John]`

#### Constant URI

Generates a constant URI.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| value | Uri | The constant URI to be generated | <http://www.w3.org/2002/07/owl#Class> |

The identifier for this plugin is `constantUri`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.



#### Current date

Outputs the current date.

This plugin does not require any parameters.
The identifier for this plugin is `currentDate`.

It can be found in the package `org.silkframework.rule.plugins.transformer.date`.



#### Dataset parameter

Reads a meta data parameter from a dataset in Corporate Memory. If authentication is enabled, workbench.superuser must be configured.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| project | ProjectReference | The project of the dataset. | cmem |
| dataset | TaskReference | The dataset the meta data parameter is read from. | *no default* |
| key | String | No description | *no default* |
| lang | String | No description | *empty string* |

The identifier for this plugin is `datasetParameter`.

It can be found in the package `com.eccenca.di.workflow.operators.datasetParam`.



#### Default Value

Generates a default value, if the input values are empty. Forwards any non-empty values.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| value | String | The default value to be generated, if input values are empty | default |

The identifier for this plugin is `defaultValue`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Forwards input values:

* Input values:
  1. `[input value]`

* Returns:

  → `[input value]`


---
##### Outputs the default value, if the inputs are empty:

* Parameters
  * *value*: `default value`

* Input values:
  1. `[]`

* Returns:

  → `[default value]`

#### Empty value

Generates an empty value.

This plugin does not require any parameters.
The identifier for this plugin is `emptyValue`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.



#### Input hash

Calculates the hash sum of the input values. Generates a single hash sum for all input values combined.
This operator supports using different hash algorithms from the [Secure Hash Algorithms family](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) (SHA, e.g. SHA256) and two algorithms from the [Message-Digest Algorithm family](https://en.wikipedia.org/wiki/MD5) (MD2 / MD5). Please be aware that some of these algorithms are not secure regarding collision- and other attacks.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| algorithm | String | The hash algorithm to be used. | SHA256 |

The identifier for this plugin is `inputHash`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[input value]`

* Returns:

  → `[f708c2afff0ed197e8551c4dd549ee5b848e0b407106cbdb8e451c8cd1479362]`

#### Random number

Generates a set of random numbers.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| min | double | The smallest number that could be generated. | 0.0 |
| max | double | The largest number that could be generated. | 100.0 |
| minCount | int | The minimum number of values to generate in each set. | 1 |
| maxCount | int | The maximum number of values to generate in each set. | 1 |

The identifier for this plugin is `randomNumber`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.



#### Read parameter

Reads a parameter from a Java Properties file.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| resource | Resource | The Java properties file to read the parameter from. | *no default* |
| parameter | String | The name of the parameter. | *no default* |

The identifier for this plugin is `readParameter`.

It can be found in the package `org.silkframework.plugins.transformer.value`.



#### UUID

 Generates UUIDs.
If no input value is provided, a random UUID (type 4) is generated using a cryptographically strong pseudo random number generator.
If input values are provided, a name-based UUID (type 3) is generated for each input value.
Each input value will generate a separate UUID. For building a UUID from multiple inputs, the Concatenate operator can be used.


This plugin does not require any parameters.
The identifier for this plugin is `uuid`.

It can be found in the package `org.silkframework.rule.plugins.transformer.value`.


##### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
##### Example 1:

* Input values:
  1. `[input value]`

* Returns:

  → `[cee963a2-8f70-3e97-b51a-85ef732e66dd]`


---
##### Example 2:

* Input values:
  1. `[üöä!, êéè]`

* Returns:

  → `[690802dd-a317-335f-807c-e4e1e32b7b5b, 925cbd7f-377b-3fbd-8f4c-ca41529b74ad]`

## Aggregations

The following aggregation functions are available:

### Average

Computes the weighted average.

This plugin does not require any parameters.
The identifier for this plugin is `average`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Computes the arithmetic mean of all similarity scores:

* Input values: [0.4, 0.5, 0.9]
* Returns: `0.6`


---
#### Multiplies individual similarity scores with their weight before averaging:

* Weights: [1, 1, 2]
* Input values: [0.3, 0.5, 0.6]
* Returns: `0.5`


---
#### Missing scores always lead to an output of none:

* Input values: [-1.0, (none), 1.0]
* Returns: `(none)`

### First non-empty score

Forwards the first input that provides a non-empty similarity score.

This plugin does not require any parameters.
The identifier for this plugin is `firstNonEmpty`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### The first defined score is returned, even if it's not the highest score:

* Input values: [(none), 0.2, 0.5]
* Returns: `0.2`

### Geometric mean

Compute the (weighted) geometric mean.

This plugin does not require any parameters.
The identifier for this plugin is `geometricMean`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Example 1:

* Weights: [1, 2, 1]
* Input values: [0.0, 0.0, 0.0]
* Returns: `0.0`


---
#### Example 2:

* Weights: [1, 2, 1]
* Input values: [1.0, 1.0, 1.0]
* Returns: `1.0`


---
#### Example 3:

* Weights: [2, 1]
* Input values: [0.5, 1.0]
* Returns: `0.629961`


---
#### Example 4:

* Weights: [2, 1, 5]
* Input values: [0.5, 1.0, 0.7]
* Returns: `0.672866`


---
#### Example 5:

* Weights: [10, 2, 3]
* Input values: [0.1, 0.9, 0.2]
* Returns: `0.153971`


---
#### Missing scores always lead to an output of none:

* Input values: [-1.0, (none), 1.0]
* Returns: `(none)`

### Handle missing values

Generates a default similarity score, if no similarity score is provided (e.g., due to missing values). Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| defaultValue | double | The default value to be generated, if no similarity score is provided. Must be a value between -1 (inclusive) and 1 (inclusive). '1' represents boolean true and '-1' represents boolean false. | -1.0 |

The identifier for this plugin is `handleMissingValues`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Forwards input similarity scores:

* Input values: [0.1]
* Returns: `0.1`


---
#### Outputs the default score, if no input score is provided:

* Parameters
  * *defaultValue*: `1.0`

* Input values: [(none)]
* Returns: `1.0`

### Or

At least one input score must be within the threshold. Selects the maximum score.

This plugin does not require any parameters.
The identifier for this plugin is `max`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Selects the maximum similarity score:

* Input values: [0.5, 0.0]
* Returns: `0.5`


---
#### Selects the maximum similarity score:

* Input values: [-1.0, -0.5, -0.3]
* Returns: `-0.3`


---
#### Missing scores default to a similarity score of -1:

* Input values: [(none)]
* Returns: `-1.0`


---
#### Weights are ignored:

* Weights: [1000, 0]
* Input values: [1.0, 0.0]
* Returns: `1.0`

### And

All input scores must be within the threshold. Selects the minimum score.

This plugin does not require any parameters.
The identifier for this plugin is `min`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Selects the minimum similarity score:

* Input values: [1.0, 0.0]
* Returns: `0.0`


---
#### Selects the minimum similarity score:

* Input values: [-1.0, 0.0, 0.5, 1.0]
* Returns: `-1.0`


---
#### Missing scores default to a similarity score of -1:

* Input values: [1.0, (none), -0.5]
* Returns: `-1.0`


---
#### Weights are ignored:

* Weights: [1000, 0]
* Input values: [1.0, 0.0]
* Returns: `0.0`

### Negate

Negates the result of the input comparison. A single input is expected. Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation.

This plugin does not require any parameters.
The identifier for this plugin is `negate`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.



### Euclidian distance

Calculates the Euclidian distance.

This plugin does not require any parameters.
The identifier for this plugin is `quadraticMean`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Example 1:

* Weights: [1, 1, 1]
* Input values: [1.0, 1.0, 1.0]
* Returns: `1.0`


---
#### Example 2:

* Weights: [1, 1]
* Input values: [1.0, 0.0]
* Returns: `0.707107`


---
#### Example 3:

* Weights: [1, 1, 1]
* Input values: [0.4, 0.5, 0.6]
* Returns: `0.506623`


---
#### Example 4:

* Weights: [1, 1]
* Input values: [0.0, 0.0]
* Returns: `0.0`


---
#### Example 5:

* Weights: [2, 1, 1]
* Input values: [1.0, 0.0, 0.0]
* Returns: `0.707107`


---
#### Example 6:

* Weights: [1, 2, 3]
* Input values: [0.4, 0.5, 0.6]
* Returns: `0.538516`


---
#### Missing scores always lead to an output of none:

* Input values: [-1.0, (none), 1.0]
* Returns: `(none)`

### Scale

Scales a similarity score by a factor.

| Parameter | Type | Description | Default |
|  -------------------- | ---------- | ------------------------- | ------------------------- |
| factor | double | All input similarity values are multiplied with this factor. | 1.0 |

The identifier for this plugin is `scale`.

It can be found in the package `org.silkframework.rule.plugins.aggegrator`.


#### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Scales similarity scores by the specified factor:

* Parameters
  * *factor*: `0.5`

* Input values: [1.0]
* Returns: `0.5`


---
#### Ignores missing values:

* Input values: [(none)]
* Returns: `(none)`


---
#### Throws a validation error if more than one input is provided:

* Input values: [0.1, 0.2]
* Returns: `(none)`
