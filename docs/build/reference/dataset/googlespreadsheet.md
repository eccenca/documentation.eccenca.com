---
title: "Excel (Google Drive)"
description: "Read data from a remote Google Spreadsheet."
icon: octicons/cross-reference-24
tags:
    - Dataset
---

# Excel (Google Drive)

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The dataset needs the document id of a "share via url" sheet on Google Drive as input.
It will automatically correct the URL and add the "export as xlsx" option to a new URL
that will be used to download an Excel Spreadsheet.
The download will be cached and treated the same way as an xlsx file in the Excel Dataset.

## Caching

The advanced parameter `invalidateCacheAfter` allows the user to specify a duration of the file cache
after which it is refreshed.
A file based cache is created to avoid CAPTCHAs. During the caching and validation of the URL
access occurs with random wait times between 1 and 5 seconds.
The cache is invalidated after 5 minutes by default.

## Parameter

### URL

Link to the document ('share with anyone having a link' must be enabled, URL parameters will be removed and corrected automatically).

- ID: `url`
- Datatype: `string`
- Default Value: `None`

### Lines to skip

The number of lines to skip in the beginning when reading files.

- ID: `linesToSkip`
- Datatype: `int`
- Default Value: `0`

## Advanced Parameter

### Streaming

Streaming enables reading and writing large Excels files. Warning: Be careful to disable streaming for large datasets (> 10MB), because of high memory consumption.

- ID: `streaming`
- Datatype: `boolean`
- Default Value: `true`

### Invalidate cache after

Duration until file based cache is invalidated.

- ID: `invalidateCacheAfter`
- Datatype: `duration`
- Default Value: `PT5M`
