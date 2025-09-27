import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Todos")

def lambda_handler(event, context):
    params = event.get("queryStringParameters")
    if params and "id" in params:
        response = table.get_item(Key={"id": params["id"]})
        item = response.get("Item", {})
        return {"statusCode": 200, "body": json.dumps(item)}
    else:
        response = table.scan()
        return {"statusCode": 200
        "headers": {
        "Access-Control-Allow-Origin": "*", 
        "Access-Control-Allow-Headers": "*",  
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE"
        }, "body": json.dumps(response["Items"])}

