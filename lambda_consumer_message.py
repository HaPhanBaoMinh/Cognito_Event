event_demo = {'Records': [{'body': '{"user_name": "user_28", "user_email": "demo5@gmail.com", "user_phone": "0912782832", "id": "f2wk3zcbbqb1ye0nmq4o11jg51"}', 'receiptHandle': 'ZDY4NWEzNzItNzMzNS00YTg5LThlMTMtNmI1ZDYxMTNiNzA3IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6Y29nbml0by1zcXMgMWM0N2NkZTMtMmMyMC00YTZhLWFiN2YtNDI3YWI1NjA3MTMwIDE3MTU0MDE1NTUuNTE5MTI5OA==', 'md5OfBody': 'e916846d7cde22ec9314f46938e95424', 'eventSourceARN': 'arn:aws:sqs:us-east-1:000000000000:cognito-sqs', 'eventSource': 'aws:sqs', 'awsRegion': 'us-east-1', 'messageId': '1c47cde3-2c20-4a6a-ab7f-427ab5607130', 'attributes': {'SenderId': '000000000000', 'SentTimestamp': '1715401555440', 'ApproximateReceiveCount': '1', 'ApproximateFirstReceiveTimestamp': '1715401555519'}, 'messageAttributes': {}}]}

import boto3
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

def handler(event, context):
    try:
        record = event['Records']
        for r in record:
            body = json.loads(r['body'])
            print(body)
            requestBody = {
                "id": {"S": body['id']},
                "user_name": {"S": body['user_name']},
                "user_email": {"S": body['user_email']},
                "user_phone": {"S": body['user_phone']}
            }
            dynamodb.put_item(
                TableName='user-metadata',
                Item=json.loads(json.dumps(requestBody))
            )
        return {
            "statusCode": 200,
            "message": "Success!"
        }
    except Exception as e:
        print(e)
        return str(e)

handler(event_demo, None)