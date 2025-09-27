import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Todos")

def lambda_handler(event, context):
    body = json.loads(event["body"])
    task_id = body["id"]

    table.delete_item(Key={"id": task_id})
    return {"statusCode": 200
    "headers": {
        "Access-Control-Allow-Origin": "*", 
        "Access-Control-Allow-Headers": "*",  
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE"
    }, "body": json.dumps({"message": "Deleted"})}

