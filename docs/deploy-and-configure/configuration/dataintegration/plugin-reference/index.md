---
tags:
    - Reference
---
# Plugin Reference

<!-- Auto-Generated. Do not edit directly! -->
<h2 id="plugin-tasks">Plugin Tasks</h2>
<p>The following plugin tasks are available:</p>
<h4 id="sql-query">SQL query</h4>
<p>Executes a custom SQL query on the first input dataset and returns the result as its output.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>command</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>SQL command. The name of<br>
the table in the<br>
statement must be<br>
‘dataset’, regardless<br>
the input.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>CustomSQLExecution</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark.operator</code>.</p>
<h4 id="parse-json">Parse JSON</h4>
<p>Takes exactly one input and reads either the defined inputPath or the first value of the first entity as a JSON document. Then executes incoming requests as if this were a JSON dataset, e.g. form a transformation task.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inputPath</td>
<td>String</td>
<td>The Silk path expression<br>
of the input entity that<br>
contains the JSON<br>
document. If not set,<br>
the value of the first<br>
defined property will be<br>
taken.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>basePath</td>
<td>String</td>
<td>The path to the elements<br>
to be read, starting<br>
from the root element,<br>
e.g., ‘/Persons/Person’.<br>
If left empty, all<br>
direct children of the<br>
root element will be<br>
read.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>uriSuffixPattern</td>
<td>String</td>
<td>A URI pattern that is<br>
relative to the base URI<br>
of the input entity,<br>
e.g., /{ID}, where<br>
{path} may contain<br>
relative paths to<br>
elements. This relative<br>
part is appended to the<br>
input entity URI to<br>
construct the full URI<br>
pattern.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>JsonParserOperator</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.json</code>.</p>
<h4 id="join-tables">Join tables</h4>
<p>Joins a set of inputs into a single table. Expects a list of entity tables and links. All entity tables are joined into the first entity table using the provided links.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>Merge</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.merge</code>.</p>
<h4 id="merge-tables">Merge tables</h4>
<p>Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>multiTableOutput</td>
<td>boolean</td>
<td>test</td>
<td>true</td>
</tr>
<tr class="even">
<td>pivotTableName</td>
<td>String</td>
<td>Name of the pivot<br>
table.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>mappingNames</td>
<td>String</td>
<td>Name of the mapping<br>
tables. Comma separated<br>
list.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>instanceSet-<br>
Names</td>
<td>String</td>
<td>Name of the tables joined<br>
to the pivot. Comma<br>
separated list.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>MultiTableMerge</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.merge</code>.</p>
<h4 id="pivot">Pivot</h4>
<p>The pivot operator takes data in separate rows, aggregates it and converts it into columns. This operator can be used in a workflow right after a mapping task.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>pivotProperty</td>
<td>String</td>
<td>The pivot column.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>firstGroupProperty</td>
<td>String</td>
<td>The name of the first<br>
group column in the<br>
range.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>lastGroupProperty</td>
<td>String</td>
<td>The name of the last<br>
group column in the<br>
range. If left empty,<br>
only the first column is<br>
used.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>valueProperty</td>
<td>String</td>
<td>The property that<br>
contains the values that<br>
will be aggregated.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>aggregation-<br>
Function</td>
<td>Enum</td>
<td>The aggregation function<br>
used to aggregate<br>
values.</td>
<td>sum</td>
</tr>
<tr class="even">
<td>uriPrefix</td>
<td>String</td>
<td>Prefix to prepend to all<br>
generated pivot<br>
columns.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Pivot</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.pivot</code>.</p>
<h4 id="rest-request">REST request</h4>
<p>Executes a REST request based on fixed configuration and/or input parameters and returns the result as entity.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>url</td>
<td>String</td>
<td>The URL to execute this<br>
request against. This<br>
can be overwritten at<br>
execution time via<br>
input.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>method</td>
<td>String</td>
<td>The HTTP method. One of<br>
GET, PUT or POST</td>
<td>GET</td>
</tr>
<tr class="odd">
<td>accept</td>
<td>String</td>
<td>The accept header<br>
String.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>requestTimeout</td>
<td>int</td>
<td>Request timeout in ms.<br>
The overall maximum time<br>
the request should<br>
take.</td>
<td>10000</td>
</tr>
<tr class="odd">
<td>connectionTimeout</td>
<td>int</td>
<td>Connection timeout in ms.<br>
The time until which a<br>
connection with the<br>
remote end must be<br>
established.</td>
<td>5000</td>
</tr>
<tr class="even">
<td>readTimeout</td>
<td>int</td>
<td>Read timeout in ms. The<br>
max. time a request<br>
stays idle, i.e. no data<br>
is send or received.</td>
<td>10000</td>
</tr>
<tr class="odd">
<td>contentType</td>
<td>String</td>
<td>The content-type header<br>
String. This can be set<br>
in case of PUT or POST.<br>
If another content type<br>
comes back, the task<br>
will fail.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>content</td>
<td>String</td>
<td>The content that is send<br>
with a POST or PUT<br>
request. For handling<br>
this payload dynamically<br>
this parameter must be<br>
overwritten via the task<br>
input.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>httpHeaders</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>Configure additional HTTP<br>
headers. One header per<br>
line. Each header entry<br>
follows the curl<br>
syntax.</td>
<td></td>
</tr>
<tr class="even">
<td>readParametersFrom-<br>
Input</td>
<td>boolean</td>
<td>If this is set to true,<br>
specific parameters can<br>
be overwritten at<br>
execution time. Else<br>
inputs are ignored.<br>
Parameters that can<br>
currently be<br>
overwritten: url,<br>
content</td>
<td>false</td>
</tr>
<tr class="odd">
<td>multipartFile-<br>
Parameter</td>
<td>String</td>
<td>If set to a non-empty<br>
String then instead of a<br>
normal POST a<br>
multipart/form-data file<br>
upload request is<br>
executed. This value is<br>
used as the form<br>
parameter name.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>authorization-<br>
Header</td>
<td>String</td>
<td>The authorization header.<br>
This is usually either<br>
‘Authorization’ or<br>
’Proxy-Authorization’If<br>
left empty, no<br>
authorization header is<br>
sent.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>authorizationHeader-<br>
Value</td>
<td>Password-<br>
Parameter</td>
<td>The authorization header<br>
value. Usually this has<br>
the form ‘type secret’,<br>
e.g. for OAuth ’bearer<br>
<insert secret access<br>
token>.’This config<br>
parameter will be<br>
encrypted in the<br>
backend.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>RestOperator</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.workflow.operators.rest</code>.</p>
<h4 id="scheduler">Scheduler</h4>
<p>Executes a workflow at specified intervals.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>task</td>
<td>TaskRefere<br>
nce</td>
<td>The name of the workflow<br>
to be executed</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>interval</td>
<td>String</td>
<td>The interval at which the<br>
scheduler should run the<br>
referenced task. Must be<br>
in ISO-8601 duration<br>
format PnDTnHnMn.n-<br>
S</td>
<td>PT15M</td>
</tr>
<tr class="odd">
<td>startTime</td>
<td>String</td>
<td>The time when the<br>
scheduled task is run<br>
for the first time,<br>
e.g., 2017-12-03T10:15:3<br>
0. If no start time is<br>
set, midnight on the day<br>
the scheduler is started<br>
is assumed.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>enabled</td>
<td>boolean</td>
<td>Enables or disables the<br>
scheduler.</td>
<td>true</td>
</tr>
<tr class="odd">
<td>stopOnError</td>
<td>boolean</td>
<td>If true, this will stop<br>
the scheduler, so the<br>
failed task is not<br>
scheduled again for<br>
execution.</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Scheduler</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.scheduler</code>.</p>
<h4 id="search-addresses">Search addresses</h4>
<p>Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>searchAttributes</td>
<td>String-<br>
Traversabl<br>
eParameter</td>
<td>List of attributes that<br>
contain search terms.<br>
Multiple attributes will<br>
be concatenated into a<br>
single search.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>limit</td>
<td>IntOption-<br>
Parameter</td>
<td>Optionally limits the<br>
number of results for<br>
each search.</td>
<td>IntOptionParameter(None)</td>
</tr>
<tr class="odd">
<td>jsonLdContext</td>
<td>Resource-<br>
Option</td>
<td>Optional JSON-LD context<br>
to be used for<br>
converting the returned<br>
JSON to RDF. If not<br>
provided, a default<br>
context will be<br>
used.</td>
<td>ResourceOption(None)</td>
</tr>
<tr class="even">
<td>additionalParameters</td>
<td>String</td>
<td>Additional URL parameters<br>
to be attached to each<br>
HTTP search request.<br>
Example: ‘&countrycodes=<br>
de&addressdetails=1’.<br>
Consult the API<br>
documentation for a list<br>
of available<br>
parameters.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>SearchAddresses</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.geo</code>.</p>
<p><strong>Configuration</strong></p>
<p>The geocoding service to be queried for searches can be set up in the configuration. The default configuration is as follows:</p>
<pre><code>com.eccenca.di.geo = {
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
}</code></pre>
<p>In general, all services adhering to the <a href="https://nominatim.org/release-docs/develop/api/Search/">Nominatim search API</a> should be usable. Please note that when using public services, the pause time should be set to avoid overloading.</p>
<p><strong>Logging</strong></p>
<p>By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:</p>
<pre><code>logging.level {
  com.eccenca.di.geo=DEBUG
}</code></pre>
<h4 id="send-email">Send eMail</h4>
<p>Sends an eMail using an SMTP server. If connected to a dataset that is based on a file in a workflow, it will send that file whenever the workflow is executed It can be used to send the result of a workflow via Mail.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>host</td>
<td>String</td>
<td>The SMTP host, e.g,<br>
mail.myProvider.com</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>port</td>
<td>int</td>
<td>The SMTP port</td>
<td>587</td>
</tr>
<tr class="odd">
<td>user</td>
<td>String</td>
<td>Username</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>password</td>
<td>Password-<br>
Parameter</td>
<td>Password</td>
<td></td>
</tr>
<tr class="odd">
<td>from</td>
<td>String</td>
<td>The sender eMail<br>
address</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>receiver</td>
<td>String</td>
<td>The email addresses of<br>
the receivers. Email<br>
addresses are comma<br>
separated. Names must be<br>
quoted when containing<br>
commas.Example:<br>
john.smith@example.com,<br>
“Doe, John” <john.doe@ex<br>
ample.com>, needs no<br>
quoting <needs.no.quotin<br>
g@example.com></td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>cc</td>
<td>String</td>
<td>The CC-receiver eMail<br>
address. Email addresses<br>
are comma separated.<br>
Names must be quoted<br>
when containing<br>
commas.Example:<br>
john.smith@example.com,<br>
“Doe, John” <john.doe@ex<br>
ample.com>, needs no<br>
quoting <needs.no.quotin<br>
g@example.com></td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>bcc</td>
<td>String</td>
<td>The BCC-receiver eMail<br>
address. Email addresses<br>
are comma separated.<br>
Names must be quoted<br>
when containing<br>
commas.Example:<br>
john.smith@example.com,<br>
“Doe, John” <john.doe@ex<br>
ample.com>, needs no<br>
quoting <needs.no.quotin<br>
g@example.com></td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>subject</td>
<td>String</td>
<td>The eMail subject</td>
<td>Dataset</td>
</tr>
<tr class="even">
<td>message</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>The eMail text<br>
message</td>
<td></td>
</tr>
<tr class="odd">
<td>withAttachment</td>
<td>boolean</td>
<td>If enabled a file from<br>
the input is attached to<br>
the email. A single<br>
input to this operator<br>
is expected that<br>
provides a file, e.g. a<br>
file based dataset (XML,<br>
JSON etc.).</td>
<td>true</td>
</tr>
<tr class="even">
<td>sslConnection</td>
<td>boolean</td>
<td>When enabled a SSL/TLS<br>
connection will be<br>
forced from the start<br>
without negotiation with<br>
the server. Not to be<br>
confused with STARTTLS<br>
which upgrades an<br>
insecure connection to a<br>
SSL/TLS connection,<br>
which is done by<br>
default.</td>
<td>false</td>
</tr>
<tr class="odd">
<td>timeout</td>
<td>int</td>
<td>Timeout in milliseconds<br>
to establish a<br>
connection or wait for a<br>
server response. Setting<br>
it to 0 or negative<br>
number will disable the<br>
timeout.</td>
<td>10000</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>SendEMail</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.mail</code>.</p>
<h4 id="execute-spark-function">Execute Spark function</h4>
<p>Applies a specified Scala function to a specified field. E.g. when the inputField is ‘name’, the inputFunction is ‘any => “Arrrrgh!” and the alias is ’xxx’,)‘a query corresponding to ’Function existingField1, existingFiled2, … “Arrrrgh!” as “xxx”’ will be generated. If alias is empty the inputField will be overwritten, otherwise a new field will be added and the rest of the schema stays the same.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>function</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>Scala function<br>
expression.</td>
<td></td>
</tr>
<tr class="even">
<td>inputField</td>
<td>String</td>
<td>Input field.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>alias</td>
<td>String</td>
<td>Alias.</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>SparkFunction</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark.operator</code>.</p>
<h4 id="evaluate-template">Evaluate template</h4>
<p>Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel. For each input entity, a output entity is generated that provides a single output attribute, which contains the evaluated template.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>template</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>The template</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>language</td>
<td>Enum</td>
<td>The template language.<br>
Currently, Jinja is<br>
supported.</td>
<td>jinja</td>
</tr>
<tr class="odd">
<td>outputAttribute</td>
<td>String</td>
<td>The attribute in the<br>
output that will hold<br>
the evaluated<br>
template.</td>
<td>output</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Template</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.templating.operators</code>.</p>
<p>The template operator supports the Jinja templating language. Documentation about Jinja can be found in the official <a href="https://jinja.palletsprojects.com/en/2.11.x/templates/">Template Designer Documentation</a>.</p>
<p>Currently, the template operator does have the following limitations: - As Jinja does not support special characters, such as colons, in variable names, RDF properties cannot be accessed. For this reason, the transformation that precedes the template operator needs to make sure that it generates attributes that are valid Jinja variable names. - Accessing nested paths is not supported. If the preceding transformation contains hierarchical mappings, only the attributes from the root mapping can be accessed.</p>
<h4 id="unpivot">Unpivot</h4>
<p>Given a list of table columns, transforms those columns into attribute-value pairs. This operator can be used in a workflow right after a mapping task.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>firstPivotProperty</td>
<td>String</td>
<td>The name of the first<br>
pivot column in the<br>
range.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>lastPivotProperty</td>
<td>String</td>
<td>the name of the last<br>
pivot column in the<br>
range. If left empty,<br>
all columns starting<br>
with the first pivot<br>
column are used.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>attributeProperty</td>
<td>String</td>
<td>The URI of the output<br>
column used to hold the<br>
attribute.</td>
<td>attribute</td>
</tr>
<tr class="even">
<td>valueProperty</td>
<td>String</td>
<td>The URI of the output<br>
column used to hold the<br>
value.</td>
<td>value</td>
</tr>
<tr class="odd">
<td>pivotColumns</td>
<td>String</td>
<td>Comma separated list of<br>
pivot column names. This<br>
property will override<br>
all inferred columns of<br>
the first two<br>
arguments.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Unpivot</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.unpivot</code>.</p>
<h4 id="parse-xml">Parse XML</h4>
<p>Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inputPath</td>
<td>String</td>
<td>The Silk path expression<br>
of the input entity that<br>
contains the XML<br>
document. If not set,<br>
the value of the first<br>
defined property will be<br>
taken.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>basePath</td>
<td>String</td>
<td>The path to the elements<br>
to be read, starting<br>
from the root element,<br>
e.g., ‘/Persons/Person’.<br>
If left empty, all<br>
direct children of the<br>
root element will be<br>
read.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>uriSuffixPattern</td>
<td>String</td>
<td>A URI pattern that is<br>
relative to the base URI<br>
of the input entity,<br>
e.g., /{ID}, where<br>
{path} may contain<br>
relative paths to<br>
elements. This relative<br>
part is appended to the<br>
input entity URI to<br>
construct the full URI<br>
pattern.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>XmlParserOperator</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.xml</code>.</p>
<h4 id="upload-file-to-knowledge-graph">Upload File to Knowledge Graph</h4>
<p>Uploads an N-Triples file from the file repository to a ‘Knowledge Graph’ dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. ‘Knowledge Graph’. The file will be uploaded to the graph specified in that dataset.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>fileNT</td>
<td>Resource</td>
<td>N-Triples file from the<br>
resource repository that<br>
should be uploaded to<br>
the Knowledge<br>
Graph.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>maxChunkSizeIn-<br>
MB</td>
<td>int</td>
<td>The N-Triples file will<br>
be split into multiple<br>
chunks if the file size<br>
exceeds the max chunk<br>
size.</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>eccencaDataPlatformGraphStoreFileUploadOperator</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.plugins.dataplatform</code>.</p>
<h4 id="script">Script</h4>
<p>A Scala script to be executed inside a workflow. The inputs are accessible using the ‘inputs: Seq[SparkEntities]’ variable. The result of the script must be a RDD[Entity] or SparkEntities instance to be returned as output.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>script</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>A Scala script to be<br>
executed inside a<br>
workflow.<br>
The inputs are accessible<br>
using the ‘inputs:<br>
Seq[SparkEntities]’<br>
variable,<br>
one entry for each input<br>
task of the script<br>
operator in the<br>
workflow.<br>
The return value of the<br>
script must be a<br>
RDD[Entity] or<br>
SparkEntities<br>
instance.</td>
<td>/* A Scala script to be<br>
executed inside a<br>
workflow.<br>
The inputs are<br>
accessible using the<br>
‘inputs: Seq[Spark-<br>
Entities]’ variable,<br>
one entry for each<br>
input task of the script<br>
operator in the<br>
workflow.<br>
The return value of<br>
the script must be a<br>
RDD[Entity] or<br>
SparkEntities<br>
instance.<br>
<br>
Further available<br>
parameters:<br>
task: Task[Spark-<br>
CustomSqlOperator] : the<br>
current task object, use<br>
this when ever a task is<br>
asked for<br>
…</td>
</tr>
<tr class="even">
<td>preserveOrder</td>
<td>boolean</td>
<td>If true, the origin order<br>
of input entities will<br>
be preserved for the<br>
resulting collection.<br>
This will decrease<br>
the performance and<br>
should only be used if<br>
the order s of<br>
importance.\</td>
<td>false</td>
</tr>
<tr class="odd">
<td>forceSpark</td>
<td>boolean</td>
<td>If true, the script is<br>
executed on Spark, even<br>
if local execution is<br>
configured.</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>script</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.scripttask</code>.</p>
<h4 id="sparql-construct-query">SPARQL Construct query</h4>
<p>A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>query</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>A SPARQL 1.1 construct<br>
query</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>tempFile</td>
<td>boolean</td>
<td>When copying directly to<br>
the same SPARQL Endpoint<br>
or when copying large<br>
amounts of triples, set<br>
to True by default</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>sparqlCopyOperator</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.tasks</code>.</p>
<h4 id="sparql-select-query">SPARQL Select query</h4>
<p>A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>selectQuery</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>A SPARQL 1.1 select<br>
query</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>limit</td>
<td>String</td>
<td>If set to a positive<br>
integer, the number of<br>
results is limited</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>optionalInput-<br>
Dataset</td>
<td>Sparql-<br>
Endpoint-<br>
Dataset-<br>
Parameter</td>
<td>An optional SPARQL<br>
dataset that can be used<br>
for example data, so<br>
e.g. the transformation<br>
editor shows mapping<br>
examples.</td>
<td></td>
</tr>
<tr class="even">
<td>sparqlTimeout</td>
<td>int</td>
<td>SPARQL query timeout<br>
(select/update) in<br>
milliseconds. A value of<br>
zero means that there is<br>
no timeout set<br>
explicitly. If a value<br>
greater zero is<br>
specified this<br>
overwrites possible<br>
default timeouts.</td>
<td>0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>sparqlSelectOperator</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.tasks</code>.</p>
<h4 id="sparql-update-query">SPARQL Update query</h4>
<p>A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template. The output of this operator should be connected to the SPARQL datasets to which the results should be written.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>sparqlUpdate-<br>
Template</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td><br>
This operator takes a<br>
SPARQL Update Query<br>
Template that depending<br>
on the templating mode<br>
(Simple/Velocity Engine)<br>
supports<br>
a set of templating<br>
features, e.g. filling<br>
in input values via<br>
placeholders in the<br>
template.<br>
<br>
Example for the ‘Simple’<br>
mode:<br>
<br>
DELETE DATA {<br>
${<PROP_FROM_ENTITY_SCHE<br>
MA1>} rdf:label<br>
${“PROP_FROM_ENTITY_SCHE<br>
MA2”} }<br>
INSERT DATA {<br>
${<PROP_FROM_ENTITY_SCHE<br>
MA1>} rdf:label<br>
${“PROP_FROM_ENTITY_SCHE<br>
MA3”} }<br>
<br>
…</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>batchSize</td>
<td>int</td>
<td>How many entities should<br>
be handled in a single<br>
update request.</td>
<td>1</td>
</tr>
<tr class="odd">
<td>templatingMode</td>
<td>Enum</td>
<td>The templating mode.<br>
‘Simple’ only allows<br>
simple URI and literal<br>
insertions, whereas<br>
‘Velocity Engine’<br>
supports complex<br>
templating. See ‘Sparql<br>
Update Template’<br>
parameter description<br>
for examples and<br>
http://velocity.apache.o<br>
rg for details on the<br>
Velocity templates.</td>
<td>simple</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>sparqlUpdateOperator</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.tasks</code>.</p>
<h4 id="request-rdf-triples">Request RDF triples</h4>
<p>A task that requests all triples from an RDF dataset.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>tripleRequestOperator</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.workflow.operators.tripleRequest</code>.</p>
<h4 id="normalize-units-of-measurement">Normalize units of measurement</h4>
<p>Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation in three columns: * The normalized numeric value. * The unit symbol of the SI-system-unit pertaining to the value. * The origin unit symbol from which it was normalized (so we are able to reverse this action).</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>valueProperties</td>
<td>String</td>
<td>The names (comma-separate<br>
d) of columns containing<br>
numeric values<br>
interpreted as<br>
quantities of the<br>
dimension indicated by<br>
the pertaining<br>
unit.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>unitProperties</td>
<td>String</td>
<td>The names (comma-separate<br>
d) of dedicated columns<br>
containing the unit<br>
symbol for the<br>
pertaining value in the<br>
value column (the<br>
positions in this list<br>
have to align with the<br>
pertaining value<br>
columns). Either this<br>
param or ‘static unit’<br>
has to be set.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>staticUnits</td>
<td>String</td>
<td>Unit symbols (comma-separ<br>
ated) defining the unit<br>
for all values in the<br>
pertaining value column.<br>
If set, the ‘unit-<br>
Property’ param will be<br>
ignored and all values<br>
of the value column have<br>
to be numbers without<br>
unit symbols (the<br>
positions in this list<br>
have to align with the<br>
pertaining value<br>
columns).</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>targetUnits</td>
<td>String</td>
<td>Unit symbols (comma-separ<br>
ated) defining the target<br>
unit to which the value<br>
column will be converted<br>
(Note: Make sure the<br>
input unit can be<br>
converted to the target<br>
unit). By default the<br>
pertaining SI-base unit<br>
will be used as<br>
normalization unit (the<br>
positions in this list<br>
have to align with the<br>
pertaining value<br>
columns)</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>suppressErrors</td>
<td>boolean</td>
<td>If true, will ignore any<br>
parsing or value<br>
conversion error and<br>
return an empty result<br>
(might happen because of<br>
unknown unit symbols or<br>
non-numbers as values).<br>
Beware, the value will<br>
be lost completely!</td>
<td>false</td>
</tr>
<tr class="even">
<td>configFilePath</td>
<td>Writable-<br>
Resource</td>
<td>An absolute file path for<br>
a unit CSV configuration<br>
file (for syntax see<br>
‘configuration’ param).<br>
If set, the ‘configurati<br>
on’ param will be<br>
ignored.</td>
<td>EmptyResource</td>
</tr>
<tr class="odd">
<td>configuration</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>While all SI units and<br>
decimal prefixes are<br>
supported by default,<br>
custom or obsolete units<br>
have to be added via<br>
this configuration.<br>
NOTE: when<br>
constructing formulae<br>
depending on other units<br>
defined in the<br>
configuration, make sure<br>
to order them<br>
dependently.<br>
ALSO: Rational<br>
numbers are not<br>
supported by the UCUM<br>
syntax, express them as<br>
a fraction (see ‘grain’<br>
example below).\</td>
<td><br>
# Example configuration,<br>
don’t forget to remove<br>
the ‘#’ in front of each<br>
row.<br>
# CSV COLUMNS:<br>
# * unit name - the<br>
human readable name of<br>
the unit<br>
# * override -<br>
(true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ucumNormalizationTask</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.measure</code>.</p>
<h4 id="xslt">XSLT</h4>
<p>A task that converts an XML resource via an XSLT script and writes the transformed output into a file resource.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Resource</td>
<td>The XSLT file to be used<br>
for transforming<br>
XML.</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>xsltOperator</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.xml</code>.</p>
<h2 id="dataset-plugins">Dataset Plugins</h2>
<p>The following dataset plugins are available:</p>
<h3 id="deprecated">Deprecated</h3>
<h4 id="sparksql-view">SparkSQL view</h4>
<p>Please use SQL endpoint (embedded) instead.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>viewName</td>
<td>String</td>
<td>The name of the view.<br>
This specifies the table<br>
that can be queried by<br>
another virtual dataset<br>
or via JDBC (the<br>
‘default’ schema is used<br>
for all virtual<br>
datasets).</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>query</td>
<td>String</td>
<td>Optional SQL query on the<br>
selected table. Has no<br>
effect when used as an<br>
output dataset.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>cache</td>
<td>boolean</td>
<td>Optional boolean option<br>
that selects if the<br>
table should be cached<br>
by Spark or not (default<br>
= true).</td>
<td>true</td>
</tr>
<tr class="even">
<td>uriPattern</td>
<td>String</td>
<td>A pattern used to<br>
construct the entity<br>
URI. If not provided the<br>
prefix + the line number<br>
is used. An example of<br>
such a pattern is<br>
‘urn:zyx:{id}’ where<br>
<em>id</em> is a name of a<br>
property.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>properties</td>
<td>String</td>
<td>Comma-separated list of<br>
URL-encoded properties.<br>
If not provided, the<br>
list of properties is<br>
read from the first<br>
line.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>charset</td>
<td>String</td>
<td>The source internal<br>
encoding, e.g., UTF8,<br>
ISO-8859-1</td>
<td>UTF-8</td>
</tr>
<tr class="odd">
<td>arraySeparator</td>
<td>String</td>
<td>The character that is<br>
used to separate the<br>
parts of array values.<br>
Write “back slash t” to<br>
specify the tab<br>
character.</td>
<td></td>
</tr>
<tr class="even">
<td>useCompatible-<br>
Types</td>
<td>boolean</td>
<td>If true, basic types will<br>
be used for types that<br>
otherwise would result<br>
in client errors. This<br>
mainly that arrays will<br>
be stored as Strings<br>
separated by the<br>
separator defined above.<br>
If the view is only for<br>
use within a<br>
SparkContext, this can<br>
be set to false.</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>sparkView</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.sql.virtual</code>.</p>
<h3 id="embedded">embedded</h3>
<h4 id="hive-database">Hive database</h4>
<p>Read from or write to an embedded Apache Hive endpoint.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>schema</td>
<td>String</td>
<td>Name of the hive schema<br>
or namespace.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>table</td>
<td>String</td>
<td>Name of the hive<br>
table.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>query</td>
<td>String</td>
<td>Optional query for<br>
projection and selection<br>
(e.g. " SELECT * FROM<br>
table WHERE x = true“.\</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>uriPattern</td>
<td>String</td>
<td>A pattern used to<br>
construct the entity<br>
URI. If not provided the<br>
prefix + the line number<br>
is used. An example of<br>
such a pattern is<br>
‘urn:zyx:{id}’ where<br>
<em>id</em> is a name of a<br>
property.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>properties</td>
<td>String</td>
<td>Comma-separated list of<br>
URL-encoded properties.<br>
If not provided, the<br>
list of properties is<br>
read from the first<br>
line.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>charset</td>
<td>String</td>
<td>The source internal<br>
encoding, e.g., UTF8,<br>
ISO-8859-1</td>
<td>UTF-8</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Hive</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark.dataset</code>.</p>
<h4 id="knowledge-graph">Knowledge Graph</h4>
<p>Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>endpoint</td>
<td>String</td>
<td>The named endpoint within<br>
the eccenca Data-<br>
Platform.</td>
<td>default</td>
</tr>
<tr class="even">
<td>graph</td>
<td>String</td>
<td>The URI of the named<br>
graph.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>pageSize</td>
<td>int</td>
<td>The number of solutions<br>
to be retrieved per<br>
SPARQL query.</td>
<td>100000</td>
</tr>
<tr class="even">
<td>pauseTime</td>
<td>int</td>
<td>The number of<br>
milliseconds to wait<br>
between subsequent<br>
query</td>
<td>0</td>
</tr>
<tr class="odd">
<td>retryCount</td>
<td>int</td>
<td>The number of retries if<br>
a query fails</td>
<td>3</td>
</tr>
<tr class="even">
<td>retryPause</td>
<td>int</td>
<td>The number of<br>
milliseconds to wait<br>
until a failed query is<br>
retried.</td>
<td>1000</td>
</tr>
<tr class="odd">
<td>strategy</td>
<td>Enum</td>
<td>The strategy use for<br>
retrieving entities:<br>
simple: Retrieve all<br>
entities using a single<br>
query; subQuery: Use a<br>
single query, but wrap<br>
it for improving the<br>
performance on Virtuoso;<br>
parallel: Use a separate<br>
Query for each entity<br>
property.</td>
<td>parallel</td>
</tr>
<tr class="even">
<td>clearGraphBefore-<br>
Execution</td>
<td>boolean</td>
<td>If set to true this will<br>
clear the specified<br>
graph before executing a<br>
workflow that writes to<br>
it.</td>
<td>false</td>
</tr>
<tr class="odd">
<td>entityList</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>A list of entities to be<br>
retrieved. If not given,<br>
all entities will be<br>
retrieved. Multiple<br>
entities are separated<br>
by whitespace.</td>
<td></td>
</tr>
<tr class="even">
<td>sparqlTimeout</td>
<td>int</td>
<td>SPARQL query timeout<br>
(select/update) in<br>
milliseconds. A value of<br>
zero means that there is<br>
no timeout. If a value<br>
greater zero is<br>
specified this<br>
overwrites possible<br>
default timeouts. This<br>
timeout is also<br>
propagated to<br>
DataPlatform and may<br>
overwrite default<br>
timeouts there.</td>
<td>0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>eccencaDataPlatform</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.plugins.dataplatform</code>.</p>
<h4 id="in-memory-dataset">In-memory dataset</h4>
<p>A Dataset that holds all data in-memory.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>clearGraphBefore-<br>
Execution</td>
<td>boolean</td>
<td>If set to true this will<br>
clear this dataset<br>
before it is used in a<br>
workflow execution.</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>inMemory</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.datasets</code>.</p>
<h4 id="internal-dataset">Internal dataset</h4>
<p>Dataset for storing entities between workflow steps.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>graphUri</td>
<td>String</td>
<td>The RDF graph that is<br>
used for storing<br>
internal data</td>
<td><em>null</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>internal</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset</code>.</p>
<h4 id="sql-endpoint">SQL endpoint</h4>
<p>Provides a JDBC endpoint that exposes workflow or transformation results as tables, which can be queried using SQL.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>tableNamePrefix</td>
<td>String</td>
<td>Prefix of the table that<br>
will be shared. In the<br>
case of complex mappings<br>
more than one table will<br>
be created. If one name<br>
is given it will be used<br>
as a prefix for table<br>
names. If left empty the<br>
table names will be<br>
generated from the user<br>
name and time stamps and<br>
start with ‘root’,<br>
‘object-mapping’</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>cache</td>
<td>boolean</td>
<td>Optional boolean option<br>
that selects if the<br>
table should be cached<br>
by Spark or not (default<br>
= true).</td>
<td>true</td>
</tr>
<tr class="odd">
<td>arraySeparator</td>
<td>String</td>
<td>The character that is<br>
used to separate the<br>
parts of array values.<br>
Write \t to specify the<br>
tab character.</td>
<td></td>
</tr>
<tr class="even">
<td>useCompatible-<br>
Types</td>
<td>boolean</td>
<td>If true, basic types will<br>
be used for unusual data<br>
types that otherwise may<br>
result in client errors.<br>
Try switching this on,<br>
if a client has weird<br>
error messages. (Default<br>
= true)</td>
<td>true</td>
</tr>
<tr class="odd">
<td>map</td>
<td>Map</td>
<td>Mapping of column names.<br>
Similar to aliases E.g.<br>
‘c1:c2’ would rename<br>
column c1 into<br>
c2.</td>
<td>Map()</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>sqlEndpoint</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.sql.endpoint</code>.</p>
<p><em>SQL endpoint dataset parameters</em></p>
<p>The dataset only requires that the <em>tableNamePrefix</em> parameter is given. This will be used as the prefix for the names of the generated tables. When a set of entities is written to the endpoint <em>a view is generated for each entity type</em> (defined by an ‘rdf_type’ attribute). That means that the mapping or data source that are used as input for the SQL endpoint need to have a type or require a user defined type mapping.</p>
<p>The operator has a <em>compatibility mode</em>. This mode will avoid complex types such as Arrays. When arrays exist in the input they are converted to a String using the given <em>arraySeparator</em>. This avoids errors and warnings in some Jdbc clients that are unable to handle typed arrays and may make working with software like Excel easier.</p>
<p>The parameter <em>aliasMap</em> of the endpoint allows the specification of column aliases. The map is a comma separated list of key-value pairs. Each key and value is denoted by <code>key:value</code>. An example for renaming 2 columns (source1, source2 to target1, target2) in the result would be: <code>source1:target1,source2:target2</code></p>
<p class="alert-info">Note: Table and column (mapping target) names will be automatically converted to be valid in as many databases as possible. Table names will be shortened to 128 characters. Only a-z, A-Z, 0-9 and _ are allowed. Others will be replaced with an underscore. Column names undergo the same transformation but will be converted to lower case as well. The log will inform about changes. The table names will be generated based on the target type of each mapping. The user needs to make sure that each object mapping specifies a unique type. If two object mappings define the same type, only the last one will be written.</p>
<p><em>SQL endpoint activity</em></p>
<p>See [ActivityDocumentation] for a general description of the Data Integration activities. The activity will <em>start</em> automatically, when the SQL endpoint is used as a data sink and Data Integration is configured to make the SQL endpoint accessible remotely.</p>
<p>When the activity is started and <em>running</em> it returns the server status and JDBC URL as its value.</p>
<p><em>Stopping</em> the activity will drop all views generated by the activity. It can be <em>restarted</em> by rerunning the workflow containing it as a sink.</p>
<p><em>Remote client configuration (via JDBC and ODBC)</em></p>
<p>Within Data Integration the SQL endpoint can be used as a source or sink like any other dataset. If the <em>startThriftServer</em> option is set to ‘true’ access via JDBC or ODBC is possible.</p>
<p><a href="https://en.wikipedia.org/wiki/Open_Database_Connectivity">ODBC</a> and <a href="https://en.wikipedia.org/wiki/Java_Database_Connectivity">JDBC</a> drivers can be used to connect to relational databases.</p>
<p>When selecting a version of a driver the client operating system and its type (32bit/64 bit) are the most important factors. The version of the client drivers sometimes is the same as the server’s. If no version of a driver is given, the newest driver of the vendor should work, as it <em>should</em> be backwards compatible.</p>
<p>Any JDBC or ODBC client can connect to an SQL endpoint dataset. SparkSQL uses the same query processing as Hive, therefore the requirements for the client are:</p>
<ul>
<li>A JDBC driver compatible with <em>Hive 1.2.1</em><a href="#fn1" class="footnote-ref" id="fnref1"><sup>1</sup></a> (platform independent driver <em>org.apache.hive.jdbc.HiveDriver</em> is needed) or</li>
<li>A JDBC driver compatible with <em>Spark 2.3.3</em></li>
<li>A Hive ODBC driver (ODBC driver for the client architecture and operating system needed)</li>
</ul>
<p>A detailed instruction to connect to a Hive or SparkSQL endpoint with various tools (e.g. SQuirreL, beeline, SQL Developer, …) can be found at <em><a href="https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients">Apache HiveServer2 Clients</a></em>. The database client <em><a href="https://dbeaver.io/">DBeaver</a></em> can connect to the SQL endpoint out of the box.</p>
<h4 id="variable-dataset">Variable dataset</h4>
<p>Dataset that acts as a placeholder in workflows and is replaced at request time.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>variableDataset</code>.</p>
<p>It can be found in the package <code>org.silkframework.dataset</code>.</p>
<h3 id="file">file</h3>
<h4 id="alignment">Alignment</h4>
<p>Writes the alignment format specified at http://alignapi.gforge.inria.fr/format.html.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>The alignment<br>
file.</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>alignment</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.datasets</code>.</p>
<h4 id="avro">Avro</h4>
<p>Read from or write to an Apache Avro file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>Path (e.g. relative like<br>
‘path/filename.avro’ or<br>
absolute ‘hdfs:///path/<br>
filename.avro’).</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>uriPattern</td>
<td>String</td>
<td>A pattern used to<br>
construct the entity<br>
URI. If not provided the<br>
prefix + the line number<br>
is used. An example of<br>
such a pattern is<br>
‘urn:zyx:{id}’ where<br>
<em>id</em> is a name of a<br>
property.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>properties</td>
<td>String</td>
<td>Comma-separated list of<br>
URL-encoded properties.<br>
If not provided, the<br>
list of properties is<br>
read from the first<br>
line.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>charset</td>
<td>String</td>
<td>The file encoding, e.g.,<br>
UTF8, ISO-8859-1</td>
<td>UTF-8</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>avro</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark.dataset</code>.</p>
<h4 id="csv">CSV</h4>
<p>Read from or write to an CSV file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>The CSV file. This may<br>
also be a zip archive of<br>
multiple CSV files that<br>
share the same<br>
schema.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>properties</td>
<td>String</td>
<td>Comma-separated list of<br>
URL-encoded properties.<br>
If not provided, the<br>
list of properties is<br>
read from the first<br>
line.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>separator</td>
<td>String</td>
<td>The character that is<br>
used to separate values.<br>
If not provided,<br>
defaults to ‘,’, i.e.,<br>
comma-separated values.<br>
“\t” for specifying<br>
tab-separated values, is<br>
also supported.</td>
<td>,</td>
</tr>
<tr class="even">
<td>arraySeparator</td>
<td>String</td>
<td>The character that is<br>
used to separate the<br>
parts of array values.<br>
Write “\t” to specify<br>
the tab character.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>quote</td>
<td>String</td>
<td>Character used to quote<br>
values.</td>
<td>“</td>
</tr>
<tr class="even">
<td>uri</td>
<td>String</td>
<td><em>Deprecated</em> A pattern<br>
used to construct the<br>
entity URI. If not<br>
provided the prefix +<br>
the line number is used.<br>
An example of such a<br>
pattern is ‘urn:zyx:{id}<br>
’ where <em>id</em> is a name of<br>
a property.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>charset</td>
<td>String</td>
<td>The file encoding, e.g.,<br>
UTF-8, UTF-8-BOM,<br>
ISO-8859-1</td>
<td>UTF-8</td>
</tr>
<tr class="even">
<td>regexFilter</td>
<td>String</td>
<td>A regex filter used to<br>
match rows from the CSV<br>
file. If not set all the<br>
rows are used.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>linesToSkip</td>
<td>int</td>
<td>The number of lines to<br>
skip in the beginning,<br>
e.g. copyright, meta<br>
information etc.</td>
<td>0</td>
</tr>
<tr class="even">
<td>maxCharsPer-<br>
Column</td>
<td>int</td>
<td>The maximum characters<br>
per column. <em>Warning</em>:<br>
System will request heap<br>
memory of that size (2<br>
bytes per character)<br>
when reading the CSV. If<br>
there are more<br>
characters found, the<br>
parser will fail.</td>
<td>128000</td>
</tr>
<tr class="odd">
<td>ignoreBadLines</td>
<td>boolean</td>
<td>If set to true then the<br>
parser will ignore lines<br>
that have syntax errors<br>
or do not have to<br>
correct number of fields<br>
according to the current<br>
config.</td>
<td>false</td>
</tr>
<tr class="even">
<td>quoteEscape-<br>
Character</td>
<td>String</td>
<td>Escape character to be<br>
used inside quotes, used<br>
to escape the quote<br>
character. It must also<br>
be used to escape<br>
itself, e.g. by doubling<br>
it, e.g. “”. If left<br>
empty, it defaults to<br>
quote.</td>
<td>“</td>
</tr>
<tr class="odd">
<td>zipFileRegex</td>
<td>String</td>
<td>If the input resource is<br>
a ZIP file, files inside<br>
the file are filtered<br>
via this regex.</td>
<td>.*\.csv$</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>csv</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.csv</code>.</p>
<h4 id="excel">Excel</h4>
<p>Read from or write to an Excel workbook in Open XML format (XLSX).</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>File name inside the<br>
resources directory.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>streaming</td>
<td>boolean</td>
<td>Streaming enables reading<br>
and writing large Excels<br>
files. Warning: Be<br>
careful to disable<br>
streaming for large<br>
datasets (> 10MB),<br>
because of high memory<br>
consumption.</td>
<td>true</td>
</tr>
<tr class="odd">
<td>linesToSkip</td>
<td>int</td>
<td>The number of lines to<br>
skip in the beginning<br>
when reading<br>
files.</td>
<td>0</td>
</tr>
<tr class="even">
<td>outputObject-<br>
Values</td>
<td>boolean</td>
<td>Output results from<br>
object rules<br>
(URIs).</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>excel</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="rdf">RDF</h4>
<p>Dataset which retrieves and writes all entities from/to an RDF file. The dataset is loaded in-memory and thus the size is restricted by the available memory. Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>The RDF file. This may<br>
also be a zip archive of<br>
multiple RDF<br>
files.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>format</td>
<td>String</td>
<td>RDF format. Can be left<br>
empty, in which case it<br>
will be auto-detetected<br>
based on the file<br>
extension. Supported<br>
input formats are:<br>
“RDF/XML”, “N-Triples”,<br>
“N-Quads”, “Turtle”.<br>
Supported output formats<br>
are: “N-Triples”.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>graph</td>
<td>String</td>
<td>The graph name to be<br>
read. If not provided,<br>
the default graph will<br>
be used. Must be<br>
provided if the format<br>
is N-Quads.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>maxReadSize</td>
<td>long</td>
<td>The maximum size of the<br>
RDF file resource for<br>
read operations. Since<br>
the whole dataset will<br>
be kept in-memory, this<br>
value should be kept low<br>
to guarantee<br>
stability.</td>
<td>10</td>
</tr>
<tr class="odd">
<td>entityList</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>A list of entities to be<br>
retrieved. If not given,<br>
all entities will be<br>
retrieved. Multiple<br>
entities are separated<br>
by whitespace.</td>
<td></td>
</tr>
<tr class="even">
<td>zipFileRegex</td>
<td>String</td>
<td>If the input resource is<br>
a ZIP file, files inside<br>
the file are filtered<br>
via this regex.</td>
<td>.*</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>file</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.datasets</code>.</p>
<h4 id="json">JSON</h4>
<p>Read from or write to a JSON file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Resource</td>
<td>Json file.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>basePath</td>
<td>String</td>
<td>The path to the elements<br>
to be read, starting<br>
from the root element,<br>
e.g., ‘/Persons/Person’.<br>
If left empty, all<br>
direct children of the<br>
root element will be<br>
read.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>uriPattern</td>
<td>String</td>
<td>A URI pattern, e.g.,<br>
http://namespace.org/<br>
{ID}, where {path} may<br>
contain relative paths<br>
to elements</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>json</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.json</code>.</p>
<p>Typically, this dataset is used to transform an JSON file to another format, e.g., to RDF.</p>
<p>It supports a number of special paths: - <code>#id</code> Is a special syntax for generating an id for a selected element. It can be used in URI patterns for entities which do not provide an identifier. Examples: <code>http://example.org/{#id}</code> or <code>http://example.org/{/pathToEntity/#id}</code>. - <code>#text</code> retrieves the text of the selected node. - The backslash can be used to navigate to the parent JSON node, e.g., <code>\parent/key</code>. The name of the backslash key (here <code>parent</code>) is ignored.</p>
<h4 id="multi-csv-zip">Multi CSV ZIP</h4>
<p>Reads from or writes to multiple CSV files from/to a single ZIP file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>Zip file name inside the<br>
resources directory/<br>
repository.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>separator</td>
<td>String</td>
<td>The character that is<br>
used to separate values.<br>
If not provided,<br>
defaults to ‘,’, i.e.,<br>
comma-separated values.<br>
“\t” for specifying<br>
tab-separated values, is<br>
also supported.</td>
<td>,</td>
</tr>
<tr class="odd">
<td>arraySeparator</td>
<td>String</td>
<td>The character that is<br>
used to separate the<br>
parts of array values.<br>
Write “\t” to specify<br>
the tab character.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>quote</td>
<td>String</td>
<td>Character used to quote<br>
values.</td>
<td>“</td>
</tr>
<tr class="odd">
<td>charset</td>
<td>String</td>
<td>The file encoding, e.g.,<br>
UTF8, ISO-8859-1</td>
<td>UTF-8</td>
</tr>
<tr class="even">
<td>linesToSkip</td>
<td>int</td>
<td>The number of lines to<br>
skip in the beginning,<br>
e.g. copyright, meta<br>
information etc.</td>
<td>0</td>
</tr>
<tr class="odd">
<td>maxCharsPer-<br>
Column</td>
<td>int</td>
<td>The maximum characters<br>
per column. If there are<br>
more characters found,<br>
the parser will<br>
fail.</td>
<td>128000</td>
</tr>
<tr class="even">
<td>ignoreBadLines</td>
<td>boolean</td>
<td>If set to true then the<br>
parser will ignore lines<br>
that have syntax errors<br>
or do not have to<br>
correct number of fields<br>
according to the current<br>
config.</td>
<td>false</td>
</tr>
<tr class="odd">
<td>quoteEscape-<br>
Character</td>
<td>String</td>
<td>Escape character to be<br>
used inside quotes, used<br>
to escape the quote<br>
character. It must also<br>
be used to escape<br>
itself, e.g. by doubling<br>
it, e.g. “”. If left<br>
empty, it defaults to<br>
quote.</td>
<td>“</td>
</tr>
<tr class="even">
<td>append</td>
<td>boolean</td>
<td>If ‘True’ then files in<br>
the ZIP archive are only<br>
added or updated, all<br>
other files in the ZIP<br>
stay untouched. If<br>
‘False’ then a new ZIP<br>
file will be created on<br>
every dataset<br>
write.</td>
<td>true</td>
</tr>
<tr class="odd">
<td>zipFileRegex</td>
<td>String</td>
<td>Filter file paths inside<br>
the ZIP file via this<br>
regex. By default sub<br>
folders or files not<br>
ending with .csv are<br>
ignored.</td>
<td><a href="#fn2" class="footnote-ref" id="fnref2"><sup>2</sup></a>*\.csv$</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>multiCsv</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.plugins.csv</code>.</p>
<h4 id="orc">ORC</h4>
<p>Read from or write to an Apache ORC file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>Path (e.g. relative like<br>
‘path/filename.orc’ or<br>
absolute ‘hdfs:///path/<br>
filename.orc’).</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>uriPattern</td>
<td>String</td>
<td>A pattern used to<br>
construct the entity<br>
URI. If not provided the<br>
prefix + the line number<br>
is used. An example of<br>
such a pattern is<br>
‘urn:zyx:{id}’ where<br>
<em>id</em> is a name of a<br>
property.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>properties</td>
<td>String</td>
<td>Comma-separated list of<br>
URL-encoded properties.<br>
If not provided, the<br>
list of properties is<br>
read from the first<br>
line.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>partition</td>
<td>String</td>
<td>Optional specification of<br>
the attribute for output<br>
partitioning</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>compression</td>
<td>String</td>
<td>Optional compression<br>
algorithm (e.g. snappy,<br>
zlib)</td>
<td>snappy</td>
</tr>
<tr class="even">
<td>charset</td>
<td>String</td>
<td>The file encoding, e.g.,<br>
UTF8, ISO-8859-1</td>
<td>UTF-8</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>orc</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark.dataset</code>.</p>
<h4 id="parquet">Parquet</h4>
<p>Read from or write to an Apache Parquet file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>Path (e.g. relative like<br>
‘path/filename.orc’ or<br>
absolute ‘hdfs:///path/<br>
filename.parquet’).</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>uriPattern</td>
<td>String</td>
<td>A pattern used to<br>
construct the entity<br>
URI. If not provided the<br>
prefix + the line number<br>
is used. An example of<br>
such a pattern is<br>
‘urn:zyx:{id}’ where<br>
<em>id</em> is a name of a<br>
property.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>properties</td>
<td>String</td>
<td>Comma-separated list of<br>
URL-encoded properties.<br>
If not provided, the<br>
list of properties is<br>
read from the first<br>
line.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>partition</td>
<td>String</td>
<td>Optional specification of<br>
the attribute for output<br>
partitioning</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>compression</td>
<td>String</td>
<td>Optional compression<br>
algorithm (e.g. snappy,<br>
zlib)</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>charset</td>
<td>String</td>
<td>The file encoding, e.g.,<br>
UTF8, ISO-8859-1</td>
<td>UTF-8</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>parquet</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark.dataset</code>.</p>
<h4 id="xml-1">XML</h4>
<p>Read from or write to an XML file.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file</td>
<td>Writable-<br>
Resource</td>
<td>The XML file. This may<br>
also be a zip archive of<br>
multiple XML files that<br>
share the same<br>
schema.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>basePath</td>
<td>String</td>
<td>The base path when<br>
writing XML. For<br>
instance: /RootElement/<br>
Entity. Should no longer<br>
be used for reading XML!<br>
Instead, set the base<br>
path by specifying it as<br>
input type on the<br>
subsequent transformatio<br>
n or linking tasks.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>uriPattern</td>
<td>String</td>
<td>A URI pattern, e.g.,<br>
http://namespace.org/<br>
{ID}, where {path} may<br>
contain relative paths<br>
to elements</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>outputTemplate</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>The output template used<br>
for writing XML. Must be<br>
valid XML. The generated<br>
entity is identified<br>
through a processing<br>
instruction of the form<br>
<!--?MyEntity ?-->.</td>
<td><root><!--?Entity ?--></<br>
Root></root></td>
</tr>
<tr class="odd">
<td>streaming</td>
<td>boolean</td>
<td>Streaming allows for<br>
reading large XML<br>
files.</td>
<td>true</td>
</tr>
<tr class="even">
<td>zipFileRegex</td>
<td>String</td>
<td>If the input resource is<br>
a ZIP file, files inside<br>
the file are filtered<br>
via this regex.</td>
<td>.*\.xml$</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>xml</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.xml</code>.</p>
<p>Typically, this dataset is used to transform an XML file to another format, e.g., to RDF. When this dataset is used as an input for another task (e.g., a transformation task), the input type of the consuming task selects the path where the entities to be read are located.</p>
<p>Example:</p>
<pre><code><Persons>
  <Person>
    <Name>John Doe</Name>
    <Year>1970</Year>
  </Person>
  <Person>
    <Name>Max Power</Name>
    <Year>1980</Year>
  </Person>
</Persons></code></pre>
<p>A transformation for reading all persons of the above XML would set the input type to <code>/Person</code>. The transformation iterates all entities matching the given input path. In the above example the first entity to be read is:</p>
<pre><code><Person>
  <Name>John Doe</Name>
  <Year>1970</Year>
</Person></code></pre>
<p>All paths used in the consuming task are relative to this, e.g., the person name can be addressed with the path <code>/Name</code>.</p>
<p>Path examples:</p>
<ul>
<li>The empty path selects the root element.</li>
<li><code>/Person</code> selects all persons.</li>
<li><code>/Person[Year = "1970"]</code> selects all persons which are born in 1970.</li>
<li><code>/#id</code> Is a special syntax for generating an id for a selected element. It can be used in URI patterns for entities which do not provide an identifier. Examples: <code>http://example.org/{#id}</code> or <code>http://example.org/{/pathToEntity/#id}</code>.</li>
<li>The wildcard * enumerates all direct children, e.g., <code>/Persons/*/Name</code>.</li>
<li>The wildcard ** enumerates all direct and indirect children.</li>
<li>The backslash can be used to navigate to the parent XML node, e.g., <code>\Persons/SomeHeader</code>.</li>
<li><code>#text</code> retrieves the text of the selected node.</li>
</ul>
<h3 id="remote">remote</h3>
<h4 id="jdbc-endpoint">JDBC endpoint</h4>
<p>Connect to an existing JDBC endpoint.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>url</td>
<td>String</td>
<td>JDBC URL, e.g.,<br>
jdbc:mysql://<br>
localhost:port/<br>
databaseName</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>table</td>
<td>String</td>
<td>Table name. Can be empty<br>
if the read-strategy is<br>
not set to read the full<br>
table. If non-empty it<br>
has to contain at least<br>
an existing table.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>sourceQuery</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>Source query (e.g.<br>
‘SELECT TOP 10 * FROM<br>
table WHERE x = true’.<br>
Warning: Uses Driver<br>
(mySql, HiveQL, MSSql,<br>
Postgres) specific<br>
syntax. Can be left<br>
empty when full tables<br>
are loaded. Note: Even<br>
if columns with<br>
spaces/special<br>
characters are named in<br>
the query, they need to<br>
be referred to<br>
URL-encoded in<br>
subsequent transformatio<br>
ns.</td>
<td></td>
</tr>
<tr class="even">
<td>groupBy</td>
<td>String</td>
<td>Comma separated list of<br>
attributes appearing in<br>
the outer SELECT clause<br>
that should be grouped<br>
by. The attributes are<br>
matched case-insensitive<br>
. All other attributes<br>
will be grouped via an<br>
aggregation function<br>
that depends on the<br>
supported DBMS, e.g.<br>
(JSON) array<br>
aggregation.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>limit</td>
<td>IntOption-<br>
Parameter</td>
<td>Optional limit of<br>
returned records. This<br>
limit should be pushed<br>
to the source. No value<br>
implies that no limit<br>
will be applied.</td>
<td>IntOptionParameter(Some(1<br>
0))</td>
</tr>
<tr class="even">
<td>queryStrategy</td>
<td>Enum</td>
<td>Query strategy. The<br>
strategy decides how the<br>
source system is<br>
queried. Possible values<br>
are: ‘access-complete-ta<br>
ble’ and ‘query’.</td>
<td>completeTable</td>
</tr>
<tr class="odd">
<td>writeStrategy</td>
<td>Enum</td>
<td>Write strategy. If this<br>
dataset is a sink, it<br>
can be selected if data<br>
is overwritten or<br>
appended. Possible<br>
values are: ‘update-tabl<br>
e’ and ‘overwrite-table’</td>
<td>defaultStrategy</td>
</tr>
<tr class="even">
<td>user</td>
<td>String</td>
<td>Username</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>password</td>
<td>Password-<br>
Parameter</td>
<td>Password</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>restriction</td>
<td>String</td>
<td>A SQL WHERE clause to<br>
filter the records to be<br>
retrieved.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>retries</td>
<td>int</td>
<td>Optional number of<br>
retries per query</td>
<td>0</td>
</tr>
<tr class="even">
<td>pause</td>
<td>int</td>
<td>Optional pause between<br>
queries in ms.</td>
<td>2000</td>
</tr>
<tr class="odd">
<td>charset</td>
<td>String</td>
<td>The source internal<br>
encoding, e.g., UTF-8,<br>
ISO-8859-1</td>
<td>UTF-8</td>
</tr>
<tr class="even">
<td>forceSparkExecution</td>
<td>boolean</td>
<td>If set to true, Spark<br>
will be used for<br>
querying the database,<br>
even if the local<br>
execution manager is<br>
configured.</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Jdbc</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.sql.jdbc</code>.</p>
<p><em>General usage</em></p>
<p>The JDBC dataset supports connections to Hive, Microsoft SQL Server, MySQL, Oracle Database, DB2 and PostgreSQL databases. A login and password and JDBC URL need to be provided. This dataset supports queries or simply schema and table names to define what should be retrieved from a source DB. If the dataset is used as a sink, queries are ignored and only schema and table parameters are used. If the dataset is used as a sink for a hierarchical mapping it behaves similar to the SqlEndpoint: One table is generated per entity type.</p>
<p>The names of the written tables are generated as follows:</p>
<ul>
<li>The table name of the root mapping is defined by the table parameter of the dataset. If the table name is empty, a name is generated from the first type of the mapping. Special characters are removed and the name shortened to maximum of 128 characters.</li>
<li>For each object mapping, the table name is generated from its type.</li>
</ul>
<p><em>Read and write strategies</em></p>
<p>There are multiple read and write strategies which can be selected depending on the purpose of the dataset in a workflow.</p>
<p>Read strategies decide how the database is queried:</p>
<ul>
<li>full-table: Queries or wraps a complete table. Only the DB schema and table name need to be set</li>
<li>query: The given source query is passed along to the database. The table name is not necessary in this case but a valid query in the SQL-dialect of the source database system must be provided.</li>
</ul>
<p>Write strategies decide how a new table is written:</p>
<ul>
<li>default: An error will occur if the table exists. If not a new one will be created.</li>
<li>overwrite: The old table will be removed and a new one will be created.</li>
<li>append: Data will be appended to the existing table. The schema of the data written has to be the same as the existing table schema.</li>
</ul>
<p><em>Optimized Writing</em></p>
<p>Usually specific database systems have custom commands for loading large amounts of data, e.g. from a CSV file into a database table. For some DBMS and specific JDBC dataset configurations we support these optimized methods of loading data.</p>
<p>Supported DBMS:</p>
<ul>
<li>MySQL and MariaDB (full support for versions 8.0.19+ and 10.4+, resp.):
<ul>
<li>if older DBMS versions are used some dataset options like ‘groupBy’ might not be supported but equivalent queries will</li>
<li>the same is true when older driver jars then the one provided by eccenca are used</li>
<li>both use the MariaDB JDBC driver</li>
<li>uses <code>LOAD DATA LOCAL INFILE</code> internally</li>
<li>only applies when appending data to an existing table and having <code>Force Spark Execution</code> disabled</li>
<li>Both the server parameter <code>local_infile</code> and the client parameter <code>allowLoadLocalInfile</code> must be enabled, e.g. by adding <code>allowLoadLocalInfile=true</code> to the JDBC URL. For MySQL starting with version 8 the <code>local_infile</code> parameter is by default disabled!</li>
</ul></li>
</ul>
<p><em>Registering JDBC drivers</em></p>
<p>More 3rd party databases are supported via adding their JDBC drivers to the classpath of Data Integration. Drivers are usually provided by the database manufactures. If 32 bit and 64 bit versions are provided the latter is usually needed and should aways equal the bit-level of the JVM. To make sure that the drivers are loaded correctly their class name (in case are jar contains multiple drivers) and location in the file system can be set with the <em>spark.sql.options.jdbc</em> option in the <code>dataintegration.conf</code> configuration file.</p>
<p>An example for adding both the DB2 and MySQL drivers to Data Integration configuration file <code>spark.sql.options.*</code> section:</p>
<pre class="raml"><code>spark.sql.options {

  ...

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
}</code></pre>
<p>Recommended DBMS versions:</p>
<p>Microsoft SQL Server 2017: Older versions might work, but do not support the <code>groupBy</code> parameter. PostgreSQL 9.5: The <code>groupBy</code> parameter needs at least version 8.4. MySQL v8.0.19: Older versions do not support the <code>groupBy</code> parameter. DB2 v11.5.x: The <code>groupBy</code> feature needs at least version 9.7 to function. Oracle 12.2.x: The <code>groupBy</code> feature does not work for versions prior to 11g Release 2.</p>
<p>These limitations are the same for JDBC drivers that are older than the fully supported databases. Queries can achieve a similar outcome if <code>groupBy</code> is not supported.</p>
<h4 id="sparql-endpoint">SPARQL endpoint</h4>
<p>Connect to an existing SPARQL endpoint.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>endpointURI</td>
<td>String</td>
<td>The URI of the SPARQL<br>
endpoint, e.g.,<br>
http://dbpedia.org/<br>
sparql</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>login</td>
<td>String</td>
<td>Login required for<br>
authentication</td>
<td><em>null</em></td>
</tr>
<tr class="odd">
<td>password</td>
<td>Password-<br>
Parameter</td>
<td>Password required for<br>
authentication</td>
<td></td>
</tr>
<tr class="even">
<td>graph</td>
<td>String</td>
<td>Only retrieve entities<br>
from a specific<br>
graph</td>
<td><em>null</em></td>
</tr>
<tr class="odd">
<td>pageSize</td>
<td>int</td>
<td>The number of solutions<br>
to be retrieved per<br>
SPARQL query.</td>
<td>1000</td>
</tr>
<tr class="even">
<td>entityList</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>A list of entities to be<br>
retrieved. If not given,<br>
all entities will be<br>
retrieved. Multiple<br>
entities are separated<br>
by whitespace.</td>
<td></td>
</tr>
<tr class="odd">
<td>pauseTime</td>
<td>int</td>
<td>The number of<br>
milliseconds to wait<br>
between subsequent<br>
query</td>
<td>0</td>
</tr>
<tr class="even">
<td>retryCount</td>
<td>int</td>
<td>The number of retries if<br>
a query fails</td>
<td>3</td>
</tr>
<tr class="odd">
<td>retryPause</td>
<td>int</td>
<td>The number of<br>
milliseconds to wait<br>
until a failed query is<br>
retried.</td>
<td>1000</td>
</tr>
<tr class="even">
<td>queryParameters</td>
<td>String</td>
<td>Additional parameters to<br>
be appended to every<br>
request e.g.<br>
&soft-limit=1</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>strategy</td>
<td>Enum</td>
<td>The strategy use for<br>
retrieving entities:<br>
simple: Retrieve all<br>
entities using a single<br>
query; subQuery: Use a<br>
single query, but wrap<br>
it for improving the<br>
performance on Virtuoso;<br>
parallel: Use a separate<br>
Query for each entity<br>
property.</td>
<td>parallel</td>
</tr>
<tr class="even">
<td>useOrderBy</td>
<td>boolean</td>
<td>Include useOrderBy in<br>
queries to enforce<br>
correct order of<br>
values.</td>
<td>true</td>
</tr>
<tr class="odd">
<td>clearGraphBefore-<br>
Execution</td>
<td>boolean</td>
<td>If set to true this will<br>
clear the specified<br>
graph before executing a<br>
workflow that writes to<br>
it.</td>
<td>false</td>
</tr>
<tr class="even">
<td>sparqlTimeout</td>
<td>int</td>
<td>SPARQL query timeout<br>
(select/update) in<br>
milliseconds. A value of<br>
zero means that the<br>
timeout configured via<br>
property is used (e.g.<br>
configured via<br>
silk.remoteSparql-<br>
Endpoint.defaults.read.ti<br>
meout.ms). To overwrite<br>
the configured value<br>
specify a value greater<br>
than zero.</td>
<td>0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>sparqlEndpoint</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.dataset.rdf.datasets</code>.</p>
<h2 id="distance-measures">Distance Measures</h2>
<p>The following distance measures are available:</p>
<h3 id="asian">Asian</h3>
<h4 id="cjk-reading-distance">CJK reading distance</h4>
<p>CJK Reading Distance.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minChar</td>
<td>char</td>
<td>No description</td>
<td>0</td>
</tr>
<tr class="even">
<td>maxChar</td>
<td>char</td>
<td>No description</td>
<td>z</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>cjkReadingDistance</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.asian</code>.</p>
<h4 id="korean-phoneme-distance">Korean phoneme distance</h4>
<p>Korean phoneme distance.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minChar</td>
<td>char</td>
<td>No description</td>
<td>0</td>
</tr>
<tr class="even">
<td>maxChar</td>
<td>char</td>
<td>No description</td>
<td>z</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>koreanPhonemeDistance</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.asian</code>.</p>
<h4 id="korean-translit-distance">Korean translit distance</h4>
<p>Transliterated Korean distance.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minChar</td>
<td>char</td>
<td>No description</td>
<td>0</td>
</tr>
<tr class="even">
<td>maxChar</td>
<td>char</td>
<td>No description</td>
<td>z</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>koreanTranslitDistance</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.asian</code>.</p>
<h3 id="characterbased">Characterbased</h3>
<p>Character-based distance measures compare strings on the character level. They are well suited for handling typographical errors.</p>
<h4 id="is-substring">Is substring</h4>
<p>Checks if a source value is a substring of a target value.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>reverse</td>
<td>boolean</td>
<td>Reverse source and target<br>
inputs</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>isSubstring</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="jaro-distance">Jaro distance</h4>
<p>String similarity based on the Jaro distance metric.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>jaro</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="jaro-winkler-distance">Jaro-Winkler distance</h4>
<p>String similarity based on the Jaro-Winkler distance measure.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>jaroWinkler</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="normalized-levenshtein-distance">Normalized Levenshtein distance</h4>
<p>Normalized Levenshtein distance.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minChar</td>
<td>char</td>
<td>The minimum character<br>
that is used for<br>
indexing</td>
<td>0</td>
</tr>
<tr class="even">
<td>maxChar</td>
<td>char</td>
<td>The maximum character<br>
that is used for<br>
indexing</td>
<td>z</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>levenshtein</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="levenshtein-distance">Levenshtein distance</h4>
<p>Levenshtein distance. Returns a distance value between zero and the size of the string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minChar</td>
<td>char</td>
<td>The minimum character<br>
that is used for<br>
indexing</td>
<td>0</td>
</tr>
<tr class="even">
<td>maxChar</td>
<td>char</td>
<td>The maximum character<br>
that is used for<br>
indexing</td>
<td>z</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>levenshteinDistance</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="qgrams">qGrams</h4>
<p>String similarity based on q-grams (by default q=2).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>q</td>
<td>int</td>
<td>No description</td>
<td>2</td>
</tr>
<tr class="even">
<td>minChar</td>
<td>char</td>
<td>No description</td>
<td>0</td>
</tr>
<tr class="odd">
<td>maxChar</td>
<td>char</td>
<td>No description</td>
<td>z</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>qGrams</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="starts-with">Starts with</h4>
<p>Returns success if the first string starts with the second string, failure otherwise.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>reverse</td>
<td>boolean</td>
<td>Reverse source and target<br>
values</td>
<td>false</td>
</tr>
<tr class="even">
<td>minLength</td>
<td>int</td>
<td>The minimum length of the<br>
string being<br>
contained.</td>
<td>2</td>
</tr>
<tr class="odd">
<td>maxLength</td>
<td>int</td>
<td>The potential maximum<br>
length of the strings<br>
that must match. If the<br>
max length is greater<br>
than the length of the<br>
string to match, the<br>
full string must<br>
match.</td>
<td>2147483647</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>startsWith</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h4 id="substring">SubString</h4>
<p>Return 0 to 1 for strong similarity to weak similarity. Based on the paper: Stoilos, Giorgos, Giorgos Stamou, and Stefanos Kollias. “A string metric for ontology alignment.” The Semantic Web-ISWC 2005. Springer Berlin Heidelberg, 2005. 624-637.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>granularity</td>
<td>String</td>
<td>The minimum length of a<br>
possible substring<br>
match.</td>
<td>3</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>substring</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.characterbased</code>.</p>
<h3 id="equality">Equality</h3>
<h4 id="constant">Constant</h4>
<p>Always returns a constant similarity value.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>value</td>
<td>double</td>
<td>No description</td>
<td>1.0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>constant</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h4 id="string-equality">String equality</h4>
<p>Checks for equality of the string representation of the given values. Returns success if string values are equal, failure otherwise. For a numeric comparison of values use the ‘Numeric Equality’ comparator.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>equality</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h4 id="greater-than">Greater than</h4>
<p>Checks if the source value is greater than the target value. If both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>orEqual</td>
<td>boolean</td>
<td>Accept equal values</td>
<td>false</td>
</tr>
<tr class="even">
<td>reverse</td>
<td>boolean</td>
<td>Reverse source and target<br>
inputs</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>greaterThan</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h4 id="inequality">Inequality</h4>
<p>Returns success if values are not equal, failure otherwise.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>inequality</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h4 id="lower-than">Lower than</h4>
<p>Checks if the source value is lower than the target value. If both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>orEqual</td>
<td>boolean</td>
<td>Accept equal values</td>
<td>false</td>
</tr>
<tr class="even">
<td>reverse</td>
<td>boolean</td>
<td>Reverse source and target<br>
inputs</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>lowerThan</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h4 id="numeric-equality">Numeric equality</h4>
<p>Compares values numerically instead of their string representation as the ‘String Equality’ operator does. Allows to set the needed precision of the comparison. A value of 0.0 means that the values must represent exactly the same (floating point) value, values higher than that allow for a margin of tolerance. Example: With a precision of 0.1, the following pairs of values will be considered equal: (1.3, 1.35), (0.0, 0.9999), (0.0, -0.90001), but following pairs will NOT match: (1.2, 1.30001), (1.0, 1.10001), (1.0, 0.89999).</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>precision</td>
<td>double</td>
<td>The range of tolerance in<br>
floating point number<br>
comparisons. Must be 0<br>
or a non-negative number<br>
smaller than<br>
1.</td>
<td>0.0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>numericEquality</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h4 id="relaxed-equality">Relaxed equality</h4>
<p>Return success if strings are equal, failure otherwise. Lower/upper case and differences like ö/o, n/ñ, c/ç etc. are treated as equal.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>relaxedEquality</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.equality</code>.</p>
<h3 id="numeric">Numeric</h3>
<h4 id="compare-physical-quantities">Compare physical quantities</h4>
<p>Computes the distance between two physical quantities. The distance is normalized to the SI base unit of the dimension. For instance for lengths, the distance will be in metres. Comparing incompatible units will yield a validation error.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>numberFormat</td>
<td>String</td>
<td>The IETF BCP 47 language<br>
tag, e.g., ‘en’.</td>
<td>en</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>PhysicalQuantitiesDistance</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.measure</code>.</p>
<p>SI units and common derived units are supported. The following section lists all supported units. By default, all quantities are normalized to their base unit. For instance, lengths will be normalized to metres.</p>
<p><em>Time</em></p>
<p>Time is expressed in seconds (s). The following alternative units are supported: mo_s, mo_g, a, min, a_g, mo, mo_j, a_j, h, a_t, d.</p>
<p><em>Length</em></p>
<p>Length is expressed in metres (m). The following alternative units are supported: in, nmi, Ao, mil, yd, AU, ft, pc, fth, mi, hd.</p>
<p><em>Mass</em></p>
<p>Mass is expressed in kilograms (kg). The following alternative units are supported: lb, ston, t, stone, u, gr, lcwt, oz, g, scwt, dr, lton.</p>
<p><em>Electric current</em></p>
<p>Electric current is expressed in amperes (A). The following alternative units are supported: Bi, Gb.</p>
<p><em>Temperature</em></p>
<p>Temperature is expressed in kelvins (K). The following alternative units are supported: Cel.</p>
<p><em>Amount of substance</em></p>
<p>Amount of substance is expressed in moles (mol).</p>
<p><em>Luminous intensity</em></p>
<p>Luminous intensity is expressed in candelas (cd).</p>
<p><em>Area</em></p>
<p>Area is expressed in square metres (m²). The following alternative units are supported: m2, ar, syd, cml, b, sft, sin.</p>
<p><em>Volume</em></p>
<p>Volume is expressed in cubic metres (㎥). The following alternative units are supported: st, bf, cyd, cr, L, l, cin, cft, m3.</p>
<p><em>Energy</em></p>
<p>Energy is expressed in joules (J). The following alternative units are supported: cal_IT, eV, cal_m, cal, cal_th.</p>
<p><em>Angle</em></p>
<p>Angle is expressed in radians (rad). The following alternative units are supported: circ, gon, deg, ‘,’’.</p>
<p><em>Others</em></p>
<ul>
<li>1/m, derived units: Ky</li>
<li>kg/(m·s), derived units: P</li>
<li>bit/s, derived units: Bd</li>
<li>bit, derived units: By</li>
<li>Sv</li>
<li>N</li>
<li>Ω, derived units: Ohm</li>
<li>T, derived units: G</li>
<li>sr, derived units: sph</li>
<li>F</li>
<li>C/kg, derived units: R</li>
<li>cd/m², derived units: sb, Lmb</li>
<li>Pa, derived units: bar, atm</li>
<li>kg/(m·s²), derived units: att</li>
<li>m²/s, derived units: St</li>
<li>A/m, derived units: Oe</li>
<li>kg·m²/s², derived units: erg</li>
<li>kg/m³, derived units: g%</li>
<li>mho</li>
<li>V</li>
<li>lx, derived units: ph</li>
<li>m/s², derived units: Gal, m/s2</li>
<li>m/s, derived units: kn</li>
<li>m·kg/s², derived units: gf, lbf, dyn</li>
<li>m²/s², derived units: RAD, REM</li>
<li>C</li>
<li>Gy</li>
<li>Hz</li>
<li>H</li>
<li>lm</li>
<li>W</li>
<li>Wb, derived units: Mx</li>
<li>Bq, derived units: Ci</li>
<li>S</li>
</ul>
<h4 id="date">Date</h4>
<p>The distance in days between two dates (‘YYYY-MM-DD’ format).</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>requireMonthAnd-<br>
Day</td>
<td>boolean</td>
<td>If true, no distance<br>
value will be generated<br>
if months or days are<br>
missing (e.g., 2019-11).<br>
If false, missing month<br>
or day fields will<br>
default to 1.</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>date</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.numeric</code>.</p>
<h4 id="datetime">DateTime</h4>
<p>Distance between two date time values (xsd:dateTime format) in seconds.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>dateTime</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.numeric</code>.</p>
<h4 id="inside-numeric-interval">Inside numeric interval</h4>
<p>Checks if a number is contained inside a numeric interval, such as ‘1900 - 2000’.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>separator</td>
<td>String</td>
<td>No description</td>
<td>—</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>insideNumericInterval</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.numeric</code>.</p>
<h4 id="numeric-similarity">Numeric similarity</h4>
<p>Computes the numeric distance between two numbers.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minValue</td>
<td>double</td>
<td>No description</td>
<td>-Infinity</td>
</tr>
<tr class="even">
<td>maxValue</td>
<td>double</td>
<td>No description</td>
<td>Infinity</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>num</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.numeric</code>.</p>
<h4 id="geographical-distance">Geographical distance</h4>
<p>Computes the geographical distance between two points. Author: Konrad Höffner (MOLE subgroup of Research Group AKSW, University of Leipzig)</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>unit</td>
<td>String</td>
<td>No description</td>
<td>km</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>wgs84</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.numeric</code>.</p>
<h3 id="tokenbased">Tokenbased</h3>
<p>While character-based distance measures work well for typographical errors, there are a number of tasks where token-base distance measures are better suited:</p>
<ul>
<li>Strings where parts are reordered e.g. “John Doe” and “Doe, John”</li>
<li>Texts consisting of multiple words</li>
</ul>
<h4 id="cosine">Cosine</h4>
<p>Cosine Distance Measure.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>k</td>
<td>int</td>
<td>No description</td>
<td>3</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>cosine</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.tokenbased</code>.</p>
<h4 id="dice-coefficient">Dice coefficient</h4>
<p>Dice similarity coefficient.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>dice</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.tokenbased</code>.</p>
<h4 id="jaccard">Jaccard</h4>
<p>Jaccard similarity coefficient.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>jaccard</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.tokenbased</code>.</p>
<h4 id="soft-jaccard">Soft Jaccard</h4>
<p>Soft Jaccard similarity coefficient. Same as Jaccard distance but values within an levenhstein distance of ‘maxDistance’ are considered equivalent.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>maxDistance</td>
<td>int</td>
<td>No description</td>
<td>1</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>softjaccard</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.tokenbased</code>.</p>
<h4 id="token-wise-distance">Token-wise distance</h4>
<p>Token-wise string distance using the specified metric.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ignoreCase</td>
<td>boolean</td>
<td>No description</td>
<td>true</td>
</tr>
<tr class="even">
<td>metricName</td>
<td>String</td>
<td>No description</td>
<td>levenshtein</td>
</tr>
<tr class="odd">
<td>splitRegex</td>
<td>String</td>
<td>No description</td>
<td>[\s\d\p{Punct}]+</td>
</tr>
<tr class="even">
<td>stopwords</td>
<td>String</td>
<td>No description</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>stopwordWeight</td>
<td>double</td>
<td>No description</td>
<td>0.01</td>
</tr>
<tr class="even">
<td>nonStopword-<br>
Weight</td>
<td>double</td>
<td>No description</td>
<td>0.1</td>
</tr>
<tr class="odd">
<td>useIncrementalIdf-<br>
Weights</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
<tr class="even">
<td>matchThreshold</td>
<td>double</td>
<td>No description</td>
<td>0.0</td>
</tr>
<tr class="odd">
<td>orderingImpact</td>
<td>double</td>
<td>No description</td>
<td>0.0</td>
</tr>
<tr class="even">
<td>adjustByToken-<br>
Length</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>tokenwiseDistance</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.distance.tokenbased</code>.</p>
<h2 id="transformations-1">Transformations</h2>
<p>The following transform and normalization functions are available:</p>
<h3 id="combine">Combine</h3>
<h4 id="concatenate">Concatenate</h4>
<p>Concatenates strings from multiple inputs.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>glue</td>
<td>String</td>
<td>Separator to be inserted<br>
between two concatenated<br>
strings.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>missingValuesAsEmpty-<br>
Strings</td>
<td>boolean</td>
<td>Handle missing values as<br>
empty strings.</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>concat</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.combine</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [] for parameters [] and input values [].</p>
<p>Returns [a] for parameters [] and input values [[a]].</p>
<p>Returns [ab] for parameters [] and input values [[a], [b]].</p>
<p>Returns [First-Last] for parameters [glue -> -] and input values [[First], [Last]].</p>
<p>Returns [First-Second, First-Third] for parameters [glue -> -] and input values [[First], [Second, Third]].</p>
<p>Returns [First–Second] for parameters [glue -> -] and input values [[First], [], [Second]].</p>
<p>Returns [] for parameters [glue -> -] and input values [[First], [], [Second]].</p>
<p>Returns [First–Second] for parameters [glue -> -, missingValuesAsEmptyStrings -> true] and input values [[First], [], [Second]].</p>
<h4 id="concatenate-multiple-values">Concatenate multiple values</h4>
<p>Concatenates multiple values received for an input. If applied to multiple inputs, yields at most one value per input. Optionally removes duplicate values.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>glue</td>
<td>String</td>
<td>No description</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>removeDuplicates</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>concatMultiValues</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.combine</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [] for parameters [] and input values [].</p>
<p>Returns [a] for parameters [] and input values [[a]].</p>
<p>Returns [ab] for parameters [] and input values [[a, b]].</p>
<p>Returns [axb] for parameters [glue -> x] and input values [[a, b]].</p>
<p>Returns [ab, 12] for parameters [] and input values [[a, b], [1, 2]].</p>
<h4 id="merge">Merge</h4>
<p>Merges the values of all inputs.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>merge</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.combine</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [] for parameters [] and input values [].</p>
<p>Returns [a, b, c] for parameters [] and input values [[a, b], [c]].</p>
<h3 id="conditional">Conditional</h3>
<h4 id="contains-all-of">Contains all of</h4>
<p>Accepts two inputs. If the first input contains all of the second input values it returns ‘true’, else ‘false’ is returned.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>containsAllOf</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conditional</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns <a href="#true">true</a> for parameters [] and input values [[A, B, C], [A, B]].</p>
<p>Returns <a href="#false">false</a> for parameters [] and input values [[A, B, C], [A, D]].</p>
<p>Returns <a href="#false">false</a> for parameters [] and input values [[A, B, C], [D]].</p>
<p>Returns <a href="#true">true</a> for parameters [] and input values [[A, B, C], [A, B, C]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[A, B, C]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[A], [A], [A]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[A]].</p>
<h4 id="contains-any-of">Contains any of</h4>
<p>Accepts two inputs. If the first input contains any of the second input values it returns ‘true’, else ‘false’ is returned.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>containsAnyOf</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conditional</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns <a href="#true">true</a> for parameters [] and input values [[A, B, C], [A, B]].</p>
<p>Returns <a href="#true">true</a> for parameters [] and input values [[A, B, C], [A, D]].</p>
<p>Returns <a href="#false">false</a> for parameters [] and input values [[A, B, C], [D]].</p>
<p>Returns <a href="#true">true</a> for parameters [] and input values [[A, B, C], [A, B, C]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[A, B, C]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[A], [A], [A]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[A]].</p>
<h4 id="if-contains">If contains</h4>
<p>Accepts two or three inputs. If the first input contains the given value, the second input is forwarded. Otherwise, the third input is forwarded (if present).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>search</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ifContains</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conditional</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [this is a match] for parameters [search -> match] and input values [[matching string], [this is a match]].</p>
<p>Returns [] for parameters [search -> match] and input values [[different string], [this is a match]].</p>
<p>Returns [this is no match] for parameters [search -> match] and input values [[different string], [this is a match], [this is no match]].</p>
<h4 id="if-exists">If exists</h4>
<p>Accepts two or three inputs. If the first input provides a value, the second input is forwarded. Otherwise, the third input is forwarded (if present).</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ifExists</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conditional</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [yes] for parameters [] and input values [<a href="#value">value</a>, [yes], [no]].</p>
<p>Returns [no] for parameters [] and input values [[], [yes], [no]].</p>
<p>Returns [] for parameters [] and input values [<a href="#value">value</a>].</p>
<h4 id="if-matches-regex">If matches regex</h4>
<pre><code>   Accepts two or three inputs.
   If any value of the first input matches the regex, the second input is forwarded.
   Otherwise, the third input is forwarded (if present).</code></pre>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>regex</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>negate</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ifMatchesRegex</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conditional</code>.</p>
<h4 id="negate-binary-not">Negate binary (NOT)</h4>
<p>Accepts one input, which is either ‘true’, ‘1’ or ‘false’, ‘0’ and negates it.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>negate</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conditional</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [1, 0, true, false, true, false] for parameters [] and input values [[0, 1, false, true, False, True]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[falsee, true]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [].</p>
<h3 id="conversion">Conversion</h3>
<h4 id="convert-charset">Convert charset</h4>
<p>Convert the string from “sourceCharset” to “targetCharset”.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>sourceCharset</td>
<td>String</td>
<td>No description</td>
<td>ISO-8859-1</td>
</tr>
<tr class="even">
<td>targetCharset</td>
<td>String</td>
<td>No description</td>
<td>UTF-8</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>convertCharset</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.conversion</code>.</p>
<h4 id="clean-html">Clean HTML</h4>
<p>Cleans HTML using a tag white list and allows selection of HTML sections with xPath or cssSelector expressions. If the tag or attribute white lists are left empty default white lists will be used. The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>tagWhiteList</td>
<td>String</td>
<td>Tags to keep in the<br>
cleaned Text (or<br>
reference to a<br>
configuration).</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>attributeWhite-<br>
List</td>
<td>String</td>
<td>Tags to keep in the<br>
cleaned Text (or<br>
reference to a<br>
configuration).</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>selectors</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>CSS or XPath queries for<br>
selection of content (or<br>
reference to a<br>
configuration). Comma<br>
separated. CssSelectors<br>
can be pipe separated<br>
for non-sequential<br>
execution.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>method</td>
<td>Enum</td>
<td>Selects use of xPath or<br>
css selectors (‘xPath’<br>
or ‘cssSelectors’).</td>
<td>xPath</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>htmlCleaner</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.plugins.html</code>.</p>
<h3 id="date-1">Date</h3>
<h4 id="parse-date">Parse date</h4>
<p>Parses and normalizes dates in different formats.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inputDateFormat-<br>
Id</td>
<td>Enum</td>
<td>The input date/time<br>
format used for parsing<br>
the date/time<br>
string.</td>
<td>w3cDate</td>
</tr>
<tr class="even">
<td>alternativeInput-<br>
Format</td>
<td>String</td>
<td>An input format string<br>
that should be used<br>
instead of the selected<br>
input format. Java<br>
DateFormat string.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>outputDateFormat-<br>
Id</td>
<td>Enum</td>
<td>The output date/time<br>
format used for parsing<br>
the date/time<br>
string.</td>
<td>w3cDate</td>
</tr>
<tr class="even">
<td>alternativeOutput-<br>
Format</td>
<td>String</td>
<td>An output format string<br>
that should be used<br>
instead of the selected<br>
output format. Java<br>
DateFormat string.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>DateTypeParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [1999-03-20] for parameters [inputDateFormatId -> German style date format, outputDateFormatId -> w3c Date] and input values [[20.03.1999]].</p>
<p>Returns [20.03.1999] for parameters [inputDateFormatId -> w3c Date, outputDateFormatId -> German style date format] and input values [[1999-03-20]].</p>
<p>Returns [2017-04-04] for parameters [inputDateFormatId -> common ISO8601, outputDateFormatId -> w3c Date] and input values [[2017-04-04T00:00:00.000+02:00]].</p>
<p>Returns [2017-04-04] for parameters [inputDateFormatId -> common ISO8601, outputDateFormatId -> w3c Date] and input values [[2017-04-04T00:00:00+02:00]].</p>
<p>Returns [1999-03-20T20:34.44] for parameters [alternativeInputFormat -> dd.MM.yyyy HH:mm.ss, alternativeOutputFormat -> yyyy-MM-dd’T’HH:mm.ss] and input values [[20.03.1999 20:34.44]].</p>
<p>Returns [12:20:00.000] for parameters [inputDateFormatId -> excelDateTime, outputDateFormatId -> xsdTime] and input values [[12:20:00.000]].</p>
<p>Returns [–01] for parameters [inputDateFormatId -> w3c YearMonth, outputDateFormatId -> w3c Month] and input values [[2020-01]].</p>
<p>Returns [—31] for parameters [inputDateFormatId -> w3c MonthDay, outputDateFormatId -> w3c Day] and input values [[–12-31]].</p>
<p>Returns [–12-31] for parameters [inputDateFormatId -> w3c Date, outputDateFormatId -> w3c MonthDay] and input values [[2020-12-31]].</p>
<p>Fails validation and thus returns [] for parameters [inputDateFormatId -> w3c MonthDay, outputDateFormatId -> w3c Date] and input values [[–12-31]].</p>
<p>Returns [2020-02-22T16:34:14] for parameters [alternativeInputFormat -> yyyy-MM-dd HH:mm:ss.SSS, outputDateFormatId -> w3cDateTime] and input values [[2020-02-22 16:34:14.000]].</p>
<h4 id="compare-dates">Compare dates</h4>
<p>Compares two dates. Returns 1 if the comparison yields true and 0 otherwise. If there are multiple dates in both sets, the comparator must be true for all dates. For instance, {2014-08-02,2014-08-03} < {2014-08-03} yields 0 as not all dates in the first set are smaller than in the second.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>comparator</td>
<td>Enum</td>
<td>No description</td>
<td>less</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>compareDates</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [1] for parameters [comparator -> <] and input values [[2017-01-01], [2017-01-02]].</p>
<p>Returns [0] for parameters [comparator -> <] and input values [[2017-01-02], [2017-01-01]].</p>
<p>Returns [1] for parameters [comparator -> >] and input values [[2017-01-02], [2017-01-01]].</p>
<p>Returns [0] for parameters [comparator -> >] and input values [[2017-01-01], [2017-01-02]].</p>
<p>Returns [1] for parameters [comparator -> =] and input values [[2017-01-01], [2017-01-01]].</p>
<p>Returns [0] for parameters [comparator -> =] and input values [[2017-01-02], [2017-01-01]].</p>
<h4 id="current-date">Current date</h4>
<p>Outputs the current date.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>currentDate</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="date-to-timestamp">Date to timestamp</h4>
<p>Convert an xsd:date to a Unix timestamp.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>datetoTimestamp</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="duration">Duration</h4>
<p>Computes the time difference between two data times.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>duration</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="duration-in-days">Duration in days</h4>
<p>Converts an xsd:duration to days.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>durationInDays</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="duration-in-seconds">Duration in seconds</h4>
<p>Converts an xsd:duration to seconds.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>durationInSeconds</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="duration-in-years">Duration in years</h4>
<p>Converts an xsd:duration to years.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>durationInYears</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="number-to-duration">Number to duration</h4>
<p>Converts a number to an xsd:duration. The base unit may be one of the following: ‘day’, ‘month’, ‘year’.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>unit</td>
<td>Enum</td>
<td>No description</td>
<td>day</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>numberToDuration</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="parse-date-pattern">Parse date pattern</h4>
<p>Parses a date based on a specified pattern, returning an xsd:date.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>format</td>
<td>String</td>
<td>The date pattern used to<br>
parse the input<br>
values</td>
<td>dd-MM-yyyy</td>
</tr>
<tr class="even">
<td>lenient</td>
<td>boolean</td>
<td>If set to true, the<br>
parser tries to use<br>
heuristics to parse<br>
dates with invalid<br>
fields (such as a day of<br>
zero).</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>parseDate</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [2015-04-03] for parameters [format -> dd.MM.yyyy] and input values [[03.04.2015]].</p>
<p>Returns [2015-04-03] for parameters [format -> dd.MM.yyyy] and input values [[3.4.2015]].</p>
<p>Returns [2015-04-03] for parameters [format -> yyyyMMdd] and input values [[20150403]].</p>
<p>Fails validation and thus returns [] for parameters [format -> yyyyMMdd, lenient -> false] and input values [[20150000]].</p>
<h4 id="timestamp-to-date">Timestamp to date</h4>
<p>Convert Unix timestamp to xsd:date.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>format</td>
<td>String</td>
<td>No description</td>
<td>yyyy-MM-dd</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>timeToDate</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [2017-07-03] for parameters [] and input values [[1499040000]].</p>
<h4 id="validate-date-after">Validate date after</h4>
<p>Validates if the first input date is after the second input date. Outputs the first input if the validation is successful.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>allowEqual</td>
<td>boolean</td>
<td>Allow both dates to be<br>
equal.</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateDateAfter</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<p><strong>Example Values</strong></p>
<p>Fails validation and thus returns [] for parameters [] and input values [[2015-04-02], [2015-04-03]].</p>
<p>Returns [2015-04-04] for parameters [] and input values [[2015-04-04], [2015-04-03]].</p>
<p>Returns [2015-04-03] for parameters [allowEqual -> true] and input values [[2015-04-03], [2015-04-03]].</p>
<p>Fails validation and thus returns [] for parameters [allowEqual -> false] and input values [[2015-04-03], [2015-04-03]].</p>
<h4 id="validate-date-range">Validate date range</h4>
<p>Validates if dates are within a specified range.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minDate</td>
<td>String</td>
<td>Earliest allowed date in<br>
YYYY-MM-DD</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>maxDate</td>
<td>String</td>
<td>Latest allowed data in<br>
YYYY-MM-DD</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateDateRange</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<h4 id="validate-numeric-range">Validate numeric range</h4>
<p>Validates if a number is within a specified range.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>min</td>
<td>double</td>
<td>Minimum allowed<br>
number</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>max</td>
<td>double</td>
<td>Maximum allowed<br>
number</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateNumericRange</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<h3 id="excel-1">Excel</h3>
<h4 id="abs">Abs</h4>
<p>Excel ABS(number): Returns the absolute value of the given number.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ABS</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ABS</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="acos">Acos</h4>
<p>Excel ACOS(number): Returns the inverse cosine of the given number in radians.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ACOS</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ACOS</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="acosh">Acosh</h4>
<p>Excel ACOSH(number): Returns the inverse hyperbolic cosine of the given number in radians.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ACOSH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ACOSH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="and">And</h4>
<p>Excel AND(argument1; argument2 …argument30): Returns TRUE if all the arguments are considered TRUE, and FALSE otherwise.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>AND</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_AND</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="asin">Asin</h4>
<p>Excel ASIN(number): Returns the inverse sine of the given number in radians.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ASIN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ASIN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="asinh">Asinh</h4>
<p>Excel ASINH(number): Returns the inverse hyperbolic sine of the given number in radians.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ASINH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ASINH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="atan">Atan</h4>
<p>Excel ATAN(number): Returns the inverse tangent of the given number in radians.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ATAN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ATAN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="atan2">Atan2</h4>
<p>Excel ATAN2(number_x; number_y): Returns the inverse tangent of the specified x and y coordinates. Number_x is the value for the x coordinate. Number_y is the value for the y coordinate.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ATAN2</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ATAN2</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="atanh">Atanh</h4>
<p>Excel ATANH(number): Returns the inverse hyperbolic tangent of the given number. (Angle is returned in radians.)</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ATANH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ATANH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="avedev">Avedev</h4>
<p>Excel AVEDEV(number1; number2; … number_30): Returns the average of the absolute deviations of data points from their mean. Displays the diffusion in a data set. Number_1; number_2; … number_30 are values or ranges that represent a sample. Each number can also be replaced by a reference.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>AVEDEV</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_AVEDEV</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="average">Average</h4>
<p>Excel AVERAGE(number_1; number_2; … number_30): Returns the average of the arguments. Number_1; number_2; … number_30 are numerical values or ranges. Text is ignored.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>AVERAGE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_AVERAGE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="ceiling">Ceiling</h4>
<p>Excel CEILING(number; significance; mode): Rounds the given number to the nearest integer or multiple of significance. Significance is the value to whose multiple of ten the value is to be rounded up (.01, .1, 1, 10, etc.). Mode is an optional value. If it is indicated and non-zero and if the number and significance are negative, rounding up is carried out based on that value.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>CEILING</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_CEILING</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="choose">Choose</h4>
<p>Excel CHOOSE(index; value1; … value30): Uses an index to return a value from a list of up to 30 values. Index is a reference or number between 1 and 30 indicating which value is to be taken from the list. Value1; … value30 is the list of values entered as a reference to a cell or as individual values.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>CHOOSE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_CHOOSE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="clean">Clean</h4>
<p>Excel CLEAN(text): Removes all non-printing characters from the string. Text refers to the text from which to remove all non-printable characters.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>CLEAN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_CLEAN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="code">Code</h4>
<p>Excel CODE(text): Returns a numeric code for the first character in a text string. Text is the text for which the code of the first character is to be found.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>CODE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_CODE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="combin">Combin</h4>
<p>Excel COMBIN(count_1; count_2): Returns the number of combinations for a given number of objects. Count_1 is the total number of elements. Count_2 is the selected count from the elements. This is the same as the nCr function on a calculator.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>COMBIN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_COMBIN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="cos">Cos</h4>
<p>Excel COS(number): Returns the cosine of the given number (angle in radians).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>COS</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_COS</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="cosh">Cosh</h4>
<p>Excel COSH(number): Returns the hyperbolic cosine of the given number (angle in radians).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>COSH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_COSH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="count">Count</h4>
<p>Excel COUNT(value_1; value_2; … value_30): Counts how many numbers are in the list of arguments. Text entries are ignored. Value_1; value_2; … value_30 are values or ranges which are to be counted.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>COUNT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_COUNT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="counta">Counta</h4>
<p>Excel COUNTA(value_1; value_2; … value_30): Counts how many values are in the list of arguments. Text entries are also counted, even when they contain an empty string of length 0. If an argument is an array or reference, empty cells within the array or reference are ignored. value_1; value_2; … value_30 are up to 30 arguments representing the values to be counted.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>COUNTA</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_COUNTA</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="degrees">Degrees</h4>
<p>Excel DEGREES(number): Converts the given number in radians to degrees.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>DEGREES</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_DEGREES</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="devsq">Devsq</h4>
<p>Excel DEVSQ(number_1; number_2; … number_30): Returns the sum of squares of deviations based on a sample mean. Number_1; number_2; … number_30 are numerical values or ranges representing a sample.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>DEVSQ</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_DEVSQ</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="even">Even</h4>
<p>Excel EVEN(number): Rounds the given number up to the nearest even integer.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>EVEN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_EVEN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="exact">Exact</h4>
<p>Excel EXACT(text_1; text_2): Compares two text strings and returns TRUE if they are identical. This function is case- sensitive. Text_1 is the first text to compare. Text_2 is the second text to compare.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>EXACT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_EXACT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="exp">Exp</h4>
<p>Excel EXP(number): Returns e raised to the power of the given number.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>EXP</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_EXP</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="fact">Fact</h4>
<p>Excel FACT(number): Returns the factorial of the given number.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>FACT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_FACT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="false">False</h4>
<p>Excel FALSE(): Set the logical value to FALSE. The FALSE() function does not require any arguments.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>FALSE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_FALSE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="find">Find</h4>
<p>Excel FIND(find_text; text; position): Looks for a string of text within another string. Where to begin the search can also be defined. The search term can be a number or any string of characters. The search is case-sensitive. Find_text is the text to be found. Text is the text where the search takes place. Position (optional) is the position in the text from which the search starts.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>FIND</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_FIND</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="floor">Floor</h4>
<p>Excel FLOOR(number; significance; mode): Rounds the given number down to the nearest multiple of significance. Significance is the value to whose multiple of ten the number is to be rounded down (.01, .1, 1, 10, etc.). Mode is an optional value. If it is indicated and non-zero and if the number and significance are negative, rounding up is carried out based on that value.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>FLOOR</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_FLOOR</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="fv">Fv</h4>
<p>Excel FV(rate; NPER; PMT; PV; type): Returns the future value of an investment based on periodic, constant payments and a constant interest rate. Rate is the periodic interest rate. NPER is the total number of periods. PMT is the annuity paid regularly per period. PV (optional) is the present cash value of an investment. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>FV</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_FV</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="if">If</h4>
<p>Excel IF(test; then_value; otherwise_value): Specifies a logical test to be performed. Test is any value or expression that can be TRUE or FALSE. Then_value (optional) is the value that is returned if the logical test is TRUE. Otherwise_value (optional) is the value that is returned if the logical test is FALSE.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>IF</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_IF</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="int">Int</h4>
<p>Excel INT(number): Rounds the given number down to the nearest integer.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>INT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_INT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="intercept">Intercept</h4>
<p>Excel INTERCEPT(data_Y; data_X): Calculates the y-value at which a line will intersect the y-axis by using known x-values and y-values. Data_Y is the dependent set of observations or data. Data_X is the independent set of observations or data. Names, arrays or references containing numbers must be used here. Numbers can also be entered directly.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>INTERCEPT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_INTERCEPT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="ipmt">Ipmt</h4>
<p>Excel IPMT(rate; period; NPER; PV; FV; type): Calculates the periodic amortization for an investment with regular payments and a constant interest rate. Rate is the periodic interest rate. Period is the period for which the compound interest is calculated. NPER is the total number of periods during which annuity is paid. Period=NPER, if compound interest for the last period is calculated. PV is the present cash value in sequence of payments. FV (optional) is the desired value (future value) at the end of the periods. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>IPMT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_IPMT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="irr">Irr</h4>
<p>Excel IRR(values; guess): Calculates the internal rate of return for an investment. The values represent cash flow values at regular intervals; at least one value must be negative (payments), and at least one value must be positive (income). Values is an array containing the values. Guess (optional) is the estimated value. If you can provide only a few values, you should provide an initial guess to enable the iteration.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>IRR</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_IRR</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="large">Large</h4>
<p>Excel LARGE(data; rank_c): Returns the Rank_c-th largest value in a data set. Data is the cell range of data. Rank_c is the ranking of the value (2nd largest, 3rd largest, etc.) written as an integer.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>LARGE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_LARGE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="ln">Ln</h4>
<p>Excel LN(number): Returns the natural logarithm based on the constant e of the given number.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>LN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_LN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="log">Log</h4>
<p>Excel LOG(number; base): Returns the logarithm of the given number to the specified base. Base is the base for the logarithm calculation.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>LOG</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_LOG</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="log10">Log10</h4>
<p>Excel LOG10(number): Returns the base-10 logarithm of the given number.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>LOG10</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_LOG10</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="max">Max</h4>
<p>Excel MAX(number_1; number_2; … number_30): Returns the maximum value in a list of arguments. Number_1; number_2; … number_30 are numerical values or ranges.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MAX</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MAX</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="maxa">Maxa</h4>
<p>Excel MAXA(value_1; value_2; … value_30): Returns the maximum value in a list of arguments. Unlike MAX, text can be entered. The value of the text is 0. Value_1; value_2; … value_30 are values or ranges.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MAXA</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MAXA</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="median">Median</h4>
<p>Excel MEDIAN(number_1; number_2; … number_30): Returns the median of a set of numbers. Number_1; number_2; … number_30 are values or ranges, which represent a sample. Each number can also be replaced by a reference.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MEDIAN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MEDIAN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="mid">Mid</h4>
<p>Excel MID(text; start; number): Returns a text segment of a character string. The parameters specify the starting position and the number of characters. Text is the text containing the characters to extract. Start is the position of the first character in the text to extract. Number is the number of characters in the part of the text.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MID</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MID</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="min">Min</h4>
<p>Excel MIN(number_1; number_2; … number_30): Returns the minimum value in a list of arguments. Number_1; number_2; … number_30 are numerical values or ranges.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MIN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MIN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="mina">Mina</h4>
<p>Excel MINA(value_1; value_2; … value_30): Returns the minimum value in a list of arguments. Here text can also be entered. The value of the text is 0. Value_1; value_2; … value_30 are values or ranges.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MINA</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MINA</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="mirr">Mirr</h4>
<p>Excel MIRR(values; investment; reinvest_rate): Calculates the modified internal rate of return of a series of investments. Values corresponds to the array or the cell reference for cells whose content corresponds to the payments. Investment is the rate of interest of the investments (the negative values of the array) Reinvest_rate is the rate of interest of the reinvestment (the positive values of the array).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MIRR</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MIRR</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="mod">Mod</h4>
<p>Excel MOD(dividend; divisor): Returns the remainder after a number is divided by a divisor. Dividend is the number which will be divided by the divisor. Divisor is the number by which to divide the dividend.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MOD</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MOD</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="mode">Mode</h4>
<p>Excel MODE(number_1; number_2; … number_30): Returns the most common value in a data set. Number_1; number_2; … number_30 are numerical values or ranges. If several values have the same frequency, it returns the smallest value. An error occurs when a value does not appear twice.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>MODE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_MODE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="not">Not</h4>
<p>Excel NOT(logical_value): Reverses the logical value. Logical_value is any value to be reversed.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>NOT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_NOT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="nper">Nper</h4>
<p>Excel NPER(rate; PMT; PV; FV; type): Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate. Rate is the periodic interest rate. PMT is the constant annuity paid in each period. PV is the present value (cash value) in a sequence of payments. FV (optional) is the future value, which is reached at the end of the last period. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>NPER</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_NPER</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="npv">Npv</h4>
<p>Excel NPV(Rate; value_1; value_2; … value_30): Returns the net present value of an investment based on a series of periodic cash flows and a discount rate. Rate is the discount rate for a period. Value_1; value_2;… value_30 are values representing deposits or withdrawals.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>NPV</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_NPV</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="odd">Odd</h4>
<p>Excel ODD(number): Rounds the given number up to the nearest odd integer.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ODD</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ODD</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="or">Or</h4>
<p>Excel OR(logical_value_1; logical_value_2; …logical_value_30): Returns TRUE if at least one argument is TRUE. Returns the value FALSE if all the arguments have the logical value FALSE. Logical_value_1; logical_value_2; …logical_value_30 are conditions to be checked. All conditions can be either TRUE or FALSE. If a range is entered as a parameter, the function uses the value from the range that is in the current column or row.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>OR</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_OR</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="percentile">Percentile</h4>
<p>Excel PERCENTILE(data; alpha): Returns the alpha-percentile of data values in an array. Data is the array of data. Alpha is the percentage of the scale between 0 and 1.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PERCENTILE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PERCENTILE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="pi">Pi</h4>
<p>Excel PI(): Returns the value of PI to fourteen decimal places.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PI</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PI</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="pmt">Pmt</h4>
<p>Excel PMT(rate; NPER; PV; FV; type): Returns the periodic payment for an annuity with constant interest rates. Rate is the periodic interest rate. NPER is the number of periods in which annuity is paid. PV is the present value (cash value) in a sequence of payments. FV (optional) is the desired value (future value) to be reached at the end of the periodic payments. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PMT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PMT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="poisson">Poisson</h4>
<p>Excel POISSON(number; mean; C): Returns the Poisson distribution for the given Number. Mean is the middle value of the Poisson distribution. C = 0 calculates the density function, and C = 1 calculates the distribution.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>POISSON</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_POISSON</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="power">Power</h4>
<p>Excel POWER(base; power): Returns the result of a number raised to a power. Base is the number that is to be raised to the given power. Power is the exponent by which the base is to be raised.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>POWER</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_POWER</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="ppmt">Ppmt</h4>
<p>Excel PPMT(rate; period; NPER; PV; FV; type): Returns for a given period the payment on the principal for an investment that is based on periodic and constant payments and a constant interest rate. Rate is the periodic interest rate. Period is the amortization period. NPER is the total number of periods during which annuity is paid. PV is the present value in the sequence of payments. FV (optional) is the desired (future) value. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PPMT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PPMT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="product">Product</h4>
<p>Excel PRODUCT(number 1 to 30): Multiplies all the numbers given as arguments and returns the product. Number 1 to number 30 are up to 30 arguments whose product is to be calculated, separated by semi-colons.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PRODUCT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PRODUCT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="proper">Proper</h4>
<p>Excel PROPER(text): Capitalizes the first letter in all words of a text string. Text is the text to be converted.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PROPER</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PROPER</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="pv">Pv</h4>
<p>Excel PV(rate; NPER; PMT; FV; type): Returns the present value of an investment resulting from a series of regular payments. Rate defines the interest rate per period. NPER is the total number of payment periods. PMT is the regular payment made per period. FV (optional) defines the future value remaining after the final installment has been made. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>PV</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_PV</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="radians">Radians</h4>
<p>Excel RADIANS(number): Converts the given number in degrees to radians.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>RADIANS</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_RADIANS</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="rand">Rand</h4>
<p>Excel RAND(): Returns a random number between 0 and 1.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>RAND</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_RAND</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="rank">Rank</h4>
<p>Excel RANK(value; data; type): Returns the rank of the given Value in a sample. Data is the array or range of data in the sample. Type (optional) is the sequence order, either ascending (0) or descending (1).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>RANK</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_RANK</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="rate">Rate</h4>
<p>Excel RATE(NPER; PMT; PV; FV; type; guess): Returns the constant interest rate per period of an annuity. NPER is the total number of periods, during which payments are made (payment period). PMT is the constant payment (annuity) paid during each period. PV is the cash value in the sequence of payments. FV (optional) is the future value, which is reached at the end of the periodic payments. Type (optional) defines whether the payment is due at the beginning (1) or the end (0) of a period. Guess (optional) determines the estimated value of the interest with iterative calculation.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>RATE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_RATE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="replace">Replace</h4>
<p>Excel REPLACE(text; position; length; new_text): Replaces part of a text string with a different text string. This function can be used to replace both characters and numbers (which are automatically converted to text). The result of the function is always displayed as text. To perform further calculations with a number which has been replaced by text, convert it back to a number using the VALUE function. Any text containing numbers must be enclosed in quotation marks so it is not interpreted as a number and automatically converted to text. Text is text of which a part will be replaced. Position is the position within the text where the replacement will begin. Length is the number of characters in text to be replaced. New_text is the text which replaces text..</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>REPLACE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_REPLACE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="rept">Rept</h4>
<p>Excel REPT(text; number): Repeats a character string by the given number of copies. Text is the text to be repeated. Number is the number of repetitions. The result can be a maximum of 255 characters.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>REPT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_REPT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="right">Right</h4>
<p>Excel RIGHT(text; number): Defines the last character or characters in a text string. Text is the text of which the right part is to be determined. Number (optional) is the number of characters from the right part of the text.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>RIGHT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_RIGHT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="roman">Roman</h4>
<p>Excel ROMAN(number; mode): Converts a number into a Roman numeral. The value range must be between 0 and 3999; the modes can be integers from 0 to 4. Number is the number that is to be converted into a Roman numeral. Mode (optional) indicates the degree of simplification. The higher the value, the greater is the simplification of the Roman numeral.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ROMAN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ROMAN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="round">Round</h4>
<p>Excel ROUND(number; count): Rounds the given number to a certain number of decimal places according to valid mathematical criteria. Count (optional) is the number of the places to which the value is to be rounded. If the count parameter is negative, only the whole number portion is rounded. It is rounded to the place indicated by the count.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ROUND</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ROUND</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="rounddown">Rounddown</h4>
<p>Excel ROUNDDOWN(number; count): Rounds the given number. Count (optional) is the number of digits to be rounded down to. If the count parameter is negative, only the whole number portion is rounded. It is rounded to the place indicated by the count.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ROUNDDOWN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ROUNDDOWN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="roundup">Roundup</h4>
<p>Excel ROUNDUP(number; count): Rounds the given number up. Count (optional) is the number of digits to which rounding up is to be done. If the count parameter is negative, only the whole number portion is rounded. It is rounded to the place indicated by the count.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>ROUNDUP</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_ROUNDUP</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="search">Search</h4>
<p>Excel SEARCH(find_text; text; position): Returns the position of a text segment within a character string. The start of the search can be set as an option. The search text can be a number or any sequence of characters. The search is not case-sensitive. The search supports regular expressions. Find_text is the text to be searched for. Text is the text where the search will take place. Position (optional) is the position in the text where the search is to start.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SEARCH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SEARCH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sign">Sign</h4>
<p>Excel SIGN(number): Returns the sign of the given number. The function returns the result 1 for a positive sign,  1 for a negative sign, and 0 for zero.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SIGN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SIGN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sin">Sin</h4>
<p>Excel SIN(number): Returns the sine of the given number (angle in radians).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SIN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SIN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sinh">Sinh</h4>
<p>Excel SINH(number): Returns the hyperbolic sine of the given number (angle in radians).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SINH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SINH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="slope">Slope</h4>
<p>Excel SLOPE(data_Y; data_X): Returns the slope of the linear regression line. Data_Y is the array or matrix of Y data. Data_X is the array or matrix of X data.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SLOPE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SLOPE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="small">Small</h4>
<p>Excel SMALL(data; rank_c): Returns the Rank_c-th smallest value in a data set. Data is the cell range of data. Rank_c is the rank of the value (2nd smallest, 3rd smallest, etc.) written as an integer.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SMALL</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SMALL</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sqrt">Sqrt</h4>
<p>Excel SQRT(number): Returns the positive square root of the given number. The value of the number must be positive.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SQRT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SQRT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="stdev">Stdev</h4>
<p>Excel STDEV(number_1; number_2; … number_30): Estimates the standard deviation based on a sample. Number_1; number_2; … number_30 are numerical values or ranges representing a sample based on an entire population.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>STDEV</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_STDEV</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="substitute">Substitute</h4>
<p>Excel SUBSTITUTE(text; search_text; new text; occurrence): Substitutes new text for old text in a string. Text is the text in which text segments are to be exchanged. Search_text is the text segment that is to be replaced (a number of times). New text is the text that is to replace the text segment. Occurrence (optional) indicates how many occurrences of the search text are to be replaced. If this parameter is missing, the search text is replaced throughout.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUBSTITUTE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUBSTITUTE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sum">Sum</h4>
<p>Excel SUM(number_1; number_2; … number_30): Adds all the numbers in a range of cells. Number_1; number_2;… number_30 are up to 30 arguments whose sum is to be calculated. You can also enter a range using cell references.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUM</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUM</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sumproduct">Sumproduct</h4>
<p>Excel SUMPRODUCT(array 1; array 2; …array 30): Multiplies corresponding elements in the given arrays, and returns the sum of those products. Array 1; array 2;…array 30 are arrays whose corresponding elements are to be multiplied. At least one array must be part of the argument list. If only one array is given, all array elements are summed.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUMPRODUCT</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUMPRODUCT</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sumsq">Sumsq</h4>
<p>Excel SUMSQ(number_1; number_2; … number_30): Calculates the sum of the squares of numbers (totaling up of the squares of the arguments) Number_1; number_2;… number_30 are up to 30 arguments, the sum of whose squares is to be calculated.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUMSQ</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUMSQ</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sumx2my2">Sumx2my2</h4>
<p>Excel SUMX2MY2(array_X; array_Y): Returns the sum of the difference of squares of corresponding values in two arrays. Array_X is the first array whose elements are to be squared and added. Array_Y is the second array whose elements are to be squared and subtracted.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUMX2MY2</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUMX2MY2</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sumx2py2">Sumx2py2</h4>
<p>Excel SUMX2PY2(array_X; array_Y): Returns the sum of the sum of squares of corresponding values in two arrays. Array_X is the first array whose arguments are to be squared and added. Array_Y is the second array, whose elements are to be added and squared.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUMX2PY2</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUMX2PY2</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="sumxmy2">Sumxmy2</h4>
<p>Excel SUMXMY2(array_X; array_Y): Adds the squares of the variance between corresponding values in two arrays. Array_X is the first array whose elements are to be subtracted and squared. Array_Y is the second array, whose elements are to be subtracted and squared.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>SUMXMY2</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_SUMXMY2</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="tan">Tan</h4>
<p>Excel TAN(number): Returns the tangent of the given number (angle in radians).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>TAN</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_TAN</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="tanh">Tanh</h4>
<p>Excel TANH(number): Returns the hyperbolic tangent of the given number (angle in radians).</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>TANH</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_TANH</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="true">True</h4>
<p>Excel TRUE(): Sets the logical value to TRUE. The TRUE() function does not require any arguments.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>TRUE</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_TRUE</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="trunc">Trunc</h4>
<p>Excel TRUNC(number; count): Truncates a number to an integer by removing the fractional part of the number according to the precision specified in Tools > Options > OpenOffice.org Calc > Calculate. Number is the number whose decimal places are to be cut off. Count is the number of decimal places which are not cut off.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>TRUNC</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_TRUNC</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="var">Var</h4>
<p>Excel VAR(number_1; number_2; … number_30): Estimates the variance based on a sample. Number_1; number_2; … number_30 are numerical values or ranges representing a sample based on an entire population.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>VAR</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_VAR</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="varp">Varp</h4>
<p>Excel VARP(Number_1; number_2; … number_30): Calculates a variance based on the entire population. Number_1; number_2; … number_30 are numerical values or ranges representing an entire population.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>functionName</td>
<td>String</td>
<td>The name of the Excel<br>
function</td>
<td>VARP</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>Excel_VARP</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h3 id="extract">Extract</h3>
<h4 id="regex-extract">Regex extract</h4>
<p>Extracts first occurrence of a regex “regex” in a string. If there is at least one capture group, it will return the string of the first capture group instead.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>regex</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>regexExtract</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.extraction</code>.</p>
<h3 id="filter">Filter</h3>
<h4 id="filter-by-length">Filter by length</h4>
<p>Removes all strings that are shorter than ‘min’ characters and longer than ‘max’ characters.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>min</td>
<td>int</td>
<td>No description</td>
<td>0</td>
</tr>
<tr class="even">
<td>max</td>
<td>int</td>
<td>No description</td>
<td>2147483647</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>filterByLength</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.filter</code>.</p>
<h4 id="filter-by-regex">Filter by regex</h4>
<p>Removes all strings that do NOT match a regex. If ‘negate’ is true, only strings will be removed that match the regex.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>regex</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>negate</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>filterByRegex</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.filter</code>.</p>
<h4 id="remove-empty-values">Remove empty values</h4>
<p>Removes empty values.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>removeEmptyValues</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.filter</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [value1, value2] for parameters [] and input values [[value1, , value2]].</p>
<p>Returns [] for parameters [] and input values [[, ]].</p>
<h4 id="remove-stopwords-remote-stopword-list">Remove stopwords (remote stopword list)</h4>
<p>Removes stopwords from all values. The stopword list is retrieved via a http connection (e.g. https://sites.google.com/site/kevinbouge/stopwords-lists/stopwords_de.txt). Each line in the stopword list contains a stopword. The separator defines a regex that is used for detecting words.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>stopWordList-<br>
Url</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>separator</td>
<td>String</td>
<td>No description</td>
<td>[\s-]+</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>removeRemoteStopwords</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.filter</code>.</p>
<h4 id="remove-stopwords">Remove stopwords</h4>
<p>Removes stopwords from all values. Each line in the stopword list contains a stopword. The separator defines a regex that is used for detecting words.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>stopwordList</td>
<td>Resource</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>separator</td>
<td>String</td>
<td>No description</td>
<td>[\s-]+</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>removeStopwords</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.filter</code>.</p>
<h4 id="remove-values">Remove values</h4>
<p>Removes values that contain words from a blacklist. The blacklist values are separated with commas.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>blacklist</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>removeValues</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.filter</code>.</p>
<h3 id="geo">Geo</h3>
<h4 id="retrieve-coordinates">Retrieve coordinates</h4>
<p>Retrieves geographic coordinates using Nominatim.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>additionalParameters</td>
<td>String</td>
<td>Additional URL parameters<br>
to be attached to each<br>
HTTP search request.<br>
Example: ‘&countrycodes=<br>
de&addressdetails=1’.<br>
Consult the API<br>
documentation for a list<br>
of available<br>
parameters.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>RetrieveCoordinates</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.geo</code>.</p>
<p><strong>Configuration</strong></p>
<p>The geocoding service to be queried for searches can be set up in the configuration. The default configuration is as follows:</p>
<pre><code>com.eccenca.di.geo = {
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
}</code></pre>
<p>In general, all services adhering to the <a href="https://nominatim.org/release-docs/develop/api/Search/">Nominatim search API</a> should be usable. Please note that when using public services, the pause time should be set to avoid overloading.</p>
<p><strong>Logging</strong></p>
<p>By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:</p>
<pre><code>logging.level {
  com.eccenca.di.geo=DEBUG
}</code></pre>
<h4 id="retrieve-latitude">Retrieve latitude</h4>
<p>Retrieves geographic coordinates using Nominatim and returns the latitude.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>additionalParameters</td>
<td>String</td>
<td>Additional URL parameters<br>
to be attached to each<br>
HTTP search request.<br>
Example: ‘&countrycodes=<br>
de&addressdetails=1’.<br>
Consult the API<br>
documentation for a list<br>
of available<br>
parameters.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>RetrieveLatitude</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.geo</code>.</p>
<p><strong>Configuration</strong></p>
<p>The geocoding service to be queried for searches can be set up in the configuration. The default configuration is as follows:</p>
<pre><code>com.eccenca.di.geo = {
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
}</code></pre>
<p>In general, all services adhering to the <a href="https://nominatim.org/release-docs/develop/api/Search/">Nominatim search API</a> should be usable. Please note that when using public services, the pause time should be set to avoid overloading.</p>
<p><strong>Logging</strong></p>
<p>By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:</p>
<pre><code>logging.level {
  com.eccenca.di.geo=DEBUG
}</code></pre>
<h4 id="retrieve-longitude">Retrieve longitude</h4>
<p>Retrieves geographic coordinates using Nominatim and returns the longitude.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>additionalParameters</td>
<td>String</td>
<td>Additional URL parameters<br>
to be attached to each<br>
HTTP search request.<br>
Example: ‘&countrycodes=<br>
de&addressdetails=1’.<br>
Consult the API<br>
documentation for a list<br>
of available<br>
parameters.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>RetrieveLongitude</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.geo</code>.</p>
<p><strong>Configuration</strong></p>
<p>The geocoding service to be queried for searches can be set up in the configuration. The default configuration is as follows:</p>
<pre><code>com.eccenca.di.geo = {
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
}</code></pre>
<p>In general, all services adhering to the <a href="https://nominatim.org/release-docs/develop/api/Search/">Nominatim search API</a> should be usable. Please note that when using public services, the pause time should be set to avoid overloading.</p>
<p><strong>Logging</strong></p>
<p>By default, individual requests to the geocoding service are not logged. To enable logging each request, the following configuration option can be set:</p>
<pre><code>logging.level {
  com.eccenca.di.geo=DEBUG
}</code></pre>
<h3 id="linguistic">Linguistic</h3>
<h4 id="nysiis">NYSIIS</h4>
<p>NYSIIS phonetic encoding. Provided by the StringMetric library: http://rockymadden.com/stringmetric/.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>refined</td>
<td>boolean</td>
<td>No description</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>NYSIIS</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.linguistic</code>.</p>
<h4 id="metaphone">Metaphone</h4>
<p>Metaphone phonetic encoding. Provided by the StringMetric library: http://rockymadden.com/stringmetric/.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>metaphone</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.linguistic</code>.</p>
<h4 id="normalize-chars">Normalize chars</h4>
<p>Replaces diacritical characters with non-diacritical ones (eg, ö -> o), plus some specialities like transforming æ -> ae, ß -> ss.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>normalizeChars</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.linguistic</code>.</p>
<h4 id="soundex">Soundex</h4>
<p>Soundex algorithm. Provided by the StringMetric library: http://rockymadden.com/stringmetric/.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>refined</td>
<td>boolean</td>
<td>No description</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>soundex</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.linguistic</code>.</p>
<h4 id="spotlight">Spotlight</h4>
<p>Concatenates all values to a string and gets a weighted entity vector from the Spotlight service.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>spotlight</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.linguistic</code>.</p>
<h4 id="stem">Stem</h4>
<p>Stems a string using the Porter Stemmer.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>stem</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.linguistic</code>.</p>
<h3 id="normalize">Normalize</h3>
<h4 id="strip-non-alphabetic-characters">Strip non-alphabetic characters</h4>
<p>Strips all non-alphabetic characters from a string. Spaces are retained.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>alphaReduce</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="capitalize">Capitalize</h4>
<p>Capitalizes the string i.e. converts the first character to upper case. If ‘allWords’ is set to true, all words are capitalized and not only the first character.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>allWords</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>capitalize</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [Capitalize me] for parameters [allWords -> false] and input values [[capitalize me]].</p>
<p>Returns [Capitalize Me] for parameters [allWords -> true] and input values [[capitalize me]].</p>
<h4 id="extract-physical-quantity">Extract physical quantity</h4>
<p>Extracts physical quantities, such as length or weight values. Values are expected of the form ‘{Number}{UnitPrefix}{Symbol}’ and are converted to the base unit.</p>
<p>Example:</p>
<ul>
<li>Given a value ‘10km, 3mg’.</li>
<li>If the symbol parameter is set to ‘m’, the extracted value is 10000.</li>
<li>If the symbol parameter is set to ‘g’, the extracted value is 0.001.</li>
</ul>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>symbol</td>
<td>String</td>
<td>The symbol of the<br>
dimension, e.g., ‘m’ for<br>
meter.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>numberFormat</td>
<td>String</td>
<td>The IETF BCP 47 language<br>
tag, e.g. ‘en’.</td>
<td>en</td>
</tr>
<tr class="odd">
<td>filter</td>
<td>String</td>
<td>Only extracts from values<br>
that contain the given<br>
regex (case-insensitive)<br>
.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>index</td>
<td>int</td>
<td>If there are multiple<br>
matches, retrieve the<br>
value with the given<br>
index (zero-based).</td>
<td>0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>extractPhysicalQuantity</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<h4 id="clean-html-1">Clean HTML</h4>
<p>Cleans HTML using a tag white list and allows selection of HTML sections with xPath or cssSelector expressions. If the tag or attribute white lists are left empty default white lists will be used. The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>tagWhiteList</td>
<td>String</td>
<td>Tags to keep in the<br>
cleaned Text (or<br>
reference to a<br>
configuration).</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>attributeWhite-<br>
List</td>
<td>String</td>
<td>Tags to keep in the<br>
cleaned Text (or<br>
reference to a<br>
configuration).</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>selectors</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>CSS or XPath queries for<br>
selection of content (or<br>
reference to a<br>
configuration). Comma<br>
separated. CssSelectors<br>
can be pipe separated<br>
for non-sequential<br>
execution.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>method</td>
<td>Enum</td>
<td>Selects use of xPath or<br>
css selectors (‘xPath’<br>
or ‘cssSelectors’).</td>
<td>xPath</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>htmlCleaner</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.plugins.html</code>.</p>
<h4 id="lower-case">Lower case</h4>
<p>Converts a string to lower case.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>lowerCase</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="remove-blanks">Remove blanks</h4>
<p>Remove whitespace from a string.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>removeBlanks</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="remove-duplicates">Remove duplicates</h4>
<p>Removes duplicated values, making a value sequence distinct.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>removeDuplicates</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="remove-parentheses">Remove parentheses</h4>
<p>Remove all parentheses including their content, e.g., transforms ‘Berlin (City)’ -> ‘Berlin’.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>removeParentheses</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="remove-special-chars">Remove special chars</h4>
<p>Remove special characters (including punctuation) from a string.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>removeSpecialChars</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="strip-uri-prefix">Strip URI prefix</h4>
<p>Strips the URI prefix and decodes the remainder. Leaves values unchanged which are not a valid URI.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>stripUriPrefix</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.substring</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns <a href="#value">value</a> for parameters [] and input values [[http://example.org/some/path/to/value]].</p>
<p>Returns <a href="#value">value</a> for parameters [] and input values [[urn:scheme:value]].</p>
<p>Returns [encoded välue] for parameters [] and input values [[http://example.org/some/path/to/encoded%20v%C3%A4lue]].</p>
<p>Returns <a href="#value">value</a> for parameters [] and input values [<a href="#value">value</a>].</p>
<h4 id="trim">Trim</h4>
<p>Remove leading and trailing whitespaces.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>trim</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="upper-case">Upper case</h4>
<p>Converts a string to upper case.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>upperCase</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="fix-uri">Fix URI</h4>
<p>Generates valid absolute URIs from the given values. Already valid absolute URIs are left untouched.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>uriPrefix</td>
<td>String</td>
<td>No description</td>
<td>urn:url-encoded-value:</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>uriFix</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [urn:url-encoded-value:ab] for parameters [] and input values [[ab]].</p>
<p>Returns [urn:url-encoded-value:a%26b] for parameters [] and input values [[a&b]].</p>
<p>Returns [http://example.org/some/path] for parameters [] and input values [[http://example.org/some/path]].</p>
<p>Returns [urn:valid:uri] for parameters [] and input values [[urn:valid:uri]].</p>
<p>Returns [http://www.broken%20domain.com/broken%20weird%20path%20%C3%A4%C3%B6%C3%BC/nice/path/andNowSomeFragment#fragment%C3%A4%C3%B6%C3%BC] for parameters [] and input values [[http://www.broken domain.com/broken weird path äöü/nice/path/andNowSomeFragment#fragmentäöü]].</p>
<p>Returns [http://domain/%23%23path#] for parameters [] and input values [[http://domain/##path#]].</p>
<h4 id="encode-url">Encode URL</h4>
<p>URL encodes the string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>encoding</td>
<td>String</td>
<td>The character<br>
encoding.</td>
<td>UTF-8</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>urlEncode</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [ab] for parameters [] and input values [[ab]].</p>
<p>Returns [a%26b] for parameters [] and input values [[a&b]].</p>
<p>Returns [http%3A%2F%2Fexample.org%2Fsome%2Fpath] for parameters [] and input values [[http://example.org/some/path]].</p>
<h3 id="numeric-1">Numeric</h3>
<h4 id="normalize-physical-quantity">Normalize physical quantity</h4>
<p>Normalizes physical quantities. Can either convert to a configured unit or to SI base units. For instance for lengths, values will be converted to metres if no target unit is configured. Will output the pure numeric value without the unit. If one input is provided, the physical quantities are parsed from the provided strings of the form “1 km”. If two inputs are provided, the numeric values are parsed from the first input and the units are parsed from the second inputs.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>targetUnit</td>
<td>String</td>
<td>Target unit. Can be left<br>
empty to convert to the<br>
respective SI base<br>
units.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>numberFormat</td>
<td>String</td>
<td>The IETF BCP 47 language<br>
tag, e.g., ‘en’.</td>
<td>en</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>PhysicalQuantitiesNormalizer</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.measure</code>.</p>
<p>SI units and common derived units are supported. The following section lists all supported units. By default, all quantities are normalized to their base unit. For instance, lengths will be normalized to metres.</p>
<p><em>Time</em></p>
<p>Time is expressed in seconds (s). The following alternative units are supported: mo_s, mo_g, a, min, a_g, mo, mo_j, a_j, h, a_t, d.</p>
<p><em>Length</em></p>
<p>Length is expressed in metres (m). The following alternative units are supported: in, nmi, Ao, mil, yd, AU, ft, pc, fth, mi, hd.</p>
<p><em>Mass</em></p>
<p>Mass is expressed in kilograms (kg). The following alternative units are supported: lb, ston, t, stone, u, gr, lcwt, oz, g, scwt, dr, lton.</p>
<p><em>Electric current</em></p>
<p>Electric current is expressed in amperes (A). The following alternative units are supported: Bi, Gb.</p>
<p><em>Temperature</em></p>
<p>Temperature is expressed in kelvins (K). The following alternative units are supported: Cel.</p>
<p><em>Amount of substance</em></p>
<p>Amount of substance is expressed in moles (mol).</p>
<p><em>Luminous intensity</em></p>
<p>Luminous intensity is expressed in candelas (cd).</p>
<p><em>Area</em></p>
<p>Area is expressed in square metres (m²). The following alternative units are supported: m2, ar, syd, cml, b, sft, sin.</p>
<p><em>Volume</em></p>
<p>Volume is expressed in cubic metres (㎥). The following alternative units are supported: st, bf, cyd, cr, L, l, cin, cft, m3.</p>
<p><em>Energy</em></p>
<p>Energy is expressed in joules (J). The following alternative units are supported: cal_IT, eV, cal_m, cal, cal_th.</p>
<p><em>Angle</em></p>
<p>Angle is expressed in radians (rad). The following alternative units are supported: circ, gon, deg, ‘,’’.</p>
<p><em>Others</em></p>
<ul>
<li>1/m, derived units: Ky</li>
<li>kg/(m·s), derived units: P</li>
<li>bit/s, derived units: Bd</li>
<li>bit, derived units: By</li>
<li>Sv</li>
<li>N</li>
<li>Ω, derived units: Ohm</li>
<li>T, derived units: G</li>
<li>sr, derived units: sph</li>
<li>F</li>
<li>C/kg, derived units: R</li>
<li>cd/m², derived units: sb, Lmb</li>
<li>Pa, derived units: bar, atm</li>
<li>kg/(m·s²), derived units: att</li>
<li>m²/s, derived units: St</li>
<li>A/m, derived units: Oe</li>
<li>kg·m²/s², derived units: erg</li>
<li>kg/m³, derived units: g%</li>
<li>mho</li>
<li>V</li>
<li>lx, derived units: ph</li>
<li>m/s², derived units: Gal, m/s2</li>
<li>m/s, derived units: kn</li>
<li>m·kg/s², derived units: gf, lbf, dyn</li>
<li>m²/s², derived units: RAD, REM</li>
<li>C</li>
<li>Gy</li>
<li>Hz</li>
<li>H</li>
<li>lm</li>
<li>W</li>
<li>Wb, derived units: Mx</li>
<li>Bq, derived units: Ci</li>
<li>S <strong>Example Values</strong></li>
</ul>
<p>Returns [1000.0] for parameters [] and input values [[1 km]].</p>
<p>Returns [0.3048] for parameters [] and input values [[1.0000 ft]].</p>
<p>Returns [0.45359237] for parameters [] and input values [[1.0lb]].</p>
<p>Returns [1.0] for parameters [] and input values [[1000000000.0 nm]].</p>
<p>Returns [-1000000.0] for parameters [] and input values [[-1E6 m]].</p>
<p>Returns [1000.5] for parameters [numberFormat -> de] and input values [[1.000,5 m]].</p>
<p>Returns [1000.5] for parameters [] and input values [[1,000.5 m]].</p>
<p>Returns [0.621371192237334] for parameters [targetUnit -> mi] and input values [[1 km]].</p>
<p>Fails validation and thus returns [] for parameters [targetUnit -> m] and input values [[1 kg]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[100.0]].</p>
<p>Returns [1000.0] for parameters [] and input values [[1], [km]].</p>
<p>Returns [1000.0, 10.0] for parameters [] and input values [[1, 10000], [km, mm]].</p>
<p>Fails validation and thus returns [] for parameters [] and input values [[1, 10000, 10], [km, mm]].</p>
<h4 id="aggregate-numbers">Aggregate numbers</h4>
<p>Aggregates all numbers in this set using a mathematical operation.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>operator</td>
<td>String</td>
<td>One of ‘+’, ’*‘, ’min’,<br>
‘max’, ‘average’.</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>aggregateNumbers</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<h4 id="compare-numbers">Compare numbers</h4>
<p>Compares the numbers of two sets. Returns 1 if the comparison yields true and 0 otherwise. If there are multiple numbers in both sets, the comparator must be true for all numbers. For instance, {1,2} < {2,3} yields 0 as not all numbers in the first set are smaller than in the second.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>comparator</td>
<td>Enum</td>
<td>No description</td>
<td>less</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>compareNumbers</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<h4 id="count-values">Count values</h4>
<p>Counts the number of values.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>count</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [1] for parameters [] and input values [[value1]].</p>
<p>Returns [2] for parameters [] and input values [[value1, value2]].</p>
<h4 id="extract-physical-quantity-1">Extract physical quantity</h4>
<p>Extracts physical quantities, such as length or weight values. Values are expected of the form ‘{Number}{UnitPrefix}{Symbol}’ and are converted to the base unit.</p>
<p>Example:</p>
<ul>
<li>Given a value ‘10km, 3mg’.</li>
<li>If the symbol parameter is set to ‘m’, the extracted value is 10000.</li>
<li>If the symbol parameter is set to ‘g’, the extracted value is 0.001.</li>
</ul>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>symbol</td>
<td>String</td>
<td>The symbol of the<br>
dimension, e.g., ‘m’ for<br>
meter.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>numberFormat</td>
<td>String</td>
<td>The IETF BCP 47 language<br>
tag, e.g. ‘en’.</td>
<td>en</td>
</tr>
<tr class="odd">
<td>filter</td>
<td>String</td>
<td>Only extracts from values<br>
that contain the given<br>
regex (case-insensitive)<br>
.</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>index</td>
<td>int</td>
<td>If there are multiple<br>
matches, retrieve the<br>
value with the given<br>
index (zero-based).</td>
<td>0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>extractPhysicalQuantity</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<h4 id="format-number">Format number</h4>
<p>Formats a number according to a user-defined pattern. The pattern syntax is documented at: https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>pattern</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>locale</td>
<td>String</td>
<td>No description</td>
<td>en</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>formatNumber</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [001] for parameters [pattern -> 000] and input values [[1]].</p>
<p>Returns [000123.780] for parameters [pattern -> 000000.000] and input values [[123.78]].</p>
<p>Returns [123,456.789] for parameters [pattern -> ###,###.###] and input values [[123456.789]].</p>
<p>Returns [123.456,789] for parameters [pattern -> ###.###,###, locale -> de] and input values [[123456.789]].</p>
<p>Returns [10 apples] for parameters [pattern -> # apples] and input values [[10]].</p>
<p>Returns [0010] for parameters [pattern -> 000’0’] and input values [[1]].</p>
<p>Returns [1] for parameters [pattern -> 0] and input values [[1.0]].</p>
<h4 id="logarithm">Logarithm</h4>
<p>Transforms all numbers by applying the logarithm function. Non-numeric values are left unchanged.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>base</td>
<td>int</td>
<td>No description</td>
<td>10</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>log</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<h4 id="numeric-operation">Numeric operation</h4>
<p>Applies a numeric operation to the values of multiple input operators. Uses double-precision floating-point numbers for computation.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>operator</td>
<td>String</td>
<td>The operator to be<br>
applied to all values.<br>
One of ‘+’, ‘-’, ’*‘,<br>
’/’</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>numOperation</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [2.0] for parameters [operator -> +] and input values [[1], [1]].</p>
<p>Returns [0.0] for parameters [operator -> -] and input values [[1], [1]].</p>
<p>Returns [30.0] for parameters [operator -> *] and input values [[5], [6]].</p>
<p>Returns [2.5] for parameters [operator -> /] and input values [[5], [2]].</p>
<p>Returns [] for parameters [operator -> +] and input values [[1], [no number]].</p>
<p>Returns [1.0] for parameters [operator -> *] and input values [[1]].</p>
<p>Returns [3.0] for parameters [operator -> +] and input values [[1, 1], [1]].</p>
<h4 id="numeric-reduce">Numeric reduce</h4>
<p>Strip all non-numeric characters from a string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>keepPunctuation</td>
<td>boolean</td>
<td>No description</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>numReduce</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [12] for parameters [keepPunctuation -> false] and input values [[some1.2Value]].</p>
<p>Returns [1.2] for parameters [keepPunctuation -> true] and input values [[some1.2Value]].</p>
<h3 id="parser">Parser</h3>
<h4 id="parse-date-1">Parse date</h4>
<p>Parses and normalizes dates in different formats.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inputDateFormat-<br>
Id</td>
<td>Enum</td>
<td>The input date/time<br>
format used for parsing<br>
the date/time<br>
string.</td>
<td>w3cDate</td>
</tr>
<tr class="even">
<td>alternativeInput-<br>
Format</td>
<td>String</td>
<td>An input format string<br>
that should be used<br>
instead of the selected<br>
input format. Java<br>
DateFormat string.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>outputDateFormat-<br>
Id</td>
<td>Enum</td>
<td>The output date/time<br>
format used for parsing<br>
the date/time<br>
string.</td>
<td>w3cDate</td>
</tr>
<tr class="even">
<td>alternativeOutput-<br>
Format</td>
<td>String</td>
<td>An output format string<br>
that should be used<br>
instead of the selected<br>
output format. Java<br>
DateFormat string.</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>DateTypeParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [1999-03-20] for parameters [inputDateFormatId -> German style date format, outputDateFormatId -> w3c Date] and input values [[20.03.1999]].</p>
<p>Returns [20.03.1999] for parameters [inputDateFormatId -> w3c Date, outputDateFormatId -> German style date format] and input values [[1999-03-20]].</p>
<p>Returns [2017-04-04] for parameters [inputDateFormatId -> common ISO8601, outputDateFormatId -> w3c Date] and input values [[2017-04-04T00:00:00.000+02:00]].</p>
<p>Returns [2017-04-04] for parameters [inputDateFormatId -> common ISO8601, outputDateFormatId -> w3c Date] and input values [[2017-04-04T00:00:00+02:00]].</p>
<p>Returns [1999-03-20T20:34.44] for parameters [alternativeInputFormat -> dd.MM.yyyy HH:mm.ss, alternativeOutputFormat -> yyyy-MM-dd’T’HH:mm.ss] and input values [[20.03.1999 20:34.44]].</p>
<p>Returns [12:20:00.000] for parameters [inputDateFormatId -> excelDateTime, outputDateFormatId -> xsdTime] and input values [[12:20:00.000]].</p>
<p>Returns [–01] for parameters [inputDateFormatId -> w3c YearMonth, outputDateFormatId -> w3c Month] and input values [[2020-01]].</p>
<p>Returns [—31] for parameters [inputDateFormatId -> w3c MonthDay, outputDateFormatId -> w3c Day] and input values [[–12-31]].</p>
<p>Returns [–12-31] for parameters [inputDateFormatId -> w3c Date, outputDateFormatId -> w3c MonthDay] and input values [[2020-12-31]].</p>
<p>Fails validation and thus returns [] for parameters [inputDateFormatId -> w3c MonthDay, outputDateFormatId -> w3c Date] and input values [[–12-31]].</p>
<p>Returns [2020-02-22T16:34:14] for parameters [alternativeInputFormat -> yyyy-MM-dd HH:mm:ss.SSS, outputDateFormatId -> w3cDateTime] and input values [[2020-02-22 16:34:14.000]].</p>
<h4 id="parse-float">Parse float</h4>
<p>Parses and normalizes float values.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>commaAsDecimal-<br>
Point</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
<tr class="even">
<td>thousandSeparator</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
<tr class="odd">
<td>bracketsFor-<br>
Negative</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>FloatTypeParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<h4 id="parse-geo-coordinate">Parse geo coordinate</h4>
<p>Parses and normalizes geo coordinates.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>GeoCoordinateParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<h4 id="parse-geo-location">Parse geo location</h4>
<p>Parses and normalizes geo locations like continents, countries, states and cities.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>parseTypeId</td>
<td>Enum</td>
<td>What type of location<br>
should be parsed.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>fullStateName</td>
<td>boolean</td>
<td>Set to true if the full<br>
state name should be<br>
output instead of the<br>
2-letter code.</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>GeoLocationParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<h4 id="parse-integer">Parse integer</h4>
<p>Parses integer values.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>commaAsDecimal-<br>
Point</td>
<td>boolean</td>
<td>Use comma as decimal<br>
point (uses a point,<br>
otherwise)</td>
<td>false</td>
</tr>
<tr class="even">
<td>thousandSeparator</td>
<td>boolean</td>
<td>Use comma or point to<br>
separate digits</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>IntegerParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<h4 id="parse-isin">Parse ISIN</h4>
<p>Parses International Securities Identification Numbers (ISIN) values and fails if the String is no valid ISIN.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>IsinParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<h4 id="parse-skos-term">Parse SKOS term</h4>
<p>Parses values from a SKOS ontology.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>surfaceFormTo-<br>
Representation-<br>
Mapping</td>
<td>Map</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>SkosTypeParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.discoverer</code>.</p>
<h4 id="parse-string">Parse string</h4>
<p>Parses string values, basically an identity function.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>StringParser</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.schema.discovery.parser</code>.</p>
<h4 id="clean-html-2">Clean HTML</h4>
<p>Cleans HTML using a tag white list and allows selection of HTML sections with xPath or cssSelector expressions. If the tag or attribute white lists are left empty default white lists will be used. The operator takes two inputs: the page HTML and (optional) the page Url which may be needed to resolve relative links in the page HTML.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>tagWhiteList</td>
<td>String</td>
<td>Tags to keep in the<br>
cleaned Text (or<br>
reference to a<br>
configuration).</td>
<td><em>empty string</em></td>
</tr>
<tr class="even">
<td>attributeWhite-<br>
List</td>
<td>String</td>
<td>Tags to keep in the<br>
cleaned Text (or<br>
reference to a<br>
configuration).</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>selectors</td>
<td>Multiline-<br>
String-<br>
Parameter</td>
<td>CSS or XPath queries for<br>
selection of content (or<br>
reference to a<br>
configuration). Comma<br>
separated. CssSelectors<br>
can be pipe separated<br>
for non-sequential<br>
execution.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>method</td>
<td>Enum</td>
<td>Selects use of xPath or<br>
css selectors (‘xPath’<br>
or ‘cssSelectors’).</td>
<td>xPath</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>htmlCleaner</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.plugins.html</code>.</p>
<h3 id="replace-1">Replace</h3>
<h4 id="excel-map">Excel map</h4>
<p>Replaces values based on a map of values read from a file in Open XML format (XLSX). The XLSX file may contain several sheets of the form:</p>
<p>mapFrom,mapTo <source string="">,<target string=""> … and more</target></p>
<p>An empty string can be created in Excel and alternatives by inserting =“” in the input line of a cell.</p>
<p class="alert-info">Note that the mapping table will be cached in memory. If the Excel file is updated (even while transforming), the map will be reloaded within seconds.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>excelFile</td>
<td>Resource</td>
<td>Excel file inside the<br>
resources directory<br>
containing one or more<br>
sheets with mapping<br>
tables.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>sheetName</td>
<td>String</td>
<td>The sheet that contains<br>
the mapping table or<br>
empty if the first sheet<br>
should be taken.</td>
<td><em>empty string</em></td>
</tr>
<tr class="odd">
<td>skipLines</td>
<td>int</td>
<td>How many rows to skip<br>
before reading the<br>
mapping table. By<br>
default the expected<br>
header row is<br>
skipped.</td>
<td>1</td>
</tr>
<tr class="even">
<td>strict</td>
<td>boolean</td>
<td>If set to true the<br>
operator throws<br>
validation errors for<br>
values it cannot map. If<br>
set to false it will<br>
output them unchanged.</td>
<td>true</td>
</tr>
<tr class="odd">
<td>conflictStrategy</td>
<td>Enum</td>
<td>The strategy how to cope<br>
with map conflicts when<br>
in strict-mode. Current<br>
strategies are to retain<br>
the values and to remove<br>
them.</td>
<td>retain</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>excelMap</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.excel</code>.</p>
<h4 id="map">Map</h4>
<p>Replaces values based on a map of values.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>map</td>
<td>Map</td>
<td>A map of values</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>default</td>
<td>String</td>
<td>Default if the map<br>
defines no value</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>map</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.replace</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [Value1] for parameters [map -> Key1:Value1,Key2:Value2, default -> Undefined] and input values [[Key1]].</p>
<p>Returns [Undefined] for parameters [map -> Key1:Value1,Key2:Value2, default -> Undefined] and input values [[Key1X]].</p>
<h4 id="map-with-default">Map with default</h4>
<p>Takes two inputs. Tries to map the first input based on the map of values parameter config. If the input value is not found in the map, it takes the value of the second input. The indexes of the mapped value and the default value match. If there are less default values than values to map, the last default value is replicated to match the count.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>map</td>
<td>Map</td>
<td>A map of values</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>mapWithDefaultInput</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.replace</code>.</p>
<h4 id="regex-replace">Regex replace</h4>
<p>Replace all occurrences of a regex “regex” with “replace” in a string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>regex</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>replace</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>regexReplace</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.replace</code>.</p>
<h4 id="replace-2">Replace</h4>
<p>Replace all occurrences of a string “search” with “replace” in a string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>search</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>replace</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>replace</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.replace</code>.</p>
<h3 id="selection">Selection</h3>
<h4 id="regex-selection">Regex selection</h4>
<pre><code>  This transformer takes 3 inputs.
  The first input should have exactly one value that should be passed out again untouched.
  The second input has at least two Regex values - two in order to make sense.
  The third input should have exactly one value which is checked against the regexes.

  The result of the transformer is a sequence with the same length of number of regexes.
  For the output value (of the first input) is set to each position in this sequence where
  the related regex also matched.

  If oneOnly is true only the position of the <strong>first</strong> matching regex will be set to the output value.</code></pre>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>oneOnly</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>regexSelect</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.selection</code>.</p>
<h3 id="sequence">Sequence</h3>
<h4 id="count-values-1">Count values</h4>
<p>Counts the number of values.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>count</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.numeric</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [1] for parameters [] and input values [[value1]].</p>
<p>Returns [2] for parameters [] and input values [[value1, value2]].</p>
<h4 id="get-value-by-index">Get value by index</h4>
<p>Returns the value found at the specified index. Fails or returns an empty result depending on failIfNoFound is set or not. Please be aware that this will work only if the data source supports some kind of ordering like XML or JSON. This is probably not a good idea to do with RDF models.</p>
<pre><code>   If emptyStringToEmptyResult is true then instead of a result with an empty String, an empty result is returned.</code></pre>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>index</td>
<td>int</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>failIfNotFound</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
<tr class="odd">
<td>emptyStringToEmpty-<br>
Result</td>
<td>boolean</td>
<td>No description</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>getValueByIndex</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.sequence</code>.</p>
<h4 id="sequence-values-to-indexes">Sequence values to indexes</h4>
<p>Transforms the sequence of values to their respective indexes in the sequence. Example: - (“a”, “b”, “c”) becomes (0, 1, 2)</p>
<p>If there is more than one input, the values are numbered from the first input on and continued for the next inputs. Applied against an RDF source the order might not be deterministic.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>toSequenceIndex</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.sequence</code>.</p>
<h3 id="substring-1">Substring</h3>
<h4 id="strip-postfix">Strip postfix</h4>
<p>Strips a postfix of a string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>postfix</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>stripPostfix</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.substring</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns <a href="#value">value</a> for parameters [postfix -> Postfix] and input values [[valuePostfix]].</p>
<p>Returns <a href="#value">Value</a> for parameters [postfix -> Postfix] and input values [<a href="#value">Value</a>].</p>
<h4 id="strip-prefix">Strip prefix</h4>
<p>Strips a prefix of a string.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>prefix</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>stripPrefix</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.substring</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns <a href="#value">Value</a> for parameters [prefix -> prefix] and input values [[prefixValue]].</p>
<p>Returns [ValueWithoutPrefix] for parameters [prefix -> prefix] and input values [[ValueWithoutPrefix]].</p>
<h4 id="strip-uri-prefix-1">Strip URI prefix</h4>
<p>Strips the URI prefix and decodes the remainder. Leaves values unchanged which are not a valid URI.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>stripUriPrefix</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.substring</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns <a href="#value">value</a> for parameters [] and input values [[http://example.org/some/path/to/value]].</p>
<p>Returns <a href="#value">value</a> for parameters [] and input values [[urn:scheme:value]].</p>
<p>Returns [encoded välue] for parameters [] and input values [[http://example.org/some/path/to/encoded%20v%C3%A4lue]].</p>
<p>Returns <a href="#value">value</a> for parameters [] and input values [<a href="#value">value</a>].</p>
<h4 id="substring-2">Substring</h4>
<p>Returns a substring between ‘beginIndex’ (inclusive) and ‘endIndex’ (exclusive). If ‘endIndex’ is 0 (default), it is ignored and the entire remaining string starting with ‘beginIndex’ is returned. If ‘endIndex’ is negative, -endIndex characters are removed from the end.</p>
<table>
<colgroup>
<col style="width: 25%">
<col style="width: 12%">
<col style="width: 31%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>beginIndex</td>
<td>int</td>
<td>The beginning index,<br>
inclusive.</td>
<td>0</td>
</tr>
<tr class="even">
<td>endIndex</td>
<td>int</td>
<td>The end index, exclusive.<br>
Ignored if set to 0,<br>
i.e., the entire<br>
remaining string<br>
starting with<br>
‘beginIndex’ is<br>
returned. If negative,<br>
-endIndex characters are<br>
removed from the end\</td>
<td>0</td>
</tr>
<tr class="odd">
<td>stringMustBeIn-<br>
Range</td>
<td>boolean</td>
<td>If true, only strings<br>
will be accepted that<br>
are within the start and<br>
end indices.</td>
<td>true</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>substring</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.substring</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [a] for parameters [beginIndex -> 0, endIndex -> 1] and input values [[abc]].</p>
<p>Returns [c] for parameters [beginIndex -> 2, endIndex -> 3] and input values [[abc]].</p>
<p>Returns [c] for parameters [beginIndex -> 2, endIndex -> 4, stringMustBeInRange -> false] and input values [[abc]].</p>
<p>Returns [ab] for parameters [beginIndex -> 0, endIndex -> -1] and input values [[abc]].</p>
<p>Returns [bc] for parameters [beginIndex -> 1, endIndex -> 0] and input values [[abc]].</p>
<h4 id="trim-1">Trim</h4>
<p>Remove leading and trailing whitespaces.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>trim</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.normalize</code>.</p>
<h4 id="until-character">Until character</h4>
<p>Extracts the substring until the character given.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>untilCharacter</td>
<td>char</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>untilCharacter</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.substring</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [ab] for parameters [untilCharacter -> c] and input values [[abcde]].</p>
<p>Returns [abab] for parameters [untilCharacter -> c] and input values [[abab]].</p>
<h3 id="tokenization">Tokenization</h3>
<h4 id="camel-case-tokenizer">Camel case tokenizer</h4>
<p>Tokenizes a camel case string. That is it splits strings between a lower case characted and an upper case character.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>camelcasetokenizer</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.tokenization</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [camel, Case, String] for parameters [] and input values [[camelCaseString]].</p>
<p>Returns [nocamelcase] for parameters [] and input values [[nocamelcase]].</p>
<h4 id="tokenize">Tokenize</h4>
<p>Tokenizes all input values.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>regex</td>
<td>String</td>
<td>The regular expression<br>
used to split<br>
values.</td>
<td>\s</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>tokenize</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.tokenization</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [Hello, World] for parameters [] and input values [[Hello World]].</p>
<p>Returns [.175, .050] for parameters [regex -> ,] and input values [[.175,.050]].</p>
<h3 id="validation">Validation</h3>
<h4 id="validate-date-after-1">Validate date after</h4>
<p>Validates if the first input date is after the second input date. Outputs the first input if the validation is successful.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>allowEqual</td>
<td>boolean</td>
<td>Allow both dates to be<br>
equal.</td>
<td>false</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateDateAfter</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<p><strong>Example Values</strong></p>
<p>Fails validation and thus returns [] for parameters [] and input values [[2015-04-02], [2015-04-03]].</p>
<p>Returns [2015-04-04] for parameters [] and input values [[2015-04-04], [2015-04-03]].</p>
<p>Returns [2015-04-03] for parameters [allowEqual -> true] and input values [[2015-04-03], [2015-04-03]].</p>
<p>Fails validation and thus returns [] for parameters [allowEqual -> false] and input values [[2015-04-03], [2015-04-03]].</p>
<h4 id="validate-date-range-1">Validate date range</h4>
<p>Validates if dates are within a specified range.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>minDate</td>
<td>String</td>
<td>Earliest allowed date in<br>
YYYY-MM-DD</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>maxDate</td>
<td>String</td>
<td>Latest allowed data in<br>
YYYY-MM-DD</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateDateRange</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<h4 id="validate-number-of-values">Validate number of values</h4>
<p>Validates that the number of values lies in a specified range.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>min</td>
<td>int</td>
<td>Minimum allowed number of<br>
values</td>
<td>0</td>
</tr>
<tr class="even">
<td>max</td>
<td>int</td>
<td>Maximum allowed number of<br>
values</td>
<td>1</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateNumberOfValues</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [value1] for parameters [min -> 0, max -> 1] and input values [[value1]].</p>
<p>Fails validation and thus returns [] for parameters [min -> 0, max -> 1] and input values [[value1, value2]].</p>
<h4 id="validate-numeric-range-1">Validate numeric range</h4>
<p>Validates if a number is within a specified range.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>min</td>
<td>double</td>
<td>Minimum allowed<br>
number</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>max</td>
<td>double</td>
<td>Maximum allowed<br>
number</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateNumericRange</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<h4 id="validate-regex">Validate regex</h4>
<p>Validates if all values match a regular expression.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>regex</td>
<td>String</td>
<td>regular expression</td>
<td>\w*</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>validateRegex</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.validation</code>.</p>
<h3 id="value">Value</h3>
<h4 id="constant-1">Constant</h4>
<p>Generates a constant value.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>value</td>
<td>String</td>
<td>The constant value to be<br>
generated</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>constant</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.value</code>.</p>
<h4 id="constant-uri">Constant URI</h4>
<p>Generates a constant URI.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>value</td>
<td>Uri</td>
<td>The constant URI to be<br>
generated</td>
<td>owl:Class</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>constantUri</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.value</code>.</p>
<h4 id="current-date-1">Current date</h4>
<p>Outputs the current date.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>currentDate</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.date</code>.</p>
<h4 id="dataset-parameter">Dataset parameter</h4>
<p>Reads a meta data parameter from a dataset in Corporate Memory. If authentication is enabled, workbench.superuser must be configured.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>project</td>
<td>Project-<br>
Reference</td>
<td>The project of the<br>
dataset.</td>
<td>ProjectReference(cmem)</td>
</tr>
<tr class="even">
<td>dataset</td>
<td>TaskRefere<br>
nce</td>
<td>The dataset the meta data<br>
parameter is read<br>
from.</td>
<td><em>no default</em></td>
</tr>
<tr class="odd">
<td>key</td>
<td>String</td>
<td>No description</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>lang</td>
<td>String</td>
<td>No description</td>
<td><em>empty string</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>datasetParameter</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.workflow.operators.datasetParam</code>.</p>
<h4 id="empty-value">Empty value</h4>
<p>Generates an empty value value.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>emptyValue</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.value</code>.</p>
<h4 id="random-number">Random number</h4>
<p>Generates a set of random numbers.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>min</td>
<td>double</td>
<td>The smallest number that<br>
could be generated.</td>
<td>0.0</td>
</tr>
<tr class="even">
<td>max</td>
<td>double</td>
<td>The largest number that<br>
could be generated.</td>
<td>100.0</td>
</tr>
<tr class="odd">
<td>minCount</td>
<td>int</td>
<td>The minimum number of<br>
values to generate in<br>
each set.</td>
<td>1</td>
</tr>
<tr class="even">
<td>maxCount</td>
<td>int</td>
<td>The maximum number of<br>
values to generate in<br>
each set.</td>
<td>1</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>randomNumber</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.value</code>.</p>
<h4 id="read-parameter">Read parameter</h4>
<p>Reads a parameter from a Java Properties file.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>resource</td>
<td>Resource</td>
<td>The Java properties file<br>
to read the parameter<br>
from.</td>
<td><em>no default</em></td>
</tr>
<tr class="even">
<td>parameter</td>
<td>String</td>
<td>The name of the<br>
parameter.</td>
<td><em>no default</em></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>readParameter</code>.</p>
<p>It can be found in the package <code>org.silkframework.plugins.transformer.value</code>.</p>
<h4 id="uuid">UUID</h4>
<p>Generates UUIDs. If no input value is provided, a random UUID (type 4) is generated using a cryptographically strong pseudo random number generator. If input values are provided, a name-based UUID (type 3) is generated for each input value. Each input value will generate a separate UUID. For building a UUID from multiple inputs, the Concatenate operator can be used.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>uuid</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.transformer.value</code>.</p>
<p><strong>Example Values</strong></p>
<p>Returns [cee963a2-8f70-3e97-b51a-85ef732e66dd] for parameters [] and input values [[input value]].</p>
<p>Returns [690802dd-a317-335f-807c-e4e1e32b7b5b, 925cbd7f-377b-3fbd-8f4c-ca41529b74ad] for parameters [] and input values [[üöä!, êéè]].</p>
<h2 id="aggregations-1">Aggregations</h2>
<p>The following aggregation functions are available:</p>
<h4 id="average-1">Average</h4>
<p>Computes the weighted average.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>average</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>
<h4 id="geometric-mean">Geometric mean</h4>
<p>Compute the (weighted) geometric mean.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>geometricMean</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>
<h4 id="or-1">Or</h4>
<p>At least one input score must be within the threshold. Selects the maximum score.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>max</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>
<h4 id="and-1">And</h4>
<p>All input scores must be within the threshold. Selects the minimum score.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>min</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>
<h4 id="negate">Negate</h4>
<p>Negates the result of the first input comparison. All other inputs are ignored.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>negate</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>
<h4 id="euclidian-distance">Euclidian distance</h4>
<p>Calculates the Euclidian distance.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>quadraticMean</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>
<h4 id="scale">Scale</h4>
<p>Scales the result of the first input. All other inputs are ignored.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>factor</td>
<td>double</td>
<td>All input similarity<br>
values are multiplied<br>
with this factor.</td>
<td>1.0</td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>scale</code>.</p>
<p>It can be found in the package <code>org.silkframework.rule.plugins.aggegrator</code>.</p>

