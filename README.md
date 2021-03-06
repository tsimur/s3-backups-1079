# AWS S3 backup script for AWS Lambda
## Logic

The script copies data from the entire source bucket
```
src_bucket
```
to a folder named as
```
backup_folder_name
```
on the destination bucket.
```
dst_bucket
```
Backups older than the number of days specified in
```
rotation_period_days
```
will be deleted every time the script is executed

## Recommendations
### IAM
IAM role Lambda functions must have a policy allowing the function read access to the source bucket and write access to the destination bucket.

### Timeout
It is necessary to set the timeout for the lambda function to be sufficient to complete the copy.

```
lambda function -> configuration -> General configuration -> Edit Timeout
```

https://stackoverflow.com/questions/62948910/aws-lambda-errormessage-task-timed-out-after-3-00-seconds



