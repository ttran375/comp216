import boto3
from datetime import datetime

dynamoDB = boto3.resource("dynamodb")
table = dynamoDB.Table("A732Table")


def lambda_handler(event, context):
    # TODO implement
    messages = event["Records"]
    print(messages)

    for message in messages:
        message_Data = {
            "mid": message["messageId"],
            "sns body": message["body"],
            "timestamp": datetime.now().isoformat(),
        }

        print(message_Data)

        table.put_item(
            Item={
                "id": message_Data["mid"],
                "notf body": message_Data["sns body"],
                "time": message_Data["timestamp"],
            }
        )
