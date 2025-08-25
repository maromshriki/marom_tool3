import boto3

route53 = boto3.client("route53")


def create_record(hosted_zone_id: str, record_name: str, record_type: str, record_value: str):
    route53.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            "Changes": [{
                "Action": "CREATE",
                "ResourceRecordSet": {
                    "Name": record_name,
                    "Type": record_type,
                    "TTL": 300,
                    "ResourceRecords": [{"Value": record_value}]
                }
            }]
        }
    )
    return f"✅ Record {record_name} נוצר בהצלחה."


def delete_record(hosted_zone_id: str, record_name: str, record_type: str, record_value: str):
    route53.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            "Changes": [{
                "Action": "DELETE",
                "ResourceRecordSet": {
                    "Name": record_name,
                    "Type": record_type,
                    "TTL": 300,
                    "ResourceRecords": [{"Value": record_value}]
                }
            }]
        }
    )
    return f"🛑 Record {record_name} נמחק בהצלחה."
