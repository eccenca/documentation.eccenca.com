---
icon: eccenca/module-charts
status: new
tags:
    - KnowledgeGraph
    - Dashboards
---

# Charts Catalog and Charts Integration

The **Charts Catalog** is a module suitable to visualize your data in a chart.

## Charts Management

You can open the Charts Catalog from the left main menu.
You will see a list of existing chart or the information **Your charts catalog is empty**.
From here you can create a new chart or edit an existing chart.

![](23-03-ChartCreation.gif){ class="bordered" }

After selecting **Create Chart** or an existing Chart you will see the Chart editor which is organized into four components:

### Metadata

You can give your charts a name and a description.

### Query selection

Select a query from the :eccenca-application-queries: [Query Catalog](../query-module/index.md) in order to fetch the data which you want to visualize.

The following activities can be done in this component:

- **Select a query** — select a query to visualize by clicking on a :material-plus-circle-outline: button. The Assisted chart form (see below) supports a sinble query, while the Advanced chart form can use multiple queries.
- From the dropdown menu:
    - **Parameters** — Some queries have parameters which have to be filled with real values here.
    - **Preview** — see a preview of the data that is retrieved.
    - **View in query catalog** — open the query in the query catalog.

### Chart forms

There are two types of forms: __Assisted__ and __Advanced__.

The assisted form can be used for the creation of simple chart types such as line, bar, bar-line and pie.
It consists of fields that assist you in visualizing your data.

The advanced form is totally flexible when it comes to the chart configuration.
It consists of a JSON editor that allows you to configure the chart yourself.

For more information about chart configuration and examples, visit the [echarts.apache.org](https://echarts.apache.org/examples/en/index.html).

### Preview

The main content on the right side consists of the preview, where you can see the visual results of your changes in the configuration.

When using an advanced chart, you will also see a tab with the datasets that were created from the selected queries.

## Charts Integration

You can integrate your charts into existing Node or Property shapes in order to show a charts in the context of a resource.
To do so, add :material-plus-circle-outline: the **Chart Visualization** property to the shape and select the wanted Chart.

!!! Note

    This means your Chart need to be accessible by the Shape Catalog.
    This can be achieved either by copying the chart and query resources to the graph or by import the query catalog graph into the shape catalog.

In order to adapt the Chart in the context of each shown resource, you need to use the placeholder `{{shuiResource}}` in your queries.

