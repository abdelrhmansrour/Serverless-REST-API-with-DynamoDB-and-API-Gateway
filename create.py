import boto3
import json
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Todos")

def lambda_handler(event, context):
    body = json.loads(event["body"])
    item = {
        "id": str(uuid.uuid4()),
        "task": body.get("task"),
        "status": body.get("status", "pending")
    }
    table.put_item(Item=item)
    return {
        "statusCode": 201
        "headers": {
        "Access-Control-Allow-Origin": "*", 
        "Access-Control-Allow-Headers": "*",  
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE"
    },
        "body": json.dumps(item)
    }

