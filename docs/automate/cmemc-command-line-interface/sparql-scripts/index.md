---
tags:
  - Automate
  - SPARQL
  - cmemc
---
# SPARQL Scripts

By prepending a [Shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line to a SPARQL query file and making this file executable, the query file can be treated as an executable script.
As an example, here is a simple text file with a generic SPARQL query which counts all triples in all graphs and outputs an ordered list:

``` sparql title="count-graphs.sh"
SELECT DISTINCT ?graph (COUNT(?graph) AS ?triples)
WHERE {
    GRAPH ?graph
    {
        ?s ?p ?o
    }
}
GROUP BY ?graph
ORDER BY DESC(?triples)
```

In order to make a SPARQL script out of this text file you need to add the following line on top of this file:

``` bash title="shebang line for SPARQL scripts"
#!/usr/bin/env -S cmemc query execute --accept text/csv
```

This will set cmemc as an interpreter for the rest of the file and by using the query execute command, the rest of the file will be used as a SPARQL query.

Now you need to define your SPARQL file as executable and run it:

``` shell-session
$ chmod a+x ./count-graphs.sh
```

``` shell-session
$ ./count-graphs.sh
graph,triples
https://vocab.eccenca.com/shacl/,1796
https://vocab.eccenca.com/dsm/,736
https://vocab.eccenca.com/sketch/,395
https://ns.eccenca.com/example/data/dataset/,233
https://ns.eccenca.com/example/data/vocabs/,128
urn:elds-backend-access-conditions-graph,97
https://ns.eccenca.com/data/queries/,32
http://di.eccenca.com/project/cmem,7
```

