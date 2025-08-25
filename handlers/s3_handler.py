import boto3, os

def create_bucket(bucket_name):
    region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
    print(f"==> Using region: {region}")
    s3 = boto3.client("s3", region_name=region)
    print(f"==> Using endpoint: {s3.meta.endpoint_url}")

    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        return f"Bucket created: {bucket_name}"
    except Exception as e:
        return f"bucket: {e}"

def upload_file(bucket_name, file_path):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket_name, os.path.basename(file_path))
        return f" file{file_path} uploaded to {bucket_name}"
    except Exception as e:
        return f" {e}"
def delete_bucket(bucket_name):
    s3 = boto3.client("s3")
    try:
        s3.delete_bucket(Bucket=bucket_name)
        return f" Bucket deleted: {bucket_name}"
    except ClientError as e:
        return f"couldnent delete bucket: {e}"
