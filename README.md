# S3 backup script
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

## Recommendations
### IAM
IAM role Lambda functions must have a policy allowing the function read access to the source bucket and write access to the destination bucket.

### Timeout
It is necessary to set a limit on the execution of the lambda function that is sufficient to authenticate the copy.



