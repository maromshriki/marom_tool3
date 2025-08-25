import argparse
from handlers import ec2_handler, s3_handler, route53_handler


def main():
    parser = argparse.ArgumentParser(description="marom_tool CLI")
    subparsers = parser.add_subparsers(dest="resource")

    # EC2
    ec2_parser = subparsers.add_parser("ec2", help="Manage EC2 instances")
    ec2_subparsers = ec2_parser.add_subparsers(dest="action")

    ec2_create = ec2_subparsers.add_parser("create", help="Create EC2 instance")
    ec2_create.add_argument("--type", required=True, help="Instance type")
    ec2_create.add_argument("--os", required=True, help="OS type (ubuntu/amazonlinux)")

    ec2_subparsers.add_parser("describe", help="List EC2 instances created by this tool")

    ec2_terminate = ec2_subparsers.add_parser("terminate", help="Terminate EC2 instance")
    ec2_terminate.add_argument("--id", required=True, help="Instance ID to terminate")

    # S3
    s3_parser = subparsers.add_parser("s3", help="Manage S3 buckets")
    s3_subparsers = s3_parser.add_subparsers(dest="action")

    s3_create = s3_subparsers.add_parser("create", help="Create S3 bucket")
    s3_create.add_argument("--name", required=True, help="Bucket name")

    s3_subparsers.add_parser("list", help="List S3 buckets created by this tool")

    s3_delete = s3_subparsers.add_parser("delete", help="Delete S3 bucket")
    s3_delete.add_argument("--name", required=True, help="Bucket name")

    args = parser.parse_args()

    if args.resource == "ec2":
        if args.action == "create":
            print(ec2_handler.create_instance(args.type, args.os))
        elif args.action == "describe":
            instances = ec2_handler.describe_instances()
            if not instances:
                print("No EC2 instances found.")
            else:
                print("=== EC2 Instances ===")
                for inst in instances:
                    print(f"- {inst['InstanceId']} | {inst['Type']} | {inst['State']} | Public IP: {inst['PublicIp']}")
        elif args.action == "terminate":
            print(ec2_handler.terminate_instance(args.id))

    elif args.resource == "s3":
        if args.action == "create":
            print(s3_handler.create_bucket(args.name))
        elif args.action == "list":
            buckets = s3_handler.list_buckets()
            if not buckets:
                print("No S3 buckets found.")
            else:
                print("=== S3 Buckets ===")
                for b in buckets:
                    print(f"- {b}")
        elif args.action == "delete":
            print(s3_handler.delete_bucket(args.name))


if __name__ == "__main__":
    main()
