# Run cloudformation stack
aws cloudformation create-stack --stack-name cognito-event --template-body file://cognito.yaml

# Check status of stack
aws cloudformation describe-stacks --stack-name cognito-event

# Delete stack
aws cloudformation delete-stack --stack-name cognito-event

sudo docker logs 5480550c9bd3
sudo docker logs 5480550c9bd3 2>&1 | grep "Cognito Event"