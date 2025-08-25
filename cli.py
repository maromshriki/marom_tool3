import argparse
from handlers import ec2_handler, s3_handler, route53_handler

def main():
    parser = argparse.ArgumentParser(prog="maromtool")
    subparsers = parser.add_subparsers(dest="resource")

    # EC2
    ec2_parser = subparsers.add_parser("ec2")
    ec2_sub = ec2_parser.add_subparsers(dest="action")
    create_ec2 = ec2_sub.add_parser("create")
    create_ec2.add_argument("--type", required=True)
    create_ec2.add_argument("--os", required=True)
    ec2_sub.add_parser("list")
    ec2_sub.add_parser("stop").add_argument("--id", required=True)
    ec2_sub.add_parser("start").add_argument("--id", required=True)
    ec2_sub.add_parser("terminate").add_argument("--id", required=True)

    # S3
    s3_parser = subparsers.add_parser("s3")
    s3_sub = s3_parser.add_subparsers(dest="action")
    create_s3 = s3_sub.add_parser("create")
    create_s3.add_argument("--name", required=True)
    create_s3.add_argument("--public", action="store_true")
    s3_sub.add_parser("list")
    s3_sub.add_parser("delete").add_argument("--name", required=True)
    upload_s3 = s3_sub.add_parser("upload")
    upload_s3.add_argument("--bucket", required=True)
    upload_s3.add_argument("--file", required=True)
    upload_s3.add_argument("--key", required=False)
    delete_file = s3_sub.add_parser("delete-file")
    delete_file.add_argument("--bucket", required=True)
    delete_file.add_argument("--key", required=True)

    # Route53
    r53_parser = subparsers.add_parser("route53")
    r53_sub = r53_parser.add_subparsers(dest="action")
    create_zone = r53_sub.add_parser("create-zone")
    create_zone.add_argument("--name", required=True)
    create_record = r53_sub.add_parser("create-record")
    create_record.add_argument("--zone-id", required=True)
    create_record.add_argument("--name", required=True)
    create_record.add_argument("--type", required=True)
    create_record.add_argument("--value", required=True)
    list_r53 = r53_sub.add_parser("list-records")
    list_r53.add_argument("--zone-id", required=True)
    delete_r53 = r53_sub.add_parser("delete-record")
    delete_r53.add_argument("--zone-id", required=True)
    delete_r53.add_argument("--name", required=True)
    delete_r53.add_argument("--type", required=True)
    delete_r53.add_argument("--value", required=True)

    args = parser.parse_args()
    if args.resource == "ec2":
        if args.action == "create":
            print(ec2_handler.create_instance(args.type, args.os))
        elif args.action == "list":
            print(ec2_handler.list_instances())
        elif args.action == "stop":
            print(ec2_handler.stop_instance(args.id))
        elif args.action == "start":
            print(ec2_handler.start_instance(args.id))
        elif args.action == "terminate":
            print(ec2_handler.terminate_instance(args.id))
    elif args.resource == "s3":
        if args.action == "create":
            print(s3_handler.create_bucket(args.name, args.public))
        elif args.action == "list":
            print(s3_handler.list_buckets())
        elif args.action == "delete":
            print(s3_handler.delete_bucket(args.name))
        elif args.action == "upload":
            print(s3_handler.upload_file(args.bucket, args.file, args.key))
        elif args.action == "delete-file":
            print(s3_handler.delete_file(args.bucket, args.key))
    elif args.resource == "route53":
        if args.action == "create-zone":
            print(route53_handler.create_zone(args.name))
        elif args.action == "create-record":
            print(route53_handler.create_record(args.zone_id, args.name, args.type, args.value))
        elif args.action == "list-records":
            print(route53_handler.list_records(args.zone_id))
        elif args.action == "delete-record":
            print(route53_handler.delete_record(args.zone_id, args.name, args.type, args.value))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
