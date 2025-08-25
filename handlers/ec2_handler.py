import boto3

def create_instance(instance_type, os_type, key_name):
    ec2 = boto3.client("ec2")
    if os_type == "ubuntu":
        image_id = "ami-080e1f13689e07408"
    else:
        image_id = "ami-0c02fb55956c7d316"

    resp = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName=key_name,
        NetworkInterfaces=[
            {
                "AssociatePublicIpAddress": True,
                "DeviceIndex": 0,
                "SubnetId": "subnet-076fcc0127fea803a"
            }
        ],
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [{"Key": "CreatedBy", "Value": "marom_tool"}]
            }
        ]
    )
    instance_id = resp["Instances"][0]["InstanceId"]
    return f" EC2 Instance created {instance_id}"

def describe_instances():
    ec2 = boto3.client("ec2")
    resp = ec2.describe_instances(Filters=[{"Name": "tag:CreatedBy", "Values": ["marom_tool"]}])
    instances = []
    for reservation in resp["Reservations"]:
        for inst in reservation["Instances"]:
            instances.append({"InstanceId": inst["InstanceId"], "State": inst["State"]["Name"]})
    return instances

def terminate_instance(instance_id):
    ec2 = boto3.client("ec2")
    ec2.terminate_instances(InstanceIds=[instance_id])
    return f" EC2 Instance deleted {instance_id} "
