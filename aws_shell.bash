# Run cloudformation stack
awslocal cloudformation create-stack --stack-name cognito-event --template-body file://cognito.yaml

# Check status of stack
awslocal cloudformation describe-stacks --stack-name cognito-event

# Delete stack
awslocal cloudformation delete-stack --stack-name cognito-event

# List all user pools clients
awslocal cognito-idp list-user-pool-clients --user-pool-id us-east-1_8dbe0dde635f4e78ba146648a1123575

# Add user to user pool name, phone_number, email, password
awslocal cognito-idp sign-up --client-id 1q2v3k4j5l6m7n8o9p0q1r2s3t4u5v6w --username testuser --password Testuser123 --user-attributes Name=email, 

# Describe user pool
awslocal cognito-idp describe-user-pool --user-pool-id us-east-1_8dbe0dde635f4e78ba146648a1123575

# List all cognito user pools
awslocal cognito-idp list-user-pools --max-results 10

# List all user pools clients
awslocal cognito-idp list-user-pool-clients --user-pool-id us-east-1_a66347492cdc4600998dee174e9d4e58

# Create user pool client
awslocal cognito-idp create-user-pool-client --user-pool-id us-east-1_4e917410c8964b34a102552d356ba702 --client-name test-client

awslocal cognito-idp sign-up  \
    --client-id d64pt3ukz32ebefh58x7xo0uo9 \
    --username user_28 \
    --password "12345678Aa@" \
    --user-attributes Name="phone",Value="0912782832" Name="email",Value="demo5@gmail.com"

awslocal cognito-idp describe-user-pool-client --user-pool-id us-east-1_2773875e3165426bb1a7914a80f4b560 --client-id mc7u7bc25emmcvry671w928qqb

# Get detail UserPool
awslocal cognito-idp describe-user-pool --user-pool-id us-east-1_2773875e3165426bb1a7914a80f4b560

# Get detail UserPoolClient based on username
awslocal cognito-idp admin-get-user --user-pool-id ap-southeast-1_78a14b94afc8443c9a8a2856091d6f86 --username haphanbaominh9674


awslocal lambda invoke --function-name cognito-event-post \
    --cli-binary-format raw-in-base64-out \
    --payload '{"body": "{\"num1\": \"10\", \"num2\": \"10\"}" }' output.txt