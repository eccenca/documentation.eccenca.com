# Link IDS event to a knowledge graph via advanced tools

## Introduction
In this tutorial, we are using the Splunk app Sauron, like example. This app contains several dasboards to help the analysts to navigate in the Hayabusa or Sigma alerts before searching manually in the data via the SPL (Search Processing Language) in Splunk.

Demo of Sauron:
![](splunk-app-sauron-demo.gif)

In this demo, the user selects the indexes of his investigation and select a alert message before searching manually. Splunk, automatically, refreshes the dashboard after each interaction of this user.



(1) export data in Splunk to Corporate Memory on the fly, (2) reconcile automatically the complex data (figure~\ref{linking}) and (3) execute these workflows and SPARQL update query directly in eccenca Corporate Memorty via his own Splunk dashboards. This scenario is for advanced users and it may be proposed in a future tutorial.

In this tutorial, we learn to:

- export Splunk data to Corporate Memory when Splunk refresh the list of IDS messages.

- reconcile automatically the ID/labels/messages into indicators of compromise rules to Mitre’s Attack-patterns and IDS alerts

- join the details of alerts in a SPLUNK dashboard

1. install the "eccenca" app in Splunk
   
2. request the Linked Open Data endpoints in Splunk, like the Wikidata endpoint with its referential of extension of files
   
3. request a private knowledge graph
   
4. join the details of alerts in a SPLUNK dashboard.

