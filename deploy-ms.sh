# Set default stack name if no stack name is provided
service_name=gateway
service_port=8080
commit_hash=123

aws cloudformation deploy --template deploy-ms.yml \
    --stack-name $service_name-stack \
    --parameter-overrides \
        AppEnv=dev \
        AppName=alinefinancial \
        ServiceName=$service_name \
        ServicePort=$service_port
        CommitHash=$commit_hash
    --capabilities CAPABILITY_NAMED_IAM