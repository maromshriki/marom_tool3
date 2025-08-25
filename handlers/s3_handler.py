import boto3
import os

def create_bucket(bucket_name):
    try:
        region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
        print(f"==> Using region: {region}")
        s3 = boto3.client("s3", region_name=region)
        print(f"==> Using endpoint: {s3.meta.endpoint_url}")
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        return f"✅ Bucket נוצר בהצלחה: {bucket_name}"
    except Exception as e:
        return f"❌ שגיאה ביצירת bucket: {str(e)}"

def list_buckets():
    s3 = boto3.client("s3")
    resp = s3.list_buckets()
    return [b["Name"] for b in resp["Buckets"]]

def delete_bucket(bucket_name):
    s3 = boto3.client("s3")
    try:
        s3.delete_bucket(Bucket=bucket_name)
        return f"🗑️ Bucket נמחק בהצלחה: {bucket_name}"
    except Exception as e:
        return f"❌ שגיאה במחיקת bucket: {str(e)}"
