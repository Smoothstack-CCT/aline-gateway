# Set default stack name if no stack name is provided
service_name=gateway

aws cloudformation deploy --template setup-ms.yml \
    --stack-name $service_name-setup-stack \
    --parameter-overrides \
        AppEnv=dev \
        AppName=alinefinancial \
        ServiceName=$service_name \
    --capabilities CAPABILITY_NAMED_IAM