---
icon: material/memory
status: new
---

# Graph Insights Sizing

This section is intended to provide assistance in estimating the required memory and the resulting indexing speed of Graph Insights on the basis of empirical values.

The following is a statistical evaluation of RDF Graph Insights on the indexing speed and the memory requirements.
For this, we considered altogether 26 datasets with up to 352M triples.
The benchmark has been conducted for different JVM memory allocations in order to roughly estimate the memory requirements to support a desired amount of triples.
Moreover, it compares our two indexing methods, namely the "one pass" and "two pass" approaches.
In particular, we generate the index (compressed dictionary and triples) in a single parsing iteration (namely "one pass": faster, higher memory consumption) or in two separate parsing iterations ("two pass": slower, but less memory consumption).

For the experiments, we used Graph Insights v16.0.1 and conducted them on an Intel(R) Core(TM) i7-3930K CPU @ 3.20GHz, 6 cores with 2 threads per core, 64 GB DDR3 @ 1334MHz.

## Memory and Disk Space Requirements

The following table should be read as a lookup table: Assuming the JVM is allocated with a certain amount of memory (**JVM Memory (GB)**), how many triples can you expect to be able to index (**Max. Num. Triples**) with RDF Graph Insights? Please note that a comparison of memory consumption of "one pass" against "two pass" for a specific memory setting should be treated with caution, as the results often refer to a different number of datasets.
Furthermore, this table also lists the initial memory allocation for loading an existing index into Graph Insights for exploration.
Since Graph Insights uses caching for performance reasons the latter will increase over time up to the given allocation limit.

| Approach  | JVM Memory (GB) | Num. Datasets | Max. Num. Triples | Max. Num. Classes | Max. Num. Instances | Indexing (MB) | Exploration after restart (MB) |
| :-------: | --------------: | ------------: | ----------------: | ----------------: | ------------------: | ------------: | ----------------------------: |
| One Pass  | 1               | 16            | 5,344,375         | 809               | 776,845             | 787           | 185                           |
| Two Pass  | 1               | 16            | 5,344,414         | 809               | 776,845             | 741           | 184                           |
| One Pass  | 5               | 19            | 19,903,402        | 809               | 1,583,073           | 2,839         | 238                           |
| Two Pass  | 5               | 19            | 19,903,402        | 809               | 1,583,073           | 4,174         | 238                           |
| One Pass  | 10              | 22            | 72,820,690        | 809               | 5,401,200           | 9,749         | 1,485                         |
| Two Pass  | 10              | 23            | 152,528,023       | 809               | 19,837,857          | 10,011        | 2,749                         |
| One Pass  | 15              | 22            | 72,820,690        | 809               | 5,401,200           | 10,446        | 1,485                         |
| Two Pass  | 15              | 24            | 158,962,783       | 10,193            | 19,837,857          | 14,827        | 3,633                         |
| One Pass  | 20              | 23            | 152,528,023       | 809               | 19,837,857          | 19,852        | 2,846                         |
| Two Pass  | 20              | 25            | 257,831,425       | 10,193            | 50,567,464          | 19,421        | 5,833                         |
| One Pass  | 30              | 24            | 158,962,783       | 10,193            | 19,837,857          | 28,582        | 3,762                         |
| Two Pass  | 30              | 25            | 257,831,425       | 10,193            | 50,567,464          | 28,736        | 5,834                         |
| One Pass  | 40              | 24            | 158,962,783       | 10,193            | 19,837,857          | 36,022        | 4,043                         |
| Two Pass  | 40              | 26            | 352,417,591       | 10,193            | 50,567,464          | 40,689        | 17,059                        |

### Disk Space Considerations

Disk space consumption can be estimated in close relation to working memory usage:

-   On average, **~30 MB per 1 million triples** are required both in memory and on disk.
-   In **managed mode**, Graph Insights maintains two index directories (to support hot-swapping during reindexing).
    In this case, disk usage is roughly **~60 MB per 1 million triples**.
-   Actual disk usage may vary depending on dataset characteristics (e.g., schema, dictionary compression ratio, and indexing options).

For practical planning, disk space can be roughly approximated by scaling the memory requirements listed in the table above with the adjustment for managed mode if applicable.

## Indexing Throughput

The indexing throughput metric that can act as a factor to estimate the initial generation time of an index for a given RDF dump file before it can be explored in Graph Insights.
Assuming our dataset has 10,000,000 triples and we are using the "one pass" approach, the average required time corresponds to `10,000,000 / 50,500 ≈ 180(s) = 3(m)`.
As can be seen, the maximum indexing throughput is much higher (factor `~3`) since the individual speed depends on the dataset and its inherent characteristics such as the depth of the class and property hierarchy or the number of object property assertions in connection with the reasoning mode of Graph Insights.
As soon as an index has been created and saved on disk, it only takes a fraction of the indexing time to load it into memory for all subsequent calls of Graph Insights.

| Approach | Mean Triples / Second | Maximum Triples / Second |
| :------: | --------------------: | -----------------------: |
| One pass | 50.5K                 | 182.0K                   |
| Two pass | 31.0K                 | 104.3K                   |

## CPU Usage

The following observations apply to a **single-user environment**.
If multiple users access Graph Insights at the same time, it is generally beneficial to configure more threads, since concurrent requests can be served in parallel.

### Indexing

!!! info "Recommendation"

    Use **6-8 threads** for indexing to get the best balance between speed and resource use.

Indexing benefits strongly from parallelism during the parsing phase, which makes up about 60% of the total work.
Adding more threads speeds this part up almost linearly up to around 6 threads.
Beyond 6-8 threads, the gains flatten out because the later phases are sequential and cannot be parallelized.
In practice, indexing can be made about 3-4 times faster than with a single thread.

### Exploration

!!! info "Recommendation"

    For exploration, **3-4 threads** are sufficient to significantly improve worst-case times.
    More threads may further reduce typical latencies, but they do not lower the maximum execution time.

The deployed exploration operations in our benchmark consisted of multiple queries executed in parallel, starting from one group node and expanding along paths up to depth 4, following both incoming and outgoing links.
We ran 847 exploration queries, selected to be representative of the dataset (covering different group node sizes and varying numbers of connected resources).
The experiments were conducted across a variety of datasets up to 250M triples:

-   **Maximum execution time:** ~10s for 1-2 threads, improved to ~5s with 3 threads, and ~4.4s with 4 or more threads.
-   **75th percentile:** ~2.6-2.8s with 1-2 threads, improved to ~1.3s with 4 threads, and ~1s with 6+ threads.-   **Beyond 4 threads:** no further improvement in maximum times was observed, though 75th percentile times continued to improve slightly.
