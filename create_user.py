import boto3

client = boto3.client('cognito-idp', region_name='us-east-1')

try:
    response = client.sign_up(
        ClientId='ru2qbn52sppuy9i7l00lgibp2z',
        Username='haphanbaominh9672',
        Password='12345678Aa@',
        UserAttributes=[
            {
                'Name': 'email',
                'Value': 'haphanbaominh96@gmail.com'
            },
        ],
    )
    print(response)
except Exception as e:
    print(e)