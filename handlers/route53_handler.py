import boto3

def create_record(zone_id, name, record_type, value):
    r53 = boto3.client("route53")
    try:
        r53.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                "Changes": [
                    {
                        "Action": "CREATE",
                        "ResourceRecordSet": {
                            "Name": name,
                            "Type": record_type,
                            "TTL": 300,
                            "ResourceRecords": [{"Value": value}]
                        }
                    }
                ]
            }
        )
        return f" secsuuses: {name} -> {value}"
    except Exception as e:
        return f"error didnt work: {e}"
