import argparse
from handlers import ec2_handler, s3_handler, route53_handler

def main():
    parser = argparse.ArgumentParser(description="Marom AWS CLI Tool")
    subparsers = parser.add_subparsers(dest="service")

    # EC2
    ec2_parser = subparsers.add_parser("ec2", help="EC2 operations")
    ec2_subparsers = ec2_parser.add_subparsers(dest="action")

    ec2_create = ec2_subparsers.add_parser("create", help="Create EC2 instance")
    ec2_create.add_argument("--type", required=True, help="Instance type")
    ec2_create.add_argument("--os", required=True, help="OS type (ubuntu/amazon)")
    ec2_create.add_argument("--key", required=True, help="EC2 key pair name")

    ec2_subparsers.add_parser("describe", help="Describe EC2 instances")

    ec2_terminate = ec2_subparsers.add_parser("terminate", help="Terminate EC2 instance")
    ec2_terminate.add_argument("--id", required=True, help="Instance ID")

    # S3
    s3_parser = subparsers.add_parser("s3", help="S3 operations")
    s3_subparsers = s3_parser.add_subparsers(dest="action")

    s3_create = s3_subparsers.add_parser("create", help="Create S3 bucket")
    s3_create.add_argument("--name", required=True, help="Bucket name")

    s3_upload = s3_subparsers.add_parser("upload", help="Upload file to bucket")
    s3_upload.add_argument("--bucket", required=True, help="Bucket name")
    s3_upload.add_argument("--file", required=True, help="File path")

    # Route53
    r53_parser = subparsers.add_parser("route53", help="Route53 operations")
    r53_subparsers = r53_parser.add_subparsers(dest="action")

    r53_create = r53_subparsers.add_parser("create-record", help="Create DNS record")
    r53_create.add_argument("--zone-id", required=True, help="Hosted Zone ID")
    r53_create.add_argument("--name", required=True, help="Record name")
    r53_create.add_argument("--type", required=True, help="Record type (A, CNAME, etc.)")
    r53_create.add_argument("--value", required=True, help="Record value")

    args = parser.parse_args()

    if args.service == "ec2":
        if args.action == "create":
            print(ec2_handler.create_instance(args.type, args.os, args.key))
        elif args.action == "describe":
            print(ec2_handler.describe_instances())
        elif args.action == "terminate":
            print(ec2_handler.terminate_instance(args.id))

    elif args.service == "s3":
        if args.action == "create":
            print(s3_handler.create_bucket(args.name))
        elif args.action == "upload":
            print(s3_handler.upload_file(args.bucket, args.file))

    elif args.service == "route53":
        if args.action == "create-record":
            print(route53_handler.create_record(args.zone_id, args.name, args.type, args.value))

if __name__ == "__main__":
    main()
