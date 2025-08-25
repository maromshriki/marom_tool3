import boto3
from config import DEFAULT_REGION

ec2 = boto3.client("ec2", region_name=DEFAULT_REGION)

def create_instance(instance_type: str, os: str):
    ami_map = {"ubuntu": "ami-123456", "amazonlinux": "ami-abcdef"}
    image_id = ami_map.get(os, "ami-123456")
    return ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{"ResourceType": "instance", "Tags": [{"Key": "CreatedBy", "Value": "marom_tool2"}]}]
    )

def list_instances():
    return ec2.describe_instances(Filters=[{"Name": "tag:CreatedBy", "Values": ["marom_tool2"]}])

def stop_instance(instance_id: str):
    return ec2.stop_instances(InstanceIds=[instance_id])

def start_instance(instance_id: str):
    return ec2.start_instances(InstanceIds=[instance_id])

def terminate_instance(instance_id: str):
    return ec2.terminate_instances(InstanceIds=[instance_id])
