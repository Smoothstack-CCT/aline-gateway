# Set default stack name if no stack name is provided
service_name=gateway

aws cloudformation deploy --template setup-ms-stack.yml \
    --stack-name $service_name-stack \
    --parameter-overrides \
        AppEnv=dev \
        AppName=alinefinancial \
        ServiceName=$service_name \
    --capabilities CAPABILITY_NAMED_IAM