To facilate these tasks, we have developed a Splunk app to extend the SPL to support the [SPARQL protocol](https://www.w3.org/TR/sparql11-protocol/). We are starting to install this app.

We learn how to 




## Install the Splunk app "Sauron" ?

TODO

!!! Success

    TODO Demo SPARQL query with Wikidata (clean the code)

```xml
    <dashboard version="1.1" script="investigation_high-level_request.js,expand_table_row_html.js,expand_table_row_barchart.js,">
  <label>Examples with the SPARQL command</label>
  <row>
    <panel>
      <title>SPARQL query with Wikidata</title>
      <table>
        <search>
          <query>| sparql 
config="wikidata"
query="
PREFIX xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; 
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; 
PREFIX schema: &lt;http://schema.org/&gt; 
PREFIX bd: &lt;http://www.bigdata.com/rdf#&gt; 
PREFIX wikibase: &lt;http://wikiba.se/ontology#&gt; 
PREFIX wd: &lt;http://www.wikidata.org/entity/&gt; 
PREFIX wdt: &lt;http://www.wikidata.org/prop/direct/&gt; 

select  ?vul ?Label ?Description ?url
where {
    ?vul wdt:P31 wd:Q631425 .
    
    BIND(URI(CONCAT('https://www.wikidata.org/wiki/Special:GoToLinkedPage/fr,en/',
               replace(xsd:string(?vul),  'http://www.wikidata.org/entity/', ''))) as ?url)
  
    # Doc : https://www.mediawiki.org/wiki/Wikidata_query_service/User_Manual#Label_service
    SERVICE wikibase:label {
         bd:serviceParam wikibase:language 'fr,en' .
         ?vul rdfs:label ?Label .
         ?vul schema:description ?Description .
    }
} 
LIMIT 10
"</query>
          <earliest>-24h@h</earliest>
          <latest>now</latest>
        </search>
        <option name="drilldown">row</option>
        <option name="refresh.display">progressbar</option>
        <option name="wrap">false</option>
        <fields>["Label","Description"]</fields>
        <drilldown>
          <link target="_blank">$row.url|n$</link>
        </drilldown>
      </table>
    </panel>
  </row>

```


## Understand a Splunk dashboard

A Splunk dashboard is coded in XML. The Splunk user can modify a dashboard via a no-code interface or directly in the code.

A user can clone any dashboard before modifying it.

1. Clone the dashboard "Sigma"

![](splunk-app-sauron-clone.gif)

In your cloned dashboard "SIGMA" of Sauron, you can find:

- the root element `form`, 
- the definition of input component to select the Splunk indexes by the user and 
- the table panel to execute a SPL query and show the result in a table

```xml
<form theme="dark">
  <label>SIGMA</label>
...
    <input type="multiselect" token="selected_index" searchWhenChanged="true">
      <label>index</label>
      <valuePrefix>index="</valuePrefix>
      <valueSuffix>"</valueSuffix>
      <delimiter> OR </delimiter>
      <fieldForLabel>index</fieldForLabel>
      <fieldForValue>index</fieldForValue>
      <search>
        <query>| eventcount summarize=false index=*
| search NOT index IN ("history", "cim_modactions", "summary")
| dedup index 
| fields index</query>
        <earliest>0</earliest>
        <latest></latest>
      </search>
      <choice value="*">all</choice>
      <default>*</default>
    </input>
...
  <row>
    <panel>
      <table>
        <search>
          <query>| tstats count where $selected_index$ sauron_metadata.sauron_source_type=hayabusa Level!=info $level$ by RuleTitle
| rename RuleTitle as "Rule name"
| sort - count</query>
          <earliest>0</earliest>
          <latest></latest>
        </search>
        <option name="drilldown">cell</option>
        <option name="refresh.display">progressbar</option>
        <drilldown>
          <set token="selected_rule">$click.value$</set>
        </drilldown>
      </table>
    </panel>
    ...
  </row>
...
</form>
```

To read this code, you need to know the Splunk concept "token". A Splunk token is a global variable in the dashboard between all the components of dashboard.

In this example, the token "selected_index" is defined by the input component and reuse it in the SPL of the table panel.

In your use case, we need to know the `RuleTitle` and the `RuleFile` to link these events to our knowledge base. We starts to test the query without token.

TODO explain the query ?
```spl
index="*" OR index="bumblebee202208_evtx" OR index="bumblebee202208_zeek_suricata" sauron_metadata.sauron_source_type=hayabusa Level!=info
| table RuleTitle RuleFile 
| dedup RuleTitle RuleFile
```

After with the tokens necessary to select the `RuleTitle` and the `RuleFile`.
```spl
$selected_index$ sauron_metadata.sauron_source_type=hayabusa  Level!=info
| table RuleTitle RuleFile 
| dedup RuleTitle RuleFile
```

!!! Success

        You can insert a new table panel with this query to test it.

## Export Splunk data to Corporate Memory

This SPL query is sensible only at the selection of indexes. So, we need to recalculate this query when the indexes change in the dashboard.

Gandalf app gives the tool to extract from Splunk the result of this SPL query. When the user selects an index, Gandalf writes a script bash (TODO) with the SPL query in the xml element `change` of input component, like in this example:

```
    <input type="multiselect" token="selected_index" searchWhenChanged="true">
      <label>index</label>
      <valuePrefix>index="</valuePrefix>
      <valueSuffix>"</valueSuffix>
      <delimiter> OR </delimiter>
      <fieldForLabel>index</fieldForLabel>
      <fieldForValue>index</fieldForValue>
      <search>
        <query>| eventcount summarize=false index=*
| search NOT index IN ("history", "cim_modactions", "summary")
| dedup index 
| fields index</query>
        <earliest>0</earliest>
        <latest></latest>
      </search>
      <choice value="*">all</choice>
      <default>*</default>
      <change>
          <set token="source_1">{
          "index": $selected_index|s$,
          "search": "sauron_metadata.sauron_source_type=hayabusa Level!=info | table RuleTitle RuleFile | dedup RuleTitle RuleFile",
          "workflowID": "b5deffdd-f4b9-4d1a-8ea0-9b3410d915e7_PoC21:investigation-hayabusa"
          }</set>
      </change>
    </input>
```

Gandalf waits 3 parameters: indexes (via a token here), the query (SPL) and the workflow ID.
The script can be executed automatically via the cron of server.

The result of this script is a file



## Export Splunk data to Corporate Memory


## Create a new Splunk app for your use case

TODO
