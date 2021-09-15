service_name=''
app_name=''
app_env=''

print_usage() {
    echo 'Usage: 
    -service-name   Name of the service to set up
    -app-name       Name of the app
    -app-env        Environemt the stack is in (dev|staging|prod)
    '
}

while getopts "service-name:app-name:app-env:" flag; do
    case $flag in 
        service-name)   service_name=${OPTARG}  ;;
        app-name)       app_name=${OPTARG}      ;;
        app-env)        app-env=${OPTARG}       ;;
        *)              print_usage >&2
                        exit 1                 
    esac
done

if [ ! -d "$service_name"] && [ ! -d "$app_name" ] && [ ! -d "$app_env" ]; then
    aws cloudformation deploy --template setup-stack.yml \
        --stack-name $service_name-setup-stack \
        --parameter-overrides \
            AppEnv=$app_env \
            AppName=$app_name \
            ServiceName=$service_name \
        --capabilities CAPABILITY_NAMED_IAM
fi