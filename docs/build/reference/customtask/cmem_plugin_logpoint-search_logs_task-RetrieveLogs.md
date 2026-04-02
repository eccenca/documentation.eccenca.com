---
title: "Search for Logs"
description: "Search and retrieve logs from a Logpoint SIEM system with flexible schema output."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Search for Logs
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This plugin integrates with Logpoint systems
to search and retrieve log data based on custom queries.

## Key Features

- **Flexible Querying**: Execute custom Logpoint queries with configurable time ranges
- **Repository Filtering**: Limit searches to specific log repositories
- **Dynamic Schema**: Define output schema paths to structure the data as needed
- **Preview Actions**: Inspect available output paths and repositories before execution

## Configuration

### Authentication

Configure the connection to your Logpoint service using:
- **Service URL**: The base URL of your Logpoint instance
- **Username**: Service account username with appropriate permissions
- **Secret Key**: API secret key for authentication

### Query Parameters

- **Query**: Logpoint search query syntax (see Logpoint documentation TODO ADD LINK)
- **Time Range**: Relative time range (e.g., `Last 1 hour`, `Last 24 hours`)
- **Limit**: Maximum number of log entries to retrieve
- **Repositories**: Optional comma-separated list of specific repositories to search

### Output Schema

- **List of output paths**: Define specific fields to extract from logs
- Use the **Preview output paths** action to discover possible, available fields
- Leave empty to return all fields with automatic schema detection
- Format: comma-separated paths
- **Note:** It may occur that not all possible output paths are listed here. Logpoint follows
  a [standardized field naming convention](https://docs.logpoint.com/docs/logpoint-taxonomy-guideline/en/latest/Field%20naming%20convention.html).
  A warning will be given if at least one of the created entities does not have a value at the
  given path.

## Usage Example

### Basic Log Search

- Query: `norm_id=*`
- Time Range: `Last 1 hour`
- Limit: `1000`
- Repositories: windows, linux
- Output paths: (empty for all fields)

Common fields include:
- `source_address`: Source IP address
- `destination_address`: Destination IP address
- `user`: Username associated with the event
- `log_ts`: The timestamp of a log.
- `device_id`: The ID of a device.

## Actions

Use the plugin actions to explore and configure your searches:
- **Preview output paths**: Executes a test query to see available field paths.
- **Preview repositories**: List all accessible log repositories in your Logpoint instance.


## Parameter

### Service URL

Base URL of the Logpoint service.

- ID: `base_url`
- Datatype: `string`
- Default Value: `https://demo.logpoint.com/`



### Username

Username for authenticating with the Logpoint service. This account must have appropriate permissions to search logs and access repositories.

- ID: `account`
- Datatype: `string`
- Default Value: `partner`



### Secret Key

API secret key for authentication. This is securely encrypted and used to authenticate requests to the Logpoint service.

- ID: `secret_key`
- Datatype: `password`
- Default Value: `None`



### Query

Logpoint search query using Logpoint query syntax. Example: 'norm_id=*' or '| chart count() by device_ip'.

- ID: `query`
- Datatype: `string`
- Default Value: `None`



### Time Range

Relative time range for the search. Common values: 'Last 1 hour', 'Last 24 hours', 'Last 7 days', 'Last 30 days'.

- ID: `time_range`
- Datatype: `string`
- Default Value: `Last 1 hour`



### Limit

Maximum number of log entries to retrieve. Must be a positive integer.

- ID: `limit`
- Datatype: `Long`
- Default Value: `1000`



### Repositories

Comma-separated list of repository names to search. Leave no trailing comma here. Example: 'windows,linux,firewall'. Leave empty to search all accessible repositories. Use the 'Preview repositories' action to see available options.

- ID: `repos`
- Datatype: `string`
- Default Value: `None`



### List of output paths

Comma-separated list of field paths to include in output. Example: 'source_address, destination_address, user, log_ts'. Leave no trailing comma here. If specified, creates a fixed output schema with only these fields. Leave empty for automatic schema detection with all available fields. Use 'Preview output paths' action to discover available field names. See Logpoint field naming conventions at: https://docs.logpoint.com/docs/logpoint-taxonomy-guideline/en/latest/Field%20naming%20convention.html

- ID: `paths_list`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`