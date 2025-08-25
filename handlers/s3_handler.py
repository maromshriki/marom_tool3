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
        return f"✅ Bucket נוצר בהצלחה: {bucket_name}"
    except Exception as e:
        return f"❌ שגיאה ביצירת bucket: {e}"

def upload_file(bucket_name, file_path):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket_name, os.path.basename(file_path))
        return f"📤 הקובץ {file_path} הועלה בהצלחה ל-{bucket_name}"
    except Exception as e:
        return f"❌ שגיאה בהעלאת קובץ: {e}"
