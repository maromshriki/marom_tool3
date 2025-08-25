import boto3
from config import DEFAULT_REGION

ec2 = boto3.client("ec2", region_name=DEFAULT_REGION)


def create_instance(instance_type: str, os: str):
    ami_map = {
        "ubuntu": "ami-080e1f13689e07408",
        "amazonlinux": "ami-0c02fb55956c7d316"
    }

    if os not in ami_map:
        raise ValueError(f"OS {os} not supported. Choose from: {', '.join(ami_map.keys())}")

    image_id = ami_map[os]

    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        NetworkInterfaces=[{
            "DeviceIndex": 0,
            "AssociatePublicIpAddress": True,
            "SubnetId": get_default_subnet()
        }],
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "CreatedBy", "Value": "marom_tool2"}]
        }]
    )

    instance_id = response["Instances"][0]["InstanceId"]
    return f" EC2 instance created InstanceId: {instance_id}"


def get_default_subnet():
    subnets = ec2.describe_subnets()["Subnets"]
    if not subnets:
        raise RuntimeError("No subnets found in region us-east-1")
    return subnets[0]["SubnetId"]


def describe_instances():
    reservations = ec2.describe_instances(
        Filters=[{"Name": "tag:CreatedBy", "Values": ["marom_tool2"]}]
    )["Reservations"]

    result = []
    for r in reservations:
        for inst in r["Instances"]:
            result.append({
                "InstanceId": inst["InstanceId"],
                "State": inst["State"]["Name"],
                "Type": inst["InstanceType"],
                "PublicIp": inst.get("PublicIpAddress", "N/A")
            })
    return result


def terminate_instance(instance_id: str):
    ec2.terminate_instances(InstanceIds=[instance_id])
    return f" EC2 instance {instance_id} shutting down"
