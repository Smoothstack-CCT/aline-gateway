FROM openjdk:11

ENV APP_SERVICE_HOST="host.docker.internal"

COPY target/aline-gateway-0.0.1-SNAPSHOT.jar aline-gateway-.0.0.1-SNAPSHOT.jar 

ENTRYPOINT [ "java", "-jar", "aline-gateway-.0.0.1-SNAPSHOT.jar" ]