---
title: "cmemc: SPARQL Scripts"
icon: eccenca/application-queries
tags:
  - Automate
  - SPARQL
  - cmemc
---
# SPARQL Scripts

By prepending a [Shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line to a SPARQL query file and making the file executable, it can be treated as an executable script.
To give an example, below is a simple text file with a generic SPARQL query that counts all triples in all graphs and outputs an ordered list.

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

In order to convert this text file into a SPARQL script you need to add the following line to the top of the file:

``` bash title="shebang line for SPARQL scripts"
#!/usr/bin/env -S cmemc query execute --accept text/csv
```

This will set cmemc as an interpreter for the rest of the file, and by using the query execute command, the rest of the file will be used as a SPARQL query.

Now you need to define your SPARQL file as executable and run it:

``` shell-session
$ chmod a+x ./count-graphs.sh
```

``` shell-session
$ ./count-graphs.sh
graph,triples
https://vocab.eccenca.com/shacl/,4510
https://vocab.eccenca.com/auth/,240
https://ns.eccenca.com/example/data/vocabs/,169
https://ns.eccenca.com/data/ac/,66
https://ns.eccenca.com/data/queries/,39
https://ns.eccenca.com/data/config/,4
https://ns.eccenca.com/data/userinfo/,4
```

