---
hide:
  - toc
---

| Property | Environment | Default | Required | Valid values|
| --- | --- | --- | --- | --- |
| store.type | STORE_TYPE  | neptune| true | NEPTUNE |
| store.neptune.host | STORE_NEPTUNE_HOST  | *none*| true | string |
| store.neptune.port | STORE_NEPTUNE_PORT  | 8182| false | integer |
| store.neptune.aws.region | STORE_NEPTUNE_AWS_REGION  | eu-central-1| true | One of the AWS regions |
| store.neptune.aws.authEnabled | STORE_NEPTUNE_AWS_AUTHENABLED  | true| true | boolean |
| store.neptune.s3.bucketNameOrAPAlias | STORE_NEPTUNE_S3_BUCKETNAMEORAPALIAS  | *none*| false | string |
| store.neptune.s3.iamRoleArn | STORE_NEPTUNE_S3_IAMROLEARN  | *none*| false | string |
| store.neptune.s3.bulkLoadThresholdInMb | STORE_NEPTUNE_S3_BULKLOADTHRESHOLDINMB  | 150| false | string |
| store.neptune.s3.bulkLoadParallelism | STORE_NEPTUNE_S3_BULKLOADPARALLELISM  | HIGH| false | LOW, MEDIUM, HIGH, OVERSUBSCRIBE |
