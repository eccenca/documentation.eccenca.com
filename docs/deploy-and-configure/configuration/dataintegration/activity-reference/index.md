---
tags:
    - Reference
---
# Activity Reference

<!-- Auto-Generated. Do not edit directly! -->
<h2 id="project-activities">Project Activities</h2>
<p>The following activities are available for each project.</p>
<h4 id="dataset-matcher">Dataset matcher</h4>
<p>Generates matches between schema paths and datasets based on the schema discovery and profiling information of the datasets.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>datasetUri</td>
<td>String</td>
<td>If set, run dataset matching only<br>
for this particular<br>
dataset.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>DatasetMatcher</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.datamatching</code>.</p>
<h2 id="task-activities">Task Activities</h2>
<p>The following activities are available for different types of tasks.</p>
<h3 id="custom">Custom</h3>
<h4 id="execute-rest-task">Execute REST Task</h4>
<p>Executes the REST task.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteRestTask</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.workflow.operators.rest</code>.</p>
<h3 id="dataset">Dataset</h3>
<h4 id="dataset-profiler">Dataset profiler</h4>
<p>Generates profiling data of a dataset, e.g. data types, statistics etc.</p>
<table>
<colgroup>
<col style="width: 27%">
<col style="width: 16%">
<col style="width: 22%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>datasetUri</td>
<td>String</td>
<td>Optional URI of the dataset<br>
resource that should be profiled.<br>
If not specified an URI will be<br>
generated.</td>
<td></td>
</tr>
<tr class="even">
<td>uriPrefix</td>
<td>String</td>
<td>Optional URI prefix that is<br>
prepended to every generated URI,<br>
e.g. property URIs for every<br>
schema path. If not specified an<br>
URI prefix will be<br>
generated.</td>
<td></td>
</tr>
<tr class="odd">
<td>entitySample-<br>
Limit</td>
<td>String</td>
<td>How many entities should be sampled<br>
for the profiling. If left blank,<br>
all entities will be<br>
considered.</td>
<td></td>
</tr>
<tr class="even">
<td>timeLimit</td>
<td>String</td>
<td>The time in milliseconds that each<br>
of the schema extraction step and<br>
profiling step should spend on.<br>
Leave blank for unlimited<br>
time.</td>
<td></td>
</tr>
<tr class="odd">
<td>classProfiling-<br>
Limit</td>
<td>int</td>
<td>The maximum number of classes that<br>
are profiled from the extracted<br>
schema.</td>
<td></td>
</tr>
<tr class="even">
<td>schemaEntity-<br>
Limit</td>
<td>int</td>
<td>The maximum number of overall<br>
schema entities (types,<br>
properties/attributes) that will<br>
be extracted.</td>
<td></td>
</tr>
<tr class="odd">
<td>executionType</td>
<td>String</td>
<td>The execution type to be used:<br>
SPARK, LEGACY. The legacy<br>
execution uses large in-memory<br>
maps and takes longer!</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>DatasetProfiler</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.profiling</code>.</p>
<h4 id="sql-endpoint-status">SQL endpoint status</h4>
<p>Shows the SQL endpoint status.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>SqlEndpointStatus</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.sql.endpoint.activity</code>.</p>
<h4 id="types-cache">Types cache</h4>
<p>Holds the most frequent types in a dataset.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>TypesCache</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.dataset</code>.</p>
<h3 id="linkspecification">LinkSpecification</h3>
<h4 id="active-learning">Active learning</h4>
<p>Executes an active learning iteration.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>fixedRandom-<br>
Seed</td>
<td>boolean</td>
<td>No description</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ActiveLearning</code>.</p>
<p>It can be found in the package <code>org.silkframework.learning.active</code>.</p>
<h4 id="evaluate-linking">Evaluate linking</h4>
<p>Evaluates the linking task by generating links.</p>
<table>
<colgroup>
<col style="width: 27%">
<col style="width: 16%">
<col style="width: 22%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>includeReference-<br>
Links</td>
<td>boolean</td>
<td>Do not generate a link for which<br>
there is a negative reference link<br>
while always generating positive<br>
reference links.</td>
<td></td>
</tr>
<tr class="even">
<td>useFileCache</td>
<td>boolean</td>
<td>Use a file cache. This avoids<br>
memory overflows for big<br>
files.</td>
<td></td>
</tr>
<tr class="odd">
<td>partitionSize</td>
<td>int</td>
<td>The number of entities in a single<br>
partition in the cache.</td>
<td></td>
</tr>
<tr class="even">
<td>generateLinksWith-<br>
Entities</td>
<td>boolean</td>
<td>Generate detailed information about<br>
the matched entities. If set to<br>
false, the generated links won’t<br>
be shown in the Workbench.</td>
<td></td>
</tr>
<tr class="odd">
<td>writeOutputs</td>
<td>boolean</td>
<td>Write the generated links to the<br>
configured output of this<br>
task.</td>
<td></td>
</tr>
<tr class="even">
<td>linkLimit</td>
<td>int</td>
<td>If defined, the execution will stop<br>
after the configured number of<br>
links is reached.<br>
This is just a hint and the<br>
execution may produce slightly<br>
fewer or more links.</td>
<td></td>
</tr>
<tr class="odd">
<td>timeout</td>
<td>int</td>
<td>Timeout in seconds after that the<br>
matching task of an evaluation<br>
should be aborted. Set to 0 or<br>
negative to disable the<br>
timeout.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>EvaluateLinking</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.linking</code>.</p>
<h4 id="execute-linking">Execute linking</h4>
<p>Executes the linking task using the configured execution.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteLinking</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.linking</code>.</p>
<h4 id="linking-paths-cache">Linking paths cache</h4>
<p>Holds the most frequent paths for the selected entities.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>LinkingPathsCache</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.linking</code>.</p>
<h4 id="reference-entities-cache">Reference entities cache</h4>
<p>For each reference link, the reference entities cache holds all values of the linked entities.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ReferenceEntitiesCache</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.linking</code>.</p>
<h4 id="supervised-learning">Supervised learning</h4>
<p>Executes the supervised learning.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>SupervisedLearning</code>.</p>
<p>It can be found in the package <code>org.silkframework.learning.active</code>.</p>
<h3 id="scheduler-1">Scheduler</h3>
<h4 id="activate">Activate</h4>
<p>Executes the scheduler</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteScheduler</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.scheduler</code>.</p>
<h3 id="scripttask">ScriptTask</h3>
<h4 id="execute-script">Execute Script</h4>
<p>Executes the script.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteScript</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.scripttask</code>.</p>
<h3 id="transformspecification">TransformSpecification</h3>
<h4 id="execute-transform">Execute transform</h4>
<p>Executes the transformation.</p>
<table>
<colgroup>
<col style="width: 27%">
<col style="width: 16%">
<col style="width: 22%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>limit</td>
<td>IntOptionParameter</td>
<td>Limits the maximum number of<br>
entities that are<br>
transformed.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ExecuteTransform</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.transform</code>.</p>
<h4 id="transform-paths-cache">Transform paths cache</h4>
<p>Holds the most frequent paths for the selected entities.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>TransformPathsCache</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.transform</code>.</p>
<h4 id="target-vocabulary-cache">Target vocabulary cache</h4>
<p>Holds the target vocabularies</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>VocabularyCache</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.transform</code>.</p>
<h3 id="workflow">Workflow</h3>
<h4 id="execute-locally">Execute locally</h4>
<p>Executes the workflow locally.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteLocalWorkflow</code>.</p>
<p>It can be found in the package <code>org.silkframework.workspace.activity.workflow</code>.</p>
<h3 id="workflowexecution">WorkflowExecution</h3>
<h4 id="generate-spark-assembly">Generate Spark assembly</h4>
<p>Generate project and Spark assembly artifacts and deploy them using the specified configuration settings: type, artifact and options like destination in case of a simple copy</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>executeStaging</td>
<td>boolean</td>
<td>Execute loading phase</td>
<td></td>
</tr>
<tr class="even">
<td>executeTransform</td>
<td>boolean</td>
<td>Execute transform phase</td>
<td></td>
</tr>
<tr class="odd">
<td>executeLoading</td>
<td>boolean</td>
<td>Execute staging phase</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>DeploySparkWorkflow</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark</code>.</p>
<h4 id="default-execution">Default execution</h4>
<p>Executes a workflow with the executor defined in the configuration</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteDefaultWorkflow</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark</code>.</p>
<h4 id="execute-operator">Execute operator</h4>
<p>Executes a workflow on with an executor that uses Apache Spark. Depending on the Spark configuration it can still run on a single local machine or on a cluster.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>operator</td>
<td>TaskReference</td>
<td>The workflow to execute.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ExecuteSparkOperator</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark</code>.</p>
<h4 id="execute-on-spark">Execute on Spark</h4>
<p>Executes a workflow on with an executor that uses Apache Spark. Depending on the Spark configuration it can still run on a single local machine or on a cluster.</p>
<p>This plugin does not require any parameters. The identifier for this plugin is <code>ExecuteSparkWorkflow</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.spark</code>.</p>
<h4 id="execute-with-payload">Execute with payload</h4>
<p>Executes a workflow with custom payload.</p>
<table>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>configuration</td>
<td>MultilineStringParameter</td>
<td>No description</td>
<td></td>
</tr>
<tr class="even">
<td>configuration-<br>
Type</td>
<td>String</td>
<td>No description</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>ExecuteWorkflowWithPayload</code>.</p>
<p>It can be found in the package <code>org.silkframework.workbench.workflow</code>.</p>
<h4 id="generate-view">Generate view</h4>
<p>Generate and share a view on a workflow executed by the Spark executor. Executes a workflow on Spark and generates a SparkSQL temporary table instead of serializing the result. The table can be accessed via JDBC</p>
<table>
<colgroup>
<col style="width: 27%">
<col style="width: 16%">
<col style="width: 22%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="header affix">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>caching</td>
<td>boolean</td>
<td>Optional parameter that enables<br>
caching (default=false).</td>
<td></td>
</tr>
<tr class="even">
<td>userDefined-<br>
Name</td>
<td>String</td>
<td>Optional View name that is used<br>
when a view on a non virtual is<br>
generated (default =<br>
[TASK-ID]_generated_view).</td>
<td></td>
</tr>
</tbody>
</table>
<p>The identifier for this plugin is <code>GenerateSparkView</code>.</p>
<p>It can be found in the package <code>com.eccenca.di.sql.virtual</code>.</p>
<section class="footnotes">
<hr>
<ol>
<li id="fn1"><p>Hive 1.2.1 is <a href="https://github.com/odpi/specs/blob/master/ODPi-Runtime.md">ODPi</a> runtime compliant<a href="#fnref1" class="footnote-back">↩</a></p></li>
<li id="fn2"><p>^/<a href="#fnref2" class="footnote-back">↩</a></p></li>
</ol>
</section>

