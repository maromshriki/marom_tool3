import boto3
from config import DEFAULT_REGION

route53 = boto3.client("route53", region_name=DEFAULT_REGION)

def create_zone(name: str):
    return route53.create_hosted_zone(Name=name, CallerReference=str(hash(name)))

def create_record(zone_id: str, name: str, record_type: str, value: str):
    return route53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={"Changes": [{
            "Action": "UPSERT",
            "ResourceRecordSet": {
                "Name": name,
                "Type": record_type,
                "TTL": 300,
                "ResourceRecords": [{"Value": value}],
            },
        }]}
    )

def list_records(zone_id: str):
    return route53.list_resource_record_sets(HostedZoneId=zone_id)

def delete_record(zone_id: str, name: str, record_type: str, value: str):
    return route53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={"Changes": [{
            "Action": "DELETE",
            "ResourceRecordSet": {
                "Name": name,
                "Type": record_type,
                "TTL": 300,
                "ResourceRecords": [{"Value": value}],
            },
        }]}
    )
