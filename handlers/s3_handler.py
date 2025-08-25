import boto3
from config import DEFAULT_REGION

s3 = boto3.client("s3", region_name=DEFAULT_REGION)


def create_bucket(bucket_name: str):
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": DEFAULT_REGION}
    )
    return f" S3 bucket created {bucket_name} "


def list_buckets():
    buckets = s3.list_buckets()["Buckets"]
    result = [b["Name"] for b in buckets if b["Name"].startswith("marom-")]
    return result


def delete_bucket(bucket_name: str):
    s3.delete_bucket(Bucket=bucket_name)
    return f" S3 bucket {bucket_name} deleted."

def upload_file(bucket_name: str, file_path: str, object_name: str = None):
    
    import os
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        return f"file '{file_path}' uploaded '{bucket_name}' name '{object_name}'"
    except Exception as e:
        return f" {str(e)}"

