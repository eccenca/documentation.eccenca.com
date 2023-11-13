
## Configuration for connecting to Neptune backend

Configuration example:

This example configures a connection to a neptune instance in the AWS region eu-central-1. Authentication is enabled 
so it is assumed that CMEM runs on a EC2 VM with configured role for authentication to neptune. Files (uncompressed) greater than 100MB are
uploaded via S3 based bulk loader. The S3 bucket is accessed in this case via an access point which is configured here. The EC2
role CMEM runs under has write access to the bucket. One of the role the neptune cluster runs under is configured in this setting and has read access to the bucket.
On bulk load the loading runs parallel in the setting HIGH which causes higher cpu load but better performance.

Also the example disables DPs generation of tracing IDs by micrometer tracing - Neptune needs UUIDs as IDs for queries etc.

```yaml
store:
  type: neptune
  authorization: REWRITE_FROM
  neptune:
    host: "neptune123.eu-central-1.neptune.amazonaws.com"
    port: 8182
    aws:
      region: "eu-central-1"
      authEnabled: true
    s3:
      bucketNameOrAPAlias: "nap1-nnipjzugs1ar45n11n316mzagiw6heuc1a-s3alias"
      iamRoleArn: "arn:aws:iam::887770733838:role/NeptuneLoadFromS3"
      bulkLoadThresholdInMb: 100
      bulkLoadParallelism: HIGH

management.tracing.enabled: false
```


***Property: store.type***

The type of the store must be set to "neptune"

| Category | Value |
|--- | ---: |
| Default | neptune |
| Required | true |
| Valid values | NEPTUNE |
| Environment | STORE_TYPE |

Configuration of a neptune instance connection.

***Property: store.neptune.host***

The name of one of the writer endpoints of the neptune instance.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | true |
| Valid values | string |
| Environment | STORE_NEPTUNE_HOST |

***Property: store.neptune.port***

The port of the neptune instance.

| Category | Value |
|--- | ---: |
| Default | 8182 |
| Required | false |
| Valid values | integer |
| Environment | STORE_NEPTUNE_PORT |

Settings for the connection to the Amazon Cloud

***Property: store.neptune.aws.region***

The region where the neptune instance is located i.e. "eu-central-1" s. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

| Category | Value |
|--- | ---: |
| Default | eu-central-1 |
| Required | true |
| Valid values | One of the AWS regions |
| Environment | STORE_NEPTUNE_AWS_REGION |

***Property: store.neptune.aws.authEnabled***

Whether the neptune instance is configured with enabled IAM authentication. In case of enabled authentication the credentials need to be accessible to the JVM of the dataplatform. Deployment on EC2 and assigning a role to the VM is sufficient. Other ways to achieve this are described in https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html

| Category | Value |
|--- | ---: |
| Default | true |
| Required | true |
| Valid values | boolean |
| Environment | STORE_NEPTUNE_AWS_AUTHENABLED |

Settings for S3 bucket connection and upload of large files to the neptune instance. The neptune store blocks all HTTP requests with size >150MB. To upload larger files a graph file is temporarily stored in a S3 bucket and uploaded via Neptune Bulk Loader. The S3 bucket needs to be in the same region as the neptune cluster. For more information s. https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html. If no S3 upload is necessary then the limit of 150 MB on HTTPS uploads apply for neptune. The whole section can be left out of the configuration.

***Property: store.neptune.s3.bucketNameOrAPAlias***

The name of the bucket or access point -> the role CMEM runs under needs write access to the bucket

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_NEPTUNE_S3_BUCKETNAMEORAPALIAS |

***Property: store.neptune.s3.iamRoleArn***

The name of the role the neptune loader accesses the bucket -> the role needs read access to the bucket s. https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM.html

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_NEPTUNE_S3_IAMROLEARN |

***Property: store.neptune.s3.bulkLoadThresholdInMb***

The threshold on uncompressed graph data when bulk upload is applied with a maximum / default of 150 MB

| Category | Value |
|--- | ---: |
| Default | 150 |
| Required | false |
| Valid values | string |
| Environment | STORE_NEPTUNE_S3_BULKLOADTHRESHOLDINMB |

***Property: store.neptune.s3.bulkLoadParallelism***

The degree of parallelism (CPU) for the neptune loader, possible values are LOW, MEDIUM, HIGH, OVERSUBSCRIBE, default of HIGH

| Category | Value |
|--- | ---: |
| Default | HIGH |
| Required | false |
| Valid values | LOW, MEDIUM, HIGH, OVERSUBSCRIBE |
| Environment | STORE_NEPTUNE_S3_BULKLOADPARALLELISM |

