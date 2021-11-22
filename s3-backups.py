import boto3
from datetime import datetime, date


def lambda_handler(event, context):
    src_bucket = 'test-exclude'
    dst_bucket = 'repli-testing'
    backup_folder_name = 'backup_' + datetime.now().strftime("%H-%M-%S-") + date.today().strftime("-%d-%m-%Y")

    s3 = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    src_obj_list = s3.list_objects_v2(Bucket=str(src_bucket))

    for src_key in src_obj_list['Contents']:
        copy_source = {'Bucket': src_bucket, 'Key': src_key['Key']}

        dst_key = backup_folder_name + "/" + src_key['Key']
        s3_resource.meta.client.copy(copy_source, dst_bucket, dst_key)
        print(dst_key)

    # Backups rotation

    rotation_period_days = 2

    today_day = date.today().strftime("%d")
    today_month = date.today().strftime("%m")
    today_year = date.today().strftime("%Y")

    dst_obj_list = s3.list_objects_v2(Bucket=str(dst_bucket))
    unique_backup_name_list = set([old_backup_name['Key'].split("/")[0] for old_backup_name in dst_obj_list['Contents']])

    for backup in unique_backup_name_list:
        day = backup.split('--')[1].split('-')[0]
        month = backup.split('--')[1].split('-')[1]
        year = backup.split('--')[1].split('-')[2]

        backup_date = date(int(year), int(month), int(day))
        now_date = date(int(today_year), int(today_month), int(today_day))
        backup_age = now_date - backup_date
        if backup_age.days > rotation_period_days:
            tmp = "delete"
            s3_resource.Bucket(dst_bucket).objects.filter(Prefix=backup + "/").delete()
            print(f"{backup} {tmp}")
