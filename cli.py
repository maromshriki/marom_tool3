#!/usr/bin/env python3
import argparse
from handlers import ec2_handler, s3_handler, route53_handler

def main():
    parser = argparse.ArgumentParser(description="Marom AWS CLI Tool")
    subparsers = parser.add_subparsers(dest="service")

    # EC2
    ec2_parser = subparsers.add_parser("ec2")
    ec2_sub = ec2_parser.add_subparsers(dest="action")
    ec2_create = ec2_sub.add_parser("create")
    ec2_create.add_argument("--type", required=True)
    ec2_create.add_argument("--os", required=True)
    ec2_sub.add_parser("describe")
    ec2_terminate = ec2_sub.add_parser("terminate")
    ec2_terminate.add_argument("--id", required=True)

    # S3
    s3_parser = subparsers.add_parser("s3")
    s3_sub = s3_parser.add_subparsers(dest="action")
    s3_create = s3_sub.add_parser("create")
    s3_create.add_argument("--name", required=True)
    s3_sub.add_parser("list")
    s3_delete = s3_sub.add_parser("delete")
    s3_delete.add_argument("--name", required=True)

    # Route53
    r53_parser = subparsers.add_parser("route53")
    r53_sub = r53_parser.add_subparsers(dest="action")
    r53_create = r53_sub.add_parser("create-zone")
    r53_create.add_argument("--name", required=True)
    r53_delete = r53_sub.add_parser("delete-zone")
    r53_delete.add_argument("--id", required=True)
    r53_sub.add_parser("list-zones")
    r53_add = r53_sub.add_parser("add-record")
    r53_add.add_argument("--zone-id", required=True)
    r53_add.add_argument("--name", required=True)
    r53_add.add_argument("--type", required=True)
    r53_add.add_argument("--value", required=True)
    r53_del = r53_sub.add_parser("delete-record")
    r53_del.add_argument("--zone-id", required=True)
    r53_del.add_argument("--name", required=True)
    r53_del.add_argument("--type", required=True)
    r53_del.add_argument("--value", required=True)

    args = parser.parse_args()

    if args.service == "ec2":
        if args.action == "create":
            print(ec2_handler.create_instance(args.type, args.os))
        elif args.action == "describe":
            print(ec2_handler.describe_instances())
        elif args.action == "terminate":
            print(ec2_handler.terminate_instance(args.id))

    elif args.service == "s3":
        if args.action == "create":
            print(s3_handler.create_bucket(args.name))
        elif args.action == "list":
            print(s3_handler.list_buckets())
        elif args.action == "delete":
            print(s3_handler.delete_bucket(args.name))

    elif args.service == "route53":
        if args.action == "create-zone":
            print(route53_handler.create_hosted_zone(args.name))
        elif args.action == "delete-zone":
            print(route53_handler.delete_hosted_zone(args.id))
        elif args.action == "list-zones":
            print(route53_handler.list_zones())
        elif args.action == "add-record":
            print(route53_handler.add_record(args.zone_id, args.name, args.type, args.value))
        elif args.action == "delete-record":
            print(route53_handler.delete_record(args.zone_id, args.name, args.type, args.value))

if __name__ == "__main__":
    main()
