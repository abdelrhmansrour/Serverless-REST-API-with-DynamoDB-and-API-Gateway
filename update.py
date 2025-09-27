import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Todos")

def lambda_handler(event, context):
    body = json.loads(event["body"])
    task_id = body["id"]

    response = table.update_item(
        Key={"id": task_id},
        UpdateExpression="set task = :t, #s = :s",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={
            ":t": body["task"],
            ":s": body["status"]
        },
        ReturnValues="UPDATED_NEW"
    )
    return {"statusCode": 200
    "headers": {
        "Access-Control-Allow-Origin": "*", 
        "Access-Control-Allow-Headers": "*",  
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE"
    }, "body": json.dumps(response["Attributes"])}


