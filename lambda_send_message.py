import boto3
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = 'user-metadata'
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(dynamodbTableName)
cognito_idp = boto3.client('cognito-idp')

def handler(event, context):
    try:
        logger.info("Event: " + json.dumps(event))
        logger.info("Context: " + str(context))
        logger.info("DynamoDB Table Name: " + dynamodbTableName)
        logger.info("DynamoDB Table: " + str(table))
        logger.info("Response: " + json.dumps(response))

        user_name = event['request']['usernameParameter']
        response = cognito_idp.admin_get_user(
            UserPoolId=event['userPoolId'],
            Username=user_name
        )

        print(response)

        return event
    except Exception as e:
        return str(e)   

event_demo = {
    'version': '$LATEST', 
    'triggerSource': 'CustomMessage_SignUp', 
    'userName': 'haphanbaominh9674', 
    'region': 'ap-southeast-1', 
    'userPoolId': 'ap-southeast-1_78a14b94afc8443c9a8a2856091d6f86', 
    'callerContext': {'awsSdkVersion': 'aws-sdk-unknown-unknown', 'clientId': 'CLIENT_ID_NOT_APPLICABLE'}, 
    'request': {'validationData': {}, 'clientMetadata': {}, 'session': [], 'codeParameter': '749263', 'usernameParameter': 'haphanbaominh9674'}, 
    'response': {}
    }

handler(event_demo, None)

