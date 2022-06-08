import json


def handler(event: dict, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "test": "test"
        })
    }
