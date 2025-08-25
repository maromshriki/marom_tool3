import boto3

def create_hosted_zone(domain_name):
    r53 = boto3.client("route53")
    resp = r53.create_hosted_zone(
        Name=domain_name,
        CallerReference=domain_name,
        HostedZoneConfig={"Comment": "Created by marom_tool", "PrivateZone": False}
    )
    return f"✅ Hosted Zone נוצר: {resp['HostedZone']['Id']}"

def delete_hosted_zone(zone_id):
    r53 = boto3.client("route53")
    r53.delete_hosted_zone(Id=zone_id)
    return f"🗑️ Hosted Zone נמחק: {zone_id}"

def list_zones():
    r53 = boto3.client("route53")
    resp = r53.list_hosted_zones()
    return [z["Name"] for z in resp["HostedZones"]]

def add_record(zone_id, name, rtype, value):
    r53 = boto3.client("route53")
    r53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            "Changes": [{
                "Action": "CREATE",
                "ResourceRecordSet": {
                    "Name": name,
                    "Type": rtype,
                    "TTL": 300,
                    "ResourceRecords": [{"Value": value}]
                }
            }]
        }
    )
    return f"✅ רשומה נוספה: {name} -> {value}"

def delete_record(zone_id, name, rtype, value):
    r53 = boto3.client("route53")
    r53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            "Changes": [{
                "Action": "DELETE",
                "ResourceRecordSet": {
                    "Name": name,
                    "Type": rtype,
                    "TTL": 300,
                    "ResourceRecords": [{"Value": value}]
                }
            }]
        }
    )
    return f"🗑️ רשומה נמחקה: {name}"
