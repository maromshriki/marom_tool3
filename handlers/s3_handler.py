import boto3
from config import DEFAULT_REGION

s3 = boto3.client("s3", region_name=DEFAULT_REGION)

def create_bucket(bucket_name: str, public: bool = False):
    params = {"Bucket": bucket_name}
    if DEFAULT_REGION != "us-east-1":
        params["CreateBucketConfiguration"] = {"LocationConstraint": DEFAULT_REGION}
    response = s3.create_bucket(**params)
    if public:
        s3.put_bucket_acl(Bucket=bucket_name, ACL="public-read")
    return response

def list_buckets():
    return s3.list_buckets()

def delete_bucket(bucket_name: str):
    return s3.delete_bucket(Bucket=bucket_name)

def upload_file(bucket_name: str, file_path: str, object_name: str = None):
    if object_name is None:
        object_name = file_path
    return s3.upload_file(file_path, bucket_name, object_name)

def delete_file(bucket_name: str, object_name: str):
    return s3.delete_object(Bucket=bucket_name, Key=object_name)
