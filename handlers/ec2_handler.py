import boto3

def create_instance(instance_type, os_name):
    ec2 = boto3.client("ec2")
    images = {
        "ubuntu": "ami-080e1f13689e07408",
        "amazon-linux": "ami-0c02fb55956c7d316"
    }
    image_id = images.get(os_name, images["ubuntu"])
    resp = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "CreatedBy", "Value": "marom_tool"}]
        }],
        NetworkInterfaces=[{
            "AssociatePublicIpAddress": True,
            "DeviceIndex": 0,
            "DeleteOnTermination": True
        }]
    )
    instance_id = resp["Instances"][0]["InstanceId"]
    return f"✅ EC2 Instance נוצר בהצלחה: {instance_id}"

def describe_instances():
    ec2 = boto3.client("ec2")
    resp = ec2.describe_instances()
    instances = []
    for res in resp["Reservations"]:
        for inst in res["Instances"]:
            instances.append({
                "id": inst["InstanceId"],
                "state": inst["State"]["Name"],
                "type": inst["InstanceType"]
            })
    return instances

def terminate_instance(instance_id):
    ec2 = boto3.client("ec2")
    ec2.terminate_instances(InstanceIds=[instance_id])
    return f"🗑️ EC2 Instance נמחק: {instance_id}"
